# Glossary

Use this page as a lightweight user-facing reference for the most common HIRMOS terms.

For deeper authority, follow the linked authority files rather than treating this page as the owner of those rules.

## Orchestrated Spec-Driven Development

The HIRMOS methodology: Spec-Driven Development with an added orchestration layer for how AI agents execute the work.

Spec-Driven Development makes the spec drive the work. HIRMOS adds governed orchestration through artifacts, controls, validation, unresolved-decision handling, hooks, and evidence-backed review.

## Requirements

The first step in the regular-user HIRMOS workflow.

The Requirements step turns user-provided goals, context, notes, prototypes, user stories, files, and constraints into requirements artifacts suitable for system design.

A clear HIRMOS artifact name in this area is `REQUIREMENTS_SOT.md`.

## System Design

The second step in the regular-user HIRMOS workflow.

The System Design step turns requirements into system model, architecture, phases, and unresolved-decision surfaces.

Clear HIRMOS artifact names in this area include `SYSTEM_SOT.md`, `ARCHITECTURE_SOT.md`, and `PHASES_SOT.md`.

## Implementation

The third step in the regular-user HIRMOS workflow.

The Implementation step plans and executes bounded work, validates results, handles repair or pauses, and includes Evidence-backed Review before work is treated as complete.

## Evidence-backed Review

A required sub-concept under Implementation.

Evidence-backed Review means HIRMOS reviews the work based on evidence: what changed, what checks ran, what passed or failed, what remains unresolved, and whether the run completed, paused, or failed.

## Use HIRMOS

The regular-user documentation track for people who want to run HIRMOS on their software projects without first learning the full framework internals.

## Extend & Contribute to HIRMOS

The power-user, contributor, and extension-author documentation track.

This lane helps readers find the right extension, contribution, and marketplace-authoring guidance while preserving the existing sources of truth.

## Core

The minimal framework layer that interprets commands, resolves extension surfaces, and enforces the public runtime contract.

Deeper authority:
- [_hirmos/core/core-rules.md](../../core/core-rules.md)
- [_hirmos/core/command-protocol.md](../../core/command-protocol.md)
- [_hirmos/core/execution-model.md](../../core/execution-model.md)

## Extension

An installed package under `_hirmos/extensions/<id>/` that adds governed capabilities to the framework.

Deeper authority:
- [_hirmos/core/authority/core/extension-manifest-authority.md](../../core/authority/core/extension-manifest-authority.md)
- [_hirmos/core/authority/extensions/extension-document-roles.md](../../core/authority/extensions/extension-document-roles.md)

## requirements-agent

The official extension ID/name for the Requirements step in the regular-user workflow.

## system-design-agent

The official system design focused extension.

In the regular-user workflow, it backs the System Design step.

## implementation-agent

The official implementation focused extension.

In the regular-user workflow, it backs the Implementation step.

## Entrypoint

A public runnable surface exposed by an extension. Entrypoints give the Orchestrator intentional command surfaces instead of exposing every internal file.

Deeper authority:
- [_hirmos/core/authority/core/entrypoint-execution-contract.md](../../core/authority/core/entrypoint-execution-contract.md)
- [_hirmos/core/authority/extensions/extension-document-roles.md](../../core/authority/extensions/extension-document-roles.md)

## Extension-local spec

A governed extension-local document that owns authoritative workflow behavior or local method. In HIRMOS, workflow or command-governing extension specs use `.spec.md`, while non-procedural doctrine and reference material use plain `.md`.

Deeper authority:
- [_hirmos/core/authority/shared/cross-folder-rules.md](../../core/authority/shared/cross-folder-rules.md)

## Hook

A bounded augmentation point that lets one surface participate in another without taking over its ownership.

Deeper authority:
- [_hirmos/core/authority/core/hook-execution-control.md](../../core/authority/core/hook-execution-control.md)

## Orchestrator

The human authority directing the framework. The framework may propose, warn, or pause, but the Orchestrator decides what to run and what to accept.

Deeper authority:
- [_hirmos/core/authority/framework/framework-operating-model.md](../../core/authority/framework/framework-operating-model.md)
