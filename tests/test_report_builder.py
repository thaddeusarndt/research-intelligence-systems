from research_intel.report_builder import build_markdown_report


def test_report_includes_ranked_items_and_approval_statuses():
    scored = [{"title": "Synthetic trend", "score": 0.91, "summary": "Public signal only."}]
    queue = [{"title": "Synthetic trend", "status": "ready_for_review", "action": "draft_report_only", "reasons": []}]

    report = build_markdown_report("Demo Report", scored, queue)

    assert report.startswith("# Demo Report")
    assert "Synthetic trend" in report
    assert "0.91" in report
    assert "ready_for_review" in report
    assert "This repository uses synthetic fixtures" in report
