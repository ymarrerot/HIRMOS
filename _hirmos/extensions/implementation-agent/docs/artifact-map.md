# implementation-agent artifact map

This page is for quick navigation. Governing artifact obligations live in the corresponding Specs.

## Main reads

The public Implementation step reads approved upstream implementation scope, including:

- `_hirmos/artifacts/sot/REQUIREMENTS_SOT.md` when relevant for traceability
- `_hirmos/artifacts/sot/SYSTEM_SOT.md`
- `_hirmos/artifacts/sot/ARCHITECTURE_SOT.md`
- `_hirmos/artifacts/sot/PHASES_SOT.md`
- `_hirmos/artifacts/phases/`
- `_hirmos/artifacts/prompts/` when planning already exists
- active stack surfaces resolved through `_hirmos/project.json`
- implementation repository files and repository-local command surfaces

## Main writes

### Public Implementation step

- `_hirmos/artifacts/context/implementation-agent/implementation/CYCLE_STATUS.md`
- `_hirmos/artifacts/context/implementation-agent/implementation/RUN_TRACE.md`
- `_hirmos/artifacts/context/implementation-agent/implementation/VALIDATION_TRACE.md`
- `_hirmos/artifacts/context/implementation-agent/implementation/DECISION_LOG.md` when decisions are made or requested

### Implementation planning

- `_hirmos/artifacts/prompts/phase-<NN>-<slug>/PROMPT_PLAN.md`
- `_hirmos/artifacts/prompts/phase-<NN>-<slug>/P<phase>-<index>-<slug>.md`
- `_hirmos/artifacts/context/implementation-agent/implementation-planning-cycle/` trust artifacts when the planning cycle is reused

### Prompt-level execution record

- `_hirmos/artifacts/ops/runs/<prompt-id>/summary.md`
- `_hirmos/artifacts/ops/runs/<prompt-id>/evidence.md`
- `_hirmos/artifacts/ops/runs/<prompt-id>/patch.diff` when code changed
- `_hirmos/artifacts/ops/reviews/<prompt-id>/...`
- `_hirmos/artifacts/ops/retries/<prompt-id>/...`
- `_hirmos/artifacts/context/implementation-agent/implementation-execution-cycle/` trust artifacts when the execution cycle is reused

### Phase review and Evidence-backed Review

- `_hirmos/artifacts/ops/reviews/<phase-id>-phase-review/`
- phase review artifact following `templates/implementation-execution-cycle/PHASE_REVIEW_TEMPLATE.md` when execution occurs
- final surfaced Implementation output following `templates/implementation/`

## Templates

The public Implementation terminal templates live under:

```text
_hirmos/extensions/implementation-agent/templates/implementation/
```

Retained planning/execution cycle templates live under:

```text
_hirmos/extensions/implementation-agent/templates/implementation-planning-cycle/
_hirmos/extensions/implementation-agent/templates/implementation-execution-cycle/
```

## Important ownership reminder

- `_hirmos/artifacts/prompts/` is owned by the active implementation authority; this extension writes there when selected for implementation work.
- `_hirmos/artifacts/ops/` is the reviewable execution record, not extension trust-state.
- `_hirmos/artifacts/context/implementation-agent/` is the implementation trust-artifact lane.
- The public Implementation step must not treat planning completion as execution completion.
