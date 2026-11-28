from datetime import datetime, timedelta, timezone

import jwt
import pytest
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi import HTTPException

import app.core.security as security
from app.core.config import Settings


class FakeSigningKey:
    def __init__(self, key):
        self.key = key


class FakeJwksClient:
    def __init__(self, key):
        self.key = key

    def get_signing_key_from_jwt(self, _token):
        return FakeSigningKey(self.key.public_key())


@pytest.fixture
def signing_material(monkeypatch):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    monkeypatch.setattr(security, "_jwks_client", lambda *_args: FakeJwksClient(private_key))
    return private_key


def make_token(private_key, *, issuer="https://id.example.test/realms/northstar", audience="northstar-api"):
    now = datetime.now(timezone.utc)
    return jwt.encode({
        "iss": issuer, "aud": audience, "sub": "synthetic-user",
        "iat": now, "exp": now + timedelta(minutes=5),
        "tenant_id": "f2f1d28f-6e4f-4ed6-bac7-5551f7d7b9f1",
        "realm_access": {"roles": ["clinician"]}, "acr": "2",
    }, private_key, algorithm="RS256")


def test_rs256_token_verifies_issuer_audience_and_claims(signing_material):
    settings = Settings(oidc_issuer="https://id.example.test/realms/northstar", oidc_jwks_url="https://id.example.test/realms/northstar/protocol/openid-connect/certs", oidc_audience="northstar-api")
    principal = security.verify_access_token(make_token(signing_material), settings)
    assert principal.subject == "synthetic-user"
    assert "clinician" in principal.roles


def test_wrong_audience_is_rejected(signing_material):
    settings = Settings(oidc_issuer="https://id.example.test/realms/northstar", oidc_jwks_url="https://id.example.test/realms/northstar/protocol/openid-connect/certs", oidc_audience="different-api")
    with pytest.raises(HTTPException) as exc:
        security.verify_access_token(make_token(signing_material), settings)
    assert exc.value.status_code == 401
