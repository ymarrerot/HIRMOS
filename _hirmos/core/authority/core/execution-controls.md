# Run Execution Controls

Run execution controls are the run-scoped Core checklist of execution controls that must be satisfied before trustworthy completion may be surfaced.

## Purpose

A single command/run may have multiple run execution controls.

Core determines the control set for the resolved command, writes that set into `RUN_EXECUTION_CONTROLS.md`, and requires the runner to satisfy every listed control before trustworthy completion may be surfaced.

`RUN_EXECUTION_CONTROLS.md` identifies which controls apply to the run, where each control is governed, and whether each control remains `PENDING` or has been moved to `EXECUTED`. It does not restate the internal execution model of each control.

## Identity-label boundary note

The rendered framework identity label used in surfaced output does not change Core architectural ownership of the command lifecycle or wrapper contract.

## Command-boundary entry condition

The execution-control lifecycle begins only after a prompt has been successfully recognized as a supported Core command.

Unsupported or malformed `hirmos` inputs fail before this lifecycle begins.

Once a prompt has been recognized as a supported Core command, command-valid surfaced output is not allowed unless the required execution-control artifacts exist, all required controls are listed, and all listed controls are truthfully satisfied.

## Default initialization

Every command begins by initializing `RUN_EXECUTION_CONTROLS.md`.

Every command starts with `Identity display execution control` as the default baseline control.

## Command-specific enrichment

After default initialization, Core examines the resolved command and run characteristics and adds any additional execution controls required for that run.

Examples:
- runnable workflow commands such as `hirmos system-design` may add `Extension execution control`;
- hook-aware runs may add `Hook execution control`;
- future commands may add other Core-owned or command-specific controls as needed.

## Artifact: `RUN_EXECUTION_CONTROLS.md`

`RUN_EXECUTION_CONTROLS.md` is a Core-owned, run-scoped artifact that must exist for command execution.

It lists only:
- control id / name;
- governing file;
- status.

Use [RUN_EXECUTION_CONTROLS template](../../templates/RUN_EXECUTION_CONTROLS_TEMPLATE.md) for the canonical artifact shape.

## Working-copy continuity verification

During a supported run, the active local working copy remains the authoritative cumulative working state.

Artifact, readiness, and completion claims must be verified against that current cumulative working copy.

If the runtime cannot truthfully verify the current cumulative working-copy state, it must not claim continuity, artifact completion, readiness, or downstream completion.

A claim that a file was created, updated, verified, already present, or ready must refer to the active cumulative working copy.

Intended work, planned work, or likely work must not be surfaced as completed work.

If verification is missing, the run must use uncertainty language or fail closed, depending on the governed surface.

## Execution control status model

Allowed statuses:
- `PENDING`;
- `EXECUTED`.

Every listed control starts as `PENDING`.

A listed control may be updated to `EXECUTED` only after the runner has followed that control's governing file sufficiently for trustworthy continuation or completion and can truthfully verify that the governed requirement was satisfied.

Artifact presence alone is insufficient.
Plausible-looking output is insufficient.
If the runtime cannot truthfully verify satisfaction, the control remains `PENDING` and the run must fail closed.

## Core execution sequence

Under uncertainty, apply the bootstrap Step 0 — Framework-wide uncertainty rule before proceeding with extension resolution, entrypoint execution, or run-state assumptions.

For running any command, Core owns this outer execution sequence:
1. resolve the command;
2. initialize `RUN_EXECUTION_CONTROLS.md`;
3. seed `Identity display execution control`;
4. enrich the control list for the resolved command and run characteristics;
5. follow each listed governing file during execution;
6. update listed controls from `PENDING` to `EXECUTED` when satisfied;
7. validate that every listed control is `EXECUTED`;
8. only then surface trustworthy completion.

## Rerun refresh rule

When a supported command is a governed rerun of an earlier run scope, `RUN_EXECUTION_CONTROLS.md` must be refreshed for the current run state rather than treated as a carry-forward record.

State-specific notes inside the active controls must be rewritten so they describe the current run truth.

Stale prior-state notes must not survive into the rerun artifact. Examples:
- paused-state notes must not remain after a truthful completed rerun;
- completed-state notes must not remain after a truthful paused rerun;
- prior-state completion or blockage notes must not be presented as if they still govern the current run.

A control may be marked `EXECUTED` on a rerun only when both the governed requirement and any state-specific notes in the control entry truthfully match the current run state.

## Self-validation

Before trustworthy completion is surfaced, Core must verify:
- `RUN_EXECUTION_CONTROLS.md` exists;
- the default baseline control was seeded;
- any additional required controls for the resolved command were added;
- every listed control has been revisited during execution rather than left as an untouched placeholder;
- every listed control is marked `EXECUTED`.

## Fail-closed rule

A run must fail closed if:
- `RUN_EXECUTION_CONTROLS.md` is missing;
- the default baseline control was not seeded;
- a required execution control is not listed;
- any listed control remains `PENDING` at completion time.

## Relationship to control-specific governing files

`RUN_EXECUTION_CONTROLS.md` identifies active controls for the run but does not restate the internal execution model of each control.

Each listed governing file remains responsible for that control's actual execution process, including any control-specific templates, artifacts, self-validation, and fail-closed behavior.

## List of built-in execution controls

Built-in execution control names and governing files:

- `Identity display execution control`
  - `_hirmos/core/authority/core/identity-display-execution-control.md`

- `Hook execution control`
  - `_hirmos/core/authority/core/hook-execution-control.md`

- `Extension execution control`
  - governing file varies by resolved extension entrypoint and its governing authority.


## Runtime artifact paths

- `RUN_EXECUTION_CONTROLS.md` must be maintained at `_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/RUN_EXECUTION_CONTROLS.md` for extension-scoped runs.
- `HOOK_EXECUTION_CONTROL.md` must be maintained at `_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/HOOK_EXECUTION_CONTROL.md` for hook-aware extension-scoped runs.


## Invalid-command exclusion note

An invalid or unsupported `hirmos` input does not produce command-valid completion.

The runtime must surface invalid-command failure rather than entering a fake, partial, or guessed run state.
