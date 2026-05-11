# Extension README Guide

Use this page to write a README that helps people understand what an extension does, when to use it, and how to begin safely. It should work like a landing page for humans, not like a thin wrapper around deeper doctrine.

Need the canonical document-role rules? See:
- [Extension README role](../../../core/authority/extensions/extension-document-roles.md#extension-readme-role)
- [Extension document roles](../../../core/authority/extensions/extension-document-roles.md)
- [Document design principles](../../../core/authority/shared/document-design-principles.md)

## Mental model

Think about an extension README as the landing page for the extension.

Put yourself in the shoes of a first-time visitor and ask:
- What does this extension do?
- What should I run first?
- What artifacts does it usually read or produce?
- What deeper files should I open next if I need more detail?

## A useful README shape

A good extension README often helps with:
- purpose
- default public entrypoint
- other important public entrypoints when present
- hooks contributed or consumed when relevant
- important artifacts read or produced
- dependencies when they materially matter
- the next deeper files to read

## Keep it human-first

Use the README to orient readers quickly.

Do not try to turn it into the entire extension contract. The README should help a human or LLM find the right deeper surfaces, not replace those surfaces.

## Use references when readers may need to go deeper

A strong README can link to:
- deeper extension docs
- key Specs
- public entrypoints
- important example artifacts
