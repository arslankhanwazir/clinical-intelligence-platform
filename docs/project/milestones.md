# Milestone roadmap - aligned to the approved three-PDF blueprint

**Roadmap source:** `01_clinical_intelligence_milestone_plan.pdf`, version 1.0, prepared 28 November 2026. The roadmap IDs and sequence below intentionally match that document. Dates are planning estimates, not guarantees.

## Current status

- **M0 - IN PROGRESS / close-out checks pending.** The private repository and first push are complete. `CONTRIBUTING.md` and the Gitleaks workflow are now being added. Branch protection and a successful secret-scan run still require verification. Ownership/IP obligations must be reviewed by the project owner.
- **M1 - DRAFT PACK PREPARED / not signed off.** Product charter and workflow artifacts are being prepared. A target clinic and qualified clinician reviewer have not yet been identified in this repository. The target-clinic as-is workflow and clinician sign-off therefore remain open.
- **M2 onward - NOT STARTED.**

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
