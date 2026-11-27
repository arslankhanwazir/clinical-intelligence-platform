# M1 open decisions and required owner input

Do not fill these with assumptions. Record answers with source, owner and date.

| Decision | Current state | Required evidence / owner |
|---|---|---|
| Target clinic for as-is workflow mapping | Not supplied | Product owner to identify one clinic/site where a workflow walkthrough is permitted. |
| Qualified clinician reviewer | Not identified | Product owner to identify clinician name, qualification/specialty and permission to review the proposed scope. |
| Current-state process | Not observed | Structured walkthrough/notes approved by the clinic; no confidential documents or patient identifiers in Git. |
| Exact in-scope population | Adult with established hypertension diagnosis - proposal only | Clinician approval of inclusion and exclusion criteria. |
| Exact patient-context fields | Candidate data groups only | Clinician + clinic specify minimum necessary fields and how each is sourced. |
| Actual system of record / integration | Unknown | Target clinic confirms HIS/EHR, FHIR capability or permitted synthetic/test export. |
| Intended-use wording | Draft in `intended-use-draft.md` | Product owner and qualified clinician sign; regulatory review follows in M2. |
| Success metric baseline and targets | Definitions drafted; no baseline values | Collect at clinic; clinician and product owner approve targets after baseline. |
| Guideline/source selection | Not selected | M2 clinician, licensing and jurisdiction review; source candidates are recorded separately. |
| Local language / RTL requirements | Not validated | Target-clinic user requirements and usability testing. |

## Minimum information needed to finalize M1

1. One target clinic/site for the workflow walkthrough, or an explicit statement that no clinic is currently available.
2. One qualified clinician reviewer, or an explicit statement that no reviewer is currently available.

Until those are provided, the product workflow remains a proposed hypothesis and M1 cannot be marked complete under the PDF exit gate.

## Deferred M1 decisions - 28 November 2026

1. Target clinic/site is not available yet. Add its name and record an observed current-state workflow when access is secured. Do not invent a clinic or describe a proposed workflow as observed.
2. Qualified clinician reviewer is not available yet. Record the reviewer's verified name, qualification, role, review date and documented approval when appointed. Do not invent a reviewer or sign-off.
3. Product-owner approval of the product requirements and intended-use draft is still pending written confirmation.
4. Public/commercial product brand and domain are deferred. Project Northstar is an internal codename only; no trademark or domain clearance is claimed.
