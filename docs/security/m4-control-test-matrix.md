# M4 security control and test matrix

| Control | Implementation | Verification | Remaining limitation |
|---|---|---|---|
| Authentication | OIDC/JWKS RS256 validation | Unit tests plus local HTTP JWKS retrieval test | Real Keycloak realm/client and user flow pending |
| Token validation | Issuer, audience, expiration, issued-at, subject, algorithm allow-list | Positive and negative tests | Production realm claim mapping pending |
| Role authorization | Signed role allow-list plus active database membership role | API negative tests | Operational role-grant governance remains deployment work |
| Tenant boundary | Signed tenant scope, active tenant membership, query filtering and PostgreSQL RLS | SQLite API tests and PostgreSQL restricted-role CI | CI result must be checked on the PR |
| Site boundary | Signed site scope, active site membership, site-to-tenant relationship | Cross-tenant site and missing-site tests | Site assignment workflow is not yet an admin feature |
| MFA | Privileged roles require configured `acr` allow-list | Insufficient-ACR denial test; production ACR must be explicit | Actual Keycloak MFA flow/claim mapping pending |
| Rate limiting | Shared database-backed fixed-window limiter for `/api/v1/*`; fail closed on store failure | 429 and retry-header test; SQLite and PostgreSQL CI | Trusted reverse-proxy/client-IP deployment configuration pending |
| Audit integrity | Hash chain; SQLite/PostgreSQL append-only triggers; PostgreSQL per-tenant advisory lock | Chain verification and mutation-denial tests | External protected backups/exports and monitoring pending |
| Secrets/configuration | Root-anchored `.env`, environment overrides, ignored local secrets, explicit production config | Config tests and secret scan | Production secrets manager and rotation pending |
| Database | SQLAlchemy + Alembic; PostgreSQL RLS with transaction-local tenant context | SQLite migration plus restricted-role PostgreSQL CI | Customer-managed production database not provisioned |
| Error handling | Validation errors do not echo rejected input | API tests | Broader logging review pending |
| HTTP headers | `no-store`, `nosniff`, frame denial, referrer policy, production HSTS | API health/header tests | TLS must be configured at deployment edge |

This matrix is implementation evidence, not an independent security assessment, certification or permission to process PHI.
