---
name: outreach
description: >-
  Prepare status-based customer/guest outreach (reconfirm bookings, collect
  balances, apply credits) as a reviewed mail-merge for one client. Use when the
  user wants to generate or preview outreach emails from a records file
  (e.g. "run the outreach for SIG", "build the guest emails", "prep the
  collections merge for <client>"). Multi-client, review-only — it NEVER sends.
---

# Outreach mail-merge skill

Turns a client's records (bookings, members, customers...) into a reviewed
mail-merge: each record is mapped to an email version (A/B/C/VERIFY) and written
to a CSV, with optional per-recipient draft previews. The engine is
`outreach/build_merge.py`; each client is a folder under `outreach/clients/<id>/`
with a `config.json`. Adding a client is config, not code.

## Safety rules — always
- **Never send email.** This skill only generates a CSV and draft previews for a
  human to review and send with their own tool. Say so explicitly.
- **A human fills in emails and payment links.** They are intentionally blank in
  the data; do not fabricate them.
- **PII stays local.** Don't paste guest/customer names, emails, or balances into
  external services. The `drafts/` output is gitignored — never commit it.
- **Respect the SEND CHECKLIST** in the client's README before declaring anything
  ready (high-value handled personally, platform bookings reconciled, `$0`/VERIFY
  records confirmed).

## Steps
1. **Pick the client.** If the user named one, use it. Otherwise list options and ask:
   ```
   python3 outreach/build_merge.py --list
   ```
2. **Validate** the config + data without writing anything:
   ```
   python3 outreach/build_merge.py --client <id> --check
   ```
   Resolve any `!` warnings (unmapped status, unproduced column) before continuing.
3. **Generate the merge sheet:**
   ```
   python3 outreach/build_merge.py --client <id>
   ```
   Report the summary back: row count, A/B/C/VERIFY breakdown, total owed, total credits.
4. **Gate on the SEND CHECKLIST.** Read `outreach/README.md` (and the client's notes)
   and tell the user what still blocks a send — typically: guest emails not yet loaded,
   payment links not created, high-value/platform/`$0` records needing manual handling.
5. **(Optional) Preview drafts** for review (never sends):
   ```
   python3 outreach/build_merge.py --client <id> --drafts
   ```
   Each draft is headed `READY` or `REVIEW`; summarize how many are ready vs. need work
   and why (no email, missing payment link, unfilled fields, channel_note flags).
6. **Hand off.** Remind the user that nothing was sent; they review the CSV/drafts and
   send via their mail-merge tool (HubSpot / Gmail), then log the sends.

## Add a new client (another test client)
Copy the example and edit config + templates + data — no code changes:
```
cp -r outreach/clients/example outreach/clients/<new-id>
```
Then edit `outreach/clients/<new-id>/config.json`, the `templates/`, and `records.json`.
Full config-field reference and a worked walkthrough are in
`outreach/clients/README.md`. Validate with `--check`, then run the smoke test:
```
python3 outreach/smoke_test.py
```

## Good to know
- `sig-lodges` is the live client; its config points at the existing
  `data/bookings.json`, `outreach/*.txt` templates, and `outreach/merge_data.csv`
  (output is byte-identical to the original script).
- Merge fields available to templates: every column the config produces, plus the
  `globals` (`sender_name`, `reservations_email`, `rescue_url`).
- Future delivery options (not built here): wrap `--drafts` in a scheduled run, or
  publish the generated CSV/summary to SharePoint for Stok colleagues to view.
