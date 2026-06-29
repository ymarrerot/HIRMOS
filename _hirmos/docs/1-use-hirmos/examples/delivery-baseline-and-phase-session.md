# Example: Delivery Baseline and Phase/Session Flow

This example shows how HIRMOS keeps larger work durable without making every request heavy.

## Starting point

```text
hirmos start "Build a local MVP with upload, processing, generated output, credits, and history"
```

HIRMOS should inspect current state and decide whether the work can be a single governed session. If the request is too broad for a safe single close, HIRMOS should propose a delivery baseline.

## Delivery Baseline — Review or Change

```text
Delivery Baseline — Review or Change

Delivery goal: local MVP with upload, processing, generated output, credits, and history.
Smallest honest shape: multi-session delivery with phases.

Proposed phases:
1. Foundation and persistence.
2. Processing and interpretation.
3. Generated output, credits, history, and close.

Gated decisions:
- runtime target;
- provider/model choices;
- local-only versus deployment-ready boundary.

Next command:
hirmos continue "Accept delivery baseline and create the next phase/session baseline"
```

Delivery authority lives under `_hirmos/system/delivery/<delivery-id>/`. Future phase files are created just in time, not as empty placeholders.

## Session Baseline — Review or Change

After delivery baseline acceptance, HIRMOS creates the next bounded phase/session baseline.

```text
Session Baseline — Review or Change

Active delivery: <delivery-id>
Active phase: PHASE-01
Session scope: foundation and persistence.
Implementation mode: implementation units required.

Next command:
hirmos continue "Accept session baseline and create IU plan"
```

The session baseline adopts delivery/phase authority. It does not replace it.

## IU Planning — Review or Change

```text
IU Plan — Review or Change

IU planning is complete.
IU execution has not started.
No material project-file edits are authorized until the IU plan is accepted.

Next command:
hirmos continue "Accept IU plan and begin IU execution"
```

This pause prevents post-hoc IU creation. IU files must exist and pass generated-artifact validation before IU execution starts.

## IU Execution and close

After IU plan acceptance, HIRMOS can implement under the accepted scope and sealed IU files. At close it should:

- reconcile implementation evidence;
- preserve limitations and carry-forward items;
- update current system state with accepted outcomes and pointers;
- archive the session.

## What should not happen

HIRMOS should not:

- implement directly from the delivery baseline;
- implement directly from the session baseline when IU mode applies;
- create future phase files as empty synchronization obligations;
- duplicate mutable delivery completion status across multiple artifacts;
- claim production readiness from local-MVP evidence.
