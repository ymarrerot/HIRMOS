# Framework Command Reference

Framework workflow commands are agent-facing HIRMOS commands used inside an AI coding tool after bootstrap.

The compact runtime command authority lives in:

```text
_hirmos/core/commands/
```

## `hirmos start`

Starts a governed run from the current system state.

Expected behavior:

- inspect relevant current state;
- select the smallest honest work shape;
- surface unresolved decisions and assumptions;
- stop at a reviewable checkpoint;
- recommend exactly one next command.

Possible checkpoints include Recommended Baseline, Session Baseline, or Delivery Baseline.

## `hirmos continue`

Continues through the next allowed governed boundary.

Continuation may mean:

- accept delivery baseline and create next phase/session baseline;
- accept session baseline and create IU plan;
- accept IU plan and begin IU execution;
- continue correction/review work;
- proceed toward close readiness.

When IU mode applies, implementation must follow:

```text
hirmos continue "Accept session baseline and create IU plan"
hirmos continue "Accept IU plan and begin IU execution"
```

## `hirmos status`

Reports active state without advancing work.

Status should show lifecycle/focus, blocked gates, unresolved items, evidence posture, derived pointer warnings, and one recommended next command.

## `hirmos close`

Closes a session only when close readiness is satisfied.

Expected behavior:

- reconcile claims against evidence;
- preserve unresolved/carry-forward items;
- update accepted current state with pointers;
- archive the session;
- avoid production-readiness overclaims.

## Terminal CLI versus framework commands

The terminal CLI installs and manages HIRMOS. Framework commands are interpreted by the AI agent after bootstrap.
