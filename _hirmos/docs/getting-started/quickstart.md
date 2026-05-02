# Quickstart

This is the smallest successful path through the framework. Think of it as a smoke test plus first real orientation.

## Bootstrap the core

```text
Read and follow the instructions in HIRMOS_CORE.md
```

## Check the active stack

Open `_hirmos/STACK_CONFIG.json` and confirm the selected stack fits the project.

## List installed extensions

```text
cmd: list extensions
```

Expected examples in a minimal Core install:
- `hello-world`
- `pretty-output`

Marketplace workflow extensions appear here only after you install them.

## Describe one extension

```text
cmd: describe extension hello-world
```

## Explain one run plan

```text
cmd: explain run extension hello-world
```

This should show:
- the target entry file
- any exposed hooks relevant to the active entrypoint
- any resolved hook subscriptions
- the execution order

## Run one extension

```text
cmd: run extension hello-world
```

With `pretty-output` installed, the run should include the main `hello-world` entry plus any matched `pretty-output` hook subscriptions.

## Named entrypoint syntax

```text
cmd: run extension some-extension:some-entrypoint
```

## Hook-only reminder

`pretty-output` is a hook-only extension and participates when another extension triggers a matching hook.

## Serious coherent extension example

Once the `hello-world` path makes sense, inspect any serious governed workflow extension that is actually installed in this project. Use `cmd: list extensions` first, then describe or explain one of its public entrypoints.

```text
cmd: describe extension <installed-extension-id>
cmd: explain run extension <installed-extension-id>:<entrypoint>
```

For a named public entrypoint, the description should surface the execution-contract summary:
- Purpose
- Produces
- Terminal States

## Go next

- Continue to [Selecting a stack](./selecting-a-stack.md) if you are staying on the canonical getting-started path.
- Go back to the [Getting started guide](./README.md) if you want the full onboarding path at a glance.

## Optional reading

- Optional examples under `../examples/` if you want to compare serious extension run shapes after installing the relevant extension.
- [Release packaging](../core/release-packaging.md) if you plan to share the framework or a working state.
