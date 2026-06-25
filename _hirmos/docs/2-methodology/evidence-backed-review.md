# Evidence-Backed Review


HIRMOS evidence is not after-the-fact compliance paperwork. It is the governed proof trail for authorized work. Review must preserve whether the work was authorized before execution, whether evidence was collected contemporaneously or during correction, and whether any governance deviation occurred.

HIRMOS should not claim readiness, implementation completion, or close success without evidence.

Evidence-backed review means that claims are tied to artifacts, observed results, validation output, or explicit not-applicable rationale.

## Evidence categories

HIRMOS distinguishes:

- observed;
- inferred;
- assumed;
- unknown;
- blocked;
- not run;
- not applicable.

This distinction prevents uncertain claims from being presented as proven facts.

## Implementation evidence

When Implementation runs, HIRMOS should record:

- implementation unit plan;
- implementation unit artifact;
- files or artifacts changed;
- commands run or not run;
- validation results;
- local unit review;
- retry or escalation if needed;
- session implementation review.

## Snapshot-backed checkpoint rule

HIRMOS must not tell the user that an artifact exists, is ready, or can be inspected unless the artifact exists and contains non-placeholder content.

## Close evidence

Before close, HIRMOS must verify that accepted outcomes, unresolved carry-forward items, session history, and future-session readiness are recorded appropriately.

## close-time evidence materialization

HIRMOS close is an evidence-backed claim. Before normal close, required evidence owners must be materialized, not only mentioned in chat or carry-forward text.

Use the owning artifact for the evidence type:

- `EVIDENCE.md` claim reconciliation for material close, validation, runtime, implementation, integration, production-readiness, packaging, and accepted-state claims;
- `EVIDENCE.md` for local setup/runtime/user-environment claims;
- `EVIDENCE.md` for role/actor/workflow-readiness claims;
- `DESIGN.md` / `EVIDENCE.md` runtime posture for runtime provider/integration posture claims;
- `EVIDENCE.md` and `implementation-units/IU-xx.md` review for implementation evidence and completion decisions.

If the right artifact is missing, the truthful result is blocked or downgraded. Do not use another artifact as a substitute owner.

## PROD-L8.22 Review Gate Salvage

HIRMOS preserves legacy evidence-backed review discipline through existing artifacts instead of restoring legacy review files.

Review gates must answer:

- What authority was reviewed?
- What evidence was reviewed?
- Was the final codebase or file state inspected?
- Does the evidence prove unit, session, phase, delivery, runtime, or production claims?
- What remains unproven?
- Why is the terminal state honest?

A passing static check is not a delivery review. A completed implementation unit is not a phase review. A phase review is not a delivery review unless cross-phase behavior and delivery-level acceptance posture are reviewed.
