# HIRMOS

**Open framework for Orchestrated Spec-Driven Development**

HIRMOS is an open modular framework for AI-assisted software engineering. It implements **Orchestrated Spec-Driven Development**: a practical workflow that uses specs to define what the AI agent should build, then adds orchestration to govern how the work proceeds, pauses, validates, and proves completion.

```text
Spec-Driven Development (SDD) gives the work a clearer source of truth: the spec.
Orchestrated SDD keeps that foundation and adds governance for how the agent proceeds, pauses, validates, and proves completion.
HIRMOS is the framework implementation for Orchestrated SDD.
```

## Why HIRMOS exists

Spec-Driven Development is a major step beyond ad hoc prompting. Clear Specs are much stronger than vague requests.

But **Clear Specs are not enough**.

The simple distinction is:

```text
Specs define the intended work.
Orchestration governs how the work proceeds.
Evidence shows whether completion can be trusted.
```

This is not only about today's model limitations. Serious AI-assisted software work needs traceable decisions, durable artifacts, reviewable outputs, validation, and honest terminal states across sessions, files, people, and time.

That need is especially visible today because AI agents can still:

- skip context or reconcile inputs incompletely;
- make silent assumptions when an unresolved decision should pause the work;
- lose assumptions, open questions, and tradeoffs in prose instead of durable artifacts;
- validate weakly or hide validation gaps;
- claim completion when required evidence, decisions, or checks are missing.

HIRMOS adds the orchestration layer around the work: runtime controls, durable artifacts, unresolved-decision handling, hooks, validation, fail-closed behavior, terminal states, and evidence-backed completion.

The result is not black-box code generation. The result is a practical workflow that stays inspectable, pauses when trust would be lost, and leaves reviewable evidence behind.

HIRMOS follows four onboarding principles:

- **Simple by default.** Start with the three-step workflow.
- **Transparent by design.** Artifacts, decisions, and evidence remain inspectable.
- **Rigorous underneath.** Runtime controls, validation, and fail-closed behavior protect the workflow.
- **Progressive disclosure.** Learn the internals only when you need them.

---

## The HIRMOS workflow

The regular-user flow is intentionally simple:

```text
Requirements → System Design → Implementation
```

It is backed by official lifecycle extensions:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

What each step does:

1. **Requirements** turns goals, notes, files, prototypes, constraints, and user context into structured requirements artifacts.
2. **System Design** turns requirements into architecture, system decisions, phase design, and implementation-ready planning artifacts.
3. **Implementation** plans, pauses for approval when needed, executes bounded phases, validates results, and completes with Evidence-backed Review.

Supporting extensions can add specialized context such as prototypes, presentation/design inputs, solution briefs, or private workflow intelligence.

---

## Fast mental model

Most users can start with Core plus the official extensions for the workflow they need.

```text
                         Requirements → System Design → Implementation

┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│  requirements-agent  │───►│  system-design-agent │───►│ implementation-agent │
└──────────────────────┘    └──────────────────────┘    └──────────────────────┘
          ▲                           ▲                            ▲
          │                           │                            │
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│ prototype-ingestion* │    │ presentation-design* │    │   solution-brief*    │
└──────────────────────┘    └──────────────────────┘    └──────────────────────┘
          ▲                           ▲                            ▲
          └───────────────┬───────────┴──────────────┬─────────────┘
                          │                          │
                 ╔══════════════════╗       ┌──────────────────────┐
                 ║  FRAMEWORK CORE  ║◄─────►│ private/community ext │
                 ╚══════════════════╝       └──────────────────────┘
```

- **Core** provides the shared operating model, command surface, runtime controls, hook governance, and fail-closed behavior.
- **Official lifecycle extensions** provide Requirements, System Design, and Implementation workflows.
- **Supporting extensions** add specialized inputs or outputs without forcing everything into Core.
- **Private/community extensions** can extend HIRMOS while preserving the same governed workflow.

---

## What HIRMOS helps with

HIRMOS is built for teams and technical builders who want AI-assisted development that remains inspectable and governed.

It helps you:

- move from rough intent to reviewable requirements;
- turn requirements into system design before coding;
- break implementation into bounded, reviewable phases;
- keep unresolved decisions visible instead of hidden in prose;
- preserve project truth in durable artifacts;
- know when the agent completed, paused, or failed honestly;
- extend the workflow through composable extensions.

HIRMOS is probably **not** the right fit if you want one-shot prompts, hidden black-box generation, or maximum speed without traceability.

---

## What this looks like in practice

### From rough input to requirements

A team starts with a vague feature request, product note, customer conversation, prototype, or set of user stories. HIRMOS helps turn that input into requirements artifacts such as `REQUIREMENTS_SOT.md`, while surfacing assumptions, open questions, and unresolved items instead of hiding them.

### From requirements to system design

A team has reviewed requirements and wants a design path before implementation. HIRMOS uses `system-design-agent` to produce system and architecture artifacts such as `SYSTEM_SOT.md`, `ARCHITECTURE_SOT.md`, and `PHASES_SOT.md`.

### From approved design to implementation

A team is ready to build. HIRMOS uses `implementation-agent` to plan implementation, pause for approval where needed, execute bounded phases, validate results, and finish with Evidence-backed Review.

---

## Installing and initializing HIRMOS

Install the HIRMOS CLI, then initialize the project from the project root:

```bash
npm install -g hirmos
hirmos init
```

If `_hirmos/` is not already present, `hirmos init` downloads the latest HIRMOS framework release package, installs the drop-in `_hirmos/` folder, and generates the default `agents` integration.

A normal install preserves your project root files and adds only the drop-in `_hirmos/` folder beside them. Do not copy the full GitHub repository checkout into a project, because the repository also contains collaboration metadata and maintainer automation that are not part of a normal project install.

`hirmos init` is a terminal command. It generates thin agent-native bootstrap files, defaults to the `agents` integration, and points the selected AI tool to `_hirmos/HIRMOS_CORE.md`. It does not invoke agents and does not run HIRMOS workflows.

To initialize a specific HIRMOS release, use:

```bash
hirmos init --version 1.3.1
```

To initialize from a local release package instead of downloading, use:

```bash
hirmos init --source /path/to/hirmos-framework.zip
```

To initialize additional agent-native adapters, rerun:

```bash
hirmos init --integration claude,cursor,copilot
```

Supported integration IDs are `agents`, `claude`, `cursor`, `copilot`, `codex`, `opencode`, `gemini`, `windsurf`, and `kiro`.

If you are not using the CLI yet, initialize HIRMOS by prompting your AI tool with the explicit bootstrap instruction:

```text
Read and follow the instructions on _hirmos/HIRMOS_CORE.md
```

After HIRMOS Core is loaded in the AI tool, use the regular HIRMOS workflow commands as agent-facing instructions:

```text
hirmos requirements
hirmos system-design
hirmos implementation
```

These workflow commands are interpreted by HIRMOS after Core has loaded. They are not terminal shell commands.

---

## Decide what you want to do next

### I want to use HIRMOS on a project

Start with the regular-user docs lane:

1. [Install and Initialize HIRMOS](./_hirmos/docs/1-use-hirmos/getting-started/install-and-initialize.md)
2. [Use HIRMOS in 3 Steps](./_hirmos/docs/1-use-hirmos/getting-started/use-hirmos-in-3-steps.md)
3. [Quickstart](./_hirmos/docs/1-use-hirmos/getting-started/quickstart.md)
4. [First Real Run](./_hirmos/docs/1-use-hirmos/getting-started/first-real-run.md)

### I want to understand the methodology

Read the Orchestrated SDD docs:

- [Orchestrated Spec-Driven Development](./_hirmos/docs/2-methodology/README.md)
- [Specs are not enough](./_hirmos/docs/2-methodology/specs-are-not-enough.md)
- [Beyond Clear Specs](./_hirmos/docs/2-methodology/beyond-clear-specs.md)

### I want to extend or contribute to HIRMOS

Start with the contributor/extension-author lane:

- [Extend & Contribute to HIRMOS](./_hirmos/docs/3-extend-contribute/README.md)
- [Extensions overview](./_hirmos/docs/3-extend-contribute/extensions/overview.md)
- [Creating your first extension](./_hirmos/docs/3-extend-contribute/extensions/creating-your-first-extension.md)

### I need reference material

Use the reference lane when you need definitions or cross-cutting artifact context:

- [Reference index](./_hirmos/docs/reference/README.md)
- [Glossary](./_hirmos/docs/reference/glossary.md)
- [Source of truth model](./_hirmos/docs/reference/source-of-truth-model.md)

---

## Extensions in this distribution

The HIRMOS framework package includes the free official starter workflow:

- `requirements-agent`
- `system-design-agent`
- `implementation-agent`

The public repository also includes demo extensions for learning and validation:

- [`hello-world`](./_hirmos/extensions/hello-world/README.md)
- [`pretty-output`](./_hirmos/extensions/pretty-output/README.md)

Supporting, marketplace, private, and community extensions can add specialized workflow intelligence without making Core larger. Examples include presentation/design input handling, prototype ingestion, solution briefs, security/compliance review, team handoff, or custom organization workflows.

Explore marketplace extensions at [hirmos.dev](https://hirmos.dev).

---

## Repository contents

This repository contains the open HIRMOS framework, bundled documentation, the free official starter workflow, example extensions, and maintainer automation for packaging and release workflows.

For install-surface navigation after your first successful use, see [_hirmos/README.md](./_hirmos/README.md). For canonical folder definitions, see [Top-level folder definitions](./_hirmos/core/authority/framework/top-level-folder-definitions.md).

---

## Contributing

Public Core contributions are welcome through GitHub issues and pull requests. Small documentation fixes can go straight to a PR. Core behavior, bootstrap, command protocol, hook, packaging, or extension-contract changes should start as a proposal issue first.

HIRMOS Core is intentionally small. Contributions that move extension-specific behavior into Core will usually be declined or redirected into an extension proposal.

---

## License

HIRMOS Core is licensed under the Apache License 2.0. Marketplace extensions, private extensions, and third-party extensions may be distributed under their own licenses unless otherwise stated.
