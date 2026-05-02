# STACK COMMANDS

## Purpose

This file defines preferred command patterns for the `python-backend` stack package.

Repository-defined commands still take precedence over generic examples.

## Environment and Tool Detection

Prefer repository evidence such as:

- `pyproject.toml`
- `requirements.txt`
- `requirements-dev.txt`
- task runner config
- documented local development commands

## Common Command Categories

### Install / Environment Setup

Prefer repository-defined setup first.

Depending on repository evidence, examples may include:

- environment sync via project tooling
- virtual environment activation plus dependency install
- pip-based or tool-based dependency installation

### Lint / Format

Prefer repository-defined commands.

Common Python ecosystems may use formatting and lint tools, but the executor should follow repository evidence first.

### Type Check

Run only when the repository clearly supports type checking.

### Test

Prefer repository-defined test commands.

Common patterns may include:

- project test script
- pytest-based workflows

### Run / Smoke Check

Use only when a safe local validation path is clear.

### Build

Use only when the repository has a real build/package step relevant to the task.

## Important Rule

These command patterns are guidance, not permission to impose a Python workflow that the repository does not actually use.

Repository-local evidence always wins.
