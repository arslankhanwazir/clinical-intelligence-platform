# Clinical Intelligence Platform

Independent clinician-facing clinical decision-support software project.

**Current status:** M0 foundation. This repository is not clinically validated, approved, certified, or authorized for patient-care use.

## Product boundary
The first proposed workflow is adult primary-care hypertension follow-up support. It is an engineering hypothesis, not validated demand, a clinician-approved protocol, or a regulatory determination. The prototype uses synthetic data only.

The intended product direction is to organize clinician-entered patient context, flag missing or conflicting information, apply separately versioned clinician-approved deterministic rules, retrieve approved/versioned evidence, and prepare a draft for qualified clinician review.

## Non-goals for the prototype
- No autonomous diagnosis, prescribing, treatment selection, or finalization.
- No real patient information, production credentials, or customer data.
- No claim of clinical effectiveness, regulatory clearance, or security certification.
- No attempt to replace an existing hospital information system (HIS/EHR).

## Planned architecture (not yet implemented)
- Web: Next.js + TypeScript.
- API: Python + FastAPI.
- Data: PostgreSQL; pgvector only when retrieval requirements justify it.
- Identity: OIDC provider; evaluate Keycloak for customer-controlled deployment.
- Interoperability: FHIR R4 first; add HL7 or other adapters only for validated requirements.
- AI: provider adapter; local Ollama is an option after a model is actually installed and evaluated.
- Quality: pytest, Playwright, static checks, dependency and secret scanning, and CI.

These are proposed choices, not claims that the tools are installed or deployed. Keep the first development loop light; do not require Docker on the current Windows workstation.

## Repository map
- `apps/web/`: clinical workspace, administration, and synthetic demo.
- `services/api/`: modular backend domains.
- `integrations/`: FHIR, HL7, and controlled import/export adapters.
- `clinical-knowledge/`: source registry, guideline versions, and rule packs.
- `evaluation/`: synthetic cases, expected results, and test reports.
- `infrastructure/`: development and customer-controlled deployment plans.
- `docs/`: product, architecture, safety, security, decisions, and project records.

## Safety and data handling
Use synthetic data only until clinical, regulatory, security, privacy, and institutional approvals have been established. Never commit patient information, credentials, private keys, or confidential third-party material. See `SECURITY.md` and `docs/safety/clinical-safety.md`.

## Project control
`docs/project/milestones.md` is the execution sequence. `docs/project/tooling-and-agent-workflow.md` defines how coding assistants and human review are used. Git history is the source of truth for code and approved documentation changes.
