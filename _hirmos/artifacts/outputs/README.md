# _hirmos/artifacts/outputs/

Authoritative top-level folder definition: see [_hirmos/core/authority/framework/top-level-folder-definitions.md](../../core/authority/framework/top-level-folder-definitions.md).

`_hirmos/artifacts/outputs/` is the governed top-level output folder for extension-owned result artifacts and deliverables intended for human consumption, approval, handoff, or external/system consumption.

Use namespaced paths:
- `_hirmos/artifacts/outputs/<extension-id>/...`

Use it for non-authoritative result surfaces that are meant to be consumed by humans or external workflows.

Examples:
- client-facing deliverables
- exported summaries
- extension-owned reports intended for downstream use
- review artifacts intended for approval, marketplace review, or API-returned result surfaces

Do not create new top-level output folders like `_hirmos/client/`, `_hirmos/reports/`, or `_hirmos/exports/` from inside an extension.

If a new top-level output folder is ever truly needed, it should be introduced as a framework decision, not invented by one extension.
