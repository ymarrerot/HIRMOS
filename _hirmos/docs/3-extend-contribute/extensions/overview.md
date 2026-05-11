# Extension Authoring Overview

Extension authoring should follow a low-to-high cognitive-load path.

## Start with the simplest mental model

An extension is an installable package that adds framework behavior without forcing that behavior into the Core.

A good extension usually has three important qualities:

- a clear public surface;
- a coherent internal boundary;
- governed runtime behavior.

## HIRMOS should not become a black box

HIRMOS gives regular users a simple path to use the framework, but extension authors need a transparent path into the mechanics.

That is why this lane exists:

```text
Extend & Contribute to HIRMOS
```

It should guide authors through the mechanics without duplicating authoritative doctrine.

## SDLC anchor

Many users find it easiest to place extensions by the kind of work they support. For example, an extension may help govern requirements, system design, implementation, presentation, solution briefs, or supporting utility work.

For the regular-user greenfield workflow, the official role-focused extension path is:

```text
Requirements   → requirements-agent
System Design  → system-design-agent
Implementation → implementation-agent
```

This gives extension authors a familiar lifecycle anchor without changing the Core/extension architecture.

## The most common authoring goals

1. create a new extension family;
2. reuse existing public extension surfaces in a custom flow;
3. extend an existing extension through hooks instead of forking when possible;
4. prepare a private, community, or marketplace-ready extension;
5. contribute framework improvements without duplicating doctrine.

## A lesson many authors learn later than they should

Clear specs are necessary, but they are only the first step. As extension work becomes more real, more branched, or more trust-sensitive, you eventually reach the point where **clear specs are not enough**.

For the SDD movement, the same lesson can be expressed this way:

```text
Specs are not enough.
```

Specs can define what should be built, but serious HIRMOS extensions must also govern how the work is executed, validated, paused, completed, and surfaced.

Read [Beyond Clear Specs methodology](../../2-methodology/beyond-clear-specs.md) and [extension application guide](beyond-clear-specs.md) early so you do not have to learn it only after repeated misses.

## A good authoring path

### Lowest cognitive load

- [Creating your first extension](creating-your-first-extension.md)
- [Public entrypoints](public-entrypoints.md)
- [Validation rules](validation-rules.md)

### Next layer

- [Spec-backed entrypoints](spec-backed-entrypoints.md)
- [Large extension structure](large-extension-structure.md)
- [Stack consumption](stack-consumption.md)

### Then go deeper when needed

- [Hooks authoring](hooks-authoring.md)
- [Reusing existing extensions](reusing-existing-extensions.md)
- [Extending existing extensions](extending-existing-extensions.md)
- [Best practices](best-practices.md)

## Public surface first

When designing an extension, start with the public surface before the internal details.

That means defining:

- what commands the Orchestrator should be able to run;
- which entrypoint is the default public surface, if the extension has one;
- which entrypoints are lower-level reusable surfaces;
- what the extension should keep private;
- what evidence the extension must surface before claiming completion.

## Grow the governance only when the work needs it

For small examples, a simple public entrypoint may be enough.
For more serious workflows, a Spec-backed model usually becomes worthwhile because it helps preserve:

- quality checks;
- honest pause/completion behavior;
- artifact discipline;
- reusable workflow method without overloading one entrypoint file.

## Runtime identity metadata

Serious runnable extensions may also declare optional runtime identity metadata in `extension.yaml`, such as:

```yaml
runtime:
  category: agent
  identity: Example Agent
```

Use this when the operator should be able to see which runtime layer is actively executing the command. The manifest declares the identity value; the core handles whether and how that identity is shown.

## Practical companion guides

- `extend-and-contribute-to-hirmos.md` — the Track 2 pathway
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

Need the exact folder ownership later? Use the [top-level folder definitions](../../reference/top-level-folder-definitions.md).
