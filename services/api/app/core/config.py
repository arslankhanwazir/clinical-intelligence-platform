from functools import lru_cache
from typing import Literal

from pydantic import Field, SecretStr, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
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
            if not self.oidc_privileged_acr_values:
                raise ValueError("Production requires an explicit privileged MFA ACR allow-list")
        return self


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
