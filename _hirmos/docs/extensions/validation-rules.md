# Validation Guide

Use this page to understand the kinds of validation a well-formed extension and the framework usually care about during normal authoring and packaging work. It is a practical guide to what tends to be checked and why.

Need the canonical validation rules? See:
- [Extension validation](../../core/authority/extensions/validation.md)
- [Validation and ordering](../../core/authority/core/validation-and-ordering.md)
- [Extension manifest authority](../../core/authority/core/extension-manifest-authority.md)
- [Versioning contract](../../core/authority/framework/versioning-contract.md)

## What validation usually checks

At a practical level, validation commonly checks things like:
- one manifest per extension folder
- valid extension version and core-compatibility fields
- folder name matches extension id
- runnable extensions expose valid public entry files
- named public entrypoints resolve to existing files
- declared dependencies exist
- declared hook files exist before loading
- unsupported or missing hook targets are handled according to the current Core contract

## What this means for extension authors

Use validation to catch contract mistakes early.

A healthy extension makes its public surfaces explicit and keeps private internals private.

Even a simple runnable extension should use the [Beyond Clear Instructions](./beyond-clear-instructions.md) when it can locally self-check whether its clear instructions were followed. Trust-sensitive synthesis and surfaced results usually need the fuller form of the pattern.

## When to go deeper

Use the Core Specs above when you need the exact runtime validation behavior rather than this practical summary.
