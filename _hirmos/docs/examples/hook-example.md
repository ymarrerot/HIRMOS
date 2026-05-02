# Example: Hook System v1

This example shows one extension exposing a hook and one extension subscribing to it.

## Owning extension

```yaml
id: system-design-agent
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - runnable
summary: Design workflows and design artifacts.
entry: entrypoints/system-design-cycle.md
entrypoints:
  system-design-cycle: entrypoints/system-design-cycle.md
exposes_hooks:
  - name: system-design-agent.system-design-cycle.before-requirements-normalization
    entrypoint: system-design-cycle
    phase: before-requirements-normalization
    summary: Runs before requirements intake normalization for system design.
```

## Subscriber extension

```yaml
id: prototype-ingestion
version: 1.0.0
requires_core: ">=1.0.0 <2.0.0"
types:
  - hook
summary: Adds optional prototype-driven design input enrichment.
hooks:
  - target: system-design-agent.system-design-cycle.before-requirements-normalization
    file: hooks/system-design-cycle.before-requirements-normalization.md
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
