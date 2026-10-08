#!/usr/bin/env python3
"""Figures for docs/across_borders.md.

Sources (fetched 2026-10-08):
- ITU Radio Regulations Article 25 (text as revised at WRC-03): 25.1 objection,
  25.2 purposes of the amateur service and personal remarks, 25.3 third parties,
  25.5 Morse decided by administrations, 25.9B visiting operators.
- ITU Radio Regulations Article 5 regions, as reproduced in 47 CFR 2.104(b).
- Radiocommunication Regulations s. 42(i), (j).
- RBR-4 Issue 3: s. 3.2 foreign equivalencies, s. 6 third parties, s. 7
  operation outside Canada, s. 9 identification by United States licensees.
- RIC-3 Issue 5 section 8: Canada-US convention (Treaty Series 1952 No. 7),
  CEPT T/R 61-01 (Basic + Advanced), IARP Class 1/Class 2, third parties.
- 47 CFR 97.107 and 97.119(g): Canadian indicator after the call sign.

Usage:
    python3 illustrations/across_borders.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "across_borders"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"


def person(fx, fy, col, lab, sub=None):
    parts = [f'<circle cx="{fx}" cy="{fy}" r="13" fill="{col}"/>',
             f'<rect x="{fx - 13}" y="{fy + 17}" width="26" height="32" rx="10" fill="{col}"/>',
             text(fx, fy + 68, lab, 12, TEXT, weight="bold")]
    if sub:
        parts.append(text(fx, fy + 86, sub, 11, MUTED, italic=True))
    return parts


# 1. Whose rules apply ---------------------------------------------------------------------------------
def layers():
    w, h = 900, 430
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Three layers of rules over every amateur station", 17, AMBER_LIGHT, weight="bold"))
    rows = [(350, 300, "International: ITU Radio Regulations (Article 25)", PURPLE),
            (270, 230, "Canada: Radiocommunication Act, Regulations, RBR-4", BLUE),
            (190, 150, "Your station", AMBER)]
    for base, half, title, col in rows:
        parts += box3d(w / 2 - half, base, half * 2, 60, 34, shade(col, -0.25), shadow=(base == 350))
        parts.append(text(w / 2, base - 8, title, 13, "#ffffff", weight="bold"))
    parts.append(text(w / 2, 404, "Lower layers bind the ones above them: Canadian rules sit inside the treaty.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Three stacked layers. At the bottom, the International Telecommunication Union Radio Regulations, a treaty whose Article 25 covers the amateur service. In the middle, Canadian law: the Radiocommunication Act, the Radiocommunication Regulations and RBR-4, administered by Innovation, Science and Economic Development Canada. On top, your station. Canadian rules sit inside the treaty.")


# 2. ITU regions ---------------------------------------------------------------------------------------
def regions():
    w, h = 900, 420
    parts = [common_defs()]
    cards = [("Region 1", TEAL, ["Europe and Africa", "the Middle East", "the former Soviet Union", "and Mongolia"]),
             ("Region 2", AMBER, ["North and South America", "Greenland and", "the eastern Pacific", "Canada is here"]),
             ("Region 3", PURPLE, ["the rest of Asia", "Australia and", "Southeast Asia", "most of Oceania"])]
    for k, (title, col, lines) in enumerate(cards):
        x0 = 15 + k * 295
        cx = x0 + 140
        parts.append(panel(x0, 15, 280, h - 30))
        parts += box3d(cx - 70, 170, 140, 50, 55 + (25 if k == 1 else 0), col)
        parts.append(text(cx, 50, title, 17, AMBER_LIGHT if k == 1 else TEXT, weight="bold"))
        for j, line in enumerate(lines):
            last = j == 3 and k == 1
            parts.append(text(cx, 225 + j * 26, line, 14 if last else 13,
                              AMBER_LIGHT if last else TEXT, weight="bold" if last else "normal"))
    parts.append(text(w / 2, 385, "Boundaries are lines on the globe (ITU Radio Regulations Article 5), not borders; each region has its own allocations.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "The three ITU regions. Region 1: Europe and Africa, the Middle East, the former Soviet Union and Mongolia. Region 2: North and South America, Greenland and the eastern Pacific; Canada is in Region 2. Region 3: the rest of Asia, Australia, Southeast Asia and most of Oceania. The boundaries are lines on the globe defined in Article 5 of the ITU Radio Regulations, and each region has its own frequency allocations.")


# 3. Who is a third party ------------------------------------------------------------------------------
def third_party():
    w, h = 900, 400
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "A third party is anyone talking over the link without a certificate", 16, AMBER_LIGHT, weight="bold"))
    parts += box3d(290, 300, 110, 40, 60, "#4a5568")
    parts.append(text(345, 273, "your station", 12, "#ffffff", weight="bold"))
    parts += box3d(510, 300, 110, 40, 60, "#4a5568")
    parts.append(text(565, 273, "their station", 12, "#ffffff", weight="bold"))
    parts.append(f'<path d="M 410 245 Q 455 200 500 245" fill="none" stroke="{AMBER}" stroke-width="3" stroke-dasharray="7 6"/>')
    parts.append(text(455, 200, "amateur radio link", 12, AMBER_LIGHT, italic=True))
    parts += person(110, 120, BLUE, "you", "certified: operator")
    parts += person(200, 120, RED, "your friend", "no certificate")
    parts += person(700, 120, BLUE, "foreign amateur", "certified: operator")
    parts += person(800, 120, RED, "their friend", "no certificate")
    parts += pill(200, 232, "third party", RED, size=12, h=26, wpx=100)
    parts += pill(800, 232, "third party", RED, size=12, h=26, wpx=100)
    parts.append(text(w / 2, 345, "Canada doesn't prohibit international third-party traffic (RBR-4 s. 6);", 12, TEXT))
    parts.append(text(w / 2, 365, "the other country decides for its end. Personal, non-commercial content only.", 12, TEXT))
    return svg(w, h, "\n".join(parts), "Two stations linked by amateur radio. At each end a certified operator stands beside a friend with no certificate. Both friends are third parties. Canada does not prohibit international third-party traffic, under RBR-4 section 6; the other country decides for its end, and the content must be personal and non-commercial.")


# 4. Visitors to Canada --------------------------------------------------------------------------------
def visitors():
    w, h = 900, 420
    parts = [common_defs()]
    cards = [("From the United States", BLUE, "no permit needed",
              ["FCC call sign, plus \"portable\"", "or \"mobile\" and the Canadian", "prefix: \"... portable VE1\"",
               "(RBR-4 s. 9)", "must be a US citizen"]),
             ("With a CEPT licence", PURPLE, "privileges: Basic + Advanced",
              ["CEPT T/R 61-01, a European", "licensing system that Canada", "recognizes", "(RIC-3 s. 8.2.1)",
               "within their own licence too"]),
             ("Other countries", TEAL, "reciprocal arrangement",
              ["a citizen of the issuing country,", "which must give Canadians", "similar privileges",
               "(Regulations s. 42(i))", "no more than their own licence"])]
    for k, (title, col, pl, lines) in enumerate(cards):
        x0 = 15 + k * 295
        cx = x0 + 140
        parts.append(panel(x0, 15, 280, h - 30))
        parts.append(text(cx, 50, title, 15, AMBER_LIGHT, weight="bold"))
        parts += person(cx, 78, col, "visitor")
        parts += pill(cx, 200, pl, col, size=12, h=28, wpx=230)
        for j, line in enumerate(lines):
            parts.append(text(cx, 250 + j * 24, line, 12, MUTED if line.startswith("(") else TEXT,
                              italic=line.startswith("(")))
    return svg(w, h, "\n".join(parts), "Three kinds of visitor operating in Canada. From the United States: no permit is needed; they use their FCC call sign plus \"portable\" or \"mobile\" and the Canadian prefix for where they are, under RBR-4 section 9, and must be United States citizens. With a CEPT licence, the European licensing system Canada recognizes: privileges equal to a Canadian with Basic and Advanced, under RIC-3 section 8.2.1, but no more than their own licence. From other countries: they must be citizens of the issuing country, which must give Canadians similar privileges, under section 42(i) of the Regulations.")


# 5. Operating abroad ----------------------------------------------------------------------------------
def abroad():
    w, h = 900, 470
    parts = [common_defs()]
    cards = [("United States", BLUE, "Basic", ["no permit; carry your", "certificate", "US band edges and", "mode rules apply",
                                                "ID: call sign, then", "\"portable\" + US area"]),
             ("CEPT countries", PURPLE, "Basic + Advanced", ["permit from Radio", "Amateurs of Canada", "host country's rules",
                                                             "apply", "ID: host prefix,", "then \"stroke\" + call"]),
             ("IARP (Americas)", TEAL, "Basic", ["permit from Radio", "Amateurs of Canada", "Class 2 (Basic):",
                                                 "above 30 MHz only", "Class 1 needs", "Morse (12 w.p.m.)"]),
             ("Anywhere else", MUTED, "ask first", ["contact the country's", "administration well", "in advance",
                                                    "", "its rules, its", "conditions"])]
    for k, (title, col, need, lines) in enumerate(cards):
        x0 = 15 + k * 220
        cx = x0 + 102
        parts.append(panel(x0, 15, 205, h - 30))
        parts.append(text(cx, 50, title, 14, AMBER_LIGHT, weight="bold"))
        parts += box3d(cx - 45, 145, 90, 35, 50, col)
        parts.append(text(cx, 182, "minimum", 11, MUTED, italic=True))
        parts += pill(cx, 207, need, col if col != MUTED else "#4a5568", size=12, h=28, wpx=170)
        for j, line in enumerate(lines):
            parts.append(text(cx, 256 + j * 24, line, 12, TEXT))
    parts.append(text(w / 2, 408, "Outside Canada you follow the host country's rules (RBR-4 s. 7; RIC-3 s. 8).", 11, MUTED, italic=True))
    parts.append(text(w / 2, 426, "A Canadian-issued CEPT permit or IARP has no legal status in Canada.", 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Four destinations for a Canadian operating abroad. United States: Basic is enough, no permit, carry your certificate, United States band edges and mode rules apply, and you identify with your call sign followed by portable and the United States call area. CEPT countries: Basic plus Advanced, a permit from Radio Amateurs of Canada, the host country's rules, and identification with the host prefix, then stroke and your call sign. IARP countries in the Americas: Basic, a permit from Radio Amateurs of Canada; Class 2 for Basic covers bands above 30 megahertz only, and Class 1 needs Morse code at 12 words per minute. Anywhere else: contact that country's administration well in advance. Outside Canada you follow the host country's rules.")


FIGURES = {"layers.svg": layers, "regions.svg": regions, "third_party.svg": third_party,
           "visitors.svg": visitors, "abroad.svg": abroad}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
