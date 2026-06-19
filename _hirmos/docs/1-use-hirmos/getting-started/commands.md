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

A safe close should reconcile session-contract review, unresolved items, implementation evidence, accepted outcomes, archive/reset behavior, and durable current system state.

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
