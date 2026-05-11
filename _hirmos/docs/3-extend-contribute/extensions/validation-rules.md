# Validation Guide

Use this page to understand the kinds of validation a well-formed extension and the framework usually care about during normal authoring and packaging work. It is a practical guide to what tends to be checked and why.

Need the canonical validation rules? See:

- [Extension validation](../../../core/authority/extensions/validation.md)
- [Validation and ordering](../../../core/authority/core/validation-and-ordering.md)
- [Extension manifest authority](../../../core/authority/core/extension-manifest-authority.md)
- [Versioning contract](../../../core/authority/framework/versioning-contract.md)

## What validation usually checks

At a practical level, validation commonly checks things like:

- one manifest per extension folder;
- valid extension version and core-compatibility fields;
- folder name matches extension id;
- runnable extensions expose valid public entry files;
- default `entry` resolves to an existing file;
- named public entrypoints resolve to existing files;
- declared dependencies exist;
- declared hook files exist before loading;
- unsupported or missing hook targets are handled according to the current Core contract.

## What this means for extension authors

Use validation to catch contract mistakes early.

A healthy extension makes its public surfaces explicit and keeps private internals private.

For serious workflow extensions, validation should also protect:

- completed/paused/failed terminal-state integrity;
- evidence-backed completion;
- unresolved-item contribution through the existing governance path;
- hook traceability;
- no hidden bypasses around Core controls.

## Front-door extension quality bar

Official workflow extensions should pass a higher practical bar:

```text
requirements-agent      → produces governed Requirements artifacts
system-design-agent     → produces governed System Design artifacts
implementation-agent    → produces approval-gated Implementation and Evidence-backed Review
```

Each should expose a default public entrypoint through `entry` and preserve narrower named entrypoints only when they avoid duplication and drift.

## When to go deeper

Use the Core Specs above when you need the exact runtime validation behavior rather than this practical summary.
