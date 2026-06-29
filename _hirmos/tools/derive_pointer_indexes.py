#!/usr/bin/env python3
"""Derive compact HIRMOS pointer indexes from filesystem source artifacts.

This utility is intentionally read-only. It prints JSON so runtime/status/close
flows can compare handwritten pointer rows against source artifacts instead of
trusting duplicated mutable state.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


def rel(path: Path, root: Path) -> str:
    try:
        return "_hirmos/" + str(path.relative_to(root)).replace('\\', '/')
    except ValueError:
        return str(path).replace('\\', '/')


def exists_rel(root: Path, path: str) -> dict[str, Any]:
    p = root / path
    return {"path": "_hirmos/" + path, "exists": p.exists(), "type": "directory" if p.is_dir() else "file" if p.is_file() else "missing"}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore") if path.exists() else ""


def _status_from_delivery_scope(text: str) -> str:
    m = re.search(r'Authority status\s*:\s*([^\n]+)', text, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r'(?m)^Status\s*:\s*([^\n]+)', text, re.I)
    return m.group(1).strip() if m else "UNKNOWN"


def _phase_lifecycle(text: str) -> str:
    m = re.search(r'Lifecycle status\s*:\s*([^\n]+)', text, re.I)
    return m.group(1).strip() if m else "UNKNOWN"


def _close_result(text: str) -> str:
    m = re.search(r'Close result\s*:\s*([^\n]+)', text, re.I)
    if m:
        return m.group(1).strip()
    m = re.search(r'Delivery result\s*\|\s*([^|\n]+)\|', text, re.I)
    return m.group(1).strip() if m else "UNKNOWN"


def _roadmap_status(text: str) -> str:
    m = re.search(r'(?m)^Roadmap status\s*:\s*([^\n]+)', text, re.I)
    return m.group(1).strip() if m else "DERIVED"


def _derive_delivery_concordance(root: Path, delivery_dir: Path, plan_text: str, css_text: str) -> dict[str, Any]:
    scope = delivery_dir / "DELIVERY_SCOPE.md"
    scope_text = _read(scope)
    phases = []
    accepted_like = 0
    for phase in sorted((delivery_dir / "phases").glob("PHASE-*.md")):
        phase_text = _read(phase)
        status = _phase_lifecycle(phase_text)
        if re.search(r'\b(ACCEPTED|COMPLETE|CLOSED|PARTIAL)\b', status, re.I):
            accepted_like += 1
        phases.append({"phase": rel(phase, root), "lifecycle_status": status})
    complete_signals = []
    combined_public = "\n".join([plan_text, css_text, scope_text])
    if re.search(r'\b(completed|complete|accepted|closed)\b', combined_public, re.I):
        complete_signals.append("roadmap/current-state/scope completion wording")
    if accepted_like and phases and accepted_like == len(phases):
        complete_signals.append("all materialized phases accepted-like")
    conflicts = []
    roadmap_status = _roadmap_status(plan_text)
    if re.search(r'\b(ACTIVE|COMPLETE|COMPLETED|ACCEPTED|PARTIAL|BLOCKED|DEFERRED|CANCELLED)\b', roadmap_status, re.I):
        conflicts.append(f"DELIVERY_PLAN owns duplicated Roadmap status: {roadmap_status}; roadmap posture should be derived")
    if complete_signals and re.search(r'(?m)^Status\s*:\s*ACTIVE\b', scope_text, re.I):
        conflicts.append("DELIVERY_SCOPE mirrors runtime Status: ACTIVE while derived completion signals exist")
    if re.search(r'\|[^\n]*\bPROPOSED\b[^\n]*\|', scope_text, re.I) and complete_signals:
        conflicts.append("DELIVERY_SCOPE requirement/status rows preserve PROPOSED after derived completion signals")
    for phase in (delivery_dir / "phases").glob("PHASE-*.md"):
        if complete_signals and re.search(r'Parent delivery status\s*:\s*ACTIVE\b', _read(phase), re.I):
            conflicts.append(f"{rel(phase, root)} mirrors Parent delivery status: ACTIVE after derived completion signals")
    return {
        "delivery_id": delivery_dir.name,
        "scope": rel(scope, root),
        "authority_status": _status_from_delivery_scope(scope_text),
        "close_result": _close_result(scope_text),
        "roadmap_status": roadmap_status,
        "phase_count": len(phases),
        "accepted_like_phase_count": accepted_like,
        "derived_completion_signals": complete_signals,
        "conflicts": conflicts,
        "phases": phases,
    }


def derive(root: Path) -> dict[str, Any]:
    delivery_root = root / "system" / "delivery"
    history_root = root / "system" / "history" / "sessions"
    session_root = root / "session"
    accepted_root = root / "system" / "accepted-state"

    delivery_plan = delivery_root / "DELIVERY_PLAN.md"
    deliveries: list[dict[str, Any]] = []
    if delivery_root.exists():
        for scope in sorted(delivery_root.glob("*/DELIVERY_SCOPE.md")):
            delivery_dir = scope.parent
            phases = [rel(p, root) for p in sorted((delivery_dir / "phases").glob("PHASE-*.md"))]
            deliveries.append({
                "delivery_id": delivery_dir.name,
                "scope": rel(scope, root),
                "phases": phases,
                "unresolved_register": rel(delivery_dir / "unresolved-items.md", root) if (delivery_dir / "unresolved-items.md").exists() else None,
                "requirements": rel(delivery_dir / "REQUIREMENTS.md", root) if (delivery_dir / "REQUIREMENTS.md").exists() else None,
                "design": rel(delivery_dir / "DESIGN.md", root) if (delivery_dir / "DESIGN.md").exists() else None,
            })

    archives: list[dict[str, Any]] = []
    if history_root.exists():
        for manifest in sorted(history_root.glob("*/ARCHIVE_MANIFEST.md")):
            archives.append({"session_id": manifest.parent.name, "manifest": rel(manifest, root)})

    optional_active = {
        "session_scope": exists_rel(root, "session/SESSION_SCOPE.md"),
        "session_ledger": exists_rel(root, "session/SESSION_LEDGER.md"),
        "bootstrap_report": exists_rel(root, "session/bootstrap/BOOTSTRAP_REPORT.md"),
        "evidence": exists_rel(root, "session/EVIDENCE.md"),
        "session_unresolved": exists_rel(root, "session/unresolved-items.md"),
        "session_requirements": exists_rel(root, "session/REQUIREMENTS.md"),
        "session_design": exists_rel(root, "session/DESIGN.md"),
        "implementation_units_dir": exists_rel(root, "session/implementation-units"),
    }
    iu_files = []
    iu_dir = session_root / "implementation-units"
    if iu_dir.exists():
        iu_files = [rel(p, root) for p in sorted(iu_dir.glob("IU-*.md"))]

    plan_text = _read(delivery_plan)
    css_text = _read(accepted_root / "CURRENT_SYSTEM_STATE.md")
    delivery_concordance = []
    if delivery_root.exists():
        for delivery in sorted(p for p in delivery_root.iterdir() if p.is_dir() and (p / "DELIVERY_SCOPE.md").exists()):
            delivery_concordance.append(_derive_delivery_concordance(root, delivery, plan_text, css_text))

    return {
        "schema_version": "hirmos-derived-pointer-index-v1",
        "root": str(root),
        "source_of_truth": "filesystem + SESSION_STATE.json + source artifact paths; handwritten pointer rows are derived caches",
        "delivery": {
            "roadmap": rel(delivery_plan, root) if delivery_plan.exists() else None,
            "deliveries": deliveries,
            "delivery_concordance": delivery_concordance,
        },
        "active_session_optional_artifacts": optional_active,
        "active_implementation_units": iu_files,
        "accepted_state": {
            "current_system_state": rel(accepted_root / "CURRENT_SYSTEM_STATE.md", root) if (accepted_root / "CURRENT_SYSTEM_STATE.md").exists() else None,
            "carry_forward": rel(accepted_root / "CARRY_FORWARD.md", root) if (accepted_root / "CARRY_FORWARD.md").exists() else None,
        },
        "archives": archives,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Derive HIRMOS pointer indexes from filesystem source artifacts.")
    ap.add_argument("root", nargs="?", default=".", help="Project root or _hirmos root")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    if (root / "_hirmos").is_dir():
        root = root / "_hirmos"
    if not (root / "session" / "SESSION_STATE.json").exists() and not (root / "core").exists():
        raise SystemExit(f"not a HIRMOS root: {root}")
    print(json.dumps(derive(root), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
