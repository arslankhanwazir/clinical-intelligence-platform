import os
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from app.core.identity import Principal
from app.core.security import get_current_principal
from app.db.models import Site, Tenant, UserMembership
from app.db.session import SessionLocal
from app.main import app

_ADMIN_URL = os.getenv("NORTHSTAR_TEST_ADMIN_DATABASE_URL")
_ADMIN_ENGINE = create_engine(_ADMIN_URL, pool_pre_ping=True) if _ADMIN_URL else None
_ADMIN_SESSION = sessionmaker(bind=_ADMIN_ENGINE, autoflush=False, expire_on_commit=False) if _ADMIN_ENGINE else None


def admin_session():
    """Use a test-only database owner for fixture setup and database-trigger checks."""
    return _ADMIN_SESSION() if _ADMIN_SESSION else SessionLocal()


def tenant_scoped_session(tenant_id: str):
    db = SessionLocal()
    if db.get_bind().dialect.name == "postgresql":
        db.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {"tenant_id": tenant_id},
        )
    return db


def set_tenant_context(db, tenant_id: str) -> None:
    if db.get_bind().dialect.name == "postgresql":
        db.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {"tenant_id": tenant_id},
        )


@pytest.fixture
def client():
    def override_principal():
        return Principal(
            subject="test-user-001",
            roles=frozenset({"clinician"}),
            tenant_ids=frozenset(),
            site_ids=frozenset(),
            acr="2",
        )

    app.dependency_overrides[get_current_principal] = override_principal
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture
def tenant_id():
    value = str(uuid4())
    db = admin_session()
    try:
        db.add(Tenant(id=value, name="Synthetic Test Tenant", status="active"))
        db.add(
            UserMembership(
                id=str(uuid4()),
                tenant_id=value,
                site_id=None,
                subject="test-user-001",
                role="clinician",
                status="active",
            )
        )
        db.commit()
    finally:
        db.close()
    return value


@pytest.fixture
def other_tenant_id():
    value = str(uuid4())
    db = admin_session()
    try:
        db.add(Tenant(id=value, name="Second Synthetic Tenant", status="active"))
        db.commit()
    finally:
        db.close()
    return value


def principal_for(
    tenant_id: str,
    roles: set[str] | None = None,
    acr: str | None = "2",
    site_ids: set[str] | None = None,
):
    return Principal(
        subject="test-user-001",
        roles=frozenset(roles or {"clinician"}),
        tenant_ids=frozenset({tenant_id}),
        site_ids=frozenset(site_ids or set()),
        acr=acr,
    )
