# ADR-0004: Append-only, tamper-evident audit event path

**Status:** Accepted by product owner as a design decision; implementation and independent verification pending.
**Date:** 28 November 2026.

## Context

Security-sensitive access, imports, policy decisions, evidence/rule/model versions and human review actions need attributable audit records.

## Accepted design decision

- Use a dedicated append-only audit write path separate from normal application update/delete permissions.
- Record actor, tenant/site, action, target reference, timestamp, outcome, correlation ID and relevant source/rule/model/prompt versions and artefact hash, while minimizing unnecessary clinical payload.
- Restrict audit read access; separate operational administrators from audit reviewers where feasible.
- Add integrity verification (for example, chained event hashes and periodic protected checkpoints) and alert on gaps or validation failures.
- Back up audit data under separate credentials and test restore.
- Treat `tamper-evident` as the design goal; do not claim `tamper-proof` or compliance until independently tested.
- Required audit failure blocks the associated attestation/finalization action.

## Consequences

- Audit schema and event taxonomy must be versioned.
- Retention and key-management duration must be decided with institution and legal/privacy review.
- Logs must not become a secondary uncontrolled copy of PHI.
