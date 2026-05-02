# ENGINEERING STACK STANDARDS

## Purpose

These standards define engineering expectations for the `generic` stack package.

They complement framework-wide engineering standards and are intentionally conservative.

## Standards

### 1. Respect Existing Conventions

Prefer the repository's established:

- naming patterns
- folder structure
- test patterns
- dependency management style
- coding style

Do not introduce a new local convention unless the task requires it.

### 2. Favor Small, Verifiable Changes

When stack uncertainty is high, smaller changes are safer than broad rewrites.

Prefer changes that are:

- easy to review
- easy to verify
- easy to revert
- low risk to unrelated system areas

### 3. Avoid Assumption-Heavy Refactoring

Do not perform broad architecture refactors based on guessed stack norms.

If the repository structure is unclear, preserve local patterns and document uncertainty.

### 4. Prefer Existing Tooling

Use existing repository tooling when present.

Examples include:

- make targets
- package scripts
- task runners
- test runners
- local helper scripts

### 5. Surface Uncertainty Explicitly

When stack-specific correctness cannot be fully verified, say so in the run outputs.

Explicit uncertainty is better than fake confidence.
