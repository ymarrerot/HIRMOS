# Vertical Slice and Status UX

HIRMOS should keep real software work moving without hiding governance.

The normal user experience should make the active slice clear:

```text
What are we working on now?
What is complete?
What is blocked?
What should happen next?
```

## Delivery Units

A Delivery Unit is a governed slice of delivery. A Phase is a specialized Delivery Unit when ordered staged delivery is natural.

Delivery Units give HIRMOS a simple user-facing rhythm while preserving Design authority:

```text
Delivery Plan
→ Phase / Phase Contract
→ Session Contract
→ Implementation Units
→ Evidence Review
→ Update System State
→ Next Delivery Unit recommendation
```

## Simple by default

In Domain Expert mode, HIRMOS should show a concise status and one primary next action.

Example:

```text
Phase 1 foundation is ready for implementation.
Recommended next command: hirmos continue
```

If something blocks progress, HIRMOS should show the blocker instead of hiding it to preserve momentum.

## Rigorous underneath

A status summary is not authority. HIRMOS must still use execution controls, unresolved-item governance, Session Contracts, implementation reviews, evidence records, and Update System State.

## Progressive disclosure

Technical Supervisor and Framework Diagnostics modes can show deeper artifact, evidence, route-back, and control details when needed.
