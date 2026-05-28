# Architecture

```text
Synthetic fixture JSON
        |
        v
redaction.py  -> removes common secret-shaped strings
        |
        v
scoring.py    -> weighted, transparent ranking
        |
        v
approval_queue.py -> ready_for_review or blocked_requires_approval
        |
        v
report_builder.py -> markdown report
```

The architecture is deliberately small and auditable. The demo favors clarity, tests, and safety boundaries over production-specific optimizations.
