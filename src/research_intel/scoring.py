"""Transparent scoring helpers for synthetic public-data fixtures."""
from __future__ import annotations

from copy import deepcopy
from typing import Mapping, Sequence


def score_item(item: Mapping, weights: Mapping[str, float]) -> dict:
    """Return a scored copy of an item using weighted public signals."""
    scored = deepcopy(dict(item))
    signals = scored.get("signals", {}) or {}
    total = 0.0
    for name, weight in weights.items():
        total += float(signals.get(name, 0.0)) * float(weight)
    scored["score"] = round(total, 4)
    return scored


def rank_items(items: Sequence[Mapping], weights: Mapping[str, float]) -> list[dict]:
    """Score and rank items highest-first without mutating caller data."""
    return sorted((score_item(item, weights) for item in items), key=lambda item: item["score"], reverse=True)
