# Architecture Overview

## Architectural style
Start with a modular monolith and explicit module boundaries. Avoid microservices, multi-agent orchestration and distributed infrastructure until measured requirements justify them.

## Planned components (not yet implemented)
- **Web:** Next.js + TypeScript; role-aware clinical workspace, admin and synthetic demo.
- **API:** Python + FastAPI + Pydantic; validation and server-side authorization.
- **Identity:** OIDC; evaluate Keycloak for customer-controlled deployments. Enforce MFA for privileged identities.
- **Data:** PostgreSQL for durable relational data. Add pgvector only if a measured evidence-retrieval benchmark justifies vector search.
- **Clinical rules:** deterministic, versioned, testable Python rule packs; never delegate rule execution to the LLM.
- **Evidence:** approved-source registry, versioned documents, retrieval and citation verification.
- **AI:** replaceable model-provider adapter; local Ollama is an option only after a model is installed and evaluated. External providers require privacy, security and contractual review.
- **Audit:** append-only events with integrity verification; do not claim tamper-proof without independent assurance.
- **Interoperability:** FHIR R4 as the first integration target. HL7 and other adapters are conditional on validated customer requirements.
- **Quality:** pytest, Playwright, static analysis, dependency/secret checks and CI.

## Logical request flow
Authenticated user -> API authorization -> tenant-scoped patient/encounter context -> validation and missing/conflict detection -> deterministic rules -> approved evidence retrieval -> optional constrained AI draft -> output/citation verification -> clinician review -> audit event.

The model does not get unrestricted database, network, filesystem or clinical write access. Each module returns structured, attributable results.

## Deployment boundary
The intended production direction is customer-controlled on-premises or private-cloud processing. The public marketing site and public demo use synthetic data only. Production PHI must not be routed through an unreviewed Vercel deployment, external model provider, analytics service, logging system or development tool.

## Current workstation constraint
The current Windows workstation is a development environment only. Docker availability has not been confirmed and Ollama currently reports no registered model. Do not block documentation, API contracts or unit-test work on local model installation. Validate hardware, disk and runtime before selecting local inference models.

## Decisions still open
Final OIDC configuration; hosting and key-management model; PostgreSQL deployment; evidence parsing and retrieval approach; charting/component libraries; model choice; FHIR server/integration profile; jurisdiction-specific regulatory classification. Record decisions as ADRs before implementation depends on them.
