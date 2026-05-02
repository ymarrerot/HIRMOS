# _hirmos/artifacts/context/

Authoritative top-level folder definition: see [_hirmos/core/authority/framework/top-level-folder-definitions.md](../../core/authority/framework/top-level-folder-definitions.md).

This folder holds normalized, non-authoritative runtime context artifacts used by extensions during planning, analysis, review, and related workflows.

## Organization rule
By default, context artifacts should be organized by owning extension:

```text
_hirmos/artifacts/context/<extension-id>/...
```

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

- `_hirmos/artifacts/context/system-design-agent/REQUIREMENTS_INPUT_PACK.md`
- `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`
- `_hirmos/artifacts/context/system-design-agent/system-design-cycle/CYCLE_STATUS.md`
- `_hirmos/artifacts/context/system-design-agent/system-design-cycle/DECISION_LOG.md`

## Exception rule
Use flat `_hirmos/artifacts/context/` files only when an artifact is intentionally framework-global rather than extension-owned.
