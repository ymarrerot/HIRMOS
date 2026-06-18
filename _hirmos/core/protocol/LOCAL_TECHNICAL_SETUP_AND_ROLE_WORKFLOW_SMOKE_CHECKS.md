# Local Technical Setup and Role-Workflow Smoke Checks Protocol

Status: core protocol.
Purpose: require truthful evidence for local setup and role workflow behavior without turning smoke testing into heavy QA bureaucracy.

## Core rule

HIRMOS must distinguish these evidence levels:

- project compiles;
- automated tests pass;
- local technical setup works;
- the app runs locally;
- each material role workflow was exercised;
- the user's environment was verified;
- production readiness was verified.

Build, lint, typecheck, and unit tests are useful evidence. They do not prove local setup, role workflow behavior, user-environment readiness, provider delivery, or production readiness.

## Local technical setup evidence

When implementation depends on local services or runtime configuration, HIRMOS must record setup evidence before claiming local runtime readiness.

Examples:

| Area | Evidence to record when applicable |
|---|---|
| Package manager | install command, result, lockfile status, dependency failures |
| Environment files | env example reviewed, env file created/updated/redacted, missing secrets |
| Database | service detected or not, connection string, database exists/created, migration result, seed result |
| Auth | secret present/redacted, callback/base URL, login route exercised |
| Provider adapters | credentials present/redacted/missing, dev fallback behavior, production blocker |
| Dev server | command, port, route response, server crash or success |
| Browser route | URL exercised, expected response, observed failure |

## Safe local setup attempts

When safe, in scope, and non-destructive, HIRMOS should attempt local technical setup before deferring it.

Allowed examples:

- inspect scripts and env examples;
- run install/build/test/lint commands when appropriate;
- check whether a local database service is reachable;
- create a local development database when clearly safe and authorized by scope;
- run migrations and seed against local development database;
- start the dev server and verify routes when environment permits;
- fix local setup problems encountered during authorized work.

Blocked without explicit approval:

- destructive database reset against unknown/non-dev data;
- production credential use;
- paid-provider account actions;
- compliance/legal decisions;
- irreversible production-like migrations;
- changing domain behavior silently.

Firm rule: attempt safe local progress; ask only when user-owned risk, credentials, cost, compliance, destructive action, or domain behavior is involved.

## Role-workflow smoke checks

When a session implements or claims role-based functionality, HIRMOS must record role-workflow smoke evidence before claiming workflow readiness.

A smoke check is not full QA. It is a minimal role-based proof that the workflow was exercised or explicitly not exercised.

For each material role, record:

- role;
- credential or access method used, with secrets redacted;
- route or workflow exercised;
- expected result;
- observed result;
- evidence state from `support/claim-reconciliation.md`;
- limitations or blockers.

For the healthcare MVP pattern, likely roles include patient, front-desk staff, provider, clinic manager, and platform/admin when applicable.

## Claim rules

HIRMOS may claim `LOGGED_COMMAND_PASSED` for build/test/lint only when logged.

HIRMOS may claim `LOCAL_RUNTIME_VERIFIED` only when the app/server/route/workflow was actually exercised and recorded.

HIRMOS may claim `USER_ENVIRONMENT_VERIFIED` only when the user's environment was verified or the user supplied observed evidence.

HIRMOS may claim role workflow readiness only for workflows with smoke evidence or explicit limitations.

## Artifact requirements

Use:

- `_hirmos/session/support/local-runtime-evidence.md` for local setup evidence;
- `_hirmos/session/support/role-workflow-smoke.md` for role workflow smoke evidence;
- `_hirmos/session/support/claim-reconciliation.md` for claim status;
- `_hirmos/session/support/evidence-review.md` for aggregate evidence review;
- `_hirmos/session/support/session-implementation-review.md` for implementation completion decision.

Firm rule: do not say “the app works locally” or “role workflows are verified” unless the corresponding evidence artifact supports that exact claim.

## Mandatory role-smoke artifact instantiation

If a session implements role-based workflows, modifies role-based routes, or claims workflow readiness for any role, HIRMOS must instantiate `_hirmos/session/support/role-workflow-smoke.md`.

The artifact is required even when smoke checks are not run. In that case, each material workflow must be recorded with canonical evidence state `NOT_RUN`, `BLOCKED`, or `NOT_APPLICABLE` and a limitation/carry-forward note.

Do not bury missing role-smoke evidence only in `CARRY_FORWARD.md`, `support/claim-reconciliation.md`, or chat output. Those artifacts may reference the limitation, but `support/role-workflow-smoke.md` is the owning workflow-smoke evidence artifact.

Firm rule: role workflow readiness is not claimable when `support/role-workflow-smoke.md` is missing for in-scope role workflows.

## Close-time local setup and role-workflow materialization

Before normal close, local setup and role-workflow evidence must be materialized in their owning artifacts when their triggers are present.

Local setup trigger examples:

- local database, migration, seed, dev server, route, auth, provider, callback, webhook, API, environment variable, or user-environment verification claim;
- app works locally / local runtime readiness claim;
- generated package/report claims local setup has been completed.

Role-workflow trigger examples:

- role, actor, approval gate, user journey, dashboard workflow, agent callback workflow, or retry workflow readiness claim;
- any claim that a user can complete a material app workflow without inspecting raw database records;
- smoke test or manual workflow verification claim.

If a trigger exists, close must instantiate the relevant owning artifact even when checks were not run. Use canonical evidence states such as `NOT_RUN`, `BLOCKED`, or `NOT_APPLICABLE`, with rationale and carry-forward pointers.

Firm rule: a missing owning evidence artifact is a close blocker, not a carry-forward-only note.

## Cross-run test and smoke quality lesson

When comparing multiple implementation candidates, HIRMOS must distinguish smoke-test breadth from smoke-test strength.

A smoke script is weak when it only proves that collections exist, counts are greater than or equal to zero, or routes are present without checking business-critical outcomes.

For workflow-heavy apps, role/workflow smoke checks should prefer meaningful assertions such as:

- required human approval gate blocks unsafe transition;
- agent output creates an artifact but does not directly approve material state;
- failed agent job becomes visible and retryable;
- state transition creates an audit event;
- dashboard attention item appears for the relevant blocked/approval/deadline condition;
- submission, award, invoice, or closeout actions require required data and rationale when applicable.

Firm rule: test breadth can be salvaged from another candidate, but workflow-readiness claims require meaningful assertions tied to requirement IDs, not only broad route execution.
