# Extension Authoring Guidance

Use this lane when you want to understand, design, build, or extend HIRMOS extensions. Most users do not need this lane during normal onboarding or normal project use.

This lane is **not** the main place to discover marketplace extensions or browse installed extensions for normal project use. If you want to discover available extensions, go to [hirmos.dev](https://hirmos.dev). If you want to browse the extensions already installed in this project, go to the [Installed extensions guide](../../extensions/README.md).

## Start here

- [Overview](./overview.md) — the extension-authoring mental model
- [Creating your first extension](./creating-your-first-extension.md) — the smallest runnable authoring path
- [Public entrypoints](./public-entrypoints.md) — how to expose the right runnable surface
- [Beyond Clear Instructions](./beyond-clear-instructions.md) — how to apply the rule that clear instructions should be paired with self-validation, and when to escalate to templates, governed outputs, and fail-closed behavior

## Go next

- [Cycles and entrypoints](./cycles-and-entrypoints.md) — when to expose a high-level governed workflow for a whole stage of work
- [Spec-backed entrypoints](./spec-backed-entrypoints.md) — how serious extension surfaces stay governed
- [Hooks authoring](./hooks-authoring.md) — how to expose and consume bounded extension hooks
- [Reusing existing extensions](./reusing-existing-extensions.md) — compose existing extension surfaces cleanly
- [Extending existing extensions](./extending-existing-extensions.md) — extend behavior without forking when possible
- [Stack consumption](./stack-consumption.md) — how extensions consume stack surfaces without owning the stack system

## Advanced reference

- [Validation rules](./validation-rules.md)
- [Naming conventions](./naming-conventions.md)
- [Best practices](./best-practices.md)
- [Large extension structure](./large-extension-structure.md)
- [Extension README contract](./extension-readme-contract.md)

## SDLC anchor

A simple way to place extension authoring work is:
- entrypoints give operators runnable surfaces for real work
- cycles usually govern broader SDLC stages
- lower-level entrypoints support narrower tasks, reruns, or utilities inside those stages
- hooks help extensions collaborate without collapsing boundaries

## Need the canonical extension rules?

Stay in this lane for practical authoring guidance first. When you need the exact extension rule, go to the [extension authority](../../core/authority/extensions/) or the local `specs/` folder inside the extension you are working on.

## Go next

- **Return to the broader docs hub:** go to the [Documentation hub](../README.md).
- **Browse extensions for real project use instead:** go to the [Installed extensions guide](../../extensions/README.md) or discover extensions at [hirmos.dev](https://hirmos.dev).
