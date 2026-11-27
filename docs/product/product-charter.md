# Product Charter

## Product
An independent clinician-facing clinical intelligence and decision-support platform. It is not a replacement HIS/EHR and is not an autonomous clinician.

## Proposed first workflow
Adult primary-care hypertension follow-up support. This is an engineering hypothesis only; demand, clinical workflow, local guidelines, clinical safety and regulatory classification are not yet validated.

## Intended-use draft (not a regulatory conclusion)
The proposed software is intended to help qualified healthcare professionals organize available patient information, surface missing or conflicting information, apply separately approved deterministic protocol rules, retrieve versioned clinical evidence, and prepare a decision-support draft for clinician review. The clinician remains responsible for interpretation and care decisions.

This wording does not determine whether the software is a medical device or exempt from regulation. Obtain jurisdiction-specific regulatory assessment, including DRAP requirements, before clinical deployment or promotion.

## Users to validate
- Treating clinician / authorized healthcare professional.
- Clinic or hospital administrator.
- Clinical governance / protocol reviewer.
- System administrator / security operator.

Each role requires a documented permission matrix. A UI role is not a substitute for server-side authorization.

## Core workflow
1. Authorized user opens an encounter.
2. System displays source-attributed patient facts and freshness.
3. System flags missing, conflicting, stale or out-of-range values.
4. Deterministic, versioned rules run only when required inputs and approved scope are satisfied.
5. Evidence retrieval returns approved source excerpts and versions.
6. AI may draft a structured summary; verification checks schema, facts and citations.
7. System records the Evidence Ledger and clinician accept/edit/reject action.
8. Nothing is finalized or sent as a care instruction without the clinician's explicit action.

## Required differentiators to prove
- Evidence Ledger: patient facts used, missing/conflicting facts, evidence source/version, rule-pack version, model/version, verification outcome and clinician changes.
- Clear abstention when information or evidence is insufficient.
- Customer-controlled deployment and transparent data boundaries.
- Independently measured security, reliability, usability and clinical performance.

## Explicit exclusions for the prototype
No autonomous diagnosis, prescribing, treatment selection, emergency triage, patient-facing medical advice, or automatic clinical record finalization. No live patient data. No unsupported claims of accuracy, certification, regulatory clearance or clinical outcomes.

## Deployment direction
Customer-controlled on-premises/private-cloud first. Hybrid operation is a later option only after data-flow, privacy, contractual, security and regulatory review. Public web hosting is for marketing and synthetic demonstrations only, not patient data.
