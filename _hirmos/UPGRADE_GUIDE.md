# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

## Current baseline

## HIRMOS 1.1.0 baseline

HIRMOS 1.1.0 is the accepted-state navigation authority and source-artifact traceability baseline. It keeps the focus-aware delivery/session authority model from the 1.0.x stabilization line and changes accepted-state governance so `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` is the single default accepted-state root navigation authority.

HIRMOS uses the scope-centered authority model:

```text
_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md
_hirmos/session/SESSION_SCOPE.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

`CURRENT_SYSTEM_STATE.md` is the accepted-state navigation authority. It owns the current governance context, accepted-state navigation and latest close metadata, concise accepted-state summary, Work History Ledger, Source Artifact Index, active delivery/phase/session pointers, and next governed navigation. It does not replace delivery/session scope, requirements, design, unresolved-item, implementation-unit, evidence, or archive artifacts as source authorities.

Detailed requirements, design, and scope remain where they originate:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md   # optional
_hirmos/system/delivery/<delivery-id>/DESIGN.md         # optional
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/REQUIREMENTS.md                         # optional
_hirmos/session/DESIGN.md                               # optional
_hirmos/system/history/sessions/<session-id>/...         # archived source
```

Default HIRMOS does not create root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md`. If a project explicitly activates cumulative accepted-state requirements governance, that activation must be documented before such a root artifact is valid.

At close, HIRMOS updates accepted state using an index-first model: current governance context, Work History Ledger, Source Artifact Index, concise accepted-state summary only when materially changed, and next recommended navigation. It must not merge delivery/session requirements into root accepted-state requirements by default.

During `delivery_baseline` focus, HIRMOS uses the delivery scope and delivery unresolved register as the active authority surfaces and must not create session-level `SESSION_SCOPE.md`, session-level `unresolved-items.md`, session-level `REQUIREMENTS.md`, or session-level `DESIGN.md` by default. Those session-level artifacts are created only when the flow advances to a bounded phase/session baseline and the selected focus justifies them.

During `phase_session_baseline` focus, HIRMOS must keep phase/session authority and ledgers fresh: the active `PHASE-xx.md` must include scalar `Entry criteria status`, `SESSION_SCOPE.md` must exist before session-baseline review, `SESSION_EXECUTION.md` must mark completed routing work as completed, and `DELIVERY_PLAN.md` must point to the active phase after phase instantiation.

Generated artifacts should explain routing from current system state, scope size, governance need, validation risk, continuity need, and artifact-authority boundaries. Project-type labels such as greenfield, brownfield, or mixed may remain useful evidence metadata, but they must not become the primary routing justification.

## CLI package

The CLI package version remains unchanged when the framework content changes but terminal command behavior does not change.

## Framework package

Release packaging must ship only canonical runtime surfaces, templates, docs, validators, and examples. Framework files must remain project-agnostic except for clearly labeled examples.

## 1.1.0 stabilization note

HIRMOS 1.1.0 includes accepted-state navigation authority, source-artifact traceability, removal of default root accepted-state requirements, index-first close guidance, validator concordance, and final dogfood-readiness stabilization. No terminal CLI version bump is required because terminal install behavior did not change.
