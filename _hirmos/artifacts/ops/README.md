# /_hirmos/artifacts/ops/

Authoritative top-level folder definition: see [Top-level folder definitions](../../core/authority/framework/top-level-folder-definitions.md).

`/_hirmos/artifacts/ops/` stores governed operational runtime artifacts produced during the implementation stage of the Software Development Lifecycle. Under the current framework authority model, only one implementation-focused extension can be **used as** the implementation authority for code-changing execution at a time, so `/_hirmos/artifacts/ops/` remains a flat canonical implementation execution lane.

Typical subfolders include:
- `/_hirmos/artifacts/ops/runs/`
- `/_hirmos/artifacts/ops/reviews/`
- `/_hirmos/artifacts/ops/retries/`

Do not use `/_hirmos/artifacts/ops/` as a generic catch-all for every internal review or analysis artifact across the framework.
