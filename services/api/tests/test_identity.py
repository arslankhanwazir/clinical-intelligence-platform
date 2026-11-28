import pytest

from app.core.identity import Principal, principal_from_claims


def test_keycloak_claims_map_only_known_roles_and_scopes():
    tenant = "f2f1d28f-6e4f-4ed6-bac7-5551f7d7b9f1"
    site = "207a9cb0-7d3d-4ac9-8d3c-9ec5b18d243c"
    principal = principal_from_claims(
        {
            "sub": "user-123",
            "tenant_ids": [tenant],
            "site_ids": [site],
            "realm_access": {"roles": ["clinician", "unknown-admin"]},
            "acr": "2",
            "purpose_of_use": "treatment",
        },
        "northstar-api",
    )
    assert principal.subject == "user-123"
    assert principal.roles == frozenset({"clinician"})
    assert principal.tenant_ids == frozenset({tenant})
    assert principal.site_ids == frozenset({site})
    assert principal.acr == "2"


def test_identity_rejects_bad_tenant_uuid():
    with pytest.raises(ValueError):
        Principal(subject="x", tenant_ids=frozenset({"not-a-uuid"}))
