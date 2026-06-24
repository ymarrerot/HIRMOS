# Execution Control Governance Authority

Status: core authority.
Purpose: define the execution-control governance mechanism that makes HIRMOS execution trustworthy.

## Execution spine

The active session execution spine is:

```text
_hirmos/session/SESSION_EXECUTION.md
```

A governed HIRMOS session is not active until this file exists and records:

- session id;
- active command;
- active lifecycle boundary;
- required execution controls;
- current control statuses;
- evidence references;
- continuation state;
- route-back records when needed.

## Control statuses

Allowed statuses:

```text
PENDING
SATISFIED
BLOCKED
NOT_APPLICABLE
```

`PENDING` means the control is required and not yet satisfied.

`SATISFIED` means the control is required and is backed by evidence or artifact state.

`BLOCKED` means the control is required and cannot be satisfied without user action, route-back, repair, or missing evidence.

`NOT_APPLICABLE` means the control is not required for this request path and has a recorded reason.

## Blocking rule

HIRMOS must not claim progress, readiness, implementation-readiness, implementation completion, update-state-readiness, close readiness, or close success while any required control is `PENDING` or `BLOCKED`.

## Baseline controls

Every advancing command must establish relevant controls before claiming progress. Baseline control families include:

- bootstrap control;
- command control;
- working-copy control;
- interaction-mode control;
- lifecycle-boundary control;
- snapshot-backed checkpoint control;
- unresolved-item control when decisions or assumptions exist;
- validation/evidence control when evidence is claimed.

Conditional controls may be added for request intake, system-state understanding, Design, stack selection, delivery planning, phase/delivery-unit authority records, session scope, Implementation, retry, Update System State, and archive.

## Evidence rule

A control is not satisfied by intent, summary, or template presence. It is satisfied only by an existing artifact, observed file state, command output, user decision, or explicit not-applicable rationale.

## Capability contribution

Capabilities may contribute required controls when activated. Those controls must be recorded in `SESSION_EXECUTION.md` and resolved before the relevant lifecycle boundary can pass.

## Archive rule

When a session closes, `SESSION_EXECUTION.md` must be preserved in session history with final control statuses and continuation state.

## Claim reconciliation control

Claim reconciliation is an execution control whenever HIRMOS is about to claim readiness, implementation completion, validation success, runtime readiness, production readiness, package completeness, update-state readiness, or close success.

The control is `SATISFIED` only when the claim is backed by existing evidence and not contradicted by final files, session state, archive state, accepted state, or known environment limitations.
