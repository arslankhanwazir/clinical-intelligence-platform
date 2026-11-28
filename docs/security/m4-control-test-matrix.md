# M4 security control and test matrix

| Control | Implementation in this slice | Test/evidence | Remaining limitation |
|---|---|---|---|
| Authentication | OIDC/JWKS RS256 validation | Code path; no live issuer yet | Keycloak integration test pending |
| Token validation | Issuer, audience, exp, iat, sub, algorithm allow-list | Unit/negative tests to be expanded with real tokens | Live realm claims pending |
| Role authorization | Keycloak realm/client roles allow-list | Automated role-denial tests | Role assignment governance pending |
| Tenant boundary | Signed token tenant scope + API query filter + PostgreSQL RLS | Local scope-denial tests | PostgreSQL RLS integration test pending |
| Site boundary | Signed token site scope | Unit/API checks | Site membership source and policy require site review |
| MFA | Privileged `acr` allow-list | Automated insufficient-ACR denial test | Keycloak MFA flow and claim mapping pending |
| Audit integrity | Hash chain + SQLite/PostgreSQL immutable triggers | Local update blocked test | PG concurrency and least-privilege test pending |
| Secret handling | Environment-based settings; `.env` ignored | No credentials committed | Production vault/secret manager pending |
| Error handling | No rejected input echoed in validation error | API behavior test | Full application logging review pending |
| HTTP headers | no-store, nosniff, frame denial, referrer policy | Health test | TLS/HSTS at deployed edge pending |
| Database | SQLAlchemy + Alembic | SQLite migration | PostgreSQL server and RLS test pending |

This matrix is an implementation record, not a certification or independent security assessment.
