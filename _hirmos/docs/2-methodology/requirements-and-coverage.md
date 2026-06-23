# Requirements and Coverage Mapping

HIRMOS uses `REQUIREMENTS.md` to prevent requirement loss across long AI-assisted delivery runs.

Raw inputs such as uploaded requirements, notes, prototypes, screenshots, UI notes, and conversation context are source material. They become governed requirements only after they are inventoried, classified, normalized, source-mapped, and either accepted into scope or explicitly marked non-goal, gated, blocked, deferred, duplicate, superseded, or not applicable.

## Main artifact

```text
_hirmos/session/REQUIREMENTS.md
```

The active session baseline controls Design and Delivery Plan coverage.

Accepted cross-session baseline:

```text
_hirmos/system/accepted-state/REQUIREMENTS.md
```

Future sessions read the accepted baseline with `CURRENT_SYSTEM_STATE.md` so they understand both current product truth and remaining requirement coverage.

## Supporting inputs

- `DESIGN.md` source matrix: source inventory and evidence extraction.
- `DESIGN.md` source matrix: prototype-derived evidence, intended/observed behavior separation, business logic, data contracts, integrations, conflicts, and missing production concerns.
- `unresolved-items.md`: gated or unresolved requirement decisions.
- `DELIVERY_PLAN.md`: delivery-unit mapping.
- `EVIDENCE.md` claim reconciliation: evidence status for claims, not requirements coverage.

## Rule of thumb

`REQUIREMENTS.md` answers what must be satisfied and where it is mapped.

`CURRENT_SYSTEM_STATE.md` answers what is accepted current truth now.

`EVIDENCE.md` claim reconciliation answers what evidence supports claims.


## Prior framework refinements

HIRMOS keeps the current compact artifact model, but applies these lessons from the prior requirements-input-pack / requirements-SoT and prototype-ingestion work:

- strong intake comes before strong requirements;
- intake artifacts are governed but non-authoritative;
- confirmed facts, assumptions, research-backed defaults, declared delivery targets, proposed delivery targets, open questions, and pending confirmations must not be collapsed;
- prototype behavior is evidence, not authority;
- single prototypes require intended/observed/business-logic/data/integration/risk extraction;
- multiple prototypes require prototype-specific findings plus set-level reconciliation;
- conflicts and variants must be visible before requirements normalization;
- workflow-heavy requirements need explicit flows, alternates, edge cases, and expected outcomes;
- Design must route back when requirements are too vague to support implementation.

## Cross-run synthesis and requirement coverage

When HIRMOS compares multiple runs, generated apps, prototypes, external spec-tool outputs, or UX-first tools, the comparison is useful only if its lessons are routed back into the current HIRMOS authority model.

Use this routing:

- product coverage gaps → `REQUIREMENTS.md`;
- UX/operator-flow strengths → UI/UX requirement IDs, delivery-unit acceptance criteria, and role workflow smoke checks;
- engineering strengths → `DESIGN.md` technical review and implementation-unit criteria;
- testing strengths → stack evidence commands and role/workflow smoke checks;
- artifact/state weaknesses → close/update-state and claim reconciliation;
- package/handoff weaknesses → packaging protocol and package-cleanliness evidence.

This keeps cross-run learning useful without adding a separate comparison artifact layer to normal HIRMOS operation.
