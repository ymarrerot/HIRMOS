# _hirmos/

This folder is the governed framework install surface inside a project.

If you are new to HIRMOS, do **not** start by browsing everything here. Start with the lightest path that gets you to a successful first run.

## Start here

- Use [Docs getting started](./docs/getting-started/README.md) as the canonical first-time-user path.
- Use [Installed extensions](./extensions/README.md) when you want to see what capabilities are available in this project.
- Use the [Top-level folder definitions](./core/authority/framework/top-level-folder-definitions.md) only when you need the canonical ownership rules for `_hirmos/` surfaces.

## Other top-level surfaces you may need later

- `_hirmos/core/` — minimal framework core and runtime behavior
- `_hirmos/core/authority/` — central authoritative doctrine lanes
- `_hirmos/extensions/` — installed extensions
- `_hirmos/docs/` — user-facing guidance and onboarding
- `_hirmos/inputs/` — raw extension-owned runtime inputs
- `_hirmos/artifacts/` — grouped project/runtime/generated artifact families
- `_hirmos/stacks/` — installed stack packages
- `_hirmos/extensions/_templates/` — maintainer-facing starter and scaffolding templates

## Usage posture

Most users should enter through `docs/` or `extensions/`, not through deeper authority surfaces.

Use `core/authority/` only when you need canonical rules, contracts, or ownership boundaries.

## Canonical ownership rule

For canonical ownership and allowed-usage rules for top-level framework folders, see [Top-level folder definitions](./core/authority/framework/top-level-folder-definitions.md).
