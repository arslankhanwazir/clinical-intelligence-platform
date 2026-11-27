# M1 personas and roles - draft

These roles follow the three-PDF blueprint. Actual job titles, privileges and workflows must be validated at the target clinic.

## 1. Treating clinician - primary user

**Goal:** Review an adult follow-up encounter with relevant authorized context and evidence visible in one place.
**Needs:** Patient/encounter identity, source-attributed facts, missing/conflicting-data states, approved rule/evidence results, a draft that can be edited/rejected/attested, and a traceable record.
**Authority:** Retains all clinical judgment and decisions. Only appropriately authorized clinical reviewers can approve clinical rule/source changes.

## 2. Clinic administrator - operational user

**Goal:** Operate the clinic/site workspace and manage authorized users and operational settings.
**Needs:** User/site management, workflow configuration, integration status and support visibility.
**Limit:** Administrative permission does not confer clinical approval or automatic access to all patient data.

## 3. Integration operator - restricted technical user

**Goal:** Maintain approved FHIR/import connections and reconcile technical failures.
**Needs:** Connection status, mapping errors, rejected records, retry state and credential health without displaying secrets.
**Limit:** Minimum technical access; no broad clinical record access and no ability to approve rules or clinical drafts by default.

## Out of scope

Patient portal, patient messaging, clinic marketplace, kiosk operator, telemedicine operator and autonomous agent roles are not v1 personas. Any later addition requires separate product, privacy, safety and security review.
