# requirements-agent Artifact Map

## Primary artifacts

| Artifact | Path | Role |
|---|---|---|
| Requirements input pack | `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md` | Normalized requirements intake and analysis artifact. Not Source of Truth. |
| Requirements SoT | `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md` | Canonical requirements baseline for System Design. |

## Unresolved-item artifacts

When unresolved assumptions, open questions, or gated requirements decisions exist, use the existing HIRMOS unresolved-item governance artifact names under the project-level canonical context:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

Do not create a Requirements-only unresolved-decision bypass artifact.
