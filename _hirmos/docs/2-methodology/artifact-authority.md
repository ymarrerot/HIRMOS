# Artifact Authority

HIRMOS separates raw inputs, active session artifacts, accepted system state, and history.

## Simple rule

A useful artifact is not automatically an authority artifact.

## Key distinctions

- **Source inputs** are raw materials: notes, tickets, prototypes, screenshots, files, and user requests.
- **Active session artifacts** are runtime evidence and governed work products for the current session.
- **Accepted system state** is durable truth for future sessions.
- **History** preserves what happened and why.

## Why this matters

This prevents mistakes such as:

- treating uploaded requirements as final governed requirements;
- treating a prototype as accepted architecture;
- treating a design draft as implementation authorization;
- treating an implementation checkpoint as proof without evidence;
- treating archived artifacts as active runtime authority.

Design owns governed requirements, design, scope, delivery structure, technical review, and implementation readiness. Implementation consumes accepted Design. Update System State persists accepted outcomes.

## Durable delivery authority

For durable multi-session delivery, a Delivery Plan is needed. Separate phase files are required only when the selected delivery shape is `MULTI_SESSION_DELIVERY_WITH_PHASE_FILES`.

Durable delivery authority lives under `_hirmos/system/delivery/<delivery-id>/`, not under `_hirmos/session/`. Active sessions consume the durable Delivery Plan and `PHASE-xx.md` through `SESSION_SCOPE.md` and implementation units.


## Accepted-state navigation authority

`CURRENT_SYSTEM_STATE.md` is the accepted-state navigation authority. It maintains current governance pointers, latest-close metadata, Work History Ledger, Source Artifact Index, and concise accepted-state summaries. It is not the source authority for full requirements, design, scope, implementation, evidence, unresolved-item, or archive content. Those remain in delivery/session/archive artifacts.
