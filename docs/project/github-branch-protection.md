# GitHub branch protection - `main`

Keep this repository private. Do not change it to public to obtain protection features.

## Configure when the GitHub plan allows it

1. Open `https://github.com/arslankhanwazir/clinical-intelligence-platform/settings/rules`.
2. Choose **New branch ruleset**.
3. Name it `protect-main` and target the default branch `main`.
4. Set enforcement to **Active**.
5. Enable **Require a pull request before merging**, **Restrict deletions**, and **Block force pushes**.
6. Do not require a second-person approval while the project has only one maintainer; add an independent reviewer when one is available.
7. After CI checks exist, require the relevant checks to pass before merging.

## GitHub plan limitation

Current GitHub documentation lists branch protection/rulesets for public repositories on GitHub Free, and for private repositories on GitHub Pro, Team and Enterprise. Confirm the plan attached to this personal account in GitHub billing/settings. If private-repository protection is unavailable, keep the repository private and record the limitation; use feature branches, pull requests where available, local review and no-force-push discipline until the plan permits enforcement.

## Evidence

Record the active ruleset URL or screenshot and date in `docs/project/m0-closeout.md` after configuration. A local Git convention is not the same as server-enforced branch protection.
