"""Add shared API rate-limit buckets for M4.

Revision ID: 0002_m4_rate_limits
Revises: 0001_secure_foundation
"""
from alembic import op
import sqlalchemy as sa

revision = "0002_m4_rate_limits"
down_revision = "0001_secure_foundation"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "api_rate_limit_buckets",
        sa.Column("key_hash", sa.String(length=64), nullable=False),
        sa.Column("window_start", sa.BigInteger(), nullable=False),
        sa.Column("request_count", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("key_hash", "window_start", name="pk_api_rate_limit_buckets"),
    )


def downgrade() -> None:
    op.drop_table("api_rate_limit_buckets")
