"""CLI demo: read a synthetic fixture and print a dry-run report."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .approval_queue import build_approval_queue
from .redaction import redact_record
from .report_builder import build_markdown_report
from .scoring import rank_items


def run_fixture(path: str | Path) -> str:
    data = json.loads(Path(path).read_text())
    safe_data = redact_record(data)
    weights = safe_data.get("weights", {})
    items = safe_data.get("items", [])
    ranked = rank_items(items, weights)
    queue = build_approval_queue(ranked, threshold=float(safe_data.get("threshold", 0.75)))
    return build_markdown_report(safe_data.get("title", "Research Intelligence Demo"), ranked, queue)


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a synthetic dry-run research intelligence report.")
    parser.add_argument("fixture", help="Path to a synthetic fixture JSON file")
    args = parser.parse_args()
    print(run_fixture(args.fixture))


if __name__ == "__main__":
    main()
