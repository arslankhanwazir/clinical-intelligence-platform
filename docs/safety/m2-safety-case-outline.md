# M2 clinical safety case outline

**Status:** Skeleton only; no safety claim is yet substantiated or approved.

| Claim ID | Proposed safety claim to examine | Evidence required | Current state |
|---|---|---|---|
| SC-01 | The product is restricted to its stated intended population, users and workflow. | Signed intended use; clinic workflow evidence; approved exclusions; role definitions; scope tests. | Open — no clinic/clinician. |
| SC-02 | Patient and encounter context is correctly identified and provenance is visible. | Identity workflow; source mapping; timestamps/units; duplicate/mismatch tests. | Open — future M5 evidence. |
| SC-03 | Missing, conflicting, stale or invalid information is not silently treated as reliable. | Clinician-approved requirements; data-quality tests; abstention/fallback tests. | Open — rules not approved. |
| SC-04 | Only approved and licensed clinical sources and rules can influence the workflow. | Source register; rights evidence; clinician approvals; rule versioning and release records. | Open — sources are candidates only. |
| SC-05 | Generated content cannot silently override source facts or deterministic outputs. | Structured schemas; verifier tests; injection and unsupported-claim tests. | Open — future M8. |
| SC-06 | Review, access and changes are attributable and auditable. | Authorization design; audit events; access-control tests; tamper-evidence verification. | Open — future M3/M4. |
| SC-07 | Failures and out-of-scope cases return users to the existing clinical workflow. | Failure-state requirements; clinic-approved fallback; synthetic fault-injection tests. | Open — clinic workflow unknown. |

## Safety case rule

Do not declare a claim “supported”, residual risk acceptable, or a release safe until the required evidence exists and the qualified clinical safety reviewer and relevant institution approve it. This outline is a planning document, not a certification or clinical safety case approval.
