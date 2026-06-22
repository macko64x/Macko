#!/usr/bin/env python3
"""Generate outreach/merge_data.csv from data/bookings.json.

Maps each confirmed booking to the correct outreach email version (A/B/C) and
produces a mail-merge-ready CSV. This only reorganizes data that already exists
in the repo — no PII leaves the machine. Email addresses and per-guest payment
links are intentionally left blank for a human to fill from the Cloudbeds export
and the payment provider.

Run from the repo root:
    python3 outreach/build_merge.py
"""
import csv
import datetime
import json
import pathlib
from collections import Counter

ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "data" / "bookings.json"
OUT = ROOT / "outreach" / "merge_data.csv"

# booking status -> email template version
VERSION = {
    "fully_paid": "A",
    "balance_owed": "B",
    "credit_owed": "C",
    "verify": "VERIFY",  # $0 / anomalous records — confirm before any send
}

PERSONAL_TOUCH_AT = 5000  # balances >= this get a personal note, not a templated blast


def fmt_date(iso: str) -> str:
    try:
        return datetime.date.fromisoformat(iso).strftime("%B %-d, %Y")
    except ValueError:
        return iso


def money(n: int) -> str:
    return "${:,.0f}".format(n)


def main() -> None:
    data = json.loads(SRC.read_text())
    props = data["properties"]
    rows = []

    for b in data["bookings"]:
        prop = props.get(b["property"], {})
        balance = b["balance"]
        guest = (b.get("guest") or "").strip()

        notes = []
        if b.get("source") == "HipCamp":
            notes.append("Booked via HipCamp — coordinate through HipCamp before billing directly.")
        if balance >= PERSONAL_TOUCH_AT:
            notes.append("High-value — handle personally, not a templated send.")

        rows.append({
            "id": b["id"],
            "email_version": VERSION.get(b["status"], "REVIEW"),
            "guest": guest,
            "first_name": guest.split()[0] if guest else "",
            "email": "",          # TODO: fill from Cloudbeds export
            "lodge": prop.get("name", b["property"]),
            "location": prop.get("location", ""),
            "check_in": fmt_date(b["check_in"]),
            "check_out": fmt_date(b["check_out"]),
            "balance_due": money(balance) if balance > 0 else "$0",
            "credit": money(-balance) if balance < 0 else "",
            "payment_link": "",   # TODO: per-guest QuickBooks/Stripe link
            "priority": "yes" if b.get("priority") else "",
            "channel_note": " ".join(notes),
            "notes": b.get("notes", ""),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    # ---- console summary ----
    by_version = Counter(r["email_version"] for r in rows)
    owed = sum(b["balance"] for b in data["bookings"] if b["balance"] > 0)
    credits = sum(-b["balance"] for b in data["bookings"] if b["balance"] < 0)

    print(f"Wrote {len(rows)} rows -> {OUT.relative_to(ROOT)}")
    print("By email version:", dict(sorted(by_version.items())))
    print(f"Total balance owed by guests: {money(owed)}")
    print(f"Total credits owed to guests: {money(credits)}")


if __name__ == "__main__":
    main()
