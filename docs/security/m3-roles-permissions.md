# M3 - Preliminary roles and permissions matrix

**Status:** Draft design. Roles and actions require product-owner and security review before implementation. The matrix is not a substitute for per-object authorization.

## Proposed roles

| Role | Intended responsibilities | Default restrictions |
|---|---|---|
| Platform operator | Operate platform services, tenant provisioning and technical health | No routine clinical-record access; break-glass access only with approval, reason and audit |
| Clinic administrator | Manage clinic/site users and operational configuration | Cannot approve clinical rules or attest clinical drafts merely by being an admin |
| Clinician | Access assigned/authorized patient encounters and review clinical drafts | Only records permitted by tenant/site membership, patient relationship and purpose policy |
| Integration operator | Maintain approved FHIR/import connections, monitor failures and reconcile jobs | No broad clinical data browsing; payload access only when explicitly required and authorized |
| Auditor | Review security/audit events and control evidence | No change permissions; sensitive clinical payloads are excluded unless separately authorized |
| Support operator | Diagnose availability and technical issues | System metadata only by default; no PHI access through routine support tools |

No patient portal role is included in V1.

## Authorization attributes

At minimum, evaluate the relevant combination of:

- authenticated subject and active account state;
- role and permitted action;
- tenant and site membership;
- patient/encounter assignment or other institution-approved relationship;
- purpose of use where required;
- resource state and action sensitivity;
- privileged MFA status and session validity;
- emergency/break-glass state, reason and required post-event review.

## Permission matrix - initial proposal

Legend: **A** = allow within assigned scope after ABAC check; **L** = limited metadata only; **D** = deny by default; **R** = read-only.

| Action | Platform operator | Clinic admin | Clinician | Integration operator | Auditor | Support |
|---|---:|---:|---:|---:|---:|---:|
| View platform health | A | L | L | A | R | A |
| Manage tenant/site configuration | A | A (own site) | D | D | R | D |
| Manage user memberships | A | A (own site) | D | D | R | D |
| View assigned patient context | D* | D* | A | D* | D* | D |
| Import/reconcile clinical data | D | L | D | A (approved feed only) | R | D |
| Review/edit a clinical draft | D | D | A | D | R metadata | D |
| Accept/attest a clinical draft | D | D | A (authorized clinician only) | D | R metadata | D |
| Approve clinical rules/sources | D | D | Only designated qualified reviewer | D | R | D |
| Read security audit events | A | R own site | R own relevant actions | R own integration events | A | L |
| Change security policy | A with MFA and change control | D | D | D | D | D |

`D*` means deny by default; any exception must be approved, time-bound, justified, tested and audited. No role grants access solely because a user knows a record identifier.

## Required authorization tests

- Anonymous and expired-session requests are denied.
- User from Tenant A cannot read or mutate Tenant B data.
- User from Site A cannot read Site B without an explicit approved policy.
- Clinic admin cannot perform clinician attestation or approve clinical rules by default.
- Integration operator cannot browse general patient records.
- Support cannot view PHI through standard logs or dashboards.
- Auditor cannot mutate business records or policy.
- Every privileged action and break-glass event records actor, tenant, target, purpose/reason and result.
