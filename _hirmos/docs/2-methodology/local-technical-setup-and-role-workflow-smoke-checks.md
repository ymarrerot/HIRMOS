# Local Technical Setup and Role-Workflow Smoke Checks

HIRMOS favors autonomous technical progress, but it must not overclaim what was verified.

## Practical rule

Build and tests are useful. They do not prove the app works locally for real users.

Before claiming local runtime readiness, HIRMOS records setup evidence: environment files, local services, migrations, seed commands, dev server behavior, and route checks.

Before claiming role workflow readiness, HIRMOS records smoke checks for material roles and workflows.

## Why this exists

AI agents often say “implementation complete” after tests pass. Serious software work needs a clearer distinction:

- the code compiled;
- the database was reachable;
- migrations and seed ran;
- the dev server responded;
- a patient/staff/provider/admin workflow was exercised;
- the user's environment was verified;
- production readiness was verified.

## Domain Expert visibility

In Domain Expert mode, HIRMOS should not flood the user with setup details. It should surface blockers, meaningful limitations, and production-readiness decisions.

Technical Supervisor and Framework Diagnostics modes can inspect the detailed evidence artifacts.

## Missing smoke checks

When role workflows are in scope, `support/role-workflow-smoke.md` must exist even if smoke checks are not run. Use `NOT_RUN`, `BLOCKED`, or `NOT_APPLICABLE` for each workflow and carry forward the limitation.
