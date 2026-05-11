# Stack Consumption for Extensions

Use this page when you want practical guidance for making an extension behave well across different project stacks. In SDLC terms, stack-aware extensions help governed work stay aligned with the technical environment chosen for design, planning, and implementation.

Need the deeper doctrine and Core-local stack mechanics? See:
- [Extension stack consumption](../../../core/authority/extensions/stacks.md)
- [Stack system](../../../core/authority/core/stack-system.md)
- [Extension manifest authority](../../../core/authority/core/extension-manifest-authority.md)

For user-facing Core and framework context, see:
- [Core stack subsystem](../core/stacks.md)
- [Stacks](../../reference/stacks.md)

## When stack awareness is useful

Some extensions need stack-aware behavior.

Examples:
- design-side extensions may need architecture and standards context
- implementation-side extensions may need commands and execution rules
- future community extensions may need either or both

## Practical consumption rule

If your extension is stack-aware, read stack context through the canonical Core path rather than inventing a separate stack discovery mechanism.

## Good consumption pattern

Read only the stack surfaces your extension actually needs.

Do not hardcode assumptions when the stack manifest already declares the authoritative mapping.

## Design guidance

- keep stack consumption explicit in your extension docs or deeper governance surface
- do not make your extension own the stack itself
- do not duplicate stack-specific content inside the extension when the stack package already provides it
