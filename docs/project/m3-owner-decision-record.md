# M3 - Product-owner architecture review and decisions

**Status:** Proposed design for product-owner review. No implementation or security assurance is claimed.
**Scope:** Synthetic-only development; no live patient data or clinical use.

## Decisions proposed for acceptance

| ID | Proposed decision | Reason | Status |
|---|---|---|---|
| M3-D01 | Use a modular monolith for the first product release. | Keep domain boundaries clear without premature microservices and excessive operations. | Proposed |
| M3-D02 | Use Next.js/TypeScript for the web workspace and Python/FastAPI/Pydantic for the API. | Matches the engineering blueprint and keeps a typed web/API boundary. | Proposed |
| M3-D03 | Use PostgreSQL with SQLAlchemy/Alembic; begin with relational/full-text search and add pgvector only if retrieval tests justify it. | Avoid premature vector infrastructure. | Proposed |
| M3-D04 | Use Keycloak/OIDC as the identity-provider candidate; enforce authorization in the API with RBAC + ABAC. | Identity tokens alone do not authorize access to individual records. | Proposed |
| M3-D05 | Use a single-customer/site deployment for the first controlled pilot, while keeping tenant/site identifiers and checks in the data model from the start. | Reduce first-deployment isolation complexity; prohibit shared SaaS until separately reviewed. | Proposed |
| M3-D06 | Begin interoperability with synthetic JSON/CSV, then FHIR R4 read-only; no EHR write-back in V1. | Validate mappings and preserve system-of-record boundaries. | Proposed |
| M3-D07 | Use an append-only, tamper-evident audit path with integrity checks; never claim tamper-proof. | Attribute access and sensitive changes while minimizing clinical payload in logs. | Proposed |
| M3-D08 | Use a provider-neutral model gateway; no external model API receives patient data. Local/private inference is a future option after security/privacy review. | Prevent vendor lock-in and uncontrolled data transfer. | Proposed |
| M3-D09 | Keep clinical rules and clinical evidence functions disabled until M2 clinical approval and source permissions exist. | Prevent unapproved clinical logic from entering software. | Proposed |
| M3-D10 | Separate public marketing/synthetic demo hosting from any future customer environment. | Prevent accidental PHI exposure. | Proposed |

## Product-owner review

- Decision: **Pending** (accept / request changes).
- Reviewer: Product owner.
- Date: ____________________
- Notes / changes required: ______________________________________________

## Security and privacy review

- Independent security reviewer: Not yet identified.
- Privacy/legal reviewer: Not yet identified.
- Until reviewed, this is a proposed design for synthetic-only work; no PHI deployment or pilot is authorized.

## Explicitly not decided here

- Clinical thresholds, treatment rules or guideline selection.
- Final DRAP classification or registration pathway.
- Production provider, region, contracts, retention schedule or lawful basis.
- Future shared multi-tenant SaaS design.
- Production model selection or performance qualification.
