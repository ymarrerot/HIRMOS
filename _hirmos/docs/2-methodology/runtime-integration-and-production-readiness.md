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


## Production-shaped by default

HIRMOS now treats production-shaped implementation as the default posture for governed software work. This does not mean every session must deploy to production or use enterprise-grade infrastructure. It means the local implementation should preserve the architecture shape needed for production where practical.

Examples:

- use local PostgreSQL when PostgreSQL is the intended production database;
- use a persisted job/worker/cron shape for long-running AI or image work;
- make metered-state/billing mutations transactional, idempotent, or explicitly limited;
- keep secrets and runtime-generated files out of release or handoff packages.

If a session intentionally uses a prototype, fixture, demo-only, or local-only shortcut, the limitation must be authorized in the Session Scope and preserved at close.

## PROD-L8.22 Review Gate Salvage

HIRMOS preserves legacy evidence-backed review discipline through existing artifacts instead of restoring legacy review files.

Review gates must answer:

- What authority was reviewed?
- What evidence was reviewed?
- Was the final codebase or file state inspected?
- Does the evidence prove unit, session, phase, delivery, runtime, or production claims?
- What remains unproven?
- Why is the terminal state honest?

A passing static check is not a delivery review. A completed implementation unit is not a phase review. A phase review is not a delivery review unless cross-phase behavior and delivery-level acceptance posture are reviewed.
