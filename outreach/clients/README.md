# Outreach clients

Each client is a folder here with a `config.json`. The engine
(`outreach/build_merge.py`) is generic — **adding a client is config, not code.**

```
outreach/clients/
  sig-lodges/   # live client (config points at the repo's existing files)
  example/      # dummy, shareable template — copy this to start a new client
    config.json
    records.json
    templates/{email_A,email_B,email_C}.txt
    merge_data.csv   # generated output
```

## Add another client
```bash
cp -r outreach/clients/example outreach/clients/<new-id>
# edit config.json, templates/, records.json
python3 outreach/build_merge.py --client <new-id> --check   # validate
python3 outreach/build_merge.py --client <new-id>           # generate CSV
python3 outreach/build_merge.py --client <new-id> --drafts  # preview emails (no send)
```
Or just run the `/outreach` skill in Claude and name the client.

## config.json reference
| key | required | meaning |
|---|---|---|
| `client_id` | ✓ | folder id, for your reference |
| `brand` | ✓ | display name shown in the run summary |
| `globals` | ✓ | values merged into every row/template: `sender_name`, `reservations_email`, `rescue_url`, plus anything else your templates use |
| `currency_symbol` |  | default `"$"` |
| `data_file` | ✓ | path to the records JSON, **relative to the repo root** |
| `records_key` |  | key in the data file holding the list (omit if the file is a top-level array) |
| `output_file` | ✓ | where to write the CSV, relative to repo root |
| `templates_dir` | ✓ | folder holding the email templates, relative to repo root |
| `template_files` | ✓ | map of version → template filename, e.g. `{"A":"email_A.txt", ...}` |
| `fields` | ✓ | maps the engine's canonical fields to your record keys: `id`, `name`, `email`, `status`, `balance` |
| `status_to_version` | ✓ | maps each record `status` value to a template version (`A`/`B`/`C`/`VERIFY`) |
| `default_version` |  | version for unmapped statuses (default `REVIEW`) |
| `lookup` |  | enrich each row from a table in the data file: `{from_field, table_key, as:{out_key: src_key}}` |
| `date_fields` |  | record fields formatted as `Month D, YYYY` and exposed to templates |
| `flag_fields` |  | record fields rendered as `yes`/`""` |
| `passthrough_fields` |  | record fields copied through verbatim |
| `payment_link_field` |  | record field holding a per-recipient payment URL (else blank for a human to fill) |
| `personal_touch_at` |  | balance ≥ this adds `personal_touch_note` to `channel_note` |
| `personal_touch_note` |  | the note text for the above |
| `special_cases` |  | list of `{when_field, equals, note}` — adds `note` to `channel_note` when `record[when_field] == equals` |
| `columns` | ✓ | ordered list of columns to write to the CSV. Use any field the config produces (the `fields` outputs, `email_version`, `balance_due`, `credit`, `payment_link`, `channel_note`, `first_name`, lookup `as` keys, date/flag/passthrough fields, and `globals`) |

## Always-computed columns
Regardless of config, these are available to `columns` and templates:
`email_version`, `first_name`, `balance_due`, `credit`, `payment_link`,
`channel_note`, plus everything in `globals`.

## Balance convention
`balance > 0` → customer owes you → version **B**, `balance_due` set.
`balance < 0` → you owe the customer a credit → version **C**, `credit` set.
`balance == 0` → typically **A** (reconfirm) or **VERIFY** for anomalous `$0` records.

## Guardrails (built in)
- Email addresses and payment links are **left blank** for a human — never invented.
- `--drafts` renders previews only and marks each `READY`/`REVIEW`; it never sends.
- `drafts/` output is gitignored (may contain PII).
- See `outreach/README.md` for the full SEND CHECKLIST a human must clear before sending.
