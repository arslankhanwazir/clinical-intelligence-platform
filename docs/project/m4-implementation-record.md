# M4 implementation record — secure API foundation and hardening

**Scope:** synthetic-only development. No live Keycloak realm, production PostgreSQL environment, PHI or clinical use is authorized by this record.

## Implemented in the code slice

- FastAPI application entry point, health endpoints, request IDs and baseline security headers.
- OIDC/JWKS access-token validation using RS256, issuer, audience, expiry and required claims; local HTTP-JWKS test verifies real key retrieval over HTTP.
- Explicit allow-list for roles and server-side privileged MFA ACR policy.
- Tenant/site scope validation from signed claims plus active database tenant, site and user-membership checks.
- Site-to-tenant relationship checks; site-scoped memberships require an explicit site selection.
- Database membership role and signed token role must agree before protected role access is granted.
- PostgreSQL transaction-local `app.tenant_id` context before queries protected by row-level security.
- Alembic migration for tenant, site, membership and audit tables; second migration adds shared API rate-limit buckets.
- Fixed-window API rate limiting backed by the database and keyed by a digest of the connecting client address. API requests fail closed if the limiter store is unavailable.
- Audit hash chain, SQLite and PostgreSQL append-only triggers, and request correlation IDs.
- Repository-root resolution for `.env` and relative SQLite database paths.
- Production settings require explicit PostgreSQL, OIDC configuration and an explicitly supplied MFA ACR allow-list.
- CI runs a SQLite suite and a PostgreSQL suite using a restricted application role without superuser or `BYPASSRLS` privileges.

## Known limits / separate gates

- A real Keycloak realm is not yet configured. The local HTTP-JWKS test validates the JWT/JWKS retrieval contract, not Keycloak realm configuration or its MFA user journey.
- PostgreSQL RLS is to be evidenced by the new GitHub Actions integration job; do not infer that it passed until the job is green.
- Rate limiting is a fixed-window per-connecting-address control. Reverse-proxy deployments must configure trusted client-address handling at the edge; do not trust arbitrary `X-Forwarded-For` headers. A future distributed multi-region edge design may require a dedicated limiter service.
- Expired rate-limit windows are pruned globally during API traffic. If API traffic stops, periodic database maintenance is still needed to remove the final expired window.
- Production secrets manager, TLS, firewall/egress controls, backup/restore, monitoring, incident response and independent security review remain deployment gates.
- The `purpose_of_use` claim is captured but is not yet an authorization rule; its allowed values and workflow policy must be approved through M1/M2 before PHI or clinical use.
- M1/M2 clinical, source-rights, privacy/legal and regulatory approvals remain outstanding. No PHI, real clinic integration, clinical rules, pilot or patient-care use is permitted.

## Workstation constraints

Local development remains in the NORTHSTAR-only `.venv`; no other project environment is modified. SQLite is synthetic local development only. The laptop does not need Docker for local coding; PostgreSQL integration validation runs in GitHub Actions.
