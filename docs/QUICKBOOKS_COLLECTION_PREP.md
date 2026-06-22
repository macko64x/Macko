# QuickBooks Collection Prep — Guest Balances & Credits

Prep sheet for re-collecting the **$37,837** owed by guests and resolving credits
after the Campfire takeover. **Nothing has been entered into QuickBooks yet** — this
is the data to use when we set up customers + invoices (with your go-ahead).

Amounts reconcile to `data/bookings.json` (source of truth) and `outreach/merge_data.csv`.

## Two entities (set up as separate companies / classes)
- **Lost Trail Lodge, LLC** — Coldstream Canyon, CA bookings (property `LT`)
- **Thelma Hut, LLC** — Red Mountain Pass, CO bookings (property `RMP`)

---

## A. Invoices to create — 7 priority balances ($37,837 total)

| # | Guest | Entity | Amount | Check-in | Send timing / notes |
|---|-------|--------|--------|----------|---------------------|
| 1 | Girl Get After It | Lost Trail Lodge, LLC | **$12,420** | Mar 24, 2027 | Largest. 12-guest group. **Personal call first**, then invoice. |
| 2 | Lauren Hickey (booking 2) | Lost Trail Lodge, LLC | **$7,510** | Feb 12, 2027 | Consecutive w/ her fully-paid Feb 9 stay. **Personal note.** |
| 3 | Jim Zellers | Lost Trail Lodge, LLC | **$5,674** | Sep 7, 2026 | Repeat guest, known to Matt. **Most urgent by date.** Personal. |
| 4 | Chrystalina Roberts-Miller | Thelma Hut, LLC | **$3,733** | Mar 5, 2027 | Standard invoice + payment link. |
| 5 | Dreama Walton | Thelma Hut, LLC | **$3,046** | Aug 28, 2026 | Invoice now (near-term). |
| 6 | Ashley Hanbury | Thelma Hut, LLC | **$2,554** | Feb 11, 2027 | Standard invoice + payment link. |
| 7 | Vyacheslav Strogolov | Thelma Hut, LLC | **$2,900** | Jul 4, 2026 | **HipCamp booking — reroute via HipCamp before billing directly.** |

Subtotals: Lost Trail **$25,604** · Thelma **$12,233** · **Total $37,837** ✓

**Invoice memo template:** `Remaining balance — {{lodge}} stay {{check_in}}–{{check_out}} (reconfirmed under Stok Investment Group after Campfire Ranch transition).`

**Suggested terms:** balance due on reconfirmation. For 2027 check-ins, optionally
offer 50% now / 50% by 30 days before arrival. Attach a Stripe/QuickBooks payment link.

---

## B. Credits to apply (SIG owes guest) — $1,576 total

| Guest | Entity | Credit | Check-in | Notes |
|-------|--------|--------|----------|-------|
| Amy Degenhard | Thelma Hut, LLC | **$788** | **Jun 30, 2026** | FIRST CHECK-IN — resolve before arrival. Email version C. |
| Nicole Valdanbrini | Thelma Hut, LLC | **$788** | Aug 4, 2026 | Apply to stay. Email version C. |

---

## C. Overpayments to verify & refund/credit

| Guest | Entity | Issue | Action |
|-------|--------|-------|--------|
| Kristina Ketting | Lost Trail Lodge, LLC | Paid $8,789 vs gross $5,729 → **~$3,060 over** | Verify in Cloudbeds; refund or credit. |
| John Gavan (RMP, booking 3) | Thelma Hut, LLC | Paid $4,576 vs gross $4,462 → **~$114 over** | Verify; likely minor — credit or ignore per Matt. |

---

## D. $0 bookings to confirm before any billing
- **William Anuszewski** (Thelma, Jul 6) — comp or data error?
- **Perry McCormac** (Thelma, Jul 30) — comp or data error?

---

## Setup checklist (when ready — needs your go-ahead)
- [ ] Confirm Cloudbeds export so every amount + guest email is verified.
- [ ] Create the two entities in QuickBooks (or one company with LT/Thelma classes).
- [ ] Create customers (the 7 above + credits/overpayments).
- [ ] Create invoices per the table; attach payment links.
- [ ] **Test one invoice + payment link end-to-end before sending to any guest.**
- [ ] Matt approves before invoices/links go out. (Charging cards = outward step.)
