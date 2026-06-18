# Governed Checkpoints Protocol

Status: core protocol.
Purpose: define how HIRMOS surfaces user-facing checkpoints without heavy output-contract machinery.

Governed checkpoints are user-facing outputs that can affect continuation. They must be concise for the active interaction mode and backed by existing session artifacts.

## Required rule

HIRMOS must not surface a checkpoint that claims a decision, readiness state, artifact availability, implementation authorization, evidence result, or close/update readiness unless the claim is backed by existing non-placeholder session artifacts and current `SESSION_EXECUTION.md` controls.

## Checkpoint types

Use these baseline checkpoint types:

```text
NEEDS_USER_DECISION
IMPLEMENTATION_READINESS
IMPLEMENTATION_COMPLETE
UPDATE_SYSTEM_STATE_READINESS
BLOCKED_FAIL_CLOSED
REQUEST_NOT_GOVERNABLE
STATUS_ONLY
```

## Required checkpoint inputs

Before surfacing a governed checkpoint, verify and record in `SESSION_EXECUTION.md`:

- checkpoint type;
- active lifecycle boundary;
- interaction mode;
- backing artifacts;
- relevant execution controls and statuses;
- unresolved-item status;
- user action required, if any;
- terminal state or next allowed action.

## Required checkpoint artifact

For checkpoints that request a user decision, claim implementation-readiness, claim implementation completion, claim update-state readiness, or fail closed, instantiate a checkpoint artifact using:

```text
_hirmos/core/templates/session/checkpoints/CHECKPOINT.md
```

Recommended active-session path:

```text
_hirmos/session/checkpoints/CHECKPOINT_<checkpoint-id>.md
```

Status-only command output may be read-only and does not require a checkpoint artifact unless it changes continuation state.

## Domain Expert rendering

In `domain_expert` mode, the checkpoint should show only:

- what HIRMOS understood or completed;
- what HIRMOS needs from the user, if anything;
- the recommended baseline when safe;
- important assumptions being carried;
- technical review pointer when relevant;
- what happens next;
- how to change, stop, or ask for details.

Do not expose execution-control tables, capability routing, or internal diagnostics by default.

## Technical Supervisor rendering

In `technical_supervisor` mode, include artifact pointers, assumptions, risks, validation/evidence status, and implementation/readiness implications.

## Framework Diagnostics rendering

In `framework_diagnostics` mode, include lifecycle boundary, capability routing, execution controls, unresolved classification, route-back triggers, and validation details.

## Unresolved-item checkpoint rule

A checkpoint that asks for user input must be sourced from `_hirmos/session/unresolved-items.md` when the input concerns decisions, assumptions, risks, scope, blockers, or continuation.

Gated items must be surfaced before they block Design, Implementation, implementation-readiness, Update System State, or close.

Non-gating assumptions may be carried only when the assumption, risk, scope, owner/source, and revalidation point are recorded in `_hirmos/session/unresolved-items.md`.

## Checkpoint completion

A checkpoint is complete only when:

- checkpoint artifact exists when required;
- `SESSION_EXECUTION.md` Checkpoint Log references it;
- execution controls reflect the checkpoint terminal state;
- unresolved-item dispositions affected by the checkpoint are recorded;
- the user-facing output does not claim more than the artifacts support.


## Production readiness checkpoints

When HIRMOS approaches production-readiness or release-readiness, a governed checkpoint must include material runtime integration status.

The checkpoint must be backed by `_hirmos/session/support/runtime-integration-readiness.md` when material integration areas exist.

In `domain_expert` mode, the checkpoint should surface:

- current implementation level in plain language;
- HIRMOS primary recommendation for each material production choice;
- alternatives and when an engineer might choose them;
- decision owner;
- blockers, credentials, accounts, compliance, or ownership items;
- whether the app is production-ready, locally real only, boundary-only, fixture/demo-backed, or blocked.

Do not expose the internal taxonomy unless needed; do not hide limitations when readiness is claimed.

## Claim reconciliation checkpoint rule

A governed checkpoint that claims readiness, implementation completion, runtime readiness, production readiness, update-state readiness, or close success must cite claim reconciliation evidence.

If claim reconciliation downgrades the claim, the checkpoint must surface the downgraded truthful claim instead of the original stronger claim.

## Autonomous technical decision checkpoints

A governed checkpoint must surface autonomous technical decisions when they become material to continuation, implementation authorization, technical review, production readiness, or release readiness.

Use `_hirmos/session/support/technical-review.md` as the backing artifact for technical decisions and `_hirmos/session/support/runtime-integration-readiness.md` for material integration posture.

In `domain_expert` mode, summarize only:

- the decision HIRMOS made or recommends;
- why it is safe or why it needs review;
- what remains blocked before production readiness;
- one primary next action.

In `technical_supervisor` mode, include alternatives, evidence, risks, and review triggers.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.
