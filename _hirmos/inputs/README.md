# _hirmos/inputs/

Authoritative top-level folder definition: see [_hirmos/core/authority/framework/top-level-folder-definitions.md](../core/authority/framework/top-level-folder-definitions.md).

`_hirmos/inputs/` stores raw extension-owned runtime inputs before normalization.

Use namespaced paths:
- `_hirmos/inputs/<extension-id>/...`

Examples:
- `_hirmos/inputs/system-design-agent/requirements/`
- `_hirmos/inputs/prototype-ingestion/prototypes/`

Normalized working artifacts belong in `_hirmos/artifacts/context/`. Authoritative outputs belong in locations such as `_hirmos/artifacts/sot/`, `_hirmos/artifacts/phases/`, or extension-specific output paths defined by the relevant extension.