## Output

This artifact is governed directly by this Spec and must follow the canonical staged-delivery targets template.

# Spec: Staged Delivery Targets

## Purpose

Generate or refine _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`)

Generate or refine this artifact directly from this Spec and the canonical staged-delivery targets template.

This artifact is the normalized staged-delivery planning-input artifact used by downstream planning workflows. When `system-design` determines staged delivery is relevant, this artifact is a required normalized intake artifact for honest downstream planning.

This artifact is not Source of Truth.

It is a governed planning-input layer that helps the framework reason honestly about roadmap-aware requirements, system planning, phase planning, and client-facing planning recommendations when multiple intended deliverables exist.

## Downstream Planning Role

A strong `STAGED_DELIVERY_TARGETS.md` may materially improve:
- `requirements-agent:requirements-input-pack`
- `requirements-agent:requirements-sot`
- `system-design-agent:system-design`
- `system-design-agent:phases-sot`
- `system-design-agent:phase-design-cycle`
- later client-facing design outputs such as solution briefs

A materially revised staged-delivery artifact may justify rerunning downstream planning workflows when it changes:
- delivery-target boundaries
- included or excluded scope
- declared vs proposed target interpretation
- roadmap assumptions
- first-delivery framing

## Output Location

_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`)

## Core Principles

1. Preserve roadmap truth without overpromoting certainty.
2. Keep declared and proposed targets distinct.
3. Normalize staged-delivery intent for planning, not for execution control.
4. Preserve multiple targets when the inputs support them.
5. Keep the artifact concise and planning-oriented.
6. Do not invent staged delivery when it is not relevant.
7. Support downstream roadmap-aware planning without turning this artifact into phase planning or release sequencing.

## Required Inputs

Use all relevant available staged-delivery signals, including:
- explicit staged-delivery declarations in source inputs
- MVP / pilot / beta / milestone / Delivery 2 / Delivery 3 references
- roadmap or rollout language from source materials
- `requirements-agent` artifacts when helpful
- assistant-user collaborative reasoning when it clarifies planning intent honestly
- existing _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) when present

## Input Precedence and Refinement Rules

If _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) already exists:
- treat it as the primary normalized staged-delivery artifact
- do not regenerate it automatically from raw signals unless refinement is actually needed
- do not silently overwrite it with a newly inferred version
- refine it only when the existing artifact is weak, stale relative to the current planning inputs, or the Orchestrator explicitly wants refinement

Raw staged-delivery signals are discovery material, not normalized design truth.

## Relevance Detection

State staged delivery as one of:
- explicitly declared
- implied
- not relevant
- proposed only for planning clarity

Rules:
- if the project clearly has multiple intended deliverables, staged delivery is relevant
- if the inputs do not support staged delivery, do not fabricate delivery targets
- if staged delivery is only proposed for planning clarity, keep that recommendation clearly separate from source-confirmed target truth

## Classification Model

`STAGED_DELIVERY_TARGETS.md` must preserve the distinction between:
- **Declared Delivery Target** → explicitly stated in source inputs
- **Proposed Delivery Target** → recommended by the Assistant or through assistant-user collaborative reasoning to improve planning clarity or roadmap communication

These classifications must not be silently collapsed into one another.

## Required Structure

Use the structure defined by this Spec and `../templates/STAGED_DELIVERY_TARGETS_TEMPLATE.md`.

The resulting document must include:
1. Staged Delivery Targets title
2. Delivery Model Summary
3. Declared Delivery Targets section
4. Proposed Delivery Targets section when relevant

For each declared target, preserve:
- Delivery Target name
- Basis / Source Signal
- Included Scope
- Excluded Scope
- Notes

For each proposed target, preserve:
- Delivery Target name
- Why Proposed
- Included Scope
- Excluded Scope
- Assumptions
- Notes

## Roadmap-Honesty Rules

- Declared targets must come from source-confirmed inputs.
- Proposed targets must remain clearly marked as recommendations, not source-confirmed truth.
- Do not present proposed targets as if they were explicitly requested by the client, prospect, or source materials.
- Do not silently collapse multiple declared targets into one target unless the inputs clearly justify doing so.
- Do not silently flatten proposed targets into declared roadmap truth.
- Keep this artifact concise and planning-input oriented.
- Do not turn this artifact into phase planning, release planning, or implementation sequencing.
- Do not define execution order or implementation-control logic here.

## Relationship to Other Planning Artifacts

This artifact should help downstream workflows remain roadmap-aware without replacing them.

Examples:
- `REQUIREMENTS_SOT.md` should preserve staged-delivery meaning without turning it into phase decomposition
- `phases-sot` should use declared delivery targets to design a roadmap-aware phase structure
- `phase-design-cycle` should preserve alignment with declared staged-delivery targets when relevant

## Local Quality Bar

`STAGED_DELIVERY_TARGETS.md` is locally acceptable only when it:
- represents roadmap intent truthfully
- follows the canonical staged-delivery targets template closely enough to support downstream planning
- distinguishes declared from proposed targets
- captures included and excluded scope per target
- makes confirmation gaps visible instead of hiding them
- preserves multiple targets when the source supports them
- stays planning-oriented rather than drifting into release execution control
- is concise enough to be used easily by downstream planning workflows
- is not vague, placeholder-only, or structurally incomplete against the required template sections

## Failure / Repair Expectation

If the artifact is weak, classification-blurring, overly speculative, or execution-plan-like:
- refine it before downstream planning relies on it
- do not expect `REQUIREMENTS_SOT.md` or `phases-sot` to repair a weak staged-delivery artifact implicitly

## Cycle-context unresolved-item contribution obligation

When this producer is executed as part of `system-design`, it must not leave its own linear workflow until every materially relevant unresolved item surfaced locally under:
- `### Assumptions`
- `### Open Questions`

has also been contributed into this producer's own `## Producer contribution: ...` section inside the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact.

Each contributed item must preserve:
- producer artifact path
- source subsection
- one contribution record per canonical unresolved item unless explicitly rejected with recorded reason

When contributing in cycle context, this producer may update only its own producer-scoped contribution section in the project-level canonical inventory structure.
It must not:
- reconcile items
- merge across producers
- classify final gating severity
- decide final handling outcomes
- update ledger outcomes on behalf of `system-design`

If this producer surfaces materially relevant local unresolved items during `system-design` context but does not update its producer-scoped inventory contribution truthfully before exit, local completion is invalid.

## Self-Validation (Mandatory)

Before finalizing, verify:
- staged delivery relevance is assessed honestly
- the artifact follows the canonical staged-delivery targets template closely enough to support downstream planning
- declared and proposed targets are separated when both exist
- proposed targets are not presented as declared truth
- each target captures included scope, excluded scope, and notes
- multiple targets are preserved when relevant
- the artifact remains concise and planning-oriented
- the artifact does not become phase planning, release planning, or implementation sequencing
- roadmap confirmation gaps remain visible when they still matter downstream

- when running inside `system-design`, every canonical local unresolved item has a matching producer-scoped inventory contribution record or explicit rejection reason

If any issue is found:
→ fix it before output.

## Acceptance Criteria

The entrypoint is complete only when the generated or refined _hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md (`/_hirmos/artifacts/context/system-design-agent/STAGED_DELIVERY_TARGETS.md`) is strong enough to serve as trustworthy normalized staged-delivery intake for downstream planning without pretending to be authoritative truth or release-control logic.