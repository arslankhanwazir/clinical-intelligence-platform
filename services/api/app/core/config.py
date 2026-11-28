from functools import lru_cache
from pathlib import Path
from typing import Literal

from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


PROJECT_ROOT = Path(__file__).resolve().parents[4]


def _resolve_database_url(value):
    raw = value.get_secret_value() if isinstance(value, SecretStr) else value
    if not isinstance(raw, str) or not raw.startswith("sqlite:///"):
        return value

    raw_path = raw[len("sqlite:///") :]
    if raw_path in {":memory:", ""} or raw_path.startswith("file:"):
        return value

    path = Path(raw_path)
    if not path.is_absolute():
        path = (PROJECT_ROOT / path).resolve()
    return "sqlite:///" + path.as_posix()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        validate_default=True,
    )

    app_name: str = "NORTHSTAR Secure API"
    app_env: Literal["development", "test", "staging", "production"] = "development"
    database_url: SecretStr = SecretStr("sqlite:///./data/northstar_dev.sqlite3")

    oidc_issuer: str | None = None
    oidc_jwks_url: str | None = None
    oidc_audience: str | None = None
    oidc_client_id: str = "northstar-api"
    oidc_privileged_acr_values: list[str] = Field(default_factory=lambda: ["2"])
    oidc_jwks_timeout_seconds: int = Field(default=5, ge=1, le=20)
    jwt_leeway_seconds: int = Field(default=30, ge=0, le=120)

    api_rate_limit_requests_per_minute: int = Field(default=120, ge=1, le=10000)
    api_rate_limit_window_seconds: int = Field(default=60, ge=1, le=3600)

    @field_validator("database_url", mode="before")
    @classmethod
    def stable_sqlite_location(cls, value):
        return _resolve_database_url(value)

    @field_validator("oidc_privileged_acr_values", mode="before")
    @classmethod
    def parse_acr_values(cls, value):
        if isinstance(value, str):
            return [part.strip() for part in value.split(",") if part.strip()]
        return value

    @model_validator(mode="after")
    def production_configuration_must_be_explicit(self):
        if self.app_env == "production":
            db_url = self.database_url.get_secret_value()
            if not db_url.startswith("postgresql+psycopg://"):
                raise ValueError("Production requires PostgreSQL via postgresql+psycopg://")
            if not all((self.oidc_issuer, self.oidc_jwks_url, self.oidc_audience)):
                raise ValueError("Production requires OIDC issuer, JWKS URL and audience")
            if "oidc_privileged_acr_values" not in self.model_fields_set:
                raise ValueError("Production requires an explicitly verified privileged MFA ACR allow-list")
            if not self.oidc_privileged_acr_values or any(
                value.upper().startswith("REPLACE_") for value in self.oidc_privileged_acr_values
            ):
                raise ValueError("Production requires the actual ACR value(s) verified with the identity provider")
        return self


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
