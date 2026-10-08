---
date: "2026-10-01 14:00"
title: "Start Here: The Electricity Behind Amateur Radio"
description: "Radio is electricity that changes direction millions of times a second. The electricity you need first, in order, mapped to the Canadian Basic Qualification syllabus."
---

# Start Here: The Electricity Behind Radio

!!! abstract "Beginner"
    The first page to read on this site. No prior knowledge required.

A radio signal is alternating current: the same current that flows in a flashlight, except that it reverses direction millions of times a second and leaves the antenna as a wave. Every idea in amateur radio, from antennas to propagation to the power limits in the regulations, is built on a handful of facts about electricity.

Those foundations live on this site's sister site, **[Exploring Electronics](https://electronics.bradpenney.io/)**, so they're written once and shared rather than repeated here. Read them first, in the order below, and everything on this site will make sense the first time.

<figure class="transit-map">
--8<-- "docs/images/start_here/transit_map.svg"
<figcaption>Three lines on Exploring Electronics meet at Radio Fundamentals, where this site's line begins. Every filled stop is a link, and the numbers match the table below.</figcaption>
</figure>

---

## The Foundations, in Order

Each article stands on its own, but they're written to be read in this order. The last column gives the Basic Qualification exam topics each one covers, by their question-bank number (the B-005-002 questions, for example, are about conductors, insulators, and current).

| # | Read | Why it matters for radio | Exam topics |
|---|---|---|---|
| 1 | [Conductors, Insulators, and Semiconductors](https://electronics.bradpenney.io/conductors_and_insulators/) | why antennas are copper and their insulators are ceramic | B-005-002 |
| 2 | [Metric Prefixes and Units](https://electronics.bradpenney.io/metric_prefixes/) | every frequency is in kilo-, mega-, or gigahertz; every capacitor in micro- to picofarads | B-005-001 |
| 3 | [Voltage](https://electronics.bradpenney.io/voltage/) | the push behind every signal, and what electromotive force (EMF) means | B-005-002, B-005-013 |
| 4 | [Current](https://electronics.bradpenney.io/current/) | what flows in an antenna, and why current is what hurts | B-005-002, B-005-013 |
| 5 | [Resistance and Conductance](https://electronics.bradpenney.io/resistance/) | feedline loss starts here, and the exam asks about conductance | B-005-002 |
| 6 | [Ohm's Law and Power](https://electronics.bradpenney.io/ohms_law/) | transmitter power, dummy loads, and the power-law questions | B-005-003, B-005-004, B-005-006 |
| 7 | [Open Circuits, Short Circuits, and Fuses](https://electronics.bradpenney.io/open_short_fuses/) | why a radio's power cord is fused, and what a blown fuse is telling you | B-005-003, B-003-019 |
| 8 | [Series and Parallel Circuits](https://electronics.bradpenney.io/series_and_parallel/) | combining resistors, and how a supply shares out its voltage | B-005-005 |
| 9 | [Cells and Batteries](https://electronics.bradpenney.io/batteries/) | powering a handheld or a portable station, and battery safety | B-003-016 |
| 10 | [AC vs DC](https://electronics.bradpenney.io/ac_dc/) | frequency, hertz, sine waves, and RMS: the language of every radio signal | B-005-007 |
| 11 | [Magnetism and Electromagnetism](https://electronics.bradpenney.io/magnetism/) | coils, transformers, and the fields that become radio waves | B-005-011 |
| 12 | [Capacitors](https://electronics.bradpenney.io/capacitors/) | stored charge, the RC time constant, and why a capacitor passes AC but blocks DC: half of every tuned circuit | B-005-009 |
| 13 | [Inductors](https://electronics.bradpenney.io/inductors/) | coils, what sets their inductance, chokes, and the other half of every tuned circuit | B-005-009 |
| 14 | [Resistor Types](https://electronics.bradpenney.io/resistor_types/) | colour codes, tolerance, temperature coefficient, and non-inductive loads | B-004-006 |
| 15 | [Diodes and LEDs](https://electronics.bradpenney.io/diodes_and_leds/) | reverse-polarity protection on a radio's power lead, rectification, Zeners, and detection | B-004-002 |
| 16 | [Transistors](https://electronics.bradpenney.io/transistors/) | bipolar and field-effect transistors as switches and amplifiers: gain, distortion, and oscillation | B-004-001, B-004-003, B-004-004 |
| 17 | [Vacuum Tubes](https://electronics.bradpenney.io/vacuum_tubes/) | cathode, grid, and plate; why a triode resembles a FET, and why high-power amplifiers still use tubes | B-004-005 |
| 18 | [Voltage Regulators](https://electronics.bradpenney.io/voltage_regulators/) | the four stages of a linear power supply, why the regulator needs a heat sink, and linear versus switching supplies (and their noise) | B-003-008, B-003-017 |

Two more are useful whenever you're ready: [How to Read a Schematic](https://electronics.bradpenney.io/reading_schematics/), since radio circuits are drawn the same way, and [Resistor Color Codes](https://electronics.bradpenney.io/resistor_color_codes/), for the exam's colour-band questions (also B-004-006).

If you'd rather see the whole picture on one page before diving in, [What Is Electricity?](https://electronics.bradpenney.io/what_is_electricity/) is a short overview of the first six.

---

## What Comes Next, and What's Still Being Written

The rest of the Basic syllabus's electronics sections are radio-specific, so they'll live on this site, in the **Radio Fundamentals** topic: decibels (B-005-008), reactance and impedance (B-005-010), and resonance and tuned circuits (B-005-012). None of them is written yet; this page will link each one as it's published.

Meanwhile, three things on this site are ready now:

- **[Getting Your Amateur Radio Certificate in Canada](getting_your_certificate.md):** what the certificate is, what 70% and 80% unlock, and how to find an examiner and get your call sign.
- **[The Amateur's Code](amateurs_code.md):** the two short codes of conduct every operator is expected to follow.
- **[The ISED Basic Qualification Anki deck](tools/ised_basic_anki_deck.md):** all 984 exam questions as flashcards, organized by syllabus section. Drill each section's cards after reading its articles, not before.

---

## Further Reading

- [RIC-3: Information on the Amateur Radio Service — ISED](https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/licences-and-certificates/radiocom-information-circulars-ric/ric-3-information-amateur-radio-service) — the Basic Qualification syllabus and how the exam is built
- [Exploring Electronics](https://electronics.bradpenney.io/) — the full sister site, including microcontroller projects beyond what radio needs
