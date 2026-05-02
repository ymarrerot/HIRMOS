# Folder Rules

## Purpose

Define what `/_hirmos/core/authority/extensions/` is for, what it owns, what it must not own, and which nearby folders it is commonly confused with.

## This folder owns

- framework-wide extension doctrine
- extension authoring standards
- extension-side contract guidance
- extension topic standards such as manifests, entrypoints, hooks, validation, naming, stacks, and lifecycle/cycles

## This folder must not own

- Core internal behavior
- user-facing tutorials and examples
- single-extension local operational method
- broader framework doctrine that belongs in `/_hirmos/core/authority/framework/`

## Common boundary confusions

Most common confusions:
- `/_hirmos/core/authority/core/`
- `/_hirmos/docs/extensions/`
- `/_hirmos/core/authority/framework/`

## If you are unsure

Ask:
- Is this the **framework-wide rule or standard for how extensions should be designed or declared**?

If yes, it likely belongs here.

## Related doctrine

- [Cross-folder rules](../shared/cross-folder-rules.md)
- [Extension document roles](./extension-document-roles.md)
