# Core Commands

The current command surface is intentionally small:

```text
cmd: run extension <id> [arguments...]
cmd: run extension <id>:<entrypoint> [arguments...]
cmd: describe extension <id>
cmd: describe extension <id>:<entrypoint>
cmd: list extensions
cmd: explain run extension <id> [arguments...]
cmd: explain run extension <id>:<entrypoint> [arguments...]
```

Use this page for normal framework operation. Use [_hirmos/core/command-protocol.md](../../core/command-protocol.md) only when you need canonical protocol mechanics.

## When to use each command

- `cmd: list extensions` to inspect what is installed
- `cmd: describe extension <id>` to inspect one extension
- `cmd: describe extension <id>:<entrypoint>` to inspect one named public entrypoint, including its execution-contract summary: Purpose, Produces, and Terminal States
- `cmd: explain run extension ...` to inspect the run plan
- `cmd: run extension ...` to execute a public entrypoint

## Important naming rule

Command names must match the public entrypoint names exactly. Spec filenames and conceptual cycle names may be more descriptive, but they are not automatic aliases.

## Parameters

Some entrypoints may require parameters after the command target. The core passes those through to the active entrypoint, and the entrypoint docs should define what they mean.


## Go next

- Go back to the [Getting started guide](./README.md) if you want the full onboarding path at a glance.
- Return to [Quickstart](./quickstart.md) if you opened this page from the optional reading link and want to stay on the main first-use path.

## Optional reading

- [Core command protocol](../../core/command-protocol.md) if you need the canonical protocol mechanics.
