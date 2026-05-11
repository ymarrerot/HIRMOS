# Core Commands

HIRMOS keeps the user-facing command surface small.

## Supported commands

```text
hirmos <command> [arguments...]
hirmos <command>:<entrypoint> [arguments...]
hirmos describe extension <id>
hirmos describe extension <id>:<entrypoint>
hirmos list extensions
hirmos explain <command> [arguments...]
hirmos explain <command>:<entrypoint> [arguments...]
```

Need the deeper Core-local protocol? See [_hirmos/core/command-protocol.md](../../../core/command-protocol.md).

## First-contact bootstrap

After installing HIRMOS in a project, you may run the terminal CLI command `hirmos init` to generate agent-native bootstrap files. Before running extension workflows, initialize the AI session with:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

This loads `_hirmos/HIRMOS_CORE.md` and starts the Core bootstrap path.

## Default extension commands

```text
hirmos <command>
```

runs the manifest-declared HIRMOS command exposed by an installed extension.

For the regular-user greenfield workflow, regular users normally run:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These map to:

| Public step | Command | Default entrypoint |
|---|---|---|
| Requirements | `hirmos requirements` | `requirements` |
| System Design | `hirmos system-design` | `system-design` |
| Implementation | `hirmos implementation` | `implementation` |

## Named entrypoint commands

```text
hirmos <command>:<entrypoint>
```

runs a named entrypoint exposed by that extension.

Use named entrypoints when you intentionally need a narrower advanced/reusable workflow.

## Inspection commands

Use these before a serious run:

```text
hirmos describe extension <id>
hirmos explain <command>
```

For a named entrypoint:

```text
hirmos describe extension <id>:<entrypoint>
hirmos explain <command>:<entrypoint>
```

A trustworthy description should show the execution-contract summary:

- Purpose
- Produces
- Terminal States

An explain command should show the resolved extension, resolved entrypoint, hooks, and execution order.

## Use the supported command form

The current command surface uses `hirmos ...` instructions. Use the documented command forms on this page instead of shorthand command names that are not part of the current installed framework.

## Go next

- Read [Quickstart](quickstart.md) for the practical regular-user workflow.
- Read [Use HIRMOS in 3 Steps](use-hirmos-in-3-steps.md) for the workflow explanation.
