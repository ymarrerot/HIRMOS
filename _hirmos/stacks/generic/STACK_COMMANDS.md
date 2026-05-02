# STACK COMMANDS

## Purpose

This file defines command selection guidance for the `generic` stack package.

Because this package is intentionally stack-neutral, command guidance is based on repository evidence rather than fixed technology assumptions.

## Command Selection Order

When a command is needed, use this order:

1. project-documented command in repository docs
2. project-defined script or task runner command
3. ecosystem-default command only when strongly supported by repository evidence
4. no command, with explicit note that verification could not be run safely

## Typical Command Categories

### Install

Examples the agent may inspect for:

- package manager install commands
- environment sync commands
- dependency bootstrap scripts

### Lint

Examples the agent may inspect for:

- repository lint script
- make lint
- task runner lint command

### Type Check

Use only when the repository clearly supports type checking.

### Test

Prefer repository-defined test commands.

### Build

Use build commands only when relevant to the task and clearly defined by the repository.

### Run / Smoke Check

Use only when a safe local run path is clear and appropriate.

## Important Rule

The `generic` package does not authorize the agent to guess commands casually.

If the command path is unclear, the agent should document that uncertainty instead of fabricating a verification path.
