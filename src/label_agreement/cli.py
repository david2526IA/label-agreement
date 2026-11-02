from __future__ import annotations

import argparse
import json
from pathlib import Path

from .metrics import agreement


def main() -> None:
    parser = argparse.ArgumentParser(description="Measure paired annotation agreement from JSONL.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, default=Path("agreement_report.json"))
    args = parser.parse_args()
    rows = [json.loads(line) for line in args.input.read_text(encoding="utf-8").splitlines() if line.strip()]
    report = agreement(rows)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: report[key] for key in ("items", "observed_agreement", "cohen_kappa")}))
