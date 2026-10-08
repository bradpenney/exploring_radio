#!/usr/bin/env python3
"""Figures for docs/getting_your_certificate.md.

Sources (all fetched 2026-10-08):
- RIC-3 Issue 5 (March 2022): 100-question Basic exam, one question from each
  of 100 topic areas, pass 70 %, 80 % for Honours; privileges in 4.5.
- RIC-1 Issue 8 (May 2025): examiner submits results within ten working days;
  ISED issues the certificate when results arrive.
- ISED "How to become an amateur radio operator": authorization key from the
  examiner, then create an account and choose a call sign.
- RBR-4 Issue 3, section 10 and Schedule V (prefixes).
- Topic areas per section counted from anki/basic_questions.json (15 July 2025
  bank): B-001 25, B-002 9, B-003 21, B-004 6, B-005 13, B-006 13, B-007 8,
  B-008 5.

Usage:
    python3 illustrations/getting_your_certificate.py
"""

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "getting_your_certificate"
BLUE = "#4299e1"
BANK = HERE.parent / "anki" / "basic_questions.json"


def _topics_per_section():
    qs = json.loads(BANK.read_text())
    seen = {}
    for q in qs:
        seen.setdefault(q["section"], set()).add(q["topic"])
    return {k: len(v) for k, v in sorted(seen.items())}


# 1. The route to a certificate ----------------------------------------------------------------------
def route():
    w, h = 900, 400
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "From studying to transmitting: the route to a certificate", 17, AMBER_LIGHT, weight="bold"))
    steps = [("Study", "the 984-question", "public bank", BLUE),
             ("Find an", "accredited examiner", "(in person or video)", BLUE),
             ("Write the", "Basic exam", "100 questions, 70% to pass", AMBER),
             ("Examiner", "submits results", "within 10 working days", "#9f7aea"),
             ("Create your", "ISED account", "with your authorization key", "#9f7aea"),
             ("Certificate", "and call sign", "valid for life", GREEN)]
    y = 220
    parts.append(f'<rect x="80" y="{y - 6}" width="740" height="12" rx="6" fill="#4a5568"/>')
    for k, (a, b, c, col) in enumerate(steps):
        x = 90 + k * 144
        parts.append(f'<circle cx="{x}" cy="{y}" r="22" fill="url(#vball)"/>' if col == AMBER else f'<circle cx="{x}" cy="{y}" r="22" fill="{col}"/>')
        parts.append(f'<circle cx="{x}" cy="{y}" r="22" fill="url(#gloss)" opacity="0.5"/>')
        parts.append(text(x, y + 6, str(k + 1), 15, "#ffffff" if col != AMBER else "#1a1a1a", weight="bold"))
        top = k % 2 == 0
        by = y - 110 if top else y + 40
        parts.append(text(x, by + 18, a, 14, TEXT, weight="bold"))
        parts.append(text(x, by + 36, b, 14, TEXT, weight="bold"))
        parts.append(text(x, by + 56, c, 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Six steps along a line. 1: study the public 984-question bank. 2: find an accredited examiner, in person or by video. 3: write the Basic exam, 100 questions, 70 percent to pass. 4: the examiner submits your results to ISED within ten working days. 5: create your ISED account with the authorization key from your examiner, choosing a call sign. 6: your certificate and call sign, valid for life.")


# 2. What the score buys ------------------------------------------------------------------------------
def score():
    w, h = 900, 400
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "One exam, three outcomes: the score decides the privileges", 17, AMBER_LIGHT, weight="bold"))
    L, R, y = 80, 820, 190
    x = lambda s: L + s / 100 * (R - L)
    bands = [(0, 70, "#4a5568", "not yet: write it again", "a different exam each time"),
             (70, 80, AMBER, "Basic", "all bands above 30 MHz"),
             (80, 100, GREEN, "Basic with Honours", "adds every band below 30 MHz (HF)")]
    for a, b, col, name, sub in bands:
        parts += box3d(x(a), y, x(b) - x(a) - 4, 40, 60, col, shadow=(a == 0))
        cx = (x(a) + x(b)) / 2
        parts.append(text(cx - 4, y - 24, name, 14, "#ffffff" if col != AMBER else "#1a1a1a", weight="bold"))
    for k, (a, b, col, name, sub) in enumerate(bands):
        ly = 262 + k * 20
        parts.append(f'<rect x="250" y="{ly - 11}" width="14" height="14" rx="3" fill="{col}"/>')
        parts.append(text(272, ly + 1, f"{name}: {sub}", 13, TEXT, "start"))
    for s in (0, 70, 80, 100):
        parts.append(text(x(s), y + 28, f"{s}%", 13, MUTED, weight="bold"))
    parts.append(text(w / 2, 336, "Morse code (5 w.p.m.) or Advanced, added to Basic, also opens HF.", 13, TEXT))
    parts.append(text(w / 2, 356, "RIC-3 sections 4.5 and 5.1; RBR-4 Schedule I", 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A 3D score bar from 0 to 100 percent. Below 70 percent the exam isn't passed yet and can be written again, with a different exam each time. From 70 to 79 percent earns the Basic Qualification: every amateur band above 30 megahertz. 80 percent or above earns Basic with Honours, which adds every band below 30 megahertz, the HF bands. Morse code or Advanced, added to Basic, also opens HF.")


# 3. The exam's 100 questions by section -----------------------------------------------------------------
def exam_sections():
    w, h = 900, 420
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Where the 100 questions come from: one per topic area", 17, AMBER_LIGHT, weight="bold"))
    names = {"B-001": "Regulations", "B-002": "Operating", "B-003": "Station, safety",
             "B-004": "Components", "B-005": "Electronics", "B-006": "Antennas",
             "B-007": "Propagation", "B-008": "Interference"}
    counts = _topics_per_section()
    base = 320
    for k, (sec, n) in enumerate(counts.items()):
        x = 70 + k * 100
        hgt = n * 8
        col = AMBER if sec == "B-001" else "#4a5568"
        parts += box3d(x, base, 60, 30, hgt, col)
        parts.append(text(x + 40, base - hgt - 22, str(n), 15, TEXT, weight="bold"))
        parts.append(text(x + 30, base + 24, sec, 12, TEXT, weight="bold"))
        parts.append(text(x + 30, base + 42, names[sec], 11, MUTED))
    parts.append(text(w / 2, 82, f"{sum(counts.values())} topic areas in all; this article is part of B-001, a quarter of the exam", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Eight 3D bars of how many of the exam's 100 questions come from each section, one per topic area: B-001 Regulations 25, B-002 Operating 9, B-003 Station and safety 21, B-004 Components 6, B-005 Electronics 13, B-006 Antennas 13, B-007 Propagation 8, B-008 Interference 5. Regulations, the section this article belongs to, is a quarter of the exam.")


# 4. Anatomy of a call sign ------------------------------------------------------------------------------------
def call_sign():
    w, h = 900, 430
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "How a Canadian call sign is built (format example, not a real station)", 17, AMBER_LIGHT, weight="bold"))
    blocks = [("VA", "country block", "VE, VA, VO or VY", BLUE, 2),
              ("1", "area digit", "where you live", AMBER, 1),
              ("· · ·", "suffix", "2 or 3 letters", GREEN, 3)]
    x = 210
    for chars, name, sub, col, n in blocks:
        bw = 70 + n * 30
        parts += box3d(x, 220, bw, 40, 100, col)
        parts.append(text(x + bw / 2, 184, chars, 36, "#ffffff" if col != AMBER else "#1a1a1a", weight="bold"))
        parts.append(text(x + bw / 2 + 10, 252, name, 14, TEXT, weight="bold"))
        parts.append(text(x + bw / 2 + 10, 270, sub, 12, MUTED, italic=True))
        x += bw + 30
    rows = [("VE1, VA1", "Nova Scotia"), ("VE2, VA2", "Quebec"), ("VE3, VA3", "Ontario"), ("VE4, VA4", "Manitoba"),
            ("VE5, VA5", "Saskatchewan"), ("VE6, VA6", "Alberta"), ("VE7, VA7", "British Columbia"),
            ("VE8", "Northwest Territories"), ("VE9", "New Brunswick"), ("VO1", "Newfoundland"), ("VO2", "Labrador"),
            ("VY1", "Yukon"), ("VY2", "Prince Edward Island"), ("VY0", "Nunavut")]
    for k, (pre, place) in enumerate(rows):
        cx = 90 + (k % 7) * 118
        cy = 318 + (k // 7) * 40
        parts.append(text(cx, cy, pre, 12, AMBER_LIGHT, weight="bold"))
        parts.append(text(cx, cy + 15, place, 10, MUTED))
    parts.append(text(w / 2, 404, "prefixes from RBR-4 Schedule V; VE0 is reserved for stations aboard vessels in international waters", 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A call sign drawn as three 3D blocks: a two-letter country block such as VA, then a digit for the area where the operator lives, such as 1 for Nova Scotia, then a suffix of two or three letters, shown blank because this is a format example and not a real station. Beneath, the prefixes for every province and territory: VE1 and VA1 Nova Scotia, VE2 and VA2 Quebec, VE3 and VA3 Ontario, VE4 and VA4 Manitoba, VE5 and VA5 Saskatchewan, VE6 and VA6 Alberta, VE7 and VA7 British Columbia, VE8 Northwest Territories, VE9 New Brunswick, VO1 Newfoundland, VO2 Labrador, VY1 Yukon, VY2 Prince Edward Island, VY0 Nunavut.")


FIGURES = {"route.svg": route, "score.svg": score, "exam_sections.svg": exam_sections, "call_sign.svg": call_sign}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
