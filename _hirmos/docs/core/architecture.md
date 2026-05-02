# Core Architecture

The Core is intentionally small.
That is not an implementation shortcut. It is one of the framework's main architectural rules.

## What the Core owns

The Core owns only the framework-wide mechanics needed to make extension behavior coherent and reliable.

Core responsibilities include:
- bootstrap
- extension discovery
- manifest validation
- public entrypoint resolution
- hook matching and ordering
- run-plan composition
- execution trace output
- project-level stack resolution

## What the Core does not own

The Core should not hold:
- design-specific workflow logic
- implementation-specific workflow logic
- deliverable-specific methods
- domain-specific business behavior
- extension-local quality bars that belong in Specs

Those belong in extensions.

## Why the Core stays small

If the Core absorbs too much workflow intelligence, three things happen:
- extensions become thinner but less meaningful
- reuse gets worse because the Core becomes role-specific
- marketplace/package independence gets weaker

A small Core keeps the framework:
- more modular
- easier to package
- easier to evolve
- easier to extend without forking everything

## Main architectural layers

### Core
The minimal orchestration and validation layer.

### Extensions
Installed packages that provide the real workflow behavior.

### Public entrypoints
The command surface deliberately exposed by an extension.

### Hooks
Optional extension-to-extension augmentation points.

### Specs
Canonical local contracts backing serious workflow entrypoints.

### Private internals
Support files that help an extension stay coherent without exposing every file as public contract.

## A useful design test

When deciding where a rule belongs, ask:

**Does this rule affect the framework as a whole, or does it belong to one extension family?**

- if it affects the framework as a whole, it may belong in the Core
- if it governs one extension family or workflow domain, it belongs in that extension

## Related docs

- `command-protocol.md`
- `loading-and-resolution.md`
- `../framework/runtime-surfaces.md`
- `extension-manifest.md`
