# Deep Reference Rules

## Purpose

Define the canonical HIRMOS internal reference format for linking from one HIRMOS markdown file to another file or to a specific section inside another file.

This rule is intended to support both:
- human navigation in repository environments such as GitHub and VS Code
- deterministic framework references that authority files, docs, and review artifacts can resolve without guessing

## Canonical internal reference format

When one HIRMOS markdown file references another HIRMOS markdown file, use markdown link syntax with a repository-relative path that resolves correctly from the current file.

Use these forms:
- file reference: `[Link Text](../framework/top-level-folder-definitions.md)`
- deep file-section reference: `[Link Text](../extensions/extension-document-roles.md#extension-level-document-roles)`

Examples:
- [Top-level folder definitions](../framework/top-level-folder-definitions.md)
- [Top-level folder definitions section](../framework/top-level-folder-definitions.md#top-level-framework-surface-definitions)
- [Extension document roles](../extensions/extension-document-roles.md)
- [Extension Specs](../extensions/extension-document-roles.md#extension-specs)

## Relative resolution rule

Resolve internal markdown links relative to the current file so they work correctly in repository viewers and local editors.

This keeps the reference:
- clickable in GitHub, VS Code, and similar repository environments
- precise for framework authority files, docs, and review artifacts
- stable as long as the linked file remains at the same repository location

## When to use relative internal links

Use relative internal links in:
- `/_hirmos/core/authority/`
- extension-local `specs/` files when they reference framework, core, or extension doctrine
- user-facing docs when linking to canonical framework surfaces
- review criteria source maps and similar reference-heavy artifacts

Prefer the shortest clear relative path that resolves from the current file.

## Deep reference rule

A deep reference must identify:
- the target file
- the exact target section anchor inside that file

Example:
- [Extension-level document roles](../extensions/extension-document-roles.md#extension-level-document-roles)

Do not use vague prose such as “section on extension document roles” when the framework expects an exact reference.

## Anchor rule

Section anchors must be derived from the target heading text using standard markdown-style normalization:
- lowercase the heading text
- replace spaces with hyphens
- remove punctuation where the renderer does so
- keep the final anchor readable and stable

Examples:
- `## Extension-level document roles` → `#extension-level-document-roles`
- `### Entrypoints role` → `#entrypoints-role`

## Heading authoring rule for deep-link targets

Sections intended for cross-file deep references must use stable, unnumbered headings.

Prefer:
- `## Extension-level document roles`
- `### Extension docs`

Avoid for deep-link targets:
- `## 2. Extension-level document roles`
- `### 2.2 Extension docs`

If numbering is useful for presentation, keep it outside the canonical heading text.

## Heading clarity rule

Headings intended for deep references should be:
- explicit
- unique enough within the file
- stable over time
- not vague placeholders such as `Overview`, `Notes`, or `More` when a more specific heading is possible

## Human-readable link text

Link text should describe the target plainly.

Prefer:
- `[Extension document roles](../extensions/extension-document-roles.md)`
- `[Top-level folder definitions](../framework/top-level-folder-definitions.md)`

Avoid generic link text such as:
- `here` with a placeholder target
- `this section` with a placeholder target

## Exact-target rule

A deep reference must target an actual heading that currently exists in the target file.

Do not create deep references from paraphrased display labels or inferred wording. Derive the anchor from the literal target heading text.

Prefer this pattern:
- target heading: `### Extension Specs`
- deep reference: `[Extension Specs](../extensions/extension-document-roles.md#extension-specs)`

Avoid this pattern:
- target heading: `### Extension Specs`
- incorrect deep reference created from a paraphrase such as `[Extension specs role](../extensions/extension-document-roles.md#extension-specs)`

## Validation rule

Before a deep reference is committed into an active authority file, review artifact, or user-facing guidance surface, validate that:
- the target file exists
- the target heading exists exactly as referenced
- the generated anchor matches the current target heading
- the deep link resolves to the intended section rather than falling back to the file top

If a deep reference cannot be validated confidently, use a whole-file reference instead of publishing an uncertain deep reference.

## Resolution behavior

When the framework resolves a canonical internal reference:
- if the target includes only a file path, load the full file
- if the target includes `#section-anchor`, load the matching section from the target file

If a deep reference target cannot be found, the framework should fail explicitly rather than guessing.

## Authoritative source versus user-facing navigation

This relative markdown link format is the canonical HIRMOS internal reference format.

It serves both purposes at once:
- clickable navigation for humans in supported environments
- deterministic authoritative references for authority files, reviews, and framework-owned rule surfaces

## Scope note

This rule governs HIRMOS-internal markdown references. It does not attempt to redefine external web links or non-HIRMOS repository navigation.
