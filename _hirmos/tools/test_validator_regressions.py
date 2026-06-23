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
import runpy
import shutil
import sys
import tempfile
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
    """Run the validator in-process against a temporary _hirmos copy.

    Subprocess execution can become slow or hang in constrained environments when
    repeated across many mutated fixture copies. `validate.py` derives its root
    from `__file__`, so runpy execution against the fixture copy preserves the
    same semantics while avoiding repeated process startup overhead.
    """
    stdout = io.StringIO()
    stderr = io.StringIO()
    old_argv = sys.argv[:]
    sys.argv = [str(root / "tools" / "validate.py")]
    try:
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            try:
                runpy.run_path(str(root / "tools" / "validate.py"), run_name="__main__")
                return ValidationResult(0, stdout.getvalue() + stderr.getvalue())
            except SystemExit as exc:
                code = exc.code if isinstance(exc.code, int) else 1
                return ValidationResult(code, stdout.getvalue() + stderr.getvalue())
    finally:
        sys.argv = old_argv


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


def write_basic_active_artifacts(root: Path) -> None:
    session = root / "session"
    (session / "SESSION_SCOPE.md").write_text("# SESSION_SCOPE.md\n")
    (session / "SESSION_EXECUTION.md").write_text("# SESSION_EXECUTION.md\n")
    (session / "unresolved-items.md").write_text("# unresolved-items.md\n")
    (session / "SESSION_SCOPE.md close verification").write_text("# SESSION_SCOPE.md close verification\n")


def write_delivery_artifacts(
    root: Path,
    *,
    include_plan: bool = True,
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
) -> None:
    activate_session(root, stage="close_ready" if close_transaction else "implementation_readiness", recommended="hirmos close" if close_transaction else "hirmos continue")
    session = root / "session"
    delivery_id = "fixture-delivery"
    plan_path = f"_hirmos/system/delivery/{delivery_id}/DELIVERY_PLAN.md"
    phase_path = f"_hirmos/system/delivery/{delivery_id}/phases/PHASE-01.md"
    css_plan = plan_path if current_state_matches else "_hirmos/system/delivery/other-delivery/DELIVERY_PLAN.md"
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
Delivery plan path: {plan_path}
Active phase path: {phase_path}

## Phase Entry Gate Evidence

Phase Entry Gate status: {entry_gate_status}
Lifecycle status supports adoption: YES
Phase type supports implementation: YES
Entry criteria satisfied: YES
Type-specific entry controls satisfied: YES
Pointer concordance satisfied: YES
Blocking open items absent or resolved: YES
""")
    cf_review_answer = "YES" if carry_forward_recorded or resulting_phase_status == "ACCEPTED" else "NO"
    if include_status_report:
        status_report = f"""
## Phase Lifecycle Status Report Record

Phase lifecycle status: {phase_status or 'UNKNOWN'}
Phase type: {phase_type}
Phase Entry Gate status: {entry_gate_status}
Phase Progress Ledger status: REVIEWED
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

    (session / "SESSION_EXECUTION.md").write_text(f"# SESSION_EXECUTION.md\n\n## Durable Phase Adoption Gate\nGate status: PASS\n\n## Phase Entry Gate Execution Log\nImplementation readiness authorized: YES\n\n## Phase Progress / Carry-Forward Record\nAdopted phase progress reviewed: PASS\nCarry-forward obligations recorded: PASS\n{status_report}\n{acceptance_execution}\n")
    (session / "unresolved-items.md").write_text("# unresolved-items.md\n")
    (session / "SESSION_SCOPE.md").write_text((session / "SESSION_SCOPE.md").read_text() + f"\n\n## Phase Entry Gate Review\nWas the Phase Entry Gate status PASS? YES\n\n## Phase Progress / Carry-Forward Review\nDid the session update or verify the durable Phase Progress Ledger? YES\nIf phase outcome is not ACCEPTED, are carry-forward obligations recorded? {cf_review_answer}\n{acceptance_review}\n")

    delivery_dir = root / "system" / "delivery" / delivery_id
    (delivery_dir / "phases").mkdir(parents=True, exist_ok=True)
    if include_plan:
        (delivery_dir / "DELIVERY_PLAN.md").write_text("# DELIVERY_PLAN.md\n\n## Delivery Status Update Log\n")

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
    cf_row = "{cf_row}" if carry_forward_recorded else "| | | | | | |"

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
Entry criteria status: SATISFIED

{greenfield_controls}
{brownfield_controls}

## Phase Acceptance Review
{acceptance_phase}
## Phase Progress Ledger

| Session/archive | Adopted scope | Completed items | Partial items | Blocked items | Deferred items | Evidence pointer | Resulting lifecycle status |
|---|---|---|---|---|---|---|---|
| fixture-session | fixture scope | fixture completed | fixture partial | fixture blocked | fixture deferred | fixture evidence | {resulting_phase_status} |

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
Delivery plan: {css_plan}
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
        (session / "SESSION_EXECUTION.md").write_text((session / "SESSION_EXECUTION.md").read_text() + f"""

## Close-Time Delivery / Phase Status Transaction

Transaction status: {status}
Delivery plan path: {plan_path}
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


def mutate_idle_stale_contract(root: Path) -> None:
    (root / "session" / "SESSION_SCOPE.md").write_text("# stale contract\n")


def mutate_active_missing_unresolved_items(root: Path) -> None:
    activate_session(root)
    session = root / "session"
    for filename in ["SESSION_SCOPE.md", "SESSION_EXECUTION.md"]:
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

# retained marker: accepted-state index reappears
CASES = [
    Case("valid baseline", mutate_none, True, "PASS:"),
    Case("idle stale SESSION_SCOPE", mutate_idle_stale_contract, False, "stale active-session"),
    Case("active missing unresolved-items", mutate_active_missing_unresolved_items, False, "missing canonical root artifact"),
    Case("unsupported legacy command", mutate_unsupported_legacy_command, False, "unsupported command"),
    Case("implementation readiness wrong recommendation", mutate_readiness_wrong_recommendation, False, "implementation_readiness"),
    Case("delivery governed active readiness passes", mutate_delivery_governed_active_readiness, True, "PASS:"),
    Case("phase entry gate valid brownfield passes", mutate_phase_entry_gate_valid_brownfield, True, "PASS:"),
    Case("phase entry gate valid mixed passes", mutate_phase_entry_gate_valid_mixed, True, "PASS:"),
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
]


def main() -> int:
    cleanup_stale_tempdirs()
    failures: list[str] = []
    for case in CASES:
        fixture_root = make_copy()
        try:
            case.mutate(fixture_root)
            result = run_validator(fixture_root)
            combined = result.output
            if case.should_pass:
                if result.returncode != 0:
                    failures.append(f"{case.name}: expected pass, got failure:\n{combined}")
            else:
                if result.returncode == 0:
                    failures.append(f"{case.name}: expected failure, got pass")
                elif case.expected.lower() not in combined.lower():
                    failures.append(f"{case.name}: failure did not mention {case.expected!r}:\n{combined}")
        finally:
            shutil.rmtree(fixture_root.parent, ignore_errors=True)

    if failures:
        print("FAIL: HIRMOS validator regression fixtures")
        for failure in failures:
            print("- " + failure.replace("\n", "\n "))
        return 1
    print(f"PASS: HIRMOS validator regression fixtures ({len(CASES)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
