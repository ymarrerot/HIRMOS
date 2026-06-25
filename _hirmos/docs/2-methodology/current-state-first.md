# Current-State-First Work

HIRMOS is current-state-first for governed software work.

That means HIRMOS must establish enough current system state before it designs, implements, validates, or updates accepted state. The user request focuses the work, but the current system state grounds what HIRMOS may safely claim or change.

## Why this matters

AI-assisted development often fails when the agent starts from the latest instruction alone:

```text
User asks for a change
→ agent assumes the project shape
→ agent edits files against stale or incomplete context
→ implementation appears complete
→ hidden conflicts appear later
```

HIRMOS uses a different posture:

```text
User asks for a change
→ HIRMOS inspects current state
→ HIRMOS identifies the governed work
→ HIRMOS implements only accepted scope
→ HIRMOS records evidence
→ HIRMOS updates current state after close
```

## Two kinds of system understanding

Understand System State includes two complementary tracks:

1. **General System State Understanding** — the broad shape of the project, stack, repository, maturity, docs, current accepted state, and evidence reliability.
2. **Focused System State Understanding** — the files, flows, requirements, architecture, runtime behavior, and constraints directly or indirectly affected by the User Request and source inputs.

A User Request guides focus, but it does not become final authority by itself.

## Greenfield, brownfield, and mixed projects

Current-state-first applies to all project types:

- **Greenfield** work starts by understanding the intended starting point, available requirements, empty or scaffolded repository state, and first safe slice.
- **Brownfield** work starts by understanding the existing system before changing it.
- **Mixed** work starts by separating what already exists from what is new, uncertain, or proposed.

HIRMOS does not need the user to classify the project perfectly. It should infer enough from the current state and ask or record unresolved items when the distinction affects the work.

## Raw inputs are not authority

Uploaded notes, tickets, prototypes, screenshots, requirements documents, chat history, and exploratory code are source inputs. They help HIRMOS understand what to inspect and what the user may want, but Design must convert them into governed requirements, scope, and implementation authorization.

Useful source material can become authority only after HIRMOS reconciles it with current state and accepted design.

## Prototype and POC inputs

Prototype and POC materials are common starting points. HIRMOS treats them as evidence, not architecture authority by accident.

Good prototype ingestion separates:

- intended behavior;
- observed behavior;
- accidental implementation details;
- business logic;
- data contracts;
- integrations;
- conflicts or variants;
- missing decisions.

## Brownfield importance

In brownfield work, current-state-first prevents HIRMOS from designing or implementing changes against stale assumptions. The request shapes what HIRMOS inspects, but repository and accepted-state evidence govern what HIRMOS may safely claim.

## What users should expect

Before implementation, a good HIRMOS run should usually make the active understanding visible at the right level:

- what it found in the current state;
- what work is in scope;
- what assumptions it is carrying;
- what decisions block progress;
- what it will build or design next;
- what evidence will be needed before close.

The amount of detail should follow progressive disclosure: simple when the path is clear, more explicit when risk, uncertainty, or scope increases.


## Generated artifact wording note

Generated HIRMOS artifacts should explain routing from current-state evidence and governance need. Project-type labels are supporting metadata, not the primary authority for selecting delivery, phase, or session shape.

## Canonical Source Reading Discipline

Current-state-first means reading `CURRENT_SYSTEM_STATE.md` as the navigation authority and then following the relevant canonical source pointers. It does not mean designing from summary prose alone.

Before material design or implementation, HIRMOS reads the active delivery/session/phase authorities, unresolved registers, evidence, carry-forward, and source requirement/design artifacts that materially affect the request. Reading depth is scoped to the request; the canonical navigation path is not optional.
