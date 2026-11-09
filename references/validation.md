# Validation — screening names cheap → expensive

Not legal advice. A knockout screen says "keep investigating", never "safe". Full research report: `docs/research.md`.

## Contents
1. The cost-ordered funnel
2. Trademark knockouts (where & how)
3. Pakistan & international filing
4. App stores
5. Domains & handles
6. Linguistic / cultural screening
7. Consumer & design testing
8. Myths vs verified failures

## 1. Funnel

| Stage | On how many | Cost | What |
|---|---|---|---|
| Gates (SCRATCH, pronounceability, store length) | ~300 → 30 | free | your judgment + `scripts/screen_names.py` |
| Knockout search | ~20–30 | free | registers + stores + web below |
| Native-speaker check | 3–7 | low | 3 speakers per key language |
| Full clearance + attorney opinion | 1–3 | ~$300–$2,000 | registers + common-law use + opinion |
| Filing | 1 | fees below | IPO-Pakistan / USPTO / Madrid |

Litigation after a conflict runs "well into six figures" — that gap is the case for clearance.

## 2. Trademark knockouts

Search exact name, phonetic variants, and visual look-alikes, in the relevant **Nice classes**: apps usually **9** (downloadable software) and **42** (SaaS/platform), plus the underlying service class (e.g. 39 transport for ride-hailing, 36 finance, 35 marketplaces/advertising, 41 education/entertainment, 44 health/beauty, 45 personal services). That class mapping is general practice — confirm with an attorney.

- USPTO Trademark Search — https://tmsearch.uspto.gov (replaced TESS 30 Nov 2023)
- WIPO Global Brand Database — https://branddb.wipo.int
- EU TMview — https://www.tmdn.org/tmview
- IPO-Pakistan — https://ipo.gov.pk (e-filing/search since 14 June 2023)
- Plus: Google search "<name> app", both app stores, Product Hunt, Crunchbase, GitHub, social platforms.

Likelihood-of-confusion logic (USPTO): similar sound/appearance/meaning **plus** related goods/services. "T. Markey" vs "Tee Marquee" conflict; Dove soap and Dove ice cream coexist. So a same-name app in a different class is a smaller risk than a sound-alike in your own class.

## 3. Pakistan & international filing

- Pakistan joined the **Madrid Protocol on 24 May 2021** → an IPO-Pakistan application can be the base for one international application (133 countries; WIPO base fee CHF 653 + per-country fees).
- Reported IPO-Pakistan fees ≈ **PKR 3,000/class to file, PKR 9,000 to register**; timeline 12–30 months. *Secondary sources — verify on ipo.gov.pk before quoting as fact.*
- USPTO: **$350 per class** (fees effective 18 Jan 2025), surcharges for free-form descriptions/insufficient info.
- Typical order for a Pakistani app studio: clear → file IPO-Pakistan (classes 9/42/+service) → Madrid designation for US/UK/EU/UAE/KSA as needed.

## 4. App stores

- **Apple 2.3.7:** app name ≤ **30 chars**, unique; no keyword stuffing, prices, other brands' trademarks, or "#1/best" claims. 4.1 / 5.2.1: no copycat names/icons.
- **Google Play:** title ≤ **30 chars**; no emoji, ALL CAPS gimmicks, "#1"/"best"/"free" style claims, or performance/ranking promises.
- Pattern: short brand (≤ ~12 chars) + descriptor → "Gig: Find Local Work". Brand stays distinctive, descriptor feeds search.
- **Apple Product Page Optimization:** up to 3 alternate icon/screenshot treatments, up to 90 days, act at 90% confidence; alternate icons must already ship in the binary → plan one release ahead. Google Play store listing experiments offer similar A/B (variant limits from secondary sources).

## 5. Domains & handles

- Paul Graham (2015): own the .com if you're a US startup (94% of top-50 YC companies did). But only ~53% of YC W24 chose .com, and Placek calls .com "just an area code".
- For apps: store uniqueness + title fit are the binding constraints. Acceptable fallbacks: `get<name>.com`, `<name>app.com`, `<name>.app`, `.io`, `.ai`, `.pk` for a local brand. Avoid a fallback that's a *different* live brand's .com.
- Check matching handles on Instagram, X, TikTok, YouTube, LinkedIn, Facebook.
- `scripts/screen_names.py` checks whether `<name>.com` resolves in DNS — a resolving domain is likely taken; non-resolving is only *possibly* free (verify with a registrar).

## 6. Linguistic / cultural screening

- Catchword method: **3 native speakers per language, living in-market**, interviewed in depth; ~115 languages; ~2 weeks; vet a 7–10 name shortlist. Company staff abroad give subjective answers — don't rely on them.
- Check: meaning, slang, sound-alikes, pronunciation difficulty, how it's spelled when heard, religious/political sensitivity, and **Roman-Urdu** renderings.
- Pakistan default panel (inferred from market): Urdu, Punjabi, Pashto, Sindhi, English; Arabic for Gulf. Add others per export market.
- You (Claude) can flag likely issues, but mark them "needs native-speaker confirmation" rather than declaring a name clean.

## 7. Testing

- Names: test **comprehension, pronunciation, spelling-from-hearing, associations, red flags — never preference**. Catchword: "consumers reject exactly the type of names that make great brands." A Hundred Monkeys avoids focus groups entirely.
- Lexicon tests **believability** ("could this name stand for a product that does X?").
- Identity: recognition (Mastercard: 81% recognised the symbol without the name), legibility at small sizes, app-icon test at 29–60 pt on real wallpapers, WCAG contrast, then real-traffic A/B via PPO.

## 8. Myths vs verified failures

| Story | Verdict |
|---|---|
| Chevy Nova flopped in Latin America ("no va") | **Myth** — sold well in Mexico/Venezuela |
| Ford Pinto renamed Corcel in Brazil | **Myth** — Pinto never sold there |
| KFC "eat your fingers off" in China | **Unverified** — no primary source |
| Mitsubishi Pajero → Montero | Partly true (renamed in Spanish markets; reason not officially confirmed) |
| Gap 2010 logo | **Verified** — reversed after ~6 days |
| Tropicana 2009 pack | **Verified** — ~20% unit sales drop, reverted after ~7 weeks |
| Twitter → X | **Verified** — ~900 existing US "X" registrations; 55% of US daily users still said "Twitter" in 2025 |
| Jaguar 2024 | Backlash real; sales collapse mostly due to halting petrol production |

Lesson: the real disasters are identity changes that **discard recognised assets**, not foreign-language naming blunders.
