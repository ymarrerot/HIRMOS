# Folder Rules

## Purpose

Define what `/_hirmos/docs/extensions/` is for, what it owns, what it must not own, and which nearby folders it is commonly confused with.

## This folder owns

- extension onboarding
- tutorials and examples
- practical author guidance
- human-friendly README guidance
- standalone practical guidance with references into `/_hirmos/core/authority/extensions/` and `/_hirmos/core/authority/core/` only when deeper authoritative detail is needed

## This folder must not own

- final extension doctrine
- review-grounding source-of-truth material
- Core internals as doctrine

## Common boundary confusions

Most common confusions:
- `/_hirmos/core/authority/extensions/`
- `/_hirmos/docs/framework/`

## If you are unsure

Ask:
- Is this helping a human **build, understand, or use extensions** rather than defining the final extension rule?

If yes, it likely belongs here.

## Related doctrine

- [Cross-folder rules](../../core/authority/shared/cross-folder-rules.md)
- [Document design principles](../../core/authority/shared/document-design-principles.md)
- [Docs authoring contract](../../core/authority/framework/docs-authoring-contract.md)
