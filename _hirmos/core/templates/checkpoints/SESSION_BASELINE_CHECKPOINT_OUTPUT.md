# SESSION_BASELINE_CHECKPOINT_OUTPUT.md

Status: governed output template.
Purpose: govern the user-facing pause produced when HIRMOS has prepared a bounded `SESSION_SCOPE.md` for single-session work or for the next phase/session of an accepted delivery.

This template is not a session artifact. It governs the response shown to the user before implementation-unit artifacts or implementation begin.

## Required heading

```text
Session Baseline — Review or Change
```

For simple single-session work, the compatible heading may be:

```text
Recommended Baseline — Review or Change
```

## Required response shape

### What HIRMOS understood

Summarize the bounded work scope in plain language. Use domain language first. Avoid low-level implementation detail unless it affects scope, cost, risk, or review.

### Recommended session scope

- Session authority: `_hirmos/session/SESSION_SCOPE.md`
- Parent delivery: `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` / NOT_APPLICABLE
- Parent phase: `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` / NOT_APPLICABLE
- What this session will do:
- What this session will not do:

### Recommended delivery shape / focus

- Shape: `SINGLE_SESSION_MINIMAL` | `SINGLE_SESSION_VERTICAL_SLICE` | `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` | `DELIVERY_PHASE_SESSION`
- Session focus: `minimal_session` | `session_baseline` | `phase_session_baseline`
- Why this shape/focus was chosen for the real software work:
- Technically possible simpler shape:
- Why simpler shape is acceptable or insufficient:
- User interaction / token-cost impact:
- If this session adopts a phase from a multi-session delivery, parent phase-count justification source:
- Phase merge pressure check for this phase:
- Why this phase remains separate instead of merged:
- Why implementation-unit files are not instantiated yet:

### Decisions needing your action

If there are no gated session items, say exactly:

```text
No gated session decisions are blocking this baseline.
```

For each gated item from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`, include:

1. `<item title or question>`
   - Recommendation:
   - Why this matters:
   - Options / answer format:
   - What happens after you answer:

### Assumptions HIRMOS will carry unless changed

List material non-gating session assumptions from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`.

For each item, include:

- Assumption:
- Why it is safe enough for now:
- Risk:
- Revalidation point:

If there are none, say:

```text
No material non-gating session assumptions need user review at this checkpoint.
```

### Technical decisions available for review

List material technical-review session items from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`.

For each item, include:

- Decision / assumption:
- Why it matters:
- Where to inspect:
- How to challenge or change it:

If there are none, say:

```text
No material technical-review session items need review at this checkpoint.
```

### Delivery assumptions resurfaced in this session

If this session belongs to a delivery, identify any accepted delivery assumption or decision that is challenged by session facts.

For each item:

- Originating delivery artifact / decision:
- Current session impact:
- Recommendation:
- Delivery authority update required? YES | NO

If none, say:

```text
No accepted delivery assumptions were challenged by this session baseline.
```

### Artifacts worth reviewing before continuing

Include only artifacts that exist and contain non-placeholder content.

- `_hirmos/session/SESSION_SCOPE.md` — complete active session authority.
- `_hirmos/session/unresolved-items.md` — session gated, non-gating, and technical-review register, if created.
- `_hirmos/session/REQUIREMENTS.md` — only if created and justified.
- `_hirmos/session/DESIGN.md` — only if created and justified.
- `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` — only if this session adopts delivery authority.
- `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` — only if this session adopts phase authority.

### What happens if you continue

Say this explicitly:

```text
If you run `hirmos continue`, HIRMOS will treat this session baseline as accepted unless you request changes first. It will then instantiate implementation-unit artifacts if needed and begin governed implementation.
```

### How to respond

Offer these options exactly, adapting item numbers to the actual output:

```text
To continue from this pause:
hirmos continue "Accept session baseline"
hirmos continue "Change item 1: <your change>"
hirmos continue "Mark item 2 uncertain"
hirmos continue "Ask for technical review summary"

To stop without continuing:
Do not run `hirmos continue`. Reply exactly: Stop / do not continue
```

## Canonical interaction posture density

Use `_hirmos/core/authority/INTERACTION_POSTURE.md`: simple by default, transparent by design, rigorous underneath, and progressively disclosed. Keep the session-baseline checkpoint concise while including artifact paths for governed claims, unresolved items, carry-forward items, parent delivery/phase authority, and implementation-readiness claims. Increase visible detail when risk, blocker state, validation failure, route-back, or user request requires it.

## Hard rules

- Do not hide gated session unresolved items in prose.
- Do not summarize session unresolved items from memory; source this output from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed` when that artifact exists.
- If no session unresolved register exists, say no material unresolved items were created and do not invent one.
- If a session item invalidates delivery authority, identify the delivery artifact that must be amended before claiming implementation readiness or close.
- Do not create or reference full implementation-unit artifacts before the session baseline has been accepted or amended.
- Recommend exactly one next governed command when the session baseline is acceptable: `hirmos continue`.
