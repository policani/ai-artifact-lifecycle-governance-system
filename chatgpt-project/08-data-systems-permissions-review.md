# Data, Systems, and Permissions Review

This is not a security audit. It is a routing screen to identify which artifacts need accountable review.

## Capture

| Area | Ask |
|---|---|
| Data | What data categories does it read, store, transform, or expose? |
| Systems | What systems does it touch? |
| Permissions | Does it use personal credentials, shared credentials, service accounts, or unknown access? |
| Writes | Does it write to any system of record or trigger downstream actions? |
| External exposure | Does data leave approved environments? |
| Retention | Does it store prompts, outputs, logs, files, or customer data? |
| Secrets | Are API keys, tokens, passwords, or credentials involved? |

## Escalation flags

- regulated data;
- customer data;
- system-of-record writes;
- shared credentials;
- secrets in code or prompts;
- external APIs with unclear terms;
- customer-facing output;
- autonomous actions without review;
- unknown owner with broad access.

## Output

Classify control need as low, moderate, high, or unknown. Recommend review owner categories, not specific approvals.
