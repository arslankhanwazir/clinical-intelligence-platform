from pathlib import Path

import pytest
from pydantic import ValidationError

from app.core.config import PROJECT_ROOT, Settings


def test_production_rejects_sqlite():
    with pytest.raises(ValidationError):
        Settings(_env_file=None, app_env="production", database_url="sqlite:///./local.db")


def test_production_requires_oidc():
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            app_env="production",
            database_url="postgresql+psycopg://northstar:secret@localhost/northstar",
        )


def test_production_requires_explicit_mfa_acr_allowlist():
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            app_env="production",
            database_url="postgresql+psycopg://northstar:secret@localhost/northstar",
            oidc_issuer="https://id.example.test/realms/northstar",
            oidc_jwks_url="https://id.example.test/realms/northstar/protocol/openid-connect/certs",
            oidc_audience="northstar-api",
        )


def test_production_rejects_placeholder_mfa_acr_allowlist():
    with pytest.raises(ValidationError):
        Settings(
            _env_file=None,
            app_env="production",
            database_url="postgresql+psycopg://northstar:secret@localhost/northstar",
            oidc_issuer="https://id.example.test/realms/northstar",
            oidc_jwks_url="https://id.example.test/realms/northstar/protocol/openid-connect/certs",
            oidc_audience="northstar-api",
            oidc_privileged_acr_values=["REPLACE_WITH_VERIFIED_KEYCLOAK_ACR"],
        )


def test_relative_sqlite_database_url_is_resolved_from_repository_root():
    settings = Settings(_env_file=None, database_url="sqlite:///./data/path-check.sqlite3")
    expected = (PROJECT_ROOT / "data" / "path-check.sqlite3").resolve().as_posix()
    assert settings.database_url.get_secret_value() == "sqlite:///" + expected
