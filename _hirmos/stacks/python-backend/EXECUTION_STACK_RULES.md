# EXECUTION STACK RULES

## Purpose

These rules define stack-specific execution behavior for projects using the `python-backend` stack package.

These rules complement framework core governance and execution-facing agent rules. They do not replace them.

## Core Behavior

When using this package, the executor should assume a Python-centric backend workflow while still respecting repository-local evidence.

The executor should:

- preserve import/module/package structure
- avoid framework-specific assumptions unless repository evidence supports them
- prefer existing dependency and environment workflows
- preserve backend-oriented separation of concerns

## Environment Discipline

The executor should respect the repository's environment model where evident, such as:

- virtual environments
- dependency lock workflows
- project-local task runners
- package or application entry points

The executor should not casually mix dependency management approaches.

## Validation Discipline

When relevant and available, the executor should prefer:

- formatting or lint checks
- type checks when the repository supports them
- tests
- application or module-level smoke validation

## Implementation Discipline

The executor should:

- preserve clear module boundaries
- avoid broad refactors unless requested or necessary
- avoid hidden runtime coupling
- avoid introducing unnecessary framework-specific abstractions
