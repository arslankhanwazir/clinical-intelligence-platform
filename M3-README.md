# NORTHSTAR M3 work package

This package applies the M3 Architecture & Security Design work described in `01_clinical_intelligence_milestone_plan.pdf` and the engineering decisions/stack in `02_clinical_intelligence_engineering_structure.pdf`.

## What is included

- System-context architecture and Mermaid diagram.
- Data-flow and trust-boundary diagram.
- Initial STRIDE threat model (not formally risk-rated).
- Preliminary roles/permissions matrix.
- Privacy-impact question set (not a legal assessment).
- Customer-controlled deployment proposal.
- ADRs for identity, tenant isolation, audit and model boundary.
- OWASP/NIST control reference map.
- Tool/agent workflow and M3 acceptance checklist.
- Corrected M0/M1/M2 status and M2 external action register.
- Product-owner architecture decision record.

## How to use

1. Review the Markdown documents and Mermaid diagrams.
2. Product owner records accept/change decisions in `m3-owner-decision-record.md`.
3. Do not mark M3 complete until its acceptance checklist is satisfied.
4. Do not enter real patient data, enable clinical rules/evidence or make clinical recommendations.

All architecture choices are proposals, not implemented controls. A qualified security reviewer and privacy/legal review remain necessary before any environment containing PHI is designed or hosted.
