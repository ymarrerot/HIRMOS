# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

## Current baseline

## HIRMOS 1.0.9 baseline

HIRMOS 1.0.9 is the dogfood-ready focus-aware delivery/session authority baseline. It keeps the scope-centered model from 1.0.5, the focus-aware delivery-baseline model from 1.0.6, the delivery-baseline session-surface minimality hardening from 1.0.7, the optional delivery-authority location hardening from 1.0.8, and adds phase/session-baseline concordance plus current-state-first generated-artifact cleanup.

HIRMOS uses the scope-centered authority model:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

During `delivery_baseline` focus, HIRMOS uses the delivery scope and delivery unresolved register as the active authority surfaces and must not create session-level `SESSION_SCOPE.md`, session-level `unresolved-items.md`, session-level `REQUIREMENTS.md`, or session-level `DESIGN.md` by default. Those session-level artifacts are created only when the flow advances to a bounded phase/session baseline and the selected focus justifies them.

During `phase_session_baseline` focus, HIRMOS must keep phase/session authority and ledgers fresh: the active `PHASE-xx.md` must include scalar `Entry criteria status`, `SESSION_SCOPE.md` must exist before session-baseline review, `SESSION_EXECUTION.md` must mark completed routing work as completed, and `DELIVERY_PLAN.md` must point to the active phase after phase instantiation.

Default implementation sessions do not create separate requirements or design artifacts unless the work objective, delivery shape, audit need, or shared multi-session adoption need justifies separate authority.

Conditional authority artifacts:

```text
_hirmos/session/REQUIREMENTS.md
_hirmos/session/DESIGN.md
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md
_hirmos/system/delivery/<delivery-id>/DESIGN.md
```

For delivery-baseline focus, conditional requirements/design authority must use the delivery-level paths. For bounded phase/session focus, conditional requirements/design authority may use the session-level paths only when explicitly justified and adopted by `SESSION_SCOPE.md`.

Generated artifacts should explain routing from current system state, scope size, governance need, validation risk, continuity need, and artifact-authority boundaries. Project-type labels such as greenfield, brownfield, or mixed may remain useful evidence metadata, but they must not become the primary routing justification.

## CLI package

The CLI package version remains unchanged when the framework content changes but terminal command behavior does not change.

## Framework package

Release packaging must ship only canonical runtime surfaces, templates, docs, validators, and examples. Framework files must remain project-agnostic except for clearly labeled examples.

## 1.0.9 stabilization note

HIRMOS 1.0.9 includes phase entry-gate concordance, post-continue ledger freshness, delivery-plan active-phase freshness, pre-acceptance delivery wording hardening, current-state-first generated-artifact cleanup, validator concordance, and final dogfood-readiness stabilization. No terminal CLI version bump is required because terminal install behavior did not change.
