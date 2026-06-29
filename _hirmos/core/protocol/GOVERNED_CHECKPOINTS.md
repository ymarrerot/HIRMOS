# Governed Checkpoints Protocol

Status: core protocol.
Purpose: define how HIRMOS surfaces user-facing checkpoints without heavy output-governance machinery.

Governed checkpoints are user-facing outputs that can affect continuation. They must follow the canonical HIRMOS interaction posture and be backed by existing session artifacts.

## Required rule

HIRMOS must not surface a checkpoint that claims a decision, readiness state, artifact availability, implementation authorization, evidence result, or close/update readiness unless the claim is backed by existing non-placeholder session artifacts and current `SESSION_LEDGER.md` controls.

## Checkpoint types

Use these baseline checkpoint types:

```text
NEEDS_USER_DECISION
IMPLEMENTATION_READINESS
IMPLEMENTATION_COMPLETE
UPDATE_SYSTEM_STATE_READINESS
BLOCKED_FAIL_CLOSED
REQUEST_NOT_GOVERNABLE
STATUS_ONLY
```

## Required checkpoint inputs

Before surfacing a governed checkpoint, verify and record in `SESSION_LEDGER.md`:

- checkpoint type;
- active lifecycle boundary;
- canonical interaction posture acknowledgement;
- backing artifacts;
- relevant execution controls and statuses;
- unresolved-item status;
- user action required, if any;
- terminal state or next allowed action.

## Required Current Continuation Snapshot

For checkpoints that request a user decision, claim implementation-readiness, claim implementation completion, claim update-state readiness, fail closed, pause, or change continuation state, HIRMOS must update `_hirmos/session/SESSION_LEDGER.md` → `Current Continuation Snapshot` before surfacing the user-facing checkpoint.

The snapshot must summarize the current lifecycle stage, terminal state, authoritative artifacts reviewed, unresolved status, evidence status, next safe governed command, and what the next model must not do.

Status-only command output may be read-only and does not require a snapshot update unless it changes continuation state.

## Canonical user-facing rendering

By default, the checkpoint should show only:

- what HIRMOS understood or completed;
- what HIRMOS needs from the user, if anything;
- the recommended baseline when safe;
- important assumptions being carried;
- technical review pointer when relevant;
- what happens next;
- how to change, stop, or ask for details.

Do not expose execution-control tables, capability routing, or internal diagnostics by default.

## Progressive disclosure and inspection

Include artifact pointers, assumptions, risks, validation/evidence status, implementation/readiness implications, lifecycle boundary, capability routing, execution controls, unresolved classification, route-back triggers, and validation details when the user asks, validation fails, blocker state requires explanation, or inspection is necessary to act responsibly.

## Unresolved-item checkpoint rule

A checkpoint that asks for user input must be sourced from `_hirmos/session/unresolved-items.md` when the input concerns decisions, assumptions, risks, scope, blockers, or continuation.

Gated items must be surfaced before they block Design, Implementation, implementation-readiness, Update System State, or close.

Non-gating assumptions may be carried only when the assumption, risk, scope, owner/source, and revalidation point are recorded in `_hirmos/session/unresolved-items.md`.

## Checkpoint completion

A checkpoint is complete only when:

- Current Continuation Snapshot is current when required;
- `SESSION_LEDGER.md` Continuation Boundary Log records the surfaced boundary;
- execution controls reflect the checkpoint terminal state;
- unresolved-item dispositions affected by the checkpoint are recorded;
- the user-facing output does not claim more than the artifacts support.


## Production readiness checkpoints

When HIRMOS approaches production-readiness or release-readiness, a governed checkpoint must include material runtime integration status.

The checkpoint must be backed by `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` when material integration areas exist.

Under the canonical posture, the checkpoint should surface:

- current implementation level in plain language;
- HIRMOS primary recommendation for each material production choice;
- alternatives and when an engineer might choose them;
- decision owner;
- blockers, credentials, accounts, compliance, or ownership items;
- whether the app is production-ready, locally real only, boundary-only, fixture/demo-backed, or blocked.

Do not expose the internal taxonomy unless needed; do not hide limitations when readiness is claimed.

## Claim reconciliation checkpoint rule

A governed checkpoint that claims readiness, implementation completion, runtime readiness, production readiness, update-state readiness, or close success must cite claim reconciliation evidence.

If claim reconciliation downgrades the claim, the checkpoint must surface the downgraded truthful claim instead of the original stronger claim.

## Autonomous technical decision checkpoints

A governed checkpoint must surface autonomous technical decisions when they become material to continuation, implementation authorization, technical review, production readiness, or release readiness.

Use `_hirmos/session/DESIGN.md` as the backing artifact for technical decisions and `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` for material integration posture.

By default, summarize only:

- the decision HIRMOS made or recommends;
- why it is safe or why it needs review;
- what remains blocked before production readiness;
- one primary next action.

Include alternatives, evidence, risks, and review triggers when requested or when needed to explain a material decision, blocker, route-back, or evidence gap.

## Local setup and role-workflow smoke evidence

Use `LOCAL_TECHNICAL_SETUP_AND_ROLE_WORKFLOW_SMOKE_CHECKS.md` for the governing rules when HIRMOS claims local runtime behavior, user-environment verification, or role workflow readiness.

Required artifacts when applicable:

- `_hirmos/session/EVIDENCE.md` records local environment, service, migration, seed, dev-server, and route evidence.
- `_hirmos/session/EVIDENCE.md` records role-specific workflow smoke evidence for the relevant end-user, operator, privileged-user, and administrative paths.
- `_hirmos/session/EVIDENCE.md` reconciles whether the claim may be surfaced.

Firm rule: tests/build/lint alone do not prove local runtime readiness or role workflow readiness.


## Start checkpoint output

For the first implementation-readiness pause produced by `hirmos start`, use `_hirmos/core/templates/checkpoints/START_CHECKPOINT_OUTPUT.md`. This checkpoint is the user's opportunity to accept or change the session scope baseline, unresolved gated items, non-gating assumptions, and material technical-review items before implementation-unit artifacts are instantiated.
