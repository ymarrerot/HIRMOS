#!/usr/bin/env python3
from __future__ import annotations
import json, subprocess, tempfile, shutil
from pathlib import Path

HERE = Path(__file__).resolve()
HIRMOS = HERE.parents[1]
TOOL = HIRMOS / 'tools' / 'derive_pointer_indexes.py'

def run(root: Path) -> dict:
    out = subprocess.check_output(['python3', str(TOOL), str(root)], text=True)
    return json.loads(out)

def make_base(tmp: Path) -> Path:
    h = tmp / '_hirmos'
    (h / 'session' / 'implementation-units').mkdir(parents=True)
    (h / 'session' / 'bootstrap').mkdir(parents=True)
    (h / 'system' / 'accepted-state').mkdir(parents=True)
    (h / 'system' / 'delivery').mkdir(parents=True)
    (h / 'system' / 'history' / 'sessions').mkdir(parents=True)
    (h / 'core').mkdir(parents=True)
    (h / 'session' / 'SESSION_STATE.json').write_text('{"status":"idle"}\n')
    (h / 'system' / 'accepted-state' / 'CURRENT_SYSTEM_STATE.md').write_text('# css\n')
    (h / 'system' / 'accepted-state' / 'CARRY_FORWARD.md').write_text('# cf\n')
    return h

def test_absent_optional_artifacts_are_reported_without_creation() -> None:
    with tempfile.TemporaryDirectory() as d:
        h = make_base(Path(d))
        data = run(h)
        assert data['active_session_optional_artifacts']['evidence']['exists'] is False
        assert data['active_session_optional_artifacts']['session_unresolved']['exists'] is False
        assert data['active_implementation_units'] == []
        assert not (h / 'session' / 'EVIDENCE.md').exists()

def test_delivery_and_archive_pointers_are_derived_from_filesystem() -> None:
    with tempfile.TemporaryDirectory() as d:
        h = make_base(Path(d))
        (h / 'system' / 'delivery' / 'DELIVERY_PLAN.md').write_text('# plan\n')
        delivery = h / 'system' / 'delivery' / 'delivery-menugen'
        (delivery / 'phases').mkdir(parents=True)
        (delivery / 'DELIVERY_SCOPE.md').write_text('# scope\n')
        (delivery / 'phases' / 'PHASE-01.md').write_text('# phase\n')
        arch = h / 'system' / 'history' / 'sessions' / 'session-001'
        arch.mkdir(parents=True)
        (arch / 'ARCHIVE_MANIFEST.md').write_text('# archive\n')
        data = run(h)
        assert data['delivery']['roadmap'] == '_hirmos/system/delivery/DELIVERY_PLAN.md'
        assert data['delivery']['deliveries'][0]['delivery_id'] == 'delivery-menugen'
        assert data['delivery']['deliveries'][0]['phases'] == ['_hirmos/system/delivery/delivery-menugen/phases/PHASE-01.md']
        assert data['archives'][0]['manifest'] == '_hirmos/system/history/sessions/session-001/ARCHIVE_MANIFEST.md'

def test_iu_files_are_derived_only_after_materialization() -> None:
    with tempfile.TemporaryDirectory() as d:
        h = make_base(Path(d))
        iu = h / 'session' / 'implementation-units' / 'IU-01.md'
        iu.write_text('# IU-01\n')
        data = run(h)
        assert data['active_implementation_units'] == ['_hirmos/session/implementation-units/IU-01.md']

if __name__ == '__main__':
    tests=[test_absent_optional_artifacts_are_reported_without_creation, test_delivery_and_archive_pointers_are_derived_from_filesystem, test_iu_files_are_derived_only_after_materialization]
    failures=[]
    for t in tests:
        try:
            t()
            print(f'PASS: {t.__name__}')
        except Exception as e:
            failures.append((t.__name__, e))
            print(f'FAIL: {t.__name__}: {e}')
    if failures:
        raise SystemExit(1)
    print(f'PASS: PROD-L8.32L JIT / derived pointer fixtures — {len(tests)}/{len(tests)}')
