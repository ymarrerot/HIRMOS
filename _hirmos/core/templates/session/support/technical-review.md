# Technical Review

Status: active-session Design and review-support artifact.
Purpose: provide reviewer-facing technical assumptions, risks, constraints, decisions, and inspection paths without overloading Domain Expert output.

## Review Context

- User Request:
- Design source:
- System-state source:
- Session Contract, if any:

## Technical Assumptions

| ID | Assumption | Source | Confidence | Impact | Review need |
|---|---|---|---|---|---|

## Technical Decisions

| ID | Decision | Alternatives considered | Rationale | Risk | Affected artifacts |
|---|---|---|---|---|---|

## Risks and Constraints

List architecture, security, data, integration, performance, migration, preservation, or operational risks.

## Third-Party Review Pointers

List the files/sections a technical reviewer should inspect.

## Challenge / Change Path

Explain how a reviewer or user can challenge, change, or request review of technical assumptions before Implementation proceeds.

## Items Not Requiring Domain Expert Input

List technical assumptions carried without immediate domain-owner decision and why they are not gated.

## Review Outcome

- Ready for implementation review? YES | NO
- Blockers:
- Follow-up required:


## Runtime Integration Review

List material technical integration assumptions and recommendations for reviewer inspection.

| Area | HIRMOS recommendation | Alternatives | Rationale | Review concern | Decision needed before production? |
|---|---|---|---|---|---:|

Technical review should challenge defaults when hosting, security, compliance, operations, cost, team preference, or future architecture make another option better.

## Autonomous Technical Decision Ledger

Use this section for technical choices HIRMOS made or recommends without interrupting Domain Expert mode.

| ID | Decision | Chosen default | Why HIRMOS could proceed without Domain Expert interruption | Alternatives | Visibility state | Evidence | Production-readiness impact | Review trigger |
|---|---|---|---|---|---|---|---|---|

Allowed visibility states:

```text
INTERNAL_RECORDED
SURFACED_TO_DOMAIN_EXPERT
TECHNICAL_REVIEW_REQUIRED
BLOCKED_NEEDS_USER_DECISION
NOT_APPLICABLE
```

Do not use this ledger to hide material choices. Surface a governed checkpoint when the choice affects domain behavior, risk, cost, compliance, ownership, implementation authorization, or production/readiness claims.

## Cross-Run Engineering Synthesis Ledger

Use this ledger when multiple candidate implementations, generated apps, OpenSpec outputs, prototypes, or prior self-runs are reviewed.

| Source | Engineering lesson | Adopt / reject / defer | Owning decision | Requirement / DU impact | Evidence / rationale |
|---|---|---|---|---|---|
| | architecture / adapter boundary / state machine / test strategy / package hygiene / maintainability | | | | |

Required checks:

- Preserve app-owned state and human/AI responsibility boundaries.
- Prefer centralized state-machine and approval-gate logic over scattered UI/API checks.
- Prefer adapter boundaries for external services and agents.
- Prefer meaningful smoke and state-transition tests over superficial existence checks.
- Record rejected candidate patterns when they conflict with accepted architecture.

Firm rule: candidate implementation quality is a design/technical signal, not a reason to bypass current HIRMOS authority, evidence, or accepted-state merge requirements.
