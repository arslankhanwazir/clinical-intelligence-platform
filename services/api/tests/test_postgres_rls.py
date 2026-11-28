import pytest
from sqlalchemy import select, text

from app.db.models import Tenant
from app.db.session import SessionLocal, engine
from conftest import tenant_scoped_session


@pytest.mark.skipif(engine.dialect.name != "postgresql", reason="PostgreSQL RLS integration test")
def test_application_database_role_is_not_superuser_or_bypassrls():
    db = SessionLocal()
    try:
        is_superuser, bypass_rls = db.execute(
            text(
                "SELECT rolsuper, rolbypassrls FROM pg_roles "
                "WHERE rolname = current_user"
            )
        ).one()
        assert is_superuser is False
        assert bypass_rls is False
    finally:
        db.close()


@pytest.mark.skipif(engine.dialect.name != "postgresql", reason="PostgreSQL privilege integration test")
def test_application_role_has_no_audit_update_or_delete_privilege():
    db = SessionLocal()
    try:
        can_update, can_delete = db.execute(
            text(
                "SELECT has_table_privilege(current_user, 'audit_events', 'UPDATE'), "
                "has_table_privilege(current_user, 'audit_events', 'DELETE')"
            )
        ).one()
        assert can_update is False
        assert can_delete is False
    finally:
        db.close()


@pytest.mark.skipif(engine.dialect.name != "postgresql", reason="PostgreSQL RLS integration test")
def test_postgres_rls_hides_rows_from_other_tenants(tenant_id, other_tenant_id):
    db = tenant_scoped_session(tenant_id)
    try:
        visible_ids = set(db.scalars(select(Tenant.id)).all())
        assert visible_ids == {tenant_id}
        hidden = db.scalar(select(Tenant.id).where(Tenant.id == other_tenant_id))
        assert hidden is None
    finally:
        db.close()
