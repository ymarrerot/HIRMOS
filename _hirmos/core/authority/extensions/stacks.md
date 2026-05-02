# Extension Stack Consumption

## Purpose

Define the framework-wide extension doctrine for stack-aware behavior.

Use this authority file when deciding:
- when an extension should be stack-aware
- how an extension should consume stack context
- what an extension may assume versus what it should resolve through the Core and stack manifests

For Core-local stack mechanics, see:
- [Stack system](../core/stack-system.md)
- [Stack package contract](../core/stack-system.md#stack-package-contract)

## When stack awareness is appropriate

An extension should be stack-aware only when stack context materially changes the extension's governed behavior.

Examples include:
- design-side standards and architecture context
- implementation-side commands or execution rules
- stack-provided constraints that genuinely affect workflow output

Do not make an extension stack-aware just because the concept exists.

## Consumption rule

If an extension is stack-aware, it should read stack context through the canonical Core and stack surfaces rather than inventing a separate stack discovery mechanism.

The extension consumes stack information. It does not own the stack.

## Assumption discipline

An extension should not hardcode assumptions when the stack manifest or Core-resolved stack surfaces already provide the authoritative mapping.

Read only the stack surfaces the extension actually needs.

## Duplication boundary

Do not duplicate stack-specific doctrine inside the extension when the stack package already provides the authoritative content.

An extension may summarize stack implications locally when that helps its users, but the authoritative stack-owned content should remain in stack surfaces.

## Review tests

When reviewing stack-aware behavior, ask:
- Is stack awareness actually necessary?
- Does the extension read stack context through canonical surfaces?
- Does the extension avoid inventing its own stack discovery mechanism?
- Does the extension avoid duplicating stack-owned doctrine locally?
