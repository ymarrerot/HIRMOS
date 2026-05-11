# system-design-agent entrypoints

This page is for people deciding which `system-design-agent` entrypoint to run.
For detailed behavioral truth, use the corresponding Spec.

## Start with this in most cases

- `system-design`

Use it when you want the HIRMOS **System Design** step after Requirements have been produced by `requirements-agent`.

Equivalent user command:

```text
hirmos system-design
```

## Public lifecycle entrypoint

### `system-design`

Use when you want the governed System Design step for a project or major change.

This entrypoint consumes Requirements artifacts such as `REQUIREMENTS_SOT.md`, then produces or refines system design, architecture, phase planning, staged delivery, unresolved-item, and trust artifacts needed before Implementation.

## Advanced/reusable lifecycle subcycles

### `system-design-cycle`

Use when you intentionally need the narrowed system-level design subcycle.

This cycle consumes Requirements artifacts produced by `requirements-agent`, produces system-level design artifacts, runs system-design-stage unresolved-item governance, and preserves the original System Design reliability discipline without re-owning Requirements.

Most regular users should run `hirmos system-design`, which composes this cycle with `phase-design-cycle`.

### `phase-design-cycle`

Use when you intentionally want a governed design pass focused on phase-level refinement.

For normal greenfield System Design, the public `system-design` entrypoint runs this cycle after the narrowed `system-design-cycle` completes and after gated blockers to phase design are resolved.

## Lower-level reusable entrypoints

### `staged-delivery-targets`
Use when you need staged delivery shape before or alongside deeper design work.

### `system-sot`
Use when you need the authoritative system-level design artifact.

### `architecture-sot`
Use when you need the authoritative architecture artifact.

### `phases-sot`
Use when you need the authoritative phase structure for the project.

### `phase-sot`
Use when you need one phase artifact refined or generated directly.

## Prototype and presentation note

Prototype and presentation enrichment hooks now target the Requirements stage for requirements enrichment and the System Design stage for design-stage unresolved contributions where appropriate. Check extension integration docs and manifests for the exact hook seams.

## Stack-aware vs stack-neutral design surfaces

Use the active stack only where the governing Spec justifies it.

- `system-design`: stack-aware as orchestration layer
- `architecture-sot`: direct stack consumer
- `system-sot`: stack-neutral
- `phases-sot`: primarily stack-indirect

## Reading order

Low cognitive load:
- start here for entrypoint selection

Deeper references:
- the entrypoint file for Purpose / Produces / Terminal States and required terminal templates where present
- the corresponding Spec for behavioral truth
- `specs/system-design.spec.md` for the default public System Design step
- `specs/system-design-cycle.spec.md` for the narrowed system-level design subcycle
- `specs/phase-design-cycle.spec.md` for phase-level design
- `specs/CYCLE_VALIDITY_SPINE.md` for serious-cycle finalization checks

## Unresolved-item centralization model

`system-design` composes unresolved-item outputs from the narrowed `system-design-cycle` and final System Design review.

System-design-stage unresolved trust artifacts may live under the public step scope and/or the narrowed cycle scope:

```text
/_hirmos/artifacts/context/system-design-agent/system-design/
/_hirmos/artifacts/context/system-design-agent/system-design-cycle/
```

with the existing artifact names:

- `UNRESOLVED_ITEMS_INVENTORY.md`
- `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
- `UNRESOLVED_ITEMS_FEED.md`
- `UNRESOLVED_ITEMS_LEDGER.md`

Requirements-stage unresolved artifacts are produced by `requirements-agent` and consumed as upstream inputs.
