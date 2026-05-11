# system-design-agent artifact map

This page is for quick navigation. Governing artifact obligations live in the corresponding Specs.

## Main reads

System Design reads completed Requirements artifacts from the Requirements step:

- `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`
- `_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md` when present/relevant
- `_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md` when present
- `_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md` when present

System Design also reads existing design artifacts when refining or rerunning:

- `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`
- `_hirmos/artifacts/sot/SYSTEM_SOT.md`
- `_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`
- `_hirmos/artifacts/sot/PHASES_SOT.md`
- `_hirmos/artifacts/sot/PRESENTATION_SOT.md` when present
- `_hirmos/artifacts/phases/*`

## Main writes

- `_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md` when staged delivery is relevant
- `_hirmos/artifacts/sot/SYSTEM_SOT.md`
- `_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`
- `_hirmos/artifacts/sot/PHASES_SOT.md`
- `_hirmos/artifacts/phases/phase_<N>_<slug>_SOT.md`
- system-design-stage trust artifacts under `_hirmos/artifacts/context/system-design-agent/system-design/`

## Requirements ownership

`system-design-agent` no longer owns Requirements production for the regular-user workflow.

Requirements artifacts are produced by:

```text
hirmos requirements
```

The canonical Requirements SOT remains:

```text
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
```


## Serious-cycle trust artifacts

For the public System Design step, trust artifacts live under:

```text
_hirmos/artifacts/context/system-design-agent/system-design/
```

Typical governed artifacts include:

- `CYCLE_STATUS.md` or step status equivalent
- `DECISION_LOG.md` when decisions are made or requested
- `VALIDATION_TRACE.md`
- `RUN_TRACE.md`
- `UNRESOLVED_ITEMS_INVENTORY.md`
- `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
- `UNRESOLVED_ITEMS_FEED.md`
- `UNRESOLVED_ITEMS_LEDGER.md`

## Important ownership reminder

- `_hirmos/artifacts/context/requirements-agent/` is Requirements territory.
- `_hirmos/artifacts/context/system-design-agent/` is System Design territory.
- `_hirmos/artifacts/sot/` and `_hirmos/artifacts/phases/` hold authoritative planning/design outputs.
- `_hirmos/artifacts/prompts/` is downstream Implementation territory, not System Design territory.
