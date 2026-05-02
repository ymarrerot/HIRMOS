# Hook Execution Control

## Purpose

This file is the governing doctrine for `Hook execution control` under `RUN_EXECUTION_CONTROLS.md`. It defines how hook-aware runs are resolved, ordered, traced, and validated.

## Required template source

Use `_hirmos/core/templates/HOOK_EXECUTION_CONTROL_TEMPLATE.md` as the required artifact template for this control. The older `HOOK_EXECUTION_MAP` naming made the artifact's concrete shape more obvious; this control and its template must preserve that clarity explicitly.

## Required artifact path

For hook-aware runs, maintain the run-scoped artifact at:

`_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/HOOK_EXECUTION_CONTROL.md`

## Governing rules

- the Core does not own a fixed global hook catalog;
- an owning extension declares the hook points it exposes in its manifest;
- installed extensions may subscribe to those declared hook points;
- hook subscriptions are optional integration declarations unless paired with `requires`; missing hook owners leave those subscriptions dormant rather than making unrelated extension commands fail;
- the Core resolves matching subscriptions for the active run;
- the Core orders and executes matching subscriptions deterministically.

## Matching and ordering rules

- matching is exact;
- names are case-sensitive unless the manifest contract later changes explicitly;
- the Core does not infer aliases;
- the Core does not normalize near-matches;
- duplicate exposed hook names inside one owning extension are invalid.

## Fail-closed rule

An incomplete hook execution control artifact is a fail-closed condition for a hook-aware run. `Hook execution control` must not be marked `EXECUTED` unless the artifact is present and complete for the run.

## Artifact completeness

Treat `HOOK_EXECUTION_CONTROL.md` as complete only if it records at minimum:
- the resolved hook points for the run;
- the matched subscribers for each resolved hook point;
- the final execution order used for those subscribers;
- the execution result or status for each hook contribution that was part of the run.

## Relation to other Core files

- Use [Execution controls](./execution-controls.md) for the outer lifecycle that lists and governs this control.
- Use [Runtime trace rules](./runtime-trace-rules.md) for trace expectations when hooks materially affect a run.


## Discovery-evidence requirement for runtime-input hooks

If a hook-aware run reports on discovered or absent runtime-input packs, the hook execution artifact must preserve evidence for:
- inspected path
- discovered candidate names
- accepted active names
- rejected candidates with reasons

Free-form claims like “none found” are insufficient when candidate directories are actually present in the active cumulative working copy.

## Runtime-pack false-negative rule

A hook-aware run must not claim that no active runtime pack was found when the inspected runtime-pack directory contains candidate pack folders unless every candidate was explicitly rejected with a recorded reason.


## Subscriber-resolution consistency rule

If the active working copy contains an installed extension whose manifest declares a hook subscription target that exactly matches a resolved hook point for the run, `Matched subscribers` must not be recorded as `none` for that hook point unless the run also records an explicit rejection reason for that installed matching subscriber.

Acceptable rejection reasons must be concrete and run-specific, such as:
- invalid manifest or hook declaration for this run
- subscriber file missing or unreadable
- subscriber excluded by an explicit runtime rule that is recorded for the run
- subscriber failed pre-execution validation and was therefore not eligible to run

Silent omission of an installed exact-match subscriber is invalid.
