import pytest
from pydantic import ValidationError

from app.core.config import Settings


def test_production_rejects_sqlite():
    with pytest.raises(ValidationError):
        Settings(app_env="production", database_url="sqlite:///./local.db")


def test_production_requires_oidc():
    with pytest.raises(ValidationError):
        Settings(
            app_env="production",
            database_url="postgresql+psycopg://northstar:secret@localhost/northstar",
        )
