# Validation and Evidence Protocol

Status: core protocol.
Purpose: define the minimum evidence discipline for trustworthy HIRMOS claims.

HIRMOS validation is based on:

```text
Execution Controls
+ Evidence Records
+ Boundary Reviews
+ Lightweight Static Validation
```

It does not require heavy runtime output-governance machinery by default.

## Core claim rule

HIRMOS must not claim progress, readiness, implementation-readiness, implementation completion, update-state-readiness, close readiness, validation success, or close success unless the claim is backed by existing artifacts, observed file state, command output, user decision, or explicit not-applicable rationale.

## Evidence vocabulary

Evidence must distinguish:

- `observed` — directly inspected in files, artifacts, command output, or user input;
- `inferred` — reasoned from observed evidence;
- `assumed` — carried without direct proof and recorded as an assumption;
- `unknown` — not known yet;
- `blocked` — cannot proceed without decision, repair, route-back, or evidence;
- `not_run` — command/check was not executed;
- `not_applicable` — check does not apply, with rationale.

## Evidence families

HIRMOS evidence includes:

- current-state evidence;
- Design evidence;
- Implementation evidence;
- Update System State evidence.

## Validation logs

When HIRMOS claims that a test, build, typecheck, lint, migration, or validation command ran, it must record:

- command;
- working directory;
- result;
- relevant output or log path;
- whether dependencies/environment were available;
- whether the result is reproducible from the current working copy.

## Boundary reviews

Before passing major boundaries, HIRMOS must review whether required controls and artifacts are ready for that boundary.

Boundary reviews include, when applicable:

- system-state readiness;
- Design readiness;
- implementation-readiness;
- implementation completion;
- update-state readiness;
- close readiness.

## Static validation

Static validation should check concrete framework and artifact properties first: required files exist, config values are valid, referenced installed stacks exist, session artifacts exist before being referenced, required controls are not unsatisfied at terminal boundaries, and archive paths preserve session evidence.


## Runtime integration evidence

When implementation, readiness, or close claims involve runtime integrations, evidence must identify the actual integration level delivered.

Record whether each material integration area is:

```text
DEMO_FIXTURE
INTEGRATION_BOUNDARY
LOCAL_REAL_INTEGRATION
PRODUCTION_PROVIDER_INTEGRATION
BLOCKED_PENDING_DECISION_OR_CREDENTIALS
NOT_APPLICABLE
```

Evidence must distinguish build/test success from local runtime verification and production-provider verification.

Examples:

- build success alone does not prove database runtime persistence;
- adapter code alone does not prove provider delivery;
- local database migration success does not prove production database readiness;
- console fallback does not prove real email/SMS delivery;
- missing credentials must be recorded as blocked, not silently treated as success.

HIRMOS must not claim production readiness until every material integration area has a production recommendation, accepted decision or review path, required credentials/environment disposition, and evidence or explicit blocker.

## Close and archive evidence

Close evidence must prove a state transaction, not merely a user-facing summary.

Required close evidence includes:

- `SESSION_EXECUTION.md` close/update control pointers accepted/rejected/evidence-only/carry-forward classification;
- `SESSION_EXECUTION.md` close controls close readiness and integrity checks;
- archive manifest under `_hirmos/system/history/sessions/<session-id>/`;
- current-state latest-close metadata and carry-forward updates;
- reset `SESSION_STATE.json` after normal close;
- post-close status expectation.

If these records disagree, close evidence is contradictory and HIRMOS must not claim normal close success.

## Claim reconciliation

When HIRMOS makes or prepares a material claim, it must apply `_hirmos/core/protocol/CLAIM_RECONCILIATION.md`.

Material claims include:

- implementation completion;
- validation success;
- local runtime readiness;
- integration readiness;
- production readiness;
- package completeness;
- update-state readiness;
- close success.

Evidence records must classify each claim as one of:

```text
NOT_CLAIMED
NOT_RUN
CLAIMED_NOT_LOGGED
LOGGED_COMMAND_PASSED
LOGGED_COMMAND_FAILED
LOCAL_RUNTIME_VERIFIED
USER_ENVIRONMENT_VERIFIED
PRODUCTION_READINESS_VERIFIED
BLOCKED
NOT_APPLICABLE
```

HIRMOS must downgrade or block claims that are unsupported, unlogged, contradicted by final files, or dependent on unavailable environment/credentials.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/EVIDENCE.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/EVIDENCE.md` records role-specific workflow smoke evidence for the relevant end-user, operator, privileged-user, and administrative paths.
- `_hirmos/session/EVIDENCE.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.
