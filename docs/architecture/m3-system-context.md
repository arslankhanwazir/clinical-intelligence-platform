# M3 - System context and architecture proposal

**Status:** Proposed architecture for owner review; not implemented or security-approved.
**Scope:** NORTHSTAR / Clinical Intelligence Platform, V1 planning boundary.

## Product boundary from the approved planning PDFs

- Focused clinician-facing clinical intelligence / decision-support workflow; not a full HMIS or EHR replacement.
- Proposed first workflow: adult primary-care hypertension follow-up, still unvalidated because no clinic or clinician reviewer is available.
- Human clinician remains the decision-maker. The model cannot diagnose, prescribe, order medication, finalize a chart or write directly to an EHR.
- Initial development uses synthetic data only.

## Modular-monolith proposal

| Layer | Proposed component | Responsibility |
|---|---|---|
| Web workspace | Next.js App Router, TypeScript, Tailwind, shadcn/ui | Admin and clinician workspace; synthetic demo kept visibly separate |
| API | Python, FastAPI, Pydantic | Modular application API, validation, authorization and orchestration |
| Persistence | PostgreSQL, SQLAlchemy, Alembic | Transactional persistence and schema migrations; full-text search first |
| Identity | Keycloak / OIDC | Identity, session/token lifecycle and MFA capability; application still enforces authorization |
| Authorization | RBAC + ABAC in API, tenant/site context and object-level checks | Every protected action checks subject, role, tenant, site, patient relationship and purpose context as applicable |
| Patient context | Canonical, provenance-preserving domain module | Normalize permitted imported facts; preserve source, units and timestamps; surface gaps/conflicts |
| Clinical rules | Separate deterministic module | Disabled until M2 clinician-approved sources/rules exist |
| Evidence | Versioned source registry and retrieval | Disabled for clinical claims until M2-approved/licensed sources exist |
| AI gateway | Provider adapter; Ollama for synthetic local development when a model is actually available | Structured draft only; never authorization, policy, system-of-record or audit authority |
| Verification | Server-side schema/fact/citation/policy checks | Reject unsupported or malformed draft; abstain when required context is absent |
| Audit | Append-only, tamper-evident event store | Actor, tenant, action, source/rule/model versions, artifact hash and human-review result |
| Integration | Narrow FHIR R4 read/import adapter first | No EHR write-back in V1 |

## Data and trust boundaries

1. User device/browser to application/API boundary.
2. Application/API to identity provider boundary.
3. API to database boundary.
4. API to external customer EHR/HIS or import boundary.
5. API to approved evidence repository boundary.
6. API to model-provider boundary. External model calls are disabled for patient information unless privacy, contract, transfer and security approvals are obtained.
7. Application to audit storage/backup boundary.
8. Customer-managed deployment boundary versus public marketing/synthetic-demo hosting boundary.

## Architecture principles

- Server-side deny-by-default authorization; never trust tenant or patient identifiers supplied by the browser without policy checks.
- Tenant and site context is derived from authenticated membership and verified server-side.
- Minimum necessary data is passed to each component.
- Original source facts and provenance are preserved; normalized values never silently overwrite source values.
- Deterministic rule outputs are separate from generated prose.
- Every source, rule pack, model, prompt and draft is versioned where applicable.
- Audit failure on a required review/attestation path fails closed; it must not be silently discarded.
- No PHI in developer workstations, GitHub, Figma, public demo, ordinary logs or coding-agent context.
- Start as one deployable backend with clear modules; do not split into microservices without evidence.

## Not decided in M3

- Final regulatory classification, intended-use wording and clinical rules.
- Clinical guideline selection or numeric thresholds.
- Production hosting provider, region, contract, retention duration or lawful basis.
- Final database-per-customer versus schema/database tenancy details for future shared SaaS.
- Production model/provider or model fitness.

These require legal, institutional, clinical, security or deployment evidence.
