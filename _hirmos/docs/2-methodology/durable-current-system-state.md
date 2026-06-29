# Durable Current System State

`CURRENT_SYSTEM_STATE.md` is the accepted-state navigation surface for the next HIRMOS run.

It should answer:

```text
What is the accepted current state of this project, and where is the source evidence?
```

It should not become a duplicate narrative of every delivery, phase, session, evidence record, or archive file.

## Ownership

`CURRENT_SYSTEM_STATE.md` owns:

- compact accepted-state posture;
- active/next delivery pointers when delivery mode applies;
- latest accepted close pointer;
- Work History Ledger pointers;
- Source Artifact Index pointers;
- known limitations and carry-forward pointers when accepted at close.

It does not own:

- detailed delivery scope;
- phase progress detail;
- session scope detail;
- IU evidence detail;
- archive content;
- mutable next-command truth.

## Derived pointer discipline

Pointer indexes are navigation caches. They should be derived from source artifacts whenever possible:

- delivery directories;
- phase files;
- session archives;
- `SESSION_LEDGER.md` close rows;
- archive manifests;
- accepted close evidence.

If a derived pointer conflicts with a source artifact, the source artifact wins and the stale pointer should be corrected or validation should fail closed.

## Delivery mode

For multi-session work, Current System State may point to:

```text
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

Those delivery and phase artifacts remain authority for their own scope. Current System State is a map, not a second copy of their contents.

## Close-time update

At close, HIRMOS should update Current System State only with accepted outcomes and source pointers. Evidence-only artifacts remain in archive unless explicitly accepted into current state.

Do not use Current System State to hide unresolved items, overclaim production readiness, or rewrite history.


## Supporting artifacts

Current System State points to supporting artifacts such as delivery scope, session archives, evidence records, carry-forward records, and source artifact indexes. Those supporting artifacts retain their own authority; Current System State should not duplicate them.


## Accepted-state invariants and canonical values

Accepted-state artifacts should use canonical runtime posture values, evidence states, and production-readiness language so future sessions can read them consistently.


## Active delivery pointers

When delivery mode is active, Current System State may contain Active delivery pointers to the delivery plan, delivery scope, active phase/session, latest accepted close, and next recommended delivery work. Future sessions must inspect these pointers, then read the source artifacts before acting.
