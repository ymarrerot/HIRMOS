# Folder Rules

## Purpose

Define what `/_hirmos/core/authority/framework/` is for, what it owns, what it must not own, and which nearby folders it is commonly confused with.

## This folder owns

- framework-wide doctrine
- framework-wide contracts
- framework-wide standards
- framework-level governance
- framework-level role boundaries
- framework-level folder and trust-surface definitions

## This folder must not own

- Core execution internals
- extension tutorials and examples
- user-facing onboarding and walkthroughs
- extension-authoring doctrine that belongs in `/_hirmos/core/authority/extensions/`

## Common boundary confusions

Most common confusions:
- `/_hirmos/core/authority/core/`
- `/_hirmos/core/authority/extensions/`
- `/_hirmos/docs/3-extend-contribute/framework/`

## If you are unsure

Ask:
- Is this a **framework-wide rule, standard, boundary, or contract**?

If yes, it likely belongs here unless it is clearly Core-local or clearly extension-doctrine.

## Related doctrine

- [Cross-folder rules](../shared/cross-folder-rules.md)
- [Framework document roles](./framework-document-roles.md)
