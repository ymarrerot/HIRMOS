# Folder Rules

## Purpose

Define what `/_hirmos/core/authority/core/` is for, what it owns, what it must not own, and which nearby folders it is commonly confused with.

## This folder owns

- authoritative Core-local behavior
- Core interpretation semantics
- Core execution mechanics
- Core command semantics
- Core validation and ordering internals
- Core runtime internals

## This folder must not own

- extension author tutorials or best practices
- framework-wide doctrine that is not Core-local
- user-facing onboarding, walkthroughs, or examples
- framework-wide review-grounding doctrine

## Common boundary confusions

Most common confusions:
- `/_hirmos/core/authority/framework/`
- `/_hirmos/core/authority/extensions/`
- `/_hirmos/docs/core/`

Use `/_hirmos/core/authority/framework/` when the question is about a framework-wide rule or standard rather than how the Core behaves internally.

Use `/_hirmos/core/authority/extensions/` when the question is about framework-wide extension doctrine rather than Core runtime behavior.

Use `/_hirmos/docs/core/` when the content teaches humans how to understand or use the Core rather than defining canonical Core-local rules.

## If you are unsure

Ask:
- Does this answer **how the Core behaves or interprets something**?

If yes, it likely belongs here.

## Related doctrine

- [Cross-folder rules](../shared/cross-folder-rules.md)
- [Core authority README](./README.md)
