# Clinical Safety Plan

This is a prototype planning document, not a clinical safety case or approval to use the system in patient care.

## Governance required before clinical rules
- Name a qualified clinician with relevant primary-care expertise to review intended use, workflow, source selection, rules, test cases and user interface.
- Define accountable clinical safety ownership and escalation.
- Maintain a hazard log with hazard, cause, foreseeable sequence, severity, likelihood, mitigation, verification evidence, residual risk and owner.
- Review applicable DRAP and other jurisdiction-specific medical-device/software requirements with qualified regulatory expertise. The product's legal classification is not determined by this repository.

## Clinical knowledge controls
- Use only approved, current, appropriately licensed clinical sources.
- Record publisher, jurisdiction, title, publication/effective date, version, URL, access date, reviewer and next review date.
- Rules must be explicit, deterministic, versioned and approved by a clinician before implementation.
- Specify units, thresholds, exclusions, missing-data behavior, conflicting-data behavior and expiry/review triggers.
- Never allow a language model to silently create, change or execute clinical rules.

## Human factors and workflow
- Make intended users, intended use and limitations visible.
- Show provenance, missing data, uncertainty, stale values and conflicting facts.
- Require explicit clinician review and action; maintain accept/edit/reject history.
- Design against automation bias, alert fatigue, ambiguous labels and misleading visualizations.

## Evaluation
- Begin with synthetic cases and clinician-approved expected results.
- Include normal, boundary, missing, stale, conflicting, unit-conversion, out-of-scope and adversarial cases.
- Measure clinically meaningful errors, including dangerous false negatives, unsupported statements, citation correctness and inappropriate non-abstention.
- Report limitations and unresolved hazards. A 100-case or larger synthetic benchmark is not proof of safety or clinical effectiveness.

## Stop conditions
No real patient data or live clinical recommendations until the intended use, clinical governance, hazard controls, security/privacy, regulatory position, institutional authorization, training and operational monitoring are approved for the specific deployment.
