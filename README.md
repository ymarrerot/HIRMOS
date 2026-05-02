# HIRMOS

**Orchestrated AI software engineering**

HIRMOS is a modular framework for governed AI-assisted software engineering. It gives teams a minimal core plus installable extensions so AI-assisted work stays reviewable, structured, and easier to evolve over time.

Use the open-source core to establish a governed operating model, then add only the extensions you need for design, implementation, presentation, ingestion, or custom workflows. You do not need to understand the internal repository structure to begin.

---

## Fast mental model

This is only a high-level picture. Most users can start with the core plus only the extensions they actually need.

```text
                             ┌──────────────────┐
                             │ solution-brief * │
                             └────────┬─────────┘
                                      │
                                      ▼
┌───────────────────────┐    ┌──────────────────┐    ┌───────────────────────┐
│ presentation-design * ├───►│   system-design-agent   │◄───┤ prototype-ingestion * │
└───────────────────────┘    │        **        │    └───────────────────────┘
                             └──────────────────┘  
                                      ▲ 
                                      │
                                      │
                                      │
┌───────────────────────┐    ╔══════════════════╗    ┌───────────────────────┐
│ private extension +   │◄───║     FRAMEWORK    ║───►│ community extension ++│
└───────────────────────┘    ║       CORE       ║    └───────────────────────┘
                             ╚══════════════════╝  
                                      │ 
                                      │
                                      │
                                      ▼                                       
                           ┌───────────────────────┐                             
                           │  implementation-agent │                             
                           │          **           │                             
                           └───────────────────────┘                             
```

- `**` major official extension
- `*` supporting official extension
- `+` private extension
- `++` community extension

---

## What this looks like in practice

### Example 1 — Turn messy requirements into a governed design path
A team starts with a vague feature request, a product note, or a customer conversation. HIRMOS can help structure that into reviewable design work, create the right supporting artifacts, and move the team toward a clearer implementation path without jumping straight into ungoverned coding.

### Example 2 — Turn approved design into reviewable AI-assisted implementation
A team already finished system design and phase design, and now wants AI help during implementation. HIRMOS can use implementation planning to turn approved design artifacts into implementation-ready prompts and then support governed implementation execution with review, retry, and clearer next steps instead of ad hoc coding sessions.

### Example 3 — Turn prototype-driven exploration into production-ready design work
A CEO, founder, or manager codes a prototype in a tool like Claude Code and hands it to the development team. HIRMOS can ingest that prototype, extract what is materially useful, and help the team convert prototype-driven exploration into governed production-ready design and implementation work.

---

## Who HIRMOS is for

HIRMOS is a strong fit for software engineers and teams who:
- already think in terms of real software delivery work
- want AI assistance without losing reviewability or control
- want a minimal core with installable workflow extensions
- are willing to use a governed process instead of pure prompt improvisation

## Who HIRMOS is not for

HIRMOS is probably not the right fit if you:
- only want a single throwaway prompt with no structured follow-up
- do not want reviewable artifacts, workflow discipline, or explicit operator decisions
- are looking for a no-process coding tool instead of a governed software engineering framework

---

## FAQ

**What is HIRMOS?**  
A modular framework for governed AI-assisted software engineering.

**Why does it exist?**  
Because AI-assisted software engineering needs more than prompts: it needs structure, reviewability, clear ownership, and workflow pieces that can evolve independently.

**What is in this repository?**  
The open HIRMOS core, bundled framework docs, extension-authoring docs, and the official/example extensions included in this distribution. Not every future extension needs to ship in this repository.

**How does HIRMOS work at a high level?**  
The core provides the shared operating model, command surface, and execution rules. Extensions add the specialized workflow intelligence for design, implementation, presentation, ingestion, or other project-specific work.

**Do I need every extension?**  
No. Use the core and only the extensions you actually need.

**Where do I find extensions?**  
Explore extensions in the HIRMOS Marketplace at [hirmos.dev](https://hirmos.dev).

**What is the difference between the core and extensions?**  
The core provides the shared operating model, while extensions add specialized workflow intelligence.

**Can I build private or community extensions?**  
Yes. You can build private extensions for your own organization or projects, and community extensions can later be shared or sold through the HIRMOS Marketplace.

**Does this README replace my project README?**  
No. This is the GitHub landing page for the framework; your project keeps its own README.

---

## What do you want to do next?

### I want to use the framework
- Follow the [Getting started guide](./_hirmos/docs/getting-started/README.md) for the canonical low-cognitive-load onboarding path. For first use, stay on that guide instead of mixing it with the broader docs lanes too early.

### I want to explore extensions
Included demo extensions in this distribution:
- `hello-world`: [hello-world README](./_hirmos/extensions/hello-world/README.md)
- `pretty-output`: [pretty-output README](./_hirmos/extensions/pretty-output/README.md)

Most official and community extensions are discovered through the marketplace:
- `system-design-agent`: [Marketplace page](https://hirmos.dev/product/system-design-agent/)
- `implementation-agent`: [Marketplace page](https://hirmos.dev/product/implementation-agent/)
- `presentation-design`: [Marketplace page](https://hirmos.dev/product/presentation-design/)
- `prototype-ingestion`: [Marketplace page](https://hirmos.dev/product/prototype-ingestion/)
- `solution-brief`: [Marketplace page](https://hirmos.dev/product/solution-brief/)

### I want to understand the framework
- Start with the docs hub: [Docs index](./_hirmos/docs/README.md)
- See the operating model: [Framework operating model](./_hirmos/docs/framework/framework-operating-model.md)
- Understand project truth and reviewability: [Source of truth model](./_hirmos/docs/framework/source-of-truth-model.md)
- Learn how extensions collaborate: [Framework hooks guide](./_hirmos/docs/framework/hooks.md)
- See how stack awareness fits in: [Framework stacks guide](./_hirmos/docs/framework/stacks.md)

### I want to build my own extensions
- Extension authoring overview: [Extensions overview](./_hirmos/docs/extensions/overview.md)
- Create your first extension: [Creating your first extension](./_hirmos/docs/extensions/creating-your-first-extension.md)
- Public entrypoints: [Public entrypoints](./_hirmos/docs/extensions/public-entrypoints.md)
- Spec-backed entrypoints: [Spec-backed entrypoints](./_hirmos/docs/extensions/spec-backed-entrypoints.md)
- Hooks authoring: [Hooks authoring](./_hirmos/docs/extensions/hooks-authoring.md)
- Best practices: [Extension best practices](./_hirmos/docs/extensions/best-practices.md)

For install-surface navigation after your first successful use, see [_hirmos/README.md](./_hirmos/README.md). For canonical folder definitions, see [Top-level folder definitions](./_hirmos/core/authority/framework/top-level-folder-definitions.md).
