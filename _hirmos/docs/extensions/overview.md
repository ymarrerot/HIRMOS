# Extension Authoring Overview

Extension authoring should also follow a low-to-high cognitive-load path.

## Start with the simplest mental model

An extension is an installable package that adds framework behavior without forcing that behavior into the Core.

A good extension usually has three important qualities:
- a clear public surface
- a coherent internal boundary
- governed runtime behavior

## SDLC anchor

Many users find it easiest to place extensions by the kind of work they support. For example, an extension may help govern requirements grounding, design, planning, implementation, execution, presentation, or supporting utility work. That does not change the framework structure, but it gives operators a familiar way to understand why an extension exists.

## The most common authoring goals

1. create a new extension family
2. reuse existing public extension surfaces in a custom flow
3. extend an existing extension through hooks instead of forking when possible

## A lesson many authors learn later than they should

Getting better at prompts and clear instructions is necessary, but it is only the first step. As extension work becomes more real, more branched, or more trust-sensitive, you eventually reach the point where **clear instructions are not enough**. That is the point where governance has to join the work directly through validation, governed intermediate collection, and governed surfaced outputs when needed. Read [Beyond Clear Instructions](./beyond-clear-instructions.md) early so you do not have to learn it only after repeated misses.

## A good authoring path

### Lowest cognitive load
- [Creating your first extension](./creating-your-first-extension.md)
- [Public entrypoints](./public-entrypoints.md)
- [Validation rules](./validation-rules.md)

### Next layer
- [Spec-backed entrypoints](./spec-backed-entrypoints.md)
- [Large extension structure](./large-extension-structure.md)
- [Stack consumption](./stack-consumption.md)

### Then go deeper when needed
- [Hooks authoring](./hooks-authoring.md)
- [Reusing existing extensions](./reusing-existing-extensions.md)
- [Extending existing extensions](./extending-existing-extensions.md)
- [Best practices](./best-practices.md)

## Public surface first

When designing an extension, start with the public surface before the internal details.

That means defining:
- what commands the Orchestrator should be able to run
- which entrypoints are high-level cycles
- which entrypoints are lower-level reusable surfaces
- what the extension should keep private

## Grow the governance only when the work needs it

For small examples, a simple public entrypoint may be enough.
For more serious workflows, a Spec-backed model usually becomes worthwhile because it helps preserve:
- quality checks
- honest pause/completion behavior
- artifact discipline
- reusable workflow method without overloading one entrypoint file

## Runtime identity metadata

Serious runnable extensions may also declare optional runtime identity metadata in `extension.yaml`, such as:

```yaml
runtime:
  category: agent
  identity: Example Agent
```

Use this when the operator should be able to see which runtime layer is actively executing the command. The manifest declares the identity value; the core handles whether and how that identity is shown.

## Practical companion guides

- `best-practices.md` — common extension design patterns and mistakes to avoid
- `naming-conventions.md` — naming rules for extension ids, entrypoints, and hooks
- `extension-readme-contract.md` — what a good extension README should cover

## Keep extension outputs inside the framework surfaces HIRMOS already provides

Extensions should write inside the existing `_hirmos/` surfaces instead of inventing new top-level folders.

Common examples:
- `_hirmos/inputs/<extension-id>/...`
- `_hirmos/artifacts/outputs/<extension-id>/...`
- `_hirmos/artifacts/context/<extension-id>/...`
- `_hirmos/artifacts/ops/...`

That keeps the framework easier to browse, easier to teach, and easier to combine with other extensions over time.

Need the exact folder ownership later? Use the [top-level folder definitions](../framework/top-level-folder-definitions.md).
