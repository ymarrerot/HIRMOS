#!/usr/bin/env python3
"""Focused fixtures for PROD-L8.32K runtime boundary gates.

This runner protects the IU Planning / IU Execution split and validator-before-transition behavior.
It selects only L8.32K cases from the broader validator regression suite.
"""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
SUITE_PATH = HERE / "test_validator_regressions.py"
REQUIRED_CASE_COUNT = 3
# Validator static guard phrase: expected at least 3 L8.32K focused cases


def _load_suite():
    spec = importlib.util.spec_from_file_location("hirmos_validator_regressions", SUITE_PATH)
    if spec is None or spec.loader is None:
        raise SystemExit("FAIL: could not load test_validator_regressions.py")
    suite = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = suite
    spec.loader.exec_module(suite)
    return suite


def _selected_cases(suite):
    return [case for case in suite.CASES if case.name.startswith("L8.32K")]


def _run_case_in_process(suite, case) -> str | None:
    fixture_root = suite.make_copy()
    try:
        case.mutate(fixture_root)
        result = suite.run_validator(fixture_root)
        output = result.output
        if case.should_pass:
            if result.returncode != 0:
                return f"{case.name}: expected pass, got failure:\n{output}"
        else:
            if result.returncode == 0:
                return f"{case.name}: expected failure, got pass"
            if case.expected.lower() not in output.lower():
                return f"{case.name}: failure did not mention {case.expected!r}:\n{output}"
        print(f"PASS: {case.name}", flush=True)
        return None
    finally:
        shutil.rmtree(fixture_root.parent, ignore_errors=True)


def _read_output(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        return ""


def _run_cases_parallel(case_names: list[str], *, max_workers: int = 3, timeout_seconds: int = 120) -> list[tuple[str, int, str]]:
    pending = list(case_names)
    running: list[dict] = []
    results: list[tuple[str, int, str]] = []

    def launch(name: str) -> None:
        output = tempfile.NamedTemporaryFile("w+", encoding="utf-8", prefix="hirmos-l832k-case-", delete=False)
        output_path = Path(output.name)
        proc = subprocess.Popen(
            [sys.executable, str(Path(__file__).resolve()), "--case", name],
            text=True,
            stdout=output,
            stderr=subprocess.STDOUT,
        )
        output.close()
        running.append({"name": name, "proc": proc, "output_path": output_path, "started": time.monotonic()})

    while pending or running:
        while pending and len(running) < max_workers:
            launch(pending.pop(0))
        for item in list(running):
            proc = item["proc"]
            name = item["name"]
            output_path = item["output_path"]
            elapsed = time.monotonic() - item["started"]
            rc = proc.poll()
            if rc is None and elapsed > timeout_seconds:
                proc.kill()
                rc = 124
            if rc is not None:
                proc.wait()
                output = _read_output(output_path)
                if rc == 124:
                    output += f"\nFAIL: focused L8.32K case timed out: {name}\n"
                results.append((name, rc, output))
                output_path.unlink(missing_ok=True)
                running.remove(item)
        if running:
            time.sleep(0.1)
    return results


def main() -> int:
    suite = _load_suite()
    cases = _selected_cases(suite)
    if len(cases) < REQUIRED_CASE_COUNT:
        print(f"FAIL: expected at least {REQUIRED_CASE_COUNT} L8.32K focused cases, found {len(cases)}")
        return 1

    if len(sys.argv) == 3 and sys.argv[1] == "--case":
        matching = [case for case in cases if case.name == sys.argv[2]]
        if len(matching) != 1:
            print(f"FAIL: expected exactly one L8.32K focused case named {sys.argv[2]!r}, found {len(matching)}")
            return 1
        failure = _run_case_in_process(suite, matching[0])
        if failure:
            print("FAIL: HIRMOS L8.32K runtime boundary fixture")
            print("- " + failure.replace("\n", "\n "))
            return 1
        return 0

    suite.cleanup_stale_tempdirs()
    failures: list[str] = []
    print(f"RUN: {len(cases)} L8.32K focused cases with bounded parallelism", flush=True)
    for case_name, rc, output in _run_cases_parallel([case.name for case in cases]):
        print(output, end="" if output.endswith("\n") else "\n", flush=True)
        if rc != 0:
            failures.append(output)

    if failures:
        print("FAIL: HIRMOS L8.32K runtime boundary fixtures")
        for failure in failures:
            print("- " + failure.replace("\n", "\n "))
        return 1

    print(f"PASS: HIRMOS L8.32K runtime boundary fixtures ({len(cases)} cases)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
