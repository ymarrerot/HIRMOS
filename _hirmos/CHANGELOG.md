# HIRMOS Changelog

This file is the concrete release history for the framework.

For the authoritative framework-wide versioning doctrine, see:
- [Versioning contract](./core/authority/framework/versioning-contract.md)

## [1.1.0] - 2026-04-20

### Added
- Promoted `/_hirmos/core/bootstrap.md` to the assembled runtime bootstrap path.
- Added `/_hirmos/core/bootstrap_supporting-notes.md`.
- Added `/_hirmos/core/templates/BOOTSTRAP_REPORT_TEMPLATE.md`.
- Added `/_hirmos/core/templates/IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md`.
- Added `/_hirmos/core/templates/HOOK_EXECUTION_CONTROL_TEMPLATE.md`.
- Added `/_hirmos/core/authority/core/identity-display-execution-control.md`.
- Added `/_hirmos/core/authority/core/hook-execution-control.md`.
- Added `/_hirmos/core/authority/extensions/beyond-clear-instructions.md`.
- Added `/_hirmos/docs/extensions/beyond-clear-instructions.md`.

### Changed
- Clarified bootstrap and execution-control artifact paths under `/_hirmos/artifacts/context/`.
- Replaced the terminal output wrapper template with `IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md`.
- Renamed the hook execution template to `HOOK_EXECUTION_CONTROL_TEMPLATE.md`.
- Refactored the bootstrap completion flow around `/_hirmos/artifacts/context/core/bootstrap-report.md`.
- Renamed the "Clear Instructions Are Not Enough" concept and file surfaces to **Beyond Clear Instructions**.
- Merged framework governance doctrine into `framework-operating-model.md`.
- Merged framework and extension README-role doctrine into their broader document-role files.
- Merged runtime identity and run-result doctrine into `identity-display-execution-control.md`.
- Merged stack package doctrine into `stack-system.md`.

### Fixed
- Aligned bootstrap, report-template, and execution-control terminology after the runtime bootstrap redesign.
- Cleaned live framework references so active docs/specs point to the new bootstrap and authority surfaces.

### Removed
- Removed merged-away authority files after cross-framework reference cleanup.
- Removed the old docs and authority files named `clear-instructions-are-not-enough.md`.

## [1.0.0] - 2026-04-01

### Added
- Framework-level versioning through `_hirmos/VERSION`.
- Framework release history through [_hirmos/CHANGELOG.md](./CHANGELOG.md).
- Framework upgrade guidance through [_hirmos/UPGRADE_GUIDE.md](./UPGRADE_GUIDE.md).
- Extension-level versioning through `version` in each `extension.yaml`.
- Extension/core compatibility through `requires_core` in each `extension.yaml`.
- Extension-level `CHANGELOG.md` and `UPGRADE_GUIDE.md` files for installed extensions.

### Changed
- Established the initial stable versioning and compatibility contract for HIRMOS.
- Standardized the framework around the `system-design-agent` and `implementation-agent` architecture.

### Fixed
- N/A

### Removed
- Extension-manifest `spec_version` from the public Hirmos extension contract.
