from datetime import datetime, timedelta, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
from threading import Thread

import jwt
import pytest
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi import HTTPException
from jwt import PyJWKClient
from jwt.algorithms import RSAAlgorithm

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


def make_token(private_key, *, issuer="https://id.example.test/realms/northstar", audience="northstar-api", kid="test-key"):
    now = datetime.now(timezone.utc)
    return jwt.encode(
        {
            "iss": issuer,
            "aud": audience,
            "sub": "synthetic-user",
            "iat": now,
            "exp": now + timedelta(minutes=5),
            "tenant_id": "f2f1d28f-6e4f-4ed6-bac7-5551f7d7b9f1",
            "realm_access": {"roles": ["clinician"]},
            "acr": "2",
        },
        private_key,
        algorithm="RS256",
        headers={"kid": kid},
    )


def test_rs256_token_verifies_issuer_audience_and_claims(signing_material):
    settings = Settings(
        oidc_issuer="https://id.example.test/realms/northstar",
        oidc_jwks_url="https://id.example.test/realms/northstar/protocol/openid-connect/certs",
        oidc_audience="northstar-api",
    )
    principal = security.verify_access_token(make_token(signing_material), settings)
    assert principal.subject == "synthetic-user"
    assert "clinician" in principal.roles


def test_wrong_audience_is_rejected(signing_material):
    settings = Settings(
        oidc_issuer="https://id.example.test/realms/northstar",
        oidc_jwks_url="https://id.example.test/realms/northstar/protocol/openid-connect/certs",
        oidc_audience="different-api",
    )
    with pytest.raises(HTTPException) as exc:
        security.verify_access_token(make_token(signing_material), settings)
    assert exc.value.status_code == 401


def test_jwks_is_retrieved_over_http_and_used_to_verify_token(monkeypatch):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_jwk = RSAAlgorithm.to_jwk(private_key.public_key(), as_dict=True)
    public_jwk.update({"kid": "northstar-http-jwks-test", "use": "sig", "alg": "RS256"})
    document = json.dumps({"keys": [public_jwk]}).encode("utf-8")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(document)))
            self.end_headers()
            self.wfile.write(document)

        def log_message(self, _format, *_args):
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        jwks_url = f"http://127.0.0.1:{server.server_port}/jwks"
        monkeypatch.setattr(
            security,
            "_jwks_client",
            lambda url, timeout: PyJWKClient(url, cache_jwk_set=False, timeout=timeout),
        )
        settings = Settings(
            oidc_issuer="https://id.example.test/realms/northstar",
            oidc_jwks_url=jwks_url,
            oidc_audience="northstar-api",
        )
        token = make_token(private_key, kid="northstar-http-jwks-test")
        principal = security.verify_access_token(token, settings)
        assert principal.subject == "synthetic-user"
        assert "clinician" in principal.roles
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
