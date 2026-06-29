# Runtime Integration and Production Readiness

HIRMOS separates implementation, local runtime evidence, and production readiness.

## Local runtime evidence

A session may prove that work runs locally through:

- build/test/lint output;
- local app startup;
- browser/user testing;
- API/provider smoke checks;
- fixture or scripted verification.

Local evidence is valuable, but it does not automatically prove deployment readiness.

## Production readiness

Production readiness requires evidence for the production-shaped system actually in scope. Depending on the project, that may include:

- deployed environment validation;
- durable storage and queues;
- authentication/security posture;
- payment/credit correctness;
- observability and failure handling;
- operational rollback/retry behavior.

If a session intentionally uses a prototype, fixture, demo-only, or local-only shortcut, the limitation must be authorized in the Session Scope and preserved at close.

## Honest close posture

Close should distinguish:

- accepted local MVP;
- accepted implementation but runtime not verified;
- partial close with carry-forward;
- production-ready outcome.

Do not collapse these into one “done” claim.


## Current implementation level

At every close, HIRMOS should state the current implementation level: design-only, implemented-not-runtime-verified, local-runtime verified, or production-ready with matching evidence.
