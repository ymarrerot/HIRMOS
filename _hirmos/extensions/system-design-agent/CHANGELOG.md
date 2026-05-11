# system-design-agent Changelog

## [1.1.0] - 2026-05-07

### Added
- Added the public default System Design entrypoint `system-design` backing `hirmos system-design`.
- Restored and narrowed `system-design-cycle` as a reusable system-level design subcycle that consumes Requirements outputs instead of producing Requirements artifacts.
- Made `phase-design-cycle` required for normal greenfield System Design completion after gated unresolved items are resolved.
- Added project-level unresolved-item contribution alignment using `_hirmos/artifacts/context/project/UNRESOLVED_ITEMS_INVENTORY.md` and related project-level unresolved-item governance artifacts.
- Added System Design hook seams for stage-appropriate unresolved-item contribution and final gating review.

### Changed
- Changed the default manifest `entry` from `system-design-cycle` to `system-design`.
- Moved Requirements ownership out of `system-design-agent`; the System Design step now consumes `requirements-agent` outputs such as `REQUIREMENTS_SOT.md`.
- Reframed old system-design cycle behavior as narrowed system-level design orchestration rather than the full Requirements + System Design lifecycle.
- Updated System Design unresolved-item handling to contribute to the project-level canonical unresolved-item inventory.
- Updated docs and artifact maps to reflect the front-door flow `Requirements → System Design → Implementation`.

### Removed
- Removed active Requirements producer ownership from `system-design-agent` for greenfield front-door operation.

## [1.0.0] - 2026-04-01

### Added
- Initial stable version baseline for `system-design-agent`.
- Public support for design workflows and authoritative design artifacts.
- system-design
- phase-design-cycle
- requirements-input-pack
- requirements-sot
- system-sot
- architecture-sot
- phases-sot
- phase-sot

### Changed
- Established extension-level versioning and core compatibility through `version` and `requires_core` in `extension.yaml`.


## Unreleased

- Added a canonical unresolved-item feed and historical ledger for `system-design`.
- Added a normalized unresolved-item contribution contract and extension hook for supporting/community contributions.
- Strengthened cycle completion so reconciliation runs from the feed and rejected invalid contributions remain visible.