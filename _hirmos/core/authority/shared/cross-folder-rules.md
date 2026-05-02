# Cross-Folder Rules

## Purpose

Define the six active framework folders that carry the main doctrine and guidance load, explain what each folder is for, what each folder must not own, and provide the first routing decision when placement is ambiguous.

This file is the global folder-routing rule for the active folder system.

## The six active folders

- `/_hirmos/core/authority/core/`
- `/_hirmos/core/authority/framework/`
- `/_hirmos/core/authority/extensions/`
- `/_hirmos/docs/framework/`
- `/_hirmos/docs/core/`
- `/_hirmos/docs/extensions/`

## Folder purposes

### `/_hirmos/core/authority/core/`
Use this folder for authoritative Core-local behavior and interpretation.

### `/_hirmos/core/authority/framework/`
Use this folder for framework-wide authoritative doctrine, contracts, and standards that are not Core-internal and not specifically extension-authoring doctrine.

### `/_hirmos/core/authority/extensions/`
Use this folder for framework-wide extension doctrine, authoring standards, and extension-side contracts.

### `/_hirmos/docs/framework/`
Use this folder for user-facing framework guidance, conceptual explanation, and practical orientation.

### `/_hirmos/docs/core/`
Use this folder for user-facing explanation of the Core as a distinct framework entity.

### `/_hirmos/docs/extensions/`
Use this folder for user-facing extension onboarding, tutorials, examples, and practical author guidance.

## What each folder must not own

### `/_hirmos/core/authority/core/` must not own
- extension author tutorials
- framework-wide standards that are not Core-local
- user-facing mental models and walkthroughs

### `/_hirmos/core/authority/framework/` must not own
- Core execution internals
- extension tutorials and examples
- user-facing onboarding

### `/_hirmos/core/authority/extensions/` must not own
- Core internal runtime behavior
- single-extension local operational method
- user-facing tutorials and examples

### `/_hirmos/docs/framework/` must not own
- final framework doctrine
- review-grounding source-of-truth material
- Core-local internals as doctrine

### `/_hirmos/docs/core/` must not own
- canonical Core doctrine
- broader framework doctrine
- extension author standards

### `/_hirmos/docs/extensions/` must not own
- final extension doctrine
- review-grounding source-of-truth material
- Core internals as doctrine

## If you are unsure

Use this decision test:

- If the question is **"How does the Core itself behave or interpret something?"** → `/_hirmos/core/authority/core/`
- If the question is **"What is the framework-wide rule, standard, boundary, or contract?"** → `/_hirmos/core/authority/framework/`
- If the question is **"What is the framework-wide rule or standard for how extensions should be designed or declared?"** → `/_hirmos/core/authority/extensions/`
- If the question is **"How does a human understand, use, or apply this?"** → `/_hirmos/docs/...`

Then refine further:

- If the guidance is about the Core specifically → `/_hirmos/docs/core/`
- If the guidance is about the framework broadly → `/_hirmos/docs/framework/`
- If the guidance is about building or understanding extensions → `/_hirmos/docs/extensions/`

## Common confusions

- `/_hirmos/core/authority/core/` vs `/_hirmos/core/authority/framework/`: Core behavior vs framework-wide doctrine
- `/_hirmos/core/authority/framework/` vs `/_hirmos/core/authority/extensions/`: broader framework doctrine vs extension doctrine
- `/_hirmos/core/authority/extensions/` vs `/_hirmos/docs/extensions/`: authoritative extension doctrine vs user-facing extension guidance
- `/_hirmos/core/authority/core/` vs `/_hirmos/docs/core/`: authoritative Core rules vs reader-friendly Core explanation
- `/_hirmos/core/authority/framework/` vs `/_hirmos/docs/framework/`: authoritative framework doctrine vs framework guidance

## Special case: the `/_hirmos/core/authority/shared/` lane

### What `shared/` owns

Use `shared/` for cross-cutting authority-system rules that:
- govern the authority lane itself; or
- apply broadly across the whole framework rather than belonging specifically in `core/`, `framework/`, or `extensions/`.

Current examples:
- `cross-folder-rules.md`
- `deep-reference-rules.md`
- `document-design-principles.md`

### What `shared/` must not become

Do not let `shared/` become a flat pile of unrelated framework doctrine.

Framework-wide doctrine that is not cross-cutting belongs under:
- `/_hirmos/core/authority/framework/`

Framework-wide extension doctrine belongs under:
- `/_hirmos/core/authority/extensions/`

## Cross-cutting discipline rules

### Reuse over restatement

When a rule, standard, boundary, or doctrine already has an authoritative home, prefer referencing that source rather than restating it locally.

Use:
- a whole-file reference when the entire source is the basis
- a deep reference when a specific section is the true basis

Local restatement is allowed only when:
- it materially improves usability or readability
- the local file must remain self-contained for its operational role
- the restatement is clearly secondary and does not compete with the authoritative source

Avoid:
- duplicating authoritative doctrine across multiple files
- paraphrased copies that can drift
- local files silently re-owning framework-wide rules

### Naming convention for authority files

Use lowercase kebab-case for filenames across `/_hirmos/core/authority/` and extension-local `specs/` folders.

- `lowercase-kebab-case.spec.md` → workflow, command, cycle, or execution-governing extension spec
- `lowercase-kebab-case.md` → authoritative doctrine, policy, standards, role definition, or reference material that is not itself an extension execution spec

## Related doctrine

This file is the first routing layer.

For supporting doctrine, see:
- [Framework document roles](../framework/framework-document-roles.md)
- [Extension document roles](../extensions/extension-document-roles.md)
- [Document design principles](./document-design-principles.md)
- [Deep reference rules](./deep-reference-rules.md)
