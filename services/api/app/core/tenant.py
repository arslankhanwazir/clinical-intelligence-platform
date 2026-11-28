from dataclasses import dataclass
from uuid import UUID

from fastapi import Depends, Header, HTTPException, status

from app.core.identity import Principal
from app.core.security import get_current_principal


@dataclass(frozen=True)
class TenantContext:
    tenant_id: str
    site_id: str | None = None


def get_tenant_context(
    principal: Principal = Depends(get_current_principal),
    x_tenant_id: str | None = Header(default=None, alias="X-Tenant-ID"),
    x_site_id: str | None = Header(default=None, alias="X-Site-ID"),
) -> TenantContext:
    if not principal.tenant_ids:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="No tenant scope assigned")

    if x_tenant_id is None:
        if len(principal.tenant_ids) != 1:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="X-Tenant-ID is required")
        tenant_id = next(iter(principal.tenant_ids))
    else:
        try:
            tenant_id = str(UUID(x_tenant_id))
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid tenant identifier") from exc

    if tenant_id not in principal.tenant_ids:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Tenant access denied")

    site_id = None
    if x_site_id is not None:
        try:
            site_id = str(UUID(x_site_id))
        except ValueError as exc:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid site identifier") from exc
        if site_id not in principal.site_ids:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Site access denied")

    return TenantContext(tenant_id=tenant_id, site_id=site_id)
