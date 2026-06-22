# Sprint 1: Guest Rescue (Days 1-3)
**Goal:** Make it impossible for guests to not know their booking is safe and who to pay.

## Task 1: Landing Page (losttraillodge.com or similar)
- Simple single-page site
- Headline: "Your reservation is confirmed under new management."
- 2-3 sentences explaining transition — honest, confident, no drama
- Two CTAs: "Confirm my booking" (email form) and "Pay my balance" (Stripe link)
- Mobile-first, fast load, no JS bloat
- Deployed same day — Vercel, no excuses

## Task 2: Per-Guest Stripe Payment Links
Generate unique Stripe payment links for each guest with outstanding balance.
Amounts:
- Girl Get After It: $12,420
- Lauren Hickey (Feb 15 booking): $7,510
- Jim Zellers: $5,674
- Chrystalina Roberts-Miller: $3,733
- Dreama Walton: $3,046
- Ashley Hanbury: $2,554
- Vyacheslav Strogolov: $2,900 (or coordinate with HipCamp first)

## Task 3: Outreach Email — All 29 Guests
Draft: warm, direct, no corporate speak. Three versions:
- Version A: Fully paid guest — "You're confirmed, here's what to expect, here's your new contact"
- Version B: Balance owed — "You're confirmed, here's your payment link for the remaining balance"  
- Version C: Credit owed — "You're confirmed, you have a $788 credit we'll apply to your stay"

Need from Cloudbeds: email addresses for all 29 guests.

## Task 4: HelloSign Waiver — Re-confirmation Under New Management
- Short waiver / agreement for all 29 existing guests to re-confirm under SIG
- Includes: acknowledgment of outdoor risk, property rules, new operator info
- Sent automatically on email confirmation
- Completion required before access codes released

## Task 5: Stripe Account Setup
- Legal entity: Lost Trail Lodge LLC and/or Thelma Hut LLC (separate accounts or sub-accounts)
- Bank accounts connected
- Tax info filed
- Test payment flow before sending to any guest

---

# Sprint 2: Core Booking System (Days 4-7)

## Task 1: Property Pages
- Lost Trail: photos, capacity (18), amenities, access info (trail description, parking), seasonality, house rules
- Red Mountain Pass: photos, capacity (post-conversion), access info (high alpine, winter-primary), partner guide info
- Both: add-on menu, partner list, FAQ

## Task 2: Booking Calendar + Form
- Dual-property calendar (separate availability)
- Date picker with blocked dates from existing bookings (import from Cloudbeds)
- Guest count selection
- Room/configuration options (whole lodge vs. east wing for LT; per-person for RMP)
- Add-on selection: chef, guide type, gear, snowmobile, cat skiing
- Pricing calculator (auto-update as selections change)

## Task 3: Stripe Checkout Flow
- Deposit amount: 25% at booking, remainder auto-charged 30 days before check-in
- Full payment required for bookings within 30 days
- Webhook handling: payment success → trigger confirmation email + waiver
- Refund policy enforcement: 100% refund >30 days, 50% 14-30 days, 0% <14 days

## Task 4: Confirmation + Pre-Arrival Email Sequence
- Immediate: booking confirmation with summary
- 7 days before: pre-arrival info (access, parking, what to bring, add-on confirmation)
- 48 hours before: final details, access codes/directions (only if waiver signed)
- Day of: emergency contact, weather check, "we're excited to have you"

---

# Sprint 3: Guest Experience Guides (Week 2)

## QR Codes to Build (Lost Trail)
Each links to a mobile-optimized page, offline-capable:

| Location | QR Label | Content |
|---|---|---|
| Kitchen | Kitchen Guide | Stove operation, fridge, bear-safe food storage, coffee setup |
| Living room | Wood Stove | How to light, damper control, fire safety |
| Bedrooms | Bedroom Guide | Linen, heater, blackout windows, noise policy |
| Bathroom | Water System | Pressure, hot water timer, composting toilet |
| Generator shed | Generator | Starting procedure, fuel location, load limits |
| Sauna | Sauna Guide | How to light wood fire, temperature, cool-down, honor system donation |
| Trailhead | Trail Map | Local trails, difficulty, emergency landmarks |
| Bear box | Bear Safety | What goes in, how to lock, what to do if you see one |
| Outdoor area | Emergency | Emergency contacts, cell signal spots, helicopter LZ location |

## Audio Buttons (Priority items — 60 sec each)
1. "How to light the wood stove" 
2. "How to fire up the sauna"
3. "Generator startup procedure"
4. "What to do in a bear encounter"
5. "Emergency protocols"

## Offline-Capable Architecture
- Next.js with next-pwa
- All guide content pre-cached on first load
- Works with zero cell signal after initial load
- QR codes printed and laminated — link to /guide/[property]/[location]

