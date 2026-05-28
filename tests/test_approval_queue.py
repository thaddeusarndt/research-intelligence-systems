from research_intel.approval_queue import build_approval_queue


def test_queue_marks_high_score_items_ready_for_review():
    items = [{"title": "Useful opportunity", "score": 0.82, "risk_flags": []}]

    queue = build_approval_queue(items, threshold=0.75)

    assert queue[0]["status"] == "ready_for_review"
    assert queue[0]["action"] == "draft_report_only"


def test_queue_blocks_items_with_risk_flags_even_when_score_is_high():
    items = [{"title": "Needs approval", "score": 0.95, "risk_flags": ["requires_login"]}]

    queue = build_approval_queue(items, threshold=0.75)

    assert queue[0]["status"] == "blocked_requires_approval"
    assert "requires_login" in queue[0]["reasons"]
