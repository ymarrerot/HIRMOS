# Unresolved Items Protocol

Status: core protocol.
Purpose: define how unresolved decisions, assumptions, blockers, risks, and uncertainties control continuation.

Unresolved items are continuation-control records, not notes.

The central active-session artifact is:

```text
_hirmos/session/unresolved-items.md
```

This register is the authoritative active-session source for unresolved-item details. Summaries in `SESSION_SCOPE.md`, checkpoints, `SESSION_EXECUTION.md`, or user-facing responses are control summaries only and are never sufficient substitutes for reading and applying `_hirmos/session/unresolved-items.md` directly.

## Required lifecycle

Unresolved-item handling follows this sequence:

```text
Producer discovery
→ Producer contribution
→ Central inventory
→ Reconciliation and classification
→ Pause / carry-forward / fail-closed decision
→ Disposition history
→ Downstream revalidation
```

A lifecycle boundary or capability must not claim completion while required unresolved-item work for that boundary is incomplete.

Before claiming any of these boundaries, HIRMOS must directly review `_hirmos/session/unresolved-items.md` and record the review result in `SESSION_EXECUTION.md` controls:

```text
bootstrap completion when a command will follow
implementation readiness
implementation completion
checkpoint surfacing
Update System State
close readiness
normal close
```

## Producer discipline

Every lifecycle stage and capability is an unresolved-item producer.

Each producer must contribute exactly one producer outcome to `_hirmos/session/unresolved-items.md` for the boundary it touched:

```text
ITEMS_FOUND
NONE_FOUND
NOT_APPLICABLE
BLOCKED
```

A producer must not hide unresolved items inside prose, local notes, implementation comments, checkpoint summaries, implementation-unit notes, or artifact assumptions. If the item affects continuation, scope, risk, authority, implementation, validation, accepted state, or user decision authority, it belongs in the central unresolved inventory.

Producer contributions must include:

- producer name;
- lifecycle stage;
- source artifact or evidence;
- contribution outcome;
- candidate items or explicit none/not applicable/blocker statement;
- reason the producer believes the contribution is complete for the current boundary.

A producer that creates a user-facing decision, readiness claim, completion claim, blocker, route-back, or non-gating assumption must provide enough backing information to populate the Current Checkpoint Feed.

## Required classifications

```text
GATED
NON_GATING
TECHNICAL_REVIEW
RESOLVED
DUPLICATE
NOT_APPLICABLE
```

`GATED` means the item blocks a lifecycle boundary unless resolved, explicitly baselined by the responsible decision owner, or routed back.

`NON_GATING` means HIRMOS may continue only if the assumption, constraint, owner/source, impact, and downstream revalidation point are recorded.

`TECHNICAL_REVIEW` means the item does not require immediate domain-owner input but must be inspectable by a technical reviewer before the affected boundary is trusted.

`RESOLVED` means the item has a disposition history entry explaining the decision/change and what changed.

`DUPLICATE` means the item has been merged or linked without losing original source evidence.

`NOT_APPLICABLE` means the producer or item was assessed and found irrelevant to the affected boundary.

## Minimum fields

Every unresolved item must preserve these minimum fields in the register:

- id;
- title;
- description;
- source producer or capability;
- source evidence;
- classification;
- decision owner;
- visibility posture;
- affected lifecycle boundary;
- current status;
- current recommendation;
- options or valid answer shape when user input is required;
- assumption if carried;
- downstream impact;
- disposition history;
- revalidation point.

A table row may summarize the item, but the register must also preserve a detail block for each material item when the table does not contain all minimum fields. Missing minimum fields are not harmless omissions; they are unresolved-governance defects.

## Field completeness rule

Before a producer, checkpoint, implementation-readiness boundary, implementation-completion boundary, or close boundary may claim completion:

- every `ITEMS_FOUND` contribution must be represented in the central inventory;
- every material item must have the minimum fields above;
- every `GATED` item must have decision owner, affected boundary, valid answer/options, and current recommendation;
- every `NON_GATING` item must have assumption, downstream impact, and revalidation point;
- every `TECHNICAL_REVIEW` item must have an inspectable review path;
- every `RESOLVED` item must have disposition history explaining what changed;
- every producer that found no material item must still record `NONE_FOUND`, `NOT_APPLICABLE`, or `BLOCKED` with rationale.

If any required field is unknown, write `UNKNOWN` and explain why. Unknown required fields on gated items block the affected boundary unless explicitly baselined by the decision owner.

## Reconciliation discipline

HIRMOS must reconcile duplicate and related items without over-merging distinct decisions.

When merging items, preserve original sources and decision history.

Use these reconciliation actions:

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

Anti-overmerge rule: do not merge items merely because they mention the same domain area. Merge only when they ask for the same decision or carry the same assumption with the same affected boundary.

## Current checkpoint feed

Before surfacing a governed checkpoint, HIRMOS must prepare the Current Checkpoint Feed in `_hirmos/session/unresolved-items.md`.

The feed must include:

- gated items requiring user action;
- safe HIRMOS recommendation or baseline, if available;
- non-gating assumptions being carried;
- technical-review items and inspection path;
- affected lifecycle boundary;
- next action after the user responds or after assumptions are carried.

The feed is the source for user-facing unresolved-item checkpoint output. It is not a substitute for the full inventory.

## Canonical checkpoint behavior

Under the canonical interaction posture:

- gated user-owned Domain/Risk/Resource/Approval items must be surfaced clearly;
- HIRMOS should recommend a baseline when safe;
- accepted baseline decisions must be recorded in disposition history;
- non-gating assumptions may be carried but must be disclosed at the appropriate checkpoint;
- technical assumptions should be reviewable through technical-review artifacts when relevant;
- governed references should include artifact paths;
- diagnostic mechanics remain available in artifacts and should be surfaced when requested or when needed to explain risk, blocker state, validation failure, or route-back.

## Blocking rules

Design cannot claim implementation authorization while gated Design items remain unresolved.

Implementation-readiness cannot pass while an affected gated unresolved item remains unresolved or blocked.

Implementation cannot proceed when a gated item affects the Session Scope, Implementation Unit authority record, validation evidence, or preservation constraint.

Update System State and close cannot proceed when a gated item affects accepted outcomes, rejected outcomes, carry-forward status, or archive readiness.

## Disposition and revalidation

Every user answer, accepted baseline, assumption carry-forward, route-back, reclassification, or resolution must be appended to Disposition History.

Every non-gating or technical-review item must have a downstream revalidation point. When that point is reached, HIRMOS must record the revalidation result before claiming the affected boundary is complete.

## Validation implications

Validators and static checks should enforce the presence of this protocol, the canonical `unresolved-items.md` template, producer obligations that explicitly reference this protocol, and template fields required to preserve item-level details.

Runtime or close-time validators should fail when:

- `_hirmos/session/unresolved-items.md` is missing during an active governed session;
- a lifecycle boundary is claimed without a direct unresolved-register review;
- `SESSION_SCOPE.md` contains unresolved-item details instead of only the compact control summary;
- a producer obligation omits the protocol reference;
- item records lack required minimum fields;
- non-gating assumptions lack revalidation points;
- resolved items lack disposition history.


## Start checkpoint disclosure rule

The `hirmos start` implementation-readiness pause must source gated items, non-gating assumptions, and technical-review pointers from `_hirmos/session/unresolved-items.md#Current Checkpoint Feed` and render them through `_hirmos/core/templates/checkpoints/START_CHECKPOINT_OUTPUT.md`. The user-facing checkpoint must not summarize unresolved items from memory or hide material non-gating assumptions.

## Gated Item Continue Semantics

A gated item blocks the boundary it governs until it is resolved, explicitly adopted from a surfaced recommendation, converted to a documented non-gating assumption, or deferred with an accepted carry-forward target.

HIRMOS must not allow a bare `hirmos continue` to silently accept a baseline when a gated item is still classified as pending user input and not reflected in the relevant delivery/session authority.
