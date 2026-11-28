# M4 Keycloak integration configuration — not yet connected

This is a configuration guide only. The local API has no live Keycloak server or realm at this stage.

1. Provision a dedicated Keycloak realm for NORTHSTAR in a controlled Linux environment; do not expose the admin console publicly.
2. Create an OIDC confidential client for the API with an explicit audience `northstar-api`; use authorization-code + PKCE for browser clients and client credentials only for workload/service accounts where appropriate.
3. Configure signed RS256 access tokens and verify the realm issuer, JWKS endpoint and API audience from the actual discovery document.
4. Add narrowly scoped role mappers for the allow-listed roles: `platform_operator`, `tenant_admin`, `clinician`, `clinical_safety_reviewer`, `records_support`, `security_auditor`, `integration_service`.
5. Add trusted claim mappers for `tenant_ids` (or `tenant_id`), `site_ids`, and `purpose_of_use`. Values must come from an administratively controlled membership source, not user-editable profile fields.
6. Configure MFA for all interactive human roles. Map verified authentication assurance to the configured `acr` value and set `OIDC_PRIVILEGED_ACR_VALUES` to the exact value observed in signed tokens. Never assume `acr=2` until tested against the actual realm.
7. Verify issuer, audience, expiry, signature, roles, tenant/site claims, MFA claim, logout/session revocation, key rotation and unavailable-JWKS behavior using non-production accounts.
8. Keep the realm and API private-network accessible; require TLS, administrative MFA, backups, monitoring and recovery tests.

Do not copy production client secrets into `.env.example`, Git, chat, screenshots or coding-agent prompts. Store live secrets in an approved secrets manager.
