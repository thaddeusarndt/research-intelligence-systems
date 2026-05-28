from research_intel.scoring import score_item, rank_items


def test_score_item_combines_public_signals_with_weights():
    item = {"title": "Synthetic AI workflow", "signals": {"momentum": 0.8, "novelty": 0.6, "fit": 1.0}}
    weights = {"momentum": 2.0, "novelty": 1.0, "fit": 3.0}

    result = score_item(item, weights)

    assert result["score"] == 5.2
    assert result["title"] == "Synthetic AI workflow"


def test_rank_items_sorts_descending_without_mutating_inputs():
    items = [
        {"title": "Low", "signals": {"momentum": 0.1}},
        {"title": "High", "signals": {"momentum": 0.9}},
    ]

    ranked = rank_items(items, {"momentum": 1.0})

    assert [item["title"] for item in ranked] == ["High", "Low"]
    assert "score" not in items[0]
