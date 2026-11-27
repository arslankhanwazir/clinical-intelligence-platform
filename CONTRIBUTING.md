# Contributing to NORTHSTAR

NORTHSTAR is an independent, private clinical-intelligence project. Contributions must preserve its security, privacy, clean-room and clinical-safety boundaries.

## Current repository policy
- Keep the GitHub repository private.
- GitHub Free does not provide server-enforced branch protection for this private repository. Until an eligible plan or supported protection mechanism is available, follow the manual policy below.
- Do not commit directly to `main`. Create a short-lived feature branch for each change.
- Review the complete diff and run the relevant checks before merging.
- Use a pull request for every change where GitHub permits it; the sole maintainer must review their own change before merging and record that limitation. Add an independent reviewer before accepting external contributions.
- Never force-push to `main`, rewrite shared history, or delete the default branch.

## Data and security
- Synthetic data only during prototype development. Do not commit real patient data, PHI, credentials, tokens, private keys or secrets.
- Run the configured Gitleaks workflow and resolve findings before merging.
- Report suspected vulnerabilities privately; do not publish exploit details or sensitive data in public issues.

## Clean-room and licensing
- Contribute only material you are authorized to use and that has a reviewed licence or clear ownership basis.
- Do not submit confidential third-party or former-employer code, prompts, documents, datasets, customer information, trade secrets or protected UI.
- Record dependency, model, dataset and asset name, source, version and licence before adoption.
- Obtain appropriate written contributor/IP terms before accepting substantive external contributions.

## Change quality
- Keep changes small and focused; document material architecture, security, model, evidence and clinical-scope changes.
- Add or update tests for implemented behaviour. Do not describe unimplemented controls as operational.
- Do not introduce clinical rules, diagnosis, treatment recommendations or live patient workflows without the required clinical and regulatory approvals.
