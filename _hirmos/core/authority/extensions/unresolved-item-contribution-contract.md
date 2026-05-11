# Unresolved Item Contribution Contract

## Purpose

Define the framework-wide artifact contract for project-level unresolved-item contribution, inventory, reconciliation, feed, and ledger traceability across HIRMOS lifecycle runs.

This file owns the shared unresolved-item artifact schemas and traceability requirements used by project lifecycle runs such as:

- `requirements-agent:requirements`
- `system-design-agent:system-design`
- future lifecycle entrypoints that need unresolved-item centralization

This file does **not** own a specific lifecycle workflow. Each lifecycle spec owns its own sequencing, fail-closed behavior, completion gating, and lifecycle-specific pause/continue rules.

## Lifecycle binding requirement

Every lifecycle that uses this contract must define its lifecycle binding, including:

- lifecycle identifier, such as `requirements-agent:requirements`;
- active run context path for run controls/traces;
- the project-level unresolved-item artifact set it contributes to or reconciles;
- lifecycle spec that owns sequencing and completion behavior;
- producer artifacts expected to contribute unresolved items;
- whether the lifecycle consumes unresolved outputs from an earlier lifecycle.

The lifecycle binding may live in the extension-local specs directory, but it must not redefine the schema owned by this contract or create a competing unresolved-item inventory.

## Covered artifact names

This contract governs the shape and traceability expectations for these canonical project-level artifacts:

- `UNRESOLVED_ITEMS_INVENTORY.md`
- `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
- `UNRESOLVED_ITEMS_FEED.md`
- `UNRESOLVED_ITEMS_LEDGER.md`

The canonical project-level paths are:

```text
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_FEED.md
_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_LEDGER.md
```

Extension- or lifecycle-scoped unresolved-item inventory paths must not be treated as canonical.

Use the shared unresolved-item artifact names under `_hirmos/artifacts/context/project/`. Do not introduce lifecycle-specific unresolved-decision bypass artifacts.

## Canonical producer unresolved sources

Producer-local unresolved items must be surfaced under:

- `## Unresolved Items`
  - `### Assumptions`
  - `### Open Questions`

Both subsections are canonical unresolved-item sources for project-level centralization.
Neither is secondary.

Validation-discovered gaps are allowed only as a backstop when a materially relevant unresolved item was not surfaced by the producer in its canonical unresolved-item section.

## Inventory item contract

Each inventory item must include:

- `Inventory Item ID`
- `Producer artifact`
- `Source subsection`
  - `Assumptions`
  - `Open Questions`
  - `validation-discovered`
- `Source wording`
- `Normalized summary`
- `Item type`
  - `explicit-assumption`
  - `explicit-open-question`
  - `validation-discovered-gap`
- `Why it matters`
- `Impact area`
- `Distinctness note`
  - `distinct`
  - `candidate-merge`
- `Provisional merge target` when relevant

## Producer-in-lifecycle contribution structure

The unresolved-item inventory remains lifecycle-owned.

When a producer is executed inside a lifecycle context, it may update only its own producer-scoped contribution section inside the project-level canonical `UNRESOLVED_ITEMS_INVENTORY.md` artifact before leaving the producer workflow.

Each producer-scoped contribution record must preserve the canonical inventory fields needed for later lifecycle-owned reconciliation, including:

- `Inventory Item ID`
- `Producer artifact`
- `Source subsection`
- `Source wording`
- `Normalized summary`
- `Why it matters`
- `Impact area`
- `Distinctness note`
- `Provisional merge target` when relevant

Producer contribution sections are preparatory inventory-stage records only.

Producers must not:

- reconcile feed items;
- merge across producers;
- classify final gating severity;
- decide final handling outcomes;
- append ledger outcomes on behalf of the lifecycle.

Later reconciliation, feed construction, ledger updates, and final completion/gating truth remain lifecycle-owned.

## Reconciliation worklist contract

Each reconciliation entry must include:

- `Source inventory item IDs`
- `Disposition`
  - `distinct-feed-item`
  - `merged-into-existing-item`
  - `rejected-invalid`
  - `no-longer-current`
- `Final target ID` when applicable
- `Justification`

When a reconciliation entry merges multiple inventory items into one feed item, it must also include merge-audit fields:

- `Shared decision`
- `Decision domain`
- `Distinctness check`
- `Information preserved`
- `Why not separate`

Merge-audit fields are validation-relevant.

A merge is invalid if the source items do not genuinely collapse into one shared unresolved decision.
Items from different primary decision domains must not be merged merely because they currently share the same handling outcome, downgrade posture, general project area, or broad readiness / operational-truth effect.

Broad reasoning such as "they jointly determine readiness", "they all affect operational truth", or "they are all gating" is not sufficient by itself.

A valid merge must also prove at least one of the following:

- one concrete shared customer question;
- one concrete Orchestrator decision;
- one clearly bounded primary decision domain.

Example primary decision domains include:

- identity / access model;
- workflow / operational model;
- reporting / export contract;
- architecture / deployment shape;
- privacy / compliance posture;
- readiness / rollout threshold.

## Feed item contract

Each accepted feed item must include:

- `Feed Item ID`
- `Title / summary`
- `Severity classification`
- `Why it matters`
- `Source inventory item IDs`
- `Producer coverage`
- `Origin classification`
  - `assumption`
  - `open-question`
  - `mixed`
  - `validation-discovered`
- `Touches gating-default category`
  - `yes`
  - `no`
- `Gating-default categories touched`
  - `<list>`
  - `none`
- `Downgrade justification`
  - `<text>`
  - `none`
- `Merge note` when applicable

## Ledger traceability contract

The ledger is the lifecycle trace across runs and reruns. Every reconciliation or feed outcome recorded in the ledger must trace back to source inventory item IDs.

When a feed item touching a gating-default category is classified below gating, the ledger must preserve the downgrade justification used for that run.

## Validation backstop

Explicit producer `Unresolved Items` sections are the primary unresolved-item source.

If validation discovers a materially relevant unresolved item that was not surfaced there, the lifecycle must either:

- register it in the inventory as `validation-discovered-gap`; or
- explicitly reject it with reason.

Such gaps must never disappear silently.

## Producer extraction coverage contract

The lifecycle must preserve extraction coverage by producer and by canonical subsection.
Coverage must distinguish:

- subsection present and inventoried;
- subsection present but empty;
- subsection present but items rejected;
- subsection missing.

For each required producer, preserve or surface:

- `Producer artifact`
- `Assumptions subsection status: present-with-items | present-empty | missing`
- `Open Questions subsection status: present-with-items | present-empty | missing`
- `Assumptions extracted count`
- `Open Questions extracted count`
- `Assumptions rejected count`
- `Open Questions rejected count`

Coverage counts must be inventory-derived.
Any reported extracted count for a producer subsection must be derived from actual inventory entries whose:

- `Producer artifact` matches that producer;
- `Source subsection` matches that subsection.

Free-form or estimated extraction counts are invalid.
Coverage reporting must not claim extraction counts that the inventory body cannot support.

If a report says a producer subsection yielded `N` extracted items, the inventory body must contain exactly `N` matching inventory entries for that producer/subsection.

If the subsection was present but yielded no inventoried items, the lifecycle must explicitly record either:

- `present-empty`; or
- rejected items with reasons.

If a canonical unresolved item from `Assumptions` or `Open Questions` is not inventoried, the lifecycle must record an explicit rejection reason.
Silent non-registration is invalid.

## Ownership boundaries

This file owns unresolved-item artifact schemas and traceability requirements.

Lifecycle specs own:

- workflow sequencing;
- fail-closed behavior;
- completion gating;
- lifecycle-specific severity thresholds;
- lifecycle-specific pause/continue behavior.

Producer specs own:

- local unresolved-item surfacing inside their artifacts;
- producer-specific self-validation;
- producer-scoped inventory contribution before returning to the lifecycle.

Templates and docs must not re-own this contract.
