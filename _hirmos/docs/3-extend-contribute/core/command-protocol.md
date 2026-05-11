# Command Protocol

This guide shows the small command surface most operators use during normal framework work. Use it to understand what you can run, inspect, and list without having to read Core-local protocol details first.

Need the canonical mechanics? See [_hirmos/core/command-protocol.md](../../../core/command-protocol.md).

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

## First-contact bootstrap

Before extension work begins, initialize the AI session with the explicit bootstrap prompt:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

This loads `_hirmos/HIRMOS_CORE.md` and starts the Core bootstrap path. The `hirmos` command protocol is available after the bootstrap has been read.

## Command-declared default vs named entrypoints

- `hirmos <command>` resolves to the installed extension that declares the command in `hirmos_commands`, then runs that command's declared entrypoint.
- `hirmos <command>:<entrypoint>` resolves the same command owner, then runs a named public entrypoint exposed by that extension.

This lets a coherent extension expose both:

- a top-level workflow for regular users;
- lower-level reusable sub-workflows for power users and extension authors.

## Regular-user workflow examples

The HIRMOS greenfield workflow uses default extension commands:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These correspond to:

```text
Requirements → System Design → Implementation
```

Named entrypoints remain available when intentionally exposed by an extension, for example:

```text
hirmos system-design:phase-design-cycle
hirmos implementation:implementation-planning-cycle
```

## Entrypoints vs Spec filenames

Entrypoint names are the public command surface. Spec filenames are deeper internal governance files. They may be related, but they are not interchangeable. The Core does not guess aliases from Spec filenames or concept names.

## When to use which

Use the highest-level coherent entrypoint first.

Drop to a lower-level public entrypoint only when you need tighter control or a narrower reusable unit.

## Explainability and traceability

The Core should make every run understandable by showing:

- the resolved extension;
- the resolved entrypoint;
- the active stack when relevant;
- matching hooks;
- execution order.

## Supported command form

The current command surface is `hirmos ...`. Use the documented `hirmos` forms when instructing an agent to run HIRMOS commands.

## Describe one named public entrypoint

`hirmos describe extension <id>:<entrypoint>` should surface the runnable entrypoint's minimal execution contract summary:

- Purpose
- Produces
- Terminal States

This keeps inspection aligned with the Core execution contract before a run begins.

## Entrypoint arguments

Runnable entrypoints may accept an optional trailing argument tail after the resolved HIRMOS command target.

Examples:

```text
hirmos some-command:some-entrypoint target-value
hirmos explain some-command:some-entrypoint target-value
```

The Core passes that argument tail through. The owning extension defines its meaning.
