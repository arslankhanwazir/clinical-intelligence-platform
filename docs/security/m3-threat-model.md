# M3 - Initial security threat model

**Status:** Initial design draft. Threat likelihood and residual risk have not been formally rated. This is a platform security threat model, not the M2 clinical hazard analysis.

## Assets to protect

- Patient identifiers and clinical data (not permitted in development at this stage).
- User identities, authentication sessions, MFA factors and service credentials.
- Tenant/site membership and access policies.
- Clinical source documents, licence metadata, versions and evidence links.
- Rule-pack versions and expected outputs (rules remain disabled pending M2).
- Model prompts, structured context, outputs and verifier results.
- Audit events, signing/checkpoint keys and backup copies.
- Build pipeline, dependency graph, signing material and release artefacts.
- Availability and integrity of the application and integration endpoints.

## Trust boundaries

- Browser/device to web/API.
- Web/API to identity provider.
- API to database and audit store.
- API to customer EHR/HIS/import files.
- API to model runtime/provider.
- API to evidence repository.
- Build/deployment pipeline to runtime.
- Customer-controlled deployment to public synthetic demo and developer tooling.

## Threat scenarios and planned controls

| ID | Scenario | Security objective / planned control | Required verification |
|---|---|---|---|
| T01 | User changes patient/encounter ID to access another record (BOLA/IDOR) | Server-side object authorization on every read/write; opaque IDs alone are not a control | Multi-user, multi-site and cross-tenant negative API tests |
| T02 | Tenant ID spoofed in header/body | Derive membership and tenant scope from verified identity and server-side membership; reject mismatches | Tampered header/body tests; query scoping tests |
| T03 | Privilege escalation or admin/clinical role confusion | Least privilege, separation of duties, RBAC+ABAC, privileged MFA, deny-by-default | Role matrix tests; horizontal and vertical escalation tests |
| T04 | Stolen session or forged/incorrect token | OIDC validation, issuer/audience/signature/expiry checks, secure session handling, revocation and MFA policy | Invalid/expired/replayed token tests and session tests |
| T05 | Prompt injection in uploaded clinical documents or retrieved content | Treat documents as untrusted data, not instructions; model tools disabled/restricted; no secrets in prompts | Prompt-injection corpus and data-exfiltration tests |
| T06 | Malicious or stale guideline/source enters retrieval | Source approval workflow, checksum, licence, version/effective dates, reviewer identity, withdrawal state | Unapproved/expired/altered source must be excluded or flagged |
| T07 | Model generates unsupported facts or fabricated citation | Structured schema, fact/citation verifier, abstention; draft only; clinician review | Unsupported-fact and unresolved-citation tests |
| T08 | Secrets exposed in Git, logs, CI or coding-agent context | Secret scanning, least-privilege tokens, secret store/env, log redaction, no secrets in prompts | Gitleaks CI, repository history scan and log inspection |
| T09 | Audit events modified or omitted | Append-only write path, restricted DB role, integrity verification, backups and alerting | Tamper simulation, missing-event and restore tests |
| T10 | Backup, export or support channel leaks data | Customer-controlled keys, restricted export, encryption, no PHI in support telemetry by default | Backup/export permissions and restore testing |
| T11 | Integration credential compromise or unsafe upstream API | Per-connection scoped credentials, rotation, outbound allowlist, schema validation, timeouts | Credential rotation and malicious upstream contract tests |
| T12 | Resource exhaustion or abuse of endpoints/model | Request size limits, rate limits, quotas, timeouts, concurrency bounds and monitoring | Load/abuse tests with safe synthetic requests |
| T13 | Dependency/build pipeline compromise | Locked dependencies, scanning, SBOM, protected CI, reviewable releases and signing strategy | Dependency scan, build provenance and release review |
| T14 | Public demo or Figma accidentally contains real patient data | Synthetic-only segregation and data review before publication; no PHI uploads to design tools | Pre-release content check and repository scan |

## STRIDE coverage

- **Spoofing:** identity/session, service account and upstream integration identity.
- **Tampering:** clinical records, imported payloads, evidence versions, audit records and build artefacts.
- **Repudiation:** incomplete or alterable audit trail.
- **Information disclosure:** cross-tenant reads, logs, exports, prompts, backups and public demos.
- **Denial of service:** API/model abuse, resource exhaustion and dependency failures.
- **Elevation of privilege:** broken role/function/object-level authorization and compromised admin credentials.

## Security design principles

- Deny by default, least privilege and server-side authorization.
- Separate authentication (who are you?) from authorization (may you perform this action on this object in this tenant/site and purpose?).
- No patient existence disclosure to unauthorized users.
- No unrestricted model tools, SQL, shell, internet access or write actions.
- No PHI in local development, issue trackers, coding assistants, public demo or routine logs.
- Security controls remain design requirements until implemented and tested; do not claim security certification or independent penetration test.

## Outstanding review

A qualified security reviewer should challenge this model before any pilot. Revisit it after actual clinic workflow, integrations, deployment provider, regulatory obligations and data inventory are known.
