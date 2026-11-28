from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.authorization import TenantContext, get_tenant_context, require_roles
from app.core.identity import Principal
from app.db.dependencies import get_tenant_db_session
from app.db.models import AuditEvent

router = APIRouter(prefix="/api/v1/audit", tags=["audit"])


@router.get("/events")
def list_audit_events(
    tenant: TenantContext = Depends(get_tenant_context),
    _principal: Principal = Depends(require_roles("security_auditor", "tenant_admin")),
    db: Session = Depends(get_tenant_db_session),
    limit: int = Query(default=50, ge=1, le=200),
):
    rows = db.scalars(
        select(AuditEvent)
        .where(AuditEvent.tenant_id == tenant.tenant_id)
        .order_by(AuditEvent.occurred_at.desc(), AuditEvent.id.desc())
        .limit(limit)
    ).all()
    return {
        "items": [
            {
                "id": row.id,
                "occurred_at": row.occurred_at.isoformat(),
                "actor_sub": row.actor_sub,
                "action": row.action,
                "resource_type": row.resource_type,
                "resource_id": row.resource_id,
                "outcome": row.outcome,
                "correlation_id": row.correlation_id,
                "previous_hash": row.previous_hash,
                "event_hash": row.event_hash,
            }
            for row in rows
        ]
    }
