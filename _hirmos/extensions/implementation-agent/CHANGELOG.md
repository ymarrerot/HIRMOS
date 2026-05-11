# implementation-agent Changelog

## [1.1.0] - 2026-05-07

### Added
- Added the public default Implementation entrypoint `implementation` backing `hirmos implementation`.
- Added Implementation lifecycle composition over `implementation-planning-cycle` and `implementation-execution-cycle`.
- Added required planning approval pause before phase execution in the public Implementation flow.
- Added Evidence-backed Review terminology and terminal templates for the public Implementation step.

### Changed
- Changed the default manifest `entry` from `implementation-planning-cycle` to `implementation`.
- Reframed `implementation-planning-cycle` and `implementation-execution-cycle` as reusable internal/advanced subcycles under the public Implementation command.
- Updated docs and artifact maps to reflect the front-door flow `Requirements → System Design → Implementation`.

## [1.0.1] - 2026-04-15

### Changed
- Hardened `implementation-execution-cycle` so phase review is a built-in stage rather than a later handoff.
- Added template-driven terminal surfacing for completed, paused, and failed execution with remaining-gap disclosure inside completed output and a governed failed template.
- Added end-of-entrypoint self-validation for terminal template selection, review disclosure, repair-loop disclosure, and surfaced-output truthfulness.

### Added
- Entry-point-specific terminal templates under `templates/implementation-execution-cycle/`.
- Required phase review artifact template for implementation execution.

- implementation-planning-cycle now uses entrypoint-specific completed and paused terminal templates with strict final self-validation.

## [1.0.0] - 2026-04-01

### Added
- Initial stable version baseline for `implementation-agent`.
- Public support for implementation planning, bounded implementation execution, local review, and retry/escalation behavior.
- implementation-planning-cycle
- prompt-planning
- agent-prompt
- implementation-execution-cycle

### Changed
- Established extension-level versioning and core compatibility through `version` and `requires_core` in `extension.yaml`.
