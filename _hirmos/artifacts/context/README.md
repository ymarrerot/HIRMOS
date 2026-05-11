# _hirmos/artifacts/context/

Authoritative top-level folder definition: see [_hirmos/core/authority/framework/top-level-folder-definitions.md](../../core/authority/framework/top-level-folder-definitions.md).

This folder holds normalized, non-authoritative runtime context artifacts used by extensions during planning, analysis, review, and related workflows.

## Organization rule
By default, context artifacts should be organized by owning extension:

```text
_hirmos/artifacts/context/<extension-id>/...
```

## Project-level context

Use `_hirmos/artifacts/context/project/` for cross-extension project context artifacts that are not owned by one extension but coordinate multiple lifecycle stages or producers.

The canonical unresolved-item governance artifacts live here:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

These are project-level coordination artifacts. They are not Core-owned, and they are not owned by `requirements-agent` or `system-design-agent` alone.

Packaging note:

`_hirmos/artifacts/context/project/` is a framework-level project context namespace and may be present in the framework install package, similar to `_hirmos/artifacts/context/core/`. Extension packages must still not ship their own runtime context folders under `_hirmos/artifacts/context/<extension-id>/`.

## Command-scoped context
When a context artifact is owned by a specific public entrypoint or cycle, it should be scoped under the owning extension and command:

```text
_hirmos/artifacts/context/<extension-id>/<entrypoint-id>/...
```

## Template rule
Extensions may define runtime/context templates under their own context namespace:

```text
_hirmos/artifacts/context/<extension-id>/templates/...
_hirmos/artifacts/context/<extension-id>/<entrypoint-id>/templates/...
```

Templates define structure and governance expectations. They do not count as generated runtime artifacts.

## Ownership rule
A context artifact may be consumed by other extensions, but it should normally be stored under the namespace of the extension that creates or governs it.

## Examples

- `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`
- `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`
- `_hirmos/artifacts/context/system-design-agent/system-design/CYCLE_STATUS.md`
- `_hirmos/artifacts/context/system-design-agent/system-design/DECISION_LOG.md`

## Exception rule
Use flat `_hirmos/artifacts/context/` files only when an artifact is intentionally framework-global rather than extension-owned.
