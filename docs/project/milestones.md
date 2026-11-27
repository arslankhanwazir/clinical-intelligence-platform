# Delivery Milestones and Execution Gates

This is the controlling execution sequence. Milestones are completed by evidence and acceptance criteria, not by dates alone. A milestone may be blocked. Do not bypass a clinical, privacy, security, or regulatory gate to meet a schedule.

## M0 — Independent foundation
**Tools:** Windows CMD, Git, private GitHub repository when ownership/access is confirmed, VS Code. Use Claude Code as the primary implementation assistant only after the repository baseline is committed; use other assistants for review, not simultaneous writes.

**Work:** establish clean-room ownership boundaries; inspect applicable prior-employment, invention-assignment, confidentiality, and third-party licence obligations; confirm the new project has no imported confidential assets; establish repository structure, policies, decision log, risk register, and agent workflow.

**Exit evidence:** reviewed README/security/product/architecture documents; `.gitignore` checked; no secrets or patient data; project ownership and contributor process recorded; first baseline commit exists. Legal obligations must be reviewed by the relevant parties/adviser where needed; this project record is not legal advice.

## M1 — Clinical scope and intended use
**Tools:** clinician workshops/review (qualified clinician required), Figma/FigJam for workflow maps, official regulator and guideline publications, requirements register.

**Work:** define user roles, setting, patient population, inputs, outputs, exclusions, workflow, foreseeable misuse, source licensing, and clinical owner. Obtain qualified review of the proposed hypertension follow-up workflow. Determine applicable DRAP and other regulatory requirements before clinical deployment.

**Exit evidence:** signed-off intended-use statement and workflow; named clinical reviewer; approved source list and version policy; documented regulatory assessment/next action; initial hazards and exclusions. No rules are encoded before clinical review.

## M2 — Security architecture and threat model
**Tools:** architecture diagrams, STRIDE-style threat modelling, OWASP ASVS/API/LLM guidance, NIST CSF 2.0 mapping, GitHub security features where available, Gitleaks or equivalent local secret scanning.

**Work:** define trust boundaries, assets, attacker scenarios, identity lifecycle, OIDC, RBAC+ABAC, MFA for privileged users, tenant isolation, key/secrets handling, audit integrity, backup/restore, logging, incident response, AI prompt-injection and data-leakage controls.

**Exit evidence:** threat model and mitigations reviewed; authorization matrix; tenant-isolation test plan; data-flow and retention map; security requirements linked to tests. Controls are not called implemented until tested.

## M3 — Synthetic domain model and API skeleton
**Tools:** Python, FastAPI, Pydantic, pytest, OpenAPI; PostgreSQL planned for integration. SQLite may be used only for isolated early tests if it does not hide PostgreSQL-specific behavior.

**Work:** model synthetic patients, encounters, observations, medication statements and provenance; implement validation and missing/conflicting/stale-data detection. Keep tenant and access checks server-side.

**Exit evidence:** documented schemas and API contracts; synthetic fixtures; unit/integration tests; no real patient information; negative authorization tests.

## M4 — Deterministic clinical rules
**Tools:** Python rule module, version-controlled rule packs, pytest, clinician-reviewed test cases.

**Work:** represent only clinician-approved rules with explicit inputs, units, thresholds, exclusions, missing-data handling, version and effective date. The language model must not invent or silently modify rules.

**Exit evidence:** clinical sign-off for each rule pack; boundary, unit-conversion, missing/conflicting-data and regression tests; traceable rule version in every result.

## M5 — Evidence registry and retrieval
**Tools:** controlled source registry, document parsing, PostgreSQL; evaluate pgvector only after a retrieval benchmark; source/version metadata and citation tests.

**Work:** ingest only approved, licensed sources; record publisher, title, URL, publication/effective date, version, jurisdiction, review date and allowed use; retrieve passages with exact source references; expire or flag stale sources.

**Exit evidence:** source approval process; reproducible ingestion; citation/provenance validation; stale-source handling; no unsupported evidence presented as authoritative.

## M6 — AI orchestration and verification
**Tools:** model-provider interface, Ollama only after a model is installed and benchmarked, structured output validation, pytest; optional external models only after privacy and contractual review.

**Work:** use the model to summarize context and draft explanations within a constrained schema. Keep clinical rules deterministic. Validate references, detect unsupported claims, abstain when data/evidence is insufficient, and prevent unrestricted tool or write access.

**Exit evidence:** model/version recorded; structured-output and prompt-injection tests; citation checker; abstention tests; sensitive-data leakage tests; no automatic diagnosis, prescribing, or finalization.

## M7 — Clinical workspace and interaction design
**Tools:** Figma/FigJam for approved design system and flows; Figma Make for prototypes if useful; Next.js + TypeScript for production UI; Playwright for browser tests; accessible charting and component libraries chosen after design review.

**Work:** implement role-aware workspaces, patient/encounter timeline, missing/conflicting-data panel, evidence references, deterministic rule results, Evidence Ledger, and clinician accept/edit/reject workflow. Use glass/3D effects only as restrained visual treatment; clinical readability and accessibility take priority.

**Exit evidence:** usability review with clinicians; keyboard and responsive checks; role-based UI tests backed by server authorization; no fake clinical metrics or synthetic data presented as real.

## M8 — Safety, security and quality evaluation
**Tools:** pytest, Playwright, API/security test suite, Gitleaks or equivalent, dependency/SBOM tooling, OWASP ZAP in an isolated test environment, clinician-reviewed synthetic benchmark.

**Work:** test clinical correctness against approved expected results; measure citation accuracy, unsupported statements, missing-data detection, conflict handling, abstention, dangerous false negatives, repeatability, authorization, tenant isolation, rate limits, backup recovery and audit integrity.

**Exit evidence:** reproducible evaluation report with limitations and unresolved hazards; remediation of release-blocking findings; independent security review appropriate to the risk. A small synthetic benchmark is not proof of clinical safety.

## M9 — Customer-controlled deployment prototype
**Tools:** Linux deployment target, PostgreSQL, OIDC provider (evaluate Keycloak), encrypted storage, managed secrets, monitoring, backup/restore automation, infrastructure-as-code after deployment needs are known. Docker is optional for the current workstation, not a prerequisite for M0.

**Work:** build installation, upgrade, rollback, offline/limited-connectivity behavior, tenant separation, operations and support procedures. Keep patient processing in customer-controlled infrastructure unless a separately reviewed hosting model is approved.

**Exit evidence:** repeatable install; security configuration; restore drill; upgrade/rollback test; operational runbook; privacy and hosting review.

## M10 — Controlled pilot-readiness review
**Tools:** release checklist, clinical governance review, security assessment, regulatory counsel/authority engagement as applicable, training and monitoring plan.

**Work:** assess intended use, clinical evidence, usability, safety hazards, regulatory position, privacy, security, support, incident response, contracts and institutional permissions.

**Exit evidence:** documented go/no-go approval by the responsible clinical, security, regulatory and institutional stakeholders. This milestone is pilot readiness only; it is not automatic permission to deploy or provide care.

## Global stop conditions
Stop progression if real patient data enters an unapproved environment, a serious security issue remains unresolved, a clinical rule lacks qualified approval, an evidence source is unlicensed/unverified, or the regulatory/intended-use position is unclear for the proposed activity.
