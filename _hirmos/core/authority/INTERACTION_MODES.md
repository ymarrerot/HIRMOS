# Interaction Modes Authority

Status: core authority.
Purpose: define how HIRMOS changes visible behavior without changing governance.

## Supported modes

```text
domain_expert
technical_supervisor
framework_diagnostics
```

## Invariant

```text
Same rigor, different visibility.
```

Interaction modes may change:

- output density;
- wording style;
- checkpoint rendering;
- pause cadence;
- artifact pointer detail;
- diagnostic visibility;
- amount of technical evidence summarized in chat.

Interaction modes must not change:

- lifecycle responsibilities;
- current-state-first requirement;
- artifact obligations;
- stage ownership;
- unresolved-item classification;
- Design authority;
- Implementation authorization;
- execution controls;
- evidence standards;
- validation requirements;
- route-back rules;
- Update System State safety;
- accepted-state mutation rules.

## domain_expert

Purpose: minimize cognitive load for domain owners and non-framework users while preserving rigorous governance.

HIRMOS should attempt to advance through Understand System State and Design until one of these states:

- Needs Domain Expert Decision;
- Ready for Implementation;
- Implementation Complete;
- Ready to Update System State / Close;
- Blocked / Fail-Closed;
- Request Not Governable.

Domain Expert mode should pause only for meaningful user-owned domain, risk, resource, approval, or blocker decisions.

It should not pause merely to expose routine internal mechanics, capability routing, templates, or validation internals.

Before Implementation, it must disclose:

- what HIRMOS understood;
- what Design produced;
- gated items resolved or still blocking;
- important assumptions being carried;
- technical review path when technical assumptions matter;
- implementation-readiness status;
- how the user can change or stop before Implementation.

## technical_supervisor

Purpose: support a technical reviewer who needs inspectable governance and evidence without full diagnostics noise.

HIRMOS should surface meaningful checkpoints around:

- system-state evidence;
- Design readiness;
- implementation authorization;
- implementation-unit plan;
- validation and evidence;
- update-state readiness.

Technical Supervisor mode should include artifact references, assumptions, validation status, risks, and evidence summaries.

## framework_diagnostics

Purpose: support framework debugging, self-runs, and architecture validation.

HIRMOS may surface:

- lifecycle boundary;
- capability routing;
- execution controls;
- artifact state;
- unresolved-item classification;
- route-back triggers;
- validation decisions;
- failure reasons.

Framework Diagnostics mode is the only shipped interaction mode intended to expose deep internal mechanics by default.


## Governed checkpoint discipline

Interaction modes change how checkpoint information is rendered, not what must be governed.

Every governed checkpoint must remain backed by `SESSION_EXECUTION.md`, current execution controls, and relevant session artifacts.

- `domain_expert` hides internal machinery by default and surfaces only actionable decisions, safe baselines, important assumptions, technical-review pointers, and next actions.
- `technical_supervisor` surfaces artifact pointers, assumptions, risks, evidence status, and implementation/readiness implications.
- `framework_diagnostics` may surface producer contributions, controls, route-back records, and classification details.

No mode may hide a gated item that blocks the active lifecycle boundary.


## Runtime integration visibility

Interaction modes must preserve runtime integration and production-readiness governance.

- `domain_expert`: HIRMOS should not interrupt the user with low-level database/auth/provider choices while safe local/default progress is possible. It must surface those choices when they affect domain behavior, risk, cost, compliance, ownership, implementation authorization, or production/readiness claims. When surfaced, provide a primary HIRMOS recommendation, rationale, alternatives, decision owner, and technical-review path.
- `technical_supervisor`: surface the full integration posture table, current implementation level, recommended production option, alternatives, environment/credential needs, and evidence requirements.
- `framework_diagnostics`: surface posture classification, controls, artifacts, unresolved-item mapping, and evidence gaps.

No mode may claim production readiness when material integration posture is blocked, fixture-only, boundary-only, locally real but not production-reviewed, or unsupported by evidence, unless that limitation is explicitly named.

## Vertical slice visibility

Interaction modes affect how much vertical-slice status is shown.

- `domain_expert`: show active slice, plain-language outcome, blockers, recommendation, and next command/action.
- `technical_supervisor`: also show source contracts, evidence status, runtime integration posture, and unresolved-item disposition.
- `framework_diagnostics`: also show Delivery Unit status table, capability decisions, controls, route-backs, and artifact pointers.

Interaction modes must not change Delivery Unit status, Session Scope authority, or evidence requirements.

## Autonomous technical progress visibility

Interaction modes must support autonomous technical progress without hiding material decisions.

- `domain_expert`: HIRMOS should proceed with safe technical defaults and safe local progress without pausing for routine implementation choices. It must surface the choice when it affects domain behavior, risk, cost, compliance, ownership, implementation authorization, or production/readiness claims. When surfaced, provide one primary recommendation, concise rationale, alternatives, and next action.
- `technical_supervisor`: surface autonomous technical decisions, defaults selected, alternatives, evidence, risks, review triggers, and production-readiness impact.
- `framework_diagnostics`: surface the full attempt-before-ask trace, execution controls, capability decisions, artifacts, and evidence states.

No mode may use simplicity as a reason to hide a blocker, unsafe operation, unverified integration, or production-readiness limitation.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/support/local-runtime-evidence.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/support/role-workflow-smoke.md` records patient/staff/provider/manager/admin workflow smoke evidence.
- `_hirmos/session/support/claim-reconciliation.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.
