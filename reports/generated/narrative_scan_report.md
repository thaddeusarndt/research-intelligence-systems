# Synthetic Narrative Scan Report

> Safety note: This repository uses synthetic fixtures and dry-run outputs only.
> It does not trade, publish, submit forms, spend funds, or mutate accounts.

## Ranked findings
1. **Approval-gated agent workflows** — score `0.83`
   - Synthetic narrative around safer human-in-loop automation.
2. **Private beta growth hack** — score `0.82`
   - Synthetic item blocked because it implies account mutation.

## Approval queue
- **Approval-gated agent workflows**: `ready_for_review` / `draft_report_only` / reasons: none
- **Private beta growth hack**: `blocked_requires_approval` / `draft_report_only` / reasons: requires_login, external_action

## Boundary
Recommendations stop at report drafting and require human approval for any external action.

