# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

## Current baseline

## HIRMOS 1.0.7 baseline

HIRMOS 1.0.7 is the dogfood-ready focus-aware delivery/session authority baseline. It keeps the scope-centered model from 1.0.5 and the focus-aware delivery-baseline model from 1.0.6, then hardens delivery-baseline session-surface minimality so delivery-level authority and unresolved items remain under `_hirmos/system/delivery/<delivery-id>/` until a bounded phase/session baseline is created.

HIRMOS uses the scope-centered authority model:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

During `delivery_baseline` focus, HIRMOS uses the delivery scope and delivery unresolved register as the active authority surfaces and must not create session-level `SESSION_SCOPE.md` or session-level `unresolved-items.md` by default. Those session-level artifacts are created only when the flow advances to a bounded phase/session baseline.

Default implementation sessions do not create separate requirements or design artifacts unless the work objective, delivery shape, audit need, or shared multi-session adoption need justifies separate authority.

Conditional authority artifacts:

```text
_hirmos/session/REQUIREMENTS.md
_hirmos/session/DESIGN.md
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md
_hirmos/system/delivery/<delivery-id>/DESIGN.md
```

## CLI package

The CLI package version remains unchanged when the framework content changes but terminal command behavior does not change.

## Framework package

Release packaging must ship only canonical runtime surfaces, templates, docs, validators, and examples. Framework files must remain project-agnostic except for clearly labeled examples.

## 1.0.7 stabilization note

HIRMOS 1.0.7 includes delivery-baseline session-surface minimality hardening, validator concordance, and final dogfood-readiness stabilization. No terminal CLI version bump is required because terminal install behavior did not change.
