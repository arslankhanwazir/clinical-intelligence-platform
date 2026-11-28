from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.authorization import TenantContext, get_tenant_context
from app.core.security import get_current_principal
from app.core.identity import Principal
from app.db.session import get_db_session


def get_tenant_db_session(
    db: Session = Depends(get_db_session),
    tenant: TenantContext = Depends(get_tenant_context),
    _principal: Principal = Depends(get_current_principal),
):
    # PostgreSQL RLS is a second enforcement boundary. The API still filters each query.
    if db.get_bind().dialect.name == "postgresql":
        db.execute(
            text("SELECT set_config('app.tenant_id', :tenant_id, true)"),
            {"tenant_id": tenant.tenant_id},
        )
    try:
        yield db
    finally:
        db.close()
