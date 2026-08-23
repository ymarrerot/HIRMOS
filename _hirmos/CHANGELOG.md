# Changelog

## PROD-L8.33G — Carry-Forward Lifecycle Consolidation and Projected Command Updates

- Consolidated active and resolved carry-forward lifecycle inside `CARRY_FORWARD.md`; no new carry-forward command or resolution artifact was added.
- Added global carry-forward IDs using `CF-YYYYMMDD-NNN` plus separate source refs for close-time local IDs.
- Added accepted-state maintenance classification for carry-forward resolution using existing `hirmos start` / `hirmos continue` / `hirmos close`.
- Strengthened `hirmos status` to report carry-forward concordance conflicts read-only.
- Strengthened `hirmos close` with a required Carry-Forward Attention block and future resolution instruction.
- Projected the updated behavior through generated integration command/skill capsules.


## 1.2.1 — Integration projection, CLI installer, and status-readiness hardening

- Bumps framework metadata and validator expected version from 1.2.0 to 1.2.1.
- Adds canonical integration command capsules for `hirmos start`, `hirmos continue`, `hirmos status`, and `hirmos close`.
- Extends the integration registry so supported tools can receive generated always-on files, explicit command files, and per-command `SKILL.md` packages from the same capsule source.
- Preserves per-command skills only; HIRMOS does not generate one broad default `hirmos/SKILL.md`.
- Adds CLI/package installer support so terminal `hirmos init --integration <tool>` emits generated command projections and per-command skills from the project-local framework payload.
- Bumps the terminal CLI package baseline to 1.3.7 because integration projection install behavior changed and the public 1.3.6 package did not provide the required generated command/skill projection behavior.
- Reinforces `hirmos start` as a non-implementation boundary and `hirmos continue` as a classify-and-gate-before-coding command.
- Preserves the IU Planning → IU Execution boundary: IU mode still requires IU plan review plus `IU_EXECUTION_AUTHORIZED` before material edits.
- Adds a `hirmos status` read-only bootstrap fast path: status may report bootstrap gaps without creating `BOOTSTRAP_REPORT.md`, while advancing commands remain blocked until bootstrap passes.
- Defines explicit minimum read sets for idle/post-close status, active-session status, and delivery/phase escalation reads.
- Adds projection, installer, and status fast-path validator/static/package coverage while preserving project-agnostic framework language.

## 1.2.0 — Post-dogfood simplification, command-surface unification, and onboarding alignment

- Bumps framework metadata and validator expected version to 1.2.0.
- Packages the post-1.1.9 hardening wave after real dogfood: shared capability control deduplication, installer integration-copy hotfix, delivery completion concordance simplification, installed-project fixture isolation, residual status hygiene, and command-surface unification.
- Makes `_hirmos/core/commands/` the single compact runtime command authority and removes the separate `_hirmos/core/runtime/` packet layer.
- Preserves the successful IU Planning → governed pause → IU Execution boundary, active generated-artifact validation, rich governed checkpoint outputs, JIT optional artifact creation, and derived pointer/concordance posture.
- Simplifies duplicated mutable delivery/phase status by deriving completion and roadmap posture from source artifacts instead of asking the model to maintain multiple narrative status mirrors.
- Aligns onboarding documentation around the four onboarding principles, refreshes the first-real-run tutorial with clear example-project credit, simplifies the root README for first-time visitors, and separates the GitHub `_hirmos/README.md` folder guide from the packaged installed-project onboarding README.
- Keeps CLI package version at 1.3.4 because terminal CLI command behavior did not change.
- Adds PROD-L8.32X continue-pass delta hardening: every `hirmos continue` must be classified as a governed pass, recorded in `SESSION_LEDGER.md`, reconciled with `SESSION_STATE.json.continuation_pass`, and reflected in `SESSION_SCOPE.md` only when accepted authority changes.
- Adds PROD-L8.32Y governance-first methodology documentation reframe: README and methodology docs now lead with permanent governed-execution requirements before current AI-agent reliability context.

## 1.1.9 — Token-efficient runtime boundary and derived-state stabilization

- Bumped framework metadata and validator expected version to 1.1.9.
- Consolidates the L8.32C–L simplification wave: `SESSION_EXECUTION.md` was replaced by compact `SESSION_LEDGER.md`, `SESSION_SCOPE.md` now carries compact IU planning pointers only, bootstrap/session ledger/evidence/current-state/delivery/phase artifacts were compressed, and normal command execution now starts from compact command files.
- Restores the explicit IU Planning → governed pause → IU Execution boundary: accepting a session baseline in IU mode authorizes IU planning/materialization only; material project-file edits require separate `IU_EXECUTION_AUTHORIZED` after IU plan review.
- Adds focused runtime-boundary fixtures proving material edits and lifecycle transition claims fail before `IU_EXECUTION_AUTHORIZED`.
- Adds just-in-time artifact creation and derived pointer-index support so optional artifacts are not pre-created as empty future synchronization obligations and pointer indexes are treated as derived navigation caches, not independent truth.
- Adds derived command-state cache metadata to `SESSION_STATE.json`; `allowed_next_commands` and `recommended_next_command` remain compatibility fields but are not independent authority.
- Preserves CLI package version 1.3.4 because terminal CLI behavior did not change.

## 1.1.7 — Single interaction posture and context-resilient routing stabilization

- Bumped framework metadata and validator expected version to 1.1.7.
- Replaced configurable interaction modes with one canonical HIRMOS interaction posture: simple by default, transparent by design, rigorous underneath, and progressive in disclosure.
- Removed legacy configurable interaction-posture config/CLI support, preserving concise domain-owner-facing behavior as the sole user-facing posture through core authority and templates.
- Realigned extension and checkpoint templates so governed claims surface concise artifact paths while detailed rigor remains in artifacts and validators.
- Added context-resilient bootstrap discipline: every session bootstrap report must include complete compact discipline answers written again from durable current artifacts, archived project history, or core protocols, not chat memory or prior bootstrap answers.
- Added general run preflight classification (`PRECHECK_PASS`, `PRECHECK_WARNING`, `PRECHECK_BLOCKER`) and clearer follow-up `hirmos start` command guidance when no active session exists.
- Added delivery-shape honesty and cost-aware routing guidance so selected delivery shape is justified by real software scope, risk, evidence, continuity, and user/token cost—not testing context.
- No terminal CLI version bump; CLI package remains 1.3.4.

## 1.1.6 — Sealed IU contracts and delivery close evidence-posture stabilization

- Bumped framework metadata and validator expected version to 1.1.6.
- Introduces sealed IU contract sections with prominent LLM Write Permission lines so IU authority remains immutable after contract seal unless route-back occurs.
- Separates contract, execution, review, retry, and handoff status semantics so implementation completion no longer requires mutating sealed IU authority.
- Adds append-only execution/review record expectations for IU-mode sessions, including explicit test/fixture/validator change rationale when validation assets are modified.
- Simplifies delivery close concordance by making DELIVERY_SCOPE.md a compact close-posture and source-pointer authority instead of a duplicated evidence ledger.
- Hardens evidence posture so implementation acceptance, local runtime evidence, and production verification remain separate claims, preventing broad runtime/production overclaims when E2E evidence is NOT_RUN, BLOCKED, or absent.
- Strengthens delivery unresolved-register reconciliation, current-state navigation posture, archived session-state normalization, and close-time contradiction checks.
- No terminal CLI version bump; CLI package remains 1.3.4.

## 1.1.5 — Pre-execution ledger and generated review-gate stabilization

- Bumped framework metadata and validator expected version to 1.1.5.
- Stabilizes pre-execution ledger enforcement introduced after 1.1.4.
- Generated IU-mode sessions must now show a pre-material-edit ledger row before material implementation start, plus an IU Set Authority Checkpoint, authorization decision, and explicit non-retrospective posture.
- Validator now rejects retrospective IU authority/compliance patterns such as adding checkpoints or expanding archived IU files during close solely to satisfy validation.
- Generated accepted/closed/partial phases and delivery closes must instantiate concrete evidence-backed review-gate fields, including codebase review, evidence levels, honest result rationale, and non-claims.
- Hardens delivery-scope close concordance, current-state source-index placeholder detection, and broad runtime/provider/production claim checks.
- No terminal CLI version bump; CLI package remains 1.3.4.

## 1.1.4 — Generated-run IU enforcement stabilization

- Bumped framework metadata and validator expected version to 1.1.4.
- Stabilizes generated-run IU enforcement introduced after 1.1.3.
- Validator now protects generated session archives for IU Set Authority Checkpoints, implementation authorization decisions, IU coverage maps, and substantive IU files when IU mode is active.
- Runtime artifact validation also checks timestamp completeness, stale accepted phase exit criteria, delivery status-log completeness, and source-index placeholder cleanup.
- No terminal CLI version bump; CLI package remains 1.3.4.


# HIRMOS Changelog

This changelog records user-visible changes to the HIRMOS framework payload.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`. This file explains what changed; it is not the machine-readable version source.

## Unreleased

### PROD-L8.32Z — Start command non-implementation boundary

- Strengthened `hirmos start` as a non-implementation command: detailed implementation instructions are scope input, not implementation authorization.
- Added a baseline acceptance pre-edit gate across command surfaces, session templates, and all current AI-tool integration templates.
- Preserved the existing IU Planning → IU Execution boundary: baseline acceptance authorizes IU planning only when IU mode applies; material edits still require `IU_EXECUTION_AUTHORIZED`.
- Added validator/fixture coverage for start-time material edits before baseline acceptance and integration-template pre-edit gate propagation.


## 1.1.3 — IU authority and evidence-backed review stabilization

- Added IU Set Authority Checkpoint expectations so implementation-unit mode proves IU files, coverage, non-placeholder review, sequencing, and authorization before material code changes.
- Defined a minimum substantive IU contract for IU-mode work, preventing thin implementation units from acting as execution authority.
- Hardened close-time concordance for phase body sections, delivery-plan pointer sections, current-state source index placeholders, carry-forward active-only invariants, and timestamp completeness.
- Strengthened evidence semantics so implementation acceptance, runtime verification, and production verification remain distinct claims.
- Salvaged legacy evidence-backed review discipline into existing session, phase, and delivery review gates without reintroducing legacy artifact sprawl.
- Preserved HIRMOS governance posture that the framework is active authority, not after-the-fact compliance paperwork.
- CLI package version remains 1.3.4 because terminal install behavior did not change.

## 1.1.2 — Governance posture and pre-execution authority stabilization

- Hardened HIRMOS governance posture so the framework is presented as active execution authority, not after-the-fact compliance paperwork.
- Clarified model role: the model executes inside HIRMOS governance and must not implement first, then reconstruct implementation units, evidence, or ledger rows afterward.
- Hardened idle `hirmos continue` command legality so idle continuations fail closed or route to governed start/correction flow before project-file changes.
- Strengthened implementation-unit pre-execution authority: when IU mode is active, IU artifacts must exist before material code changes begin; retrospective IU creation is a governance deviation/correction.
- Strengthened correction ledger concordance so material correction commands are recorded as distinct command-level passes rather than collapsed summaries.
- Hardened close-time concordance guidance for timestamp chronology, delivery-plan freshness, and later carry-forward resolution evidence.
- Preserved current-state-first source reading discipline, protocol ownership, validator minimality, capability taxonomy, and source-authority matrix from the 1.1.1 baseline.
- CLI package version remains 1.3.4 because terminal install behavior did not change.

## 1.1.1 — Current-state source reading and complexity-pressure stabilization

### Changed

- Hardened Understand System State guidance so HIRMOS reads `CURRENT_SYSTEM_STATE.md` first, follows active governance pointers, and reads materially relevant source artifacts before design or implementation.
- Added runtime freshness guidance so `SESSION_STATE.json`, `SESSION_LEDGER.md`, `PHASE-xx.md`, `SESSION_SCOPE.md`, `EVIDENCE.md`, and active accepted-state pointers must be reconciled after governed transitions and implementation passes.
- Clarified implementation-unit timing: when implementation-unit mode is active, `IU-xx.md` files are instantiated after session-baseline acceptance and before material code changes begin.
- Hardened gated continue semantics so unresolved gated items cannot be silently accepted by bare `hirmos continue` unless the surfaced recommendation is explicitly adopted, the item is resolved, or it is reclassified/deferred under governed rules.
- Added evidence claim reconciliation guidance so historical failures and current pass/fail claims cannot remain contradictory.
- Removed default `DECISION_LOG.md` from accepted-state support surfaces; decision logging is now conditional on explicit decision-log governance.
- Added protocol ownership and validator minimality guidance to reduce overlap and discourage brittle exact-wording validators when authority-safety or structural/status checks are sufficient.
- Added capability-family taxonomy and source-authority matrix clarifying that capability IDs are stable dispatch identifiers and that requirements/design/scope authority should live at the narrowest safe source level.

### Validation

- Revalidated private/public framework payloads, validator fixtures, CLI tests, package generation, package verification, and independence checks for the 1.1.1 framework package.

## 1.1.0 — Accepted-state navigation authority and source-artifact traceability

### Changed

- Reframed `CURRENT_SYSTEM_STATE.md` as the accepted-state navigation authority with current governance pointers, Work History Ledger, Source Artifact Index, and concise source-linked summaries.
- Removed default root accepted-state `REQUIREMENTS.md`; detailed requirements remain in delivery/session/archive source artifacts unless explicit cumulative requirements governance is activated.
- Updated close/start/continue/status guidance so accepted-state updates are index-first: current pointers, ledger row, source artifact index, concise summary when material, and next navigation.
- Added validator and regression coverage to fail default root accepted-state requirements/design/scope artifacts unless explicit governance activation metadata is present.

## 1.0.9 — Phase-baseline concordance and current-state-first delivery review stabilization

### Changed

- Aligned phase entry-gate templates and validator expectations by requiring scalar `Entry criteria status` evidence, with tables treated as supplementary evidence instead of the only authority signal.
- Hardened post-continue ledger freshness so `SESSION_LEDGER.md` reflects completed phase-baseline and session-scope routing after `PHASE-xx.md` and `SESSION_SCOPE.md` exist.
- Clarified delivery plan freshness after phase instantiation so active phase pointers must not remain `none` once a phase is active.
- Added status-aware delivery-baseline wording so pre-acceptance deliveries are described as Candidate Delivery, Proposed Delivery, or Delivery Under Baseline Review instead of Active Delivery.
- Clarified that generated artifacts should explain delivery/session/phase routing from current-state evidence, scope, governance need, validation risk, continuity need, and artifact authority.
- Reduced generated-artifact encouragement to use greenfield/brownfield labels as primary routing reasons; project-type labels remain supporting evidence metadata or phase-control routing metadata when useful.
- Added validator and regression coverage for phase entry-gate concordance, post-continue ledger freshness, delivery-plan current phase freshness, and pre-acceptance delivery wording conflicts.

## 1.0.8 — Delivery-baseline optional authority location and dogfood stabilization

### Changed

- Hardened `delivery_baseline` focus so optional requirements and design authority are created only under `_hirmos/system/delivery/<delivery-id>/` when justified.
- Clarified that session-local `REQUIREMENTS.md` and `DESIGN.md` are not valid during delivery-baseline focus because no bounded phase/session authority exists yet.
- Updated validators and regression fixtures so delivery-baseline runs fail when session-local optional authority artifacts are created and pass when justified optional authority lives under the delivery folder.
- Completed final dogfood-readiness stabilization for the focus-aware delivery/session boundary model.

## 1.0.7 — Delivery-baseline session-surface minimality and dogfood stabilization

### Changed

- Hardened `delivery_baseline` focus so the active session remains a runtime envelope while delivery-level authority stays under `_hirmos/system/delivery/<delivery-id>/`.
- Clarified that delivery-baseline work must use `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` as the active delivery authority and unresolved register.
- Tightened command, routing, checkpoint, and execution-ledger guidance so session-level `SESSION_SCOPE.md` and `unresolved-items.md` are not created before phase/session baseline authority exists.
- Updated validators and regression expectations to preserve the delivery/session boundary before delivery-baseline acceptance.
- Completed final dogfood-readiness stabilization for the focus-aware delivery/session model.

## 1.0.6 — Focus-aware delivery baseline and multi-session authority hardening

### Added

- Added the focus-aware runtime session model, including `session_focus`, `active_authority`, delivery pointer, and phase pointer fields in `SESSION_STATE.json`.
- Added delivery-baseline and phase/session-baseline capability surfaces without introducing a separate delivery-agent extension.
- Added delivery-level optional authority templates for `_hirmos/system/delivery/<delivery-id>/REQUIREMENTS.md`, `_hirmos/system/delivery/<delivery-id>/DESIGN.md`, and `_hirmos/system/delivery/<delivery-id>/unresolved-items.md`.
- Added governed checkpoint templates for delivery-baseline and session-baseline review.
- Added focus-aware documentation and examples for delivery-baseline and phase/session workflows.
- Added an example showing durable delivery baseline review before phase/session authority and implementation-unit artifacts are instantiated.

### Changed

- Clarified that HIRMOS always runs inside a governed runtime session envelope, but artifacts are activated only when the selected focus requires them.
- Clarified that `SESSION_SCOPE.md` is required only when the active work has a bounded phase/session work scope.
- Clarified that durable delivery work first enters `delivery_baseline` focus and uses `DELIVERY_SCOPE.md` as the active authority before phase/session authority is instantiated.
- Clarified that `DELIVERY_SCOPE.md` must include a complete phase coverage plan before delivery-baseline approval, while future `PHASE-xx.md` files are created just in time by default.
- Rewired command and capability-routing guidance so delivery-baseline acceptance transitions to phase/session baseline preparation instead of direct implementation.
- Hardened validators and regression fixtures for focus-aware delivery/session artifact rules.
- Generalized remaining framework-facing preservation wording from brownfield-specific language to existing-system preservation language.

## 1.0.5 — Dogfood-ready start checkpoint and authority hardening

### Added

- Added a governed start checkpoint output for `hirmos start`: `Recommended Baseline — Review or Change`.
- Added explicit first-review behavior so users can accept, change, mark uncertain, request technical review, or stop before implementation begins.
- Added machine-readable `SESSION_STATE.json.run_context` as the canonical runtime timestamp source for session artifacts.

### Changed

- Delayed full implementation-unit artifact creation until after the session scope baseline is accepted or amended.
- Hardened `unresolved-items.md` as the canonical register for gated items, non-gating assumptions, technical-review items, blockers, and material uncertainties.
- Clarified that `SESSION_SCOPE.md` remains the complete active session authority and close-verification root, while optional `REQUIREMENTS.md` and `DESIGN.md` are subordinate detail authorities only when explicitly adopted.
- Tightened responsibility boundaries for `REQUIREMENTS.md`, `DESIGN.md`, `SESSION_LEDGER.md`, implementation-unit records, delivery scopes, and phase scopes.
- Consolidated runtime timestamp context into `SESSION_STATE.json` and kept timestamp capture evidence in `BOOTSTRAP_REPORT.md`.
- Restricted project-agnostic marker checks to shipped framework surfaces so generated project artifacts may mention project-specific names and features.
- Removed residual scope-authority wording that used legacy contract/baseline terminology in shipped framework surfaces.

### Removed

- Removed the separate `RUN_CONTEXT.json` template; runtime context now lives in `SESSION_STATE.json.run_context`.

## 1.0.4 — Scope authority simplification and delivery navigation hardening

### Added

- Added the scope-centered authority model as the canonical first-version model: `SESSION_SCOPE.md`, top-level `DELIVERY_PLAN.md`, per-delivery `DELIVERY_SCOPE.md`, phase files, and history-level `ARCHIVE_MANIFEST.md`.
- Added explicit delivery navigation fields for `Last accepted delivery`, `Next recommended delivery`, and `Next recommended delivery scope`.
- Added project-type-neutral multi-session delivery guidance: durable multi-session delivery applies when justified by governance need, regardless of whether the project is greenfield, brownfield, or mixed.

### Changed

- Made `SESSION_SCOPE.md` the active session authority and constrained `SESSION_LEDGER.md` to a compact continuation handoff and append-only command/control ledger.
- Changed `DELIVERY_PLAN.md` into a durable roadmap/register that is updated or appended when future deliveries are planned, rather than overwritten.
- Made `DELIVERY_SCOPE.md` the default combined authority for a durable delivery or release.
- Renamed canonical independent requirements authority to `REQUIREMENTS.md` and kept `REQUIREMENTS.md` / `DESIGN.md` conditional rather than default implementation-session artifacts.
- Aligned documentation, examples, validators, regression fixtures, accepted-state surfaces, archive surfaces, command routing guidance, and release payload guidance with the scope-authority model.
- Generalized framework-facing language so shipped framework files remain project-agnostic except for clearly labeled examples.
- Clarified that CLI package versioning is independent from framework payload documentation/template changes when terminal CLI behavior is unchanged.

### Removed

- Removed shipped support for legacy scope-authority surfaces and replaced them with the canonical scope-authority model.
- Removed legacy per-delivery `DELIVERY_PLAN.md` authority guidance in favor of top-level roadmap/register plus per-delivery `DELIVERY_SCOPE.md`.
- Removed migration/compatibility framing from shipped framework guidance so 1.0.4 presents the simplified model as canonical.

## 1.0.3 — Production-shaped doctrine, delivery shape, and artifact simplification

### Added

- Added a core production-shaped implementation doctrine: governed implementation should aim for production-shaped software by default unless the Session Scope explicitly authorizes a prototype, demo, fixture, or local-only result.
- Added a Production-Shaped Engineering Gate before implementation readiness and at close.
- Added production-shaped Design obligations for material engineering areas such as persistence, background jobs, usage/quotas, provider APIs, file storage, secrets/configuration, and critical-flow evidence.
- Added concrete Next.js TypeScript engineering standards for local PostgreSQL preference, long-running job architecture, usage/quota safety, provider boundaries, upload/storage hygiene, environment hygiene, and evidence expectations.
- Added explicit smallest-sufficient delivery-shape decision logic for greenfield, brownfield, and mixed work.
- Added the strict-necessity session artifact rule: separate artifacts are justified only for authority, machine state, evidence, gating, continuity, or audit/history.
- Added a required near-top `Current Continuation Snapshot` section in `SESSION_LEDGER.md` for cross-chat continuation.

### Changed

- Strengthened core lifecycle, command, runtime-integration, and stack protocols so production-shaped implementation is a core HIRMOS posture, not only stack-level advice.
- Updated Design and Implementation entrypoints to reject unapproved demo/local shortcuts as neutral implementation choices.
- Changed delivery-shape selection so HIRMOS prefers the smallest sufficient governed delivery shape instead of treating broad work as automatically multi-session.
- Consolidated former session support-artifact responsibilities into major artifacts: `SESSION_SCOPE.md`, `DESIGN.md`, `EVIDENCE.md`, `SESSION_LEDGER.md`, and implementation units.
- Consolidated checkpoint continuation into `SESSION_LEDGER.md` and removed the separate checkpoint artifact/folder model.
- Removed the session `support/` directory model and moved conditional machine-readable stack routing to root `stack-resolution.json`.
- Minimized `SESSION_STATE.json` so it owns only machine-readable command and lifecycle state, while `SESSION_LEDGER.md` owns human-readable continuation.
- Improved artifact quality rules around `SESSION_SCOPE.md`, `DESIGN.md`, `SESSION_LEDGER.md`, unresolved-item detail, and stale support-artifact regressions.

### Removed

- Removed the separate `checkpoints/` artifact model.
- Removed the separate `support/` directory model.
- Removed obsolete `SESSION_STATE.json` fields that duplicated human-readable continuation context.

### Upgrade notes

- Active sessions created under an older artifact model may be finished with their current model or restarted under 1.0.3 if the simplified session surface is preferred.
- Future implementation-capable sessions should expect stronger production-shape checks before implementation authorization and close acceptance.
- New sessions should not create `support/`, `checkpoints/`, or legacy support files such as request intake, source materials, technical review, implementation readiness, local runtime evidence, role workflow smoke, claim reconciliation, close checklist, archive manifest, or session-scope review as separate artifacts. Their responsibilities now live in the major artifacts. If stack routing needs machine-readable state, use root `stack-resolution.json`.

## 1.0.2 — Lifecycle and CLI reference documentation alignment

### Added

- Added a dedicated CLI reference at `_hirmos/docs/reference/cli-reference.md` as the complete public guide for installing, checking, updating, and using the `hirmos` terminal CLI.
- Added a dedicated framework command reference at `_hirmos/docs/reference/framework-command-reference.md` for AI-tool workflow commands such as `hirmos start`, `hirmos status`, `hirmos continue`, and `hirmos close`.

### Changed

- Standardized public lifecycle wording to `User Request → Understand System State → Design → Implementation → Update System State` across public README and documentation surfaces.
- Updated CLI mentions in public getting-started and reference docs to point users to the dedicated CLI reference for complete usage.
- Updated generated GitHub release notes to include the recommended `cd /your/project/path` install flow and a pointer to the CLI reference.
- Cleaned public README branding so the logo acts as the primary HIRMOS heading without a duplicate `# HIRMOS` title.

### Removed

- Removed stale public lifecycle wording variants such as `Design the Work`, `Implement with Evidence`, and `Update Current State`.
- Removed CLI usage details from the framework command reference so terminal CLI usage and AI-tool framework commands are documented separately.

## 1.0.1 — CLI publishing and release-note automation

### Added

- Added public-facing CLI install, version-check, and update instructions across the README and getting-started documentation.
- Added documentation for the split release model: HIRMOS framework versions align with GitHub framework release tags, while the `hirmos` npm CLI package may use a different npm version because npm package history cannot be reset.
- Added generated GitHub release notes support that derives the framework version and release-specific change summary from this changelog.

### Changed

- Standardized public lifecycle wording to `User Request → Understand System State → Design → Implementation → Update System State` across README and public documentation surfaces.
- Clarified that `hirmos init` installs the latest GitHub framework release by default, while `hirmos init --version X.Y.Z` installs the matching GitHub framework release tag `vX.Y.Z`.
- Updated release packaging guidance so users install from `hirmos-framework.zip`, not GitHub-generated source archives.

### Fixed

- Ignored local CLI dependency and packaging artifacts such as `tools/cli/node_modules/`, npm tarballs, logs, coverage output, and TypeScript build-info files.

### Upgrade notes

- Existing projects may continue using their current `_hirmos/` payload, or install 1.0.1 when they want the updated documentation and release metadata.
- CLI npm package updates are managed separately from the framework version; use `npm install -g hirmos@latest` to update the terminal CLI.

## 1.0.0 — Initial public baseline

### Added

- Introduced HIRMOS as an orchestration framework for AI-assisted software development.
- Added the current-state-first lifecycle: User Request → Understand System State → Design → Implementation → Update System State.
- Added the workflow command set used inside AI coding tools: `hirmos start`, `hirmos status`, `hirmos continue`, and `hirmos close`.
- Added the contract-centered session artifact spine: `SESSION_SCOPE.md`, `SESSION_LEDGER.md`, `REQUIREMENTS.md`, `DESIGN.md`, `unresolved-items.md`, `SESSION_SCOPE.md` close verification, and `implementation-units/IU-xx.md`.
- Added durable accepted-state artifacts under `_hirmos/system/accepted-state/`.
- Added delivery and phase lifecycle support for large or multi-session work.
- Added canonical extension/capability routing through extension manifests, extension default entrypoints, capability manifests, and capability default entrypoints.
- Added public onboarding documentation organized into `1-use-hirmos`, `2-methodology`, `3-extend-contribute`, and `reference` lanes.
- Added AI-tool integration templates and registry under `_hirmos/integrations/agent-tools`.

### Notes

- This is the initial public HIRMOS baseline.
- Terminal CLI scope is limited to installation/bootstrap concerns. The terminal CLI command is `hirmos init`; workflow commands are used inside the AI-tool conversation.
- Framework versioning is tracked in `_hirmos/hirmos.config.json`; HIRMOS does not use a separate `_hirmos/VERSION` file.

## Unreleased — PROD-L8.15

- Hardened current-state-first source reading discipline: `CURRENT_SYSTEM_STATE.md` is mandatory first read, followed by scoped reads of active and materially relevant source artifacts.
- Added runtime freshness expectations for session ledger, phase lifecycle, session scope previews, evidence reconciliation, and active current-state pointers.
- Hardened gated unresolved item continue semantics so pending user input cannot be silently accepted by bare `hirmos continue`.
- Made `DECISION_LOG.md` conditional rather than a default accepted-state root artifact; `CARRY_FORWARD.md` remains active-only support.
- Added reuse-first complexity-control doctrine before adding new governance surfaces.

## PROD-L8.19 command legality / IU authority / correction ledger hardening

- Hardened idle-state `hirmos continue` semantics: no direct project-file mutation while no active governed session exists.
- Hardened IU pre-execution authority: when IU mode is active, IU artifacts must exist before material code changes; retrospective IU creation is a governance deviation unless lightweight/no-IU mode was declared before edits.
- Hardened correction-ledger expectations so material correction commands are recorded individually in `SESSION_LEDGER.md`.
- Hardened close-time chronology, delivery-plan freshness, and later carry-forward resolution concordance.

## PROD-L8.21 IU set authority and close-time concordance hardening

- Added an IU Set Authority Checkpoint in `SESSION_LEDGER.md` to prove IU authority before material edits.
- Added minimum IU content requirements so thin stubs cannot authorize implementation in IU mode.
- Added close-time concordance sweeps for phase files, delivery plan pointers, current-state source indexes, carry-forward invariants, and evidence semantics.
- Clarified evidence levels: implementation accepted, runtime verified, and production verified.

## PROD-L8.22 phase and delivery review gate hardening

- Added evidence-backed session, phase, and delivery review gate discipline using existing artifacts.
- Required review gates to distinguish implementation accepted, runtime verified, and production verified claims.
- Added actual-codebase-reviewed expectations for implementation review boundaries.
- Hardened close so higher-level acceptance cannot overclaim beyond the evidence level proven.
## PROD-L8.23 — Generated-Run IU Enforcement and Runtime Artifact Validator Hardening

- Added generated-run validation for IU-mode sessions, not just static framework templates.
- Validator now fails generated sessions with IU files but no IU Set Authority Checkpoint, no authorization decision, no IU Set Coverage Map, or no proof that IU files existed before material edits.
- Validator now fails thin generated IU files below the minimum IU contract standard.
- Added runtime checks for archived SESSION_STATE timestamp/run-context completeness, accepted phase stale binary-exit criteria, delivery status-log phase close coverage, and blank source-index placeholders.
- Added regression cases for missing IU checkpoints, thin generated IUs, and null archived session timestamps.



## PROD-L8.24 — Pre-Execution Ledger Enforcement and Generated Review Gate Validation
- Requires generated IU-mode sessions to record a Pre-Material-Edit Ledger Row before material implementation begins.
- Rejects retrospective IU checkpoint / IU expansion during close as clean governance.
- Validates generated phase and delivery review gates for concrete evidence-backed acceptance fields.
- Hardens delivery-scope, source-index, and scoped runtime/provider claim concordance checks.
