# Core Rules

This file is the bootstrap framing file for Core operation.

It defines the minimum behavioral rules the Core must adopt before performing framework work.

## Core responsibilities

The core must do only the following:

1. Bootstrap framework operation through `_hirmos/HIRMOS_CORE.md` and the `_hirmos/core/bootstrap.md` handoff it requires.
2. Discover installed extensions.
3. Read and validate extension manifests.
4. Resolve public runnable surfaces declared by manifests.
5. Validate required dependencies.
6. Build a deterministic run plan.
7. Initialize and maintain `RUN_EXECUTION_CONTROLS.md` for the active command.
8. Compose hook contributions for the requested extension.
9. Resolve the active stack package and expose normalized stack context.
10. Execute the target extension using the composed context.
11. Emit a concise execution trace.

## Core non-goals

The core must not contain:
- role-specific long instructions
- business workflows
- cycle logic
- deliverable templates
- domain-specific policies
- client-specific behavior
- stack-specific content

Those belong in extensions or stack packages as appropriate.

## Extension-first rule

If a new capability can be expressed as:
- a new runnable unit
- a named public entrypoint
- a hook contribution
- an optional policy pack
- a reusable template

then it should be added as an extension instead of expanding the core.

## Public-surface rule

The core must treat manifests as authoritative for public runnable surfaces.

That means:
- `entry` defines the default public entrypoint
- `entrypoints` defines named public entrypoints
- hooks are public contributions declared by manifests
- not every internal file inside an extension is publicly runnable


## Run execution controls rule

For running any command, Core must treat [Execution controls](./authority/core/execution-controls.md) as the sole canonical owner of the outer command path.

That means Core must:
- initialize `RUN_EXECUTION_CONTROLS.md`;
- seed the default baseline control;
- enrich the control list for the resolved command and run characteristics;
- satisfy each listed governing file;
- fail closed if any listed control remains `PENDING` at completion time.

## Determinism rule

The same installed extension set should produce the same run plan unless the Orchestrator changes the requested command or inputs.

## Explainability rule

A run should be explainable in terms of:
- target extension
- target entrypoint
- dependencies loaded
- hook contributors loaded
- final execution order

## Framing rule

The framework is extension-based and agent-capable, but not every extension is an agent.

## Bootstrap relationship to Core Specs

This file is read directly during Core bootstrap.

It does not replace the narrower authoritative doctrine files under `/_hirmos/core/authority/core/`. Those files remain the canonical references for specific Core-local topics such as manifests, hooks, execution contracts, stacks, validation, run-result rules, and trace rules.
