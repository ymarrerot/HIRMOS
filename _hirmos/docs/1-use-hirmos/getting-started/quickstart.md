# Quickstart

This is the smallest practical path through HIRMOS after the framework and official workflow extensions are installed.

The regular-user HIRMOS workflow is:

```text
Requirements → System Design → Implementation
```

The practical HIRMOS workflow commands are:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

Use those commands inside your AI tool after HIRMOS Core has loaded. They are not terminal shell commands.

## 1. Initialize agent discovery

Install the HIRMOS CLI, then run `hirmos init` from the project root:

```bash
npm install -g hirmos
hirmos init
```

If `_hirmos/` is not already present, `hirmos init` downloads the latest HIRMOS framework release package and installs it before generating the default agent bootstrap file.

This generates or updates agent-native bootstrap files and points the selected tool to `_hirmos/HIRMOS_CORE.md`. It does not run a workflow.

To generate specific tool adapters, run:

```bash
hirmos init --integration claude,cursor,copilot
```

If you are not using the CLI yet, skip this terminal step.

## 2. Load HIRMOS Core in your AI tool

For the safest first run, tell your AI tool:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

This loads the Core runtime discipline before any extension command can be trusted. Agent-native integration files created by `hirmos init` are only bootstrap adapters; they do not replace Core.

## 3. Check what is installed

Inside the AI tool after Core has loaded, ask for:

```text
hirmos list extensions
```

For the full official greenfield regular-user workflow, expect these extensions to be installed:

```text
requirements-agent
system-design-agent
implementation-agent
```

Minimal demo/support installs may also include:

```text
hello-world
pretty-output
```

If one of the three workflow extensions is missing, install it before following this quickstart.

## 4. Run Requirements

```text
hirmos requirements
```

Use this step when you need HIRMOS to turn user-provided goals, context, notes, prototypes, user stories, files, attachments, bounded repository context, and constraints into requirements artifacts suitable for system design.

For short requirements, you may also pass a prompt directly after the command:

```text
hirmos requirements Build a menu management app for a small restaurant.
```

For longer or reusable requirements, use the current chat/session prompt, online attachments, files under `_hirmos/inputs/requirements-agent/requirements/`, or explicit bounded local file references. HIRMOS should not automatically ingest the whole repository without a bounded scope.

Typical important outputs include:

```text
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
```

If the run pauses, resolve the gated requirements decisions or provide the requested input, then rerun the Requirements command.

## 5. Run System Design

```text
hirmos system-design
```

Use this step after Requirements is complete enough for design. System Design consumes Requirements outputs and produces system, architecture, phase, and staged delivery artifacts.

Typical important outputs include:

```text
_hirmos/artifacts/sot/SYSTEM_SOT.md
_hirmos/artifacts/sot/ARCHITECTURE_SOT.md
_hirmos/artifacts/sot/PHASES_SOT.md
_hirmos/artifacts/phases/phase_<N>_<slug>_SOT.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
```

If the run pauses, resolve gated design or phase decisions before continuing.

## 6. Run Implementation

```text
hirmos implementation
```

Use this step after System Design and phase scope are approved.

Implementation performs or refreshes planning when needed, then pauses for explicit approval before phase execution. Do not treat implementation planning as permission to execute code until that approval is given.

Typical important outputs include:

```text
_hirmos/artifacts/prompts/
_hirmos/artifacts/context/implementation-agent/implementation/
_hirmos/artifacts/ops/
```

Implementation completes with **Evidence-backed Review**: what changed, what checks ran, what passed or failed, what remains unresolved, and whether the step completed, paused, or failed.

## Terminal states

| State | Meaning |
|---|---|
| `completed` | The step finished and surfaced evidence supporting completion. |
| `paused` | HIRMOS needs input, a decision, approval, or a missing prerequisite. |
| `failed` | HIRMOS cannot continue truthfully within the governed recovery path. |

## Named entrypoint syntax for power users

Most regular users should run the default extension commands above. Power users can run a named entrypoint when they intentionally need a narrower workflow:

```text
hirmos <command>:<entrypoint>
```

Use named entrypoints only when you understand the narrower scope. See [Core commands](core-commands.md) for the syntax and inspection commands.

## Go next

- Read [Use HIRMOS in 3 Steps](use-hirmos-in-3-steps.md) for the regular-user explanation.
- Read [Core commands](core-commands.md) for command syntax.
- Read the [Operator playbook](../orchestrator/operator-playbook.md) for how to handle pauses and decisions.
