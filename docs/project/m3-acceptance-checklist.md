# M3 acceptance checklist - Architecture & security design

This checklist follows the M3 definition of done in `01_clinical_intelligence_milestone_plan.pdf`.

## Required deliverables

- [x] Proposed architecture context and module boundaries documented.
- [x] Proposed data flow and trust boundaries documented; clinical rule/evidence modules explicitly disabled pending M2.
- [x] Initial threat scenarios documented; likelihood and residual risk are not formally rated and require independent review before PHI or pilot.
- [x] Preliminary roles and permissions matrix documented.
- [x] Privacy-impact question set prepared; this is not a legal/privacy assessment.
- [x] Initial deployment topology proposal documented; production provider/region not selected.
- [x] ADR proposals recorded for identity, tenant isolation, audit and model-inference boundary.
- [x] Security reference map updated to OWASP ASVS 5.0.0, OWASP API Top 10 2023, OWASP GenAI LLM Top 10 2026 and NIST CSF 2.0.

## Product-owner and review gates

- [x] Product owner reviewed and accepted all ten architecture decisions, threat-model direction, roles and deployment proposal on 28 November 2026. See `m3-owner-decision-record.md`.
- [x] Independent security reviewer is not currently available. Product owner explicitly accepts residual design risk for synthetic-only development; independent review is mandatory before PHI, customer pilot or production.
- [x] Privacy/legal questions are assigned to the product owner for resolution with qualified reviewers before any PHI environment is designed, hosted or connected. Questions remain unresolved.
- [x] M1/M2 dependencies and no-clinical-use restrictions remain visible in the design and project status records.

## M3 decision and remaining limits

**M3 design status: ACCEPTED for synthetic-only development.** The architecture-design gate is accepted by the product owner with the restrictions above. This does not mean controls are implemented or security-tested, and it does not authorize PHI, clinical rules, live clinical use, customer pilot or production deployment.

Before any PHI environment or pilot, obtain independent security review, qualified privacy/legal assessment, clinical and regulatory approvals required by M1/M2, and site/institution authorization. M4 implementation must still pass its own authorization, MFA, audit and secret-management tests.
