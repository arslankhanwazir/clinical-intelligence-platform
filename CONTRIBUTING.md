# Contributing and change control

This repository is an independent clinical decision-support product. Its documents, code, test data and Git history are the project record.

## Work unit
- Every change must have a GitHub Issue or an explicitly recorded task, a named owner, acceptance criteria and evidence of review.
- One coding agent or human author owns modifications to a working tree at a time. Other agents may review read-only or work in separate branches/worktrees.
- The human project owner reviews every diff and command before merge or deployment.
- Do not merge unfinished or unreviewed clinical-scope, safety, security, identity, tenant or data-flow changes.

## Branch and pull-request practice
- Keep `main` as the protected integration branch when the repository plan supports protection.
- Work in a short-lived branch named `docs/...`, `feature/...`, `fix/...` or `security/...`.
- Use a pull request for changes to `main` wherever GitHub branch rules are available.
- Do not force-push shared branches or rewrite published history without a documented recovery decision.
- Keep commits small and use descriptive messages.

## Clinical change control
- No clinical thresholds, medication advice, diagnostic criteria, escalation pathways or rule logic may be invented by a developer or AI agent.
- Clinical rules require an identified qualified reviewer, approved jurisdiction-specific source, source/version record, documented exclusions, clinician approval, tests and a controlled release record.
- A language model is not a clinical approver, policy engine, permission engine or audit authority.
- Clinical output remains a draft for qualified clinician review. No autonomous diagnosis, prescription, medication order or silent chart write-back is in v1 scope.

## Data and security
- Synthetic data only until applicable clinical, regulatory, privacy, institutional and security gates are approved.
- Never commit patient information, credentials, keys, tokens, private documents or third-party confidential material.
- Do not send patient data, credentials or private customer documents to coding agents or public model APIs.
- Report suspected secrets or vulnerabilities privately; rotate any exposed credential immediately. Removing a secret from the latest file does not remove it from Git history.

## Third-party and clean-room rules
- Use independently created materials and properly licensed public materials only.
- Record third-party package, model, guideline and data licences before adoption.
- Do not copy or reconstruct confidential code, prompts, documents, datasets, architecture or customer information from a competitor, former employer or partner.

## Before requesting review
- [ ] Acceptance criteria are met.
- [ ] Relevant tests and checks are included or their absence is explained.
- [ ] No secrets or real patient data are included.
- [ ] Clinical claims have approved sources and reviewer status, or are clearly marked as unapproved drafts.
- [ ] Docs, risk register and source/version records are updated where relevant.
- [ ] The diff has been reviewed by the author and project owner.
