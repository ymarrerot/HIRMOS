# DELIVERY_BASELINE_CHECKPOINT_OUTPUT.md

Status: governed output template.
Purpose: govern the user-facing pause produced when `hirmos start` selects `session_focus = delivery_baseline` before phase/session authority or implementation begins.

This template is not a delivery artifact and not a session artifact. It governs the response shown to the user while the active authority is `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`.

## Required heading

```text
Delivery Baseline — Review or Change
```

## Required response shape

### What HIRMOS understood

Summarize the delivery/release/change requested in plain language. Use domain language first. Avoid low-level implementation detail unless it affects scope, cost, risk, phase coverage, or review.

### Recommended delivery baseline

Use status-aware wording. Before acceptance, describe this as a Candidate Delivery, Proposed Delivery, or Delivery Under Baseline Review; do not call it active until baseline acceptance/amendment has occurred.

- Delivery ID:
- Delivery status: `PROPOSED` | `READY_FOR_BASELINE_REVIEW`
- Delivery authority: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md`
- Delivery roadmap/register: `_hirmos/system/delivery/DELIVERY_PLAN.md`
- What this delivery will produce:
- What this delivery will not produce:

### Recommended delivery shape

- Shape: `DELIVERY_BASELINE`
- Current-state evidence that durable delivery governance is needed:
- Why the smaller single-session shape is not sufficient for this current state and scope:
- Why phase files are not instantiated yet:

### Delivery phase coverage

Summarize the phase coverage plan from `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md#Phase Plan / Phase Coverage Plan`.

Required statements:

- All in-scope delivery requirements have planned phase coverage: YES | NO | BLOCKED
- All delivery design/engineering decisions have planned phase coverage: YES | NO | BLOCKED
- All production-shaped gates have delivery-level or phase-level planned evidence: YES | NO | BLOCKED
- Future phase files are instantiated now: NO, unless explicitly justified

If any answer is NO or BLOCKED, surface the blocking delivery unresolved item.

### Decisions needing your action

If there are no gated delivery items, say exactly:

```text
No gated delivery decisions are blocking this baseline.
```

For each gated item from `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`, include:

1. `<item title or question>`
   - Recommendation:
   - Why this matters:
   - Options / answer format:
   - What happens after you answer:

### Assumptions HIRMOS will carry unless changed

List material non-gating delivery assumptions from `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`.

For each item, include:

- Assumption:
- Why it is safe enough for now:
- Risk:
- Revalidation point:

If there are none, say:

```text
No material non-gating delivery assumptions need user review at this checkpoint.
```

### Technical decisions available for review

List material technical-review delivery items from `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`.

For each item, include:

- Decision / assumption:
- Why it matters:
- Where to inspect:
- How to challenge or change it:

If there are none, say:

```text
No material technical-review delivery items need review at this checkpoint.
```

### Artifacts worth reviewing before continuing

Include only artifacts that exist and contain non-placeholder content.

- `_hirmos/system/delivery/DELIVERY_PLAN.md` — delivery roadmap/register.
- `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` — complete delivery authority and phase coverage plan.
- `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` — complete delivery unresolved register.
- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` — only if created and justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` — only if created and justified.

Do not list `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md` during `delivery_baseline`. If optional authority exists, it must be under `_hirmos/system/delivery/<delivery-id>/`.

Do not list `_hirmos/session/SESSION_SCOPE.md` unless a bounded phase/session scope already exists.

### What happens if you continue

Say this explicitly:

```text
If there are no gated delivery decisions requiring user input, `hirmos continue` will treat this delivery baseline as accepted unless you request changes first; it will then activate or amend the delivery, instantiate only the next needed phase/session authority, and pause again for Session Baseline — Review or Change before implementation begins. If gated decisions are listed as pending user input and not reflected in delivery authority, you must either answer them, explicitly adopt the surfaced recommendation, or ask HIRMOS to reclassify them before `hirmos continue` may accept the baseline.
```

### How to respond

Offer these options exactly, adapting item numbers to the actual output:

```text
Accept delivery baseline
Change 1: ...
Mark item 2 uncertain
Ask for technical review summary
Stop / do not continue
```

## Interaction-mode density

- `domain_expert`: show concise recommendations, phase coverage, why decisions matter, and clear options. Link technical details instead of expanding them by default.
- `technical_supervisor`: include artifact paths, technical-review items, phase coverage assignments, and challenge/change paths.
- `framework_diagnostics`: include `session_focus`, capability route, item classifications, artifact concordance notes, and validation status.

## Hard rules

- Do not hide gated delivery unresolved items in prose.
- Do not summarize delivery unresolved items from memory; source this output from `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`.
- Do not create or reference `_hirmos/session/SESSION_SCOPE.md` before a bounded phase/session scope exists.
- Do not create or reference concrete future `PHASE-xx.md` paths unless those files exist.
- Do not instantiate implementation-unit artifacts from the delivery baseline checkpoint.
- Recommend exactly one next governed command when the delivery baseline is acceptable: `hirmos continue`.


## Surface Minimality Requirement

During `delivery_baseline`, do not list `_hirmos/session/unresolved-items.md` or `_hirmos/session/SESSION_SCOPE.md` as review artifacts. They are `NOT_APPLICABLE` until a bounded phase/session baseline exists. Delivery unresolved items must be sourced from `_hirmos/system/delivery/<delivery-id>/unresolved-items.md#Current Checkpoint Feed`.

## PROD-L8.11 Delivery-Baseline Optional Authority Location

When `SESSION_STATE.json.session_focus = delivery_baseline`, the active authority is delivery-level. Optional requirements/design authority must be located under `_hirmos/system/delivery/<delivery-id>/` only:

- `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md` when separate delivery-level requirements authority is justified.
- `_hirmos/system/delivery/<delivery-id>/DESIGN.md` when separate delivery-level design authority is justified.

During `delivery_baseline`, HIRMOS must not create, update, list, or depend on `_hirmos/session/REQUIREMENTS.md` or `_hirmos/session/DESIGN.md`. If separate optional authority is not justified, requirements and design decisions remain inside `DELIVERY_SCOPE.md` only. Session-level optional authority artifacts become applicable only after the flow advances to a bounded `phase_session_baseline` or `session_baseline` focus.


## PROD-L8.13 Current-State-First Wording

The checkpoint must explain delivery/session/phase routing from current system state, request scope, governance need, validation risk, continuity requirements, and artifact-authority boundaries. It may mention project-type classification as supporting metadata, but must not present greenfield/brownfield labels as the primary reason for durable delivery governance.
