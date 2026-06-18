# Runtime integration and production readiness

HIRMOS should not silently treat a fixture-backed demo as a production-ready implementation.

For Domain Expert users, HIRMOS keeps this simple: it uses safe local defaults when appropriate and surfaces low-level integration choices only when they affect domain behavior, risk, cost, compliance, ownership, implementation authorization, or production readiness.

Underneath, HIRMOS tracks the current implementation level for material areas such as database, authentication, messaging, storage, deployment, and provider APIs.

Before claiming production readiness, HIRMOS must surface:

- current implementation level;
- HIRMOS primary recommendation;
- alternatives;
- why the recommendation fits;
- decision owner;
- technical-review path;
- blockers before production readiness.

A passing build is not enough to prove production readiness. Real runtime behavior and provider readiness require specific evidence.

## Canonical runtime posture values

Runtime integration posture fields use only the canonical posture values from `RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`. Do not use shorthand such as `LOCAL_REAL`, `provider-ready`, or `production ready pending credentials` in posture fields.
