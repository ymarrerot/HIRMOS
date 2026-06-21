# Close, Archive, and Accepted-State Integrity Protocol

Status: core protocol.
Purpose: ensure `hirmos close` is a governed state transaction, not a chat summary.

## close invariant

`hirmos close` is not complete until four surfaces agree:

1. **Session contract truth** — `_hirmos/session/SESSION_CONTRACT.md`, especially section 11, shows what was promised, what was verified, unresolved-item disposition, and the final fail-closed verdict.
2. **Execution truth** — `_hirmos/session/SESSION_EXECUTION.md` records the close command, execution controls, evidence log, archive/reset controls, and exactly one legal next command or action.
3. **Accepted current truth** — `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`, active-only `CARRY_FORWARD.md`, and `DECISION_LOG.md` reflect only accepted outcomes and durable decisions.
4. **Archive/reset truth** — the archive records archived artifacts and post-close verification, while active `_hirmos/session/` is reset to idle scaffolding. Archive manifest information belongs in `SESSION_EXECUTION.md` archive controls; do not create a separate active-session archive manifest support file.

If any surface disagrees, HIRMOS must report `Close Blocked`, not `Closed / Archived`.

## Core rule

Close is an integrity-sensitive operation. HIRMOS must not claim close success, archive success, accepted-state update, future-session readiness, or package cleanliness unless the active session artifacts, accepted-state records, archive contents, and active session reset all agree.

## Close transaction model

A normal close is a transaction with seven ordered parts:

1. **Readiness verification** — verify `SESSION_CONTRACT.md` including section 11, `unresolved-items.md`, `SESSION_EXECUTION.md`, implementation-unit reviews, `EVIDENCE.md` when present, and active execution controls.
2. **Accepted-state decision** — classify every material session outcome as accepted, superseded, rejected / not applied, evidence-only, carry-forward, or blocked.
3. **Accepted-state application** — update `_hirmos/system/accepted-state/` only for accepted outcomes, durable decisions, and active carry-forward items.
4. **Archive preservation** — copy the complete active session artifact set to `_hirmos/system/history/sessions/<session-id>/` and create `SESSION_EXECUTION.md` archive controls there.
5. **Archive-state normalization** — preserve pre-close state as history, and ensure the archived `SESSION_STATE.json` is terminal (`closed`, `archived`, or `history_only`), not active.
6. **Active-session reset** — reset `_hirmos/session/` to minimal idle scaffolding after archive preservation succeeds.
7. **Post-close verification** — verify archive path, current-state latest-close metadata, active-only carry-forward state, idle session state, and no stale active artifacts before surfacing close success.

If any required part fails, HIRMOS must stop at `Close Blocked` or use explicit `Abort Closed` when authorized. It must not partially claim normal close success.

## Required close authorities

Before normal close can be claimed, these active-session authorities must exist and contain non-placeholder content:

- `_hirmos/session/SESSION_CONTRACT.md` — scope, completion criteria, and close-verification mirror;
- `_hirmos/session/SESSION_CONTRACT.md` section 11 — governed promised-vs-verified review and final verdict;
- `_hirmos/session/unresolved-items.md` — governed unresolved-item register and disposition history;
- `_hirmos/session/SESSION_EXECUTION.md` — close execution controls, evidence log, and reset controls.

Implementation sessions also require:

- `_hirmos/session/implementation-units/IU-xx.md` for each planned implementation unit; each unit must include contract, evidence, unit review, and result.

Evidence beyond implementation-unit records is required only when the claim family is active and cannot be captured clearly in the relevant implementation-unit artifact. In that case, use root `EVIDENCE.md` as the consolidated evidence surface. Do not create separate runtime-readiness, local-runtime-evidence, role-workflow-smoke, claim-reconciliation, close-checklist, archive-manifest, or session-contract-review support files for new sessions.

`SESSION_EXECUTION.md` close/update controls, implementation-unit reviews, `EVIDENCE.md`, and `SESSION_CONTRACT.md` section 11 are the close evidence surfaces in the strict-necessity model. Close authority comes from `SESSION_CONTRACT.md`, `SESSION_EXECUTION.md`, `unresolved-items.md`, implementation-unit artifacts, `EVIDENCE.md` when present, and accepted-state files.

## Accepted-state records

Accepted state lives under:

```text
_hirmos/system/accepted-state/
```

The baseline accepted-state files are:

- `CURRENT_SYSTEM_STATE.md` — canonical merged current truth, accepted-state navigation, active development-context pointers, and latest-close metadata;
- `CARRY_FORWARD.md` — active carry-forward obligations only;
- `DECISION_LOG.md` — durable accepted, rejected, superseded, and replaced decisions;
- `REQUIREMENTS_BASELINE.md` when requirements governance is active.

A session archive is not accepted state by itself. Archived artifacts are history. Only accepted outcomes merged into `CURRENT_SYSTEM_STATE.md` become current accepted state.

## Archive manifest

Every normal close must archive a manifest at:

```text
_hirmos/system/history/sessions/<session-id>/ARCHIVE_MANIFEST.md
```

The archive manifest records:

- session id;
- close type;
- source active-session path;
- archive path;
- files archived;
- accepted outcomes applied;
- rejected / not-applied outcomes;
- evidence-only artifacts;
- carry-forward items;
- pre-close session state preservation;
- archived session state normalization;
- active-session reset result;
- post-close verification result.

## Integrity checks

Normal close requires all checks below to pass:

| Check | Required result |
|---|---|
| Session identity consistency | `SESSION_CONTRACT.md`, `SESSION_CONTRACT.md` section 11, `SESSION_EXECUTION.md`, archive path, and `SESSION_STATE.json` reference the same session id or explain why not applicable. |
| Contract review | `SESSION_CONTRACT.md` section 11 directly reviews `SESSION_CONTRACT.md`, `unresolved-items.md`, implementation units, validation/evidence appendices, and current system state as applicable. |
| Execution controls | no required control remains `PENDING`, `UNSATISFIED`, or `BLOCKED`. |
| Unresolved items | gated items are resolved, rejected, deferred with approval, or close is blocked; non-gating items are accepted as assumptions or carried forward. |
| Evidence claims | every accepted outcome has evidence or is explicitly accepted as documentation/design-only. |
| Runtime integration | accepted state and close output do not claim more integration or production readiness than evidence supports. |
| Delivery status | active Delivery / Phase status is reconciled with accepted outcomes and next recommendation when applicable. |
| Archive completeness | all active session artifacts are archived or exceptions are recorded. |
| Accepted-state application | accepted-state files are updated only with accepted outcomes, active carry-forward obligations, and durable decisions. |
| Active-session reset | `_hirmos/session/` is reset to minimal idle scaffolding after normal close. |
| Stale artifact scan | no active-session runtime artifact remains outside the allowed idle scaffolding. |
| Post-close status | `hirmos status` after close reports no active session and points to the latest archive and current-state latest-close metadata. |

## Active-session reset

After successful normal close, `_hirmos/session/` must contain only:

```text
_hirmos/session/.gitkeep
_hirmos/session/SESSION_STATE.json
_hirmos/session/bootstrap/.gitkeep
_hirmos/session/implementation-units/.gitkeep

```

`SESSION_STATE.json` must indicate idle status, no active governed session, and must point to the latest archived session when known.

The following are stale after normal close and must block close success if they remain active:

```text
SESSION_CONTRACT.md
SESSION_EXECUTION.md
unresolved-items.md
REQUIREMENTS_BASELINE.md
DESIGN.md
EVIDENCE.md
implementation-units/IU-*.md
stack-resolution.json
```

## Blocked close

Close must be blocked when:

- `SESSION_CONTRACT.md` section 11 is missing, placeholder-only, or not directly grounded in the session contract;
- accepted outcomes and evidence are not reconciled;
- gated unresolved items remain undecided;
- implementation was active but implementation units lack unit review or result sections;
- runtime integration posture is missing for material runtime claims;
- archive preservation cannot be verified;
- active-session reset would destroy unarchived artifacts;
- stale active-session artifacts remain after reset;
- close would require new Design or Implementation work;
- accepted-state records would contradict the archive or active session evidence.

## Abort close

Abort close preserves available artifacts and failure reasons in history but must not update accepted-state records as if the session succeeded.

Abort close output must say that work was archived for history only and is not accepted current system state.

## User-facing close output

Close output must be concise and mode-sensitive, but it must include:

- close result;
- accepted outcomes;
- archive path;
- current-state latest-close metadata path;
- carry-forward items;
- evidence or production-readiness limitations;
- one primary next command/action or next Delivery Unit recommendation when supported.

Do not claim that the app works, is production-ready, or that a delivery unit is complete unless the archived evidence and accepted-state records support that claim.

## archive/session-state integrity archive-state enforcement

Close is not complete until archive state and active state are both truthful.

HIRMOS must enforce these rules:

1. **Archive the pre-close truth without leaving active-state contradictions.** If the active session state is useful as historical evidence, preserve it as `PRE_CLOSE_SESSION_STATE.json` or an explicitly labeled section in `SESSION_EXECUTION.md` archive controls.
2. **Normalize the archived session state.** The archive copy of `SESSION_STATE.json` must not say `active`, `implementation_complete`, or any active-session status after normal close. It must say the session is closed, archived, or history-only.
3. **Reset the active session state.** `_hirmos/session/SESSION_STATE.json` must say idle / no active session after normal close.
4. **Reconcile all three state views.** `SESSION_EXECUTION.md`, `SESSION_EXECUTION.md` archive controls, and active `_hirmos/session/SESSION_STATE.json` must agree about close result, latest archive, and accepted-state update.
5. **Block close on disagreement.** If archived state, active state, accepted state, or close controls disagree, HIRMOS must report `Close Blocked`. It must not claim archive success or update-state success.

Firm rule: archive only after the change is complete and state is consistent. A chat statement that close succeeded is not close evidence.

### Required archive-state fields

`SESSION_EXECUTION.md` archive controls must record:

- `pre_close_session_state_recorded`: yes / no / not_applicable;
- `archived_session_state_status`: closed / archived / history_only / missing / conflict;
- `active_session_state_after_close`: idle / conflict / not_checked;
- `accepted_state_update_status`: applied / not_applied / blocked;
- `post_close_status_result`: consistent / conflict / not_checked.

Any value other than `closed`, `archived`, `history_only`, `idle`, `applied`, or `consistent` where required blocks normal close.

## durable current-system-state durable current-system-state merge

Normal close must merge accepted outcomes into `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`.

Close is blocked when `CURRENT_SYSTEM_STATE.md` is missing, stale, or not updated for accepted session outcomes.

The accepted-state folder must contain:

- `CURRENT_SYSTEM_STATE.md` — canonical merged current truth;
- `CURRENT_SYSTEM_STATE.md` latest-close metadata — navigation, latest close pointer, and accepted-state file index;
- `CARRY_FORWARD.md` — active carry-forward obligations only;
- `DECISION_LOG.md` — durable accepted, rejected, and superseded decisions.

### Current-state merge requirements

Before close success is surfaced, HIRMOS must verify:

1. accepted outcomes are mapped to sections in `CURRENT_SYSTEM_STATE.md`;
2. rejected / not-applied outcomes are not promoted into current truth;
3. evidence-only outcomes remain archive evidence only;
4. active carry-forward items are reflected in `CARRY_FORWARD.md`, while resolved/closed carry-forward history is recorded in the archive and `CURRENT_SYSTEM_STATE.md` History / Traceability;
5. durable decisions are reflected in `DECISION_LOG.md`;
6. `CURRENT_SYSTEM_STATE.md` latest-close metadata points to the updated current state and latest archive;
7. production-readiness planning, provider readiness, compliance readiness, and go-live approval remain separate tracks.

Firm rule: `hirmos close` is not complete until current system state, current-state latest-close metadata, active carry-forward records, decision log, archive manifest, and active session reset agree.

## Accepted-state invariant and canonical-value close enforcement

Before normal close, HIRMOS must verify accepted-state artifact invariants and canonical runtime values.

Required checks:

1. `CURRENT_SYSTEM_STATE.md`, `CURRENT_SYSTEM_STATE.md` latest-close metadata, `CARRY_FORWARD.md`, and `DECISION_LOG.md` preserve their accepted-state invariant block.
2. `CURRENT_SYSTEM_STATE.md` latest-close metadata remains navigation/latest-close metadata and does not replace `CURRENT_SYSTEM_STATE.md`.
3. Runtime posture fields use only canonical posture values.
4. Evidence/status fields use only canonical evidence values.
5. Accepted-state decision classifications are not written into evidence/status fields.
6. Role-workflow smoke claims are backed by `EVIDENCE.md`, including `NOT_RUN` when smoke checks were intentionally not performed.
7. Shared packages exclude local secrets, generated runtime folders, and operating-system metadata before being treated as clean review/package evidence.

Firm rule: archive and close are blocked when accepted-state artifacts would lose required invariants or contain noncanonical runtime/evidence values.

## close-time compliance gate and evidence artifact materialization

Close-time compliance does not create a new evidence authority. It makes the existing close transaction enforce the existing evidence authorities before close success is surfaced.

Normal close is itself a material close/archive/update-state claim. Therefore `_hirmos/session/EVIDENCE.md` is mandatory for every normal close. The artifact may record `NOT_APPLICABLE` for claim families that were not active, but it must exist and reconcile close, archive, accepted-state, validation, runtime, and packaging claims before normal close is reported.

### Evidence artifact materialization matrix

Before normal close, HIRMOS must materialize the owning evidence artifact when its trigger is present. Do not replace a missing owning artifact with chat output, carry-forward prose, or a summary in another artifact.

| Trigger | Owning artifact that must exist before close | Required close behavior |
|---|---|---|
| Any normal close / archive / accepted-state claim | `_hirmos/session/EVIDENCE.md` | Reconcile the close claim using canonical evidence states. |
| Any Implementation was active | `_hirmos/session/implementation-units/IU-xx.md review` and `_hirmos/session/EVIDENCE.md` | Decide whether implementation completion is accepted, partial, blocked, or evidence-only. |
| Any local runtime, database, provider, setup, seed, dev-server, route, or user-environment claim | `_hirmos/session/EVIDENCE.md` | Record setup attempts and limitations with canonical evidence states. |
| Any role, actor, approval, user journey, or workflow-readiness claim | `_hirmos/session/EVIDENCE.md` | Record smoke checks or `NOT_RUN` / `BLOCKED` / `NOT_APPLICABLE` per material workflow. |
| Any runtime provider / integration posture claim | `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` | Use canonical runtime posture values only. |
| Any package, export, downloadable zip, or review-package claim | package-cleanliness record in `SESSION_EXECUTION.md` archive controls, `SESSION_EXECUTION.md`, or the package report | Record excluded/allowed local files and block clean-package claims if dirty files are present. |

### Close-time validator gate

Before normal close success is surfaced, HIRMOS must run or explicitly record the result of the framework validator when the framework files changed or when accepted-state invariants are involved.

Required result:

```text
python3 _hirmos/tools/validate.py = PASS
```

If validation is not run, record `NOT_RUN` in `EVIDENCE.md` claim reconciliation and do not claim framework compliance. If validation fails, normal close is blocked until the failure is fixed or the close is explicitly downgraded to blocked/abort history.

### Close-time canonical scan

Before normal close, HIRMOS must scan generated session and accepted-state artifacts for noncanonical evidence/status/runtime posture values in structured fields. At minimum, scan:

- `_hirmos/session/EVIDENCE.md`;
- `_hirmos/session/EVIDENCE.md` when present;
- `_hirmos/session/DESIGN.md` / `_hirmos/session/EVIDENCE.md` when present;
- `_hirmos/session/EVIDENCE.md` when present;
- `_hirmos/session/EVIDENCE.md` when present;
- `_hirmos/session/SESSION_CONTRACT.md`;
- `_hirmos/session/SESSION_EXECUTION.md`;
- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`;
- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` accepted-state navigation/latest-close section;
- `_hirmos/system/accepted-state/CARRY_FORWARD.md`;
- `_hirmos/system/accepted-state/DECISION_LOG.md`.

Any noncanonical value found in a structured evidence/status/posture field must be translated through the owning protocol before close. Prose notes may include explanatory words, but structured status fields must remain canonical.

### Close-time invariant preservation

Accepted-state invariant blocks are preserved system content. Update System State may update values around them, but must not delete, rename, or weaken them. If an accepted-state artifact loses its invariant block or required invariant phrase, close is blocked and the artifact must be restored before archive success is claimed.

Firm rule: close does not get a compliance grace period. Missing evidence artifacts, failed validation, lost accepted-state invariants, noncanonical structured values, or dirty package claims make the correct result `Close Blocked`, not `Closed with caveats`.
