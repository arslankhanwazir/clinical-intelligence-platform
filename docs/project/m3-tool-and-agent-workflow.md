# M3 - Tool and engineering-agent workflow

**Status:** Working agreement aligned to the milestone plan and engineering blueprint.

## Human ownership

The project owner approves requirements, architecture decisions, repository changes, merges, deployments and security-sensitive actions. No agent is allowed to approve its own work.

## Tool roles

| Tool | Role | Guardrails |
|---|---|---|
| VS Code + Git | Local workbench and version control | Review every diff; use branches; no secrets or patient data in workspace |
| Claude Code | Primary implementation agent for a clearly scoped ticket after design acceptance | One active code owner per task; read-only audit first; inspect proposed commands and diffs |
| Cursor | Human-led editing, navigation, refactoring and second review | Do not make concurrent conflicting edits on the same files |
| Google Antigravity | Independent architecture/test review or isolated parallel task | Separate branch/worktree; no shared write ownership; review output before merge |
| Grok | Adversarial reviewer for design, requirements and test cases | Reviewer only; not a clinical authority, not a source of truth, no PHI/secrets |
| Figma FigJam / Design | Journey mapping and visual source of truth in M9 | Synthetic content only; no patient data; no direct copying of competitor assets |
| Excalidraw / Mermaid | Versionable architecture and trust-boundary diagrams in M3 | Keep source diagrams in Git and reconcile with approved architecture |
| GitHub Actions + Gitleaks | CI and secret scanning | Verify successful run and retain evidence; secret scan does not prove absence of all secrets |

## Task protocol

1. One ticket, one named owner, one branch/worktree.
2. Provide agents only public documentation, synthetic fixtures and the minimum files needed.
3. State acceptance tests before code changes.
4. Require a diff summary, tests run, failures, dependencies and security impact.
5. A separate reviewer inspects the diff; owner merges only after checks pass.
6. No agent receives real patient data, production credentials, private keys or confidential IHS/MindHYVE materials.
