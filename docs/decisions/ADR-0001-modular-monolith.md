# ADR-0001: Start with a Modular Monolith

**Status:** Accepted for the initial prototype; subject to review.

## Context
Clinical scope and customer deployment requirements are not yet validated. Microservices and multi-agent orchestration would add operational and security complexity before there is evidence they are needed.

## Decision
Use one deployable API application with explicit modules for identity/authorization, patient and encounter context, deterministic rules, evidence retrieval, AI orchestration, verification and audit. Keep module contracts clear so components can be extracted later if justified.

## Consequences
- Simpler local development and deployment.
- Clear module boundaries and test ownership remain mandatory.
- Enforce authorization and tenant context consistently across modules.
- Extract a service only when scale, isolation, reliability or customer deployment requirements justify the additional operational cost.
