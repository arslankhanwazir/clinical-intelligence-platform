# M3 - Deployment topology decision proposal

**Status:** Proposed design decision for review; no hosting provider or production environment has been selected.

## Environments

| Environment | Data allowed | Hosting boundary | Purpose |
|---|---|---|---|
| Developer workstation | Synthetic fixtures only | Local F: workspace; local services only | Development and unit tests |
| CI | Source code, test fixtures and synthetic data | GitHub Actions with scoped secrets | Build, tests, scans and artefact creation |
| Public marketing / demo | Synthetic data only | Static/public web hosting may be used after review | Product explanation and safe interactive demonstration |
| Customer pilot | Only after approvals | Customer-controlled single-site Linux on-prem or approved private cloud | Supervised, approved workflow |

## Proposed first pilot topology

- Begin with a single customer/site deployment to limit the initial isolation problem.
- Keep the application API, database, audit storage and model gateway inside the customer-controlled or explicitly approved environment.
- The first integration is a narrow read/import path; no chart write-back.
- Local/private inference is the default direction for any later sensitive data path. A model provider is not selected or approved yet.
- Backups are encrypted; key ownership, recovery access and retention are defined with the customer before deployment.
- Monitoring exports service-level metadata only; clinical content is excluded from standard logs.
- Remote support is disabled by default for PHI access. Any approved support access is time-bound, least-privilege, reason-coded and audited.

## Public cloud / website boundary

- Public website and public demo may contain marketing material and synthetic cases only.
- Do not send patient data, clinical records, real screenshots, credentials or identifiable clinical events to public hosting, Figma, analytics or coding tools.
- Any private-cloud hosting of PHI requires provider due diligence, contractual/privacy review, residency/transfer review, key-management design and institution approval first.

## Explicitly deferred

- Multi-tenant shared SaaS deployment.
- Production region/provider selection.
- External LLM API for patient content.
- Cross-site data aggregation.
- Mobile apps, patient portal and EHR write-back.

## Go/no-go conditions

No production deployment until intended use and regulatory route are assessed, a site approves the data flow and contracts, security testing is complete, backup/restore and incident plans are tested, access controls are verified, and clinical/safety gates are met.
