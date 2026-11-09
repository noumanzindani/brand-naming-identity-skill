# Visual identity — the studio method at small scale

Sources: Pentagram (Mastercard, Slack, Windows), Wolff Olins (Uber 2018, AOL, London 2012), Collins (Twitch 2019, Dropbox 2017, Mailchimp), Porto Rocha (Twitch 2023, Gemini), JKR (Burger King 2021), DesignStudio (Airbnb 2014, Premier League 2016), Koto (Bolt), Linear. Full research report: `docs/research.md`.

## 1. Immerse & audit equity

- For a rebrand: list every asset users recognise (colour, mark, sound, mascot, phrase, layout). Collins/Twitch: sort into **advance / leave behind / amplify**.
- For a new brand: audit the category's visual landscape — screenshot 8–12 competitors' icons, store pages and onboarding. Find the sea of sameness (Koto/Bolt escaped "everyone is blue" with bright yellow).
- Big-brand rule: winning routes usually **sharpen what's recognised** — Mastercard kept circles, Slack kept the octothorpe, Premier League kept the lion (~90% of 1,000+ fans linked it), Twitch kept purple.

## 2. Principles / reframing question

Turn the brief into 2–3 testable design principles or one sharp question:
- Wolff Olins / Uber: "let in the light, embrace black", "invest in a wordmark, not a symbol", "bring back the U".
- Paula Scher / Windows: "Your name is Windows. Why are you a flag?" → a real window in perspective.
- Collins / Twitch: "What made people first fall in love with Twitch?"

Write them so a route can clearly pass or fail them.

## 3. Routes

No standard number at top studios (Armin Vit shows 3–5; some studios show one). For this skill: **2–3 genuinely different routes**, then recommend one. Each route:

| Element | Decide |
|---|---|
| Idea | one sentence linking back to the associations |
| Mark | wordmark vs symbol vs monogram; concept sketch in words; silhouette test |
| Colour | 1 brand seed + 1 accent + neutrals; give them names (Burger King: Fiery Red, Melty Yellow); reserve a colour for a meaning (Uber "safety blue" for assurance) |
| Type | display + text pairing; open-source is fine (Inter, Manrope, Plus Jakarta Sans, Space Grotesk, DM Sans, Outfit, IBM Plex, Noto Nastaliq Urdu / Noto Naskh Arabic for Urdu/Arabic UI) |
| Shape | corner-radius language (sharp 4 / soft 12 / pill), stroke weight, icon style |
| Motion | feel (snappy 150–200 ms / calm 300–400 ms), easing, signature transition |
| Imagery | photo vs illustration, style rules |
| Voice | 3–4 "X, not Y" rules + sample microcopy (empty state, error, push) |
| Flexible layer | the one thing that varies: pattern, illustration system, variable font, layout grid, artwork behind a fixed mark |

Linear's Karri Saarinen: **typography and consistency do more for perceived quality than the logo** — good news when there's no budget for a custom typeface.

## 4. System, not logo

- Few fixed constants + one generative layer (Mastercard parametric circles, Burger King variable font, AOL changing artwork, Porto Rocha's Twitch layout toolkit).
- Rebuild the mark for small screens; it must work as a **one-colour silhouette at 16–48 px**.
- Provide light **and** dark tints/shades of the brand colour (Twitch 2023 added these explicitly).
- Deliver as tokens + component examples, not a PDF manual.

## 5. AI and the mark

- Use image models for exploration; a human redraws the chosen direction as vectors with deliberate changes; reverse-image search; trademark knockout.
- US Copyright Office (Jan 2025): "prompts alone do not provide sufficient human control" → raw AI output isn't copyrightable; human selection/modification can be. Supreme Court declined *Thaler* (2 Mar 2026). Trademark registration is still possible if distinctive and cleared.
- Pentagram precedent: humans set the style, Midjourney produced ~1,500 icons within it (Performance.gov) — and drew backlash.

## 6. Scale reality (what NOT to copy)

Mastercard 6+ months, Uber ~9 months, Burger King 2 years; teams 4–25; London 2012 design fee £400k; boutique identity $5–20k; freelancer basic identity $1–5k; logo-only $500–3k; 99designs contests $249–1,050 (plagiarism risk — buyer polices it; AIGA opposes spec work). Identities get refreshed every ~4–7 years, often by a different studio.

## 7. Tools

If connected: Figma MCP (build routes, components, variables), Stitch (generate screens with a design system), Canva. Otherwise describe routes precisely and generate an HTML preview page / Flutter sample screen showing colour, type and components in light & dark.
