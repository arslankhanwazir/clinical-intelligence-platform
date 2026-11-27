# Security Baseline and Verification Plan

Security requirements are design targets until implemented and tested. This list is not a certification or a claim of compliance.

## Identity and authorization
- OIDC authentication with secure session lifecycle, token validation and revocation.
- RBAC plus ABAC, least privilege, separation of duties and deny-by-default.
- MFA for privileged accounts; stronger authentication policy for sensitive roles.
- Server-side object-, function- and tenant-level authorization on every request.
- Account provisioning, deprovisioning, session expiry and emergency access procedures.

## Tenant and data protection
- Explicit tenant context from trusted identity, never from an unchecked client parameter.
- Database and API tenant isolation with negative cross-tenant tests.
- TLS for transport; encryption at rest using managed keys where supported.
- Key rotation, secrets manager, encrypted backups and tested restore.
- Data minimization, retention/deletion rules, access logging and approved data-flow map.
- No PHI in logs, analytics, error traces, AI prompts to unapproved providers or coding assistants.

## Application and API security
- Input schema validation, output encoding, CSRF/session controls where applicable, rate limits and abuse protection.
- Secure headers, CORS allowlist, strict error handling and no debug endpoints in production.
- API inventory, versioning and authorization tests for each endpoint.
- Dependency pinning/review, vulnerability scanning, SBOM and signed/reproducible release process where feasible.

## Audit and operations
- Append-only audit events with integrity verification, access monitoring and time synchronization.
- Audit who accessed/changed what, when, under which tenant and role, and which rule/evidence/model versions were used.
- Security monitoring, alerting, incident response, vulnerability disclosure and recovery runbooks.
- Regular restore drills, patching, access reviews and penetration testing before sensitive production use.

## AI-specific controls
- Treat uploaded or retrieved documents as untrusted data, not instructions.
- Prompt-injection and indirect prompt-injection tests; strict tool allowlists and least privilege.
- No unrestricted SQL, shell, network or write tools for the model.
- Validate structured output, source references, units and allowed fields; reject malformed output.
- Test sensitive-data leakage, model hallucination, refusal/abstention behavior and cross-tenant retrieval.
- Record provider/model/version and relevant configuration for each generated draft.

## Security verification references
Use OWASP ASVS, OWASP API Security Top 10, OWASP Top 10 for LLM Applications, and NIST CSF 2.0 as engineering references. Consider ISO/IEC 27001 as a management-system target if justified. Do not claim certification or conformance without scoped independent assessment.

## Initial release blockers
Any confirmed cross-tenant exposure, unauthorized patient/encounter access, secrets in source control, unencrypted sensitive backup, critical unresolved vulnerability, unaudited clinical write path, or unsafe model tool permission blocks release.
