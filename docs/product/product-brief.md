# Product brief - Clinical Intelligence Platform

**Status:** M1 draft; not approved for clinical use.
**Internal repository name:** `clinical-intelligence-platform` (working name, not a cleared public brand).
**Initial market hypothesis:** Pakistan private primary-care clinics/hospitals first; prepare public-sector procurement readiness in parallel. International expansion requires separate jurisdiction review.

## Product direction

Build an independent, clinician-facing clinical intelligence / clinical decision-support product for one bounded workflow: **adult primary-care follow-up for patients with an established hypertension diagnosis**. This is the agreed planning candidate, not validated demand or an approved clinical protocol.

The product should organize authorized patient context, make missing, conflicting or stale information visible, expose only clinician-approved deterministic rules and approved evidence, and prepare a source-linked draft for qualified clinician review and attestation.

## Primary users

1. **Clinician:** reviews patient context and a draft; remains responsible for clinical interpretation and decisions.
2. **Clinic administrator:** manages clinic/site users and operational configuration; does not approve clinical rules by virtue of the admin role.
3. **Restricted integration operator:** manages approved data connections and import errors; receives no broad clinical access by default.

Patient-facing portal, patient messaging and partner marketplace are outside v1 scope.

## Product boundary

- Software-first clinical intelligence layer that integrates beside an existing HIS/EHR.
- The clinic's existing HIS/EHR remains the system of record for demographics, encounters, orders and results unless a later signed integration contract says otherwise.
- Store only the minimum context and decision-support artifacts needed for the approved workflow; avoid a duplicate shadow chart by default.
- First integration direction: read-only FHIR R4 or controlled synthetic CSV import. No clinical write-back in v1.
- Customer-controlled on-premises or private-cloud deployment is the planned direction; no production PHI in public demos or unapproved external services.

## Intended product outcome

Make the information and evidence used for a follow-up review easier to inspect and trace, while keeping clinical authority with the qualified clinician. The product is not intended to replace clinical judgment or the clinic's record system.

## Evidence of value to collect

Measure the existing workflow first, then compare the assisted workflow using pre-agreed definitions. Do not claim time savings, improved outcomes, diagnostic accuracy or superiority until measured and reviewed.

## Approval state

- Product owner: Arslan Khan - draft direction approved in project chat on 2026-11-28; approval record: docs/product/product-owner-approval.md.
- Qualified clinical reviewer: not yet identified in the project record.
- Target clinic and current-state workflow: not yet identified or observed.
- Clinical, regulatory, privacy and security approvals: not obtained.

## System working name

**Project Northstar** is the internal working codename for this Clinical Intelligence Platform. It is not a cleared public brand or registered trademark. The repository name remains `clinical-intelligence-platform`. Public naming, domain selection and trademark clearance are deferred until a separate brand review.
