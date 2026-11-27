# M1 preliminary product risks

This is an early product risk list for M1, not the formal clinical hazard analysis or security threat model. Those are M2/M3 deliverables.

| ID | Risk | Why it matters | M1/M2 response | Owner/status |
|---|---|---|---|---|
| P-01 | No target clinic selected | The current-state workflow and baseline cannot be truthfully mapped. | Select a clinic and conduct a structured walkthrough; otherwise keep the workflow explicitly hypothetical. | Product owner - open |
| P-02 | No qualified clinical reviewer identified | Intended use, exclusions, data requirements and metrics cannot be clinically approved. | Identify and engage an appropriately qualified reviewer; record credentials and review scope. | Product owner - open |
| P-03 | Scope drift into diagnosis/treatment | Users may interpret drafts as autonomous medical advice. | Restrict intended use and interface language; prohibit diagnosis/prescribing/triage/write-back in v1. | Product + clinician - open |
| P-04 | Missing, stale, conflicting or incorrectly matched data | A draft may be based on the wrong patient or incomplete context. | Tenant/site and relationship checks, source provenance, freshness and mismatch states; formal threat/risk review in M2/M3. | Product + engineering - open |
| P-05 | Guideline conflict, expiry or unlicensed use | Outdated or improperly reused material can make output unsafe or unlawful. | Select sources with clinician and licence review in M2; version and freshness controls in M7. | Clinical reviewer - open |
| P-06 | Regulatory status assumed incorrectly | Software with an intended medical purpose may fall within DRAP medical-device rules. | Obtain qualified regulatory advice and, where needed, DRAP clarification in M2; do not claim exemption or class. | Product owner + counsel - open |
| P-07 | PHI leakage through demo, logs or AI tools | Could expose highly sensitive patient data. | Synthetic-only development; customer-controlled data boundary; privacy/security assessment before any live data. | Security owner - open |
| P-08 | Workflow does not fit actual clinic operations | Product may add work rather than remove it. | Observe current workflow, map handoffs and collect baseline before claiming benefit. | Product owner - open |
| P-09 | Reviewer or integration access unavailable | Critical validation and pilot dependencies may stall. | Keep synthetic-only scope; record dependency and do not bypass clinical or data-access gates. | Product owner - open |
| P-10 | Competitor or former-employer IP contamination | Could create legal and ownership exposure. | Clean-room design, public-source citations, review agreements and exclude all non-public materials. | Product owner - ongoing |
