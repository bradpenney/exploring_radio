# CLAUDE.md

This file provides guidance to Claude Code when working with this repository.

## Repository Overview

**Exploring Radio** teaches amateur radio to any curious adult, from studying for the Canadian Amateur Radio Operator Certificate to building antennas, understanding propagation, and making real contacts. It follows the same editorial standards as the other exploring_* sites.

This is a **hobby site**, like exploring_electronics and exploring_cnc. It isn't a career booster the way exploring_kubernetes or exploring_gitops are. The bar for accuracy is the same, though. A wrong frequency, power limit, or safety number here is as serious as a wrong command on the Kubernetes site. Some of these mistakes can put a reader outside the law or near a lethal hazard.

**Target Audience:** Anyone in Canada who wants to get on the air: hobbyists, preppers and emergency-communications volunteers, outdoors people, retirees, makers, and technical professionals. No electronics, radio, or coding background is assumed. Many readers arrive while studying for the Basic Qualification exam, and the site should get them through it *with understanding*, not by memorising the question bank.

**Brad's priority (2026-09-30, his words):** "while passing the exam is a concern, understanding this stuff is MUCH more important." He writes the Basic exam in December 2026 aiming for 100%, and expects to clear it easily. Every article goes deeper than the exam asks (mechanism, the why, where the simple model breaks). The exam gets a short "On the exam" aside; it never decides an article's shape.

**Teaching Philosophy:** Every concept is grounded in something a reasonable adult already understands (ripples on a pond, a stadium crowd doing the wave, tuning a car radio) before the formal name or the formula appears. The exam is a milestone, not the goal. The goal is an operator who knows *why* the rules and the physics are what they are.

**Status (2026-10-08):** four pages (Start Here, Getting Your Certificate, The Amateur's Code, the Anki deck). Not yet a git repo, and Brad is holding it back until there's enough content to launch; DNS, GitHub Pages, and hub links are his steps. Electronics is live (pushed 2026-10-01), so Start Here's links all resolve. First article planned: "Getting Your Amateur Radio Certificate in Canada" (Getting Licensed, B-001).

**Author's journey:** Brad is studying for the Basic Qualification right now (started 2026-09-30) and doesn't have a call sign or any gear yet. Like the CNC site's X-Carve, Brad's own station becomes the worked example **as he actually acquires it**. Never invent equipment, a call sign, or on-air experience for him. Until he owns something, examples use generic, clearly representative gear ("a typical 5 W dual-band handheld").

## Diagrams: 3D Figures, Not Mermaid (estate-wide, 2026-09-30)

**This overrides every mermaid instruction elsewhere in this file.** Brad, 2026-09-30: mermaid "loses its value as declarative diagrams once you're available to improve/tweak", and it looks poor next to hand-built figures. He also asked for "AS MANY DIAGRAMS as possible".

- **No new mermaid.** Every diagram is a hand-built, 3D-lit SVG emitted by a standard-library Python generator in this repo's `illustrations/<article>.py` (one script per article, output under `docs/images/<article>/`). Mermaid already in published articles is legacy debt: replace it when the article is touched.
- **House style** (copy `illustrations/style3d.py` from exploring_electronics or exploring_radio): radial-gradient lit spheres, glassy translucent shells and panels, gloss overlays, drop-shadow ellipses, depth-sorted perspective, glow via radial gradients, the shared amber/slate palette, transparent background. The reference figures are `exploring_electronics/illustrations/conductors_and_insulators.py`.
- **Numbers come from sources.** Anything plotted cites its source in the generator's docstring, and the generator computes it rather than hard-coding a drawn shape.
- **Look before shipping.** Render every figure to PNG (`magick -background '#1e1e1e' -density 96 fig.svg -flatten fig.png`) and read it: fix overlaps, clipped labels, and anything that teaches something false.
- **Gotchas:** escape text for XML (`&` vanishes otherwise); an SVG blur filter on a perfectly horizontal or vertical line has a zero-height box and disappears, so fake that glow with a soft rect.
- **Never replace schematics.** Real circuit schematics in standard notation (schemdraw) stay exactly as they are: Brad, 2026-09-30, "readers need to be comfortable with these." They are a 2D language the reader is learning to read, so they are never converted to 3D, and articles that show a circuit should keep (or add) its schematic alongside any 3D figure. Photos stay too. The 3D rule replaces mermaid and decorative flat illustrations only.
- Reference each figure with `<figure markdown>` + `![alt](...){ width="..." }` + `<figcaption>`, with alt text that describes what the figure shows.

## Regulatory Frame: Canada Only

This site teaches **Canadian** amateur radio. It does not cover FCC rules, US licence classes (Technician/General/Extra), or ARRL band plans except in a passing note where a reader would otherwise be confused (for example, a US-published book they picked up). Never present a US rule as if it applied in Canada.

### Primary sources (the only authorities for regulatory claims)

| Source | What it governs | Current version (verified 2026-09-30) |
|---|---|---|
| [Radiocommunication Act](https://laws-lois.justice.gc.ca/eng/acts/r-2/) | The legal authority for everything below | Consolidated online |
| [RBR-4](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/regulations-reference-rbr/rbr-4-standards-operation-radio-stations-amateur-radio-service) | Operating standards: bands per qualification, power, bandwidth, identification | Issue 3, July 2022 |
| [RIC-3](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/radiocom-information-circulars-ric/ric-3-information-amateur-radio-service) | Qualifications, privileges, exam structure, the Basic syllabus | Issue 5, March 2022 |
| [Basic Qualification question bank](https://ised-isde.canada.ca/site/amateur-radio-operator-certificate-services/en/downloads) | The exam's actual question pool | 15 July 2025 edition |
| [RIC-1](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/radiocom-information-circulars-ric/ric-1-guide-examiners-accredited-conduct-examinations-amateur-radio-operator-certificates) | How exams are administered by accredited examiners | Check at write time |
| RIC-9 (Call Sign Policy) | Call sign prefixes and formats | Check at write time |
| Health Canada **Safety Code 6** + ISED **RSS-102** | Radio-frequency (RF) exposure limits | Check at write time |
| ISED **CPC-2-0-03** | Antenna system siting and land-use consultation | Check at write time |
| [Radio Amateurs of Canada (RAC)](https://www.rac.ca/) band plans | Voluntary band-usage conventions (not law) | Check at write time |

**Rules for regulatory content:**

- **Never state a regulatory fact from memory.** Fetch the current ISED document with WebFetch at write time, cite it inline, and name its issue or date. ISED revises these documents, and a stale number published confidently is the worst failure this site can have.
- **Law vs convention.** RBR-4 is law, and a RAC band plan is a gentlemen's agreement. Every frequency statement must say which one it comes from. "The 2 m band is 144–148 MHz" (RBR-4) is not the same kind of claim as "FM simplex calling is on 146.520 MHz" (band-plan convention).
- **Re-verify on edit.** When touching a published article that states a regulatory number, re-check that number against the source.
- **Terminology.** In Canada, amateurs hold an **Amateur Radio Operator Certificate** with one or more **qualifications** (Basic, Basic with Honours, Advanced, Morse code). There is no separate station licence. Use "certificate" and "qualification" in regulatory contexts. "Licence" is fine colloquially (it's what people search for), but the first use in an article should say what the formal term is. Use Canadian spelling throughout: *licence* (noun), *license* (verb), *metre*, *colour*, *centre*.

### Verified facts (2026-09-30, from RIC-3 Issue 5 / RIC-1 / RBR-4 Issue 3; RBR-4 items re-read in full 2026-10-08, still Issue 3, July 2022)

These were checked for the site scaffold. Re-verify before publishing them in an article.

- The Basic exam has **100 questions**, one drawn from each of 100 topic areas. The pass mark is **70%**, and **80%+ is Basic with Honours**.
- **Basic** gives access to all amateur bands **above 30 MHz**. **Basic with Honours** adds all bands **below 30 MHz** (HF). **Morse code** (5 words per minute, 100% receiving pass mark) combined with Basic also gives HF access, and so does Basic combined with **Advanced** (RBR-4 Schedule I lists every band below 30 MHz as "B and 5, B/H, B and A", and every band above it as "B"; Schedule I runs from 135.7 kHz to 250 GHz, with a maximum bandwidth per band in Column II).
- **Advanced** is a separate **50-question** exam with a **70%** pass mark. It adds higher power, the right to build and modify transmitters, the right to set up repeaters and club stations, and remote control.
- **Power (RBR-4 section 10):** Basic: 250 W DC input "to the anode or collector circuit of the transmitter stage that supplies radio frequency energy to the antenna", or, as RF output "measured across an impedance-matched load", 560 W PEP for any single-sideband emission or 190 W carrier power for any other emission. Advanced: 1,000 W DC input, or 2,250 W PEP (SSB) / 750 W carrier. Section 10.1: an amplifier at the station "shall not be capable of exceeding by more than 3 dB" those limits. Quote RBR-4 directly when publishing this, because the definitions matter.
- **Identification (RBR-4 section 9):** "in English or French, at the beginning and end of each period of exchange of communication or test transmission, and at intervals of no more than 30 minutes throughout."
- **Other RBR-4 rules worth an article:** unmodulated carriers below 30 MHz only for brief tests; AM limited to 100% modulation; stations need a way to determine transmit frequency to crystal-calibrator accuracy and to indicate or prevent overmodulation (section 11); antenna siting follows CPC-2-0-03 (section 12); change of mailing address to ISED within 30 days (section 13).

## Site Boundaries: Radio vs Electronics

The exam's **B-004 Circuit Components** and **B-005 Basic Electronics and Theory** overlap heavily with [exploring_electronics](https://electronics.bradpenney.io). The no-repetition rule applies *across* sites too:

- **exploring_electronics owns** DC circuit theory: voltage, current, resistance, Ohm's law, series/parallel, reading schematics, resistor codes, general components, and microcontrollers. Radio articles **link to** these and never re-teach them.
- **exploring_radio owns** everything that only matters because of radio frequency: frequency and wavelength, alternating current (AC) as it applies to RF, reactance, resonance, tuned circuits, impedance matching, decibels, modulation, antennas, feedlines, propagation, interference, RF exposure, and operating.
- **The bridge pattern:** when an exam section needs DC basics, write a short radio-angle bridge ("the exam asks you to compute power in a dummy load, which is Ohm's law, covered on Exploring Electronics"), link out, and then add only what is radio-specific.
- If radio genuinely needs an electronics concept that exploring_electronics hasn't published yet, **flag it to Brad** as a gap on the electronics site rather than writing it here. It belongs there.
- Before writing any article in Radio Fundamentals, check exploring_electronics' `mkdocs.yaml` for what's published.

### "Before This" Prerequisites (Brad, 2026-10-01)

Readers need electricity before radio, and that material lives on exploring_electronics. Two mechanisms carry it:

- **`docs/start_here.md`** is the ordered path: each electronics article it depends on, a one-line "why it matters for radio", and the exam topics (question-bank IDs, e.g. `B-005-002`) it covers. When electronics publishes a page radio needs (inductors and capacitors, diodes, transistors), add a row there. Its figure is a clickable transit map from `illustrations/start_here.py`, inlined with a snippets `--8<--` line so its links work (an `<img>` kills links); keep its stops and numbers in sync with the table.
- **Every radio article's difficulty admonition names its prerequisites** in one sentence with absolute links, e.g. *"Before this: [Ohm's Law and Power](https://electronics.bradpenney.io/ohms_law/) and [AC vs DC](https://electronics.bradpenney.io/ac_dc/)."* Absolute `https://electronics.bradpenney.io/<slug>/` URLs only: htmlproofer can't check them, so confirm each slug exists in electronics' `mkdocs.yaml` nav (and isn't in its exclude glob) before linking. It's still one admonition, never a second box.
- **One-way for now.** Electronics does not link to radio until radio has published articles (Brad, 2026-10-01). Don't add radio links to electronics pages.
- Topic numbers come from the question bank (`anki/basic_questions.json`), not memory: check a topic's actual questions before tagging an article with it.

## Content Architecture: Topics

Same model as exploring_electronics and exploring_cnc: **no tiers, no paywall**, organised purely by topic, with a per-article difficulty tag.

**The seven stable topics**, and the Basic syllabus sections (RIC-3 §5.1) each one carries:

| # | Topic | Scope | Exam sections |
|---|---|---|---|
| 1 | **Getting Licensed** | The certificate, qualifications, the exam, call signs, what each qualification permits, the Radiocommunication Act and RBR-4 | B-001 Regulations and Policies |
| 2 | **Radio Fundamentals** | Frequency, wavelength, AC/RF, reactance and resonance, decibels, modulation (AM, FM, SSB, CW), receivers and transmitters as block diagrams | B-004 Circuit Components, B-005 Basic Electronics and Theory (radio-specific parts only; see Site Boundaries) |
| 3 | **Antennas & Feedlines** | Dipoles, verticals, Yagis, coax, standing wave ratio (SWR), baluns, matching | B-006 Feedlines and Antenna Systems |
| 4 | **Propagation** | Ground wave, line of sight, the ionosphere, skip, solar cycle, VHF/UHF effects | B-007 Radio Wave Propagation |
| 5 | **On the Air** | Repeaters, simplex, phonetics, Q-codes, contacts, nets, logging, emergency communications | B-002 Operating and Procedures |
| 6 | **Station & Safety** | Station assembly, power supplies, grounding and bonding, lightning, RF exposure, towers, interference and filtering | B-003 Station Assembly, Practice and Safety; B-008 Interference and Suppression |
| 7 | **Digital Modes & SDR** | Beyond the exam: APRS, FT8, Winlink, software-defined radio (SDR) receivers | (none, post-licence) |

**Practical Tools** is a cross-cutting reference shelf (CHIRP radio programming, RTL-SDR receivers, antenna analysers, SWR meters, logging software, the ISED exam generator), **not** a topic. It gets its own top-level nav section.

**Navigation rules:**

- Nav is **topic-first**: each topic is its own top-level nav group. There's no tier wrapper.
- Add a topic to the nav **only once it has a published article**. Never show empty groups.
- **Every topic with two or more articles gets a landing page**, as on exploring_electronics (Brad, 2026-10-02): a flat `docs/<topic>.md` first in its nav group as `Overview`, articles in reading order grouped into stages with one-line hooks. The homepage links topic cards to landing pages rather than listing every article.
- **Directory stays flat** (`docs/*.md`, plus `tools/`) until a topic has about three or more articles.

**Suggested build order** (follows Brad's own exam study, not a publishing schedule): Getting Licensed first (it frames everything), then Radio Fundamentals → Antennas & Feedlines → Propagation → On the Air → Station & Safety. Digital Modes & SDR comes after Brad has a call sign. This is an ordering, not a timeline. No cadence commitments.

**Difficulty tags + exam tag:** every article carries a `!!! abstract "Beginner"` / `"Intermediate"` / `"Advanced"` admonition right under the H1. When the article covers exam material, that same admonition names the section, e.g. *"Covers Basic exam section B-006 (Feedlines and Antenna Systems)."* It's one admonition, never two stacked boxes.

- **Beginner**: no prior radio or electronics knowledge. Most exam-path articles are Beginner.
- **Intermediate**: assumes the Basic Qualification level of knowledge (or equivalent). Requires a **"Where You Might Have Seen This"** section that bridges to everyday technology (car radio, Wi-Fi router, phone signal bars, a garage door opener) or the reader's own on-air experience.
- **Advanced**: Advanced Qualification material (transmitter design, amplifiers, repeater systems) or deep technical treatment. Colleague-to-colleague.

## Important Preferences

**Git Operations**: The user handles all git operations (commits, pushes, etc.) themselves. Do not commit or push changes.

**MkDocs Operations:** `poetry run mkdocs build --strict` is allowed for verification. `mkdocs serve` is allowed only as a short-lived test on a non-default port (not 3000, and not 8123, which is Home Assistant), never left running. The user handles real previews and all deploys.

**No devcontainer** on this site, matching exploring_cnc (Brad declined one for that hobby site).

---

## SEO Strategy and Publication Process

Same draft/publish workflow as the sibling sites.

### Required Metadata for Every Article

```yaml
---
date: "YYYY-MM-DD HH:MM"
title: "Title With a Colon: Must Be Quoted"
description: Compelling description for search results (150-160 chars ideal)
---
```

- `date:` is required on every article (RSS feed and sitemap `lastmod`).
- Quote any title containing a colon.
- Titles ≤60 characters, descriptions ≤160.
- Search terms people actually use belong in titles and descriptions: "ham radio", "amateur radio licence Canada", "Basic Qualification exam".

### The Exclude Plugin

The exclude plugin is **commented out in `mkdocs.yaml`** because no draft articles exist yet. When the first draft lands:

1. Uncomment the `exclude:` block and list each draft file path.
2. Record the list below.

**Current exclude configuration:** none (no drafts).

**Published pages:** `getting_licensed.md` (landing page, transit map via `illustrations/landing_pages.py` + `transit.py` copied from electronics), `antennas_and_neighbours.md` (Getting Licensed, 2026-10-08; CPC-2-0-03 Issue 6 July 2022 [live page confirmed current; DGSO-001-26 May 2026 proposes changes — portal, 3× radius — NOT yet in force, revisit], Safety Code 6 2015 Table 5, EMCAB-2 Issue 1 June 1994; B-001-023/024/025; flags SC6 not stating the 'body absorbs most' reason) — B-001 now fully covered across 6 articles, `who_enforces_the_rules.md` (Getting Licensed, 2026-10-08; Act ss. 2, 4(1), 5(1)(d)(j)(l), 5(2), 6(1), 8, 8.1, 9(1), 10(1)-(2), 15.1 [AMP: individual ≤$25,000, subsequent ≤$50,000], 15.11(2); Regs ss. 2, 38, 45; B-001-001/003), `across_borders.md` (Getting Licensed, 2026-10-08; ITU RR Art. 25 via ANCOM extract `.cache/src/ancom25.pdf` [ITU PDF blocks curl], Art. 5 regions via 47 CFR 2.104, RBR-4 ss. 3.2/6/7/9, RIC-3 s.8, Regs s.42, 47 CFR 97.107/97.115/97.119(g), UNCLOS art. 3; B-001-014/020/021), `what_you_may_say.md` (Getting Licensed, 2026-10-08; Regs ss. 39, 40, 44, 46–49, 54, Act definition + ss. 5(1)(l), 9, 9.1, 10, RBR-4 s.8, ITU RR 4.9; B-001-005 to 012; flags that s.39 says "licence" and that the bank's "amateur traffic may be divulged" isn't found in Act/Regs), `what_you_may_transmit.md` (Getting Licensed, 2026-10-08; RBR-4 sections 3–11 + Schedule I notes, B-001-013/015/016/017/018/019), `getting_your_certificate.md` (Getting Licensed, first article, in nav for review 2026-10-08; RIC-3 Issue 5, RIC-1 Issue 8, RIC-9, RBR-4, Regulations, ISED fees/how-to pages, RAC requirements), `index.md`, `tools/ised_basic_anki_deck.md` (2026-09-30), `amateurs_code.md` (On the Air, in nav for Brad's review 2026-10-02; first article). `start_here.md` (top of nav, in nav for review 2026-10-01; the electricity prerequisites path).

### The Anki Deck (rebuild when ISED publishes a new bank)

1. Download the delimited ZIP (`https://apc-cap.ic.gc.ca/datafiles/amat_basic_quest.zip`) and the PDF bank from ISED's downloads page; put the TXT in `anki/source/`.
2. `python3 anki/parse_bank.py <bank.pdf> anki/basic_questions.json` (needs poppler's `pdftotext`; must report 984-ish questions, 0 problems).
3. `poetry install --with anki && poetry run python anki/build_deck.py` — the delimited TXT is authoritative; PDF order is used only where the two agree.
4. Update `BANK_DATE`, the disputed-question list on the deck page, and the counts; re-run `python3 illustrations/anki_deck.py`.
5. The 2025-07-15 files disagree on 11 questions (listed on the deck page): the PDF misfiles the OCF-antenna question under B-003-019-008, omits "chassis ground", and adds "stereo amplifiers". Worth reporting to ISED's Amateur Radio Service Centre if Brad wants.


### How to Publish an Article

1. Complete the [Quality Standards Checklist](#quality-standards-checklist).
2. Remove the article's line from the exclude glob (the entire line, not commented).
3. Uncomment or add it in `nav:`, and uncomment its topic group if this is the topic's first article.
4. Update `docs/index.md`'s topic list.
5. `poetry run mkdocs build --strict`, then `grep -o '<loc>[^<]*</loc>' site/sitemap.xml | grep <slug>`.
6. Update the exclude/published lists above.

### SEO Checklist

- [ ] Frontmatter present (date, title, description), title unique
- [ ] All images have alt text
- [ ] Internal links point only to published articles; no "coming soon" links
- [ ] External links validated with WebFetch (ISED URLs move; re-check every one)
- [ ] One H1, hierarchical headings
- [ ] No duplicated content, on this site or exploring_electronics

---

## CRITICAL: No Repetition, Respect the Reader's Time

1. **Cross-link instead of repeating**, including across to exploring_electronics.
2. **Only repeat for a significantly different perspective**, and say what the new angle is.
3. **Progressive depth**: build on earlier articles without re-explaining them.
4. **Audit before publishing**: use the Explore agent to search this site *and* exploring_electronics for the concepts being explained.

---

## Project Structure

- `docs/`: Markdown content, flat (grouped by topic in nav)
  - `tools/`: Practical Tools reference shelf
  - `images/`: diagrams and photos; `images/schematics/` holds generated schematic SVGs
  - `stylesheets/extra.css`: shared brand layer (byte-identical across sites) + site-specific section
- `schematics/`: schemdraw source (see `schematics/README.md`)
- `branding/`: `make_logo.py` regenerates the mascot from the networking mascot (Oswald Bold, OFL, bundled). It writes `branding/exploring_radio.png`; copy it to `docs/images/` and the repo root. It takes ~2 min (per-pixel loop).
- `overrides/`: footer (Buy Me a Coffee), analytics hostname gate, sitemap `lastmod` from `date:`
- `mkdocs.yaml`, `pyproject.toml`

## Common Commands

```bash
poetry install
poetry run mkdocs build --strict
poetry run mkdocs serve -a 127.0.0.1:8471      # short-lived test only
poetry install --with schematics && poetry run python schematics/build.py
```

---

## Content Guidelines

### Tone and Style

- **Beginner**: mentor voice, warm but adult-to-adult. Physical analogies (water, ripples, springs, swings), no software analogies. Explain consequences before any risky step.
- **Intermediate**: peer-to-peer. Assumes Basic-level knowledge. Everyday-technology bridges.
- **Advanced**: colleague-to-colleague, standards and engineering depth.

**Hooks state the practice as a fact rather than guessing at the reader's history.** Write "Every repeater in Canada is listening on one frequency and talking on another," not "You've probably heard a repeater…". Don't write reader biography.

**Prose register:** follow the cross-site standards in memory. Em-dashes stay under 1 per 100 words, spell out every acronym on first use (radio is acronym-dense: SWR, CTCSS, PEP, SSB, VHF, APRS, all of them), use no generic `note` admonitions, never stack admonitions, and give every heading its own lead sentence.

**Required sections (every article):**

1. Opening hook with real-world context
2. **"Where You Might Have Seen This"** (Intermediate/Advanced only)
3. Core content with real frequencies, real numbers, worked calculations
4. Safety warnings where relevant
5. Practice exercises with nested solutions (`??? question` containing `??? tip "Solution"`)
6. Quick Recap
7. What's Next (above Further Reading)
8. Further Reading, by category: **Regulations** (ISED), **Band Plans & Clubs** (RAC), **Deep Dives**, **Related Articles** (including exploring_electronics)

### Radio-Specific Writing Guidelines

#### Transmitting Requires a Qualification

Anything that tells the reader to **transmit** must say, where the instruction first appears, that transmitting on amateur frequencies requires an Amateur Radio Operator Certificate with the right qualification for that band. Listening needs no certificate. Receiver projects (SDR, scanner listening, tuning in a repeater) are the right hands-on work for pre-licence readers, and articles should say so. Never suggest transmitting "just to test" without a qualification, and never suggest a handheld "works on" non-amateur frequencies (GMRS, FRS, marine, business bands) as if that were allowed. Out-of-band transmission is a real, common violation.

#### Safety: NEVER Skip These

Use `!!! danger` for life-safety hazards, with the *why* at Beginner:

- **Antennas and power lines**: the leading cause of death in the hobby. Any antenna-raising article states the fall-distance rule (the antenna must not be able to reach a power line if it falls, in any direction).
- **RF exposure**: cite Health Canada Safety Code 6 / ISED RSS-102. Higher power, higher frequency, and closeness to the antenna all raise exposure. Handhelds are held close to the eyes and head.
- **Towers and climbing**: fall protection, and never climb alone.
- **Lightning**: disconnect and ground feedlines. Explain what grounding does and doesn't protect.
- **High voltage** in linear amplifiers, tube equipment, and switching power supplies. Capacitors hold a charge after power-off.
- **Lithium batteries** in handhelds and portable packs.

Use `!!! warning` for equipment damage: transmitting into no antenna or a badly mismatched load, reverse polarity on a 13.8 V supply, overdriving an amplifier.

#### Numbers, Units, and Calculations

- SI units with symbols: kHz, MHz, GHz, W, mW, dB, dBm, Ω, m, cm. Write "146.520 MHz", not "146.52" or "146.52 megs".
- **Bands are named by wavelength and frequency together** the first time: "the 2 m band (144–148 MHz)".
- **Show every calculation as a worked example** (wavelength = 300 / f(MHz) in metres, dipole length, dB arithmetic), and **verify every computed number** with a quick Python check before publishing. State the approximation, such as the 0.95 velocity/end-effect factor in "half-wave dipole ≈ 143 / f(MHz) m", and where it comes from.
- Math follows the cross-site rule: no inline `$...$` in prose, and LaTeX only in display blocks for worked math.

#### Exam Material

- **The one exception is the Anki deck** (`docs/tools/ised_basic_anki_deck.md`, built by `anki/build_deck.py`), which reproduces the whole bank verbatim under ISED's non-commercial terms with the required attribution. Articles still never reproduce it.
- **Teach the concept, don't reproduce the bank.** Refer to question IDs (e.g., `B-006-003-001`) when useful, and paraphrase rather than quote whole questions. Practice exercises are original, exam-*style* questions.
- Every exam-path article ends its recap with **"On the exam"**: the specific facts the Basic exam tests from this section, verified against the current question bank's answers.
- When the question bank's expected answer is a simplification, teach the fuller truth *and* say what the exam wants. Don't leave a reader to fail a question because the site was more precise than the bank.

#### Call Signs and Phonetics

- Brad's own call sign becomes the worked example once he has one (record it here when issued). Until then, describe the *format* (prefix + digit + suffix, e.g. "VA1 plus a two- or three-letter suffix for Nova Scotia"), verified against RIC-9, and never present a made-up call sign as a real station. If an example is unavoidable, mark it as a format example.
- Use ITU phonetics (Alfa, Bravo, Charlie…, with the ITU spellings "Alfa" and "Juliett").

#### Diagrams

**No mermaid (Brad, 2026-09-30).** Figures are hand-built 3D-lit SVGs generated by Python scripts in `illustrations/<page>.py`, in the house style from exploring_electronics' `illustrations/conductors_and_insulators.py` (lit spheres, glassy shells, panels, gloss, perspective). Use as many figures as a page can carry. The mermaid notes below are superseded.

- **Mermaid**: block and logical diagrams (transmitter/receiver chains, repeater offset flow, station layout, propagation paths as structure). Use structural shapes (branches, hubs, decision trees) and never linear A→B→C restatements. Avoid nested subgraphs.
- **schemdraw schematics**: real circuits (tuned circuits, filters, a dipole feed). Always build through `dark_drawing()` in `schematics/style.py`. schemdraw has antenna and ground elements.
- **SVG illustrations**: for things neither tool draws well (waveforms, standing waves, ionospheric skip geometry), hand-authored SVG in the slate/amber palette.
- **Photos**: real gear and real builds (Brad's, once he has them). In Beginner articles, put the photo first and then the schematic.

**Mermaid colour scheme (shared with the other sites):**

- Standard Node (Slate 800): `fill:#2d3748,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- Highlighted Node (Amber 600): `fill:#d97706,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- Darker Node (Slate 900): `fill:#1a202c,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- Warning/Danger (Red 600): `fill:#c53030,stroke:#cbd5e0,stroke-width:2px,color:#fff`
- Success/Output (Green 700): `fill:#2f855a,stroke:#cbd5e0,stroke-width:2px,color:#fff`

#### Software and Tools

Command line first, with minimal GUIs, following the cross-site rule. For radio that means CHIRP's CLI where it's practical, `rtl_sdr`/`rtl_fm`, and Linux-native tools, with GUI tools named honestly when no CLI equivalent exists (WSJT-X for FT8, for example). Cross-link Exploring Linux for anything shell-related.

### Article Layouts by Type

**Concept articles** (What Is a Radio Wave?, Decibels, How the Ionosphere Works): hook → structural mermaid diagram → core explanation with worked numbers → card grid of variants/cases → safety → exercises → recap with "On the exam" → What's Next → Further Reading.

**Regulatory articles** (Getting Your Certificate, What Basic Lets You Do): hook → the rule, quoted and cited from the ISED source with its issue → *why* the rule exists → a table of privileges/limits → common misconceptions (including US-rule confusion) → exercises → recap with "On the exam" → What's Next → Further Reading (Regulations first).

**Hands-on articles** (Build a 2 m Dipole, Listen to a Repeater with an SDR): what you'll build → licence note (listen vs transmit) → parts list with exact values → worked calculation → step-by-step → verification (analyser/SWR reading, what "good" looks like) → troubleshooting (collapsible) → exercises → What's Next → Further Reading.

### Cross-Linking Strategy

- **exploring_electronics** is the primary sibling. Link for every DC/component concept (see Site Boundaries).
- **Exploring Linux** for SDR tooling and shell use.
- **Exploring Networking** for digital-mode concepts that are really networking (packet, APRS as a network, Winlink as store-and-forward).
- **Exploring Computer Science** for sampling, the Fourier transform, and encoding when SDR and digital modes need them.

---

## Quality Standards Checklist

**✅ Accuracy (non-negotiable on this site):**

- [ ] Every regulatory claim cited to a current ISED document, fetched at write time, with its issue/date
- [ ] Every frequency labelled as law (RBR-4) or convention (RAC band plan)
- [ ] Every computed number verified with a Python check
- [ ] "On the exam" facts match the current question bank's answer key
- [ ] No US rules presented as Canadian
- [ ] Transmit instructions carry the qualification note

**✅ Content Quality:**

- [ ] **No-repetition audit** across this site *and* exploring_electronics
- [ ] Opening hook states a practice/fact, not reader biography
- [ ] Safety addressed at the right tag level (never skipped)
- [ ] Practice exercises with nested solutions
- [ ] Quick Recap (+ "On the exam" for exam-path articles), What's Next, Further Reading

**✅ Tone and Formatting:**

- [ ] Correct voice for the difficulty tag; difficulty + exam section in one admonition under the H1
- [ ] Every acronym spelled out on first use
- [ ] Canadian spelling; "certificate"/"qualification" in regulatory contexts
- [ ] SI units with symbols; bands named with wavelength + frequency on first mention
- [ ] All code blocks have `title=` and `linenums="1"`
- [ ] Blank lines before all lists
- [ ] At least one structural mermaid diagram in every substantial article, in the slate/amber scheme
- [ ] Emoji limited (1–3, strategic)

**✅ Integration:**

- [ ] Links only to published articles; external links validated with WebFetch
- [ ] Referenced from the previous article's What's Next
- [ ] `docs/index.md` topic list updated

---

## Final Notes

The goal is an operator who **passes the Basic exam with Honours because they understand it**, then keeps going: building antennas, reading the bands, and helping when the power goes out. Err on the side of:

- Primary sources over summaries, and ISED over forums
- More safety context, especially antennas near power lines and RF exposure
- Showing the calculation rather than stating the answer
- Linking to exploring_electronics rather than re-explaining
