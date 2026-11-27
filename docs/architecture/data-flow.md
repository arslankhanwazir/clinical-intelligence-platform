# Data-Flow and Trust-Boundary Draft

This is a logical design draft. Validate it in the threat model before implementation.

## Proposed flow
1. Clinician authenticates through the approved OIDC identity provider.
2. API validates identity, role, tenant and requested resource authorization.
3. API loads only the authorized encounter context and records source, timestamp and provenance for each fact.
4. Validation identifies missing, stale, conflicting or out-of-range facts.
5. Deterministic rule module evaluates approved rule packs only when prerequisites are met.
6. Evidence service retrieves approved, versioned source passages and identifiers.
7. Optional AI service receives a minimized, authorized context and returns a constrained draft; no direct clinical write access.
8. Verification validates schema, source references, allowed content and abstention requirements.
9. Clinician reviews, edits, accepts or rejects the draft.
10. Audit service records access and decision events with actor, tenant, versions and timestamps.

## Trust boundaries to design and test
- Browser to API.
- Identity provider to API.
- Tenant boundary and database access.
- API to model runtime/provider.
- Evidence ingestion and retrieved documents to model context.
- API to integrations / external HIS.
- Application services to logs, monitoring, backups and support tooling.

No PHI may cross a boundary until its purpose, legal basis, security controls, retention and vendor terms have been reviewed. Retrieved content is untrusted input, not privileged instruction.
