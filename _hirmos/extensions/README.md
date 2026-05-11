# Installed Extensions in This Project

This folder shows the HIRMOS extensions that are installed in **this specific project**.

In a minimal framework copy, this folder may contain only the built-in demo and support extensions:
- [hello-world](./hello-world/README.md)
- [pretty-output](./pretty-output/README.md)

That is normal.

If you want to **discover available HIRMOS extensions**, including official and community extensions, go to the HIRMOS extension marketplace at [hirmos.dev](https://hirmos.dev).

Use this folder when you want to answer questions like:
- Which extensions are already installed in this project?
- Where does an installed extension fit in the Software Development Lifecycle?
- What usually comes before or after this installed extension in project work?

You do **not** need extension authoring docs just to browse installed extensions. You also do **not** need to study each extension's internal folders to decide whether it is relevant. Start with the README of the extension you care about and treat deeper folders as optional reading unless you are implementing, extending, or debugging that extension. If you want to build or modify extensions, go to [Extension authoring guidance](../docs/3-extend-contribute/extensions/README.md).

## Start here after getting started

If you already finished the [Getting started guide](../docs/1-use-hirmos/getting-started/README.md), use this folder to browse the extensions that are actually installed in this workspace.

If you are still deciding what to install, start at the HIRMOS extension marketplace at [hirmos.dev](https://hirmos.dev).

## Understand what you are looking at

There are three different extension contexts in HIRMOS:

1. **Marketplace discovery** — use [hirmos.dev](https://hirmos.dev) to see what official and community extensions exist.
2. **Installed extensions in this project** — use this folder to see what is already available in the current workspace. Start with each extension's `README.md`; deeper subfolders such as `docs/`, `entrypoints/`, `specs/`, `internal/`, and `templates/` are not required reading for casual browsing.
3. **Demo/support extensions in a minimal install** — expect [hello-world](./hello-world/README.md) and [pretty-output](./pretty-output/README.md) even before you install serious workflow extensions.

## Most common extensions by SDLC stage

### Requirements work
- [requirements-agent](https://hirmos.dev/marketplace/requirements-agent/) — turns user goals, context, notes, prototypes, user stories, files, and constraints into governed requirements artifacts suitable for system design

### Design and planning work
- [system-design-agent](https://hirmos.dev/marketplace/system-design-agent/) — turns requirements into governed design, architecture, and phase artifacts before implementation begins
- [presentation-design](https://hirmos.dev/marketplace/presentation-design/) — normalizes presentation constraints and design-pack signals before or during broader design work
- [prototype-ingestion](https://hirmos.dev/marketplace/prototype-ingestion/) — turns raw prototype evidence into governed prototype artifacts before broader design continues

### Implementation work
- [implementation-agent](https://hirmos.dev/marketplace/implementation-agent/) — turns approved design into governed implementation prompts, execution, and verification

### External communication and handoff
- [solution-brief](https://hirmos.dev/marketplace/solution-brief/) — turns trusted internal planning artifacts into a concise outward-facing brief

### Demo and support extensions
- [hello-world](./hello-world/README.md) — smallest runnable example for understanding the command model
- [pretty-output](./pretty-output/README.md) — hook-only example that enhances hello-world output

## Common official extension path by SDLC stage

A common official path across major SDLC stages looks like this:

1. Start with [requirements-agent](https://hirmos.dev/marketplace/requirements-agent/) when you need governed requirements artifacts from user goals, context, notes, prototypes, user stories, files, and constraints.
2. Continue to [system-design-agent](https://hirmos.dev/marketplace/system-design-agent/) when requirements are ready for governed system design, architecture, and phase planning.
3. Add [prototype-ingestion](https://hirmos.dev/marketplace/prototype-ingestion/) or [presentation-design](https://hirmos.dev/marketplace/presentation-design/) when prototype or presentation inputs materially shape requirements or design.
4. Continue to [implementation-agent](https://hirmos.dev/marketplace/implementation-agent/) when approved design is ready for governed build work.
5. Use [solution-brief](https://hirmos.dev/marketplace/solution-brief/) when you need a concise external summary grounded in trusted upstream artifacts.

## Go next

- **Discover more extensions:** browse the HIRMOS extension marketplace at [hirmos.dev](https://hirmos.dev).
- **Browse what is already installed here:** stay in this folder and open the installed extension that matches the kind of work you need to do.
- **Understand the broader operating model:** go to [Framework guidance](../docs/3-extend-contribute/framework/README.md).
- **Operate serious runs safely:** go to the [Operator playbook](../docs/1-use-hirmos/orchestrator/operator-playbook.md).

## Optional reading

- **Build or modify extensions:** go to [Extension authoring guidance](../docs/3-extend-contribute/extensions/README.md).
- **Need the canonical folder rule?** See [Top-level folder definitions](../core/authority/framework/top-level-folder-definitions.md).
