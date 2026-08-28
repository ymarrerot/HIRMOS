#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.34 governed automated testing and test integrity."""
from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from test_validator_regressions import mutate_single_session_not_applicable_readiness

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
    return subprocess.run(
        [sys.executable, str(hirmos_dir / 'tools/validate.py')],
        cwd=hirmos_dir,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_testing_contract_and_integrity_surfaces() -> None:
    required = {
        'core/protocol/VALIDATION_AND_EVIDENCE.md': [
            'Governed automated testing and test integrity',
            'The test delta must be explainable by the behavioral-authority delta',
            'FAILING implementation',
        ],
        'core/templates/session/SESSION_SCOPE.md': [
            'Automated Testing Posture',
            'Unit-test posture: REQUIRED | NOT_APPLICABLE | COVERED_ELSEWHERE',
            'Material behaviors requiring unit tests / isolated automated tests',
        ],
        'core/templates/session/implementation-units/IU.md': [
            'Automated Testing Posture',
            'Test delta classification(s)',
            'Orphan/stale tests or fixtures removed',
        ],
        'extensions/implementation-agent/capabilities/implementation-execution/entrypoints/default.md': [
            'Do not respond to a failing valid test',
            'INVALID_TEST_CORRECTION',
        ],
        'extensions/implementation-agent/capabilities/implementation-unit-review/entrypoints/default.md': [
            'Test integrity and lifecycle review',
            'weakened while its behavioral authority remained unchanged',
        ],
    }
    for rel, phrases in required.items():
        for phrase in phrases:
            assert_contains(HIRMOS / rel, phrase)


def test_testing_policy_stays_lightweight_and_repository_native() -> None:
    protocol = (HIRMOS / 'core/protocol/VALIDATION_AND_EVIDENCE.md').read_text(errors='ignore')
    scope = (HIRMOS / 'core/templates/session/SESSION_SCOPE.md').read_text(errors='ignore')
    methodology = (HIRMOS / 'docs/2-methodology/implementation-evidence-and-claim-reconciliation.md').read_text(errors='ignore')
    assert 'Reuse the project\'s existing test framework' in protocol
    assert 'no universal numeric coverage threshold' in protocol
    assert 'HIRMOS does not impose a universal coverage percentage' in scope
    assert 'does not create `TEST_PLAN.md` or `TEST_REPORT.md` by default' in methodology


def test_cursor_projection_contains_test_integrity_rule() -> None:
    project = copy_hirmos('hirmos-l834-cursor-')
    try:
        result = subprocess.run(
            ['node', str(CLI), 'init', str(project), '--integration', 'cursor', '--offline'],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        assert result.returncode == 0, result.stdout
        assert_contains(project / '.cursor/commands/hirmos-continue.md', 'Governed automated testing and test integrity')
        assert_contains(project / '.cursor/commands/hirmos-continue.md', 'Do not weaken, skip, delete, trivialize, over-mock, or loosen still-valid behavioral tests merely to obtain PASS')
        assert_contains(project / '.cursor/skills/hirmos-continue/SKILL.md', 'For reproducible defects, add a focused regression test when practical')
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_active_session_requires_testing_posture() -> None:
    project = copy_hirmos('hirmos-l834-active-session-')
    try:
        hirmos = project / '_hirmos'
        mutate_single_session_not_applicable_readiness(hirmos)
        baseline = run_validator(hirmos)
        assert baseline.returncode == 0, baseline.stdout

        scope = hirmos / 'session/SESSION_SCOPE.md'
        body = scope.read_text()
        start = body.index('## Automated Testing Posture')
        body = body[:start].rstrip() + '\n'
        scope.write_text(body)

        result = run_validator(hirmos)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.34 active SESSION_SCOPE.md missing Automated Testing Posture' in result.stdout, result.stdout
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_validator_rejects_missing_testing_contract_surface() -> None:
    project = copy_hirmos('hirmos-l834-validator-')
    try:
        iu_template = project / '_hirmos/core/templates/session/implementation-units/IU.md'
        body = iu_template.read_text()
        body = body.replace('Automated Testing Posture', 'Test Notes')
        iu_template.write_text(body)
        result = run_validator(project / '_hirmos')
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.34' in result.stdout, result.stdout
        assert 'Automated Testing Posture' in result.stdout, result.stdout
    finally:
        shutil.rmtree(project, ignore_errors=True)


def main() -> int:
    tests = [
        test_testing_contract_and_integrity_surfaces,
        test_testing_policy_stays_lightweight_and_repository_native,
        test_cursor_projection_contains_test_integrity_rule,
        test_active_session_requires_testing_posture,
        test_validator_rejects_missing_testing_contract_surface,
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
        return 1
    print(f'PASS: PROD-L8.34 focused fixtures ({len(tests)}/{len(tests)})')
    return 0


if __name__ == '__main__':
    sys.exit(main())
