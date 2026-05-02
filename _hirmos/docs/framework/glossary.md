# Glossary

Use this page as a lightweight user-facing reference for the most common HIRMOS terms.

For deeper authority, follow the linked authority files rather than treating this page as the owner of those rules.

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
