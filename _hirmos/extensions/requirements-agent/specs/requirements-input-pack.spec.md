## Output

This artifact is governed directly by this Spec. No shipped template is required at the current framework stage.

# Spec: Requirements Input Pack

## Purpose

Generate a structured `REQUIREMENTS_INPUT_PACK.md` that consolidates source inputs, assistant-user collaborative reasoning, research-backed findings, assumptions, open questions, and delivery-target signals into a strong normalized input package for `requirements-agent:requirements-sot`.

This artifact is **not** Source of Truth.

It is a governed intake-and-analysis artifact that strengthens requirements generation.

## Downstream Rerun Impact

A stronger or materially revised `REQUIREMENTS_INPUT_PACK.md` may justify rerunning downstream System Design workflows, especially `system-design-agent:system-design`.

This is appropriate when the revised pack materially changes:
- assumptions
- open questions
- delivery-target interpretation
- scope understanding
- research-backed defaults that shape planning

## Output Location

_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md (`/_hirmos/artifacts/context/requirements-agent/REQUIREMENTS_INPUT_PACK.md`)

Generate or refine this artifact directly from this Spec.

No shipped template is required for this artifact at the current framework stage.

## Core Principles

1. Strong intake before strong requirements.
2. Preserve provenance of information.
3. Separate confirmed facts from assumptions.
4. Surface ambiguity instead of hiding it.
5. Strengthen downstream planning without pretending certainty.
6. Support both weak and strong source inputs.
7. Preserve delivery-target distinctions when relevant.

## Classification Model

`REQUIREMENTS_INPUT_PACK.md` must preserve clear distinctions between:

- **Confirmed** → directly supported by source inputs
- **Assumption** → needed for planning but not source-confirmed
- **Research-Backed Default** → supported by external research or common domain practice, but not source-confirmed
- **Declared Delivery Target** → explicitly stated in source inputs
- **Proposed Delivery Target** → recommended by the Assistant or through assistant-user collaborative reasoning
- **Pending Confirmation Item** → a material item that still requires explicit confirmation inside the cycle-processing model, even when the final intake artifact exposes that uncertainty through `Assumptions` or `Open Questions` rather than a separate section

These classifications must not be silently collapsed into one another.

## Required Inputs

Use all relevant available requirements inputs, including:

- direct prompt or command argument-tail Requirements input for the active run
- manually attached requirement-relevant inputs, including online-service attachments visible in the current LLM session
- files under `_hirmos/inputs/requirements-agent/requirements/` when present
- explicit bounded local file paths or repository-context references surfaced by the user or Orchestrator
- assistant-user collaborative reasoning produced during the session
- relevant existing context artifacts when useful
- staged-delivery inputs when present
- optional research findings when useful

The pack should remain agnostic about how the inputs were obtained.

## Input Alignment Rules

`REQUIREMENTS_INPUT_PACK.md` must stay aligned to the available source inputs and collaborative reasoning used to strengthen them.

It must not:
- silently convert assumptions into confirmed facts
- silently convert research-backed defaults into client-confirmed truth
- erase important ambiguity that still affects downstream planning
- collapse declared and proposed delivery targets into one undifferentiated list when both exist


## Runtime Input Source Rules

The preferred local runtime input folder for reusable Requirements source material is:

```text
_hirmos/inputs/requirements-agent/requirements/
```

This folder is a project runtime surface, not extension package content. It may be created by the active Core/entrypoint path during init or first run when needed.

Do not automatically scan the full repository. If repository context is needed, use files in the Requirements runtime input folder, explicit bounded local file paths, explicit bounded directories/file sets, or derived context artifacts produced through declared hooks.

When running in an online LLM environment, visible attachments count as session-provided inputs even if they do not exist as local files. If a required attachment or file reference is unavailable, pause and surface the missing source.

## Output Status

`REQUIREMENTS_INPUT_PACK.md` is:
- assistant-generated
- governed
- reusable
- non-authoritative
- an upstream planning-input artifact

It must not be treated as SoT.

## Required Structure

`REQUIREMENTS_INPUT_PACK.md` must include:

- system / product name or working label when known
- project intent / problem framing
- extracted requirements signals grouped by confidence
- explicit notes on missing or ambiguous requirement-shaping information
- `## Unresolved Items`
  - `### Assumptions`
  - `### Open Questions`
- source traceability to the raw intake

Any materially relevant unresolved belonging to this intake artifact must appear under one of the two `Unresolved Items` subsections rather than remaining only in surrounding prose.

Requirements-level extraction and reconciliation are governed by [`requirements.spec.md`](./requirements.spec.md).

## Staged Delivery Handling

When staged delivery is explicit, implied, or worth proposing for planning clarity, preserve:

- Delivery Target Signals
- Declared Delivery Targets
- Proposed Delivery Targets

Rules:
- declared = source-confirmed
- proposed = assistant recommendation or assistant-user collaborative recommendation
- proposed targets must remain clearly marked as recommendations
- if a proposed delivery target materially shapes the roadmap or later client-facing recommendations, it should remain explicitly distinguishable from source-declared targets in downstream artifacts

Preserve the staged-delivery target shape required by this Spec.

## Research-Backed Defaults and Notes

When research meaningfully strengthens the pack:
- include concise research-backed defaults or notes
- keep them clearly separate from source-confirmed facts
- do not silently promote research-backed defaults into confirmed requirements
- if a research-backed default materially shapes downstream planning and remains unconfirmed, preserve that uncertainty through `Assumptions`, `Open Questions`, and downstream unresolved-item handling as appropriate

## Downstream Planning Notes

Add strong downstream notes that improve:
- `requirements-agent:requirements-sot`
- system planning
- staged-delivery interpretation
- later client-facing design outputs when relevant

## Local Quality Bar

When this artifact is generated or refined during `requirements-agent:requirements`, materially relevant unresolved items preserved here must also be contributed into this producer's own `## Producer contribution: ...` section inside the project-level canonical `/_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md` artifact using the Requirements lifecycle binding at `/_hirmos/extensions/requirements-agent/specs/unresolved-item-contribution-contract.md`, which binds to the shared framework contract at `/_hirmos/core/authority/extensions/unresolved-item-contribution-contract.md`.


`REQUIREMENTS_INPUT_PACK.md` is locally acceptable only when:

- source inputs are clear
- confirmed facts remain separate from assumptions
- research-backed defaults remain distinct
- materially relevant assumptions are explicit
- materially relevant open questions are explicit
- staged delivery distinctions are preserved when relevant
- downstream planning notes are strong enough to improve requirements generation

## Failure / Repair Expectation

If the pack is weak, ambiguous, or classification-blurring:
- refine it before using it as normalized intake for `requirements-agent:requirements-sot`
- do not rely on requirements generation to repair weak intake structure

## Cycle-context unresolved-item contribution obligation

When this producer is executed as part of `requirements-agent:requirements`, it must not leave its own linear workflow until every materially relevant unresolved item surfaced locally under:
- `### Assumptions`
- `### Open Questions`

has also been contributed into this producer's own `## Producer contribution: ...` section inside the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact.

Each contributed item must preserve:
- producer artifact path
- source subsection
- one contribution record per canonical unresolved item unless explicitly rejected with recorded reason

When contributing in cycle context, this producer may update only its own producer-scoped contribution section in the cycle-owned inventory structure.
It must not:
- reconcile items
- merge across producers
- classify final gating severity
- decide final handling outcomes
- update ledger outcomes on behalf of `requirements-agent:requirements`

If this producer surfaces materially relevant local unresolved items during `requirements-agent:requirements` context but does not update its producer-scoped inventory contribution truthfully before exit, local completion is invalid.

## Self-Validation (Mandatory)

Before finalizing, verify:

- inputs used are clear
- confirmed facts are separated from assumptions
- materially relevant assumptions are explicit
- materially relevant open questions are explicit
- raw discovery gaps and confirmation-needing items were normalized into the final interface rather than left as overlapping final sections
- staged delivery is handled correctly when relevant
- declared and proposed targets are separated when both exist
- the artifact improves requirements generation
- the artifact does not pretend to be Source of Truth
- research-backed defaults are separated from confirmed facts
- proposed delivery targets are separated from declared targets
- materially important assumptions remain visible for downstream confirmation handling when appropriate

- when running inside `requirements-agent:requirements`, every canonical local unresolved item has a matching producer-scoped inventory contribution record or explicit rejection reason

If any issue is found:
→ fix it before output.

## Acceptance Criteria

The entrypoint is complete only when the generated or refined `REQUIREMENTS_INPUT_PACK.md` is strong enough to serve as trustworthy normalized intake for `requirements-agent:requirements-sot` without pretending to be authoritative truth.