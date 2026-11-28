# M3 acceptance checklist - Architecture & security design

M3 follows the exit gate in `01_clinical_intelligence_milestone_plan.pdf`.

## Required deliverables

- [x] Proposed architecture context and module boundaries documented.
- [x] Proposed data flow and trust boundaries documented; clinical rule/evidence modules explicitly disabled pending M2.
- [x] Initial threat scenarios documented; likelihood/residual risk review remains outstanding.
- [x] Preliminary roles and permissions matrix documented.
- [x] Privacy impact question set prepared; no legal assessment claimed.
- [x] Initial deployment topology proposal documented; production provider/region not selected.
- [x] ADR proposals recorded for identity, tenant isolation, audit and model-inference boundary.
- [x] Security reference map updated to stable OWASP ASVS 5.0.0, OWASP API Top 10 2023, OWASP GenAI LLM Top 10 2026 and NIST CSF 2.0.

## Acceptance still required

- [ ] Product owner reviews and accepts architecture, threat model, roles and deployment proposal.
- [ ] Security reviewer challenges threat model and access model, or the review is explicitly recorded as unavailable with residual risks accepted only for synthetic development.
- [ ] Privacy/legal questions are assigned for resolution before any PHI environment is designed or hosted.
- [ ] M2 dependencies and no-clinical-use restrictions remain visible in the project plan.

**M3 status: DRAFT PACKAGE PREPARED - NOT ACCEPTED / NOT COMPLETE.**

No live PHI, clinical rules, external model calls with patient information, or clinical pilot is authorized by this design package.
