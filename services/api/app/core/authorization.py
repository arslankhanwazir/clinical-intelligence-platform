from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import Settings, get_settings
from app.core.identity import PRIVILEGED_HUMAN_ROLES, Principal
from app.core.security import get_current_principal
from app.core.tenant import TenantContext, get_tenant_context
from app.db.dependencies import active_memberships, get_tenant_db_session

# Re-export these names to preserve the imports already used by the API routes.
__all__ = ["TenantContext", "get_tenant_context", "require_roles"]


def require_roles(*required_roles: str):
    def dependency(
        principal: Principal = Depends(get_current_principal),
        tenant: TenantContext = Depends(get_tenant_context),
        db: Session = Depends(get_tenant_db_session),
        settings: Settings = Depends(get_settings),
    ) -> Principal:
        memberships = active_memberships(db, tenant, principal)
        database_roles = {membership.role for membership in memberships}
        effective_roles = set(principal.roles) & database_roles

        if not effective_roles.intersection(required_roles):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient active membership role")

        if effective_roles.intersection(PRIVILEGED_HUMAN_ROLES):
            if not settings.oidc_privileged_acr_values or principal.acr not in settings.oidc_privileged_acr_values:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail="Privileged access requires an approved MFA assurance level",
                )
        return principal

    return dependency
