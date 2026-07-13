# Unresolved Items

Unresolved items are continuation-control records, not notes.

Unresolved decisions require governance because unrecorded decisions become system behavior. Serious software work needs a durable record of what is unknown, who can decide it, whether work may safely continue, and where the decision must be revalidated.

HIRMOS uses unresolved-item governance to prevent hidden assumptions from becoming implementation direction. AI-assisted development makes this more acute because an agent can select defaults quickly and invisibly unless the workflow forces uncertainty to be surfaced. When a question, assumption, blocker, ambiguity, or technical concern can affect the work, HIRMOS records it, classifies it, and applies it at lifecycle boundaries.

Authoritative active-session register:

```text
_hirmos/session/unresolved-items.md
```

`SESSION_SCOPE.md` may contain a compact control summary, but that summary is not sufficient for review, implementation, continuation, continuation checkpointing, or close. HIRMOS must read and apply the register directly before every lifecycle boundary.

## The simple idea

HIRMOS does not need every question answered before work can begin.

But it must know the difference between:

```text
A decision that blocks safe progress
```

and:

```text
An assumption that can be carried temporarily and revalidated later
```

That distinction is what makes HIRMOS practical without becoming careless.

## Basic classification

- **Gated** — must be resolved before the affected lifecycle boundary can continue.
- **Non-gating** — can be carried as an explicit assumption or constraint only when owner/source, impact, and revalidation point are recorded.
- **Technical review** — inspectable technical assumption or risk that does not require immediate domain-owner input.
- **Resolved** — item has disposition history and “what changed.”
- **Duplicate** — item was merged without losing source evidence.
- **Not applicable** — producer or item was assessed and found irrelevant to the affected boundary.

## When an item is gated

An item should be gated when continuing without a decision could cause material rework, unsafe behavior, false claims, or unauthorized scope.

Examples:

- implementing real payments before the payment approach is authorized;
- changing production-facing behavior without ownership or compliance clarity;
- choosing a data model when unresolved requirements change core entities;
- closing a session while acceptance evidence is missing;
- entering a phase when the phase entry gate is not satisfied.

## When an item is non-gating

An item can be non-gating when HIRMOS can make a safe, explicit, reversible assumption for the current bounded work.

Examples:

- using a local development default while production configuration remains open;
- implementing a provider adapter before real credentials are available;
- carrying a UI copy assumption until product review;
- limiting a first implementation slice while a larger delivery remains planned.

Non-gating does not mean forgotten. It means recorded, bounded, and revalidated at the right point.

## Producer discipline

Each stage or capability that can discover unresolved items must contribute exactly one producer outcome:

```text
ITEMS_FOUND
NONE_FOUND
NOT_APPLICABLE
BLOCKED
```

This keeps HIRMOS from skipping uncertainty simply because a producer stayed silent.

Every producer must apply:

```text
_hirmos/core/protocol/UNRESOLVED_ITEMS.md
```

## Minimum item fields

Every material unresolved item must preserve:

- id;
- title;
- description;
- source producer or capability;
- source evidence;
- classification;
- decision owner;
- visibility mode;
- affected lifecycle boundary;
- current status;
- current recommendation;
- options or valid answer shape when user input is required;
- assumption if carried;
- downstream impact;
- disposition history;
- revalidation point.

For dense or important items, use detail blocks in `_hirmos/session/unresolved-items.md`; do not rely only on summary tables.

## Central inventory

The active session maintains unresolved items in `_hirmos/session/unresolved-items.md`.

That artifact preserves:

- register controls;
- Producer Contributions;
- Inventory Summary;
- Required Item Detail Blocks;
- reconciliation and classification;
- active gated items;
- active non-gating items;
- technical-review items;
- current checkpoint feed;
- disposition and carry-forward history.

## What users should expect

A good HIRMOS run should not flood the user with every small uncertainty. It should surface the items that materially affect scope, safety, architecture, acceptance, or next action.

The user should be able to answer:

```text
What is blocked?
What assumption is being carried?
When will it be revisited?
What can continue safely now?
```
