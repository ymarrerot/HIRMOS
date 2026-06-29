# Shared Capability Controls

Purpose: common runtime controls for HIRMOS extension and capability entrypoints. Capability entrypoints keep their execution contract, activation triggers, inputs, capability-specific obligations, and terminal states; this file owns repeated cross-cutting controls so entrypoints do not duplicate mutable rule blocks.

## Required behavior baseline

Every runnable extension/capability entrypoint must:

1. Confirm and record the capability decision under `_hirmos/core/protocol/CAPABILITY_ROUTING.md` in `_hirmos/session/SESSION_LEDGER.md` when capability routing is material.
2. Instantiate or update only canonical artifacts required by the active request path; do not create empty future synchronization obligations.
3. Produce non-placeholder content before claiming completion.
4. Preserve lifecycle ownership boundaries and route back in `SESSION_LEDGER.md` when evidence invalidates an earlier stage.
5. Apply the selected extension method plus the capability-specific execution surface; do not execute from chat summaries or raw inputs alone.

## Canonical interaction posture visibility

Use `_hirmos/core/authority/INTERACTION_POSTURE.md` for user-visible output: concise by default, transparent artifact pointers for governed claims, and progressive disclosure when risk, validation failure, blocker state, route-back, or user request requires more detail.

Default visibility:

- Surface user-owned decisions, blockers, readiness/completion status, and concise artifact pointers.
- Surface assumptions, artifacts/evidence, and review implications when needed for responsible review.
- Surface activation reason, entrypoint path, controls, unresolved-item contribution, route-back decisions, and terminal-state basis when validation failure, blocker state, route-back, or inspection need requires it.

## Unresolved-item producer obligation

Capabilities that can discover uncertainty are unresolved-item producers and must apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`.

Before marking a producer capability complete, record exactly one producer outcome in the focus-appropriate unresolved register selected by `SESSION_STATE.json.session_focus`: `ITEMS_FOUND`, `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED`. When items exist, preserve the protocol fields including current status, downstream impact, and revalidation point.

## Runtime integration responsibilities

When material runtime services, provider integrations, local workflow evidence, or production-shaped claims are involved, apply `_hirmos/core/protocol/RUNTIME_INTEGRATION_AND_PRODUCTION_READINESS.md`.

Do not claim fixture, mock, boundary, local, production, or provider-integration levels beyond what active artifacts and evidence support. Record detailed evidence in the owning IU, `EVIDENCE.md`, or accepted-state/archive source; the capability entrypoint should point rather than duplicate.

## Output and terminal-state discipline

A capability result must identify its terminal state, artifact/evidence pointers, unresolved-item outcome when applicable, route-back decision when applicable, and the next governed command or checkpoint when the capability changes the lifecycle boundary.
