from uuid import uuid4

from app.core.identity import Principal
from app.core.security import get_current_principal
from app.db.models import Site, UserMembership
from app.main import app
from conftest import admin_session, principal_for


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
    db = admin_session()
    try:
        db.add(
            UserMembership(
                id=str(uuid4()),
                tenant_id=tenant_id,
                site_id=None,
                subject="test-user-001",
                role="tenant_admin",
                status="active",
            )
        )
        db.commit()
    finally:
        db.close()

    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id, {"tenant_admin"}, acr="1")
    response = client.get("/api/v1/audit/events", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403
    assert "MFA" in response.json()["detail"]


def test_privileged_role_requires_mfa_on_all_protected_tenant_routes(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id, {"clinician"}, acr="1")
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403
    assert "MFA" in response.json()["detail"]


def test_audit_endpoint_denies_non_auditor(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id, {"clinician"})
    response = client.get("/api/v1/audit/events", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403


def test_token_role_without_active_database_membership_is_denied(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id, {"security_auditor"})
    response = client.get("/api/v1/audit/events", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403
    assert "membership" in response.json()["detail"].lower()


def test_inactive_membership_is_denied(client, tenant_id):
    db = admin_session()
    try:
        membership = db.query(UserMembership).filter_by(
            tenant_id=tenant_id, subject="test-user-001", role="clinician"
        ).one()
        membership.status = "suspended"
        db.commit()
    finally:
        db.close()

    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id)
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 403


def test_site_must_belong_to_selected_tenant(client, tenant_id, other_tenant_id):
    site_id = str(uuid4())
    db = admin_session()
    try:
        db.add(Site(id=site_id, tenant_id=other_tenant_id, name="Other tenant site", status="active"))
        db.add(
            UserMembership(
                id=str(uuid4()),
                tenant_id=other_tenant_id,
                site_id=site_id,
                subject="test-user-001",
                role="clinician",
                status="active",
            )
        )
        db.commit()
    finally:
        db.close()

    app.dependency_overrides[get_current_principal] = lambda: principal_for(
        tenant_id, site_ids={site_id}
    )
    response = client.get(
        "/api/v1/security/me",
        headers={"X-Tenant-ID": tenant_id, "X-Site-ID": site_id},
    )
    assert response.status_code == 403
    assert "site" in response.json()["detail"].lower()


def test_site_scoped_membership_requires_site_header(client, tenant_id):
    site_id = str(uuid4())
    db = admin_session()
    try:
        db.add(Site(id=site_id, tenant_id=tenant_id, name="Assigned site", status="active"))
        membership = db.query(UserMembership).filter_by(
            tenant_id=tenant_id, subject="test-user-001", role="clinician"
        ).one()
        membership.site_id = site_id
        db.commit()
    finally:
        db.close()

    app.dependency_overrides[get_current_principal] = lambda: principal_for(
        tenant_id, site_ids={site_id}
    )
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 400
    assert "X-Site-ID" in response.json()["detail"]
