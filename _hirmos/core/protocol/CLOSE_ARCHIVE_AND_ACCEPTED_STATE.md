# Close, Archive, and Accepted-State Integrity Protocol

Status: core protocol.
Purpose: ensure `hirmos close` is a governed state transaction, not a chat summary.

## close invariant

`hirmos close` is not complete until four surfaces agree:

1. **Session scope truth** — `_hirmos/session/SESSION_SCOPE.md`, especially close verification, shows what was promised, what was verified, unresolved-item disposition, and the final fail-closed verdict.
2. **Execution truth** — `_hirmos/session/SESSION_EXECUTION.md` records the close command, execution controls, evidence pointers, archive/reset control pointers, and exactly one legal next command or action.
3. **Accepted current truth** — `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`, active-only `CARRY_FORWARD.md`, and conditional `DECISION_LOG.md` when explicit decision-log governance is active reflect only accepted outcomes, active carry-forward obligations, and governed durable decisions.
4. **Archive/reset truth** — the archive records archived artifacts and post-close verification, while active `_hirmos/session/` is reset to idle scaffolding. Archive manifest information belongs in history at `ARCHIVE_MANIFEST.md` and in `SESSION_EXECUTION.md` archive controls; do not create a separate active-session archive manifest support file.

If any surface disagrees, HIRMOS must report `Close Blocked`, not `Closed / Archived`.

## Core rule

Close is an integrity-sensitive operation. HIRMOS must not claim close success, archive success, accepted-state update, future-session readiness, or package cleanliness unless the active session artifacts, accepted-state records, archive contents, and active session reset all agree.

## Close transaction model

A normal close is a transaction with seven ordered parts:

1. **Readiness verification** — verify `SESSION_SCOPE.md` including close verification, `unresolved-items.md`, `SESSION_EXECUTION.md`, implementation-unit reviews, `EVIDENCE.md` when present, and active execution controls.
2. **Close-time carry-forward triage** — classify every unresolved/evidence/follow-up candidate before final close as `AUTO_RESOLVED_NOW`, `USER_RESOLVED_NOW`, `APPROVED_CARRY_FORWARD`, `BLOCKING_UNRESOLVED`, or `NO_LONGER_APPLIES`.
3. **Accepted-state decision** — classify every material session outcome as accepted, superseded, rejected / not applied, evidence-only, approved carry-forward, or blocked.
4. **Accepted-state application** — update `_hirmos/system/accepted-state/` only for accepted outcomes, durable decisions, and user-approved active carry-forward items.
4. **Archive preservation** — copy the complete active session artifact set to `_hirmos/system/history/sessions/<session-id>/` and create `SESSION_EXECUTION.md` archive controls there.
5. **Archive-state normalization** — preserve pre-close state as history, and ensure the archived `SESSION_STATE.json` is terminal (`closed`, `archived`, or `history_only`), not active.
6. **Active-session reset** — reset `_hirmos/session/` to minimal idle scaffolding after archive preservation succeeds.
7. **Post-close verification** — verify archive path, current-state latest-close metadata, active-only carry-forward state, idle session state, and no stale active artifacts before surfacing close success.

If any required part fails, HIRMOS must stop at `Close Blocked` or use explicit `Abort Closed` when authorized. It must not partially claim normal close success.

## Required close authorities

Before normal close can be claimed, these active-session authorities must exist and contain non-placeholder content:

- `_hirmos/session/SESSION_SCOPE.md` — scope, completion criteria, and close-verification mirror;
- `_hirmos/session/SESSION_SCOPE.md` close verification — governed promised-vs-verified review and final verdict;
- `_hirmos/session/unresolved-items.md` — governed unresolved-item register and disposition history;
- `_hirmos/session/SESSION_EXECUTION.md` — close execution controls, evidence log, and reset controls.

Implementation sessions also require:

- `_hirmos/session/implementation-units/IU-xx.md` for each planned implementation unit; each unit must include contract, evidence, unit review, and result.

Evidence beyond implementation-unit records is required only when the claim family is active and cannot be captured clearly in the relevant implementation-unit artifact. In that case, use root `EVIDENCE.md` as the consolidated evidence surface. Do not create separate runtime-readiness, local-runtime-evidence, role-workflow-smoke, claim-reconciliation, close-checklist, archive-manifest, or session-scope-review support files for new sessions.

`SESSION_EXECUTION.md` close/update control pointers, implementation-unit reviews, `EVIDENCE.md`, and `SESSION_SCOPE.md` close verification are the close evidence surfaces in the strict-necessity model. Close authority comes from `SESSION_SCOPE.md`, `SESSION_EXECUTION.md`, `unresolved-items.md`, implementation-unit artifacts, `EVIDENCE.md` when present, and accepted-state files.

## Close-time carry-forward triage doctrine

Carry-forward is a last-resort close disposition. HIRMOS must not use `_hirmos/system/accepted-state/CARRY_FORWARD.md` as a default bucket for checks, evidence gaps, minor cleanup, or safe local verification that can be completed within the approved session/delivery baseline.

Before normal close, HIRMOS must run a **Close-Time Carry-Forward Candidate Review** using these dispositions:

| Disposition | Meaning | Close impact |
|---|---|---|
| `AUTO_RESOLVED_NOW` | HIRMOS safely resolved the candidate within approved scope during close-time reconciliation. | Do not create active carry-forward; record evidence in active session and archive. |
| `USER_RESOLVED_NOW` | User supplied the missing evidence/input or approved an in-session check before close finalized. | Do not create active carry-forward unless a residual obligation remains. |
| `APPROVED_CARRY_FORWARD` | User explicitly approved deferral or the accepted scope already authorized deferred/partial close. | Record an active item in `CARRY_FORWARD.md` with source archive and future-session instruction. |
| `BLOCKING_UNRESOLVED` | The item is required for the claimed close/acceptance level and is not resolved or approved for deferral. | Close is blocked or downgraded. |
| `NO_LONGER_APPLIES` | Later evidence or scope reconciliation made the candidate obsolete. | Do not create active carry-forward; record why it no longer applies. |

User approval for deferral must be explicit when the item materially affects acceptance, evidence posture, runtime/production claims, or future implementation. A post-close `hirmos start` recommendation is valid only for `APPROVED_CARRY_FORWARD` items or separately scoped new work.

## Accepted-state records

Accepted state lives under:

```text
_hirmos/system/accepted-state/
```

The baseline accepted-state files are:

- `CURRENT_SYSTEM_STATE.md` — accepted-state navigation authority, current governance pointers, chronological Work History Ledger, Source Artifact Index, concise current-state summary, and latest-close metadata;
- `CARRY_FORWARD.md` — active carry-forward obligations only;
- `DECISION_LOG.md` — conditional durable accepted, rejected, superseded, and replaced decisions when explicit decision-log governance is active.

Default HIRMOS must not create root accepted-state `REQUIREMENTS.md`, `DESIGN.md`, `SYSTEM_SCOPE.md`, `DECISIONS.md`, or `ACCEPTED_CHANGES.md`. Requirements, design, and scope remain source authorities at delivery/session/archive level unless a future explicit cumulative-governance mode is activated.

A session archive is not accepted state by itself. Archived artifacts are history. Accepted outcomes become current accepted state by updating `CURRENT_SYSTEM_STATE.md` navigation, Work History Ledger, Source Artifact Index, and concise accepted-state summary as needed.

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
| Session identity consistency | `SESSION_SCOPE.md`, `SESSION_SCOPE.md` close verification, `SESSION_EXECUTION.md`, archive path, and `SESSION_STATE.json` reference the same session id or explain why not applicable. |
| Scope review | `SESSION_SCOPE.md` close verification directly reviews `SESSION_SCOPE.md`, `unresolved-items.md`, implementation units, validation/evidence appendices, and current system state as applicable. |
| Execution controls | no required control remains `PENDING`, `UNSATISFIED`, or `BLOCKED`. |
| Close-time carry-forward triage | every unresolved/evidence/follow-up candidate is auto-resolved, user-resolved, approved for carry-forward, blocked, or marked no-longer-applicable with evidence. |
| Unresolved items | gated items are resolved, rejected, deferred with approval, or close is blocked; non-gating items are accepted as assumptions or approved carry-forward after triage. |
| Evidence claims | every accepted outcome has evidence or is explicitly accepted as documentation/design-only. |
| Runtime integration | accepted state and close output do not claim more integration or production readiness than evidence supports. |
| Delivery status | active Delivery / Phase status is reconciled with accepted outcomes and next recommendation when applicable. |
| Archive completeness | all active session artifacts are archived or exceptions are recorded. |
| Accepted-state application | accepted-state files are updated only with accepted outcomes, active carry-forward obligations, durable decisions, source artifact pointers, Work History Ledger rows, and current governance navigation. Detailed requirements/design/scope content is not copied into root accepted-state artifacts by default. |
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
SESSION_SCOPE.md
SESSION_EXECUTION.md
unresolved-items.md
REQUIREMENTS.md
DESIGN.md
EVIDENCE.md
implementation-units/IU-*.md
stack-resolution.json
```

## Blocked close

Close must be blocked when:

- `SESSION_SCOPE.md` close verification is missing, placeholder-only, or not directly grounded in the session scope;
- accepted outcomes and evidence are not reconciled;
- gated unresolved items remain undecided;
- implementation was active but implementation units lack unit review or result sections;
- runtime integration posture is missing for material runtime claims;
- archive preservation cannot be verified;
- active-session reset would destroy unarchived artifacts;
- stale active-session artifacts remain after reset;
- close would require new Design or Implementation work;
- accepted-state records would contradict the archive, source artifact index, Work History Ledger, or active session evidence.

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
- `DECISION_LOG.md` — conditional durable accepted, rejected, and superseded decisions when explicit decision-log governance is active.

### Current-state merge requirements

Before close success is surfaced, HIRMOS must verify:

1. accepted outcomes are mapped to sections in `CURRENT_SYSTEM_STATE.md`;
2. rejected / not-applied outcomes are not promoted into current truth;
3. evidence-only outcomes remain archive evidence only;
4. active carry-forward items are reflected in `CARRY_FORWARD.md`, while resolved/closed carry-forward history is recorded in the archive and `CURRENT_SYSTEM_STATE.md` History / Traceability;
5. durable decisions are reflected in conditional `DECISION_LOG.md` when explicit decision-log governance is active;
6. `CURRENT_SYSTEM_STATE.md` latest-close metadata points to the updated current state and latest archive;
7. production-readiness planning, provider readiness, compliance readiness, and go-live approval remain separate tracks.

Firm rule: `hirmos close` is not complete until current system state, current-state latest-close metadata, active carry-forward records, decision log, archive manifest, and active session reset agree.

## Accepted-state invariant and canonical-value close enforcement

Before normal close, HIRMOS must verify accepted-state artifact invariants and canonical runtime values.

Required checks:

1. `CURRENT_SYSTEM_STATE.md`, latest-close metadata, and `CARRY_FORWARD.md` preserve their accepted-state invariant blocks; conditional `DECISION_LOG.md` does so when active.
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
- `_hirmos/session/SESSION_SCOPE.md`;
- `_hirmos/session/SESSION_EXECUTION.md`;
- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md`;
- `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` accepted-state navigation/latest-close section;
- `_hirmos/system/accepted-state/CARRY_FORWARD.md`;
- `_hirmos/system/accepted-state/DECISION_LOG.md` only when explicit decision-log governance is active.

Any noncanonical value found in a structured evidence/status/posture field must be translated through the owning protocol before close. Prose notes may include explanatory words, but structured status fields must remain canonical.

### Close-time invariant preservation

Accepted-state invariant blocks are preserved system content. Update System State may update values around them, but must not delete, rename, or weaken them. If an accepted-state artifact loses its invariant block or required invariant phrase, close is blocked and the artifact must be restored before archive success is claimed.

Firm rule: close does not get a compliance grace period. Missing evidence artifacts, failed validation, lost accepted-state invariants, noncanonical structured values, or dirty package claims make the correct result `Close Blocked`, not `Closed with caveats`.


## PROD-L6 accepted-state/history alignment

ARCHIVE_MANIFEST.md is history-only. It records the close transaction and concordance checks, but it does not become accepted current truth by itself. Normal close is valid only when the archive manifest, `SESSION_EXECUTION.md` close controls, `SESSION_SCOPE.md` close verification, active-session reset, and accepted-state files agree.

For delivery-governed work, close must verify that Current System State delivery pointers refreshed or were explicitly verified unchanged. The required pointer model is:

```text
Delivery roadmap: _hirmos/system/delivery/DELIVERY_PLAN.md
Active delivery scope: _hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md
Active phase: _hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md
```

A normal close must not leave accepted state pointing to `_hirmos/system/delivery/<delivery-id>/DELIVERY_PLAN.md` as active delivery authority. That path is legacy/historical only under the PROD-L model.

Close is blocked if `ARCHIVE_MANIFEST.md`, archived `SESSION_STATE.json`, active reset `SESSION_STATE.json`, and `CURRENT_SYSTEM_STATE.md` disagree about the close verdict, accepted outcomes, carry-forward state, delivery pointer updates, or next governed command.


## PROD-L8.14 accepted-state navigation authority

At normal close, HIRMOS must update `CURRENT_SYSTEM_STATE.md` using an index-first model:

1. Current Governance Context.
2. Work History Ledger.
3. Source Artifact Index.
4. Accepted State Summary only when materially changed.
5. Next recommended work / navigation.

Close must not merge session or delivery requirements into `_hirmos/system/accepted-state/REQUIREMENTS.md` by default. Instead, it records the source artifact path and accepted result in `CURRENT_SYSTEM_STATE.md`. A cumulative root requirements baseline requires explicit future governance activation and close-time merge/deprecation controls.

## Active Navigation Updates vs Accepted Outcome Updates

`hirmos continue` may refresh active navigation pointers in `CURRENT_SYSTEM_STATE.md` when the active delivery, phase, session scope, unresolved register, or next recommended command changes. That transition update is not an accepted close outcome.

`hirmos close` owns accepted outcome updates: latest accepted close metadata, final Work History Ledger rows, accepted-state summary changes, final Source Artifact Index changes, archive concordance, and active-session reset.

Close must fail closed if active pointer updates and accepted outcome records contradict each other.

## PROD-L8.19 archive chronology and carry-forward concordance

Close must verify chronology and cross-artifact freshness before surfacing success.

### Session archive timestamp monotonicity

Archived session timestamps must be monotonic with the governed transcript/session sequence unless an explicit chronology exception is recorded. A later session must not appear to start or close before an earlier session close without explanation.

Required check:

- archived session ID / sequence;
- `created_at`, `started_at`, `closed_at`, and archive manifest timestamp;
- prior archived session close timestamp;
- transcript order when available;
- chronology exception rationale when monotonicity is not possible due to imported/restored history.

### Delivery-plan multi-section freshness

`DELIVERY_PLAN.md` close-time reconciliation must update or mark historical every active/pointer section that can affect future routing. It is not enough to append a correct final section while older active context, accepted-state pointers, delivery review, or status-log sections still imply stale active phase, stale carry-forward, stale current-state version, or stale next command.

### Later carry-forward resolution concordance

When a later session resolves a carry-forward item that limited earlier phase acceptance, HIRMOS must either:

- update affected phase/delivery current verification posture with a link to later evidence; or
- explicitly mark the original phase verdict as historical and point to the later resolution record.

The original close verdict may remain historically true, but current navigation must not leave future sessions believing the carry-forward is still unresolved.

## PROD-L8.21 close-time concordance hardening

Close must perform a cross-artifact concordance sweep before success claims:

- archived session timestamp completeness and monotonicity;
- `PHASE-xx.md` close-time phase concordance sweep;
- `DELIVERY_PLAN.md` delivery close concordance sweep;
- `CURRENT_SYSTEM_STATE.md` source-artifact index placeholder cleanup;
- `CARRY_FORWARD.md` Active-Only Rule template concordance;
- evidence semantics separation: implementation accepted vs runtime verified vs production verified.

A close may append historical records, but current pointer sections must be fresh or explicitly historical before HIRMOS claims close success.

## PROD-L8.22 phase and delivery evidence-backed review gates

Close must run evidence-backed review gates before updating accepted state.

### Phase review gate

For each phase being accepted, partially accepted, blocked, or failed, close must reconcile:

- phase authority and adopted scope;
- session and IU execution evidence;
- actual final codebase review where project files changed;
- unit-level completion and cross-unit integration;
- runtime/provider evidence level;
- production evidence level;
- unresolved and carry-forward impact;
- final phase result and what is not claimed.

### Delivery review gate

For each delivery being accepted, partially accepted, blocked, or failed, close must reconcile:

- all phase review gates;
- cross-phase integration;
- end-to-end workflow evidence;
- requirements/scope coverage posture;
- runtime/provider evidence level;
- production evidence level;
- carry-forward items affecting acceptance;
- final delivery result and what is not claimed.

Close must not claim full delivery, MVP, runtime, or production success when the available evidence only supports implementation acceptance. When evidence is partial, the honest terminal state is `PARTIAL`, `BLOCKED`, or a narrower `implementation accepted` claim.


## PROD-L8.23 Generated-Run Close Concordance Validation
Close/archive must leave generated artifacts validator-inspectable, not merely plausible. Before close succeeds, HIRMOS should verify generated runtime artifacts for timestamp completeness, monotonic archive chronology, phase-current-body concordance, delivery-plan status-log coverage, carry-forward status accuracy, and evidence-claim separation. If any generated artifact remains stale or contradictory, close must downgrade the result, mark the stale section as historical, or fail closed until reconciled.


## PROD-L8.24 Retrospective Governance Close Guard
Close/archive may normalize evidence and reconcile accepted state, but it must not create or expand pre-execution authority for the first time and then represent the session as cleanly governed. If close detects missing IU authority, missing pre-material-edit ledger proof, missing generated review gates, stale delivery scope/phase status, or source-index placeholders, close must record a governance deviation, downgrade acceptance, or block close until corrected through governed recovery.

## PROD-L8.26 Delivery Close Concordance Simplification and Evidence Posture Hardening

When close affects durable delivery work, HIRMOS must reduce duplicated close truth and harden only dangerous evidence contradictions.

Ownership model:

- `DELIVERY_SCOPE.md` owns compact delivery close posture and delivery authority pointers.
- `PHASE-xx.md` owns phase-level outcome and phase review posture.
- archived `SESSION_SCOPE.md`, implementation units, and `EVIDENCE.md` own session-level details.
- `_hirmos/system/delivery/<delivery-id>/unresolved-items.md` owns live delivery-level unresolved items only.
- `CURRENT_SYSTEM_STATE.md` owns accepted-state navigation and compact current evidence posture only.
- `ARCHIVE_MANIFEST.md` owns archive completeness and reset concordance only.

Close must not duplicate full evidence tables across all of those surfaces. It must update compact status/pointer rows and archive/evidence source pointers.

Close must block or downgrade when:

- delivery close claims full `PASS`, `LOCAL_E2E_VERIFIED`, `LOCAL_RUNTIME_VERIFIED`, `USER_ENVIRONMENT_VERIFIED`, `PRODUCTION_VERIFIED`, or `PRODUCTION_READINESS_VERIFIED` while material critical-flow/provider/browser/image/database/production evidence is `NOT_RUN`, `BLOCKED`, absent, or explicitly not verified;
- `DELIVERY_SCOPE.md` remains in current rows with stale `planned`, `ready_for_adoption`, `PENDING`, or `NOT_STARTED` values after final delivery/phase/session acceptance;
- delivery unresolved items remain current `OPEN`, `CARRIED`, `REVIEWABLE`, or `PENDING` while accepted phase/session outcomes contradict them;
- `CURRENT_SYSTEM_STATE.md` contains generated placeholder Source Artifact Index rows or broad runtime/production claims unsupported by evidence;
- archived `SESSION_STATE.json` remains active or points active authority to reset active-session paths;
- close chronology contains impossible timestamp ordering without an explicit exception.

Use `CLOSED_PARTIAL`, `ACCEPTED_WITH_LIMITATIONS`, `PARTIAL`, `NOT_RUN`, `BLOCKED`, or carry-forward when those are the honest states. Implementation acceptance is allowed without claiming runtime or production verification.

## PROD-L8.27 Pre-Archive Validation Gate and Archive Immutability

Close/archive must validate fixable active work before creating historical archives. This updates the existing close transaction model; it does not create a new artifact authority.

### Pre-archive validation gate

Before archive preservation begins, HIRMOS must run an active-session validation gate over the active close surfaces:

- `_hirmos/session/SESSION_SCOPE.md` close verification;
- `_hirmos/session/SESSION_EXECUTION.md` close controls, IU timing controls, review gates, and evidence pointers;
- `_hirmos/session/implementation-units/IU-xx.md` sealed contract sections and append-only execution/review records when IU mode is active;
- `_hirmos/session/EVIDENCE.md` when present;
- `_hirmos/session/unresolved-items.md` or the active delivery unresolved register, depending on session focus;
- active delivery/phase/delivery-scope/current-state close posture when delivery governance is active.

If the pre-archive validation gate fails, HIRMOS may correct active artifacts, route back, block, or close partial with an explicit governance deviation. HIRMOS must not archive first and then repair historical authority/evidence to make the validator pass.

### Archive immutability boundary

After the archive snapshot is created under `_hirmos/system/history/sessions/<session-id>/`, archived historical governance and evidence artifacts are immutable evidence. HIRMOS must not edit archived IU contracts, pre-execution checkpoints, review gates, execution status, evidence posture, or session authority content to satisfy a validator after the fact.

Allowed post-archive repair is limited to archive transaction mechanics:

- fixing a missing or incorrect `ARCHIVE_MANIFEST.md` inventory row;
- correcting archive path/copy/packaging mistakes;
- normalizing archived `SESSION_STATE.json` to terminal/history-only state when the archive transaction created the wrong machine-state copy;
- adding an external corrective/supersession note or marking a governance deviation.

Historical governance gaps discovered after archive are `ARCHIVE_HISTORICAL_IMMUTABLE`: record the limitation, downgrade/block close as needed, and carry forward a process/framework issue. Do not rewrite history.

### Failure classes

Validator and close messages should classify failures as:

| Failure class | Meaning | Allowed response |
|---|---|---|
| `ACTIVE_FIXABLE` | Active close artifact is still mutable before archive. | Fix active artifact, route back, block, or close partial. |
| `ARCHIVE_TRANSACTION_REPAIRABLE` | Archive packaging/reset mechanics are wrong. | Repair archive transaction mechanics and record the repair. |
| `ARCHIVE_HISTORICAL_IMMUTABLE` | Historical authority/evidence was missing, thin, stale, or contradictory when archived. | Do not patch history; record governance deviation, supersession note, blocked/partial close, or carry-forward. |

Normal close success requires a recorded pre-archive validation result of `PASS` or an honest partial/blocked result that explains the unresolved active-validation failure before archiving.

## PROD-L8.28 Generated IU Instantiation and Active Close Concordance

Generated implementation-unit artifacts must be validated while the session is active and before archive. A generated IU is close-eligible only when its sealed contract sections were fully instantiated before execution and its append-only Execution Record and Unit Review contain concrete evidence-backed completion/review results.

Active close must fail closed, downgrade to partial, or route back when IU status contradicts session/phase/delivery close claims. In particular, implementation-complete, phase-accepted, delivery-accepted, or delivery-closed claims are invalid when any applicable IU remains `Execution status: NOT_STARTED`, `Review status: PENDING`, lacks Unit Result, lacks validation/evidence comparison, or lacks a required Test / Fixture / Validator Change Rationale. Historical archives must not be expanded to repair these defects after snapshot; apply PROD-L8.27 archive immutability instead.

## PROD-L8.31 Mechanical Close Acceptance Gate

Generated close cannot rely on narrative compliance. Before archive preservation, active artifacts must pass generated-run mechanical validation:

- bootstrap answers complete;
- planned IU count matches full IU artifacts or `LIGHTWEIGHT_NO_IU` was declared before edits;
- active generated-artifact validation result is `PASS` before completion/acceptance claims;
- carry-forward entries marked `APPROVED_CARRY_FORWARD` include explicit approval/deferral source;
- current-state and delivery pointers are refreshed and concordant.

Any failure must be fixed while active, downgraded honestly, or recorded as blocked/partial. Do not archive a clean close when generated-run mechanical gates failed.
