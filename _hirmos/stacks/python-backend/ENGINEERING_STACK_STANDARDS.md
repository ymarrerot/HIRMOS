# ENGINEERING STACK STANDARDS

## Purpose

These standards define engineering expectations for the `python-backend` stack package.

They complement framework-wide engineering standards with Python backend specific discipline.

## Standards

### 1. Preserve Readable Module Structure

Prefer clear module organization and explicit imports over clever but opaque structure.

### 2. Respect Repository Dependency Model

Use the dependency and environment model already present in the repository.

Do not mix incompatible workflows casually.

### 3. Keep Backend Boundaries Clear

Preserve clear boundaries between concerns such as:

- API layer
- business logic
- persistence
- tasks or workers
- integration utilities

### 4. Use Type Checking When the Repository Supports It

If the project uses type hints and a type checker, changes should respect that workflow.

### 5. Avoid Overengineering

Prefer clear, testable backend code over abstraction-heavy patterns unless the repository or task clearly requires them.
