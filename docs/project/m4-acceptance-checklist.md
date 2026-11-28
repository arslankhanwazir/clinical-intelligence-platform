# M4 acceptance checklist — Secure platform foundation

## Locally implemented / testable

- [ ] Isolated Python 3.13 environment created under NORTHSTAR `.venv`.
- [ ] Dependencies installed from pinned requirements.
- [ ] FastAPI app imports and starts locally.
- [ ] Health liveness and database readiness tests pass.
- [ ] OIDC/JWKS validation code enforces RS256, issuer, audience, expiry and required claims.
- [ ] Role allow-list and server-side tenant/site scope tests pass.
- [ ] Privileged MFA `acr` assurance check tests pass.
- [ ] Alembic migration succeeds on local synthetic SQLite database.
- [ ] Audit event is appended and SQLite blocks update/delete.
- [ ] GitHub Actions API test workflow passes.

## External / deployment gates — not yet passed

- [ ] Real Keycloak realm/client configured and token/MFA integration verified.
- [ ] PostgreSQL provisioned; migration and RLS verified with a non-superuser, non-BYPASSRLS application role.
- [ ] Tenant cross-access negative tests pass against PostgreSQL.
- [ ] Production secrets manager, TLS, network controls and host hardening reviewed.
- [ ] Backup/restore, monitoring and incident procedures tested at target environment.
- [ ] Independent security review completed; no unresolved critical/high findings.

**M4 status rule:** Do not mark complete until the local checks and deployment-dependent security gates are evidenced. No PHI, real patient use or clinical capability in this slice.
