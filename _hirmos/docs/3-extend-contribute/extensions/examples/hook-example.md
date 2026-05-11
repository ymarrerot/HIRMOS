# Example: Hook System v1

This example shows one extension exposing a hook and one extension subscribing to it.

## Owning extension

```yaml
id: requirements-agent
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Requirements workflows and requirements artifacts.
entry: entrypoints/requirements.md
entrypoints:
  requirements: entrypoints/requirements.md
exposes_hooks:
  - name: requirements-agent.requirements.before-requirements-normalization
    entrypoint: requirements
    phase: before-requirements-normalization
    summary: Runs before requirements normalization in the Requirements step.
```

## Subscriber extension

```yaml
id: prototype-ingestion
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - hook
summary: Adds optional prototype-driven requirements input enrichment.
hooks:
  - target: requirements-agent.requirements.before-requirements-normalization
    file: hooks/requirements-agent.requirements.before-requirements-normalization.md
    priority: 10
```

## Ordering note

If another subscriber uses priority `20`, the `priority: 10` subscriber runs first.

## Reporting expectation

A trustworthy run should make visible:
- the exposed hook considered
- the matched subscribers
- their priority order
- any material effect on the run
