# Example: a Europe → Gulf money-transfer app (Round 1)

A real run of the skill, from a blank page to a name shortlist.

**Input from the user:** an app that sends money from Europe to the Gulf, used mostly by Arabic speakers who are *worried* when they first find it. It must feel trustworthy, easy, fast and premium. Competitors named were NayaPay, Altras, Cashi and Graishat. It is a standalone brand, and the user's favourite names were "Fastran" and "Maalapp".

| File | Step | What it shows |
|---|---|---|
| `01-brief.pdf` / `.html` | 1 · Brief | Onliness statement and competitor-swap test, 3 associations (Certainty · Swiftness · Dignified care), voice rules, a first look at the favourites, hard gates, and a scorecard written before any names (max 65) |
| `longlist_internal.md` | 2 · Generate | About 320 candidates across 4 lanes (real brief, competitor, diversion objects, sound and roots) |
| `screen_names_output.txt` | 3 · Screen | `scripts/screen_names.py` output: length, store title, .com DNS |
| `scores.csv` | 4 · Score | Weighted scores, computed with code |
| `02-shortlist.pdf` / `.html` | 5 · Shortlist | 8 names in safe ↔ bold pairs: Safir/Hudhud, Certa/Akeed, Wasla/Qasid, Surely/Rasil. Includes a table of cuts with reasons, in-context store titles and notifications, and decision coaching |

**Lessons from this run:**
- The user's favourite "Fastran" is one letter away from Qatar's national instant-payment system, Fawran.
- "Maalapp" contains *mal*, which means "bad" in the French, Spanish and Italian sending markets.
- "Sila" and "Wafi" were cut because of live payments brands with the same names.

These are knockout screens from web and app-store searches on 10 Nov 2026. They are not trademark-register searches and not legal advice. PDFs were rendered from the HTML with headless Chrome.
