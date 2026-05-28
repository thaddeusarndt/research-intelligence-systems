"""Approval-gated queue builder for dry-run recommendations."""
from __future__ import annotations

from copy import deepcopy
from typing import Sequence, Mapping


def build_approval_queue(items: Sequence[Mapping], threshold: float = 0.75) -> list[dict]:
    """Convert scored recommendations into review-only queue entries.

    This package never executes external actions. Even ready items are limited to
    drafting reports for human review.
    """
    queue: list[dict] = []
    for raw in items:
        item = deepcopy(dict(raw))
        risk_flags = list(item.get("risk_flags", []) or [])
        score = float(item.get("score", 0.0))
        reasons: list[str] = []
        if score < threshold:
            reasons.append("below_threshold")
        reasons.extend(risk_flags)
        status = "ready_for_review" if not reasons else "blocked_requires_approval"
        queue.append({
            "title": item.get("title", "Untitled"),
            "score": score,
            "status": status,
            "action": "draft_report_only",
            "reasons": reasons,
        })
    return queue
