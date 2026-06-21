# Installation and Packaging Protocol

Status: core protocol.

## Purpose

Define how HIRMOS is packaged, installed, and validated as a self-contained project-local framework folder.

## Package shape

The release package must contain one archive root and one installed framework folder:

```text
hirmos-framework/_hirmos/
```

The package must not place HIRMOS runtime authority at the target project root.

## Included surfaces

A release package must include these `_hirmos/` surfaces when present:

- `AGENTS.md`
- `README.md`
- `hirmos.config.json`
- `core/`
- `docs/`
- `extensions/`
- `stacks/`
- `tools/`
- `inputs/`
- `session/`
- `system/`

## Excluded surfaces

A release package must not include development-only workspace material, temporary implementation scripts, development report packages, obsolete runtime-authority paths, transcript/self-review diagnostic requirements, obsolete runtime machinery or legacy output-hash machinery.

## Runtime preservation on install

Installers must preserve existing target-project runtime state by default:

- `_hirmos/system/`
- `_hirmos/session/`
- `_hirmos/inputs/`

A fresh install may remove `_hirmos/` only when explicitly requested.

## Packaging verification

Packaging verification must check:

- package contains `_hirmos/AGENTS.md`
- package contains `_hirmos/core/bootstrap.md`
- package contains `_hirmos/hirmos.config.json`
- package contains bundled extensions and stack packages
- package excludes development-only paths and obsolete runtime-authority paths
- packaged `_hirmos/tools/validate.py` passes after extraction

## Relationship to validation

Packaging checks do not replace framework validation. They verify that the installed payload shape is clean and self-contained.

## Accepted-state installation surface

The installed `_hirmos/` framework includes `_hirmos/system/accepted-state/` and `_hirmos/system/history/sessions/` scaffolding. These folders are runtime state surfaces, not development-only reports.

Packaging must preserve this structure while excluding development-only work files.

## Clean self-run and review package rule

When HIRMOS prepares or evaluates a self-run, review, or handoff package, the package must exclude local/generated/noisy material unless the user explicitly asks for it and the package labels it as local evidence.

Default excluded items:

```text
.env
.env.*
!.env.example
.DS_Store
__MACOSX/
node_modules/
.next/
dist/
build/
coverage/
.cache/
.turbo/
.git/
```

Secrets may be represented through redacted evidence records, not by shipping live local secret files.

Clean-package claim rule: HIRMOS must not claim a package is clean or suitable for review if excluded items are present and unacknowledged.

## Package cleanliness evidence gate

Package cleanliness evidence preserves the package exclusion rules and makes clean-package claims evidence-backed.

When a package, review package, self-run package, or downloadable handoff is produced, HIRMOS must record package-cleanliness evidence before claiming the package is clean, reviewable, or suitable for handoff.

Minimum package-cleanliness evidence:

- package root path;
- package filename;
- explicit exclusion check for `.env`, `.env.*` except `.env.example`, `.DS_Store`, `__MACOSX/`, `node_modules/`, `.next/`, `.git/`, generated runtime folders, and live secret files;
- any intentionally included local evidence files and their label/rationale;
- whether secret values are absent, redacted, placeholder-only, or intentionally included by explicit user request;
- final package-cleanliness claim status recorded in `EVIDENCE.md` claim reconciliation when package cleanliness is surfaced.

A package may include generated application source when that source is the product being handed off, but it must not silently include local machine state, live secrets, dependency folders, build cache, or operating-system metadata.

Firm rule: a package link is a material package claim. If cleanliness was not checked, do not say the package is clean; record `NOT_RUN` or `CLAIMED_NOT_LOGGED`.

## Cross-run handoff/package synthesis

When comparing outputs from multiple tools or agents, package quality must be evaluated separately from product feature coverage.

A candidate with strong UI or broad implementation may still be weak as a handoff baseline if it includes local machine state, live secrets, dependency folders, build caches, generated platform metadata, or unclear setup instructions.

Cross-run package lessons must route to:

- package-cleanliness evidence for handoff claims;
- setup instructions and `.env.example` expectations;
- carry-forward items when a baseline is usable but not safely package-clean;
- `EVIDENCE.md` claim reconciliation when package cleanliness or reproducibility is surfaced.

Firm rule: do not select a baseline solely on product coverage when its package/handoff state would make local continuation unsafe, unreproducible, or confusing.
