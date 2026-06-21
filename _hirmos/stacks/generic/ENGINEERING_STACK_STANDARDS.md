# Generic Engineering Stack Standards

Status: stack guidance.
Purpose: Use when no more specific installed stack can be selected safely or when evidence is insufficient.

Stack guidance is not repository authority. Repository evidence and accepted HIRMOS system state govern actual commands, structure, and constraints.

## Generic production-shaped baseline

When no specific stack standard applies, HIRMOS should still prefer production-shaped engineering defaults: durable persistence for durable business data, explicit provider/configuration boundaries, safe secret/runtime-artifact handling, non-synchronous handling for long-running work, and evidence for critical flows. Weaker demo/local-only shortcuts must be explicitly authorized and preserved as limitations.
