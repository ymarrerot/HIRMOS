# Extension Authoring Guidance

Use this lane when you want to understand, design, build, extend, package, or contribute HIRMOS extensions. Most users do not need this lane during normal onboarding or normal project use.

This lane is part of:

```text
Track 2 — Extend & Contribute to HIRMOS
```

If you want to run HIRMOS on a software project, start with [Use HIRMOS in 3 Steps](../../1-use-hirmos/getting-started/use-hirmos-in-3-steps.md). If you want to discover available extensions, go to [hirmos.dev](https://hirmos.dev). If you want to browse the extensions already installed in this project, go to the [Installed extensions guide](../../../extensions/README.md).

## Start here

- [Extend & Contribute to HIRMOS](../README.md) — the Track 2 pathway
- [Overview](overview.md) — the extension-authoring mental model
- [Creating your first extension](creating-your-first-extension.md) — the smallest runnable authoring path
- [Public entrypoints](public-entrypoints.md) — how to expose the right runnable surface
- [Beyond Clear Specs](../../2-methodology/beyond-clear-specs.md) — the methodology-level reliability pattern
- [Applying Beyond Clear Specs in extensions](beyond-clear-specs.md) — how extension authors apply the pattern safely

## Go next

- [Cycles and entrypoints](cycles-and-entrypoints.md) — when to expose a high-level governed workflow for a whole stage of work
- [Spec-backed entrypoints](spec-backed-entrypoints.md) — how serious extension surfaces stay governed
- [Hooks authoring](hooks-authoring.md) — how to expose and consume bounded extension hooks
- [Reusing existing extensions](reusing-existing-extensions.md) — compose existing extension surfaces cleanly
- [Extending existing extensions](extending-existing-extensions.md) — extend behavior without forking when possible
- [Stack consumption](stack-consumption.md) — how extensions consume stack surfaces without owning the stack system

## Advanced reference

- [Validation rules](validation-rules.md)
- [Naming conventions](naming-conventions.md)
- [Best practices](best-practices.md)
- [Large extension structure](large-extension-structure.md)
- [Extension README contract](extension-readme-contract.md)

## Extension authoring posture

A simple way to place extension authoring work is:

- entrypoints give operators runnable surfaces for real work;
- cycles or high-level entrypoints may govern broader lifecycle steps;
- lower-level entrypoints support narrower tasks, reruns, or utilities inside those stages;
- hooks help extensions collaborate without collapsing boundaries;
- serious outputs should support completed, paused, or failed terminal states with evidence.

## Role-focused extensions

HIRMOS can describe some official extensions by the lifecycle role they support.

For the regular-user workflow:

```text
Requirements   → requirements-agent
System Design  → system-design-agent
Implementation → implementation-agent
```

These official extensions provide the practical command-backed front door. Use the supported `hirmos <command>...` commands shown in the getting-started docs.

## Need the canonical extension rules?

Stay in this lane for practical authoring guidance first. When you need the exact extension rule, go to the [extension authority](../../../core/authority/extensions/) or the local `specs/` folder inside the extension you are working on.

## Go next

- **Return to the broader docs hub:** go to the [Documentation hub](../../README.md).
- **Browse extensions for real project use instead:** go to the [Installed extensions guide](../../../extensions/README.md) or discover extensions at [hirmos.dev](https://hirmos.dev).
