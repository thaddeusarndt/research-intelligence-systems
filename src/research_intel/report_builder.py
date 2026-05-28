"""Markdown report rendering for synthetic research-intelligence demos."""
from __future__ import annotations

from typing import Sequence, Mapping


def build_markdown_report(title: str, scored_items: Sequence[Mapping], queue: Sequence[Mapping]) -> str:
    """Build a recruiter-readable markdown report from scored synthetic items."""
    lines = [
        f"# {title}",
        "",
        "> Safety note: This repository uses synthetic fixtures and dry-run outputs only.",
        "> It does not trade, publish, submit forms, spend funds, or mutate accounts.",
        "",
        "## Ranked findings",
    ]
    for idx, item in enumerate(scored_items, start=1):
        lines.extend([
            f"{idx}. **{item.get('title', 'Untitled')}** — score `{float(item.get('score', 0.0)):.2f}`",
            f"   - {item.get('summary', 'No summary provided.')}",
        ])
    lines.extend(["", "## Approval queue"] )
    by_title = {entry.get("title"): entry for entry in queue}
    for item in scored_items:
        entry = by_title.get(item.get("title"), {})
        reasons = ", ".join(entry.get("reasons", []) or ["none"])
        lines.append(f"- **{item.get('title', 'Untitled')}**: `{entry.get('status', 'unknown')}` / `{entry.get('action', 'draft_report_only')}` / reasons: {reasons}")
    lines.extend(["", "## Boundary", "Recommendations stop at report drafting and require human approval for any external action.", ""] )
    return "\n".join(lines)
