# Milestone roadmap - aligned to the approved three-PDF blueprint

**Roadmap source:** `01_clinical_intelligence_milestone_plan.pdf`, version 1.0, prepared 28 November 2026. The roadmap IDs and sequence below intentionally match that document. Dates are planning estimates, not guarantees.

## Current status

- **M0 - COMPLETE.** Private repository, ownership/IP and clean-room records, workstation baseline, contribution policy and secret-scanning workflow are in place. GitHub Free branch-protection limitations are documented; Gitleaks success was owner-confirmed.
- **M1 - DOCUMENTATION PREPARED / EXIT GATE BLOCKED.** Product brief, requirements, intended-use draft, proposed workflow, personas, non-goals, metrics and risks are recorded. A target-clinic observed workflow and qualified clinician approval remain outstanding.
- **M2 - DESK RESEARCH PREPARED / EXIT GATE BLOCKED.** Candidate source and permission registers, exclusions, approval workflow, preliminary hazards and regulatory assessment notes are recorded. Qualified clinical/source-rights and regulatory approvals remain outstanding.
- **M3 - COMPLETE: DESIGN ACCEPTED FOR SYNTHETIC-ONLY DEVELOPMENT.** Architecture, threat model, data flow, ADRs, role matrix, privacy questions and deployment decision were accepted by the product owner and merged into `main`. This is not independent security certification or PHI authorization.
- **M4 - IN PROGRESS.** Secure API foundation is merged into `main`; 16 local tests passed before the current hardening work. Tenant/site membership, rate limiting, PostgreSQL RLS verification and CI hardening are being added. Do not mark M4 complete until its updated checklist and CI evidence pass.
- **M5-M13 - NOT STARTED.** No patient-context feature, clinical rules, evidence ingestion, AI synthesis, frontend build, pilot or launch work is authorized by this status update.

## Roadmap

| ID | Planning window | Milestone | Main work | Exit gate |
|---|---|---|---|---|
| M0 | Days 1-3 | Independent foundation | Private repository, ownership/IP separation, workstation/tool check, source register, risk log, contribution rules and secret scan. | Repository/access model approved; branch protection where available; required foundation files; secret scan clean; no production data; ownership/IP checklist reviewed. |
| M1 | Week 1 | Product charter & workflow | User roles, one narrow workflow, target-clinic workflow map, patient context, inputs, output, handoff, operational failures, non-goals, pilot hypothesis and measurable outcomes. | One-page product brief, requirements, workflow diagram, personas, non-goals, metric definitions and risks; intended-use draft approved by product owner and qualified clinician. |
| M2 | Weeks 1-2 | Clinical & regulatory boundary | Qualified clinical safety reviewer, current/licensable guidelines, exclusions, hazard analysis, DRAP/regulatory review and safety-case outline. | Signed scope, source/version policy, exclusions, rule approval workflow, regulatory actions and clinical hazards register. |
| M3 | Weeks 2-3 | Architecture & security design | Trust boundaries, threat model, tenant/site isolation, access matrix, audit events, privacy questions, local inference boundary, retention, backup and deployment topology. | Architecture, threat model, data-flow map, ADRs, roles/permissions matrix, privacy-impact questions and deployment decision accepted. |
| M4 | Weeks 3-5 | Secure foundation | API shell, database migrations, OIDC, tenant middleware, server-side RBAC/ABAC, privileged MFA, rate limits, audit events and secrets. | Authorization and tenant-isolation tests pass; MFA for privileged roles; audit path verified; no secret leaks. |
| M5 | Weeks 5-7 | Patient context & interoperability | Patients, encounters, observations, medications, allergies, normalization, provenance, freshness/missing/conflict flags and synthetic FHIR. | Synthetic records import reproducibly; source, timestamps, units and transformations are preserved. |
| M6 | Weeks 7-9 | Deterministic clinical rule pack | Clinician-approved hypertension follow-up rules, units, applicability, exclusions, missing-data gates and versioning. | Clinician-signed rules; unit tests and case-level expected results pass. |
| M7 | Weeks 8-10 | Evidence library & provenance | Approved source ingestion, page/section references, versions/effective dates, licences, retrieval and freshness. | Every evidence item is traceable; stale/unsupported sources are blocked or flagged. |
| M8 | Weeks 10-12 | AI synthesis & verification | Model gateway, structured output, evidence-linked draft, verifier, abstention and prompt-injection controls. | Verifier rejects unsupported claims; safe-abstention scenarios pass. |
| M9 | Weeks 9-14 | Frontend workspace | Figma system, command center, patient timeline, encounter workspace, Evidence Ledger, review flow and administration. | Design review, keyboard/accessibility, responsive and synthetic end-to-end tests pass. |
| M10 | Weeks 14-17 | Clinical evaluation & security QA | Synthetic benchmark, clinician adjudication, adversarial tests, access-control tests, DAST and threat-model update. | No unresolved critical/high security issues; clinical thresholds set by reviewers and met. |
| M11 | Weeks 17-20 | Deployment & integration hardening | Linux on-prem/private-cloud packaging, backup/restore, monitoring, FHIR adapter, performance, upgrade and rollback. | Repeatable install and recovery drill; performance measured on target hardware. |
| M12 | Weeks 20-24 | Pilot readiness | Site SOPs, training, permissions, privacy/security documents, pilot protocol, support and incident plan. | Formal go/no-go by clinical, security, regulatory and institutional stakeholders. |
| M13 | After gates | Controlled pilot & launch | Limited supervised workflow only after approvals; measure outcomes; publish synthetic demo and verified results. | Pilot evidence reviewed; public claims match results; incident and rollback process ready. |

## Critical sequencing rules

1. M1 workflow mapping must distinguish observed target-clinic practice from our proposed product workflow. Do not present an assumption as a fact about a clinic.
2. M2 clinical and regulatory approval is a blocker to clinical rules and any real clinical use. Do not improvise numeric thresholds, medication advice or escalation pathways.
3. M4 security foundation is a blocker to any real patient data.
4. Synthetic-only design, test data, screenshots and demos remain the rule until applicable approvals are obtained.
5. The language model never becomes the system of record, rules authority, authorization engine or audit authority.
