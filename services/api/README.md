# NORTHSTAR API — M4 secure foundation

This is the first executable backend foundation. It is a synthetic-data development baseline, not a production deployment or a clinical application.

## Current implementation

- FastAPI application with public liveness/readiness checks.
- OIDC access-token verification through a Keycloak-compatible JWKS endpoint (RS256 only; issuer/audience/expiry required).
- Role extraction from Keycloak realm/client role claims, restricted to an allow-list.
- Server-side tenant/site scope checks from trusted token claims; request headers only select among token-authorized scopes.
- MFA assurance gate for interactive privileged roles using an explicitly configured `acr` allow-list.
- SQLAlchemy models and Alembic migration for tenants, sites, user memberships and audit events.
- PostgreSQL row-level security policies and append-only audit triggers in the migration.
- SQLite local-only migration triggers for audit immutability tests.
- SHA-256 chained audit events; call them tamper-evident, not tamper-proof.
- Safe validation errors, request correlation IDs and API security headers.
- Automated tests for health, claim mapping, tenant denial, role denial, MFA gate and audit immutability.

## Local setup

The repository setup script creates `.venv` from the Python 3.13 interpreter already present on the workstation, installs pinned dependencies, creates a local SQLite database under `data/`, runs Alembic and executes tests.

Start the API from the repository root:

```cmd
.venv\Scripts\python.exe -m uvicorn app.main:app --app-dir services\api --host 127.0.0.1 --port 8000
```

The local environment uses SQLite only for synthetic development. It is not the target production database. Production settings reject SQLite and require PostgreSQL and explicit OIDC issuer/JWKS/audience values.

## Keycloak configuration still required

A live Keycloak realm/client is not bundled or provisioned. Before accepting real tokens, create an OIDC client for `northstar-api`, configure signed RS256 access tokens, publish issuer/JWKS/audience, and add trusted protocol mappers for `tenant_ids` (or `tenant_id`), `site_ids`, and `purpose_of_use`. Configure the Keycloak authentication flow to emit the approved `acr` assurance value after MFA; configure the same exact value in `OIDC_PRIVILEGED_ACR_VALUES`. Verify token claims and MFA behavior against the actual realm before calling the integration complete.

Do not use test overrides, development shortcuts or hand-crafted unsigned JWTs outside automated tests.

## PostgreSQL controls

The migration enables and forces row-level security on tenant-owned tables using the transaction-local PostgreSQL setting `app.tenant_id`. The API applies that setting after validating the tenant in the signed token. The database application role must not be a superuser or have `BYPASSRLS`; an owner/superuser can bypass policies. Test using the actual least-privilege database role before claiming tenant isolation.

The audit trigger blocks update/delete. The service serializes audit-chain appends with a PostgreSQL transaction advisory lock. These controls still need integration tests against a real PostgreSQL server.

## Explicit gaps / not yet complete

- No live Keycloak server or real OIDC realm has been configured or tested.
- No PostgreSQL server has been provisioned or migration tested against PostgreSQL.
- No production secrets manager, TLS reverse proxy, firewall or host hardening has been deployed.
- No independent security review or penetration test has been performed.
- No patient, encounter, clinical rule, guideline, model or patient-facing endpoint exists in this M4 slice.
- No real patient data or clinical use is permitted.

## Commands

```cmd
.venv\Scripts\python.exe -m alembic -c services\api\alembic.ini upgrade head
set PYTHONPATH=services\api
.venv\Scripts\python.exe -m pytest services\api\tests -q
```
