# Top-Level Folder Definitions

Use this page when you want a practical orientation to the main top-level folders under `_hirmos/`. It is most useful after your first successful use, when you start asking where different framework materials usually live.

Need the canonical rule for folder ownership or artifact classification? See [the framework authority file](../../core/authority/framework/top-level-folder-definitions.md).

## Quick orientation

HIRMOS uses a small set of governed top-level framework surfaces directly under `_hirmos/`.

At a glance:
- `_hirmos/core/authority/` — central authoritative doctrine lanes
- `_hirmos/core/` — the minimal framework core and its core-owned surfaces
- `_hirmos/extensions/` — installed extensions
- `_hirmos/stacks/` — installed stack packages
- `_hirmos/extensions/_templates/` — maintainer-facing starter and scaffolding templates
- `_hirmos/inputs/` — raw extension-owned runtime inputs
- `_hirmos/artifacts/` — grouped project/runtime/generated artifact families

Inside `/_hirmos/artifacts/`:
- `/_hirmos/artifacts/context/` — normalized extension-owned runtime context artifacts
- `/_hirmos/artifacts/outputs/` — extension-owned result artifacts and deliverables
- `/_hirmos/artifacts/sot/` — authoritative source-of-truth artifacts
- `/_hirmos/artifacts/phases/` — generated phase contracts
- `/_hirmos/artifacts/prompts/` — generated execution prompts
- `/_hirmos/artifacts/ops/` — canonical implementation-stage operational runtime artifacts

## When to use the authority file instead of this page

Use [_hirmos/core/authority/framework/top-level-folder-definitions.md](../../core/authority/framework/top-level-folder-definitions.md) when you need:
- the canonical meaning of a top-level folder
- ownership and write-boundary rules
- the correct top-level artifact family for a generated artifact
- a review-grounding reference for folder discipline
