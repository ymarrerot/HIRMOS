# Upgrade Guide

## 1.1.9 stabilization note

HIRMOS 1.1.9 is the token-efficient runtime boundary and derived-state stabilization baseline. It includes the L8.32C–L simplification wave: compact session ledger replacement, scope/IU authority separation, compressed bootstrap and ledger surfaces, pointer-oriented evidence/current-state/delivery/phase artifacts, command-first runtime guidance, restored IU planning versus IU execution pause, runtime-boundary fixtures, just-in-time optional artifact creation, and derived pointer-index support. No terminal CLI version bump is required because terminal command behavior did not change.

## HIRMOS 1.1.6 baseline

HIRMOS 1.1.6 is the sealed IU contract and delivery close evidence-posture stabilization baseline. It builds on 1.1.5 by separating immutable IU contract authority from append-only execution/review records, adding LLM Write Permission lines to implementation-unit sections, requiring rationale when tests/fixtures/validators are modified, simplifying delivery close concordance into compact posture/source-pointer summaries, and hardening evidence claims so implementation acceptance, local runtime verification, and production verification remain distinct. No terminal CLI version bump is required because terminal install behavior did not change.

## HIRMOS 1.1.5 baseline

HIRMOS 1.1.5 is the pre-execution ledger and generated review-gate stabilization baseline. It builds on 1.1.4 by making IU pre-execution authority observable in the active ledger, rejecting retrospective IU authority or validator-compliance cleanup, and validating concrete phase/delivery evidence-backed review gates in generated project runs. It also strengthens delivery-scope close concordance, source-index placeholder detection, and broad runtime/provider/production claim checks.

## HIRMOS 1.1.4 baseline

HIRMOS 1.1.4 is the generated-run IU enforcement stabilization baseline. It builds on 1.1.3 by validating generated session archives, not only framework templates, for IU Set Authority Checkpoints, implementation authorization, IU coverage mapping, minimum IU substance, timestamp completeness, stale accepted-phase exit criteria, delivery status-log completeness, and source-index placeholder cleanup.


# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

## Current baseline


## PROD-L8.20 governance posture note

HIRMOS must be treated as active governance, not an after-the-fact compliance layer. The model is the executor inside HIRMOS governance. Material implementation, correction, evidence, close, or accepted-state work requires valid command state and active authority before acting.

If work occurs outside valid authority, HIRMOS must record a governance deviation/correction and reconcile it before readiness, completion, or close claims.


## HIRMOS 1.1.3 baseline

HIRMOS 1.1.3 is the IU authority and evidence-backed review stabilization baseline. It builds on the 1.1.2 governance-posture baseline by requiring IU Set Authority Checkpoints before material edits when IU mode is active, enforcing substantive IU contracts, strengthening close-time concordance, and distinguishing implementation acceptance from runtime and production verification.

## HIRMOS 1.1.2 baseline

HIRMOS 1.1.2 is the governance posture and pre-execution authority stabilization baseline. It builds on the 1.1.1 current-state-first source-reading baseline by clarifying that HIRMOS is active governance authority, not after-the-fact compliance paperwork, and by strengthening idle command legality, implementation-unit timing, correction-ledger concordance, and close-time chronology/freshness guidance.

## HIRMOS 1.1.1 baseline

HIRMOS 1.1.1 is the current-state-first source reading, runtime freshness, and complexity-pressure stabilization baseline. It builds on the 1.1.0 accepted-state navigation model by strengthening how HIRMOS follows source artifacts during Understand System State and how runtime artifacts stay fresh after governed transitions.

HIRMOS uses the scope-centered authority model:

```text
_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md
_hirmos/session/SESSION_SCOPE.md
_hirmos/system/delivery/DELIVERY_PLAN.md
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/unresolved-items.md
_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

`CURRENT_SYSTEM_STATE.md` is the accepted-state navigation authority and the mandatory first read for current-state-first work. It owns the current governance context, accepted-state navigation and latest close metadata, concise accepted-state summary, Work History Ledger, Source Artifact Index, active delivery/phase/session pointers, and next governed navigation. It does not replace delivery/session scope, requirements, design, unresolved-item, implementation-unit, evidence, or archive artifacts as source authorities.

During Understand System State, HIRMOS must read `CURRENT_SYSTEM_STATE.md` first, follow active-governance pointers, and read materially relevant canonical source artifacts before material design or implementation. Reading depth is scoped/progressive; HIRMOS should not perform a blind exhaustive history scan for every small request, but it must not design from summaries alone when source authority is available.

Detailed requirements, design, and scope remain where they originate:

```text
_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md   # optional
_hirmos/system/delivery/<delivery-id>/DESIGN.md         # optional
_hirmos/session/SESSION_SCOPE.md
_hirmos/session/REQUIREMENTS.md                         # optional
_hirmos/session/DESIGN.md                               # optional
_hirmos/system/history/sessions/<session-id>/...         # archived source
```

Default HIRMOS does not create root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md`. Default HIRMOS also does not create `DECISION_LOG.md`; decision logging is conditional on explicit decision-log governance. If a project explicitly activates cumulative accepted-state requirements governance, that activation must be documented before such a root artifact is valid.

At close, HIRMOS updates accepted state using an index-first model: current governance context, Work History Ledger, Source Artifact Index, concise accepted-state summary only when materially changed, and next recommended navigation. It must not merge delivery/session requirements into root accepted-state requirements by default. Active navigation pointers may be updated during governed transitions, but accepted-state summaries and historical outcome rows are finalized through close/update-state discipline.

During `delivery_baseline` focus, HIRMOS uses the delivery scope and delivery unresolved register as the active authority surfaces and must not create session-level `SESSION_SCOPE.md`, session-level `unresolved-items.md`, session-level `REQUIREMENTS.md`, or session-level `DESIGN.md` by default. Those session-level artifacts are created only when the flow advances to a bounded phase/session baseline and the selected focus justifies them.

During `phase_session_baseline` focus, HIRMOS must keep phase/session authority and ledgers fresh: the active `PHASE-xx.md` must include scalar `Entry criteria status`, `SESSION_SCOPE.md` must exist before session-baseline review, `SESSION_LEDGER.md` must mark completed routing work as completed, and `DELIVERY_PLAN.md` must point to the active phase after phase instantiation.

When implementation-unit mode is active, implementation-unit files must be instantiated after session-baseline acceptance and before material code changes begin. Retrospective implementation-unit creation requires explicit correction/reconciliation. Runtime mirrors such as `SESSION_LEDGER.md`, `PHASE-xx.md`, `SESSION_SCOPE.md`, and `EVIDENCE.md` must be reconciled after implementation starts or completes so stale lower sections do not contradict current machine state.

Generated artifacts should explain routing from current system state, scope size, governance need, validation risk, continuity need, and artifact-authority boundaries. Project-type labels such as greenfield, brownfield, or mixed may remain useful evidence metadata, but they must not become the primary routing justification.

Capability IDs are stable dispatch identifiers, not user-facing workflow names. HIRMOS should reuse existing capability families where possible and place requirements/design/scope authority at the narrowest safe source level. Validators should protect authority safety, freshness, and structural/status concordance; exact wording checks should be avoided unless wording affects authority safety.

## CLI package

The CLI package version remains unchanged when the framework content changes but terminal command behavior does not change.

## Framework package

Release packaging must ship only canonical runtime surfaces, templates, docs, validators, and examples. Framework files must remain project-agnostic except for clearly labeled examples.



## 1.1.7 stabilization note

HIRMOS 1.1.7 includes the canonical single interaction posture, interaction-mode config/CLI removal, extension/template realignment, context-resilient bootstrap discipline, general run preflight classification, follow-up command clarity, and delivery-shape honesty/cost-aware routing. No terminal CLI version bump is required because terminal command behavior did not change.


## 1.1.6 stabilization note

HIRMOS 1.1.6 includes sealed IU contract sections, append-only execution/review records, separated contract/execution/review status semantics, test/fixture/validator change rationale, delivery close concordance simplification, and evidence posture hardening for implementation/runtime/production claim separation. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.5 stabilization note

HIRMOS 1.1.5 includes pre-execution ledger enforcement and generated review-gate validation. It materially changes validation behavior for generated project runs by failing IU-mode sessions where IU authority cannot be proven before material implementation, where IU authority artifacts appear to be retrofitted during close/archive cleanup, or where accepted phase/delivery artifacts lack concrete evidence-backed review-gate fields. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.4 stabilization note

HIRMOS 1.1.4 includes generated-run IU enforcement and runtime artifact validator hardening. It materially changes validation behavior for generated project runs by failing IU-mode sessions that lack the L8.21 IU Set Authority Checkpoint, an implementation authorization decision, IU coverage mapping, or substantive IU files. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.3 stabilization note

HIRMOS 1.1.3 includes IU Set Authority Checkpoints, minimum IU content standards, phase/delivery evidence-backed review gates, close-time concordance sweeps, and stricter evidence semantics separating implementation acceptance from runtime and production verification. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.2 stabilization note

HIRMOS 1.1.2 includes governance-posture clarity, idle `hirmos continue` fail-closed behavior, implementation-unit pre-execution authority, correction-command ledger concordance, timestamp chronology guidance, delivery-plan close-time freshness, and carry-forward resolution concordance. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.1 stabilization note

HIRMOS 1.1.1 includes current-state-first source reading discipline, runtime freshness guidance, implementation-unit timing hardening, gated continue semantics, evidence claim reconciliation, accepted-state support minimality, protocol ownership guidance, validator minimality classes, capability taxonomy, and source-authority matrix stabilization. No terminal CLI version bump is required because terminal install behavior did not change.

## 1.1.0 stabilization note

HIRMOS 1.1.0 includes accepted-state navigation authority, source-artifact traceability, removal of default root accepted-state requirements, index-first close guidance, validator concordance, and final dogfood-readiness stabilization. No terminal CLI version bump is required because terminal install behavior did not change.

## PROD-L8.15 current-state source reading and freshness

Framework users should treat `CURRENT_SYSTEM_STATE.md` as the first read and navigation authority, then follow active and materially relevant source artifact pointers before design or implementation. Existing projects with a default `_hirmos/system/accepted-state/DECISION_LOG.md` may remove it unless explicit decision-log governance is active.

## PROD-L8.19 command legality / IU authority / correction ledger hardening

- Hardened idle-state `hirmos continue` semantics: no direct project-file mutation while no active governed session exists.
- Hardened IU pre-execution authority: when IU mode is active, IU artifacts must exist before material code changes; retrospective IU creation is a governance deviation unless lightweight/no-IU mode was declared before edits.
- Hardened correction-ledger expectations so material correction commands are recorded individually in `SESSION_LEDGER.md`.
- Hardened close-time chronology, delivery-plan freshness, and later carry-forward resolution concordance.

## PROD-L8.21 IU set authority and close-time concordance hardening

If IU mode is active, create substantive IU files and record the IU Set Authority Checkpoint before material code changes. Close must reconcile phase, delivery, current-state, carry-forward, and evidence semantics before success claims.

## PROD-L8.22 Review Gate Hardening

Review and close flows now require explicit session/phase/delivery review gate discipline. Existing projects should preserve final-result honesty by recording what was reviewed, what evidence was available, whether the actual codebase was reviewed, and what runtime or production claims are not made.
## PROD-L8.23 Generated-Run Validation Upgrade Note

HIRMOS now validates generated runtime artifacts more aggressively. Existing generated runs may fail if IU-mode sessions lack a `PROD-L8.21 IU Set Authority Checkpoint`, an explicit authorization decision, an IU Set Coverage Map, substantive IU files, or complete archived session timestamps. This is intentional: framework-template compliance is no longer enough to prove generated-run governance.



## PROD-L8.24 — Pre-Execution Ledger Enforcement and Generated Review Gate Validation
- Requires generated IU-mode sessions to record a Pre-Material-Edit Ledger Row before material implementation begins.
- Rejects retrospective IU checkpoint / IU expansion during close as clean governance.
- Validates generated phase and delivery review gates for concrete evidence-backed acceptance fields.
- Hardens delivery-scope, source-index, and scoped runtime/provider claim concordance checks.
