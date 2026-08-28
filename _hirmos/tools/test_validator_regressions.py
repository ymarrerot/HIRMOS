#!/usr/bin/env python3
"""Regression fixtures for HIRMOS command-state validation.

Regression fixtures for HIRMOS command-state, delivery-governance, phase-entry-gate, and phase progress/carry-forward validation.

This runner intentionally mutates temporary framework copies and verifies that
`_hirmos/tools/validate.py` fails closed for known-bad command/session states.
It is not a replacement for the main validator; it protects the validator itself.
"""
from __future__ import annotations

import contextlib
import io
import json
import os
import runpy
import subprocess
import shutil
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Case:
    name: str
    mutate: Callable[[Path], None]
    should_pass: bool
    expected: str


@dataclass(frozen=True)
class ValidationResult:
    returncode: int
    output: str


def run_validator(root: Path) -> ValidationResult:
    """Run the validator against a temporary _hirmos copy.

    Output is written to a temporary file instead of a pipe so many sequential
    fixture subprocesses cannot block on captured stdout/stderr buffers.
    """
    output_path = root.parent / "validator-output.txt"
    with output_path.open("w+", encoding="utf-8") as output_file:
        try:
            completed = subprocess.run(
                [sys.executable, str(root / "tools" / "validate.py")],
                cwd=str(root.parent),
                text=True,
                stdout=output_file,
                stderr=subprocess.STDOUT,
                timeout=30,
            )
            output_file.seek(0)
            return ValidationResult(completed.returncode, output_file.read())
        except subprocess.TimeoutExpired:
            output_file.seek(0)
            return ValidationResult(124, output_file.read() + "\nFAIL: validator fixture subprocess timed out\n")


def cleanup_stale_tempdirs() -> None:
    tmp_root = Path(tempfile.gettempdir())
    for child in tmp_root.glob("hirmos-validator-regression-*"):
        if child.is_dir():
            shutil.rmtree(child, ignore_errors=True)


def make_copy() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix="hirmos-validator-regression-"))
    target = tmp / "_hirmos"
    shutil.copytree(
        ROOT,
        target,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )
    return target


def read_state(root: Path) -> dict:
    return json.loads((root / "session" / "SESSION_STATE.json").read_text())


def write_state(root: Path, state: dict) -> None:
    (root / "session" / "SESSION_STATE.json").write_text(json.dumps(state, indent=2) + "\n")


def activate_session(root: Path, stage: str = "implementation_readiness", recommended: str = "hirmos continue") -> None:
    state = read_state(root)
    allowed_by_stage = {
        "implementation_readiness": ["hirmos continue", "hirmos status"],
        "close_ready": ["hirmos close", "hirmos status"],
        "implementation_complete": ["hirmos close", "hirmos status"],
    }
    state.update({
        "status": "active",
        "session_id": "fixture-delivery-001",
        "lifecycle_stage": stage,
        "continuation_pass": 1,
        "pending_correction": False,
        "allowed_next_commands": allowed_by_stage.get(stage, [recommended, "hirmos status"]),
        "recommended_next_command": recommended,
        "updated_at": "2026-01-01T00:00:00Z",
    })
    write_state(root, state)
    (root / "session" / "implementation-units").mkdir(exist_ok=True)


def _l834_fixture_testing_posture() -> str:
    return """
## Automated Testing Posture

- Software behavior in scope: NO
- Existing repository test architecture / commands: fixture validator only
- Unit-test posture: NOT_APPLICABLE
- New or materially changed isolated deterministic logic expected: NO
- Material behaviors requiring unit tests / isolated automated tests: NOT_APPLICABLE
- Relevant existing tests / targeted baseline: NOT_APPLICABLE
- Reproducible defect regression test expected: NOT_APPLICABLE
- Other required test layers: framework validator regression
- If NOT_APPLICABLE or COVERED_ELSEWHERE, rationale: fixture exercises HIRMOS governance rather than product software behavior
- Repository coverage policy, if any: NOT_APPLICABLE
"""


def write_basic_active_artifacts(root: Path) -> None:
    session = root / "session"
    (session / "bootstrap").mkdir(exist_ok=True)
    (session / "bootstrap" / "BOOTSTRAP_REPORT.md").write_text(_l831a_full_bootstrap())
    (session / "SESSION_SCOPE.md").write_text("# SESSION_SCOPE.md\n" + _l834_fixture_testing_posture())
    (session / "SESSION_LEDGER.md").write_text("# SESSION_LEDGER.md\n")
    (session / "unresolved-items.md").write_text("# unresolved-items.md\n")
    (session / "SESSION_SCOPE.md close verification").write_text("# SESSION_SCOPE.md close verification\n")


def write_delivery_artifacts(
    root: Path,
    *,
    include_plan: bool = True,
    include_scope: bool = True,
    use_legacy_per_delivery_plan: bool = False,
    current_state_matches: bool = True,
    close_transaction: bool = False,
    close_applied: bool = True,
    classification: str = "YES",
    phase_status: str | None = "READY_FOR_ADOPTION",
    phase_type: str = "GREENFIELD",
    entry_gate_status: str = "PASS",
    include_greenfield_controls: bool = True,
    include_brownfield_controls: bool = True,
    resulting_phase_status: str = "ACCEPTED",
    carry_forward_recorded: bool = False,
    include_acceptance_evidence: bool = True,
    include_status_report: bool = True,
    status_report_complete: bool = True,
    entry_criteria_scalar: bool = True,
    stale_post_continue_ledger: bool = False,
    delivery_plan_current_phase_none: bool = False,
) -> None:
    activate_session(root, stage="close_ready" if close_transaction else "implementation_readiness", recommended="hirmos close" if close_transaction else "hirmos continue")
    session = root / "session"
    (session / "bootstrap").mkdir(exist_ok=True)
    (session / "bootstrap" / "BOOTSTRAP_REPORT.md").write_text(_l831a_full_bootstrap())
    delivery_id = "fixture-delivery"
    plan_path = f"_hirmos/system/delivery/{delivery_id}/DELIVERY_PLAN.md" if use_legacy_per_delivery_plan else "_hirmos/system/delivery/DELIVERY_PLAN.md"
    scope_path = f"_hirmos/system/delivery/{delivery_id}/DELIVERY_SCOPE.md"
    phase_path = f"_hirmos/system/delivery/{delivery_id}/phases/PHASE-01.md"
    css_plan = plan_path if current_state_matches else "_hirmos/system/delivery/DELIVERY_PLAN.md"
    css_scope = scope_path if current_state_matches else "_hirmos/system/delivery/other-delivery/DELIVERY_SCOPE.md"
    css_phase = phase_path if current_state_matches else "_hirmos/system/delivery/other-delivery/phases/PHASE-01.md"

    acceptance_execution = ""
    acceptance_review = ""
    acceptance_phase = ""
    acceptance_update = ""
    if close_transaction and resulting_phase_status == "ACCEPTED" and include_acceptance_evidence:
        acceptance_execution = """
## Phase Acceptance Enforcement Record

Phase Acceptance Evidence Gate inspected: PASS
All adopted Session Scope items reviewed: PASS
Implementation Unit evidence complete: PASS
Greenfield acceptance evidence complete when applicable: PASS
Brownfield acceptance evidence complete when applicable: PASS
Delivery Plan / Phase / Current System State updates prepared: PASS
"""
        gf_value = "COMPLETE" if phase_type in {"GREENFIELD", "MIXED"} else "NOT_APPLICABLE"
        bf_value = "COMPLETE" if phase_type in {"BROWNFIELD", "MIXED"} else "NOT_APPLICABLE"
        acceptance_review = f"""
## Phase Acceptance Review

Phase acceptance verdict: ACCEPTED
Phase acceptance evidence status: COMPLETE
All adopted Session Scope items satisfied or explicitly deferred/excluded: yes
All implementation units reviewed: yes
Unresolved adopted work remaining: no
Greenfield acceptance evidence complete when applicable: yes
Brownfield acceptance evidence complete when applicable: yes
Acceptance decision can update durable phase to ACCEPTED: yes
"""
        acceptance_phase = f"""
## Phase Acceptance Evidence Gate

Acceptance gate status: PASS
Phase acceptance evidence status: COMPLETE
All exit criteria satisfied or explicitly deferred/excluded: yes
Session Scope close verification review acceptance verdict: ACCEPTED
Implementation Unit evidence complete: yes
Unresolved adopted work remaining: no
Delivery Plan status updated: yes
Current System State pointers refreshed: yes

### Greenfield Acceptance Evidence

Greenfield acceptance evidence: {gf_value}
MVP slice verified against phase objective: yes
Architecture-to-implementation claims reconciled: yes
Prototype-vs-production claims controlled: yes
Known gaps carried forward or explicitly deferred: yes

### Brownfield Acceptance Evidence

Brownfield acceptance evidence: {bf_value}
Preservation evidence complete: yes
Affected surfaces reviewed: yes
Regression-sensitive behavior reviewed: yes
Compatibility/data-safety constraints reviewed: yes
Do-not-touch boundaries respected: yes
"""
        acceptance_update = f"""
## Phase Acceptance Transaction

Phase acceptance status: ACCEPTED
Phase acceptance evidence status: COMPLETE
Adopted phase path: {phase_path}
Delivery Plan status update applied: yes
Durable Phase status update applied: yes
CURRENT_SYSTEM_STATE.md delivery pointers refreshed: yes
Remaining adopted work: NONE
Greenfield acceptance evidence: {gf_value}
Brownfield acceptance evidence: {bf_value}
"""

    (session / "SESSION_SCOPE.md").write_text(f"""# SESSION_SCOPE.md

## Delivery Shape Decision

What is the smallest sufficient governed delivery shape for this request?
Answer: {classification}
Evidence: fixture evidence.
Decision factors: fixture factors.
Single-session safety justification: not applicable when YES.

## Active Durable Phase Adoption

Adoption status: ADOPTED
Delivery roadmap path: {plan_path}
Delivery scope path: {scope_path}
Active phase path: {phase_path}

## Phase Entry Gate Evidence

Phase Entry Gate status: {entry_gate_status}
Lifecycle status supports adoption: YES
Phase type supports implementation: YES
Entry criteria satisfied: YES
Type-specific entry controls satisfied: YES
Pointer concordance satisfied: YES
Blocking open items absent or resolved: YES
""" + _l834_fixture_testing_posture())
    cf_review_answer = "YES" if carry_forward_recorded or resulting_phase_status == "ACCEPTED" else "NO"
    if include_status_report:
        status_report = f"""
## Phase Lifecycle Status Report Record

Phase lifecycle status: {phase_status or 'UNKNOWN'}
Phase type: {phase_type}
Phase Entry Gate status: {entry_gate_status}
Phase Progress Pointer Index status: REVIEWED
Carry-forward status: {"RECORDED" if carry_forward_recorded else "NOT_APPLICABLE"}
Phase Acceptance Evidence Gate status: {"PASS" if include_acceptance_evidence else "MISSING"}
Greenfield status group: {"COMPLETE" if phase_type in {"GREENFIELD", "MIXED"} and include_greenfield_controls else "NOT_APPLICABLE"}
Brownfield status group: {"COMPLETE" if phase_type in {"BROWNFIELD", "MIXED"} and include_brownfield_controls else "NOT_APPLICABLE"}
Status Blocked By Phase Lifecycle Conflict: NO
Exactly one recommended next command: {"hirmos close" if close_transaction else "hirmos continue"}
"""
        if not status_report_complete:
            status_report = """
## Phase Lifecycle Status Report Record

Phase lifecycle status:
Phase type:
Phase Entry Gate status:
Phase Acceptance Evidence Gate status:
Exactly one recommended next command:
"""
    else:
        status_report = ""

    phase_route_status = "PENDING" if stale_post_continue_ledger else "COMPLETED"
    session_route_status = "PENDING" if stale_post_continue_ledger else "COMPLETED"
    phase_concordance_status = "NOT_APPLICABLE" if stale_post_continue_ledger else "SATISFIED"
    session_concordance_status = "NOT_APPLICABLE" if stale_post_continue_ledger else "SATISFIED"
    (session / "SESSION_LEDGER.md").write_text(f"""# SESSION_LEDGER.md

## Continuation Pass Register

| Pass | Command | Pass type | Scope effect | SESSION_SCOPE.md impact | Artifacts updated | Evidence pointer | Result | Next governed command |
|---:|---|---|---|---|---|---|---|---|
| 1 | hirmos continue | {"CLOSE_PREPARATION" if close_transaction else "VALIDATION_ONLY"} | NONE | NO_SCOPE_CHANGE | fixture governance artifacts | SESSION_LEDGER.md | PASS | {"hirmos close" if close_transaction else "hirmos continue"} |

## Focus-Aware Capability Routing Log

| Capability | Expected durable/session output | Status | Evidence path | Notes |
|---|---|---|---|---|
| delivery-baseline | `_hirmos/system/delivery/DELIVERY_PLAN.md` and `<delivery-id>/DELIVERY_SCOPE.md` | COMPLETED | {scope_path} | fixture |
| phase-baseline | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` when phase files are selected | {phase_route_status} | {phase_path} | fixture |
| session-scope | `_hirmos/session/SESSION_SCOPE.md` adopts and narrows active delivery/phase authority | {session_route_status} | `_hirmos/session/SESSION_SCOPE.md` | fixture |
| implementation-readiness | `SESSION_SCOPE.md` authorizes implementation and required controls are satisfied | READY_FOR_REVIEW | `_hirmos/session/SESSION_SCOPE.md` | fixture |

## Current System State Delivery Pointer Concordance

| Check | Result | Evidence | Notes |
|---|---|---|---|
| Current System State delivery pointers read | SATISFIED | `_hirmos/system/accepted-state/CURRENT_SYSTEM_STATE.md` | fixture |
| Delivery roadmap pointer exists when required | SATISFIED | `_hirmos/system/delivery/DELIVERY_PLAN.md` | fixture |
| Delivery scope pointer exists when required | SATISFIED | `_hirmos/system/delivery/<delivery-id>/DELIVERY_SCOPE.md` | fixture |
| Active Phase pointer exists when required | {phase_concordance_status} | `_hirmos/system/delivery/<delivery-id>/phases/PHASE-xx.md` | fixture |
| Session Scope adopts the same delivery/phase authority | {session_concordance_status} | `SESSION_SCOPE.md` | fixture |
| Next phase / next command concordance checked | SATISFIED | `DELIVERY_PLAN.md`, `SESSION_STATE.json` | fixture |

## Durable Phase Adoption Gate
Gate status: PASS

## Phase Entry Gate Execution Log
Entry criteria status: SATISFIED
Implementation readiness authorized: YES

## Phase Progress / Carry-Forward Record
Adopted phase progress reviewed: PASS
Carry-forward obligations recorded: PASS

## PROD-L8.31 Generated-Run Mechanical Gate Record
Active generated-artifact validation result: PASS
Planned IU count matches actual full IU files: YES
Mechanical gate decision: PASS

{status_report}
{acceptance_execution}
""")
    (session / "unresolved-items.md").write_text("# unresolved-items.md\n")
    (session / "SESSION_SCOPE.md").write_text((session / "SESSION_SCOPE.md").read_text() + f"\n\n## Phase Entry Gate Review\nWas the Phase Entry Gate status PASS? YES\n\n## Phase Progress / Carry-Forward Review\nDid the session update or verify the durable Phase Progress Pointer Index? YES\nIf phase outcome is not ACCEPTED, are carry-forward obligations recorded? {cf_review_answer}\n{acceptance_review}\n")

    delivery_root = root / "system" / "delivery"
    delivery_dir = delivery_root / delivery_id
    (delivery_dir / "phases").mkdir(parents=True, exist_ok=True)
    if include_plan:
        if use_legacy_per_delivery_plan:
            (delivery_dir / "DELIVERY_PLAN.md").write_text("# DELIVERY_PLAN.md\n\n## Legacy per-delivery plan\n")
        else:
            current_phase_value = "none" if delivery_plan_current_phase_none else phase_path
            (delivery_root / "DELIVERY_PLAN.md").write_text(f"# DELIVERY_PLAN.md\n\n## Delivery Index\n\n## Delivery Status Pointer Index\n\n## Active Development Context\n\n- Active delivery: {delivery_id}\n- Active delivery scope: {scope_path}\n- Current phase: {current_phase_value}\n- Next recommended delivery: none\n- Next recommended delivery scope: none\n- Next recommended phase: none\n")
    if include_scope:
        (delivery_dir / "DELIVERY_SCOPE.md").write_text("# DELIVERY_SCOPE.md\n\n## Delivery Close Verification\n\n## Session Adoption Rules\n")

    lifecycle_line = f"Lifecycle status: {phase_status}\n" if phase_status is not None else ""
    greenfield_controls = """
## Greenfield Controls

MVP boundary: defined fixture MVP boundary.
Primary user/workflow slice: defined fixture slice.
Prototype vs production intent: production-intent fixture.
Architecture dependency status: resolved enough for this phase.
Out-of-scope expansion guard: defined fixture guard.
Validation level required: fixture validation.
Production-readiness claim allowed: PARTIAL
""" if include_greenfield_controls else """
## Greenfield Controls

MVP boundary:
Primary user/workflow slice:
Architecture dependency status:
Out-of-scope expansion guard:
"""
    cf_row = "| fixture remaining item | PARTIAL | continue in PHASE-02 | _hirmos/system/delivery/fixture-delivery/phases/PHASE-02.md | no | fixture |" if carry_forward_recorded else "| | | | | | |"

    brownfield_controls = """
## Brownfield Controls

Preservation baseline: defined fixture baseline.
Affected existing surfaces: defined fixture surfaces.
Regression-sensitive behavior: defined fixture behavior.
Do-not-touch boundaries: defined fixture boundaries.
Compatibility constraints: defined fixture compatibility.
Data/migration safety constraints: defined fixture data safety.
Rollback/recovery considerations: defined fixture rollback.
Regression evidence required: defined fixture regression evidence.
""" if include_brownfield_controls else """
## Brownfield Controls

Preservation baseline:
Affected existing surfaces:
Regression-sensitive behavior:
Do-not-touch boundaries:
"""
    (delivery_dir / "phases" / "PHASE-01.md").write_text(f"""# PHASE-01.md

{lifecycle_line}Phase type: {phase_type}

## Phase Entry Gate

Entry gate status: {entry_gate_status}
{("Entry criteria status: SATISFIED" if entry_criteria_scalar else "| Entry criteria | Delivery baseline accepted | SATISFIED |")}

{greenfield_controls}
{brownfield_controls}

## Phase Acceptance Review
{acceptance_phase}
## Phase Progress Pointer Index

| Session/archive | Scope/result pointer | Evidence pointer | Remaining-work pointer | Status impact |
|---|---|---|---|---|
| fixture-session | `_hirmos/session/SESSION_SCOPE.md` | `_hirmos/session/SESSION_LEDGER.md` | {"_hirmos/system/delivery/fixture-delivery/phases/PHASE-02.md" if carry_forward_recorded else "none"} | {resulting_phase_status} |

## Carry-Forward Enforcement

Carry-forward status: {"RECORDED" if carry_forward_recorded else "NOT_APPLICABLE"}

| Remaining item | Classification | Required next action | Carry-forward target | Blocking? | Owner/source |
|---|---|---|---|---:|---|
{cf_row}
""")

    css_file = root / "system" / "accepted-state" / "CURRENT_SYSTEM_STATE.md"
    css_existing = css_file.read_text(errors="ignore")
    css_file.write_text(css_existing + f"""

## Active Development Context and Delivery Pointers - Fixture

Delivery governance active: YES
Active delivery ID: {delivery_id}
Delivery roadmap: {css_plan}
Active delivery scope: {css_scope}
Active phase: {css_phase}
Active phase lifecycle status: {phase_status or 'UNKNOWN'}
Active phase type: {phase_type}
Last accepted phase: none
Last accepted session/archive: none
Next recommended phase: _hirmos/system/delivery/fixture-delivery/phases/PHASE-02.md
Next governed command: hirmos continue
""")

    if close_transaction:
        status = "DELIVERY_STATUS_UPDATE_APPLIED" if close_applied else "DELIVERY_STATUS_PENDING"
        cf_status = "RECORDED" if carry_forward_recorded else "NOT_APPLICABLE"
        cf_target = "_hirmos/system/delivery/fixture-delivery/phases/PHASE-02.md" if carry_forward_recorded else ""
        (session / "SESSION_LEDGER.md").write_text((session / "SESSION_LEDGER.md").read_text() + f"""

## Close-Time Delivery / Phase Status Transaction

Transaction status: {status}
Delivery roadmap path: {plan_path}
Delivery scope path: {scope_path}
Active phase path: {phase_path}
New lifecycle status: {resulting_phase_status}

## Phase Progress / Carry-Forward Transaction

Resulting phase lifecycle status: {resulting_phase_status}
Carry-forward required: {"yes" if resulting_phase_status in {"PARTIAL", "BLOCKED", "DEFERRED"} else "no"}
Carry-forward status: {cf_status}
Carry-forward target: {cf_target}
{acceptance_update}
""")

def mutate_none(root: Path) -> None:
    return None


def mutate_idle_stale_scope(root: Path) -> None:
    (root / "session" / "SESSION_SCOPE.md").write_text("# stale scope\n")


def mutate_active_missing_unresolved_items(root: Path) -> None:
    activate_session(root)
    session = root / "session"
    for filename in ["SESSION_SCOPE.md", "SESSION_LEDGER.md"]:
        (session / filename).write_text(f"# {filename}\n")
    # Deliberately omit unresolved-items.md.


def mutate_unsupported_legacy_command(root: Path) -> None:
    state = read_state(root)
    state["allowed_next_commands"] = ["hirmos build"]
    state["recommended_next_command"] = "hirmos build"
    write_state(root, state)


def mutate_readiness_wrong_recommendation(root: Path) -> None:
    state = read_state(root)
    state.update({
        "status": "active",
        "session_id": "fixture-active-002",
        "lifecycle_stage": "implementation_readiness",
        "allowed_next_commands": ["hirmos close", "hirmos status"],
        "recommended_next_command": "hirmos close",
    })
    write_state(root, state)


def mutate_delivery_governed_active_readiness(root: Path) -> None:
    write_delivery_artifacts(root)


def mutate_single_session_not_applicable_readiness(root: Path) -> None:
    activate_session(root, stage="implementation_readiness", recommended="hirmos continue")
    session = root / "session"
    (session / "bootstrap").mkdir(exist_ok=True)
    (session / "bootstrap" / "BOOTSTRAP_REPORT.md").write_text(_l831a_full_bootstrap())
    (session / "SESSION_SCOPE.md").write_text("""# SESSION_SCOPE.md

## Delivery Shape Decision

Delivery governance active: NOT_APPLICABLE
Selected delivery shape: SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS
Single-session safety justification: fixture bounded scope.
""" + _l834_fixture_testing_posture())
    (session / "SESSION_LEDGER.md").write_text("# SESSION_LEDGER.md\n\n## Runtime Route Record\nSelected route: SINGLE_SESSION_WITH_IMPLEMENTATION_UNITS\n\n## Continuation Pass Register\n\n| Pass | Command | Type | Result |\n|---:|---|---|---|\n| 1 | hirmos continue | VALIDATION_ONLY | PASS |\n")
    (session / "unresolved-items.md").write_text("# unresolved-items.md\n")


def mutate_delivery_missing_delivery_scope(root: Path) -> None:
    write_delivery_artifacts(root, include_scope=False)


def mutate_delivery_legacy_per_delivery_plan_path(root: Path) -> None:
    write_delivery_artifacts(root, use_legacy_per_delivery_plan=True)


def mutate_phase_entry_gate_valid_brownfield(root: Path) -> None:
    write_delivery_artifacts(root, phase_type="BROWNFIELD")


def mutate_phase_entry_gate_valid_mixed(root: Path) -> None:
    write_delivery_artifacts(root, phase_type="MIXED")


def mutate_phase_status_report_missing_required_fields(root: Path) -> None:
    write_delivery_artifacts(root, status_report_complete=False)


def mutate_phase_status_report_complete(root: Path) -> None:
    write_delivery_artifacts(root, status_report_complete=True)


def mutate_delivery_missing_durable_plan(root: Path) -> None:
    write_delivery_artifacts(root, include_plan=False)


def mutate_delivery_uncertain_at_readiness(root: Path) -> None:
    write_delivery_artifacts(root, classification="UNCERTAIN")


def mutate_delivery_pointer_mismatch(root: Path) -> None:
    write_delivery_artifacts(root, current_state_matches=False)


def mutate_delivery_close_missing_status_transaction(root: Path) -> None:
    write_delivery_artifacts(root)
    activate_session(root, stage="close_ready", recommended="hirmos close")


def mutate_delivery_close_applied_status(root: Path) -> None:
    write_delivery_artifacts(root, close_transaction=True, close_applied=True)




def mutate_phase_partial_close_missing_carry_forward(root: Path) -> None:
    write_delivery_artifacts(root, close_transaction=True, close_applied=True, resulting_phase_status="PARTIAL", carry_forward_recorded=False)


def mutate_phase_partial_close_with_carry_forward(root: Path) -> None:
    write_delivery_artifacts(root, close_transaction=True, close_applied=True, resulting_phase_status="PARTIAL", carry_forward_recorded=True)



def mutate_phase_accepted_missing_acceptance_evidence(root: Path) -> None:
    write_delivery_artifacts(root, close_transaction=True, close_applied=True, resulting_phase_status="ACCEPTED", include_acceptance_evidence=False)


def mutate_phase_accepted_with_acceptance_evidence(root: Path) -> None:
    write_delivery_artifacts(root, close_transaction=True, close_applied=True, resulting_phase_status="ACCEPTED", include_acceptance_evidence=True)

def mutate_phase_missing_lifecycle_status(root: Path) -> None:
    write_delivery_artifacts(root, phase_status=None)


def mutate_phase_blocked_lifecycle_status(root: Path) -> None:
    write_delivery_artifacts(root, phase_status="BLOCKED")


def mutate_phase_unknown_type(root: Path) -> None:
    write_delivery_artifacts(root, phase_type="UNKNOWN")


def mutate_greenfield_missing_mvp_boundary(root: Path) -> None:
    write_delivery_artifacts(root, phase_type="GREENFIELD", include_greenfield_controls=False)


def mutate_brownfield_missing_preservation_baseline(root: Path) -> None:
    write_delivery_artifacts(root, phase_type="BROWNFIELD", include_brownfield_controls=False)


def mutate_mixed_missing_brownfield_controls(root: Path) -> None:
    write_delivery_artifacts(root, phase_type="MIXED", include_brownfield_controls=False)


def mutate_legacy_capability_entrypoint_wrapper(root: Path) -> None:
    wrapper = root / "extensions" / "design-agent" / "capabilities" / "session-scope" / "entrypoint.md"
    wrapper.write_text("# legacy wrapper\n\nThis capability entrypoint has moved to `entrypoints/default.md`.\n")


def mutate_accepted_state_legacy_per_delivery_plan_pointer(root: Path) -> None:
    css = root / "system" / "accepted-state" / "CURRENT_SYSTEM_STATE.md"
    body = css.read_text()
    body += "\nLegacy bad pointer: _hirmos/system/delivery/fixture-delivery/DELIVERY_PLAN.md\n"
    css.write_text(body)


def mutate_archive_manifest_missing_normalization(root: Path) -> None:
    manifest = root / "core" / "templates" / "system" / "history" / "sessions" / "ARCHIVE_MANIFEST.md"
    body = manifest.read_text()
    body = body.replace("## 6. Archived Session State Normalization", "## 6. Archived State")
    manifest.write_text(body)



def mutate_delivery_baseline_without_session_scope_passes(root: Path) -> None:
    state = read_state(root)
    state.update({
        "status": "active",
        "session_id": "fixture-delivery-baseline-001",
        "session_focus": "delivery_baseline",
        "lifecycle_stage": "design",
        "active_authority": "_hirmos/system/delivery/fixture-delivery/DELIVERY_SCOPE.md",
        "active_delivery_id": "fixture-delivery",
        "active_delivery_scope": "_hirmos/system/delivery/fixture-delivery/DELIVERY_SCOPE.md",
        "active_phase": None,
        "continuation_pass": 0,
        "pending_correction": False,
        "allowed_next_commands": ["hirmos continue", "hirmos status"],
        "recommended_next_command": "hirmos continue",
        "updated_at": "2026-01-01T00:00:00Z",
    })
    write_state(root, state)
    session = root / "session"
    (session / "bootstrap").mkdir(exist_ok=True)
    (session / "bootstrap" / "BOOTSTRAP_REPORT.md").write_text(_l831a_full_bootstrap())
    for rel in ["SESSION_SCOPE.md", "unresolved-items.md"]:
        p = session / rel
        if p.exists():
            p.unlink()
    (session / "SESSION_LEDGER.md").write_text("# SESSION_LEDGER.md\n\nCurrent focus: delivery_baseline\nActive authority: _hirmos/system/delivery/fixture-delivery/DELIVERY_SCOPE.md\nCheckpoint: Delivery Baseline — Review or Change\n")
    delivery = root / "system" / "delivery" / "fixture-delivery"
    delivery.mkdir(parents=True, exist_ok=True)
    (root / "system" / "delivery" / "DELIVERY_PLAN.md").write_text("# DELIVERY_PLAN.md\n\nDelivery Index\n")
    (delivery / "DELIVERY_SCOPE.md").write_text("# DELIVERY_SCOPE.md\n\nStatus: READY_FOR_BASELINE_REVIEW\n\n## Phase Plan / Phase Coverage Plan\n\n| Phase | Purpose | Delivery requirements covered | Design areas covered | Production gates covered | Entry condition | Exit condition | Status | Phase file |\n|---|---|---|---|---|---|---|---|---|\n| PHASE-01 | Test | REQ-01 | DD-01 | Gate | Accepted delivery baseline | Done | planned | not instantiated |\n\n## Delivery Coverage Self-Check\n\n- All in-scope delivery requirements assigned to one or more phases: YES\n- All required design/engineering decisions assigned to one or more phases: YES\n- All production-shaped gates assigned to delivery-level or phase-level evidence: YES\n- No future concrete `PHASE-xx.md` paths referenced unless the files exist: YES\n")
    (delivery / "unresolved-items.md").write_text("# Delivery Unresolved Items\n\n## Current Checkpoint Feed\n\n### Gated delivery items\n\nNone.\n\n### Non-gating delivery assumptions\n\nNone.\n\n### Technical-review delivery items\n\nNone.\n")


def mutate_delivery_baseline_with_session_scope_fails(root: Path) -> None:
    mutate_delivery_baseline_without_session_scope_passes(root)
    (root / "session" / "SESSION_SCOPE.md").write_text("# SESSION_SCOPE.md\n\nThis should not exist during delivery_baseline focus.\n")


def mutate_delivery_baseline_with_session_unresolved_fails(root: Path) -> None:
    mutate_delivery_baseline_without_session_scope_passes(root)
    (root / "session" / "unresolved-items.md").write_text("# unresolved-items.md\n\nDelivery-level unresolved items were incorrectly stored here.\n")


def mutate_delivery_baseline_with_session_requirements_fails(root: Path) -> None:
    mutate_delivery_baseline_without_session_scope_passes(root)
    (root / "session" / "REQUIREMENTS.md").write_text("# REQUIREMENTS.md\n\nDelivery-level requirements were incorrectly stored in the session surface.\n")


def mutate_delivery_baseline_with_session_design_fails(root: Path) -> None:
    mutate_delivery_baseline_without_session_scope_passes(root)
    (root / "session" / "DESIGN.md").write_text("# DESIGN.md\n\nDelivery-level design was incorrectly stored in the session surface.\n")


def mutate_delivery_baseline_with_delivery_optional_authority_passes(root: Path) -> None:
    mutate_delivery_baseline_without_session_scope_passes(root)
    delivery = root / "system" / "delivery" / "fixture-delivery"
    (delivery / "REQUIREMENTS.md").write_text("# REQUIREMENTS.md\n\nStatus: delivery-level optional requirements authority.\n")
    (delivery / "DESIGN.md").write_text("# DESIGN.md\n\nStatus: delivery-level optional design authority.\n")


def mutate_phase_entry_gate_table_only_fails(root: Path) -> None:
    write_delivery_artifacts(root, entry_criteria_scalar=False)


def mutate_phase_session_baseline_fresh_ledger_passes(root: Path) -> None:
    write_delivery_artifacts(root, stale_post_continue_ledger=False, delivery_plan_current_phase_none=False)
    state = read_state(root)
    state["session_focus"] = "phase_session_baseline"
    state["active_phase"] = "_hirmos/system/delivery/fixture-delivery/phases/PHASE-01.md"
    write_state(root, state)


def mutate_phase_session_baseline_stale_routing_log_fails(root: Path) -> None:
    write_delivery_artifacts(root, stale_post_continue_ledger=True, delivery_plan_current_phase_none=False)
    state = read_state(root)
    state["session_focus"] = "phase_session_baseline"
    state["active_phase"] = "_hirmos/system/delivery/fixture-delivery/phases/PHASE-01.md"
    write_state(root, state)


def mutate_phase_session_baseline_stale_delivery_plan_current_phase_fails(root: Path) -> None:
    write_delivery_artifacts(root, stale_post_continue_ledger=False, delivery_plan_current_phase_none=True)
    state = read_state(root)
    state["session_focus"] = "phase_session_baseline"
    state["active_phase"] = "_hirmos/system/delivery/fixture-delivery/phases/PHASE-01.md"
    write_state(root, state)


def mutate_delivery_baseline_active_wording_fails(root: Path) -> None:
    mutate_delivery_baseline_without_session_scope_passes(root)
    (root / "system" / "delivery" / "DELIVERY_PLAN.md").write_text("""# DELIVERY_PLAN.md

Status: READY_FOR_BASELINE_REVIEW

## Active Delivery

- Active delivery ID: fixture-delivery
- Active delivery scope: _hirmos/system/delivery/fixture-delivery/DELIVERY_SCOPE.md
""")


def mutate_root_accepted_requirements_without_governance_fails(root: Path) -> None:
    (root / "system" / "accepted-state" / "REQUIREMENTS.md").write_text("# REQUIREMENTS.md\n\nStatus: accepted requirements catalog.\n")


def mutate_root_accepted_requirements_with_governance_passes(root: Path) -> None:
    (root / "system" / "accepted-state" / "REQUIREMENTS.md").write_text("# REQUIREMENTS.md\n\nCumulative accepted requirements governance: ACTIVE\n\nStatus: explicitly governed cumulative accepted requirements baseline.\n")



def _write_generated_history_session(root: Path, *, checkpoint: bool = True, thin_iu: bool = False, null_timestamps: bool = False, no_iu: bool = False) -> Path:
    sess = root / "system" / "history" / "sessions" / "2026-01-01-iu-fixture"
    iu_dir = sess / "implementation-units"
    iu_dir.mkdir(parents=True, exist_ok=True)
    state = {
        "schema_version": "session-state-v1",
        "status": "archived",
        "session_id": "2026-01-01-iu-fixture",
        "lifecycle_stage": "implementation_complete",
        "created_at": None if null_timestamps else "2026-01-01T00:00:00Z",
        "updated_at": None if null_timestamps else "2026-01-01T00:10:00Z",
        "run_context": None if null_timestamps else {"run_started_at_utc": "2026-01-01T00:00:00Z", "source": "fixture"},
    }
    (sess / "SESSION_STATE.json").write_text(json.dumps(state, indent=2) + "\n")
    if checkpoint:
        (sess / "SESSION_LEDGER.md").write_text("""# SESSION_LEDGER.md

## PROD-L8.24 Pre-Execution Ledger Enforcement

### Pre-Material-Edit Ledger Row
Timestamp: 2026-01-01T00:01:00Z
Active session id: 2026-01-01-iu-fixture
Source phase/session authority: SESSION_SCOPE.md SR-01
IU files verified: implementation-units/IU-01.md
IU Set Authority Checkpoint present: YES
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU_EXECUTION_AUTHORIZED: PASS
Active gate validator result: PASS
Active generated-artifact validation result: PASS
Material implementation started: NO
First material-edit command/event: NOT_STARTED
Retrospective checkpoint or IU expansion: NO
Evidence path(s): SESSION_LEDGER.md, implementation-units/IU-01.md

## PROD-L8.21 IU Set Authority Checkpoint
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU files created before material edits: YES
Non-placeholder IU review: PASS
IU Set Coverage Map
| Source scope item | Source artifact | IU file(s) | Coverage status | Notes |
|---|---|---|---|---|
| SR-01 | SESSION_SCOPE.md | IU-01.md | COVERED | fixture |

## Material Edit Start Record
Timestamp: 2026-01-01T00:02:00Z
Command/trigger: fixture implementation
Files/areas about to be edited: app/fixture.ts
Authorization pointer: Pre-Material-Edit Ledger Row
""")
    else:
        (sess / "SESSION_LEDGER.md").write_text("# SESSION_LEDGER.md\n\nImplementation completed.\n")
    if no_iu:
        return sess
    if thin_iu:
        (iu_dir / "IU-01.md").write_text("# IU-01\nStatus: complete\nObjective: fixture\nPre-Execution: IU created before code changes — YES\n")
    else:
        (iu_dir / "IU-01.md").write_text("""# IU-01 — Fixture Implementation Unit

## 1. Unit Identity
- Unit ID: IU-01
- Objective source: fixture
- Source Scope item(s): SR-01

## 2. Unit Scope
### Objective
Implement fixture behavior.
### Context
Fixture context.
### In Scope
- Fixture file change.
### Out of Scope
- Unrelated work.
### Files / Areas
- app/fixture.ts
### Preservation Rules
- Preserve fixture boundaries.
### Implementation Requirements
- Implement the requested fixture behavior.
### Automated Testing Posture
- Unit-test posture: NOT_APPLICABLE
- Existing repository test framework / conventions: fixture-only validator regression
- If NOT_APPLICABLE or COVERED_ELSEWHERE, rationale: framework validator fixture has no product behavior
### Verification Commands / Checks
- fixture check
### Evidence Requirements
- fixture evidence
### Runtime Integration Posture
| Area | Authorized posture | Allowed fallback | Required environment/config | Evidence required |
|---|---|---|---|---|
| fixture | boundary | none | none | command output |
### Binary Acceptance Criteria
| Criterion | Evidence required | Pass/Fail basis |
|---|---|---|
| fixture works | command output | pass/fail |

## 3. Pre-Execution Checks
| Check | Result | Evidence / notes |
|---|---|---|
| Unit authority record is non-placeholder | YES | fixture |
| Failure / route-back condition recorded | YES | route back if fixture check fails |

## 4. Execution Record
### Failure / route-back condition
Route back if required fixture verification fails.
### Actions Performed
Pending.
""")
    return sess


def mutate_generated_iu_session_missing_checkpoint_fails(root: Path) -> None:
    _write_generated_history_session(root, checkpoint=False, thin_iu=False)


def mutate_generated_iu_session_thin_iu_fails(root: Path) -> None:
    _write_generated_history_session(root, checkpoint=True, thin_iu=True)


def mutate_generated_archived_session_null_timestamps_fails(root: Path) -> None:
    _write_generated_history_session(root, checkpoint=True, thin_iu=False, null_timestamps=True, no_iu=True)



def mutate_generated_iu_session_retrospective_cleanup_fails(root: Path) -> None:
    sess = _write_generated_history_session(root, checkpoint=True, thin_iu=False)
    p = sess / "SESSION_LEDGER.md"
    p.write_text(p.read_text() + "\n## Close Cleanup\nAdding the required IU authority checkpoint to satisfy the validator.\n")


def mutate_generated_phase_missing_review_gate_fails(root: Path) -> None:
    phase = root / "system" / "delivery" / "fixture-delivery" / "phases" / "PHASE-01.md"
    phase.parent.mkdir(parents=True, exist_ok=True)
    phase.write_text("""# PHASE-01
Lifecycle status: ACCEPTED

## Binary Exit Criteria
| Criterion | Status |
|---|---|
| fixture | PASS |
""")


def mutate_generated_current_state_placeholder_row_fails(root: Path) -> None:
    css = root / "system" / "accepted-state" / "CURRENT_SYSTEM_STATE.md"
    css.write_text(css.read_text() + """

## 6. Source Artifact Index
| Source class | Source path | Status | Notes |
|---|---|---|---|
| | delivery / session / archive / generated synthesis | active / accepted / archived / superseded / not source authority | |
""")



# PROD-L8.31A generated-run mechanical gate fixture helpers

def _l831a_full_bootstrap() -> str:
    lines = ["# BOOTSTRAP_REPORT.md", "", "## Bootstrap Discipline Answers", ""]
    for i in range(1, 17):
        lines += [
            f"Q{i} — Fixture bootstrap question {i}",
            "Answer: Fixture answer written again for this session from durable sources.",
            "Source: _hirmos/core/bootstrap.md; _hirmos/session/SESSION_STATE.json",
            "Answer basis: ANSWERED_FROM_CURRENT_AND_CORE_SOURCES",
            "",
        ]
    return "\n".join(lines) + "\n"


def _l831a_write_generated_session(root: Path, name: str = "2026-01-02-l831a-fixture", *, bootstrap: str | None = None, scope: str = "", execution: str = "", iu_bodies: list[str] | None = None) -> Path:
    sess = root / "system" / "history" / "sessions" / name
    (sess / "bootstrap").mkdir(parents=True, exist_ok=True)
    (sess / "implementation-units").mkdir(parents=True, exist_ok=True)
    (sess / "SESSION_STATE.json").write_text(json.dumps({
        "schema_version": "session-state-v1",
        "status": "archived",
        "session_id": name,
        "lifecycle_stage": "implementation_complete" if "implementation_complete" in execution.lower() else "implementation_readiness",
        "created_at": "2026-01-02T00:00:00Z",
        "updated_at": "2026-01-02T00:10:00Z",
        "run_context": {"run_started_at_utc": "2026-01-02T00:00:00Z", "source": "fixture"},
    }, indent=2) + "\n")
    (sess / "bootstrap" / "BOOTSTRAP_REPORT.md").write_text(bootstrap if bootstrap is not None else _l831a_full_bootstrap())
    (sess / "SESSION_SCOPE.md").write_text(scope or "# SESSION_SCOPE.md\n")
    (sess / "SESSION_LEDGER.md").write_text(execution or "# SESSION_LEDGER.md\n")
    if iu_bodies:
        for idx, body in enumerate(iu_bodies, 1):
            (sess / "implementation-units" / f"IU-{idx:02d}.md").write_text(body)
    return sess


def _l831a_incomplete_bootstrap() -> str:
    return """# BOOTSTRAP_REPORT.md

## Bootstrap Discipline Answers

Q1 — Only one answer
Answer: incomplete fixture answer.
Source: _hirmos/core/bootstrap.md
Answer basis: ANSWERED_FROM_CORE_PROTOCOLS
"""


def _l831a_thin_iu() -> str:
    return """# IU-01
Status: complete
Objective: thin fixture
Contract sealed before material edits: YES
"""



def _l832k_full_iu() -> str:
    sections = [
        "# IU-01 — L8.32K Fixture Implementation Unit",
        "",
        "## PROD-L8.21 Minimum IU Contract",
        "",
        "## Unit Identity / Contract Metadata",
        "- Unit ID: IU-01",
        "- Contract sealed before material edits: YES",
        "",
        "## Unit Scope / Authority",
        "### Objective",
        "Implement the L8.32K fixture behavior.",
        "### Source Scope",
        "- SR-01 from SESSION_SCOPE.md",
        "### In Scope",
        "- Fixture implementation only.",
        "### Out of Scope",
        "- Any unrelated behavior.",
        "### Files / Areas",
        "- app/fixture.ts",
        "",
        "## Implementation Requirements",
        "- Implement fixture behavior exactly.",
        "- Preserve route-back conditions.",
        "",
        "## Automated Testing Posture",
        "- Unit-test posture: NOT_APPLICABLE",
        "- Existing repository test framework / conventions: fixture-only validator regression",
        "- If NOT_APPLICABLE or COVERED_ELSEWHERE, rationale: framework validator fixture has no product behavior",
        "",
        "## Verification Commands / Checks",
        "- fixture verification check",
        "",
        "## Evidence Requirements",
        "- Provide command output for fixture validation.",
        "",
        "## Runtime Integration Posture",
        "| Area | Authorized posture | Evidence required |",
        "|---|---|---|",
        "| fixture | local only | validator output |",
        "",
        "## Binary Acceptance Criteria",
        "| Criterion | Status | Evidence |",
        "|---|---|---|",
        "| fixture passes | PENDING | validator output |",
        "",
        "## Pre-Execution Checks",
        "| Check | Result | Evidence / notes |",
        "|---|---|---|",
        "| Full IU contract sections populated before material edits | YES | fixture |",
        "| Failure / route-back condition recorded | YES | fixture |",
        "",
        "## Execution Record",
        "### Actions Performed",
        "- Pending until IU execution is authorized.",
        "### Files / Artifacts Changed",
        "- Pending.",
        "### Validation / Checks Performed",
        "- Pending.",
        "### Claim Evidence Produced",
        "- Pending.",
        "### Execution Result",
        "- Pending.",
        "",
        "## Unit Review",
        "### Request-to-Result Review",
        "- Pending.",
        "### Validation Review",
        "- Pending.",
        "### Claim Reconciliation",
        "- Pending.",
        "### Unit Result",
        "Unit Result: PASS — Evidence: active gate validator result PASS and fixture validation output.",
        "",
        "## Retries",
        "- None.",
    ]
    for i in range(7):
        sections.append(f"LLM Write Permission: fixture permission {i+1}")
    return "\n".join(sections) + "\n"

def mutate_l831_generated_session_incomplete_bootstrap_fails(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l831a-incomplete-bootstrap",
        bootstrap=_l831a_incomplete_bootstrap(),
        execution="# SESSION_LEDGER.md\n\nStarted generated session.\n",
    )


def mutate_l831_planned_ius_no_files_fails(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l831a-planned-no-iu",
        scope="# SESSION_SCOPE.md\n\n## PROD-L8.31 Planned IU Count Gate\nImplementation units required: YES\nPlanned IU count: 3\nImplementation may begin before full IU artifacts exist: NO\n",
        execution="# SESSION_LEDGER.md\n\nIU mode / IU planned: YES\nPlanned IU count: 3\n",
    )


def mutate_l831_thin_ius_fail(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l831a-thin-ius",
        scope="# SESSION_SCOPE.md\n\n## 1. Session Identity\n\n- Scope status: ACCEPTED\n\n## 3. Authorized Scope / Outcome\n\n- Baseline acceptance authority recorded: YES\n- Material project/source edit authorization: REQUIRES_IU_EXECUTION_AUTHORIZATION\n\nImplementation units required: YES\nPlanned IU count: 1\n",
        execution="""# SESSION_LEDGER.md

## Start / Baseline Pre-Edit Gate
| Gate | Required before | Status | Authority source | Evidence pointer | Next allowed transition |
|---|---|---|---|---|---|
| BASELINE_ACCEPTED_OR_AMENDED | material project/source edits | PASS | user continuation + `SESSION_SCOPE.md` status | Continuation Pass Register | IU planning |

## Continuation Pass Register
| Pass | Command | Pass type | Scope effect | SESSION_SCOPE.md impact | Artifacts updated | Evidence pointer | Result | Next governed command |
|---:|---|---|---|---|---|---|---|---|
| 1 | hirmos continue | ACCEPTANCE_ONLY | BASELINE_ACCEPTED | BASELINE_ACCEPTED | SESSION_SCOPE.md SESSION_LEDGER.md | fixture | PASS | hirmos continue |

## PROD-L8.21 IU Set Authority Checkpoint
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU files created before material edits: YES
Non-placeholder IU review: PASS

Execution Result: PASS
Unit Review: PASS
Request-to-Result Review: PASS
Validation Review: PASS
Claim Reconciliation: PASS
Unit Result: PASS
""",
        iu_bodies=[_l831a_thin_iu()],
    )


def mutate_l831_lifecycle_claim_without_active_validation_fails(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l831a-no-active-validation",
        execution="# SESSION_LEDGER.md\n\nimplementation_complete\n\n## PROD-L8.31 Generated-Run Mechanical Gate Record\nMechanical gate decision: PASS\n",
    )


def mutate_l831_lifecycle_claim_without_mechanical_gate_fails(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l831a-no-mechanical-record",
        execution="# SESSION_LEDGER.md\n\nimplementation_complete\nActive generated-artifact validation result: PASS\n",
    )



def mutate_l832k_material_edit_before_iu_execution_authorized_fails(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l832k-material-before-auth",
        scope="# SESSION_SCOPE.md\n\nImplementation units required: YES\nPlanned IU count: 1\nImplementation may begin before full IU artifacts exist: NO\n",
        execution="""# SESSION_LEDGER.md

## PROD-L8.21 IU Set Authority Checkpoint
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU files created before material edits: YES
Non-placeholder IU review: PASS
IU Set Coverage Map
| Source scope item | Source artifact | IU file(s) | Coverage status | Notes |
|---|---|---|---|---|
| SR-01 | SESSION_SCOPE.md | IU-01.md | COVERED | fixture |

## IU Planning / IU Execution Boundary Record
| Gate | Required before | Status | Authority source | Evidence pointer | Next allowed transition |
|---|---|---|---|---|---|
| IU_PLANNING_COMPLETE | before IU plan review checkpoint | PASS | implementation-units/IU-01.md | validation PASS | pause for IU Plan Review |

## Material Edit Start Record
Timestamp: 2026-01-02T00:02:00Z
Files/areas about to be edited: app/fixture.ts
""",
        iu_bodies=[_l832k_full_iu()],
    )


def mutate_l832k_lifecycle_claim_before_iu_execution_authorized_fails(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l832k-lifecycle-before-auth",
        scope="# SESSION_SCOPE.md\n\n## 1. Session Identity\n\n- Scope status: ACCEPTED\n\n## 3. Authorized Scope / Outcome\n\n- Baseline acceptance authority recorded: YES\n- Material project/source edit authorization: REQUIRES_IU_EXECUTION_AUTHORIZATION\n\nImplementation units required: YES\nPlanned IU count: 1\n",
        execution="""# SESSION_LEDGER.md

## Start / Baseline Pre-Edit Gate
| Gate | Required before | Status | Authority source | Evidence pointer | Next allowed transition |
|---|---|---|---|---|---|
| BASELINE_ACCEPTED_OR_AMENDED | material project/source edits | PASS | user continuation + `SESSION_SCOPE.md` status | Continuation Pass Register | IU planning |

## Continuation Pass Register
| Pass | Command | Pass type | Scope effect | SESSION_SCOPE.md impact | Artifacts updated | Evidence pointer | Result | Next governed command |
|---:|---|---|---|---|---|---|---|---|
| 1 | hirmos continue | ACCEPTANCE_ONLY | BASELINE_ACCEPTED | BASELINE_ACCEPTED | SESSION_SCOPE.md SESSION_LEDGER.md | fixture | PASS | hirmos continue |

## PROD-L8.21 IU Set Authority Checkpoint
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU files created before material edits: YES
Non-placeholder IU review: PASS
IU Set Coverage Map
| Source scope item | Source artifact | IU file(s) | Coverage status | Notes |
|---|---|---|---|---|
| SR-01 | SESSION_SCOPE.md | IU-01.md | COVERED | fixture |

Active generated-artifact validation result: PASS
implementation_complete
""",
        iu_bodies=[_l832k_full_iu()],
    )


def mutate_l832k_authorized_material_transition_passes(root: Path) -> None:
    _l831a_write_generated_session(
        root,
        name="2026-01-02-l832k-authorized-transition",
        scope="# SESSION_SCOPE.md\n\n## 1. Session Identity\n\n- Scope status: ACCEPTED\n\n## 3. Authorized Scope / Outcome\n\n- Baseline acceptance authority recorded: YES\n- Material project/source edit authorization: REQUIRES_IU_EXECUTION_AUTHORIZATION\n\nImplementation units required: YES\nPlanned IU count: 1\n",
        execution="""# SESSION_LEDGER.md

## Start / Baseline Pre-Edit Gate
| Gate | Required before | Status | Authority source | Evidence pointer | Next allowed transition |
|---|---|---|---|---|---|
| BASELINE_ACCEPTED_OR_AMENDED | material project/source edits | PASS | user continuation + `SESSION_SCOPE.md` status | Continuation Pass Register | IU planning |

## Continuation Pass Register
| Pass | Command | Pass type | Scope effect | SESSION_SCOPE.md impact | Artifacts updated | Evidence pointer | Result | Next governed command |
|---:|---|---|---|---|---|---|---|---|
| 1 | hirmos continue | ACCEPTANCE_ONLY | BASELINE_ACCEPTED | BASELINE_ACCEPTED | SESSION_SCOPE.md SESSION_LEDGER.md | fixture | PASS | hirmos continue |

## PROD-L8.24 Pre-Execution Ledger Enforcement

### Pre-Material-Edit Ledger Row
Timestamp: 2026-01-02T00:01:00Z
Active session id: 2026-01-02-l832k-authorized-transition
Source phase/session authority: SESSION_SCOPE.md SR-01
IU files verified: implementation-units/IU-01.md
IU Set Authority Checkpoint present: YES
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU_EXECUTION_AUTHORIZED: PASS
Active gate validator result: PASS
Active generated-artifact validation result: PASS
Material implementation started: NO
First material-edit command/event: NOT_STARTED
Retrospective checkpoint or IU expansion: NO
Evidence path(s): SESSION_LEDGER.md, implementation-units/IU-01.md

## PROD-L8.21 IU Set Authority Checkpoint
Authorization decision: IMPLEMENTATION_AUTHORIZED
IU files created before material edits: YES
Non-placeholder IU review: PASS
IU Set Coverage Map
| Source scope item | Source artifact | IU file(s) | Coverage status | Notes |
|---|---|---|---|---|
| SR-01 | SESSION_SCOPE.md | IU-01.md | COVERED | fixture |

## PROD-L8.32K Runtime Boundary Validation Record
Command file used: _hirmos/core/commands/continue.md
Active gate validator result: PASS
IU_EXECUTION_AUTHORIZED: PASS
Material project-file edits before authorization: NO
Transition claim allowed: YES

## Material Edit Start Record
Timestamp: 2026-01-02T00:02:00Z
Command/trigger: fixture implementation
Files/areas about to be edited: app/fixture.ts
Authorization pointer: Pre-Material-Edit Ledger Row

Implementation complete

## PROD-L8.31 Generated-Run Mechanical Gate Record
Mechanical gate decision: PASS
Planned IU count matches actual full IU files: PASS
""",
        iu_bodies=[_l832k_full_iu()],
    )

def mutate_l831_approved_carry_forward_without_source_fails(root: Path) -> None:
    cf = root / "system" / "accepted-state" / "CARRY_FORWARD.md"
    cf.write_text(cf.read_text() + """

## Fixture Bad Active Carry-Forward

- CF-01
  - Disposition: APPROVED_CARRY_FORWARD
  - Approval / deferral source: TBD
""")


def mutate_l831_current_state_pointer_concordance_fails(root: Path) -> None:
    delivery = root / "system" / "delivery" / "fixture-delivery"
    delivery.mkdir(parents=True, exist_ok=True)
    (delivery / "DELIVERY_SCOPE.md").write_text("""# DELIVERY_SCOPE.md

Delivery result: CLOSED_PARTIAL
Delivery accepted: yes
""")
    css = root / "system" / "accepted-state" / "CURRENT_SYSTEM_STATE.md"
    css.write_text(css.read_text() + """

## Fixture Bad Generated Pointer
Next recommended phase: TBD
""")

# retained marker: accepted-state index reappears
CASES = [
    Case("valid baseline", mutate_none, True, "PASS:"),
    Case("L8.32K material edit before IU execution authorization fails", mutate_l832k_material_edit_before_iu_execution_authorized_fails, False, "PROD-L8.32K IU-mode material edit before IU_EXECUTION_AUTHORIZED"),
    Case("L8.32K lifecycle claim before IU execution authorization fails", mutate_l832k_lifecycle_claim_before_iu_execution_authorized_fails, False, "PROD-L8.32K IU-mode lifecycle transition claim before IU_EXECUTION_AUTHORIZED"),
    Case("L8.32K authorized material transition passes", mutate_l832k_authorized_material_transition_passes, True, "PASS:"),
    Case("idle stale SESSION_SCOPE", mutate_idle_stale_scope, False, "stale active-session"),
    Case("active missing unresolved-items", mutate_active_missing_unresolved_items, False, "missing canonical root artifact"),
    Case("unsupported legacy command", mutate_unsupported_legacy_command, False, "unsupported command"),
    Case("implementation readiness wrong recommendation", mutate_readiness_wrong_recommendation, False, "implementation_readiness"),
    Case("delivery governed active readiness passes", mutate_delivery_governed_active_readiness, True, "PASS:"),
    Case("single-session NOT_APPLICABLE readiness passes", mutate_single_session_not_applicable_readiness, True, "PASS:"),
    Case("delivery missing DELIVERY_SCOPE fails", mutate_delivery_missing_delivery_scope, False, "missing durable delivery scope"),
    Case("delivery legacy per-delivery plan path fails", mutate_delivery_legacy_per_delivery_plan_path, False, "durable roadmap/register"),
    Case("accepted-state legacy per-delivery plan pointer fails", mutate_accepted_state_legacy_per_delivery_plan_pointer, False, "legacy per-delivery plan path"),
    Case("archive manifest missing normalization fails", mutate_archive_manifest_missing_normalization, False, "Archived Session State Normalization"),
    Case("phase entry gate valid brownfield passes", mutate_phase_entry_gate_valid_brownfield, True, "PASS:"),
    Case("phase entry gate valid mixed passes", mutate_phase_entry_gate_valid_mixed, True, "PASS:"),
    Case("phase entry gate table-only evidence fails", mutate_phase_entry_gate_table_only_fails, False, "scalar evidence"),
    Case("phase session baseline fresh ledger passes", mutate_phase_session_baseline_fresh_ledger_passes, True, "PASS:"),
    Case("phase session baseline stale routing log fails", mutate_phase_session_baseline_stale_routing_log_fails, False, "routing log leaves phase-baseline PENDING"),
    Case("phase session baseline stale delivery plan current phase fails", mutate_phase_session_baseline_stale_delivery_plan_current_phase_fails, False, "Current phase as none"),
    Case("phase lifecycle status report missing fields fails", mutate_phase_status_report_missing_required_fields, False, "Phase Lifecycle Status Report"),
    Case("phase lifecycle status report complete passes", mutate_phase_status_report_complete, True, "PASS:"),
    Case("legacy capability entrypoint wrapper fails", mutate_legacy_capability_entrypoint_wrapper, False, "legacy capability entrypoint wrapper"),
    Case("delivery missing durable plan fails", mutate_delivery_missing_durable_plan, False, "missing durable plan"),
    Case("delivery uncertain at readiness fails", mutate_delivery_uncertain_at_readiness, False, "UNCERTAIN"),
    Case("delivery pointer mismatch fails", mutate_delivery_pointer_mismatch, False, "pointer mismatch"),
    Case("delivery close missing status transaction fails", mutate_delivery_close_missing_status_transaction, False, "missing status transaction"),
    Case("delivery close applied status passes", mutate_delivery_close_applied_status, True, "PASS:"),
    Case("phase partial close missing carry-forward fails", mutate_phase_partial_close_missing_carry_forward, False, "carry-forward obligations"),
    Case("phase partial close with carry-forward passes", mutate_phase_partial_close_with_carry_forward, True, "PASS:"),
    Case("phase accepted missing acceptance evidence fails", mutate_phase_accepted_missing_acceptance_evidence, False, "acceptance evidence"),
    Case("phase accepted with acceptance evidence passes", mutate_phase_accepted_with_acceptance_evidence, True, "PASS:"),
    Case("phase missing lifecycle status fails", mutate_phase_missing_lifecycle_status, False, "missing lifecycle status"),
    Case("phase blocked lifecycle status fails", mutate_phase_blocked_lifecycle_status, False, "lifecycle status"),
    Case("phase unknown type fails", mutate_phase_unknown_type, False, "UNKNOWN phase type"),
    Case("greenfield phase missing MVP boundary fails", mutate_greenfield_missing_mvp_boundary, False, "MVP boundary"),
    Case("brownfield phase missing preservation baseline fails", mutate_brownfield_missing_preservation_baseline, False, "Preservation baseline"),
    Case("mixed phase missing brownfield controls fails", mutate_mixed_missing_brownfield_controls, False, "Preservation baseline"),
    Case("delivery baseline without SESSION_SCOPE passes", mutate_delivery_baseline_without_session_scope_passes, True, "PASS:"),
    Case("delivery baseline with SESSION_SCOPE fails", mutate_delivery_baseline_with_session_scope_fails, False, "delivery_baseline focus must not create SESSION_SCOPE.md"),
    Case("delivery baseline with session unresolved fails", mutate_delivery_baseline_with_session_unresolved_fails, False, "delivery_baseline focus must store delivery unresolved items"),
    Case("delivery baseline with session REQUIREMENTS fails", mutate_delivery_baseline_with_session_requirements_fails, False, "delivery_baseline focus must store optional requirements authority"),
    Case("delivery baseline with session DESIGN fails", mutate_delivery_baseline_with_session_design_fails, False, "delivery_baseline focus must store optional design authority"),
    Case("delivery baseline with delivery optional authority passes", mutate_delivery_baseline_with_delivery_optional_authority_passes, True, "PASS:"),
    Case("delivery baseline active wording fails", mutate_delivery_baseline_active_wording_fails, False, "delivery wording conflict"),
    Case("root accepted-state requirements without governance fails", mutate_root_accepted_requirements_without_governance_fails, False, "default root accepted-state artifact exists"),
    Case("root accepted-state requirements with governance passes", mutate_root_accepted_requirements_with_governance_passes, True, "PASS:"),
    Case("generated IU session missing checkpoint fails", mutate_generated_iu_session_missing_checkpoint_fails, False, "missing SESSION_LEDGER marker"),
    Case("generated IU session thin IU fails", mutate_generated_iu_session_thin_iu_fails, False, "generated IU too thin"),
    Case("generated archived session null timestamps fails", mutate_generated_archived_session_null_timestamps_fails, False, "missing created_at"),
    Case("generated IU retrospective cleanup fails", mutate_generated_iu_session_retrospective_cleanup_fails, False, "retrospective IU governance"),
    Case("generated accepted phase missing review gate fails", mutate_generated_phase_missing_review_gate_fails, False, "missing concrete review gate"),
    Case("generated current state placeholder row fails", mutate_generated_current_state_placeholder_row_fails, False, "placeholder row"),
    Case("L8.31 incomplete bootstrap start gate fails", mutate_l831_generated_session_incomplete_bootstrap_fails, False, "generated session did not mechanically start"),
    Case("L8.31 planned IUs with no files fails", mutate_l831_planned_ius_no_files_fails, False, "planned IUs but no IU files exist"),
    Case("L8.31 thin IU files fail", mutate_l831_thin_ius_fail, False, "thin or placeholder IU files detected"),
    Case("L8.31 lifecycle claim without active validation fails", mutate_l831_lifecycle_claim_without_active_validation_fails, False, "lifecycle claim without active generated-artifact validation PASS"),
    Case("L8.31 lifecycle claim without mechanical gate record fails", mutate_l831_lifecycle_claim_without_mechanical_gate_fails, False, "lifecycle claim without mechanical gate record"),
    Case("L8.31 approved carry-forward without source fails", mutate_l831_approved_carry_forward_without_source_fails, False, "APPROVED_CARRY_FORWARD without explicit approval/deferral source"),
    Case("L8.31 current-state pointer placeholder fails", mutate_l831_current_state_pointer_concordance_fails, False, "placeholder next delivery/phase pointer"),
]


def _run_case(case: Case) -> str | None:
    fixture_root = make_copy()
    try:
        case.mutate(fixture_root)
        result = run_validator(fixture_root)
        combined = result.output
        if case.should_pass:
            if result.returncode != 0:
                return f"{case.name}: expected pass, got failure:\n{combined}"
        else:
            if result.returncode == 0:
                return f"{case.name}: expected failure, got pass"
            if case.expected.lower() not in combined.lower():
                return f"{case.name}: failure did not mention {case.expected!r}:\n{combined}"
        return None
    finally:
        shutil.rmtree(fixture_root.parent, ignore_errors=True)


def main() -> int:
    cleanup_stale_tempdirs()
    requested_workers = int(os.environ.get("HIRMOS_VALIDATOR_FIXTURE_WORKERS", "8"))
    workers = max(1, min(requested_workers, len(CASES)))
    failures: list[str] = []
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(_run_case, case) for case in CASES]
        for future in as_completed(futures):
            failure = future.result()
            if failure:
                failures.append(failure)

    if failures:
        print("FAIL: HIRMOS validator regression fixtures")
        for failure in sorted(failures):
            print("- " + failure.replace("\n", "\n "))
        return 1
    print(f"PASS: HIRMOS validator regression fixtures ({len(CASES)} cases, {workers} workers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
