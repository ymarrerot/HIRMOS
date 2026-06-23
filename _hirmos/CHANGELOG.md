# HIRMOS Changelog

This changelog records user-visible changes to the HIRMOS framework payload.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`. This file explains what changed; it is not the machine-readable version source.

## Unreleased

### Changed

- Aligned documentation, examples, and CLI/release payload guidance with the PROD-L scope-authority model: `SESSION_SCOPE.md`, top-level `DELIVERY_PLAN.md`, per-delivery `DELIVERY_SCOPE.md`, and history-level `ARCHIVE_MANIFEST.md`.
- Clarified that CLI package versioning is independent from framework payload documentation/template changes when terminal CLI behavior is unchanged.

## 1.0.3 — Production-shaped doctrine, delivery shape, and artifact simplification

### Added

- Added a core production-shaped implementation doctrine: governed implementation should aim for production-shaped software by default unless the Session Scope explicitly authorizes a prototype, demo, fixture, or local-only result.
- Added a Production-Shaped Engineering Gate before implementation readiness and at close.
- Added production-shaped Design obligations for material engineering areas such as persistence, background jobs, usage/quotas, provider APIs, file storage, secrets/configuration, and critical-flow evidence.
- Added concrete Next.js TypeScript engineering standards for local PostgreSQL preference, long-running job architecture, usage/quota safety, provider boundaries, upload/storage hygiene, environment hygiene, and evidence expectations.
- Added explicit smallest-sufficient delivery-shape decision logic for greenfield, brownfield, and mixed work.
- Added the strict-necessity session artifact rule: separate artifacts are justified only for authority, machine state, evidence, gating, continuity, or audit/history.
- Added a required near-top `Current Continuation Snapshot` section in `SESSION_EXECUTION.md` for cross-chat continuation.

### Changed

- Strengthened core lifecycle, command, runtime-integration, and stack protocols so production-shaped implementation is a core HIRMOS posture, not only stack-level advice.
- Updated Design and Implementation entrypoints to reject unapproved demo/local shortcuts as neutral implementation choices.
- Changed delivery-shape selection so HIRMOS prefers the smallest sufficient governed delivery shape instead of treating broad work as automatically multi-session.
- Consolidated former session support-artifact responsibilities into major artifacts: `SESSION_SCOPE.md`, `DESIGN.md`, `EVIDENCE.md`, `SESSION_EXECUTION.md`, and implementation units.
- Consolidated checkpoint continuation into `SESSION_EXECUTION.md` and removed the separate checkpoint artifact/folder model.
- Removed the session `support/` directory model and moved conditional machine-readable stack routing to root `stack-resolution.json`.
- Minimized `SESSION_STATE.json` so it owns only machine-readable command and lifecycle state, while `SESSION_EXECUTION.md` owns human-readable continuation.
- Improved artifact quality rules around `SESSION_SCOPE.md`, `DESIGN.md`, `SESSION_EXECUTION.md`, unresolved-item detail, and stale support-artifact regressions.

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
- Added the contract-centered session artifact spine: `SESSION_SCOPE.md`, `SESSION_EXECUTION.md`, `REQUIREMENTS.md`, `DESIGN.md`, `unresolved-items.md`, `SESSION_SCOPE.md` close verification, and `implementation-units/IU-xx.md`.
- Added durable accepted-state artifacts under `_hirmos/system/accepted-state/`.
- Added delivery and phase lifecycle support for large or multi-session work.
- Added canonical extension/capability routing through extension manifests, extension default entrypoints, capability manifests, and capability default entrypoints.
- Added public onboarding documentation organized into `1-use-hirmos`, `2-methodology`, `3-extend-contribute`, and `reference` lanes.
- Added AI-tool integration templates and registry under `_hirmos/integrations/agent-tools`.

### Notes

- This is the initial public HIRMOS baseline.
- Terminal CLI scope is limited to installation/bootstrap concerns. The terminal CLI command is `hirmos init`; workflow commands are used inside the AI-tool conversation.
- Framework versioning is tracked in `_hirmos/hirmos.config.json`; HIRMOS does not use a separate `_hirmos/VERSION` file.
