<!-- HIRMOS-CAPSULE:start:PROD-L8.33C-2 canonical command capsule v1 -->
## hirmos start command capsule

`hirmos start` establishes governed starting authority. It is not an implementation command and must end at a governed baseline checkpoint.

Required behavior:
1. Read `_hirmos/AGENTS.md` and the start command authority.
2. Inspect current system state, relevant user inputs, and only the project files needed to scope the request.
3. Create or update the required HIRMOS session/delivery governance artifacts.
4. Present the governed baseline checkpoint for user review.
5. Stop.

Forbidden behavior:
- Do not edit product/source files outside `_hirmos/` during `hirmos start`.
- Do not treat detailed implementation instructions as implementation authorization.
- Do not mark the baseline accepted without user acceptance.

<!-- /HIRMOS-CAPSULE:start:PROD-L8.33C-2 canonical command capsule v1 -->
