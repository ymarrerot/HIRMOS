# HIRMOS Changelog

This changelog records user-visible changes to the HIRMOS framework payload.

The framework version source of truth is `_hirmos/hirmos.config.json` under `framework.version`. This file explains what changed; it is not the machine-readable version source.

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
