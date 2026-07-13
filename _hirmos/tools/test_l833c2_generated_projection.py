#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.33C-2 generated command and per-command skill projection."""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
HIRMOS = HERE.parent
ROOT = HIRMOS.parent.parent
CLI = ROOT / 'tools/cli/dist/index.js'

COMMANDS = ['start', 'continue', 'status', 'close']


def make_project() -> Path:
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l833c2-project-'))
    shutil.copytree(HIRMOS, tmp / '_hirmos', ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    return tmp


def run_cli(project: Path, integrations: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(['node', str(CLI), 'init', str(project), '--integration', integrations], cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def assert_contains(path: Path, phrase: str) -> None:
    assert path.exists(), f'missing {path}'
    body = path.read_text(errors='ignore')
    assert phrase in body, f'{path} missing {phrase!r}'


def test_cursor_generates_always_on_commands_and_per_command_skills() -> None:
    project = make_project()
    try:
        result = run_cli(project, 'cursor')
        assert result.returncode == 0, result.stdout
        assert_contains(project / '.cursor/rules/hirmos.mdc', 'HIRMOS-CAPSULE:invariants:PROD-L8.33C-2 canonical command capsule v1')
        for cmd in COMMANDS:
            assert_contains(project / f'.cursor/commands/hirmos-{cmd}.md', f'HIRMOS-CAPSULE:{cmd}:PROD-L8.33C-2 canonical command capsule v1')
            assert_contains(project / f'.cursor/skills/hirmos-{cmd}/SKILL.md', f'HIRMOS-CAPSULE:{cmd}:PROD-L8.33C-2 canonical command capsule v1')
        assert not (project / '.cursor/skills/hirmos/SKILL.md').exists(), 'must not generate broad hirmos/SKILL.md'
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_claude_uses_openspec_style_command_and_skill_paths() -> None:
    project = make_project()
    try:
        result = run_cli(project, 'claude')
        assert result.returncode == 0, result.stdout
        assert_contains(project / 'CLAUDE.md', 'HIRMOS-CAPSULE:invariants:PROD-L8.33C-2 canonical command capsule v1')
        assert_contains(project / '.claude/commands/hirmos/continue.md', 'hirmos continue` must classify and gate before it codes')
        assert_contains(project / '.claude/skills/hirmos-continue/SKILL.md', 'not a broad generic HIRMOS skill')
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_agents_fallback_does_not_generate_commands_or_skills() -> None:
    project = make_project()
    try:
        result = run_cli(project, 'agents')
        assert result.returncode == 0, result.stdout
        assert_contains(project / 'AGENTS.md', 'HIRMOS-CAPSULE:invariants:PROD-L8.33C-2 canonical command capsule v1')
        assert not any(project.glob('.*/commands/hirmos*')), 'agents fallback must not generate command files'
        assert not any(project.glob('.*/skills/hirmos*/SKILL.md')), 'agents fallback must not generate skills'
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_codex_generates_project_local_skills_but_no_default_commands() -> None:
    project = make_project()
    try:
        result = run_cli(project, 'codex')
        assert result.returncode == 0, result.stdout
        assert_contains(project / 'AGENTS.md', 'HIRMOS-CAPSULE:invariants:PROD-L8.33C-2 canonical command capsule v1')
        assert_contains(project / '.codex/skills/hirmos-continue/SKILL.md', 'HIRMOS-CAPSULE:continue:PROD-L8.33C-2 canonical command capsule v1')
        assert not any(project.glob('.codex/commands/**')), 'codex must not silently generate default command prompts'
    finally:
        shutil.rmtree(project, ignore_errors=True)


def test_static_validator_rejects_broad_skill_default() -> None:
    tmp = Path(tempfile.mkdtemp(prefix='hirmos-l833c2-validator-'))
    dst = tmp / '_hirmos'
    shutil.copytree(HIRMOS, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.DS_Store'))
    try:
        reg_path = dst / 'integrations/agent-tools/registry.json'
        registry = json.loads(reg_path.read_text())
        registry['projection_model']['broad_skill_default'] = 'enabled'
        reg_path.write_text(json.dumps(registry, indent=2) + '\n')
        result = subprocess.run([sys.executable, str(dst / 'tools/validate.py')], cwd=dst, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        assert result.returncode != 0, result.stdout
        assert 'PROD-L8.33C-2 broad default hirmos/SKILL.md must be disabled' in result.stdout
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    tests = [
        test_cursor_generates_always_on_commands_and_per_command_skills,
        test_claude_uses_openspec_style_command_and_skill_paths,
        test_agents_fallback_does_not_generate_commands_or_skills,
        test_codex_generates_project_local_skills_but_no_default_commands,
        test_static_validator_rejects_broad_skill_default,
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
    print(f'PASS: PROD-L8.33C-2 focused fixtures ({len(tests)}/{len(tests)})')
