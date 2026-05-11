# Methodology docs folder rules

This folder owns user-facing methodology explanation for Orchestrated Spec-Driven Development.

## This folder owns

- Practical explanation of Orchestrated Spec-Driven Development.
- The relationship between Spec-Driven Development and Orchestrated SDD.
- The SDD-facing narrative that specs are necessary, but not enough.
- The general Beyond Clear Specs reliability pattern.
- The five pillars as methodology-level concepts.
- Methodology-level explanations of unresolved decisions, evidence-backed review, and the Requirements → System Design → Implementation lifecycle.
- How HIRMOS implements the methodology at a high level.

## This folder must not own

- Core runtime authority.
- Extension-authoring doctrine.
- Extension-local specs or entrypoint behavior.
- Marketplace commercial policy.
- Vendor/tool comparison pages.
- GSK/OpenSpec/Kiro-specific positioning.
- Detailed hook, manifest, or template authoring rules.

## Separation of concerns

Methodology explains the pattern.

Extension docs explain how extension authors implement the pattern safely.

Framework docs explain how HIRMOS is structured and operated.

Core authority files define enforceable runtime rules.

## Style

Use plain language before internal vocabulary.

Prefer practical examples over abstract definitions.

Use this pattern when explaining methodology concepts:

```text
durable orchestration requirement → practical example → consequence → solution → evidence
```

Lead with the long-term reason first: serious AI-assisted development needs traceable decisions, durable artifacts, reviewable outputs, validation, and honest terminal states.

Then explain the current pain that makes it urgent today: AI agents can still skip context, make silent assumptions, miss unresolved decisions, overclaim completion, or hide weak validation.

Use “orchestration” as the front-door word. Use “governed execution” when it clarifies the trust boundary, but do not make the methodology sound academic or compliance-heavy.

Do not frame Orchestrated SDD primarily as a workaround for current model limitations. Current model behavior matters, but the durable point is broader: specs define the intended work, orchestration governs how the work proceeds, and evidence shows whether completion can be trusted.
