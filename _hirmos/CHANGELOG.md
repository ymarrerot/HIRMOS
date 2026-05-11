# HIRMOS Changelog

This file is the concrete release history for the framework.

For the authoritative framework-wide versioning doctrine, see:
- [Versioning contract](./core/authority/framework/versioning-contract.md)

## [Unreleased]

No unreleased changes yet.

## [1.3.3] - 2026-05-11

### Changed

- Updated the `hirmos init` first-run summary so the primary next step is the productized HIRMOS workflow command path: `hirmos requirements`, `hirmos system-design`, and `hirmos implementation` inside the user's AI coding tool.
- Reframed the Core bootstrap prompt as fallback initialization for tools that do not automatically pick up the selected agent/tool integration files.

## [1.3.2] - 2026-05-11

### Added

- Added a non-blocking npm update notice to `hirmos init`. When a newer published HIRMOS CLI version is available, the CLI now shows an update hint without blocking initialization.

### Changed

- Updated CLI help and README guidance to document the update notice and the `HIRMOS_CLI_UPDATE_CHECK=0` escape hatch for disabling only the npm update check.

## [1.3.1] - 2026-05-11

### Added

- Added remote release install support to `hirmos init`: when `_hirmos/` is missing and `--source` is not provided, the CLI can download `hirmos-framework.zip` from the latest or a specific GitHub release using `--version`.
- Added `--offline` to disable remote download and fail clearly when `_hirmos/` is missing.
- Added release-download URL normalization and tests for latest and versioned GitHub release assets.

### Changed

- Updated public onboarding so the default install path is `npm install -g hirmos` followed by `hirmos init`.
- Updated README/getting-started/reference docs to say “HIRMOS framework release package” instead of “HIRMOS Core release package” now that the framework package includes the free starter workflow extensions.
- Removed public-facing “CLI v1” wording from README/getting-started/reference docs while preserving the distinction between terminal CLI commands and HIRMOS workflow commands.
- Updated release packaging to generate GitHub release-note helper output and SHA-256 checksum output in `ops/dist/`.

## [1.3.0] - 2026-05-10

### Added

- Added `_hirmos/project.json` as the project-level HIRMOS configuration file, replacing the previous stack-only config surface.
- Added manifest-declared HIRMOS workflow commands through `hirmos_commands` in runnable extension manifests.
- Added the DP-2 agent/IDE/tool integration registry, templates, managed-block rules, and generation examples under `_hirmos/integrations/agent-tools/`.
- Added contributor-facing agent/tool integration guidance and the `hirmos init` CLI design under `_hirmos/integrations/agent-tools/docs/`.
- Added the DP-3B TypeScript CLI implementation under `_hirmos/tools/cli/` with the `hirmos init` command.
- Added CLI tests for managed-block updates, `_hirmos/project.json` integration merging, shared-target integrations, invalid integration handling, and local source-folder/source-zip install behavior.
- Added DP-4 onboarding docs for the productized `hirmos init` path, including `Install and Initialize HIRMOS` in the regular-user getting-started lane.
- Added DP-5 and release-structure validation reports under `ops/release-reports/`.

### Changed

- Migrated the active public command surface from the pre-1.3.0 `cmd:` Core command protocol to `hirmos <command>[:entrypoint] [arguments]`.
- Updated Core command protocol, bootstrap, docs, and official extension manifests so workflow commands resolve through extension manifest declarations.
- Clarified that `hirmos init` is a terminal CLI command, while `hirmos requirements`, `hirmos system-design`, and `hirmos implementation` are HIRMOS workflow commands used inside the AI tool after Core bootstrap.
- Moved active stack selection from `_hirmos/STACK_CONFIG.json` into `_hirmos/project.json` under `stack.active_stack`.
- Classified `_hirmos/integrations/agent-tools/` as a HIRMOS productization/tool-discovery adapter surface, outside Core runtime behavior and outside extension behavior.
- Moved the product-facing TypeScript CLI source from root-level `packages/cli/` to `_hirmos/tools/cli/` so HIRMOS product tooling stays inside the single `_hirmos/` project install surface.
- Renamed `_hirmos/agent-integrations/` to `_hirmos/integrations/agent-tools/` to make integrations a broader HIRMOS concern while keeping the current agent/IDE/tool integration family explicit.
- Renamed ops scripts to match the current release model: `package-hirmos-framework.sh`, `package-other-extensions.sh`, and `update-public-repo.sh`. Kept `install-hirmos.sh` as an internal/local install helper rather than the public onboarding path.
- Renamed the generated install archive from `hirmos-core-framework.zip` to `hirmos-framework.zip` because the release package now includes the free regular-user workflow extensions.
- Bundled `requirements-agent`, `system-design-agent`, and `implementation-agent` into the HIRMOS framework release package as the free regular-user workflow.
- Packaging now writes the GitHub repo root `README.md` into packaged `_hirmos/README.md`, while the public repo can keep its lighter `_hirmos/README.md` for folder browsing.
- Updated public publishing so repo-root `AGENTS.md` is no longer copied; `AGENTS.md` is generated in target projects by `hirmos init` when requested.
- Updated packaging, install, public-repo update, and package-verification scripts to preserve the clean target-project shape: one `_hirmos/` folder and no root-level `packages/` folder.
- Updated the root README, docs hub, regular-user onboarding docs, methodology docs, and CLI README for the productized initialization path.
- Reframed the `2-methodology` documentation around durable orchestration and governed execution while preserving the practical HIRMOS tone and current AI-agent pain-point examples.
- Renamed methodology-level Pillar 2 from “Intermediate artifacts” to “Durable artifacts” and completed the terminology impact pass across the methodology and extension-authoring Beyond Clear Specs surfaces.
- Validated the developer-productization package state after DP-1 through DP-5, including CLI tests, stale-reference audits, package verification, and public-repo update verification.

### Removed

- Removed `_hirmos/STACK_CONFIG.json` from the active framework package after migrating its stack data into `_hirmos/project.json`.
- Removed active uses of the pre-1.3.0 `cmd:` command surface from live framework files. Historical and migration notes may still mention the old command forms explicitly.
- Removed repo-root `AGENTS.md` from `_private` and `_public`; it is now generated in target projects by `hirmos init` only when selected.
- Removed root-level `packages/` from the HIRMOS source/public project layout.

## [1.2.0] - 2026-05-08

### Added
- Added the official `requirements-agent` extension as the executable backing for the Requirements step in the public HIRMOS flow.
- Added methodology documentation for Orchestrated Spec-Driven Development under `/_hirmos/docs/2-methodology/`.
- Added the project-level unresolved-item context namespace at `/_hirmos/artifacts/context/project/`.
- Added the project-level canonical unresolved-item governance artifacts:
  - `UNRESOLVED_ITEMS_INVENTORY.md`
  - `UNRESOLVED_ITEMS_RECONCILIATION_WORKLIST.md`
  - `UNRESOLVED_ITEMS_FEED.md`
  - `UNRESOLVED_ITEMS_LEDGER.md`
- Added progressive-disclosure documentation lanes:
  - `/_hirmos/docs/1-use-hirmos/`
  - `/_hirmos/docs/2-methodology/`
  - `/_hirmos/docs/3-extend-contribute/`
  - `/_hirmos/docs/reference/`

### Changed
- Made the practical public front door executable as `Requirements → System Design → Implementation`.
- Changed the default public extension surfaces so the three primary workflow commands are:
  - `cmd: run extension requirements-agent`
  - `cmd: run extension system-design-agent`
  - `cmd: run extension implementation-agent`
- Refactored `system-design-agent` so the default System Design entrypoint composes the narrowed `system-design-cycle` and required `phase-design-cycle` for normal greenfield completion.
- Refactored `implementation-agent` so the default Implementation entrypoint composes planning and execution while preserving the required planning approval pause.
- Standardized unresolved-item governance around a single project-level canonical inventory instead of stage-scoped inventories.
- Updated `presentation-design` and `prototype-ingestion` hook/spec guidance so unresolved-item producers refresh their own artifact-scoped inventory sections inline before completion.
- Reorganized documentation around reader intent and progressive disclosure rather than exposing internal framework categories at the docs root.
- Updated the root `README.md` as the primary GitHub landing page for the story: Spec-Driven Development → Orchestrated Spec-Driven Development → HIRMOS.
- Clarified that the first-contact bootstrap remains the explicit instruction: `Read and follow the instructions on _hirmos/HIRMOS_CORE.md`.

### Fixed
- Removed the temporary `hirmos init` documentation because arbitrary LLM sessions cannot understand HIRMOS command syntax before loading HIRMOS Core.
- Removed stale docs paths after the documentation information-architecture restructure.
- Removed stage-scoped concrete `UNRESOLVED_ITEMS_*` paths from live framework documentation/spec surfaces.
- Removed old reliability-pattern terminology from active methodology surfaces after the Beyond Clear Specs migration.

### Notes
- Historical 1.2.0 note: framework-level CLI initialization was still future work at the time of this release. That gap is addressed by later DP-3B/DP-4 productization work, while the explicit bootstrap instruction remains the canonical fallback and Core authority-loading prompt.
- Extension manifests continue to use `requires_core: ">=1.0.0 <2.0.0"`, so existing official extensions remain compatible with Core 1.2.0.

## [1.1.0] - 2026-04-20

### Added
- Promoted `/_hirmos/core/bootstrap.md` to the assembled runtime bootstrap path.
- Added `/_hirmos/core/bootstrap_supporting-notes.md`.
- Added `/_hirmos/core/templates/BOOTSTRAP_REPORT_TEMPLATE.md`.
- Added `/_hirmos/core/templates/IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md`.
- Added `/_hirmos/core/templates/HOOK_EXECUTION_CONTROL_TEMPLATE.md`.
- Added `/_hirmos/core/authority/core/identity-display-execution-control.md`.
- Added `/_hirmos/core/authority/core/hook-execution-control.md`.
- Added `/_hirmos/core/authority/extensions/beyond-clear-specs.md`.
- Added `/_hirmos/docs/3-extend-contribute/extensions/beyond-clear-specs.md`.

### Changed
- Clarified bootstrap and execution-control artifact paths under `/_hirmos/artifacts/context/`.
- Replaced the terminal output wrapper template with `IDENTITY_DISPLAY_EXECUTION_CONTROL_TEMPLATE.md`.
- Renamed the hook execution template to `HOOK_EXECUTION_CONTROL_TEMPLATE.md`.
- Refactored the bootstrap completion flow around `/_hirmos/artifacts/context/core/bootstrap-report.md`.
- Renamed the reliability-pattern concept and file surfaces to **Beyond Clear Specs**.
- Merged framework governance doctrine into `framework-operating-model.md`.
- Merged framework and extension README-role doctrine into their broader document-role files.
- Merged runtime identity and run-result doctrine into `identity-display-execution-control.md`.
- Merged stack package doctrine into `stack-system.md`.

### Fixed
- Aligned bootstrap, report-template, and execution-control terminology after the runtime bootstrap redesign.
- Cleaned live framework references so active docs/specs point to the new bootstrap and authority surfaces.

### Removed
- Removed merged-away authority files after cross-framework reference cleanup.
- Removed older reliability-pattern docs and authority file surfaces after the Beyond Clear Specs standardization.

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
