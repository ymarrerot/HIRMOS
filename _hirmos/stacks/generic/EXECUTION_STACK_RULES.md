# EXECUTION STACK RULES

## Purpose

These rules define stack-specific execution behavior for projects using the `generic` stack package.

These rules complement framework core governance and execution-facing agent rules. They do not replace them.

## Core Behavior

When using the `generic` package, the executor must:

- avoid assuming a language, framework, package manager, or runtime without evidence
- inspect the repository before selecting commands or implementation patterns
- prefer existing repository conventions over guessed best practices
- explain assumptions clearly in run outputs when stack uncertainty remains

## Command Selection Discipline

When commands are needed, the executor must:

- first look for repository-defined commands or scripts
- prefer project-local documented commands over ecosystem defaults
- avoid inventing commands that are not grounded in the repository or prompt
- record which commands were used and why

## Verification Discipline

When verification is possible, the executor should prefer the strongest relevant checks available in the repository, such as:

- tests
- linting
- type checking
- builds
- smoke checks

If strong verification is not available, the executor must state the gap explicitly instead of pretending verification was complete.

## Implementation Discipline

When using the `generic` package, the executor should:

- minimize unnecessary structural changes
- follow established repository patterns
- avoid introducing framework-specific abstractions unless clearly justified
- avoid large refactors unless requested or required by the task

## Escalation Rule

If the repository clearly matches a specific stack for which a dedicated package exists, the executor should note that the current project may benefit from switching from `generic` to a more specific stack package.
