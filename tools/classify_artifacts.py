#!/usr/bin/env python3
"""Lightweight CSV classifier for AI/software artifact inventories.

This utility is intentionally simple. It does not approve tools or replace human review.
It turns a CSV artifact inventory into a Markdown starter pack for discussion.
"""
import argparse
import csv
from pathlib import Path

SENSITIVE_TERMS = ["customer", "confidential", "regulated", "finance", "financial", "personal", "pii"]
WRITE_TERMS = ["write", "read/write", "system of record", "erp", "crm"]
CUSTOMER_TERMS = ["direct", "customer", "external"]


def contains_any(value, terms):
    value = (value or "").lower()
    return any(term in value for term in terms)


def classify(row):
    users = (row.get("users") or "").lower()
    current_use = (row.get("current_use") or "").lower()
    data = (row.get("data_touched") or "").lower()
    systems = (row.get("systems_touched") or "").lower()
    exposure = (row.get("customer_exposure") or "").lower()
    value = (row.get("value_signal") or "").lower()

    customer = contains_any(exposure, CUSTOMER_TERMS) and "none" not in exposure
    sensitive = contains_any(data, SENSITIVE_TERMS)
    writes = contains_any(systems, WRITE_TERMS)
    recurring = any(x in current_use for x in ["daily", "weekly", "monthly", "recurring", "operational"])
    many_users = any(x in users for x in ["team", "leadership", "department", "managers", "pilot", "group"]) or any(ch.isdigit() for ch in users)

    if customer:
        klass = "Customer-Facing Promise candidate"
    elif writes or (recurring and many_users):
        klass = "Supported Internal Product candidate"
    elif many_users or "pilot" in users:
        klass = "Team Beta"
    else:
        klass = "Personal Tool"

    flags = []
    if sensitive:
        flags.append("sensitive/confidential data")
    if writes:
        flags.append("write-enabled/system impact")
    if customer:
        flags.append("customer exposure")
    if not row.get("backup_owner"):
        flags.append("backup owner gap")

    if klass.startswith("Customer"):
        route = "Hold beta or formalize before expansion"
    elif klass.startswith("Supported") and (writes or sensitive):
        route = "Formalize support/controls"
    elif klass == "Team Beta":
        route = "Hold beta; define proof and failure plan"
    else:
        route = "Keep personal unless reliance expands"

    return klass, "; ".join(flags) if flags else "low", route


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Input CSV path")
    parser.add_argument("--output", required=True, help="Output Markdown path")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)
    rows = list(csv.DictReader(input_path.open(newline="", encoding="utf-8")))

    lines = ["# Generated Artifact Classification Starter", "", "| ID | Artifact | Provisional Class | Flags | Route |", "|---|---|---|---|---|"]
    for row in rows:
        klass, flags, route = classify(row)
        lines.append(f"| {row.get('id','')} | {row.get('artifact','')} | {klass} | {flags} | {route} |")

    lines.extend([
        "",
        "## Note",
        "This is a starter classification for human review. It does not approve production use or certify security, privacy, compliance, architecture, or business value.",
    ])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
