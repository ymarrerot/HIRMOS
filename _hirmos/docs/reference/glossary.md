# Glossary

## Accepted State

The durable current truth HIRMOS should use at the start of future work. Accepted state is updated at close and is navigated through `CURRENT_SYSTEM_STATE.md`.

## Current-State-First

The principle that HIRMOS starts by understanding the current system before designing or implementing work.

## Delivery Baseline

A proposed durable delivery authority prepared before phase/session implementation work. It is surfaced through `Delivery Baseline — Review or Change` and stored under `_hirmos/system/delivery/<delivery-id>/` when accepted.

## Delivery Plan

The project-level delivery roadmap/register at `_hirmos/system/delivery/DELIVERY_PLAN.md`. It points to delivery authority and should not duplicate mutable runtime status.

## Derived Pointer Index

A navigation cache derived from source artifacts such as delivery directories, phase files, session archives, close records, and current-state pointers. Source artifacts win if the derived index conflicts.

## Gate

A required control recorded in `SESSION_LEDGER.md` that must be satisfied, blocked, pending, or not applicable before HIRMOS can claim progress or readiness.

## Implementation Unit / IU

A bounded implementation authority file under `_hirmos/session/implementation-units/`. IU files own unit scope, execution evidence, review, and retry records when IU mode applies.

## IU Planning

The governed step after session baseline acceptance where HIRMOS creates and validates IU files. IU Planning does not authorize material project-file edits.

## IU Execution

The governed implementation step after the user accepts the IU plan. Material project-file edits require IU Execution authorization when IU mode applies.

## Phase

A delivery unit used when ordered staged delivery is natural. Phase authority lives under `_hirmos/system/delivery/<delivery-id>/phases/` and is created just in time.

## Phase/Session Route

The route used when an accepted delivery advances into a bounded implementation session for the next phase or delivery unit.

## Session Baseline

A reviewable checkpoint that defines the active session scope before implementation or other governed work proceeds.

## Session Ledger

`SESSION_LEDGER.md`, the compact command/gate ledger for the active session.

## Session Scope

`SESSION_SCOPE.md`, the canonical active session authority.

## Unresolved Item

A governed blocker, assumption, technical-review item, or carry-forward item that must remain visible until resolved, accepted, deferred, or explicitly carried forward.
