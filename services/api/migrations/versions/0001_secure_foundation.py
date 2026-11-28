"""M4 secure foundation: tenant boundaries, memberships and audit ledger.

Revision ID: 0001_secure_foundation
Revises:
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_secure_foundation"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tenants",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_table(
        "sites",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=36), sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_sites_tenant_id", "sites", ["tenant_id"])

    op.create_table(
        "user_memberships",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=36), sa.ForeignKey("tenants.id", ondelete="CASCADE"), nullable=False),
        sa.Column("site_id", sa.String(length=36), sa.ForeignKey("sites.id", ondelete="CASCADE"), nullable=True),
        sa.Column("subject", sa.String(length=255), nullable=False),
        sa.Column("role", sa.String(length=60), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False, server_default="active"),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()),
    )
    op.create_index("ix_memberships_tenant_subject", "user_memberships", ["tenant_id", "subject"])
    op.create_index("ix_memberships_site_id", "user_memberships", ["site_id"])

    op.create_table(
        "audit_events",
        sa.Column("id", sa.String(length=36), primary_key=True),
        sa.Column("tenant_id", sa.String(length=36), sa.ForeignKey("tenants.id", ondelete="RESTRICT"), nullable=False),
        sa.Column("actor_sub", sa.String(length=255), nullable=False),
        sa.Column("action", sa.String(length=120), nullable=False),
        sa.Column("resource_type", sa.String(length=80), nullable=False),
        sa.Column("resource_id", sa.String(length=255), nullable=True),
        sa.Column("outcome", sa.String(length=30), nullable=False),
        sa.Column("correlation_id", sa.String(length=80), nullable=False),
        sa.Column("occurred_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("previous_hash", sa.String(length=64), nullable=False),
        sa.Column("event_hash", sa.String(length=64), nullable=False, unique=True),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
    )
    op.create_index("ix_audit_tenant_time", "audit_events", ["tenant_id", "occurred_at"])
    op.create_index("ix_audit_actor_time", "audit_events", ["tenant_id", "actor_sub", "occurred_at"])

    bind = op.get_bind()
    if bind.dialect.name == "sqlite":
        op.execute("""
            CREATE TRIGGER audit_events_no_update
            BEFORE UPDATE ON audit_events
            BEGIN SELECT RAISE(ABORT, 'audit_events are append-only'); END;
        """)
        op.execute("""
            CREATE TRIGGER audit_events_no_delete
            BEFORE DELETE ON audit_events
            BEGIN SELECT RAISE(ABORT, 'audit_events are append-only'); END;
        """)
    elif bind.dialect.name == "postgresql":
        for table, expression in [
            ("tenants", "id = current_setting('app.tenant_id', true)"),
            ("sites", "tenant_id = current_setting('app.tenant_id', true)"),
            ("user_memberships", "tenant_id = current_setting('app.tenant_id', true)"),
            ("audit_events", "tenant_id = current_setting('app.tenant_id', true)"),
        ]:
            op.execute(f"ALTER TABLE {table} ENABLE ROW LEVEL SECURITY")
            op.execute(f"ALTER TABLE {table} FORCE ROW LEVEL SECURITY")
            op.execute(
                f"CREATE POLICY tenant_isolation ON {table} "
                f"USING ({expression}) WITH CHECK ({expression})"
            )
        op.execute("""
            CREATE FUNCTION northstar_prevent_audit_mutation() RETURNS trigger AS $$
            BEGIN RAISE EXCEPTION 'audit_events are append-only'; END;
            $$ LANGUAGE plpgsql;
        """)
        op.execute("""
            CREATE TRIGGER audit_events_no_update_delete
            BEFORE UPDATE OR DELETE ON audit_events
            FOR EACH ROW EXECUTE FUNCTION northstar_prevent_audit_mutation();
        """)


def downgrade() -> None:
    bind = op.get_bind()
    if bind.dialect.name == "sqlite":
        op.execute("DROP TRIGGER IF EXISTS audit_events_no_update")
        op.execute("DROP TRIGGER IF EXISTS audit_events_no_delete")
    elif bind.dialect.name == "postgresql":
        op.execute("DROP TRIGGER IF EXISTS audit_events_no_update_delete ON audit_events")
        op.execute("DROP FUNCTION IF EXISTS northstar_prevent_audit_mutation()")
        for table in ("audit_events", "user_memberships", "sites", "tenants"):
            op.execute(f"DROP POLICY IF EXISTS tenant_isolation ON {table}")
            op.execute(f"ALTER TABLE {table} NO FORCE ROW LEVEL SECURITY")
            op.execute(f"ALTER TABLE {table} DISABLE ROW LEVEL SECURITY")
    op.drop_index("ix_audit_actor_time", table_name="audit_events")
    op.drop_index("ix_audit_tenant_time", table_name="audit_events")
    op.drop_table("audit_events")
    op.drop_index("ix_memberships_site_id", table_name="user_memberships")
    op.drop_index("ix_memberships_tenant_subject", table_name="user_memberships")
    op.drop_table("user_memberships")
    op.drop_index("ix_sites_tenant_id", table_name="sites")
    op.drop_table("sites")
    op.drop_table("tenants")
