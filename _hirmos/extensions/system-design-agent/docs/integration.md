# system-design-agent integration

`system-design-agent` is the official HIRMOS extension for the **System Design** step.

Workflow placement:

```text
Requirements → System Design → Implementation
```

The default public command is:

```text
hirmos system-design
```

## Upstream dependency

System Design depends on completed Requirements artifacts from `requirements-agent`.

Required upstream artifact:

```text
_hirmos/artifacts/sot/REQUIREMENTS_SOT.md
```

Relevant upstream context when present:

```text
_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

If Requirements artifacts are missing or unusable, System Design must pause and direct the Orchestrator to run or repair:

```text
hirmos requirements
```

## Downstream consumers

The common downstream consumer is:

```text
hirmos implementation
```

Implementation should consume System Design outputs such as:

- `SYSTEM_SOT.md`
- `ARCHITECTURE_SOT.md`
- `PHASES_SOT.md`
- phase-level SOT artifacts under `_hirmos/artifacts/phases/`
- staged delivery context when relevant

## Supporting extensions

Prototype and presentation extensions may enrich Requirements and System Design.

Requirements-stage enrichment hooks now target `requirements-agent` hook seams. Design-stage unresolved-item contribution can target the System Design step when presentation, prototype, or other extension-specific consequences materially affect design or phase planning.

Current important seams include:

```text
requirements-agent.requirements.before-input-discovery
requirements-agent.requirements.before-requirements-normalization
requirements-agent.requirements.contribute-unresolved-items
system-design-agent.system-design.contribute-unresolved-items
system-design-agent.system-design.before-final-gating-review
```

## Unresolved-item integration

Requirements-stage unresolved artifacts are upstream inputs.

System-design-stage unresolved items should use the existing unresolved-item artifact names under the System Design run scope.

Do not create separate bypass artifacts for design decisions.
