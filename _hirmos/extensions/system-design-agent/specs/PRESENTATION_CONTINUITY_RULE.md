# Presentation Continuity Rule

## Purpose

Define the single governing rule for how `system-design-agent` consumes normalized presentation truth without becoming the presentation-domain specialist.

## Rule

When _hirmos/artifacts/context/presentation-design/PRESENTATION_INPUT_PACK.md (`/_hirmos/artifacts/context/presentation-design/PRESENTATION_INPUT_PACK.md`) exists and preserves canonical unresolved items, it is itself a canonical unresolved-item producer and must contribute into its own producer-scoped section of the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact.

When _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`) exists, `system-design-agent` must treat it as the primary normalized presentation-design input and preserve all implementation-relevant presentation constraints through downstream unified design outputs and final implementation-agent prompts. Materially relevant unresolved presentation items should remain visible locally through explicit `Assumptions` and `Open Questions` sections in presentation artifacts where appropriate, and they must also contribute into the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact through a producer-scoped contribution section using the governed unresolved-item contribution model defined in `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md` and any compatible system-design-agent local contract. `PRESENTATION_SOT.md` is itself a canonical unresolved-item producer when it exists; contribution from `_hirmos/artifacts/context/presentation-design/PRESENTATION_INPUT_PACK.md` does not substitute for contributing canonical unresolved items preserved in `_hirmos/artifacts/sot/PRESENTATION_SOT.md`. They must not create a parallel presentation-only classification lane.

## Boundaries

- `system-design-agent` owns the final integrated project-design decisions when presentation constraints materially affect architecture, phase shape, implementation planning, or final implementation-agent prompts.
- `system-design-agent` does **not** become the specialist interpreter of raw presentation materials, assets, templates, screenshots, or design-tool exports.
- Supporting presentation context artifacts may clarify `PRESENTATION_SOT.md`, but they must not become parallel planning-truth surfaces.
- `presentation-design` and other supporting extensions may surface locally owned unresolved presentation items and contribute them into producer-scoped sections of the project-level canonical inventory artifact, but `system-design-agent` remains the owner of the central unresolved-item inventory, reconciliation model, feed, and final completion validity.

## Materiality guidance

Normalized presentation constraints are materially relevant when they affect one or more of:
- architecture or application structure
- phase boundaries or sequencing
- shared UI foundation work
- UX-heavy flows or onboarding shape
- asset usage requirements
- template adaptation requirements
- final implementation prompt content

## Local application rule

Local system-design-agent specs may reference this rule and the generalized unresolved-item contribution contract at `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md`, and apply only the cycle-specific consequences. They should not restate the full policy in divergent wording or invent ad hoc unresolved-item routing rules.

## Propagation rule

`system-design-agent` should not force all presentation meaning into _hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`) or _hirmos/artifacts/sot/REQUIREMENTS_SOT.md (`/_hirmos/artifacts/sot/REQUIREMENTS_SOT.md`).

Instead, when normalized presentation constraints materially affect requirements meaning, system design, phase design, implementation planning, final implementation-agent prompts, or customer-facing solution framing, `system-design-agent` must preserve those consequences in the relevant downstream artifact(s). Otherwise, the presentation-specific truth may remain primarily governed by _hirmos/artifacts/sot/PRESENTATION_SOT.md (`/_hirmos/artifacts/sot/PRESENTATION_SOT.md`).