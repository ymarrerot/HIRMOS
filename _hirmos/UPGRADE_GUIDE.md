# HIRMOS Version Guide

This file records version-level operational notes for the installed HIRMOS framework.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`.

## Current baseline — 1.2.5

HIRMOS 1.2.5 is the governed automated-testing/test-integrity and public-documentation-hygiene baseline. Terminal CLI 1.3.8 remains the current CLI because terminal CLI implementation did not change in this framework release.

For implementation-capable software work, HIRMOS now requires an explicit automated-testing posture. Material new or changed isolated deterministic logic should normally receive meaningful unit tests when practical; existing tests that still represent authoritative behavior must not be weakened merely to obtain PASS; and tests whose governing behavior legitimately changes or disappears should be updated or removed rather than retained as orphaned validation. Existing repository-native test conventions remain preferred, and HIRMOS does not impose a universal coverage percentage or a new default testing-report artifact family.

The 1.2.5 public documentation surface also removes maintainer project-plan identifiers and adds package/public-repository guards so those internal identifiers do not leak back into user-facing README, changelog, upgrade, methodology, or reference documentation.

For an existing HIRMOS project, update the terminal CLI first if needed, then update the project-local framework from an idle HIRMOS boundary:

```bash
npm install -g hirmos@latest
cd /your/project/path
hirmos update
```

If a governed session is active, finish and close it under the currently installed framework before upgrading. After a successful update, open a new AI-agent context so the upgraded bootstrap and generated integration surfaces are loaded.

The update replaces framework-owned surfaces but preserves the project's `_hirmos/system/`, `_hirmos/session/`, and `_hirmos/inputs/` directories exactly. `_hirmos/hirmos.config.json` is ownership-aware merged so incoming framework metadata/defaults can advance while project-local stack settings, integration selection, and unknown project fields remain intact. Recorded integrations are reconciled and regenerated from the new framework payload, the installed validator must pass, and a post-swap failure restores the previous framework and affected generated integration files.

`hirmos update --version X.Y.Z` pins a GitHub framework release. `--source` may use a local `_hirmos` folder, a folder containing `_hirmos`, or `hirmos-framework.zip`. Offline updates require an explicit local source. Normal updates reject semantic framework downgrades.

Maintainer `install-hirmos.sh --mode merge` follows the same ownership boundary for framework state/config: framework-owned surfaces are replaced, project-owned `system/`, `session/`, and `inputs/` are preserved exactly, and project-local configuration is ownership-aware merged.

## HIRMOS 1.2.4 baseline

HIRMOS 1.2.4 introduced the safe installed-framework update and state-preserving merge baseline together with terminal CLI 1.3.8, the first CLI version that provides the first-class `hirmos update` command. It established the idle-session update boundary, state-preserving framework transaction, ownership-aware config merge, integration reprojection, rollback behavior, and aligned maintainer merge-install semantics.

## CLI 1.3.8 state-preserving updater baseline

CLI 1.3.8 or newer is required to use `hirmos update`. Older installed projects do not need an intermediate framework migration: update the npm CLI first, then run `hirmos update` from an idle project boundary.

The framework and CLI versions remain independent release identities. HIRMOS framework 1.2.4 is paired with CLI 1.3.8 because both framework/package behavior and terminal CLI behavior changed in this release.

## HIRMOS 1.2.3 baseline

HIRMOS 1.2.3 is the bootstrap front-door simplification and authority-deduplication baseline.

It builds on 1.2.2 by returning `AGENTS.md` to a compact first-contact role while preserving HIRMOS identity, AI-agent orientation, current-working-copy authority, governance/pre-edit safety, per-context bootstrap discipline, command intent, and bootstrap-only boundaries.

Full bootstrap remains mandatory for advancing commands (`hirmos start`, `hirmos continue`, and `hirmos close`), while `hirmos status` retains its strictly read-only bootstrap fast path. The canonical bootstrap-report template is the sole report-structure authority, and stale historical hardening labels plus duplicated command/report-schema mechanics were removed from the two front-door files.

Bootstrap Steps 3–11, the required core reads, and the complete 16-question open-book quiz are intentionally unchanged. Any deeper removal of the current open-book repetition remains deferred until dedicated weak/strong-model validation proves it safe.

No terminal CLI package bump is required for 1.2.3; CLI 1.3.7 remains the projection-installer baseline because terminal CLI implementation did not change.

## HIRMOS 1.2.2 baseline

HIRMOS 1.2.2 is the carry-forward, implementation-convergence, and distribution-boundary hardening baseline.

It consolidates carry-forward lifecycle handling into the canonical carry-forward artifact, strengthens status/close concordance, and projects the updated carry-forward behavior through generated command and per-command skill surfaces.

Implementation converges through applicable validation, IU review, unresolved-item review, session implementation review, and the implementation-completion decision in the same authorized continuation when evidence is available. The planned IU-mode review pauses remain intact; an additional pre-close pause is conditional on real user-owned evidence or decisions, correction, or blockers. A bare `hirmos continue` after authorized work is already executed must infer the outstanding implementation-review / close-preparation boundary instead of resuming open-ended implementation.

The 1.2.2 line also hardens the distribution boundary: maintainer-only development instructions are kept out of shipping framework documentation, and package verification rejects maintainer-workspace path leakage before publication. The public-repository verifier remains an independent downstream guard.

No terminal CLI package bump was required for 1.2.2; CLI 1.3.7 remained the projection-installer baseline because terminal CLI implementation did not change.

## HIRMOS 1.2.1 baseline

HIRMOS 1.2.1 is the integration-projection, CLI-installer, and status-readiness hardening baseline.

It added canonical integration command capsules, generated per-command command surfaces, generated per-command `SKILL.md` packages where supported, and CLI installer support for emitting those projections from the project-local framework payload.

The generated projection model changed terminal `hirmos init` behavior: CLI 1.3.7 or newer is required to emit command projections and per-command skill packages from the project-local `_hirmos/` payload. CLI 1.3.4 can still write older always-on integration files but does not reliably install the newer command/skill projections.

HIRMOS 1.2.1 also clarified `hirmos status` as a read-only command with an explicit bootstrap fast path and minimum read set. `hirmos status` may report that bootstrap is incomplete without creating `BOOTSTRAP_REPORT.md`; advancing commands (`hirmos start`, `hirmos continue`, and `hirmos close`) still require bootstrap completion before execution.

The continuation hardening retained in the 1.2.x line strengthened behavior for real sessions: every `hirmos continue` is a governed pass recorded in `SESSION_LEDGER.md`, and `SESSION_SCOPE.md` is updated only for accepted authority deltas such as changed scope, IU objectives, acceptance criteria, validation requirements, unresolved-item disposition, or close-satisfaction criteria.

## HIRMOS 1.2.0 baseline

HIRMOS 1.2.0 is the post-dogfood simplification and onboarding-alignment baseline. It consolidated the compact runtime command surface into `_hirmos/core/commands/`, preserved the IU Planning → IU Execution boundary, reduced duplicated mutable delivery/phase status, strengthened derived delivery concordance and installed-project fixture isolation, hardened package/install hygiene, and refreshed onboarding documentation for first-time users.

## CLI 1.3.7 projection installer baseline

Use CLI package 1.3.7 or newer when installing HIRMOS 1.2.1+ framework packages that include generated command capsules and per-command skills. For local dogfooding, call the workspace CLI directly with `node tools/cli/dist/index.js init <project> --integration <id> --offline` after `_hirmos/` has been installed into the target project.

## HIRMOS 1.1.9 baseline

HIRMOS 1.1.9 is the token-efficient runtime boundary and derived-state stabilization baseline. It includes the runtime simplification wave: compact session ledger replacement, scope/IU authority separation, compressed bootstrap and ledger surfaces, pointer-oriented evidence/current-state/delivery/phase artifacts, restored IU planning versus IU execution pause, runtime-boundary fixtures, just-in-time optional artifact creation, and derived pointer-index support.

No terminal CLI version bump was required because terminal command behavior did not change.

## HIRMOS 1.1.7 baseline

HIRMOS 1.1.7 includes the canonical single interaction posture, interaction-mode config/CLI removal, extension/template realignment, context-resilient bootstrap discipline, general run preflight classification, follow-up command clarity, and delivery-shape honesty/cost-aware routing.

## HIRMOS 1.1.6 baseline

HIRMOS 1.1.6 includes sealed IU contract sections, append-only execution/review records, separated contract/execution/review status semantics, test/fixture/validator change rationale, delivery close concordance simplification, and evidence posture hardening for implementation/runtime/production claim separation.

## HIRMOS 1.1.5 baseline

HIRMOS 1.1.5 includes pre-execution ledger enforcement and generated review-gate validation. It materially changes validation behavior for generated project runs by failing IU-mode sessions where IU authority cannot be proven before material implementation, where IU authority artifacts appear to be retrofitted during close/archive cleanup, or where accepted phase/delivery artifacts lack concrete evidence-backed review-gate fields.

## HIRMOS 1.1.4 baseline

HIRMOS 1.1.4 includes generated-run IU enforcement and runtime artifact validator hardening. It materially changes validation behavior for generated project runs by failing IU-mode sessions that lack the required IU Set Authority Checkpoint, an implementation authorization decision, IU coverage mapping, or substantive IU files.

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
