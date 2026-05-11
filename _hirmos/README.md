# _hirmos/

This folder is the governed framework install surface inside a project.

HIRMOS is an open modular framework for Orchestrated Spec-Driven Development. The regular-user workflow is `Requirements → System Design → Implementation`.

If you are new to HIRMOS, do **not** start by browsing everything here. Start with the lightest path that gets you to a successful first run.

## Start here

- Use [Install and Initialize HIRMOS](./docs/1-use-hirmos/getting-started/install-and-initialize.md) when you need the productized `hirmos init` path.
- Use [Docs getting started](./docs/1-use-hirmos/getting-started/README.md) as the canonical first-time-user path.
- Use [Use HIRMOS in 3 Steps](./docs/1-use-hirmos/getting-started/use-hirmos-in-3-steps.md) for the regular-user workflow.
- Use [Installed extensions](./extensions/README.md) when you want to see what capabilities are available in this project.
- Use the [Top-level folder definitions](./core/authority/framework/top-level-folder-definitions.md) only when you need the canonical ownership rules for `_hirmos/` surfaces.

## Other top-level surfaces you may need later

- `_hirmos/integrations/` — HIRMOS-owned integrations; v1 uses `integrations/agent-tools/` for agent/IDE/tool bootstrap templates
- `_hirmos/core/` — minimal framework core and runtime behavior
- `_hirmos/core/authority/` — central authoritative doctrine lanes
- `_hirmos/extensions/` — installed extensions
- `_hirmos/docs/` — user-facing guidance, onboarding, and extension/contribution pathways
- `_hirmos/inputs/` — raw extension-owned runtime inputs
- `_hirmos/artifacts/` — grouped project/runtime/generated artifact families
- `_hirmos/stacks/` — installed stack packages
- `_hirmos/tools/` — HIRMOS-maintained developer tooling, including the TypeScript `hirmos init` CLI
- `_hirmos/extensions/_templates/` — maintainer-facing starter and scaffolding templates

## Usage posture

Most users should enter through `docs/` or `extensions/`, not through deeper authority surfaces.

Use `core/authority/` only when you need canonical rules, contracts, or ownership boundaries.

## Canonical ownership rule

For canonical ownership and allowed-usage rules for top-level framework folders, see [Top-level folder definitions](./core/authority/framework/top-level-folder-definitions.md).
