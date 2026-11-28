# ADR-0002: Central identity with OIDC and server-side authorization

**Status:** Proposed for M3 review.
**Date:** 28 November 2026.

## Context

The platform needs authenticated users, privileged MFA, clear role separation and patient/site/tenant-level authorization. Identity provider roles alone cannot enforce every resource-level rule.

## Decision proposal

- Use Keycloak as the initial OIDC identity-provider candidate, subject to deployment and maintenance review.
- The API validates issuer, audience, signature, expiry and required authentication context.
- The API remains the authorization enforcement point and applies RBAC + ABAC on every protected operation.
- Enforce privileged MFA and session expiry/revocation policy.
- Derive active tenant/site membership server-side; do not trust client-supplied tenant headers or record IDs.
- Default-deny unknown role, attribute, policy or missing identity context.

## Consequences

- Identity-provider configuration and application authorization policy need separate tests.
- Every patient/encounter endpoint must have object-level authorization tests.
- Role mapping and break-glass policy require institution review.
- Keycloak is a selected candidate, not yet installed, configured or security-validated.

## Revisit when

A deployment requirement, supported identity provider, institutional SSO policy or security review changes the choice.
