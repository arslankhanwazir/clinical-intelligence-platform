# M4 implementation record — first secure API slice

**Status:** Initial implementation package; synthetic local testing only.

## Implemented in this slice

- FastAPI application entry point and health endpoints.
- External OIDC/JWKS access-token verification boundary; no local password store.
- Keycloak realm/client role claim extraction with an explicit role allow-list.
- Tenant/site scope validation from signed token claims.
- Privileged-role MFA assurance check against configured OIDC `acr` values.
- SQLAlchemy schema for tenant, site, user membership and audit event records.
- Alembic migration with PostgreSQL RLS policies and append-only audit triggers; SQLite triggers support local immutability tests.
- Audit hash chain and request correlation ID.
- Safe request-validation errors and baseline API security headers.
- Test suite for implemented behavior.

## Not claimed as complete

Keycloak is not running/configured. PostgreSQL is not installed/provisioned or integration-tested. Production secrets management, TLS termination, network controls, backup/restore, independent security review and penetration testing remain open. No clinical data or logic is included.

## Workstation constraints

Local development uses Python 3.13.14 from `F:\n8n-scraper\python.exe` as the base interpreter, with a NORTHSTAR-only virtual environment at `.venv`. The other project environment is not modified. SQLite is for local synthetic tests only. Docker is not available on the recorded workstation, so Keycloak/PostgreSQL production-equivalent services are not provisioned here.

## M4 evidence to capture

- Dependency installation output and package versions.
- Alembic migration success.
- Automated test output.
- GitHub Actions API CI result.
- Later: PostgreSQL RLS integration test under a non-owner/non-BYPASSRLS account, real Keycloak OIDC and MFA integration test, and security review.
