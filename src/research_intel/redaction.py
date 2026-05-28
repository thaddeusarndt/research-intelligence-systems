"""Small redaction utilities for public examples and reports."""
from __future__ import annotations

import re
from typing import Any

EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
SECRET_ASSIGNMENT_RE = re.compile(r"(?i)\b(token|password|api[_-]?key|secret)\s*=\s*[^\s,;]+")
BEARER_RE = re.compile(r"(?i)(Authorization:\s*Bearer\s+)[A-Za-z0-9._~+/=-]+")


def redact_text(text: str) -> str:
    """Redact common secret-shaped strings from display text."""
    text = EMAIL_RE.sub("[REDACTED_EMAIL]", text)
    text = SECRET_ASSIGNMENT_RE.sub(lambda match: f"{match.group(1)}=[REDACTED_SECRET]", text)
    text = BEARER_RE.sub(r"\1[REDACTED_SECRET]", text)
    return text


def redact_record(value: Any) -> Any:
    """Recursively redact strings inside dictionaries/lists."""
    if isinstance(value, str):
        return redact_text(value)
    if isinstance(value, list):
        return [redact_record(item) for item in value]
    if isinstance(value, dict):
        return {key: redact_record(item) for key, item in value.items()}
    return value
