# M3 - Privacy impact assessment questions

**Status:** Question set only; no legal/privacy assessment completed. No real patient data is approved for development.

## Data inventory and purpose

- Which personal and health data elements are strictly necessary for the final intended workflow?
- Which direct identifiers can remain inside the customer environment and never enter the application model context?
- What are the sources of demographics, observations, medicines, allergies, encounter notes and imported records?
- What is the documented purpose for every collection, processing, model inference, export and audit event?
- Can the workflow operate with pseudonymous patient IDs and minimum necessary context?

## Roles and legal basis

- Who is the data controller, processor, service provider and subprocessor for each deployment model?
- What lawful basis, patient notice, consent or other authorization applies in each target institution and jurisdiction?
- Which professional, institutional, contractual, health-data and cybersecurity obligations apply?
- Who handles access, correction, deletion, complaints and data-subject requests?

## Data location and sharing

- Where do application data, audit logs, backups, telemetry and support records physically reside?
- Does any data cross provincial or national borders or reach a third-party model, observability, email, analytics or support provider?
- Which subprocessors receive data, under what contract, and can their access be disabled?
- Are FHIR/import connections read-only and limited to approved endpoints and fields?

## Retention and security

- What retention schedule applies to source records, derived context, drafts, audit events, logs, backups and model/evaluation artefacts?
- How are retention, legal hold, deletion, backup expiry and cryptographic key destruction handled?
- What encryption, key custody, access logging, breach response and recovery controls are mandatory at the site?
- Can operational monitoring work without clinical content? Which fields must be redacted?

## AI-specific privacy

- Which fields may be sent to an inference process, and which must be excluded or pseudonymized?
- Is inference local, customer-private or external? What contractual and transfer review is required before external inference?
- Are prompts/outputs retained by any model provider? Are they used for training? Can retention/training be disabled and verified contractually?
- Can Figma, issue trackers, coding agents, telemetry or crash reports receive any PHI? Default answer is no.
- Are secondary use, model training, research and cross-customer aggregation disabled unless separately authorized?

## Governance and incident handling

- Who approves new data fields, integrations, subprocessors, data exports and retention changes?
- Who is notified after an incident, in what timeframe, under which contract and law?
- Who can invoke break-glass access, how is it reviewed and how is it revoked?
- What evidence must be kept to demonstrate compliance and respond to audits?

**Required output before PHI:** a jurisdiction-specific privacy assessment, documented controller/processor roles, approved data-flow and retention schedule, contracts/permissions, and institutional security/privacy approval.
