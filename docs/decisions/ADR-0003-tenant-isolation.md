# ADR-0003: Single-customer deployment for the first pilot; tenant-aware design

**Status:** Accepted by product owner as a design decision; implementation and independent verification pending.
**Date:** 28 November 2026.

## Context

Cross-tenant data leakage is an unacceptable design risk. The first pilot should avoid unnecessary shared-SaaS complexity while preserving tenant/site scope in the application model.

## Accepted design decision

- Target one customer/site deployment for the first controlled pilot, pending institutional approval.
- Persist tenant and site identifiers on relevant records and audit events even in a single-customer installation.
- Enforce tenant/site scope in API services and database access; do not rely on frontend filtering.
- Add negative tests for cross-tenant and cross-site requests before any multi-site or shared deployment.
- Do not enable shared multi-tenant SaaS until a separate architecture/security review approves isolation, operations, backup and key boundaries.

## Consequences

- First deployment is simpler to isolate and support.
- Future multi-tenant hosting may require schema, row-level security, separate databases or separate deployments; no choice is made without a threat and operational review.
- Tenant-aware code is still required from the start to avoid unsafe shortcuts.
