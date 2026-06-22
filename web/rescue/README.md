# Guest-Rescue Landing Page

Static, mobile-first reassurance + reconfirmation page for the 29 guests inherited
from Campfire Ranch. **No build step, no framework, no PII** — safe to deploy anywhere
static (Vercel, Netlify, Cloudflare Pages, GitHub Pages, S3).

## Files
- `index.html` — the page (hero, property selector, steps, reconfirm form, balances, FAQ, contact)
- `styles.css` — styling; property accent switches via `body[data-property]` (`lt` / `rmp` / `both`)
- `app.js` — property selector, URL params, form handling. **Edit the CONFIG block at the top.**

## Configure before launch (`app.js`)
- `RESERVATIONS_EMAIL` — monitored inbox guests reach. Currently `macko@stok.com`;
  swap to a dedicated alias (e.g. `guests@<brand>.com`) once created.
- `FORM_ENDPOINT` — POST URL for the reconfirm form (Formspree / HubSpot form / serverless fn).
  Leave empty `""` and the form falls back to opening a prefilled email, so nothing is ever lost.

## URL parameters (use in per-guest outreach links)
- `?p=lt` or `?p=rmp` — pre-selects the lodge and accent
- `?ref=ABC123` — prefills the booking reference
- `?pay=1` — ticks "need payment link" and jumps to the balances section

Example: `https://<domain>/?p=lt&ref=GGAI-2027&pay=1`

## Before publishing (owner sign-off required)
- [ ] Confirm the "I already paid Campfire Ranch" FAQ wording with legal/Matt — it's sensitive.
- [ ] Set `RESERVATIONS_EMAIL` to the inbox that will actually be monitored daily.
- [ ] Wire `FORM_ENDPOINT` (or confirm the email fallback is acceptable for launch).
- [ ] Remove the `<meta name="robots" content="noindex">` line in `index.html` when ready for search engines.

## Local preview
```
cd web/rescue && python3 -m http.server 8080
# open http://localhost:8080
```
