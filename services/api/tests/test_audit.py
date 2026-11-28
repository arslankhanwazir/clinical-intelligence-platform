import pytest
from sqlalchemy import select, update, delete
from sqlalchemy.exc import DBAPIError

from app.core.security import get_current_principal
from app.db.audit import append_audit_event, verify_audit_chain
from app.db.models import AuditEvent
from app.main import app
from conftest import admin_session, principal_for, set_tenant_context, tenant_scoped_session


def test_identity_access_creates_verifiable_audit_event(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id)
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 200
    db = tenant_scoped_session(tenant_id)
    try:
        events = db.scalars(
            select(AuditEvent)
            .where(AuditEvent.tenant_id == tenant_id)
            .order_by(AuditEvent.occurred_at, AuditEvent.id)
        ).all()
        assert len(events) == 1
        assert events[0].action == "security.identity.read"
        assert len(events[0].event_hash) == 64
        assert len(events[0].previous_hash) == 64
        assert verify_audit_chain(events) is True
    finally:
        db.close()


def test_audit_rows_cannot_be_updated_or_deleted(client, tenant_id):
    app.dependency_overrides[get_current_principal] = lambda: principal_for(tenant_id)
    response = client.get("/api/v1/security/me", headers={"X-Tenant-ID": tenant_id})
    assert response.status_code == 200
    # Use the test-only owner connection so the PostgreSQL trigger, not merely app-role grants/RLS, is exercised.
    db = admin_session()
    try:
        event = db.scalar(select(AuditEvent).where(AuditEvent.tenant_id == tenant_id))
        assert event is not None
        with pytest.raises(DBAPIError):
            db.execute(update(AuditEvent).where(AuditEvent.id == event.id).values(outcome="changed"))
            db.commit()
        db.rollback()
        with pytest.raises(DBAPIError):
            db.execute(delete(AuditEvent).where(AuditEvent.id == event.id))
            db.commit()
        db.rollback()
    finally:
        db.close()


def test_hash_chain_detects_in_memory_tampering(client, tenant_id):
    db = tenant_scoped_session(tenant_id)
    try:
        for action in ("test.one", "test.two"):
            set_tenant_context(db, tenant_id)
            append_audit_event(
                db,
                tenant_id=tenant_id,
                actor_sub="test-user",
                action=action,
                resource_type="test",
                resource_id=None,
                outcome="success",
                correlation_id="test-correlation",
            )
            db.commit()
        set_tenant_context(db, tenant_id)
        events = db.scalars(
            select(AuditEvent)
            .where(AuditEvent.tenant_id == tenant_id)
            .order_by(AuditEvent.occurred_at, AuditEvent.id)
        ).all()
        assert verify_audit_chain(events) is True
        events[0].action = "tampered.action"
        assert verify_audit_chain(events) is False
    finally:
        db.rollback()
        db.close()
