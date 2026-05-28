from research_intel.redaction import redact_text, redact_record


def test_redact_text_removes_common_secret_shapes():
    text = "Email me at person@example.com with token=abc123 and Authorization: Bearer secretvalue"

    redacted = redact_text(text)

    assert "person@example.com" not in redacted
    assert "abc123" not in redacted
    assert "secretvalue" not in redacted
    assert "[REDACTED_EMAIL]" in redacted
    assert "[REDACTED_SECRET]" in redacted


def test_redact_record_recurses_nested_public_fixture_data():
    record = {"owner": "person@example.com", "nested": {"note": "password=hunter2"}}

    redacted = redact_record(record)

    assert redacted["owner"] == "[REDACTED_EMAIL]"
    assert redacted["nested"]["note"] == "password=[REDACTED_SECRET]"
