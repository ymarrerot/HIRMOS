# HIRMOS Changelog

This changelog records user-visible changes to the HIRMOS framework payload.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`. This file explains what changed; it is not the machine-readable version source.

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

- No breaking framework migration is required from 1.0.0 to 1.0.1.
- Existing projects may continue using their current `_hirmos/` payload, or install 1.0.1 when they want the updated documentation and release metadata.
- CLI npm package updates are managed separately from the framework version; use `npm install -g hirmos@latest` to update the terminal CLI.

## 1.0.0 — Initial public baseline

### Added

- Introduced HIRMOS as an orchestration framework for AI-assisted software development.
- Added the current-state-first lifecycle: User Request → Understand System State → Design → Implementation → Update System State.
- Added the workflow command set used inside AI coding tools: `hirmos start`, `hirmos status`, `hirmos continue`, and `hirmos close`.
- Added the contract-centered session artifact spine: `SESSION_CONTRACT.md`, `SESSION_EXECUTION.md`, `REQUIREMENTS_BASELINE.md`, `DESIGN.md`, `unresolved-items.md`, `session-contract-review.md`, and `implementation-units/IU-xx.md`.
- Added durable accepted-state artifacts under `_hirmos/system/accepted-state/`.
- Added delivery and phase lifecycle support for large or multi-session work.
- Added canonical extension/capability routing through extension manifests, extension default entrypoints, capability manifests, and capability default entrypoints.
- Added public onboarding documentation organized into `1-use-hirmos`, `2-methodology`, `3-extend-contribute`, and `reference` lanes.
- Added AI-tool integration templates and registry under `_hirmos/integrations/agent-tools`.

### Notes

- This is the initial public HIRMOS baseline.
- Terminal CLI scope is limited to installation/bootstrap concerns. The terminal CLI command is `hirmos init`; workflow commands are used inside the AI-tool conversation.
- Framework versioning is tracked in `_hirmos/hirmos.config.json`; HIRMOS does not use a separate `_hirmos/VERSION` file.
