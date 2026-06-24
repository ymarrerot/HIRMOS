# START_CHECKPOINT_OUTPUT.md

Status: governed output template.
Purpose: govern the user-facing pause produced by `hirmos start` before implementation begins.

This template is not a session artifact. It governs the response shown to the user at the first implementation-readiness checkpoint.

## Required heading

```text
Recommended Baseline — Review or Change
```

## Required response shape

### What HIRMOS understood

Summarize the request in plain language. Use domain language first. Avoid low-level implementation detail unless it affects scope, cost, risk, or review.

### Recommended scope

- What this session will do:
- What this session will not do:

### Recommended delivery shape

- Shape: `SINGLE_SESSION_VERTICAL_SLICE` | `SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS` | `MULTI_SESSION_DELIVERY` | `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`
- Why this shape was chosen:
- Smaller-shape safety summary:
- Larger-shape overhead summary:

### Decisions needing your action

If there are no gated items, say exactly:

```text
No gated decisions are blocking this baseline.
```

For each gated unresolved item from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`, include:

1. `<item title or question>`
   - Recommendation:
   - Why this matters:
   - Options / answer format:
   - What happens after you answer:

### Assumptions HIRMOS will carry unless changed

List material non-gating assumptions from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`.

For each item, include:

- Assumption:
- Why it is safe enough for now:
- Risk:
- Revalidation point:

If there are none, say:

```text
No material non-gating assumptions need user review at this checkpoint.
```

### Technical decisions available for review

List material technical-review items from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`.

For each item, include:

- Decision / assumption:
- Why it matters:
- Where to inspect:
- How to challenge or change it:

If there are none, say:

```text
No material technical-review items need review at this checkpoint.
```

### Artifacts worth reviewing before continuing

Include only artifacts that exist and contain non-placeholder content.

- `_hirmos/session/SESSION_SCOPE.md` — session authority.
- `_hirmos/session/unresolved-items.md` — complete gated, non-gating, and technical-review register.
- `_hirmos/session/REQUIREMENTS.md` — only if created and justified.
- `_hirmos/session/DESIGN.md` — only if created and justified.
- `_hirmos/system/delivery/DELIVERY_PLAN.md` — only if durable delivery governance is active.
- `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` — only if durable delivery governance is active.

### What happens if you continue

Say this explicitly:

```text
If you run `hirmos continue`, HIRMOS will treat this recommended baseline as accepted unless you request changes first. It will then instantiate implementation-unit artifacts if needed and begin governed implementation.
```

### How to respond

Offer these options exactly, adapting item numbers to the actual output:

```text
Accept baseline
Change 1: ...
Mark item 2 uncertain
Ask for technical review summary
Stop / do not continue
```

## Interaction-mode density

- `domain_expert`: show concise recommendations, why they matter, and clear options. Link technical details instead of expanding them by default.
- `technical_supervisor`: include artifact paths, technical-review items, and challenge/change paths.
- `framework_diagnostics`: include control names, item classifications, and artifact concordance notes.

## Hard rules

- Do not hide gated unresolved items in prose.
- Do not summarize unresolved items from memory; source this output from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed`.
- Do not tell the user an artifact exists unless it exists and is non-placeholder.
- Do not create or reference full implementation-unit artifacts before the session scope baseline has been accepted or amended.
- Do not use implementation-unit previews as implementation authority.
- Recommend exactly one next governed command when the baseline is acceptable: `hirmos continue`.
