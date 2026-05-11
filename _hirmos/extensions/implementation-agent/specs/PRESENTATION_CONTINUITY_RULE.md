# Presentation Continuity Rule

## Purpose

Define the local implementation-agent rule for preserving implementation-relevant consequences from normalized presentation artifacts without depending on any particular design-side or presentation-side extension.

## Rule

When `_hirmos/artifacts/sot/PRESENTATION_SOT.md` exists, `implementation-agent` must treat it as an optional normalized project artifact and preserve all implementation-relevant presentation constraints through implementation planning, prompt planning, and final agent prompts.

`implementation-agent` must not require `system-design-agent`, `presentation-design`, or any other specific extension to be installed in order to apply this rule. It consumes normalized project artifacts when they exist; it does not depend on another extension's private specs.

## Boundaries

- `implementation-agent` owns the implementation-side preservation of normalized presentation consequences in implementation plans and generated execution prompts.
- `implementation-agent` does **not** become the specialist interpreter of raw presentation materials, assets, templates, screenshots, or design-tool exports.
- Supporting presentation context artifacts may clarify `PRESENTATION_SOT.md`, but they must not become parallel implementation-truth surfaces.
- If normalized presentation artifacts are absent, implementation-agent must not invent presentation constraints.

## Materiality guidance

Normalized presentation constraints are materially relevant when they affect one or more of:

- implementation architecture or application structure
- phase boundaries, prompt boundaries, or sequencing
- shared UI foundation work
- UX-heavy flows or onboarding shape
- asset usage requirements
- template adaptation requirements
- final agent prompt content
- acceptance criteria, verification, or deliverables

## Local application rule

Local implementation-agent specs may reference this rule and apply only the cycle-specific consequences. They should not restate the full policy in divergent wording or deep-link to another extension's private specs.
