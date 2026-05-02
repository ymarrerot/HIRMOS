# Extension Document Roles

## Purpose

Define extension-level document role boundaries.

This file explains the roles of extension-facing document types once content has already been routed into the correct high-level folder.

It does **not** govern cross-folder routing. For cross-folder routing, use [Cross-folder rules](../shared/cross-folder-rules.md). For the local rules of `/_hirmos/core/authority/extensions/`, use [Folder rules](./folder-rules.md).

## Extension README role {#extension-readme-role}

An extension README is the package-level landing page for humans.

It should:
- explain what the extension is for
- clarify where the extension fits in the broader workflow
- help a reader discover the main runnable or reference surfaces
- point to deeper local specs, docs, and authority when needed

It should not silently become the deepest local doctrine owner when a more specific extension file already exists.

### What an extension README should do well {#extension-readme-do-well}

A good extension README should:
- orient the reader quickly
- explain what the extension adds to the framework
- make the main public surfaces easy to find
- summarize without becoming a second authority file

### What an extension README should avoid {#extension-readme-avoid}

An extension README should avoid:
- re-owning local method already defined in a spec
- hiding serious validation or trust rules only in README prose
- mixing first-contact guidance with deep implementation detail
- becoming the only place where important workflow behavior is described

### Typical extension concerns a README may surface

An extension README may surface:
- what the extension does
- where it fits in the lifecycle
- what entrypoints or commands it exposes
- which outputs or artifacts it commonly produces
- what deeper specs or docs to read next

### Relationship to framework authority, docs, and specs

The extension README is the package-level front door. Framework authority still owns framework-wide rules. Extension-local specs own serious local method and workflow behavior. Docs teach and illustrate. The README should connect those surfaces without trying to replace them.

## Extension guidance docs

Extension guidance docs explain an extension to humans.

They should:
- teach
- summarize
- guide
- illustrate
- point to deeper extension-local specs or framework authority when needed

They should not silently replace the authoritative local method or canonical framework doctrine.

## Extension specs

Extension specs own serious local method, workflow behavior, contract detail, validation expectations, or pause/provisional/completion rules.

They should:
- define local method and quality bars
- centralize serious workflow behavior
- stay stronger than a casual instruction page

## Entrypoints and wrappers

Entrypoints and wrappers are public runnable surfaces.

They should:
- expose the public contract
- point to deeper governing local method when needed
- remain lean enough to read at execution time

They should not try to absorb every deeper local rule that belongs in a spec.

## Templates, hooks, manifests, and internal notes

These surfaces each play narrower roles:
- templates stabilize governed shapes
- hooks augment another extension's behavior without taking over ownership
- manifests declare public package surfaces
- internal notes support maintenance and development rather than public execution

## Review tests

When reviewing extension document roles, ask:
- Does this file match the role it claims to play?
- Is serious local workflow method owned in specs instead of scattered across README prose?
- Does the extension README stay a landing page instead of becoming a doctrine dump?
- Are public runnable surfaces clearly distinguished from deeper local governance files?
- Are supporting file types doing their own jobs without re-owning each other?
