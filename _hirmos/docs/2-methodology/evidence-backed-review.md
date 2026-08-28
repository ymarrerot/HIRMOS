# Evidence-Backed Review

HIRMOS review is evidence-backed. In serious software work, done is not a declaration; it is a claim that must match evidence.

AI-assisted development makes this discipline more important because generated code or prose can look plausible before it has been tested, reviewed, or reconciled against accepted scope. HIRMOS therefore requires completion claims to be supported by appropriate evidence.

## What counts as evidence

Evidence can include:

- command output;
- test/build/lint results;
- runtime smoke results;
- user-observed verification;
- artifact validation;
- implementation-unit review rows;
- archive/close pointers.

The evidence must be appropriate to the claim. Local validation is not production-readiness evidence unless production deployment was actually exercised.

## Review gates

Review gates should answer:

- What was requested?
- What changed?
- What checks ran?
- What evidence supports the claim?
- What remains unresolved or limited?
- Is the claim partial, local-only, or production-ready?

## Salvage and correction

If review finds a problem, HIRMOS may correct it under the active authority. The correction should be recorded honestly with evidence. It should not erase the fact that a correction was needed.


## Review Gate Salvage

A passing static check is not a delivery review. Review must compare requested scope, implementation result, evidence, runtime posture, and remaining limitations.
