# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`.

## Current baseline — 1.2.0

HIRMOS 1.2.0 is the post-dogfood simplification and onboarding-alignment baseline.

It builds on 1.1.9 by consolidating the compact runtime command surface into `_hirmos/core/commands/`, preserving the IU Planning → IU Execution boundary that proved effective in real dogfood, reducing duplicated mutable delivery/phase status, strengthening derived delivery concordance and installed-project fixture isolation, hardening package/install hygiene, and refreshing onboarding documentation for first-time users.

No terminal CLI version bump is required because terminal CLI behavior did not change. The CLI package remains 1.3.4.

## HIRMOS 1.1.9 baseline

HIRMOS 1.1.9 is the token-efficient runtime boundary and derived-state stabilization baseline. It includes the L8.32C–L simplification wave: compact session ledger replacement, scope/IU authority separation, compressed bootstrap and ledger surfaces, pointer-oriented evidence/current-state/delivery/phase artifacts, restored IU planning versus IU execution pause, runtime-boundary fixtures, just-in-time optional artifact creation, and derived pointer-index support.

No terminal CLI version bump was required because terminal command behavior did not change.

## HIRMOS 1.1.7 baseline

HIRMOS 1.1.7 includes the canonical single interaction posture, interaction-mode config/CLI removal, extension/template realignment, context-resilient bootstrap discipline, general run preflight classification, follow-up command clarity, and delivery-shape honesty/cost-aware routing.

## HIRMOS 1.1.6 baseline

HIRMOS 1.1.6 includes sealed IU contract sections, append-only execution/review records, separated contract/execution/review status semantics, test/fixture/validator change rationale, delivery close concordance simplification, and evidence posture hardening for implementation/runtime/production claim separation.

## HIRMOS 1.1.5 baseline

HIRMOS 1.1.5 includes pre-execution ledger enforcement and generated review-gate validation. It materially changes validation behavior for generated project runs by failing IU-mode sessions where IU authority cannot be proven before material implementation, where IU authority artifacts appear to be retrofitted during close/archive cleanup, or where accepted phase/delivery artifacts lack concrete evidence-backed review-gate fields.

## HIRMOS 1.1.4 baseline

HIRMOS 1.1.4 includes generated-run IU enforcement and runtime artifact validator hardening. It materially changes validation behavior for generated project runs by failing IU-mode sessions that lack the L8.21 IU Set Authority Checkpoint, an implementation authorization decision, IU coverage mapping, or substantive IU files.

## HIRMOS 1.1.3 baseline

HIRMOS 1.1.3 includes IU Set Authority Checkpoints, minimum IU content standards, phase/delivery evidence-backed review gates, close-time concordance sweeps, and stricter evidence semantics separating implementation acceptance from runtime and production verification.

## HIRMOS 1.1.2 baseline

HIRMOS 1.1.2 is the governance posture and pre-execution authority stabilization baseline. It builds on the 1.1.1 current-state-first source-reading baseline by clarifying that HIRMOS is active governance authority, not after-the-fact compliance paperwork, and by strengthening idle command legality, implementation-unit timing, correction-ledger concordance, and close-time chronology/freshness guidance.

## HIRMOS 1.1.1 baseline

HIRMOS 1.1.1 is the current-state-first source reading, runtime freshness, and complexity-pressure stabilization baseline. It builds on the 1.1.0 accepted-state navigation model by strengthening how HIRMOS follows source artifacts during Understand System State and how runtime artifacts stay fresh after governed transitions.

## Operational posture retained across versions

HIRMOS must be treated as active governance, not an after-the-fact compliance layer. The model is the executor inside HIRMOS governance. Material implementation, correction, evidence, close, or accepted-state work requires valid command state and active authority before acting.

If work occurs outside valid authority, HIRMOS must record a governance deviation/correction and reconcile it before readiness, completion, or close claims.

## CLI package

The CLI package version remains unchanged when the framework content changes but terminal command behavior does not change.

## Framework package

Release packaging must ship only canonical runtime surfaces, templates, docs, validators, and examples. Framework files must remain project-agnostic except for clearly labeled examples.
