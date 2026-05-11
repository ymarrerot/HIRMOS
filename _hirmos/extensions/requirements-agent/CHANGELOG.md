# requirements-agent Changelog

## [1.0.0] - 2026-05-07

### Added
- Initial stable version baseline for `requirements-agent`.
- Public support for the HIRMOS Requirements step in the front-door flow:
  - `Requirements → System Design → Implementation`.
- Default public command backing:
  - `hirmos requirements`.
- Public Requirements lifecycle entrypoint:
  - `requirements`.
- Requirements producer entrypoints:
  - `requirements-input-pack`.
  - `requirements-sot`.
- Requirements input contract covering:
  - current prompt/session context;
  - optional command argument tail;
  - online-service attachments;
  - `_hirmos/inputs/requirements-agent/requirements/` runtime input folder;
  - bounded local file or repository-context references;
  - hook-derived artifacts.
- Requirements-owned production of `REQUIREMENTS_SOT.md`.
- Requirements input pack production under the requirements-agent runtime context.
- Requirements-stage hooks for input discovery, requirements normalization, unresolved-item contribution, and final gating review.
- Inline producer contribution obligations for project-level unresolved-item governance.
- Requirements terminal/completion templates.

### Changed
- Requirements ownership moved out of `system-design-agent` into `requirements-agent` for the greenfield HIRMOS front-door flow.
- Requirements unresolved-item contributions now use the project-level canonical unresolved-item inventory pattern.

### Notes
- Runtime input folders are not shipped inside the extension package. Core/entrypoint execution creates missing runtime folders during init or first run according to the HIRMOS command protocol.
