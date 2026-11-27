# Initial Project Risk Register

| ID | Risk | Current status | Required control / next action |
|---|---|---|---|
| R-01 | No qualified clinical reviewer yet recorded | Open | Identify and engage a relevant clinician before clinical workflow/rule design. |
| R-02 | Intended use and DRAP classification not determined | Open | Obtain jurisdiction-specific regulatory assessment before clinical deployment or claims. |
| R-03 | No approved guideline/source register | Open | Identify current licensed sources and qualified reviewer; record versions. |
| R-04 | Local Ollama has no registered models | Confirmed at M0 | Do not rely on local inference; select and benchmark a model at M6. |
| R-05 | Docker availability not confirmed on workstation | Unknown | Do not make Docker a local M0 prerequisite; validate later for target deployment. |
| R-06 | Windows workstation and free disk constrain heavy local services | Needs measurement | Check machine resources before installing databases, models or containers. |
| R-07 | PHI could leak to logs, external model providers or coding assistants | Open | Synthetic-only development; data-flow map, provider review, redaction and access controls. |
| R-08 | Cross-tenant or role authorization failure | Open | Threat model and negative authorization tests before patient data support. |
| R-09 | Prompt injection or unsupported AI output | Open | Treat retrieved content as untrusted; restrict tools; validate citations and abstain. |
| R-10 | Competitor/vendor claims mistaken for independently verified facts | Open | Keep source URL, access date, claim owner, evidence type and confidence in research register. |
| R-11 | Prior-employment or third-party IP/licence conflict | Must be checked | Clean-room development; review applicable obligations and dependency/model licences. |
| R-12 | Scope expansion into full HIS or autonomous agents | Ongoing | Keep the first release to one clinician-facing workflow; record scope changes. |

Review this register at each milestone. Add owner, severity, likelihood, due date and residual risk when the risk assessment process is established.
