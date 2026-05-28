# Research Intelligence Systems

Clean-room public-data research workflows for content gaps, market monitoring, narrative scanning, and opportunity discovery.

This repository is a portfolio-safe demo for recruiter and collaborator review. It shows how I structure research automation systems while keeping private strategies, accounts, credentials, and live execution paths out of public code.

## What this demonstrates

- transparent weighted scoring over public-style signals
- synthetic fixtures for content-gap, narrative-scan, and market-monitor examples
- redaction of common sensitive strings before reporting
- approval-gated queues that stop at `draft_report_only`
- markdown report generation
- tests and GitHub Actions CI

## Safety boundaries

This repo is intentionally dry-run only. It does **not** include:

- credentials, cookies, API keys, tokens, wallets, or account IDs
- private source lists, strategy thresholds, logs, or screenshots
- code that trades, submits forms, publishes posts, spends money, or mutates accounts
- production scraping, private endpoints, or proprietary edge logic

See [`docs/safety-boundaries.md`](docs/safety-boundaries.md).

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install pytest
PYTHONPATH=src pytest -q
PYTHONPATH=src python -m research_intel.demo examples/content_gap_input.json
```

Generate all sample reports:

```bash
mkdir -p reports/generated
for f in examples/*_input.json; do
  base=$(basename "$f" _input.json)
  PYTHONPATH=src python -m research_intel.demo "$f" > "reports/generated/${base}_report.md"
done
```

## Author

Thaddeus Arndt / Preballin

- Portfolio: https://www.preballin.com/portfolio/
- GitHub: https://github.com/thaddeusarndt
