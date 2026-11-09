---
name: brand-naming-identity
description: Runs the top-agency brand process (Lexicon/Catchword naming funnel + Pentagram/Wolff Olins/Collins identity method) as an interactive workshop — brief, strategy, name generation, screening, shortlist, visual identity, and a token-driven Flutter app theme. Use this whenever the user wants to name or rename anything (an app, startup, product, feature, company, studio, sub-brand), asks "what should I call…", wants name ideas, a tagline, a logo direction, brand colours, a brand identity, a rebrand, a visual theme or design language, an app icon concept, or wants to turn a brand into a Flutter ThemeData/ColorScheme or design tokens — even if they never say "branding". Also use when they ask whether an existing name/theme is good, trademark-safe, or app-store-ready.
---

# Brand Naming & Identity

Agencies don't win on genius; they win on **judgment under constraint**: write the strategy and the evaluation criteria *before* any options exist, generate far more than feels necessary from deliberately different angles, kill candidates with cheap checks before expensive ones, and protect the decision from the client's pull toward "safe". This skill runs that funnel at solo-developer scale. Read the reference files only when you reach the step that needs them.

The user is usually an app developer (Flutter, often Pakistan-based, several apps). Tailor examples to that, but the process works for any brand.

## 0. Scope the job

Figure out which slice is wanted — don't run all 8 steps for a colour-palette question.

| Request | Run steps |
|---|---|
| "Name my app/product/company" / "rename X" | 1 → 6, then **stop and offer** 7–8 in one line |
| "Create my brand from zero" / "full rebrand incl. look" | 1 → 8 across several turns (name first, identity after a name is chosen) |
| "Brand identity / colours / logo direction / theme" for an existing name | 1 (short) → 7 → 8 |
| "Turn our brand into a Flutter theme / tokens" | 8 only (ask for brand colour, type, feel) |
| "Is this name good / safe?" | 3 + 6 on that name; verdict + a few alternatives if it fails |

When offering the next slice, describe it generically ("a visual identity + Flutter theme built from tokens") — don't promise a specific technique like `fromSeed` before you've seen the brand colour.

Deliver only the slice that was asked for. A naming answer that also ships identity routes, tokens and Dart files buries the decision the user actually has to make; identity work is wasted until a name is chosen anyway. Offer the next slice instead of doing it.

If the current working directory is the project in question, read `pubspec.yaml`, `README*`, store listing files and existing theme code first — it shortens the brief and shows the current equity. Don't go hunting through other folders for a project the user didn't point you to; if you suspect one exists, ask.

## 1. Brief — the workshop (ask, don't assume)

Ask **one batch** of 3–6 questions (use AskUserQuestion if available; otherwise a numbered list). Skip anything the repo already answers. Cover:

1. What it does and for whom — the audience and their *state of mind* when they first meet the name (stressed commuter? curious teen?).
2. The 3–5 ideas/feelings the name or identity must convey, and what it must *not* feel like.
3. Personality sliders — have them pick a side for 4–5 pairs, e.g. Playful↔Serious, Bold↔Calm, Premium↔Accessible, Modern↔Heritage, Local↔Global.
4. Markets & languages (e.g. Pakistan + Gulf + global English) → drives linguistic screening.
5. Brand architecture: standalone brand, or under a studio/master brand? (A branded house means new apps need only a descriptor — cheaper to clear and market.)
6. Constraints: names already rejected/loved, name style preference, must-have domain or not, budget for clearance/design.

Then write the **one-page brief** and show it before generating anything:

- **Onliness statement** (Neumeier): *Our [what] is the only [category] that [differentiator] for [who] in [where] because [why] in an era of [when].* Run the **competitor-swap test** — put a competitor's name in; if it still fits, sharpen it.
- **2–3 core associations** (Ritson: one page, not an "essence/DNA/values" stack).
- **3–5 personality traits** + tone rules as "X, not Y".
- **Evaluation criteria, written now** — the scorecard in step 5 with any weight changes the user wants. Writing criteria before options is the single most valuable agency habit: later choices get judged against strategy, not taste.

Get a quick "yes / tweak" on the brief. It's also the prompt for everything that follows.

## 2. Generate — wide, from diverted angles

Generate **300+ candidates internally** (judgment banned at this stage — strong names typically appear only after the obvious ones are exhausted). Do it in separate lanes so you don't anchor on the first idea; if you have subagents, running lanes in parallel with *different briefs* reproduces Lexicon's parallel-team trick more faithfully:

- **Lane A — the real brief.**
- **Lane B — "you're naming the competitor"** that wants to beat this product.
- **Lane C — diversion:** a different object with the same emotional job (Lexicon named Windsurf while thinking about "flow", not IDEs; BlackBerry signalled joy, not email stress).
- **Lane D — sound & roots:** Latin/Greek/Arabic/Urdu/Persian roots, compounds ("1+1=3": PowerBook), invented words engineered for sound.

Cover all four name types — Descriptive (weakest), Invented, Experiential, Evocative (strongest) — and lean toward suggestive/arbitrary/coined, which are legally stronger. Techniques, sound-symbolism rules and the type taxonomy: `references/naming-techniques.md`.

## 3. Screen — cheap gates first

Cut to ~20–30 internally with pass/fail gates, then score. Never show the user the 300.

Gates (fail any → out):
- **SCRATCH deal-breakers:** Spelling-challenged, Copycat, Restrictive, Annoying, Tame, Curse of knowledge, Hard to pronounce.
- **Pronounceable & clean** in every target language — for Pakistan check Urdu, Roman-Urdu spellings, Punjabi, Pashto; Arabic for the Gulf. Flag anything you're unsure of for a native speaker rather than guessing.
- **Store-ready:** brand ≤ ~12 chars so "Brand: descriptor" fits the 30-char App Store / Play title.
- **Not descriptive/generic** (weak trademark) and **not obviously taken** in the category.
- **Domain-sensitive meanings:** for finance in Pakistan/Gulf, flag anything that evokes interest/riba (e.g. "tenor", "yield", "rate"), gambling, or religious terms that a product would trivialise (e.g. مہر *mehr*, the marriage dower, for a wedding-savings app). Health, kids and food have their own equivalents — think about who could be offended or misled.

Then run `scripts/screen_names.py` on the survivors for length/store-title/.com-DNS signals, and do quick web/store searches on the top ~10 for live apps or brands in the same class. Label all of this as a **knockout screen, not clearance**. Details: `references/validation.md`.

## 4. (internal) Score

Score survivors 1–5 on the brief's criteria. Default weights (adjust to what the user said in step 1):

| Criterion | Weight |
|---|---|
| Fit with the 2–3 core associations | 3 |
| Distinctiveness in category (incl. trademark strength) | 3 |
| Sound & pronunciation across target languages | 2 |
| Memorability / spellability after hearing it once | 2 |
| Room to grow (not restrictive) | 1 |
| Store/domain/handle practicality | 1 |

Max = 60. Compute totals with code (a quick Python one-liner) rather than mental arithmetic, and show the per-criterion row so the user can check it — a visible sum that doesn't add up undermines trust in the whole shortlist.

## 5. Present the shortlist — protect against "safe"

Present **8–12 new names**, grouped by type, as **safe ↔ bold pairs** (the current name, if any, is a reference line, not a slot). Keep the reply tight — a brief, a cuts table, the shortlist and the next steps; the 300-name longlist and full scoring sheet go in a file or stay internal. Aim for something the user can read in five minutes. For each:
- the name, type, and a 1–2 line story (why it fits the associations)
- in context: store title (`Brand: descriptor`), a spoken sentence ("I booked it on ___"), and a push-notification line
- score + any flags (needs native-speaker check, possible conflict)

Then coach the decision the way Lexicon does:
- Ask "what could this name *do* for us?" before anyone criticises.
- **Competitor test:** "A competitor just launched with this name — how do you feel?" Dread = strong.
- A split reaction is a good sign (Intel split on Pentium). Unanimous comfort usually means tame.
- If they test with users, test **believability, comprehension and pronunciation — never preference**; consumers reject exactly the names that become great brands.

Iterate: take their reactions, generate a new round in the liked direction, re-screen. 2–3 rounds is normal.

## 6. Validate the finalists (1–3 names)

Give a concrete, costed checklist — knockouts on IPO-Pakistan, USPTO, WIPO Brand DB, TMview in the right Nice classes (9, 42 + service class); app stores; domains/handles; 3 native speakers per key language; then an attorney clearance opinion on the winner and filing (IPO-Pakistan as Madrid base if going international). Exact links, fees, classes and the myths-vs-real-failures list: `references/validation.md`. Be clear this is not legal advice and that Pakistani fee figures need checking with IPO.

## 7. Visual identity

Run the studio method at small scale (`references/visual-identity.md`):
1. **Equity audit** (rebrands): what do users already recognise? Sort into *advance / drop / amplify*. Keep and sharpen recognised assets — the verified disasters (Gap, Tropicana, Twitter→X) threw them away.
2. **Reframing question / 3 design principles** derived from the brief (Wolff Olins Uber: "invest in a wordmark, not a symbol").
3. **2–3 routes**, each: idea, mark concept, colour (seed + accent + neutrals with names), type pairing (open-source, e.g. Inter / Manrope / Space Grotesk), shape language (corner radius), motion feel, imagery, voice ("X, not Y"). Recommend one.
4. **System, not logo:** a few fixed constants + one flexible layer. The mark must work as a **one-colour silhouette at 16–48 px** — that feeds the app icon, Android monochrome layer, iOS tinted/clear variants, notifications and favicon.

If Figma / Stitch / design tools are connected, offer to mock the routes there. Recommend a human redraw of any AI-generated mark (prompt-only output isn't copyrightable in the US; trademark still possible if distinctive and cleared).

## 8. Brand → app theme (Flutter)

Follow `references/flutter-theme.md`:
- Express the identity as **DTCG tokens** (`brand.tokens.json`): brand seed + exact hex, neutrals, type, 4/8 spacing, radius, elevation, motion.
- Generate `ColorScheme.fromSeed` with a **deliberate `dynamicSchemeVariant`** mapped from the personality sliders (bold → `fidelity`/`vibrant`; calm → `tonalSpot`), light + dark + `contrastLevel` high-contrast variant; override `primary` only if the exact hex is mandatory. Then neutralise the seed-tinted surfaces if the brand wants clean greys. For very light or very saturated brand colours (yellow, lime, cyan) use the colour as a *fill with dark ink on it*, not as text on light backgrounds — see the reference for when to hand-build roles instead.
- Verify the **generated** theme, not just the brand hexes: brand pairs via `scripts/contrast_check.py`, and — when Flutter is installed — a contrast unit test over the real `ColorScheme` roles plus `flutter analyze` in a scratch project. WCAG 2.2: 4.5:1 text, 3:1 large text/UI/icons, in **both** modes. Fix failures before handing over and report the tightest passes.
- Icon specs for iOS Icon Composer (layered 1024², six appearances) and Android adaptive (108 dp, 66 dp safe zone, monochrome layer).

Before writing files into the user's project, say which files you'll create/modify and get a yes.

## Deliverable

End with a compact **Brand Sheet** (and offer to save it as `BRAND.md` / `brand/` in the project):

```
Name: … (type) — story in one line
Store title: …            Domain/handles: … (status)
Onliness: …
Associations: … · … · …     Traits: …     Voice: X, not Y; …
Colours: seed #…, accent #…, neutrals …  (variant: …, contrast checked ✔)
Type: display …, text …     Radius: …     Motion: …
Icon: silhouette rule …
Open risks / next checks: trademark clearance in classes …, native-speaker check in …
```

## Principles to keep in mind

- Strategy and criteria before options; options before opinions.
- Volume and diversion beat cleverness — but show only the curated few.
- Cheap checks early, expensive checks only on finalists.
- Bold names feel uncomfortable at first; that's information, not a veto.
- For apps the theme reaches users more than the logo does — build it from tokens and check contrast.
- Be honest about uncertainty: knockout ≠ clearance; language checks you can't verify go to native speakers.
