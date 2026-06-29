#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.32R installed-project fixture isolation and residual status hygiene."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIRMOS = HERE.parent


def make_installed_copy() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l832r-'))
    project = tmp / 'project'
    dst = project / '_hirmos'
    project.mkdir(parents=True, exist_ok=True)
    shutil.copytree(HIRMOS, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    return dst


def run_validator(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(root / 'tools' / 'validate.py')], cwd=root.parent, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def write_completed_delivery(root: Path, *, roadmap_status: bool = False, parent_status: bool = False, phase_progress_ledger: bool = False) -> None:
    delivery_root = root / 'system' / 'delivery'
    delivery = delivery_root / 'menugen-mvp'
    phase_dir = delivery / 'phases'
    phase_dir.mkdir(parents=True, exist_ok=True)
    delivery_root.mkdir(parents=True, exist_ok=True)
    plan_prefix = 'Roadmap status: ACTIVE\n' if roadmap_status else 'Roadmap posture: derived\n'
    (delivery_root / 'DELIVERY_PLAN.md').write_text(
        '# Delivery Plan\n\n'
        + plan_prefix
        + '\n## Delivery Index\n\n| Delivery ID | Name | Status | Scope file |\n|---|---|---|---|\n| menugen-mvp | MenuGen | completed | _hirmos/system/delivery/menugen-mvp/DELIVERY_SCOPE.md |\n| PHASE-01 | MenuGen phase | ACCEPTED | _hirmos/system/delivery/menugen-mvp/phases/PHASE-01.md |\n'
    )
    (delivery / 'DELIVERY_SCOPE.md').write_text(
        '# Delivery Scope\n\nAuthority status: BASELINED\n\nClose result: ACCEPTED\n\n| Requirement ID | Name | Priority | Coverage |\n|---|---|---|---|\n| FR-001 | Upload | MUST | PHASE-01 |\n'
    )
    parent_line = 'Parent delivery status: ACTIVE\n' if parent_status else 'Parent delivery status source: derived from roadmap/register and current-state pointers\n'
    progress = '## Phase Progress Ledger\n\n- stale narrative row\n' if phase_progress_ledger else '## Phase Progress Pointer Index\n\n| Session/archive | Scope/result pointer | Evidence pointer | Remaining-work pointer | Status impact |\n|---|---|---|---|---|\n| archive | scope | evidence | none | accepted |\n'
    (phase_dir / 'PHASE-01.md').write_text(
        '# Phase Scope\n\nLifecycle status: ACCEPTED\n'
        + parent_line
        + '\n'
        + progress
        + '\n## Phase Review Gate\n\n'
        + '- Actual final codebase reviewed: YES\n'
        + '- Scope coverage result: PASS\n'
        + '- Runtime evidence level: LOCAL_RUNTIME_VERIFIED\n'
        + '- Production evidence level: NOT_CLAIMED\n'
        + '- Final phase review result: PASS\n'
        + '- Why this result is honest: synthetic fixture has accepted phase evidence.\n'
        + '- What is not claimed: production readiness.\n'
    )
    css = root / 'system' / 'accepted-state' / 'CURRENT_SYSTEM_STATE.md'
    css.parent.mkdir(parents=True, exist_ok=True)
    if css.exists():
        css.write_text(css.read_text(errors='ignore') + '\nLatest accepted delivery: menugen-mvp complete\n')
    else:
        css.write_text('# Current System State\n\nLatest accepted delivery: menugen-mvp complete\n')


def test_q_fixture_isolation_inside_installed_project_passes() -> None:
    root = make_installed_copy()
    try:
        # Add unrelated generated state that used to contaminate the Q fixture when
        # the fixture was run from an installed project instead of the clean package.
        write_completed_delivery(root, roadmap_status=True, parent_status=True, phase_progress_ledger=True)
        result = subprocess.run([sys.executable, str(root / 'tools' / 'test_l832q_delivery_concordance.py')], cwd=root.parent, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert result.returncode == 0, result.stdout
    finally:
        shutil.rmtree(root.parent.parent, ignore_errors=True)


def test_roadmap_status_field_fails() -> None:
    root = make_installed_copy()
    try:
        write_completed_delivery(root, roadmap_status=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'Roadmap status' in result.stdout
    finally:
        shutil.rmtree(root.parent.parent, ignore_errors=True)


def test_parent_delivery_status_field_fails() -> None:
    root = make_installed_copy()
    try:
        write_completed_delivery(root, parent_status=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert ('Parent delivery status field' in result.stdout) or ('phase mirrors stale parent delivery ACTIVE' in result.stdout)
    finally:
        shutil.rmtree(root.parent.parent, ignore_errors=True)


def test_phase_progress_ledger_heading_fails() -> None:
    root = make_installed_copy()
    try:
        write_completed_delivery(root, phase_progress_ledger=True)
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'Phase Progress Ledger' in result.stdout
    finally:
        shutil.rmtree(root.parent.parent, ignore_errors=True)


def test_macos_artifact_hygiene_fails() -> None:
    root = make_installed_copy()
    try:
        (root.parent / '.DS_Store').write_text('mac artifact')
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert '.DS_Store' in result.stdout
    finally:
        shutil.rmtree(root.parent.parent, ignore_errors=True)


def test_completed_project_readme_boilerplate_fails() -> None:
    root = make_installed_copy()
    try:
        write_completed_delivery(root)
        (root.parent / 'README.md').write_text('This is a Next.js project bootstrapped with create-next-app.\n')
        result = run_validator(root)
        assert result.returncode != 0, result.stdout
        assert 'create-next-app boilerplate README' in result.stdout
    finally:
        shutil.rmtree(root.parent.parent, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_q_fixture_isolation_inside_installed_project_passes,
        test_roadmap_status_field_fails,
        test_parent_delivery_status_field_fails,
        test_phase_progress_ledger_heading_fails,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print(f'PASS: {test.__name__}')
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f'FAIL: {test.__name__}: {exc}')
    if failures:
        raise SystemExit(1)
    print(f'PASS: PROD-L8.32R installed-project fixture isolation and residual status hygiene fixtures — {len(tests)}/{len(tests)}')
