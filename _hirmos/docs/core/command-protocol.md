# Command Protocol

This guide shows the small command surface most operators use during normal framework work. Use it to understand what you can run, inspect, and list without having to read Core-local protocol details first.

Need the canonical mechanics? See [_hirmos/core/command-protocol.md](../../core/command-protocol.md).

## Supported commands

```text
cmd: run extension <id> [arguments...]
cmd: run extension <id>:<entrypoint> [arguments...]
cmd: describe extension <id>
cmd: describe extension <id>:<entrypoint>
cmd: list extensions
cmd: explain run extension <id> [arguments...]
cmd: explain run extension <id>:<entrypoint> [arguments...]
```

## Default vs named entrypoints

- `cmd: run extension <id>` uses the extension's default public entrypoint.
- `cmd: run extension <id>:<entrypoint>` uses a named public entrypoint exposed by that extension.

This lets a coherent extension expose both:

- a top-level workflow
- lower-level reusable sub-workflows

## Entrypoints vs Spec filenames

Entrypoint names are the public command surface. Spec filenames are deeper internal governance files. They may be related, but they are not interchangeable. The core does not guess aliases from Spec filenames or concept names.

## When to use which

Use the highest-level coherent entrypoint first.
Drop to a lower-level public entrypoint when you need tighter control or a narrower reusable unit.

## Explainability and traceability

The core should make every run understandable by showing:

- the resolved extension
- the resolved entrypoint
- the active stack when relevant
- matching hooks
- execution order

## Why this matters

This command model preserves a minimal core while making the framework ready for decomposition of serious workflow families.

## Describe one named public entrypoint

`cmd: describe extension <id>:<entrypoint>` should surface the runnable entrypoint's minimal execution contract summary:

- Purpose
- Produces
- Terminal States

This keeps inspection aligned with the core execution contract before a run begins.


## Entrypoint arguments

Runnable entrypoints may accept an optional trailing argument tail after the resolved extension target.

Examples:
- `cmd: run extension some-extension:some-entrypoint target-value`
- `cmd: explain run extension some-extension:some-entrypoint target-value`

The core passes that argument tail through. The owning extension defines its meaning.