# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

## Current baseline

## HIRMOS 1.1.1 baseline

HIRMOS 1.1.1 is the current-state-first source reading, runtime freshness, and complexity-pressure stabilization baseline. It builds on the 1.1.0 accepted-state navigation model by strengthening how HIRMOS follows source artifacts during Understand System State and how runtime artifacts stay fresh after governed transitions.

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

`CURRENT_SYSTEM_STATE.md` is the accepted-state navigation authority and the mandatory first read for current-state-first work. It owns the current governance context, accepted-state navigation and latest close metadata, concise accepted-state summary, Work History Ledger, Source Artifact Index, active delivery/phase/session pointers, and next governed navigation. It does not replace delivery/session scope, requirements, design, unresolved-item, implementation-unit, evidence, or archive artifacts as source authorities.

During Understand System State, HIRMOS must read `CURRENT_SYSTEM_STATE.md` first, follow active-governance pointers, and read materially relevant canonical source artifacts before material design or implementation. Reading depth is scoped/progressive; HIRMOS should not perform a blind exhaustive history scan for every small request, but it must not design from summaries alone when source authority is available.

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

Default HIRMOS does not create root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md`. Default HIRMOS also does not create `DECISION_LOG.md`; decision logging is conditional on explicit decision-log governance. If a project explicitly activates cumulative accepted-state requirements governance, that activation must be documented before such a root artifact is valid.

At close, HIRMOS updates accepted state using an index-first model: current governance context, Work History Ledger, Source Artifact Index, concise accepted-state summary only when materially changed, and next recommended navigation. It must not merge delivery/session requirements into root accepted-state requirements by default. Active navigation pointers may be updated during governed transitions, but accepted-state summaries and historical outcome rows are finalized through close/update-state discipline.

During `delivery_baseline` focus, HIRMOS uses the delivery scope and delivery unresolved register as the active authority surfaces and must not create session-level `SESSION_SCOPE.md`, session-level `unresolved-items.md`, session-level `REQUIREMENTS.md`, or session-level `DESIGN.md` by default. Those session-level artifacts are created only when the flow advances to a bounded phase/session baseline and the selected focus justifies them.

During `phase_session_baseline` focus, HIRMOS must keep phase/session authority and ledgers fresh: the active `PHASE-xx.md` must include scalar `Entry criteria status`, `SESSION_SCOPE.md` must exist before session-baseline review, `SESSION_EXECUTION.md` must mark completed routing work as completed, and `DELIVERY_PLAN.md` must point to the active phase after phase instantiation.

When implementation-unit mode is active, implementation-unit files must be instantiated after session-baseline acceptance and before material code changes begin. Retrospective implementation-unit creation requires explicit correction/reconciliation. Runtime mirrors such as `SESSION_EXECUTION.md`, `PHASE-xx.md`, `SESSION_SCOPE.md`, and `EVIDENCE.md` must be reconciled after implementation starts or completes so stale lower sections do not contradict current machine state.

Generated artifacts should explain routing from current system state, scope size, governance need, validation risk, continuity need, and artifact-authority boundaries. Project-type labels such as greenfield, brownfield, or mixed may remain useful evidence metadata, but they must not become the primary routing justification.

Capability IDs are stable dispatch identifiers, not user-facing workflow names. HIRMOS should reuse existing capability families where possible and place requirements/design/scope authority at the narrowest safe source level. Validators should protect authority safety, freshness, and structural/status concordance; exact wording checks should be avoided unless wording affects authority safety.

## CLI package

The CLI package version remains unchanged when the framework content changes but terminal command behavior does not change.

## Framework package

Release packaging must ship only canonical runtime surfaces, templates, docs, validators, and examples. Framework files must remain project-agnostic except for clearly labeled examples.


## 1.1.1 stabilization note

HIRMOS 1.1.1 includes current-state-first source reading discipline, runtime freshness guidance, implementation-unit timing hardening, gated continue semantics, evidence claim reconciliation, accepted-state support minimality, protocol ownership guidance, validator minimality classes, capability taxonomy, and source-authority matrix stabilization. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.0 stabilization note

HIRMOS 1.1.0 includes accepted-state navigation authority, source-artifact traceability, removal of default root accepted-state requirements, index-first close guidance, validator concordance, and final dogfood-readiness stabilization. No terminal CLI version bump is required because terminal install behavior did not change.

## PROD-L8.15 current-state source reading and freshness

Framework users should treat `CURRENT_SYSTEM_STATE.md` as the first read and navigation authority, then follow active and materially relevant source artifact pointers before design or implementation. Existing projects with a default `_hirmos/system/accepted-state/DECISION_LOG.md` may remove it unless explicit decision-log governance is active.
