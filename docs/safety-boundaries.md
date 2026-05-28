# Safety Boundaries

This is a clean-room portfolio repository. It is not a production bot, trading system, scraper, or account automation tool.

## Included

- synthetic fixtures
- dry-run scoring
- redaction utilities
- approval queue modeling
- markdown reports
- tests

## Excluded

- credentials, cookies, tokens, API keys, passwords, wallets, signing code
- private endpoints, private source lists, production strategy thresholds
- logs, screenshots, account identifiers, personal data
- live execution paths that trade, submit, publish, spend, or mutate accounts

## Approval model

The only action emitted by the queue is `draft_report_only`. Risk flags or low scores produce `blocked_requires_approval`.
