#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.33G carry-forward lifecycle consolidation."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIRMOS = HERE.parent
ROOT = HIRMOS.parent.parent
CLI = ROOT / 'tools/cli/dist/index.js'


def assert_contains(path: Path, phrase: str) -> None:
    assert path.exists(), f'missing {path}'
    body = path.read_text(errors='ignore')
    assert phrase in body, f'{path} missing {phrase!r}'


def copy_hirmos(prefix: str) -> Path:
    tmp = Path(tempfile.mkdtemp(prefix=prefix))
    shutil.copytree(HIRMOS, tmp / '_hirmos', ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    return tmp


def run_validator(hirmos_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(hirmos_dir / 'tools/validate.py')], cwd=hirmos_dir, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def test_carry_forward_template_owns_active_and_resolved_lifecycle() -> None:
    cf = HIRMOS / 'system/accepted-state/CARRY_FORWARD.md'
    for phrase in [
        'single accepted-state authority for carry-forward lifecycle',
        'Active Carry-Forward Register',
        'Resolved Carry-Forward Register',
        'CF-YYYYMMDD-NNN',
        'source_ref',
        'Removal / Resolution Concordance Rule',
        'Accepted-State Maintenance Flow',
    ]:
        assert_contains(cf, phrase)


def test_command_surfaces_define_existing_command_flow_not_new_command() -> None:
    for rel, phrases in {
        'core/commands/start.md': ['ACCEPTED_STATE_MAINTENANCE', 'CARRY_FORWARD_RESOLUTION', 'must not edit product/source files'],
        'core/commands/continue.md': ['accepted-state-only write boundary', 'Resolved Carry-Forward Register', 'Do not mutate historical archives'],
        'core/commands/status.md': ['Status Blocked By Carry-Forward Concordance Conflict', 'matching resolved carry-forward row', 'recommend exactly one next command'],
        'core/commands/close.md': ['Carry-Forward Attention block', 'CF-YYYYMMDD-NNN', 'later resolution uses the existing command flow'],
    }.items():
        path = HIRMOS / rel
        for phrase in phrases:
            assert_contains(path, phrase)


def test_cursor_projection_contains_carry_forward_lifecycle_rules() -> None:
    project = copy_hirmos('hirmos-l833g-cursor-')
    try:
        result = subprocess.run(['node', str(CLI), 'init', str(project), '--integration', 'cursor', '--offline'], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert result.returncode == 0, result.stdout
        assert_contains(project / '.cursor/rules/hirmos.mdc', 'Carry-forward lifecycle is consolidated in `CARRY_FORWARD.md`')
        assert_contains(project / '.cursor/commands/hirmos-status.md', 'Carry-forward concordance')
        assert_contains(project / '.cursor/skills/hirmos-close/SKILL.md', 'Carry-Forward Attention')
        assert_contains(project / '.cursor/skills/hirmos-start/SKILL.md', 'ACCEPTED_STATE_MAINTENANCE')
        assert not (project / '.cursor/skills/hirmos/SKILL.md').exists(), 'must not generate broad HIRMOS skill'
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_validator_rejects_missing_carry_forward_lifecycle_rule() -> None:
    project = copy_hirmos('hirmos-l833g-validator-')
    try:
        cf = project / '_hirmos/system/accepted-state/CARRY_FORWARD.md'
        body = cf.read_text()
        cf.write_text(body.replace('Removal / Resolution Concordance Rule', 'Removal Rule'))
        result = run_validator(project / '_hirmos')
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.33G' in result.stdout or 'carry-forward lifecycle' in result.stdout.lower(), result.stdout
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_validator_rejects_missing_close_attention_block() -> None:
    project = copy_hirmos('hirmos-l833g-close-')
    try:
        close = project / '_hirmos/core/commands/close.md'
        close.write_text(close.read_text().replace('Carry-Forward Attention block', 'Carry-Forward Review block'))
        result = run_validator(project / '_hirmos')
        assert result.returncode != 0, result.stdout
        assert 'Carry-Forward Attention' in result.stdout, result.stdout
    finally:
        shutil.rmtree(project, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_carry_forward_template_owns_active_and_resolved_lifecycle,
        test_command_surfaces_define_existing_command_flow_not_new_command,
        test_cursor_projection_contains_carry_forward_lifecycle_rules,
        test_validator_rejects_missing_carry_forward_lifecycle_rule,
        test_validator_rejects_missing_close_attention_block,
    ]
    failures = 0
    for test in tests:
        try:
            test()
            print(f'PASS: {test.__name__}')
        except Exception as exc:
            failures += 1
            print(f'FAIL: {test.__name__}: {exc}')
    if failures:
        sys.exit(1)
    print(f'PASS: PROD-L8.33G focused fixtures ({len(tests)}/{len(tests)})')
