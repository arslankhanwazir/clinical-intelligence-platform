from typing import Any
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

ALLOWED_ROLES = {
    "platform_operator",
    "tenant_admin",
    "clinician",
    "clinical_safety_reviewer",
    "records_support",
    "security_auditor",
    "integration_service",
}

# All interactive human roles are treated as privileged until a site-specific
# security review approves a narrower policy. Machine integration uses workload identity.
PRIVILEGED_HUMAN_ROLES = {
    "platform_operator",
    "tenant_admin",
    "clinician",
    "clinical_safety_reviewer",
    "records_support",
    "security_auditor",
}


class Principal(BaseModel):
    model_config = ConfigDict(frozen=True)

    subject: str = Field(min_length=1, max_length=255)
    roles: frozenset[str] = frozenset()
    tenant_ids: frozenset[str] = frozenset()
    site_ids: frozenset[str] = frozenset()
    acr: str | None = None
    purpose_of_use: str | None = None

    @field_validator("tenant_ids", "site_ids")
    @classmethod
    def validate_uuid_scopes(cls, values):
        normalized = set()
        for value in values:
            normalized.add(str(UUID(str(value))))
        return frozenset(normalized)


def principal_from_claims(claims: dict[str, Any], client_id: str) -> Principal:
    subject = claims.get("sub")
    if not isinstance(subject, str) or not subject.strip():
        raise ValueError("Token subject is missing")

    roles: set[str] = set()
    realm_access = claims.get("realm_access") or {}
    realm_roles = realm_access.get("roles", []) if isinstance(realm_access, dict) else []
    if isinstance(realm_roles, list):
        roles.update(role for role in realm_roles if isinstance(role, str))

    resource_access = claims.get("resource_access") or {}
    client_access = resource_access.get(client_id, {}) if isinstance(resource_access, dict) else {}
    client_roles = client_access.get("roles", []) if isinstance(client_access, dict) else []
    if isinstance(client_roles, list):
        roles.update(role for role in client_roles if isinstance(role, str))

    roles.intersection_update(ALLOWED_ROLES)

    raw_tenants = claims.get("tenant_ids")
    if raw_tenants is None:
        one_tenant = claims.get("tenant_id")
        raw_tenants = [one_tenant] if one_tenant else []
    if not isinstance(raw_tenants, list):
        raise ValueError("Tenant scope claim must be a list")

    raw_sites = claims.get("site_ids", [])
    if not isinstance(raw_sites, list):
        raise ValueError("Site scope claim must be a list")

    return Principal(
        subject=subject,
        roles=frozenset(roles),
        tenant_ids=frozenset(str(value) for value in raw_tenants),
        site_ids=frozenset(str(value) for value in raw_sites),
        acr=str(claims["acr"]) if claims.get("acr") is not None else None,
        purpose_of_use=str(claims["purpose_of_use"]) if claims.get("purpose_of_use") else None,
    )
