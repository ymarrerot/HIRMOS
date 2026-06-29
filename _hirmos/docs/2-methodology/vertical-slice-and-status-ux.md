# Vertical Slice and Status UX

HIRMOS should make progress visible without turning status text into authority.

## Delivery Units

A Delivery Unit is a governed slice of delivery. A Phase is a specialized Delivery Unit when ordered staged delivery is natural.

A typical delivery rhythm is:

```text
Delivery Plan
→ Delivery Baseline
→ Phase/session baseline
→ IU Planning when needed
→ IU Execution
→ Close / Update System State
→ Next Delivery Unit recommendation
```

## Status is not authority

A status summary is a user-facing navigation aid. HIRMOS must still use execution controls, unresolved-item governance, Session Scopes, implementation reviews, evidence records, and Update System State.

Prefer derived pointer indexes over duplicated mutable status fields. The source artifacts and evidence remain authority.


## Onboarding posture

- Simple by default: show the next slice and next command clearly.
- Rigorous underneath: keep scope, evidence, and close gates authoritative.
- Progressive disclosure: link deeper details only when the user needs them.
