# M3 - Product-owner architecture review and decisions

**Status:** ACCEPTED BY PRODUCT OWNER for synthetic-only development. This is design approval, not implementation, independent security assurance, legal approval or production authorization.
**Reviewer:** Arslan Khan, product owner (approval recorded in project conversation)
**Decision date:** 28 November 2026
**Scope:** Synthetic-only development. No live patient data or clinical use.

## Product-owner decision

**Decision: APPROVE all ten proposed M3 architecture decisions as the initial design baseline, subject to the constraints and open reviews recorded below.**

| ID | Accepted design decision | Status |
|---|---|---|
| M3-D01 | Use a modular monolith for the first product release. | Accepted for design |
| M3-D02 | Use Next.js/TypeScript for the web workspace and Python/FastAPI/Pydantic for the API. | Accepted for design |
| M3-D03 | Use PostgreSQL with SQLAlchemy/Alembic; start with relational/full-text search and add pgvector only if retrieval tests justify it. | Accepted for design |
| M3-D04 | Use Keycloak/OIDC as the initial identity-provider candidate; enforce authorization in the API with RBAC + ABAC. | Accepted for design |
| M3-D05 | Use a single-customer/site deployment for the first controlled pilot, while retaining tenant/site identifiers and checks in the data model from the start. | Accepted for design |
| M3-D06 | Begin interoperability with synthetic JSON/CSV, then FHIR R4 read-only; no EHR write-back in V1. | Accepted for design |
| M3-D07 | Use an append-only, tamper-evident audit path with integrity checks; never claim tamper-proof. | Accepted for design |
| M3-D08 | Use a provider-neutral model gateway; no external model API receives patient data. Local/private inference remains a future option subject to security/privacy review. | Accepted for design |
| M3-D09 | Keep clinical rules and clinical evidence functions disabled until M2 clinical approval and source permissions exist. | Accepted for design |
| M3-D10 | Separate public marketing/synthetic demo hosting from any future customer environment. | Accepted for design |

## Conditions attached to this approval

1. The architecture is approved as a proposed design baseline only. The controls are not implemented, tested or independently certified by this approval.
2. Development remains synthetic-data-only. No PHI, real patient accounts, real clinic integrations or clinical use are authorized.
3. Clinical rules, guideline-derived recommendations and clinical evidence functions remain disabled until the M1/M2 clinical, source-rights and regulatory gates are satisfied.
4. No external model API may receive patient data. Gemini and Grok API keys are not needed for M3; any later use is restricted to synthetic test material unless separately reviewed and approved.
5. The first deployment design remains one customer/site. Shared multi-tenant SaaS, production hosting provider/region and EHR write-back are not approved by this record.

## Security and privacy review status

- Independent security reviewer: **Not currently available.** The product owner accepts the documented residual design risk only for synthetic-only development. Independent security review is required before any PHI environment, customer pilot or production deployment.
- Privacy/legal reviewer: **Not currently available.** The product owner is assigned to obtain qualified privacy/legal review and resolve the privacy-impact questions before any PHI environment is designed, hosted or connected.
- These limitations are not security certification, penetration-test evidence, legal advice or regulatory approval.

## Explicitly not decided or approved

- Clinical thresholds, treatment rules, guideline selection or clinical source approval.
- Final DRAP classification, registration pathway or regulatory exemption.
- Production provider, region, contracts, retention schedule, lawful basis or cross-border transfer approval.
- Future shared multi-tenant SaaS design.
- Production model selection, external inference permission or model performance qualification.
- PHI processing, patient-care use, clinical pilot or public clinical claims.

## Approval record

The product owner approved all ten M3 design decisions in the project conversation on 28 November 2026. No handwritten or cryptographic signature was supplied. This record documents that chat approval and its restrictions; it does not imply any third-party approval.
