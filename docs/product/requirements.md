# Product requirements - M1 draft

These are product-level requirements, not clinical rules. Clinical field lists, thresholds, required inputs and medical logic remain subject to qualified clinical review in M2 and later rule approval in M6.

| ID | Requirement | Acceptance evidence | Status |
|---|---|---|---|
| PR-001 | Provide a clinician-first workspace for the approved adult hypertension follow-up workflow only. | Clinician walkthrough confirms workflow boundary and user tasks. | Draft |
| PR-002 | Provide separate clinician and clinic-administrator experiences; keep integration operator permissions restricted. | Role/persona review and access matrix in M3. | Draft |
| PR-003 | Select an authorized patient/encounter within the user's tenant, site and permitted relationship. | Approved patient-matching and access requirements; security tests in M4. | Draft |
| PR-004 | Read the minimum approved patient context from the clinic's system of record through FHIR R4 or a controlled import path. | Clinic-approved data mapping, source IDs and test fixtures in M5. | Draft |
| PR-005 | Preserve source, source-record identifier, effective time, received time, units, status and transformation version for imported facts. | Synthetic import tests preserve provenance in M5. | Draft |
| PR-006 | Make missing, conflicting, stale, unmapped or implausible information visible; never fill a gap by guessing. | Synthetic data-quality test cases in M5/M10. | Draft |
| PR-007 | Display only deterministic rules that have an approved owner, source/version, scope, exclusions, tests and release approval. | Clinical rule change-control record in M6. | Blocked until M2/M6 |
| PR-008 | Display evidence only from the approved, versioned source register with exact source references and licence status. | Evidence traceability tests in M7. | Blocked until M2/M7 |
| PR-009 | Any generated content is a structured draft tied to the authorized facts, rule version and evidence references. | Schema, factual and citation verification tests in M8. | Draft |
| PR-010 | The responsible clinician can edit, reject or accept/attest a draft; actor and time are recorded. | Review flow and audit tests in M9/M10. | Draft |
| PR-011 | No autonomous diagnosis, prescribing, medication ordering, emergency triage, autonomous patient messaging or silent chart write-back in v1. | Product and interface review confirms prohibited actions are absent. | Draft |
| PR-012 | If required data, evidence, model service, verification or audit is unavailable, disclose the failure and abstain/return to the existing clinical workflow. | Failure-state tests in M8/M10. | Draft |
| PR-013 | Public demos, test fixtures and screenshots use synthetic data only. | Repository and release review; secret/data scan. | Active constraint |
| PR-014 | The platform integrates beside an existing HIS/EHR and does not become a duplicate system of record by default. | Integration boundary documented in M3/M5. | Draft |

## Open requirement decisions

- Final required patient-context fields and data-quality rules: clinician + target clinic.
- Exact output artefact and where it may be stored: target-clinic workflow and legal/privacy review.
- Which FHIR resources and profiles are actually available at the target site: integration discovery.
- Required languages and RTL scope: target clinic and user testing; do not claim localization before validation.
- Numerical clinical thresholds and performance acceptance levels: not defined in M1.

## Product-owner approval clarifications (2026-11-28)

- Context completeness may be displayed as a data-quality indicator only. It is not a clinical sufficiency/safety decision and must not drive clinical logic until required fields and rules are approved by a qualified clinician.
- Clinician accept/attest records review in NORTHSTAR only. It does not sign, finalize or write to the official HIS/EHR record; v1 has no automatic or silent write-back.
- Pakistan private clinics/hospitals remain an initial market hypothesis, not validated demand or a verified willingness-to-pay finding.
- These clarifications do not authorize clinical rules, thresholds, recommendations, real-patient use or clinician-independent decisions.
