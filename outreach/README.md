# Guest Outreach — Campfire → SIG reconfirmation

Drafts for reaching the 29 inherited guests. **Nothing here sends automatically.**
These are ready for a human to review, personalize, and send once we have guest
email addresses (from the Cloudbeds export) and per-guest payment links.

> **This is now a reusable, multi-client engine.** SIG Lodges is one client
> (`clients/sig-lodges/`); copy `clients/example/` to onboard another. Run it
> inside Claude with the `/outreach` skill, or on the CLI. Config reference and
> "add a client" steps: [`clients/README.md`](clients/README.md). Skill:
> [`../.claude/skills/outreach/SKILL.md`](../.claude/skills/outreach/SKILL.md).

## Files
- `build_merge.py` — the generic, config-driven engine (`--client`, `--check`, `--drafts`, `--list`).
- `smoke_test.py` — fast checks for the engine + the `example` client.
- `clients/<id>/config.json` — per-client config (paths, status→version map, thresholds, special cases).
- `email_A_fully_paid.txt` — SIG: guest owes nothing; reconfirm only.
- `email_B_balance_owed.txt` — SIG: guest owes a balance; includes payment link.
- `email_C_credit_owed.txt` — SIG: SIG owes the guest a credit; applied to stay.
- `merge_data.csv` — SIG's generated mail-merge sheet (one row per booking).

The SIG client config (`clients/sig-lodges/config.json`) points at these existing
files, so the output is byte-identical to the original single-purpose script.

## How the version is chosen (from `data/bookings.json` status)
| status         | version | meaning                                  |
|----------------|---------|------------------------------------------|
| `fully_paid`   | **A**   | $0 balance — reconfirm only              |
| `balance_owed` | **B**   | guest owes money — send payment link     |
| `credit_owed`  | **C**   | SIG owes a credit — apply to stay        |
| `verify`       | VERIFY  | $0 / anomalous record — confirm first    |

## Merge fields used in the templates
`{{first_name}}` `{{lodge}}` `{{location}}` `{{check_in}}` `{{check_out}}`
`{{balance_due}}` `{{credit}}` `{{payment_link}}` `{{sender_name}}`
`{{reservations_email}}` `{{rescue_url}}`

Set these three globals once before sending:
- `{{sender_name}}` — who signs the email (e.g., Matt)
- `{{reservations_email}}` — monitored inbox (interim: macko@stok.com)
- `{{rescue_url}}` — the deployed guest-rescue page URL

## Regenerate the merge sheet
```
python3 outreach/build_merge.py --client sig-lodges            # write merge_data.csv
python3 outreach/build_merge.py --client sig-lodges --drafts   # also render review drafts (no send)
```
Drafts land in `outreach/drafts/` (gitignored, may contain PII) and are marked
`READY`/`REVIEW` — with no guest emails loaded yet, all rows are `REVIEW`.

## SEND CHECKLIST (do not skip)
- [ ] **Guest emails** filled into `merge_data.csv` (need the Cloudbeds export).
- [ ] **Payment links** created per balance-owed guest (QuickBooks/Stripe) and pasted in.
- [ ] **Handle personally** (not a blast): Girl Get After It ($12,420), Lauren Hickey
      Feb-12 booking ($7,510), Jim Zellers ($5,674). Flagged `channel_note` in the CSV.
- [ ] **HipCamp:** Vyacheslav Strogolov is platform-controlled — reroute via HipCamp
      before sending any direct payment link. Flagged in the CSV.
- [ ] **Verify $0 records** (William Anuszewski, Perry McCormac) before contacting.
- [ ] **Amy Degenhard** (first check-in Jun 30, $788 credit) — version C, send first.
- [ ] Matt reviews and approves the final copy + recipient list.
- [ ] Send via the chosen tool (HubSpot / Gmail mail-merge). Log sends.

## Note on sensitive wording
The "anything you already paid Campfire" line in email B is deliberate and
legally sensitive — it commits to a conversation, not a refund/credit of funds SIG
never received. Keep that wording (or have legal adjust it); don't over-promise.
