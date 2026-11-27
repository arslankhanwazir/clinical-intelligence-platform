# Development Tools and AI-Agent Workflow

## Source of truth
Git repository, reviewed issues, architecture decision records (ADRs), tests and approved documentation are the source of truth. Chat conversations and AI-generated plans are not authoritative specifications until reviewed and committed.

## Core engineering tools
- **VS Code:** primary editor and terminal.
- **Git:** version history; feature branches for changes; reviewed commits.
- **Python + FastAPI:** backend and API.
- **Node.js + Next.js + TypeScript:** web application.
- **PostgreSQL:** intended relational datastore; configure only when the data-model milestone begins.
- **OIDC / Keycloak evaluation:** identity architecture; do not build a custom authentication system.
- **pytest / Playwright:** API, unit, integration and browser tests.
- **Figma / FigJam:** approved design system, flows and screen specifications before frontend build.
- **Ollama:** optional local model runtime. Current `ollama list` returned no models; do not assume local inference is ready.

## AI coding assistants: controlled roles
- **Claude Code:** primary implementation assistant for a bounded task, when available. It is the only agent allowed to write to that task's working tree.
- **Google Antigravity:** independent plan/code review or a separate task in a separate worktree/branch; never simultaneous writes to the same files.
- **Cursor:** editor and alternative coding/review assistant. Do not let it and Claude Code modify the same working tree concurrently.
- **Grok:** adversarial review / test-case critique where available; its output is a suggestion, not an authority or source of truth.
- **Human project owner:** approves scope, merges code, reviews dependencies/licences, checks test evidence and makes release decisions.

Use only tools actually installed and available. Do not send patient data, secrets, credentials, private keys, confidential third-party material or unapproved source documents to any assistant or external model. Use synthetic examples only.

## Task protocol
1. Create a small issue with scope, non-goals and acceptance criteria.
2. Create a feature branch or isolated worktree.
3. Assign one coding agent as the sole writer; provide only the necessary repository context.
4. Require tests and a summary of changed files, assumptions, dependencies and risks.
5. Have a different tool/person review the diff and test plan without modifying the same working tree.
6. Run tests locally; inspect the diff and dependency licences.
7. Human approves and commits. Record material decisions in an ADR.

## No-agent rules
No agent may commit directly to main, access production systems, provision cloud resources, change secrets, use real patient information, make clinical decisions, or declare compliance/certification. Never accept a generated clinical rule without qualified clinician approval.
