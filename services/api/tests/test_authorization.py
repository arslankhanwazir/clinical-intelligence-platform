from uuid import uuid4

from app.core.security import get_current_principal
from app.main import app
from conftest import principal_for


def test_authenticated_identity_requires_tenant_scope(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id)
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 200
    assert response.json()["tenant_id"] == tenant_id


def test_cross_tenant_access_is_denied(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id)
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": str(uuid4())})
    assert response.status_code == 403


def test_privileged_role_requires_mfa_assurance(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id, {"tenant_admin"}, acr="1")
    response = client.get("/api/v1/audit/events", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403
    assert "MFA" in response.json()["detail"]


def test_audit_endpoint_denies_non_auditor(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id, {"clinician"})
    response = client.get("/api/v1/audit/events", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403
