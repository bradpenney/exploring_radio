#!/usr/bin/env python3
"""Figures for docs/tools/ised_basic_anki_deck.md.

Counts come from the parsed question bank (anki/basic_questions.json); the
exam-question count per section is the number of distinct topic areas, which
matches RIC-3 Issue 5 section 5.1 (25, 9, 21, 6, 13, 13, 8, 5).

Usage:
    python3 illustrations/anki_deck.py
"""

import collections
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT,  # noqa: E402
                     common_defs, panel, svg, text)

ROOT = HERE.parent
OUT = ROOT / "docs" / "images" / "anki"

SHORT = {
    "B-001": "Regulations",
    "B-002": "Operating",
    "B-003": "Station & Safety",
    "B-004": "Components",
    "B-005": "Electronics",
    "B-006": "Antennas & Feedlines",
    "B-007": "Propagation",
    "B-008": "Interference",
}


def counts():
    qs = json.loads((ROOT / "anki" / "basic_questions.json").read_text(encoding="utf-8"))
    bank = collections.Counter(q["section"] for q in qs)
    topics = collections.defaultdict(set)
    for q in qs:
        topics[q["section"]].add(q["topic"])
    exam = {s: len(t) for s, t in topics.items()}
    assert sum(exam.values()) == 100 and sum(bank.values()) == 984
    return bank, exam


def column(x, base, wid, hgt, dep, top, front, side):
    """Isometric column standing on y=base."""
    dx, dy = dep * 0.7, -dep * 0.45
    return [
        f'<ellipse cx="{x + wid / 2 + dx / 2:.1f}" cy="{base + 4:.1f}" rx="{wid / 2 + dx / 2 + 5:.1f}" ry="6" fill="#000" fill-opacity="0.4"/>',
        f'<polygon points="{x:.1f},{base - hgt:.1f} {x + wid:.1f},{base - hgt:.1f} {x + wid + dx:.1f},{base - hgt + dy:.1f} {x + dx:.1f},{base - hgt + dy:.1f}" fill="{top}"/>',
        f'<rect x="{x:.1f}" y="{base - hgt:.1f}" width="{wid}" height="{hgt:.1f}" fill="{front}"/>',
        f'<rect x="{x:.1f}" y="{base - hgt:.1f}" width="{wid}" height="{hgt:.1f}" fill="url(#gloss)"/>',
        f'<polygon points="{x + wid:.1f},{base:.1f} {x + wid:.1f},{base - hgt:.1f} {x + wid + dx:.1f},{base - hgt + dy:.1f} {x + wid + dx:.1f},{base + dy:.1f}" fill="{side}"/>',
    ]


# 1. Exam composition: 3D columns ------------------------------------------------
def exam_composition():
    bank, exam = counts()
    order = sorted(exam, key=lambda s: -exam[s])
    w, h = 780, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    base, scale, wid, gap = 320, 9.0, 52, 90
    x0 = 58
    for i, s in enumerate(order):
        x = x0 + i * gap
        hi = exam[s] >= 20
        top, front, side = (("#fde68a", "#f59e0b", "#92400e") if hi else ("#cbd5e0", "#718096", "#2d3748"))
        parts += column(x, base, wid, exam[s] * scale, 26, top, front, side)
        parts.append(text(x + wid / 2 + 9, base - exam[s] * scale - 22, str(exam[s]), 20,
                          AMBER_LIGHT if hi else TEXT, weight="bold"))
        parts.append(text(x + wid / 2 + 4, base + 28, s, 13, TEXT, weight="bold"))
        parts.append(text(x + wid / 2 + 4, base + 46, SHORT[s], 11, MUTED))
        parts.append(text(x + wid / 2 + 4, base + 66, f"{bank[s]} in bank", 11, MUTED, italic=True))
    parts.append(text(w / 2, 46, "Questions on a 100-question Basic exam, by section", 16, TEXT, weight="bold"))
    parts.append(text(w / 2, 68, "one question from each of 100 topic areas · regulations and station practice = 46 of 100",
                      12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "3D column chart of exam questions per section: regulations 25, station and safety 21, electronics 13, antennas 13, operating 9, propagation 8, components 6, interference 5")


# 2. Deck structure: card stacks --------------------------------------------------
def card_stack(cx, base, n_cards, label_top, label_bottom, hl=False):
    out = []
    layers = max(3, round(n_cards / 12))
    for k in range(layers):
        y = base - k * 3.2
        out.append(f'<rect x="{cx - 34 + k * 0.6:.1f}" y="{y - 46:.1f}" width="68" height="46" rx="6" '
                   f'fill="{"#d97706" if hl else "#2d3748"}" stroke="#cbd5e0" stroke-opacity="0.35"/>')
    top_y = base - (layers - 1) * 3.2
    out.append(f'<rect x="{cx - 34 + (layers - 1) * 0.6:.1f}" y="{top_y - 46:.1f}" width="68" height="46" rx="6" fill="url(#gloss)"/>')
    out.insert(0, f'<ellipse cx="{cx}" cy="{base + 4}" rx="44" ry="7" fill="#000" fill-opacity="0.4"/>')
    out.append(text(cx + (layers - 1) * 0.6, top_y - 17, label_top, 16, "#fff", weight="bold"))
    out.append(text(cx, base + 24, label_bottom, 11, MUTED))
    return out, top_y - 46


def deck_structure():
    bank, _ = counts()
    w, h = 780, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(390, 46, "ISED Basic Qualification (2025-07-15)", 16, AMBER_LIGHT, weight="bold"))
    xs = [70 + i * 91.5 for i in range(8)]
    base = 350
    tops = {}
    for s in sorted(bank):
        layers = max(3, round(bank[s] / 12))
        tops[s] = base - (layers - 1) * 3.2 - 46
    for i, s in enumerate(sorted(bank)):
        parts.append(f'<path d="M390,214 C390,250 {xs[i]:.1f},226 {xs[i]:.1f},{tops[s] - 6:.1f}" '
                     f'fill="none" stroke="{AMBER}" stroke-opacity="0.45" stroke-width="2"/>')
    root, _ = card_stack(390, 180, 144, "984", "", hl=True)
    parts += root
    parts.append(text(390, 204, "the whole bank", 11, MUTED))
    for i, s in enumerate(sorted(bank)):
        stack, _ = card_stack(xs[i], base, bank[s], str(bank[s]), s)
        parts += stack
        parts.append(text(xs[i], base + 40, SHORT[s], 10, TEXT))
    parts.append(text(w / 2, h - 30, "stack height shows the number of cards in each section's subdeck", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A root stack of 984 cards branching into eight section subdecks, each stack sized by its card count")


# 3. Study loop -------------------------------------------------------------------
def study_loop():
    w, h = 780, 460
    cx, cy, rx, ry = 360, 245, 200, 125
    extra = ('<linearGradient id="ring" x1="0" y1="0" x2="1" y2="1">'
             '<stop offset="0" stop-color="#f59e0b"/><stop offset="1" stop-color="#2f855a"/></linearGradient>'
             '<marker id="arrowred" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
             'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#fc8181"/></marker>')
    parts = [common_defs(extra), panel(15, 15, w - 30, h - 30)]
    parts.append(f'<ellipse cx="{cx}" cy="{cy + 10}" rx="{rx}" ry="{ry}" fill="none" stroke="#000" stroke-opacity="0.35" stroke-width="16"/>')
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#ring)" stroke-width="12" stroke-opacity="0.85"/>')
    parts.append(f'<ellipse cx="{cx}" cy="{cy - 3}" rx="{rx}" ry="{ry}" fill="none" stroke="#fff" stroke-opacity="0.25" stroke-width="3"/>')
    for deg in (45, 135, 225, 315):
        a = math.radians(deg)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        ang = math.degrees(math.atan2(ry * math.cos(a), -rx * math.sin(a)))
        parts.append(f'<path d="M-9,-9 L5,0 L-9,9" fill="none" stroke="#fff" stroke-width="3.5" stroke-linecap="round" '
                     f'stroke-linejoin="round" transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})"/>')

    def pill(x, y, lab, fill, fg="#fff", wpx=None):
        wpx = wpx or 9 * len(lab) + 30
        return [f'<rect x="{x - wpx / 2:.1f}" y="{y - 20:.1f}" width="{wpx}" height="40" rx="20" fill="{fill}"/>',
                f'<rect x="{x - wpx / 2:.1f}" y="{y - 20:.1f}" width="{wpx}" height="40" rx="20" fill="url(#gloss)"/>',
                text(x, y + 5, lab, 14, fg, weight="bold")]

    parts += pill(cx, cy - ry, "Drill the section's cards", "#2d3748")
    parts += pill(cx + rx, cy, "Right, and know why?", "#d97706", "#1a1a1a")
    parts += pill(cx, cy + ry, "Anki spaces it out", "#2f855a")
    parts += pill(cx - rx, cy, "Review comes due", "#2d3748")
    # entry
    parts += pill(130, 62, "Learn the idea first", "#4a5568")
    parts.append(f'<path d="M230,62 Q{cx - 60},60 {cx - 70},{cy - ry - 22}" fill="none" stroke="{AMBER}" stroke-width="3" marker-end="url(#arrow)"/>')
    # red branch: guessed or wrong
    bx, by = 655, 395
    parts.append(f'<path d="M{cx + rx},{cy + 22} Q{cx + rx + 10},{by - 30} {bx - 10},{by - 30}" fill="none" stroke="#fc8181" '
                 f'stroke-width="3" stroke-dasharray="6 5" marker-end="url(#arrowred)"/>')
    parts.append(f'<rect x="{bx - 115}" y="{by - 28}" width="230" height="60" rx="16" fill="#c53030" fill-opacity="0.85"/>')
    parts.append(f'<rect x="{bx - 115}" y="{by - 28}" width="230" height="60" rx="16" fill="url(#gloss)"/>')
    parts.append(text(bx, by - 6, "Guessed or wrong:", 14, "#fff", weight="bold"))
    parts.append(text(bx, by + 14, "mark it wrong, re-read the idea", 13, "#fff"))
    parts.append(f'<path d="M{bx + 40},{by - 30} Q{bx + 80},{cy - ry - 20} {cx + 130},{cy - ry - 4}" fill="none" stroke="#fc8181" '
                 f'stroke-width="3" stroke-dasharray="6 5" marker-end="url(#arrowred)"/>')
    parts.append(text(cx + rx * 0.62, cy + ry * 0.5, "yes", 13, GREEN, "start", "bold"))
    parts.append(text(cx + rx + 70, cy + 70, "no", 13, "#fc8181", "start", "bold"))
    parts.append(text(cx + 5, cy - 4, "the loop that", 13, MUTED, italic=True))
    parts.append(text(cx + 5, cy + 14, "builds understanding", 13, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Study loop: learn the idea, drill the cards, check you know why; correct answers get spaced out by Anki, guessed or wrong ones send you back to re-read the idea")


FIGURES = {
    "exam_composition.svg": exam_composition,
    "deck_structure.svg": deck_structure,
    "study_loop.svg": study_loop,
}


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in FIGURES.items():
        (OUT / name).write_text(fn())
        print("wrote", OUT / name)


if __name__ == "__main__":
    main()
