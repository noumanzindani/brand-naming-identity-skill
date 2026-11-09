# Brand Naming & Identity Skill

**By Nouman Zindani**: an open-source Claude Agent Skill that runs the process top agencies use for naming and identity. It covers the naming funnel used by Lexicon and Catchword, the identity method used by Pentagram, Wolff Olins and Collins, and turns the result into a token-driven Flutter app theme. It works as an interactive workshop and is sized for a solo developer or a small studio.

> Agencies don't win on genius; they win on **judgment under constraint**: strategy and criteria before options, volume from deliberately diverted angles, cheap checks before expensive ones, and a decision protected from the pull toward "safe".

## What it does

| Step | What happens |
|---|---|
| 1. Brief | One round of questions, then a one-page brief: onliness statement plus competitor-swap test, 2–3 core associations, personality, voice, and a **scorecard written before any names exist** |
| 2. Generate | 300+ candidates from four lanes: the real brief, a competitor's brief, a diversion brief (Lexicon's trick) and sound/roots |
| 3. Screen | Cheap gates first: SCRATCH deal-breakers, pronunciation across target languages, domain-sensitive meanings, 30-char store titles, knockout searches |
| 4. Score | Weighted scorecard, computed rather than eyeballed |
| 5. Shortlist | 8–12 names in **safe ↔ bold pairs**, each with a story, store title, spoken line and push-notification line, plus Lexicon-style decision coaching |
| 6. Validate | Costed checklist: IPO-Pakistan / USPTO / WIPO / TMview, Nice classes, Madrid Protocol, native-speaker panels, attorney clearance |
| 7. Identity | Equity audit, design principles, 2–3 routes, and a system rather than just a logo (mark works as a one-colour silhouette at 16–48 px) |
| 8. Flutter theme | DTCG 2025.10 design tokens, `ColorScheme` (deliberate variant, light/dark/high-contrast), contrast verified on the *generated* scheme, iOS Icon Composer and Android adaptive icon specs |

It only runs the steps you ask for. Naming stops at the shortlist and offers identity and theme as the next step.

## Install

```bash
git clone https://github.com/noumanzindani/brand-naming-identity-skill ~/.claude/skills/brand-naming-identity
```

Claude Code picks it up automatically. Then ask in plain words:

- "name my new app — it helps … for …"
- "is 'Time Vault' a good name? trademark safe?"
- "rebrand my marketplace app, Pakistan + UAE"
- "turn my brand colour #FFC300 into a Flutter theme"

## Contents

```
SKILL.md                         workflow (≈150 lines)
references/naming-techniques.md  funnel numbers, name types, generation lanes, sound symbolism, origin stories
references/validation.md         trademark/linguistic/app-store/domain checks, myths vs verified failures
references/visual-identity.md    studio method, routes, system thinking, AI & copyright
references/flutter-theme.md      DTCG tokens, ColorScheme variants & fixes, contrast test, icon specs
scripts/contrast_check.py        WCAG 2.2 contrast checker (stdlib, exits 1 on failure)
scripts/screen_names.py          length / store-title / spellability / .com DNS signals (stdlib)
evals/evals.json                 test prompts + assertions
docs/research.md                 the cited research report the skill is built on
```

## Evaluation

The skill was tested on three realistic prompts, each run with and without it, and graded against objective assertions:

| Iteration | With skill | Without skill |
|---|---|---|
| 1 | 100% | 69% |
| 2 (harder assertions + new eval) | 96% | 62% |

## Caveats

- This is not legal advice. A knockout screen means "keep investigating", not "safe". Clear the final name with a trademark attorney.
- Pakistan trademark fees and timelines in the references come from secondary sources, so check them with IPO-Pakistan.
- Language and cultural flags raised by the model need confirming by native speakers.

## License

Apache-2.0
