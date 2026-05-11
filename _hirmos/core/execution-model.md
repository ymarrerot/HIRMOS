# Execution Model

The execution model is intentionally small and deterministic.

Use [Identity display execution control](./authority/core/identity-display-execution-control.md), [Execution controls](./authority/core/execution-controls.md), [Runtime trace rules](./authority/core/runtime-trace-rules.md), and [Entrypoint execution contract](./authority/core/entrypoint-execution-contract.md) for the authoritative Core-local doctrine that governs runtime behavior.

## Run execution controls model

All commands execute within the run execution controls model governed by [Execution controls](./authority/core/execution-controls.md).

That file is the sole canonical owner of the outer command path and `RUN_EXECUTION_CONTROLS.md` lifecycle. This file explains the runtime model but does not restate that outer execution sequence.

## Runnable command shape

For runnable workflow commands such as `hirmos system-design` or `hirmos system-design:phase-design-cycle`, Core resolves the manifest-declared command owner, any optional entrypoint selector, any argument tail, and any runtime prerequisites, then executes the run under [Execution controls](./authority/core/execution-controls.md).

The resolved entrypoint remains the primary instruction source for extension-local workflow behavior. Trustworthy completion may be surfaced only after all listed run execution controls are `EXECUTED`.

## Hook-aware execution in MVP

Owning workflows may include explicit hook invocation markers. When a command/run is hook-aware, [Execution controls](./authority/core/execution-controls.md) adds `Hook execution control`, and [Hook execution control](./authority/core/hook-execution-control.md) governs that control. This file does not reteach that control lifecycle.

## Entrypoint arguments

The core may carry an optional argument tail for runnable entrypoints.

The core owns only:
- parsing the workflow command and optional entrypoint selector;
- separating the trailing argument tail from that command target;
- passing that tail through to the active entrypoint.

The owning extension owns:
- argument meaning;
- argument validation;
- parameter-specific pause or failure behavior.

## Primary instruction source

The resolved extension entry file remains the primary instruction source for extension-local workflow behavior.

Core-owned execution controls may still apply to the run. When they do, the runner must return to their governing files through [Execution controls](./authority/core/execution-controls.md) rather than drifting into extension-spec-first execution.
