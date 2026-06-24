# Example: Delivery Baseline and Phase/Session Flow

This example shows how HIRMOS should handle durable multi-session delivery without over-creating phase or session artifacts before the user accepts the delivery baseline.

## User request

```text
Build a first practical version of a product, but keep a later version in mind. The first version should support the core workflow. Later, we want analytics, paid usage readiness, and operational hardening.
```

## `hirmos start` result

HIRMOS decides the request needs durable delivery governance and sets:

```text
session_focus = delivery_baseline
active_authority = _hirmos/system/delivery/mvp/DELIVERY_SCOPE.md
```

Expected artifacts:

```text
_hirmos/session/SESSION_STATE.json
_hirmos/session/SESSION_EXECUTION.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/mvp/DELIVERY_SCOPE.md
_hirmos/system/delivery/mvp/unresolved-items.md
_hirmos/system/delivery/mvp/REQUIREMENTS.md   # optional, only if justified
_hirmos/system/delivery/mvp/DESIGN.md         # optional, only if justified
```

Not created yet by default:

```text
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/unresolved-items.md
_hirmos/session/implementation-units/IU-xx.md
_hirmos/system/delivery/mvp/phases/PHASE-xx.md
```

## Delivery baseline checkpoint

The user sees:

```text
Delivery Baseline — Review or Change
```

The checkpoint summarizes:

- what HIRMOS understood;
- the proposed delivery scope;
- gated delivery decisions;
- non-gating delivery assumptions;
- technical-review delivery decisions;
- phase coverage plan completeness;
- what will happen if the user runs `hirmos continue`.

## After delivery baseline acceptance

`hirmos continue` accepts or amends the delivery baseline, marks the delivery active, and prepares only the next phase/session authority by default:

```text
_hirmos/system/delivery/mvp/phases/PHASE-01.md
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/unresolved-items.md   # only if session-level items exist
```

HIRMOS then pauses again:

```text
Session Baseline — Review or Change
```

## After session baseline acceptance

The next `hirmos continue` accepts or amends the session baseline, creates implementation-unit files only if needed, and begins governed implementation.

## Coverage rule

Even when future phase files are created just in time, `DELIVERY_SCOPE.md` must include a complete phase coverage plan before delivery-baseline approval so HIRMOS can answer:

```text
Do the planned phases cover 100% of DELIVERY_SCOPE.md?
```

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.
