from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.core.identity import Principal
from app.core.security import get_current_principal
from app.db.models import Tenant
from app.db.session import SessionLocal
from app.main import app


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
    db = SessionLocal()
    try:
        db.add(Tenant(id=value, name="Synthetic Test Tenant", status="active"))
        db.commit()
    finally:
        db.close()
    return value


def principal_for(tenant_id: str, roles: set[str] | None = None, acr: str | None = "2"):
    return Principal(
        subject="test-user-001",
        roles=frozenset(roles or {"clinician"}),
        tenant_ids=frozenset({tenant_id}),
        site_ids=frozenset(),
        acr=acr,
    )
