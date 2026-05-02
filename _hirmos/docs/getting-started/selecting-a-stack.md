# Selecting a Stack

HIRMOS uses an active stack setting so extensions can adapt to the project's technical environment.

## Default selection

The active stack is selected in:

```text
_hirmos/STACK_CONFIG.json
```

The shipped default is:

```json
{
  "spec_version": 1,
  "active_stack": "generic"
}
```

## How to switch stacks

1. open `_hirmos/STACK_CONFIG.json`
2. change `active_stack` to the desired stack id
3. make sure the stack exists under `_hirmos/stacks/<stack-id>/`
4. rerun the relevant governed workflow

## When to use `generic`

Use `generic` when the project stack is:
- still being discovered
- mixed or unusual
- not yet modeled by a more specific stack package

You can start with `generic` and switch later as the project becomes clearer.

## What happens after switching

After switching, rerun the relevant governed workflow. Stack-aware extensions should adapt to the new active stack.

## Go next

- Continue to [First real run](./first-real-run.md) if you are staying on the canonical getting-started path.
- Go back to the [Getting started guide](./README.md) if you want the full onboarding path at a glance.

## Optional reading

- [Core stacks](../core/stacks.md) if you want the deeper stack-package and stack-resolution mechanics.
