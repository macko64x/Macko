# SIG Lodges — Claude Code Project Brief
**Owner:** Matt Macko / Stok Investment Group (SIG)  
**Date:** June 2026  
**Status:** Active crisis → launch mode. Properties just reverted to SIG. Need to be operational within days.

---

## WHAT JUST HAPPENED (Read This First)

Campfire Ranch (the operator) dissolved June 18, 2026. SIG owns the two properties as landlord (PropCo entities: Lost Trail Lodge LLC and Thelma Hut LLC). Campfire notified all 29 confirmed future guests that reservations were cancelled. SIG is now stepping in to:

1. Honor as many of those bookings as possible under SIG's own operation
2. Build a permanent, self-operated lodging business at both properties
3. Get a website, booking system, and guest experience infrastructure live ASAP

There are 29 confirmed future bookings worth $125,306 gross, first check-in June 30. The $92,218 Campfire had collected from guests is likely unrecoverable. SIG must re-collect from guests or offer credit. Outstanding guest balances of $37,837 still need to be collected.

Booking data lives in Cloudbeds (being transferred to SIG). Guest names, contact info, amounts, and dates are known.

---

## THE TWO PROPERTIES

### Property 1: Lost Trail Lodge (Coldstream Canyon, CA — near Truckee)
- **Legal entity:** Lost Trail Lodge, LLC  
- **Former operator:** Campfire Coldstream LLC  
- **Debt service:** ~$6,500/month  
- **Property type:** Backcountry lodge, off-grid, river adjacent, Coldstream Canyon  
- **Current capacity:** 18 guests max (whole-lodge bookings historically)  
- **Location character:** Accessible summer/fall on foot/bike/horse; winter snowmobile or ski-in  
- **Key assets:** Main lodge, multiple sleeping areas, large kitchen, outdoor spaces, river access  
- **Planned additions:** Riverside wood-fired sauna  
- **Special event permits:** Up to 3/year allowing events beyond 18-person day-use limit  
- **Debt service:** $6,500/month

### Property 2: Red Mountain Pass / Thelma Hut (CO — San Juan Mountains)
- **Legal entity:** Thelma Hut, LLC  
- **Former operator:** Campfire Thelma LLC  
- **Debt service:** ~$3,500/month  
- **Property type:** Single backcountry hut/cabin, high alpine, winter ski access  
- **Current capacity:** Will increase — convert primary bedroom to bunk room to maximize occupancy  
- **Location character:** High alpine, winter-primary, guiding-partnership model  
- **Key assets:** Single hut structure, stunning alpine setting  
- **Planned change:** Bedroom → bunk room conversion to increase capacity and price per-person  
- **Debt service:** $3,500/month

---

## BUSINESS MODEL

### Lost Trail — Full Operating Model

**Revenue streams (priority order):**

1. **Weekly Group Buyouts** — PRIMARY REVENUE DRIVER  
   Full lodge buyout for corporate groups, outdoor brand retreats, adventure companies. Target: North Face, RMU, Patagonia, tech companies, outdoor startups, film crews. Price as premium all-inclusive experience. Minimum 2 nights preferred. These are the highest-margin bookings.

2. **Special Event Buyouts** — UP TO 3/YEAR, HIGH MARKUP  
   Weddings, milestone events, brand activations. Limited supply = premium pricing. 3 special event permits per year allowing beyond-18-person gatherings during day. These should be the highest-priced inventory.

3. **Nightly/Weekend Individual Bookings — A La Carte Model**  
   Guests book the space. Curated add-ons available at time of booking or post-booking:
   - Chef (from curated partner list, guests choose)
   - Guide (MTB, climbing, trail, forestry, packrafting)
   - Gear rental
   - Snowmobile rental (winter)
   - Cat skiing through Pacific Crest (winter) or High Sierra
   - Camp host / experience facilitation
   Booking partners: MTB groups, rock climbing schools, forestry/outdoor education, packrafting outfitters

4. **Local Day-Use Membership** — COMMUNITY / BRAND BUILDING  
   "If you're back in Coldstream Canyon and want a place to chill from the heat and grab a beer, we have access."  
   Members get access to: common areas, outdoor spaces, riverside sauna, day facilities. NOT bedrooms or large kitchen (when booked by overnight guests).  
   Honor system for sauna (QR code donation), reasonably priced membership tier.  
   Overnight access is a separate booking/pricing tier.

5. **Annual Rotating Chef Event** — ONCE/YEAR  
   Signature event, curated chef-led experience, high price point, drives press and social content.

**Operational model by season:**

*Winter (Nov–April):*
- Live-in hut manager on-site (see job description below)
- Full service for booked guests
- Sauna maintained and accessible to members and guests
- Cat skiing and snowmobile add-ons facilitated by manager

*Summer (May–Oct):*
- Self-service model with detailed guest guides (QR codes, voice buttons)
- Weekly laundry service (sheets, towels — guests responsible for basic upkeep)
- Monthly trash pickup (dumpster on-site with keyed access)
- Monthly sauna cleaning
- Guests responsible for bear-safe practices (cameras in outdoor/public areas only)
- Guests change own sheets, leave property as found or better

**Honor system / sauna:**
- Wood-fired riverside sauna — members and overnight guests
- QR code donation system for sauna access
- Access control TBD (possibly lock with member code, honor system in summer)

**Weddings / events:**
- Special event permits: 3/year
- High markup, limited availability
- Signature add-ons: curated catering, florals, photography partner list
- T&Cs and liability waivers mandatory (especially post-Tahoe avalanche)

---

### Red Mountain Pass (Thelma) — Lean Partner Model

- Primary partnership with an established guiding company (target: first outreach to Mountain Trip Guides who already operate in the San Juan backcountry)
- Guiding company serves as de facto host — lower SIG revenue share but near-100% of revenue is profit since SIG's costs are low
- SIG provides: the hut, basic maintenance, booking platform
- Partner provides: guests, guides, food/experience
- Price per person, not whole-hut buyout
- After bunk room conversion: maximize per-person occupancy
- A la carte add-ons similar to Lost Trail where relevant
- Simple self-service guide for guests when no partner guide present
- Maintenance focus: keep R&M low, systems reliable, no frills

---

## WHAT TO BUILD

### 1. Public Website
- Brand: clean, outdoorsy, premium but accessible. Not corporate. Think: "serious mountain people who want the real thing."
- Pages: Home, Lost Trail (property page), Red Mountain Pass (property page), Membership, Events/Weddings, Partners, Book Now
- Mobile-first — guests are on phones in parking lots and on trail
- Content: property photos, amenities, location/access info, partner list, add-on menu
- Legal: T&Cs, waiver links, privacy policy all accessible from footer

### 2. Booking System
- Calendar-based availability for both properties independently
- Whole-lodge buyout booking (primary) and per-person/per-room booking (secondary, RMP)
- Pricing tiers: weekday/weekend, seasonal, group size
- Add-on selection at booking (chef, guide, gear, etc.) or post-booking upsell
- Deposit collection at booking (TBD: 25-50% deposit, remainder 30 days prior)
- Full payment collection with Stripe (credit cards required)
- Booking confirmation emails with property access instructions
- Automated pre-arrival email sequence (7 days out, 48 hours out, day-of)

### 3. Payment Infrastructure
- Stripe integration for all payments
- Deposit at booking, balance auto-charged per schedule
- Refund policy enforced programmatically (30-day cancellation for full refund, etc.)
- Membership subscription billing (monthly or annual)
- Add-on payments (can be pre-paid or paid at experience)
- Tip/donation QR code for sauna and honor system items
- All financial transactions logged and reportable

### 4. Guest Experience — Off-Grid Digital Guides
- QR codes posted throughout each property (kitchen, bedroom, sauna, outdoor areas, etc.)
- Each QR links to a mobile-optimized property guide page
- Guide content: how to use the wood stove, water system, generator, sauna, composting toilet, bear boxes, emergency contacts, trail maps, local conditions
- Optional: short-form voice audio buttons ("tap to hear how to light the sauna") — simple HTML5 audio, no app required
- Offline-capable (service worker cache) since properties are off-grid / low signal
- Content managed via simple CMS so Matt can update without dev help
- Emergency contact always visible, one tap to call

### 5. Digital Waiver & Signature
- HelloSign or DocuSign API integration
- Waiver sent automatically on booking confirmation
- Must be signed before access codes/directions are released
- T&Cs cover: outdoor risk, bear country, avalanche terrain (RMP), property damage, noise/leave-no-trace
- Signature stored with booking record
- Separate enhanced waiver for special events / large groups

### 6. Member Portal — Lost Trail Day-Use Membership
- Membership signup flow (Stripe subscription)
- Member card / QR code for access
- Member benefits clearly stated: day-use areas, sauna access, honor system
- Blackout dates (when property is fully booked by overnight guests)
- Member directory optional (community feel)
- Email list / comms channel for members (events, chef nights, volunteer days)

### 7. Partner Directory & Integration
- Curated partner list: chefs, guides (MTB, climbing, packrafting, ski/snowshoe), gear rental, cat skiing operators, photographers, florists (events)
- Partners listed on site with booking inquiry flow
- Partner add-on selection in booking flow
- Partner contact/commission system (simple at first — email notification + flat fee or % cut)
- Ability to add/remove partners from CMS

### 8. Admin Dashboard
- View all bookings (both properties), filter by date/status/property
- Guest contact info, waiver status, payment status
- Outstanding balance tracking (the $37,837 currently owed by guests)
- Add-on fulfillment status
- Member list and membership status
- Special event permit tracker (max 3/year, countdown)
- Revenue dashboard: monthly, by property, by revenue stream
- Laundry/maintenance schedule tracker
- Camera feed access (outdoor cameras)

### 9. Legal / Compliance Pages
- Full T&Cs (outdoor recreation, property rules, cancellation policy)
- Privacy policy (CCPA compliant — CA property)
- Waiver / assumption of risk document
- Bear safety acknowledgment (separate checkbox at booking)
- Avalanche risk acknowledgment (RMP bookings — mandatory)
- All signed digitally and stored

---

## TECH STACK RECOMMENDATIONS

These are suggestions — Matt has final call on stack:

- **Frontend:** Next.js (React) — good for SEO, fast, mobile-first, easy to deploy
- **Hosting:** Vercel (frontend) + Railway or Supabase (backend/DB)
- **Database:** PostgreSQL via Supabase (auth, bookings, members, payments all in one)
- **Payments:** Stripe (subscriptions + one-time + deposits + payout tracking)
- **Booking calendar:** Build custom or integrate with Cal.com (open source, embeddable)
- **Email:** Resend or Postmark for transactional, Loops or Mailchimp for member comms
- **Signatures:** HelloSign (now Dropbox Sign) API — simpler than DocuSign for this use case
- **CMS for guest guides:** Sanity.io or Notion API (easy for non-dev updates)
- **QR codes:** Generated programmatically (qrcode npm package), printed and posted on-site
- **Audio guides:** Simple HTML5 audio files hosted on S3 or Cloudflare R2
- **Auth:** Supabase Auth (member portal login)
- **Offline support:** Next.js service worker via next-pwa
- **Cameras:** Reolink or similar — separate system, just need admin access URL in dashboard

---

## CURRENT BOOKING DATA TO MIGRATE

29 confirmed future guests. Key data per guest:
- Res ID, first name, last name, property (LT or RMP), check-in, check-out, gross total, amount paid by Campfire, balance still owed by guest, booking source

First check-in: June 30, 2026 (RMP — Amy Degenhard)  
Last check-in: March 24, 2027 (LT — Girl Get After It group, $16,020, only $3,600 paid)

**Priority outreach list (outstanding balances):**
| Guest | Property | Check-in | Owed |
|---|---|---|---|
| Girl Get After It | LT | Mar 27 | $12,420 |
| Lauren Hickey (booking 2) | LT | Feb 15 | $7,510 |
| Jim Zellers | LT | Sep 10 | $5,674 |
| Chrystalina Roberts-Miller | RMP | Mar 7 | $3,733 |
| Vyacheslav Strogolov | RMP | Jul 6 | $2,900 (HipCamp) |
| Dreama Walton | RMP | Aug 30 | $3,046 |
| Ashley Hanbury | RMP | Feb 14 | $2,554 |

**$0 bookings to verify:** William Anuszewski (RMP Jul 6), Perry McCormac (RMP Jul 30) — unknown if comp or error.

Data source: Cloudbeds (being transferred). Full CSV available on request.

---

## JOB: WINTER HUT MANAGER (Lost Trail Lodge — Truckee Area)

See separate file: `JOB_HutManager_LostTrail.md`

---

## FINANCIAL CONTEXT

- LT debt service: $6,500/month → need ~$78K/year in revenue to break even before opex
- RMP debt service: $3,500/month → need ~$42K/year minimum
- Combined minimum revenue target: ~$150K/year (after basic opex) to be cash-flow neutral
- Target revenue: $300-500K combined once fully operational (2-3 year horizon)
- RMP 2025 season revenue (under Campfire): ~$216K full year
- LT projected: similar or higher given whole-lodge pricing power

---

## OPEN QUESTIONS FOR MATT TO DECIDE BEFORE BUILD

1. Domain / brand name — "SIG Lodges"? "Lost Trail Lodge"? Separate brands per property?
2. Membership pricing — what's "reasonable" for day-use in Coldstream Canyon?
3. Sauna access control — lock with member code, honor system, or unstaffed open access?
4. Pet policy
5. Minimum stay requirements (2-night minimum? No minimum for members?)
6. Partner revenue share model — flat referral fee vs. % commission
7. Whether to keep Cloudbeds as the booking backend or replace entirely with custom build
8. Cancellation policy specifics (30/60/90 days, % retained)
9. Pricing strategy — publish rates online or "contact for pricing" for buyouts?

---

## CONTACTS (Do Not Lose)

- **Patrick R. Akers** (Campfire attorney) — pakers@markuswilliams.com — (303) 301-3151
- **Samuel Degenhard** (Campfire founder, has Cloudbeds credentials) — sam@campfireranch.co
- **Heather Kendrick** (SIG's attorney, Kutak Rock) — heather.kendrick@kutakrock.com
- **John Gavan** — repeat guest, 3 bookings across both properties, fully paid, VIP
- **Jim Zellers** — repeat guest, $5,674 outstanding, September booking LT
- **Mountain Trip Guides** — potential RMP partner, already guides at Red Mountain Pass

---

## WHAT TO BUILD FIRST (Suggested Sprint Order)

**Sprint 1 (Days 1-3): Guest rescue**
- Simple landing page: "Your reservation is safe. Here's what happened and what's next."
- Contact form / email capture for the 29 Campfire guests
- Stripe payment link for outstanding balances (per-guest)
- Signed waiver flow (HelloSign) for guests re-confirming under new management

**Sprint 2 (Days 4-7): Core booking**
- Property pages with photos and details
- Availability calendar (both properties)
- Booking form with deposit collection (Stripe)
- Booking confirmation + pre-arrival email sequence
- T&Cs and waiver integrated into booking flow

**Sprint 3 (Week 2): Guest experience**
- QR code guide pages for both properties (offline-capable)
- Audio buttons for key instructions
- Bear safety, emergency contacts, property rules
- Admin dashboard: view bookings, payment status, waiver status

**Sprint 4 (Week 3+): Membership + partners**
- Lost Trail day-use membership signup + Stripe subscription
- Member portal (login, QR code, blackout dates)
- Partner directory + add-on selection in booking flow
- Special event inquiry flow (separate from standard booking)

**Sprint 5 (Ongoing): Revenue optimization**
- Dynamic pricing by season/day
- Upsell email sequences
- Review/testimonial collection
- SEO and content

