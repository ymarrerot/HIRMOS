# Validation

HIRMOS uses validation to keep the framework installable, internally consistent, and safe to evolve.

This page is a contributor-facing overview for the public framework payload.

## What validation protects

Validation should protect the framework from drift in areas such as:

- required framework files;
- docs navigation and onboarding entrypoints;
- session artifact templates;
- command and lifecycle protocols;
- extension manifests and entrypoints;
- integration-tool registry/templates;
- regression fixture behavior.

## Public repository validation

For public framework-content changes, run the validator that ships inside the public framework payload:

```bash
python3 _hirmos/tools/validate.py
```

This is the validation command public contributors can rely on from the public repository.

## Maintainer validation

The maintainer's local workspace may run additional private/public parity, packaging, CLI, and release checks. Those checks belong to the local maintainer workspace and are intentionally not documented here as public repository requirements.

## Validator vs regression fixtures

Use the validator for static framework invariants.

Use regression fixtures for known failure modes that must remain protected over time.

A good regression case is useful when a bug could come back silently, such as:

- missing required artifacts;
- incomplete execution surfaces;
- invalid phase lifecycle state;
- broken integration registry;
- package/init mismatch;
- artifact surfaces drifting from the current model.

## CLI validation

The terminal CLI is an installer utility. Its most important responsibility is `hirmos init`.

From the public repository perspective, CLI behavior should be documented by what the published CLI does for users:

- installs the `_hirmos/` framework payload;
- reads `_hirmos/integrations/agent-tools/`;
- generates the selected AI-tool integration files;
- keeps workflow execution inside the AI coding tool rather than the terminal CLI.

## Failure posture

Validation failures should be treated as framework integrity failures, not cosmetic warnings.

Do not patch around a failing validator by weakening the invariant unless the invariant itself has been explicitly replaced by a better one.

## Validator minimality guidance

Prefer validator checks that protect authority safety, freshness, concordance, legal state transitions, required paths, and required status fields. Avoid exact-prose checks unless the wording itself prevents an authority-safety failure.

When a wording check is needed, phrase the invariant in structural terms where possible. For example, a delivery with `READY_FOR_BASELINE_REVIEW` must not be represented as accepted/active; the validator should check the delivery status and conflicting active labels, not require a single exact sentence.
