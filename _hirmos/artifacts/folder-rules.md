# Folder Rules

## Purpose

`/_hirmos/artifacts/` is the umbrella folder for project/runtime/generated artifact families inside HIRMOS.

It exists to make the install surface easier to understand for first-time visitors by grouping artifact families that were previously separate top-level folders.

## This folder owns

- the shared artifact-family home for:
  - `context`
  - `outputs`
  - `sot`
  - `phases`
  - `prompts`
  - `ops`
- the high-level distinction between:
  - canonical project artifact lanes
  - extension-owned runtime/result lanes
  - implementation operational lanes

## This folder must not own

- framework-wide doctrine that belongs in `/_hirmos/core/authority/framework/...`
- core-local doctrine that belongs in `/_hirmos/core/authority/core/...`
- user-facing framework or extension guidance that belongs in `/_hirmos/docs/...`
- extension package code that belongs in `/_hirmos/extensions/...`

## Common confusions

- `/_hirmos/artifacts/context/` is not the same as `/_hirmos/artifacts/sot/`
- `/_hirmos/artifacts/outputs/` is not the same as `/_hirmos/artifacts/sot/`
- `/_hirmos/artifacts/prompts/` is not the same as `/_hirmos/artifacts/ops/`
- `/_hirmos/artifacts/` is an umbrella folder, not a replacement for the distinct rules of the artifact families inside it

## If you are unsure

- If the content is authoritative doctrine or governance, it does not belong under `/_hirmos/artifacts/`
- If the content is a generated, maintained, or runtime/project artifact family, `/_hirmos/artifacts/` is the correct top-level home
- Then choose the specific artifact family inside `/_hirmos/artifacts/` based on its purpose

## Related doctrine

- [Top-level folder definitions](../core/authority/framework/top-level-folder-definitions.md)
- [Framework operating model](../core/authority/framework/framework-operating-model.md)


## Core-owned runtime context artifacts

- `_hirmos/artifacts/context/core/` is valid for Core-owned runtime context artifacts.
- `_hirmos/artifacts/context/core/bootstrap-report.md` is the canonical bootstrap report path.

## Extension-scoped runtime control artifacts

- `_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/RUN_EXECUTION_CONTROLS.md` is the canonical run execution controls artifact path for extension-scoped runs.
- `_hirmos/artifacts/context/<extension-id>/<extension-entrypoint>/HOOK_EXECUTION_CONTROL.md` is the canonical hook execution control artifact path for hook-aware extension-scoped runs.


## Project-level runtime context artifacts

- `_hirmos/artifacts/context/project/` is valid for cross-extension project context artifacts that are not owned by a single extension.
- The canonical unresolved-item governance artifacts live under `_hirmos/artifacts/context/project/`:
  - `UNRESOLVED_ITEMS_INVENTORY.md`
  - `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
  - `UNRESOLVED_ITEMS_FEED.md`
  - `UNRESOLVED_ITEMS_LEDGER.md`
- These artifacts are project coordination surfaces, not Core-owned runtime controls and not extension-local inventories.
