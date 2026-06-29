# Commands

HIRMOS workflow commands are written inside the AI-agent conversation after the project has been initialized and bootstrapped.

They are not terminal commands. The terminal CLI installs and updates the framework; the agent-facing commands guide the HIRMOS workflow.

## Command authority

The compact runtime command authority lives in:

```text
_hirmos/core/commands/
```

Protocol files under `_hirmos/core/protocol/` are deeper reference authority. A normal run should follow the active command file first and read deeper protocol files only when the command or a gate requires it.

## Core workflow commands

| Command | Purpose |
|---|---|
| `hirmos start "<request>"` | Start a governed run from the current system state. |
| `hirmos continue` | Continue through the next allowed governed boundary. |
| `hirmos status` | Inspect active state without advancing work. |
| `hirmos close` | Reconcile evidence, update current system state, and archive when ready. |

## `hirmos start`

Use `hirmos start` to begin work. HIRMOS should inspect current state, select the smallest honest work shape, and stop at a reviewable checkpoint.

Common first checkpoints:

| Work shape | First checkpoint |
|---|---|
| Small bounded work | Recommended Baseline or Session Baseline |
| Single-session implementation | Session Baseline — Review or Change |
| Larger delivery | Delivery Baseline — Review or Change |
| Phase of accepted delivery | Session Baseline — Review or Change |

## `hirmos continue`

Use `hirmos continue` only when HIRMOS has shown that continuation is allowed.

Continuation does not always mean “start coding.” It can mean:

- accept a delivery baseline and prepare the next phase/session baseline;
- accept a session baseline and create the IU plan;
- accept an IU plan and begin IU execution;
- continue a correction or review pass;
- proceed toward close readiness.

When IU mode applies, the expected sequence is:

```text
hirmos continue "Accept session baseline and create IU plan"
hirmos continue "Accept IU plan and begin IU execution"
```

Material project-file edits require implementation authorization. IU Planning alone is not implementation authorization.

## `hirmos status`

Use `hirmos status` to inspect active state without changing artifacts except read-only status output when the framework explicitly allows it.

Status should report:

- current lifecycle position;
- active scope/delivery pointers;
- blocked or pending gates;
- unresolved items;
- evidence posture;
- one recommended next command.

## `hirmos close`

Use `hirmos close` when the work is ready to reconcile evidence and update durable state.

Close should not overclaim. For example, a local MVP close can be accepted as local-runtime evidence without claiming production readiness.

## Work-shape focus values

The active focus determines which artifacts are required:

| Focus | Typical use | Authority |
|---|---|---|
| `minimal_session` | Small bounded output or non-implementation work | generated only when needed |
| `session_baseline` | Single-session scope | `SESSION_SCOPE.md` |
| `delivery_baseline` | Durable delivery planning | `DELIVERY_PLAN.md`, `DELIVERY_SCOPE.md` |
| `phase_session_baseline` | Next slice of accepted delivery | phase file + `SESSION_SCOPE.md` |
| `implementation` | Authorized implementation | accepted scope and IU/evidence surfaces as needed |

HIRMOS should create optional artifacts just in time. Empty future artifacts create synchronization cost and should be avoided.
