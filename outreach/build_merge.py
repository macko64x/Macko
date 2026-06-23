#!/usr/bin/env python3
"""Config-driven outreach mail-merge engine (multi-client).

Maps each record (a booking, member, customer, ...) to an email template
version and produces a mail-merge-ready CSV for a human to review and send.
It only reorganizes data that already exists locally — no PII leaves the
machine, and email addresses / payment links are intentionally left blank for
a human to fill in.

One client == one folder under ``outreach/clients/<id>/`` with a
``config.json``. The config points at the client's data file, templates, and
output path, and declares the status->version map, thresholds, and special
cases. Adding a new client is config, not code.

Usage (from the repo root):
    python3 outreach/build_merge.py --client sig-lodges      # generate the CSV
    python3 outreach/build_merge.py --client example
    python3 outreach/build_merge.py --client example --check # validate only
    python3 outreach/build_merge.py --list                   # list clients

See ``outreach/clients/README.md`` for the config reference and the
``/outreach`` Claude skill (``.claude/skills/outreach/SKILL.md``) for the
human-in-the-loop workflow.
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import pathlib
import re
import sys
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
CLIENTS_DIR = ROOT / "outreach" / "clients"


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #
def fmt_date(iso: str) -> str:
    """ISO date -> 'June 30, 2026'. Pass through anything unparseable."""
    if not iso:
        return ""
    try:
        return datetime.date.fromisoformat(str(iso)).strftime("%B %-d, %Y")
    except ValueError:
        return str(iso)


def money(n: float, symbol: str = "$") -> str:
    return "{}{:,.0f}".format(symbol, n)


def list_clients() -> list[str]:
    if not CLIENTS_DIR.is_dir():
        return []
    return sorted(
        p.name
        for p in CLIENTS_DIR.iterdir()
        if p.is_dir() and (p / "config.json").is_file()
    )


def load_config(client: str) -> dict:
    cfg_path = CLIENTS_DIR / client / "config.json"
    if not cfg_path.is_file():
        raise SystemExit(
            f"No config for client '{client}'. Expected {cfg_path.relative_to(ROOT)}.\n"
            f"Known clients: {', '.join(list_clients()) or '(none)'}"
        )
    cfg = json.loads(cfg_path.read_text())
    cfg["_path"] = str(cfg_path)
    return cfg


def resolve(path_str: str) -> pathlib.Path:
    """Config paths are relative to the repo root."""
    p = pathlib.Path(path_str)
    return p if p.is_absolute() else (ROOT / p)


def load_records(cfg: dict):
    data = json.loads(resolve(cfg["data_file"]).read_text())
    records_key = cfg.get("records_key")
    return data, (data[records_key] if records_key else data)


# --------------------------------------------------------------------------- #
# core
# --------------------------------------------------------------------------- #
def build_rows(cfg: dict) -> tuple[list[dict], list[str]]:
    """Return (rows, warnings) for the given client config."""
    warnings: list[str] = []
    fields = cfg["fields"]
    symbol = cfg.get("currency_symbol", "$")
    globals_ = cfg.get("globals", {})
    status_map = cfg["status_to_version"]
    default_version = cfg.get("default_version", "REVIEW")
    lookup = cfg.get("lookup")
    date_fields = cfg.get("date_fields", [])
    flag_fields = cfg.get("flag_fields", [])
    passthrough = cfg.get("passthrough_fields", [])
    special_cases = cfg.get("special_cases", [])
    touch_at = cfg.get("personal_touch_at")
    touch_note = cfg.get("personal_touch_note", "")
    pay_field = cfg.get("payment_link_field")

    data, records = load_records(cfg)
    lookup_table = data.get(lookup["table_key"], {}) if lookup else {}

    rows: list[dict] = []
    for r in records:
        status = r.get(fields["status"])
        if status not in status_map:
            warnings.append(f"record {r.get(fields['id'])}: unmapped status '{status}'")
        version = status_map.get(status, default_version)

        name = (r.get(fields["name"]) or "").strip()
        balance = r.get(fields["balance"], 0) or 0

        notes = []
        for sc in special_cases:
            if r.get(sc["when_field"]) == sc["equals"]:
                notes.append(sc["note"])
        if touch_at is not None and balance >= touch_at:
            notes.append(touch_note)

        row = {
            fields["id"]: r.get(fields["id"], ""),
            fields["name"]: name,
            "first_name": name.split()[0] if name else "",
            fields["email"]: r.get(fields["email"], "") or "",
            "email_version": version,
            "balance_due": money(balance, symbol) if balance > 0 else money(0, symbol),
            "credit": money(-balance, symbol) if balance < 0 else "",
            "payment_link": (r.get(pay_field, "") or "") if pay_field else "",
            "channel_note": " ".join(notes),
        }

        if lookup:
            entry = lookup_table.get(r.get(lookup["from_field"]), {})
            for out_key, src_key in lookup["as"].items():
                row[out_key] = entry.get(src_key, "")
        for f in date_fields:
            row[f] = fmt_date(r.get(f, ""))
        for f in flag_fields:
            row[f] = "yes" if r.get(f) else ""
        for f in passthrough:
            row[f] = r.get(f, "")
        for k, v in globals_.items():
            row[k] = v

        rows.append(row)
    return rows, warnings


def run(client: str, check: bool = False) -> dict:
    """Generate (or validate) the merge sheet. Returns a summary dict."""
    cfg = load_config(client)
    columns = cfg["columns"]
    rows, warnings = build_rows(cfg)

    for c in columns:
        if rows and c not in rows[0]:
            warnings.append(f"column '{c}' is not produced by the config (will be blank)")

    by_version = Counter(r["email_version"] for r in rows)
    _, records = load_records(cfg)
    bal_field = cfg["fields"]["balance"]
    balances = [(r.get(bal_field, 0) or 0) for r in records]
    owed = sum(b for b in balances if b > 0)
    credits = sum(-b for b in balances if b < 0)
    symbol = cfg.get("currency_symbol", "$")

    out_path = resolve(cfg["output_file"])
    if not check:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("w", newline="") as f:
            writer = csv.DictWriter(
                f, fieldnames=columns, extrasaction="ignore", lineterminator="\n"
            )
            writer.writeheader()
            for r in rows:
                writer.writerow({c: r.get(c, "") for c in columns})

    return {
        "client": client,
        "brand": cfg.get("brand", client),
        "rows": len(rows),
        "by_version": dict(sorted(by_version.items())),
        "owed": owed,
        "credits": credits,
        "symbol": symbol,
        "output": out_path,
        "warnings": warnings,
        "checked_only": check,
    }


def print_summary(s: dict) -> None:
    try:
        rel = s["output"].relative_to(ROOT)
    except ValueError:
        rel = s["output"]
    verb = "Would write" if s["checked_only"] else "Wrote"
    print(f"[{s['client']}] {s['brand']}")
    print(f"{verb} {s['rows']} rows -> {rel}")
    print("By email version:", s["by_version"])
    print(f"Total balance owed: {money(s['owed'], s['symbol'])}")
    print(f"Total credits owed: {money(s['credits'], s['symbol'])}")
    for w in s["warnings"]:
        print(f"  ! {w}")


def render_drafts(client: str) -> dict:
    """Merge templates with each row into per-recipient draft files for review.

    Writes to ``<output_dir>/drafts/``. Renders previews only — it never sends.
    Every draft is marked READY or REVIEW; REVIEW means a human must resolve the
    listed reasons (no email on file, missing payment link, unfilled fields, or
    a channel_note flag) before it can go out.
    """
    cfg = load_config(client)
    rows, _ = build_rows(cfg)
    fields = cfg["fields"]
    tdir = resolve(cfg["templates_dir"])
    tfiles = cfg.get("template_files", {})
    out_dir = resolve(cfg["output_file"]).parent / "drafts"
    out_dir.mkdir(parents=True, exist_ok=True)

    ready, review, skipped = [], [], []
    for row in rows:
        ver = row["email_version"]
        rid = row.get(fields["id"], "")
        if ver not in tfiles:  # VERIFY / REVIEW: needs human triage first
            skipped.append((rid, ver))
            continue
        body = re.sub(
            r"{{\s*(\w+)\s*}}",
            lambda m: str(row.get(m.group(1), m.group(0))),
            (tdir / tfiles[ver]).read_text(),
        )
        email = row.get(fields["email"], "")
        reasons = []
        if not email:
            reasons.append("no email on file")
        if ver == "B" and not row.get("payment_link"):
            reasons.append("missing payment_link")
        leftover = sorted(set(re.findall(r"{{\s*\w+\s*}}", body)))
        if leftover:
            reasons.append("unfilled fields: " + ", ".join(leftover))
        if row.get("channel_note"):
            reasons.append("channel_note: " + row["channel_note"])

        status = "READY" if not reasons else "REVIEW"
        header = [
            f"# DRAFT — {status} — DO NOT SEND WITHOUT HUMAN REVIEW",
            f"# client: {client}   record: {rid}   version: {ver}",
            f"# to: {email or '(no email on file)'}",
        ] + [f"#   - {r}" for r in reasons] + [""]
        (out_dir / f"{rid}_{ver}.txt").write_text("\n".join(header) + body)
        (ready if status == "READY" else review).append(rid)

    return {
        "client": client,
        "out_dir": out_dir,
        "ready": ready,
        "review": review,
        "skipped": skipped,
        "total": len(rows),
    }


# --------------------------------------------------------------------------- #
# cli
# --------------------------------------------------------------------------- #
def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Config-driven outreach mail-merge engine.")
    ap.add_argument("--client", default="sig-lodges", help="client id under outreach/clients/")
    ap.add_argument("--check", action="store_true", help="validate only; do not write the CSV")
    ap.add_argument("--drafts", action="store_true", help="render per-recipient draft emails for review (never sends)")
    ap.add_argument("--list", action="store_true", help="list available clients and exit")
    args = ap.parse_args(argv)

    if args.list:
        clients = list_clients()
        print("Available clients:", ", ".join(clients) if clients else "(none)")
        return 0

    summary = run(args.client, check=args.check)
    print_summary(summary)

    if args.drafts:
        d = render_drafts(args.client)
        rel = d["out_dir"].relative_to(ROOT)
        print(f"\nDrafts -> {rel}/  (review only, nothing sent)")
        print(f"  READY: {len(d['ready'])}   REVIEW: {len(d['review'])}   "
              f"skipped (verify/unmapped): {len(d['skipped'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
