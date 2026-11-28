from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session

from app.core.authorization import TenantContext, get_tenant_context
from app.core.identity import Principal
from app.core.security import get_current_principal
from app.db.audit import append_audit_event
from app.db.dependencies import get_tenant_db_session

router = APIRouter(prefix="/api/v1/security", tags=["security"])


@router.get("/me")
def who_am_i(
    request: Request,
    principal: Principal = Depends(get_current_principal),
    tenant: TenantContext = Depends(get_tenant_context),
    db: Session = Depends(get_tenant_db_session),
):
    append_audit_event(
        db,
        tenant_id=tenant.tenant_id,
        actor_sub=principal.subject,
        action="security.identity.read",
        resource_type="identity",
        resource_id=principal.subject,
        outcome="success",
        correlation_id=request.state.request_id,
    )
    db.commit()
    return {
        "subject": principal.subject,
        "roles": sorted(principal.roles),
        "tenant_id": tenant.tenant_id,
        "site_id": tenant.site_id,
        "purpose_of_use": principal.purpose_of_use,
        "mfa_assurance": principal.acr,
    }
