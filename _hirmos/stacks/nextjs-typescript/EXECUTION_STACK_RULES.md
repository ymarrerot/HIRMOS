# EXECUTION STACK RULES

## Purpose

These rules define stack-specific execution behavior for projects using the `nextjs-typescript` stack package.

These rules complement framework core governance and execution-facing agent rules. They do not replace them.

## Core Behavior

When using this package, the executor should assume a modern typed web application workflow, but must still follow repository-local evidence when it differs.

The executor should:

- prefer existing repository scripts over guessed commands
- preserve TypeScript correctness
- preserve framework-specific routing and build conventions
- avoid introducing patterns that conflict with the current Next.js structure

## Implementation Discipline

The executor should:

- respect whether the project uses the app router, pages router, or a mixed transitional structure
- avoid moving files across routing boundaries without strong justification
- preserve server/client component intent where applicable
- avoid introducing untyped shortcuts to bypass TypeScript issues
- avoid silent broad dependency changes unless required

## Validation Discipline

When relevant and available, the executor should prefer:

- install or dependency sync
- lint
- type check
- test
- build

The executor should use repository-defined scripts first.

## Dependency and Tooling Discipline

The executor should infer and respect the repository's package manager where possible, such as:

- npm
- pnpm
- yarn

Do not mix package manager lockfile ecosystems casually.
