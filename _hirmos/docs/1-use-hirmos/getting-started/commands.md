# Command Guide

HIRMOS keeps the everyday workflow command surface small.

```text
hirmos start
hirmos continue
hirmos status
hirmos close
```

These are framework workflow commands used inside the AI-agent conversation after bootstrap. They are not terminal CLI commands.

The terminal CLI is focused on installation and integration setup. For complete CLI usage, see [CLI Reference](../../reference/cli-reference.md).

## `hirmos start`

Starts a governed session from a user request.

Examples:

```text
hirmos start "Add Google login"
hirmos start
```

`hirmos start` should begin with current-state understanding. It should not authorize implementation by itself unless the governed workflow has reached implementation readiness.

A strong `hirmos start` should establish or update the active session context, identify unresolved items, and recommend exactly one safe next command.

## `hirmos continue`

Advances the active lifecycle boundary when continuation is allowed.

Use it after HIRMOS has paused for a decision, reported implementation readiness, completed a unit, or otherwise indicated the next continuation point.

`continue` should be cumulative. It should append to active execution history rather than rewriting the session as if earlier work did not happen.

## `hirmos status`

Inspects the active or last known session state without advancing work.

It should summarize:

- active lifecycle boundary;
- current session or delivery state;
- unresolved gated items and non-gating assumptions;
- implementation-unit or phase progress when applicable;
- close readiness when relevant;
- exactly one recommended next command.

## `hirmos close`

Runs Update System State when the session is ready to close.

It should not repair missing Design or Implementation work. If close readiness is not satisfied, HIRMOS should block close and explain which owning stage must be revisited.

A safe close should reconcile session-scope review, unresolved items, implementation evidence, accepted outcomes, archive/reset behavior, and durable current system state.

## What commands must not do

Commands must not:

- claim readiness or completion while required execution controls are `PENDING` or `BLOCKED`;
- reference an artifact as ready or inspectable unless it exists and contains non-placeholder content;
- treat source inputs as accepted design authority;
- silently skip unresolved gated decisions;
- close a session while active artifacts contradict each other.

## Command state machine

HIRMOS command legality is governed by `_hirmos/core/protocol/COMMAND_STATE_MACHINE.md` and `_hirmos/session/SESSION_STATE.json`.

The practical rule is simple:

```text
start establishes governed work
continue advances only when safe
status observes without mutation
close updates current state only when evidence and artifacts agree
```


New governed sessions use `_hirmos/session/SESSION_SCOPE.md` as the active session authority. Durable multi-session work uses `_hirmos/system/delivery/DELIVERY_PLAN.md` plus `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` when needed.

## Focus-aware command behavior

HIRMOS always runs inside a governed runtime session envelope, but the active focus determines which authority artifacts are required.

| Focus | When used | Required authority | Default next checkpoint |
|---|---|---|---|
| `minimal_session` | Small bounded output or non-implementation work | `SESSION_SCOPE.md` only when bounded authority is needed | Session Baseline / Recommended Baseline |
| `session_baseline` | Single-session implementation or reviewable session scope | `SESSION_SCOPE.md` | Session Baseline — Review or Change |
| `delivery_baseline` | Durable delivery/release planning before phase/session work | `DELIVERY_SCOPE.md` and delivery unresolved register | Delivery Baseline — Review or Change |
| `phase_session_baseline` | First or next phase/session inside an accepted delivery | `PHASE-xx.md` and `SESSION_SCOPE.md` | Session Baseline — Review or Change |
| `implementation` | Accepted session scope is ready to implement | `SESSION_SCOPE.md` and implementation controls | Implementation / evidence |

During `delivery_baseline`, `hirmos start` must not create `SESSION_SCOPE.md`, session unresolved items, phase files, or implementation-unit files by default. It prepares delivery authority and pauses for delivery baseline review. After acceptance, `hirmos continue` transitions to the next phase/session baseline rather than implementing directly.

During `session_baseline` or `phase_session_baseline`, `hirmos continue` accepts or amends the session baseline and only then creates implementation-unit artifacts when they are actually needed.
