# Extension Manifests

## Purpose

Define the framework-wide extension doctrine for manifest authoring from the extension side.

Use this authority file when deciding:
- what the manifest is responsible for declaring
- how much behavior should be expressed declaratively
- what belongs in the manifest versus deeper docs or extension-local specs
- how extension authors should think about manifest boundaries

For the canonical Core-local field contract and interpretation behavior, see:
- [Extension manifest authority](../core/extension-manifest-authority.md)

## Role of the manifest

An extension manifest is the authoritative declaration surface for extension identity and public runtime participation.

From the extension side, the manifest should declare:
- who the extension is
- what kind of extension it is
- what HIRMOS workflow commands it exposes
- what public runnable surfaces those commands resolve to
- what dependencies it requires
- what hooks it exposes or subscribes to
- what runtime identity metadata it declares when applicable

The manifest should not become a substitute for deeper workflow method or tutorial explanation.

## Declarative boundary

Use the manifest for declarations.

Do not overload the manifest with explanatory prose or local operational method that belongs in:
- extension README files
- user-facing docs
- extension-local specs

The manifest states what the extension declares. Other surfaces explain why and how.

## Public command and surface declarations

If an extension exposes a user-runnable workflow, the manifest should declare a HIRMOS workflow command under `hirmos_commands`.

The command declaration should resolve to an entrypoint exposed by `entry` or `entrypoints`.

If a file is not meant to be run as part of the extension's public contract, do not expose it through manifest declarations.

For public surface doctrine, see:
- [Extension entrypoints](./entrypoints.md)

## Dependency declarations

Dependencies declared in the manifest should reflect real runtime or governance requirements.

Do not declare dependencies casually.

A dependency should mean the extension expects another extension's declared surface to exist and materially matter.

## Hook declarations

Use manifest hook declarations when the extension is:
- exposing a hook seam it owns
- subscribing to a declared seam exposed by another extension

The manifest is authoritative for the existence of those declarations. Hook quality and appropriateness are governed by extension hook doctrine.

For hook doctrine, see:
- [Extension hooks](./hooks.md)

## Runtime identity declarations

If an extension benefits from a chat-facing runtime identity, declare `runtime.identity` in the manifest.

The extension declares the value only. The Core owns display behavior and formatting.

## Relationship to Core interpretation

This file defines extension-side manifest authoring doctrine.

The Core authority file remains authoritative for:
- exact field contract
- parsing behavior
- validation behavior
- interpretation of declared values

## Review tests

When reviewing an extension manifest, ask:
- Is the manifest used as a declaration surface rather than an explanation surface?
- Are HIRMOS workflow commands declared intentionally?
- Do declared workflow commands resolve to valid public entrypoints?
- Are dependencies real and meaningful?
- Are hook declarations healthy and justified?
- Is deeper workflow method kept out of the manifest?
