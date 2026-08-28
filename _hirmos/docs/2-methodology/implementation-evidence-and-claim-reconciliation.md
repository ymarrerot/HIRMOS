# Implementation Evidence and Claim Reconciliation

HIRMOS treats implementation claims as evidence-backed claims, not just model assertions. In serious software work, implementation status must be demonstrated by evidence that matches the scope of the claim.

AI-assisted development makes claim reconciliation more important because an agent can complete many edits before the human has inspected whether the evidence supports local runtime, production readiness, partial completion, or a blocked result.

## Evidence levels

Implementation work may produce several kinds of evidence:

- code diff evidence;
- static validation evidence;
- build/test/lint evidence;
- runtime smoke evidence;
- user-observed runtime evidence;
- production-readiness evidence when production readiness is actually in scope.

A claim must match the evidence level. A local MVP can be accepted as local runtime work without claiming production readiness.

## IU evidence

When implementation units are used, each IU should record:

- requested outcome;
- files/artifacts changed;
- checks performed;
- evidence produced;
- unit result;
- review result.

`SESSION_LEDGER.md` should point to IU/evidence records instead of duplicating all evidence detail.

## Governed automated testing and test integrity

HIRMOS treats automated tests as implementation evidence tied to behavioral authority.

For material software work:

- inspect and reuse the repository's existing test architecture;
- prefer unit tests for new or changed isolated deterministic logic when practical;
- bind the testing posture into `SESSION_SCOPE.md` and, when IU mode applies, each sealed IU contract;
- use relevant targeted existing tests as a pre-change comparison point when practical;
- write practical regression tests for reproducible defects;
- preserve the strength of valid tests when their governing behavior remains unchanged;
- update or remove tests/fixtures when the governed behavior changes or disappears so orphan tests do not accumulate;
- classify material test deltas and explain changes that could weaken validation;
- use component/integration/runtime evidence where those layers are necessary to prove the claim.

A failing implementation must not be made green by weakening a still-valid test. Conversely, an obsolete test must not be preserved artificially after its business rule disappears. The test suite should describe current governed behavior, not historical requirements and not whatever output the current implementation happens to produce.

HIRMOS does not impose a universal coverage percentage and does not create `TEST_PLAN.md` or `TEST_REPORT.md` by default. Testing obligations live in the existing scope/IU/evidence/review surfaces.

## Claim reconciliation

Before completion or close claims, HIRMOS must reconcile:

- accepted scope;
- implementation results;
- validation output;
- unresolved items;
- production/runtime limitations;
- carry-forward items.

If evidence is missing or contradictory, HIRMOS should report blocked or partial status rather than overclaiming.

## Generated-run validation boundary

Generated HIRMOS artifacts are part of the run. They must satisfy generated-run mechanical gates before HIRMOS claims a clean implementation or close.

## No retrospective compliance

HIRMOS must not implement first and then backfill governance artifacts as if they authorized the work. Retrospective correction may honestly document what happened, but it does not turn an unauthorized action into a clean gate pass.

## IU Planning before IU Execution

When IU mode applies:

```text
Session Baseline accepted → IU Planning only
IU Plan accepted → IU Execution
```

Material project-file edits require IU execution authorization.


## Command and environment evidence wording

A claim should say whether the logged command passed, failed, was not run, or was user environment verified. User environment verified evidence is useful, but it should be labeled separately from commands the agent actually ran.

## Generated-Run Validation Boundary

Generated session archives are part of the evidence record. HIRMOS must validate active and archived generated artifacts before claiming a clean generated-run result.

## Retrospective Compliance Boundary

The active ledger must prove pre-execution authorization. Backfilled artifacts can document a correction honestly, but they cannot convert unauthorized implementation into a clean pre-execution gate pass.

## Generated-Run Mechanical Gates

HIRMOS must report all generated-run gate failures instead of hiding failures behind a generic completion claim.
