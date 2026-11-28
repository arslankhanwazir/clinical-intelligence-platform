from collections.abc import Sequence

from fastapi import Depends, HTTPException, status
from sqlalchemy import or_, select, text
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.core.identity import PRIVILEGED_HUMAN_ROLES, Principal
from app.core.tenant import TenantContext, get_tenant_context
from app.core.security import get_current_principal
from app.db.models import Site, Tenant, UserMembership
from app.db.session import get_db_session


def active_memberships(db: Session, tenant: TenantContext, principal: Principal) -> Sequence[UserMembership]:
    statement = select(UserMembership).where(
        UserMembership.tenant_id == tenant.tenant_id,
        UserMembership.subject == principal.subject,
        UserMembership.status == "active",
    )
    if tenant.site_id is None:
        statement = statement.where(UserMembership.site_id.is_(None))
    else:
        statement = statement.where(
            or_(UserMembership.site_id == tenant.site_id, UserMembership.site_id.is_(None))
        )
    return db.scalars(statement).all()


def get_tenant_db_session(
    db: Session = Depends(get_db_session),
    tenant: TenantContext = Depends(get_tenant_context),
    principal: Principal = Depends(get_current_principal),
    settings: Settings = Depends(get_settings),
):
    # Set PostgreSQL's transaction-local tenant context before reading any RLS-protected row.
    if db.get_bind().dialect.name == "postgresql":
        db.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {"tenant_id": tenant.tenant_id},
        )

    tenant_row = db.scalar(
        select(Tenant).where(Tenant.id == tenant.tenant_id, Tenant.status == "active")
    )
    if tenant_row is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Tenant is unavailable")

    if tenant.site_id is not None:
        site_row = db.scalar(
            select(Site).where(
                Site.id == tenant.site_id,
                Site.tenant_id == tenant.tenant_id,
                Site.status == "active",
            )
        )
        if site_row is None:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Site does not belong to this tenant or is unavailable")

    memberships = active_memberships(db, tenant, principal)
    if not memberships and tenant.site_id is None:
        site_membership = db.scalar(
            select(UserMembership.id)
            .where(
                UserMembership.tenant_id == tenant.tenant_id,
                UserMembership.subject == principal.subject,
                UserMembership.status == "active",
                UserMembership.site_id.is_not(None),
            )
            .limit(1)
        )
        if site_membership is not None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Site-ID is required for this membership")

    membership_roles = {membership.role for membership in memberships}
    effective_roles = membership_roles & set(principal.roles)
    if not memberships or not effective_roles:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No active tenant/site membership for this identity")

    # Apply the privileged-role MFA policy to every protected tenant API route, not only admin routes.
    if effective_roles.intersection(PRIVILEGED_HUMAN_ROLES):
        if not settings.oidc_privileged_acr_values or principal.acr not in settings.oidc_privileged_acr_values:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Privileged access requires an approved MFA assurance level",
            )

    yield db
