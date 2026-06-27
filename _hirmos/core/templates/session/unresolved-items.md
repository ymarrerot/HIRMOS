# Unresolved Items Register

Status: active-session governed register artifact.
Purpose: capture, classify, reconcile, dispose, carry, and revalidate every gated item, non-gating assumption, technical-review item, blocker, and material uncertainty discovered during the active session.

This register is authoritative for unresolved-item details. Summaries in `SESSION_SCOPE.md`, checkpoints, `SESSION_EXECUTION.md`, or user-facing responses are not sufficient substitutes.

Protocol authority: `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`

## Register Controls

- Direct review required before every lifecycle boundary: YES | NO
- Last direct review boundary:
- Last direct review result: CLEAR | BLOCKED | PARTIAL | NOT_REVIEWED
- Blocking status: BLOCKED | NOT_BLOCKED
- Gated item count:
- Non-gating item count:
- Technical-review item count:
- Resolved item count this session:

## Producer Contributions

Each unresolved-item producer must apply `_hirmos/core/protocol/UNRESOLVED_ITEMS.md` before the producing lifecycle stage or capability can be marked complete.

Allowed producer outcomes:

```text
ITEMS_FOUND
NONE_FOUND
NOT_APPLICABLE
BLOCKED
```

| Contribution ID | Producer | Lifecycle stage | Source artifact/evidence | Outcome | Candidate items or none/not-applicable/blocker statement | Producer completeness rationale |
|---|---|---|---|---|---|---|

## Inventory Summary

Use this table as an index only. Each material item must also have a detail block in `Required Item Detail Blocks` unless the item is explicitly `NOT_APPLICABLE` and has no downstream effect.

| Item ID | Title | Classification | Owner | Visibility | Affected boundary | Current status | Current recommendation | Detail block present? |
|---|---|---|---|---|---|---|---|---|

Required classifications:

```text
GATED
NON_GATING
TECHNICAL_REVIEW
RESOLVED
DUPLICATE
NOT_APPLICABLE
```

## Required Item Detail Blocks

Every material unresolved item must preserve the minimum fields from `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`, including `NON_GATING` items. Non-gating items are governed decisions or assumptions, not casual notes; they can hide risky shortcuts, deferred choices, or assumptions that must remain visible. Do not rely on summary tables when details are needed for user review, implementation, continuation, close, or future revalidation.

### `<ITEM-ID>` — `<Title>`

- ID:
- Title:
- Description:
- Source producer/capability:
- Source evidence:
- Classification: GATED | NON_GATING | TECHNICAL_REVIEW | RESOLVED | DUPLICATE | NOT_APPLICABLE
- Decision owner:
- Visibility posture: user-facing | technical-review | internal-note
- Affected lifecycle boundary:
- Current status: OPEN | BLOCKED | CARRIED | RESOLVED | DUPLICATE | NOT_APPLICABLE
- Current recommendation:
- Why this matters:
- Options / valid answer shape when user input is required:
- What happens after answer, if user input is required:
- Assumption if carried:
- Why it is safe enough for now:
- Risk if wrong or stale:
- Downstream impact:
- Revalidation point:
- How to challenge or change it:
- Disposition history reference:

## Active Gated Items

Items that block Design, Implementation, readiness, Update System State, close, or future continuation until resolved or explicitly baselined by the responsible decision owner.

| Item ID | Decision needed | Decision owner | Why it blocks | Options / valid answers | HIRMOS recommendation | Required before |
|---|---|---|---|---|---|---|

## Active Non-Gating Items

Items carried as assumptions, constraints, or revalidation obligations that do not block continuation but must remain visible and applied.

| Item ID | Assumption / constraint | Owner/source | Why non-gating | Risk | Where carried forward | Revalidation point |
|---|---|---|---|---|---|---|

## Technical Review Items

Technical assumptions or decisions that do not require immediate domain-owner input but must be inspectable.

| Item ID | Technical item | Review artifact/path | Risk | Affected boundary | Challenge/change path |
|---|---|---|---|---|---|

## Reconciliation Worklist

Record every merge, split, duplicate, reclassification, route-back, or carry-forward decision. Avoid over-merging unrelated decisions.

Allowed reconciliation actions:

```text
KEEP_DISTINCT
MERGE_DUPLICATE
SPLIT_ITEM
RECLASSIFY
RESOLVE
CARRY_FORWARD
ROUTE_BACK
MARK_NOT_APPLICABLE
```

| Seq | Action | Items affected | Reason | Sources preserved | Result |
|---:|---|---|---|---|---|

## Disposition History

Append-only record of user decisions, HIRMOS baselines, assumptions, route-backs, reclassifications, resolutions, and “what changed” entries.

| Seq | Item ID | Disposition | Decided by/source | Date/sequence | Evidence | What changed |
|---:|---|---|---|---|---|---|

## Current Checkpoint Feed

Prepare the concise user-facing unresolved-item basis for the next governed checkpoint. This feed must be current before HIRMOS surfaces a checkpoint asking for decisions or claiming readiness.

### Gated items to surface

Each gated item surfaced to the user must include a description/question, recommended baseline, why it matters, options/answer format, and what happens after answer.

| Item ID | User-facing question | Recommended baseline | Why it matters | Options / answer format | What happens after answer |
|---|---|---|---|---|---|

### Non-gating assumptions to disclose

Each material non-gating item must disclose the assumption, why it is safe enough for now, risk, scope, and revalidation point. Non-gating does not mean invisible.

| Item ID | Assumption | Why it is safe enough for now | Risk | Scope | Revalidation point |
|---|---|---|---|---|---|

### Technical review pointer

Each material technical-review item must point to where it can be inspected and how it can be challenged or changed.

| Item ID | Decision / assumption to inspect | Artifact/path | Why it matters | How to challenge or change it |
|---|---|---|---|---|

### Checkpoint terminal state supported

- Terminal state:
- Backing Current Continuation Snapshot:
- Next allowed action:

## Accepted Assumptions and Carry-Forward Records

| Item ID | Accepted/carry-forward statement | Accepted by/source | Scope | Revalidation trigger |
|---|---|---|---|---|

## Downstream Revalidation History

| Seq | Trigger | Items revalidated | Result | Controls affected |
|---:|---|---|---|---|

## Coverage and Self-Check

Before claiming readiness, implementation completion, close readiness, or normal close, verify:

- [ ] all required producer contributions are present;
- [ ] every producer contribution uses exactly one allowed outcome;
- [ ] no unresolved gated item is hidden in prose, checkpoints, implementation notes, or assumptions;
- [ ] every material item has a detail block with all required minimum fields from `_hirmos/core/protocol/UNRESOLVED_ITEMS.md`;
- [ ] every gated item has a decision owner, affected boundary, valid answer/options, and current recommendation;
- [ ] every non-gating assumption has scope, downstream impact, and revalidation point;
- [ ] every technical-review item points to an inspectable artifact/path;
- [ ] resolved items have Disposition History with “what changed”;
- [ ] reconciliation decisions preserve source evidence;
- [ ] the Current Checkpoint Feed is current when a checkpoint is surfaced;
- [ ] `SESSION_EXECUTION.md` records the latest direct unresolved-register review.
