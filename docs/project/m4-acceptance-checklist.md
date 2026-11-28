# M4 acceptance checklist — Secure platform foundation

**Scope:** synthetic-only secure API foundation. This checklist follows M4 in `01_clinical_intelligence_milestone_plan.pdf`.

## M4 implementation and automated verification

- [x] Isolated Python 3.13 environment and pinned dependencies installed.
- [x] FastAPI application imports and starts locally.
- [x] Health liveness and database readiness endpoints are tested.
- [x] OIDC/JWKS code enforces RS256, issuer, audience, expiry and required claims.
- [x] Role allow-list and MFA assurance policy are enforced server-side.
- [x] Tenant and site claims are checked against active database tenant/site membership.
- [x] A site is checked as belonging to the selected active tenant.
- [x] Database membership role and signed token role must agree for protected role access.
- [x] PostgreSQL tenant context is transaction-local and applied before RLS-protected queries.
- [x] Audit events are hash-chained; SQLite and PostgreSQL append-only triggers are defined.
- [x] API routes have shared database-backed fixed-window rate limiting; limiter-store failure denies the API request.
- [x] Relative `.env` and SQLite paths resolve from the repository root, independent of working directory.
- [x] Production configuration requires explicit OIDC settings and an explicitly supplied MFA ACR allow-list.
- [x] GitHub Actions contains SQLite and restricted-role PostgreSQL test jobs.

## Evidence still required before closing M4

- [ ] Local SQLite migration and complete test suite pass after this hardening patch.
- [ ] GitHub Actions SQLite job passes on the hardening PR.
- [ ] GitHub Actions PostgreSQL job passes, including restricted-role RLS and audit-trigger tests.
- [ ] CI logs confirm the application role is neither superuser nor `BYPASSRLS`.
- [ ] Secret scan remains clean after the change.

## External deployment / pre-PHI gates (not a reason to rebuild the M4 code slice)

- [ ] A real Keycloak realm/client is configured and its issuer, audience, roles, tenant/site claims, MFA ACR, logout/revocation and key rotation are verified.
- [ ] Production secrets manager, TLS termination, private network and trusted-proxy configuration are reviewed.
- [ ] Production backup/restore, monitoring, incident response and operational procedures are tested.
- [ ] Independent security review and penetration testing are completed before PHI or customer pilot.
- [ ] Qualified clinical, privacy/legal, regulatory and institutional approvals required by M1/M2 are obtained before PHI or clinical use.

**Status rule:** do not mark M4 complete until all implementation/evidence items above pass. External deployment and pre-PHI gates remain mandatory before any real patient data, customer pilot or clinical use. SQLite is development-only. No clinical rules are included or enabled.
