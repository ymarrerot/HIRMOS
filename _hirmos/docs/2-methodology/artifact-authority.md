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

For multi-session work in any project type, a Delivery Plan is needed and separate phase files are required.

Durable delivery authority lives under `_hirmos/system/delivery/<delivery-id>/`, not under `_hirmos/session/`. Active sessions consume the durable Delivery Plan and `PHASE-xx.md` through `SESSION_CONTRACT.md` and implementation units.
