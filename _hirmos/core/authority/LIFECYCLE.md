# Lifecycle Authority

Status: core authority.
Purpose: define HIRMOS lifecycle responsibilities and route-back rules.

## Canonical request flow

```text
User Request
↓
Understand System State
→ Design
→ Implementation
→ Update System State
```

This is an ordered governance lifecycle, not a waterfall and not a loose capability bag.

## Production-shaped implementation posture

HIRMOS implementation aims to produce production-shaped software by default. A session may intentionally produce a prototype, demo, fixture, local-only result, or throwaway experiment, but that limitation must be explicitly authorized in `SESSION_SCOPE.md`, reflected in Design when Design is active, and preserved during Update System State.

Production-shaped does not mean enterprise-grade, cloud-only, overbuilt, or fully deployed. It means the implementation should follow the architecture shape that would reasonably support production use for the requested system: durable data where durability matters, production-aligned local infrastructure where practical, real integration boundaries, safe secret/configuration handling, long-running work outside synchronous request paths, and evidence for critical flows.

Core HIRMOS owns this posture. Selected-stack standards translate it into stack-specific defaults.


Extension capabilities execute inside lifecycle-stage responsibilities. They do not replace the lifecycle.

Lifecycle stages define the responsibility boundary. Extension capabilities are activated only when the active lifecycle stage needs specialized work to satisfy that boundary. Command-driven capability activation is governed by `_hirmos/core/protocol/COMMANDS.md`; capability discovery, routing, entrypoint resolution, and capability-decision recording are governed by `_hirmos/core/protocol/CAPABILITY_ROUTING.md`.

## User Request

A User Request starts and focuses the work, shaping focused system-state understanding.

A User Request may include prose, uploaded requirements, tickets, screenshots, prototypes, proof-of-concept code, existing docs, or other source inputs.

A User Request is not:

- governed requirements;
- design authority;
- implementation authorization;
- accepted system state;
- validation evidence by itself.

## Understand System State

Understand System State grounds the session in current project truth and is mandatory before HIRMOS performs governed software work that designs, implements, validates, accepts, or changes anything about a software system.

It owns:

- request signal extraction;
- source input inventory;
- prototype or source-material evidence classification;
- general system-state understanding;
- User Request-focused system-state understanding;
- observed, inferred, assumed, unknown, stale, and contradictory-state separation;
- current-state confidence;
- constraints and preservation requirements discovered from current state;
- handoff evidence to Design.

It does not own:

- requirements authority;
- design authority;
- delivery-plan authority;
- implementation authorization;
- accepted system-state mutation.

## Design

Design owns governed definition of what should happen and what is allowed next.

It owns:

- governed requirements;
- system and application design;
- delivery plan;
- delivery-unit or phase planning;
- delivery-unit or phase scopes;
- preservation scope when needed;
- regression evidence strategy when needed;
- session scope;
- unresolved-item disposition for Design decisions;
- technical review pointer;
- completion criteria;
- implementation authorization;
- implementation-readiness decision.

Design can satisfy requests whose requested outcome is requirements, design, planning, scoping, or decision resolution. Implementation is not mandatory for those sessions.

Design does not perform implementation or mutate accepted system state.

## Implementation

Implementation is governed realization of accepted Design with evidence. It is not only coding.

It owns:

- implementation-unit planning;
- implementation-unit requests;
- project-file changes when authorized;
- implementation execution;
- validation execution;
- implementation-unit review;
- retry and escalation;
- evidence capture;
- session implementation review;
- implementation completion decision.

Implementation does not own requirements authority, design authority, session-scope authority, or accepted system-state mutation.

If Implementation discovers that Design or system-state evidence is wrong, incomplete, or unsafe, it must record the blocker and route back to the owning stage. It must not silently rewrite Design authority.

## Update System State

Update System State preserves accepted, reviewed outcomes as durable system state and session history.

It owns:

- update-state readiness;
- accepted-outcome decision;
- accepted state update;
- non-application records;
- carry-forward unresolved items;
- session close;
- session archive;
- future-session readiness.

Update System State does not implement, invent missing requirements, repair incomplete Design, or silently complete missing Implementation evidence.

## Route-back and regeneration

The lifecycle is ordered, but later stages may discover new truth that invalidates earlier assumptions.

Route-back is required when:

- Design discovers current-state uncertainty that blocks safe Design;
- Implementation discovers new system truth or invalid Design assumptions;
- validation evidence contradicts requirements, Design, scope, or implementation claims;
- Update System State finds incomplete evidence, unresolved gated items, or unsafe accepted-state mutation.

Route-back must:

1. record the discovery;
2. identify the owning lifecycle stage;
3. block the affected continuation claim;
4. regenerate or amend the owning artifact explicitly;
5. preserve history of the change.

## Current-State-First Source Reading Discipline

Understand System State is source-directed, not summary-directed. HIRMOS must read `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` first, then follow the current-state navigation spine to the relevant canonical source artifacts before material Design, Implementation, continuation, or close decisions.

Mandatory navigation spine:

- Current Governance Context;
- Accepted-State Navigation and Latest Close;
- Work History Ledger;
- Source Artifact Index;
- active carry-forward pointer or carry-forward summary;
- next governed command / next recommended work.

Required source-reading behavior:

1. Read `CURRENT_SYSTEM_STATE.md` before treating any delivery, session, archive, chat transcript, generated report, or remembered context as current truth.
2. Read active-governance pointers when present: active delivery scope, active phase, active session scope, active unresolved registers, latest close/archive pointer, and active carry-forward records.
3. Read source artifacts materially relevant to the user request before material Design or Implementation. Source artifacts may include delivery/session scope, optional requirements/design, phase files, unresolved registers, implementation-unit records, evidence, close/archive records, and stack guidance.
4. Use scoped/progressive reading depth. Small isolated requests require only directly relevant sources; broad planning, architecture, refactor, requirements, close, or delivery/session continuation requires deeper source coverage.
5. Record material read coverage in `SESSION_EXECUTION.md` or `BOOTSTRAP_REPORT.md` when the session will design, implement, close, or update accepted state.
6. If a required source artifact is missing, stale, contradictory, or inaccessible, surface it as an unresolved item, technical-review item, or fail-closed blocker before proceeding.

This rule reuses existing `CURRENT_SYSTEM_STATE.md`, `SESSION_EXECUTION.md`, bootstrap, unresolved-item, and evidence surfaces. Do not add a new governance artifact only to record source reading unless the existing surfaces cannot safely own the responsibility.

Current-state understanding is source-complete, not content-complete: it must identify and read the canonical sources needed for the request without duplicating every source into one summary artifact.
