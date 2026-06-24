# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

## Current baseline

## HIRMOS 1.0.5 baseline

HIRMOS 1.0.5 is the dogfood-ready scope-authority baseline for the framework payload. It presents the simplified authority model as the first-version model, adds a governed start checkpoint before implementation, consolidates runtime timestamp context into `SESSION_STATE.json.run_context`, and does not preserve legacy authority filenames as supported runtime surfaces.


HIRMOS uses the scope-centered authority model:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

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
