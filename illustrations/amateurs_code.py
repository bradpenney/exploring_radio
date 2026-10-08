#!/usr/bin/env python3
"""Figures for docs/amateurs_code.md.

Sources: Radio Amateurs of Canada, Operating Guidelines (Bill Wilson VE3NR's
Code of Ethics, The Canadian Amateur, December 1997); ARRL, "Amateur Code"
(Paul M. Segal, W9EEA, 1928, revised twice since). RBR-4 Issue 3 for the
identification rule (call sign at least every 30 minutes).

Usage:
    python3 illustrations/amateurs_code.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, MUTED, TEXT, box3d, common_defs,  # noqa: E402
                     panel, render_all, svg, text)

OUT = HERE.parent / "docs" / "images" / "amateurs_code"


def pillars(x0, base, names, color, width=88, gap=14, height=150):
    out = []
    for i, name in enumerate(names):
        x = x0 + i * (width + gap)
        out += box3d(x, base, width, 26, height, color, shadow=(i == 0))
        out += box3d(x - 6, base - height, width + 12, 30, 12, "#cbd5e0", shadow=False)
        out += box3d(x - 6, base + 10, width + 12, 30, 10, "#a0aec0", shadow=False)
        cx, cy = x + width / 2 + 5, base - height / 2
        out.append(f'<text x="{cx:.1f}" y="{cy:.1f}" font-size="14" fill="#ffffff" text-anchor="middle" font-weight="bold" '
                   f'font-family="IBM Plex Sans, Helvetica, Arial, sans-serif" transform="rotate(-90 {cx:.1f} {cy:.1f})">{name}</text>')
    return out


def two_codes():
    w, h = 900, 470
    parts = [common_defs()]
    parts.append(panel(15, 15, 390, 440))
    parts.append(text(210, 50, "Code of Ethics for Canadian", 15, AMBER_LIGHT, weight="bold"))
    parts.append(text(210, 70, "Amateur Radio Operators", 15, AMBER_LIGHT, weight="bold"))
    parts.append(text(210, 92, "Bill Wilson, VE3NR · 1997", 12, MUTED, italic=True))
    parts += pillars(45, 330, ["Responsible", "Progressive", "Helpful", "Public Spirited"], "#b7791f", width=72, gap=14)
    parts.append(text(210, 400, "four qualities of", 12, TEXT))
    parts.append(text(210, 418, "\"the thoughtful Radio Amateur\"", 12, TEXT))
    parts.append(panel(420, 15, 465, 440))
    parts.append(text(652, 50, "The Radio Amateur's Code", 15, AMBER_LIGHT, weight="bold"))
    parts.append(text(652, 72, "Paul M. Segal, W9EEA · 1928", 12, MUTED, italic=True))
    parts += pillars(445, 330, ["Considerate", "Loyal", "Progressive", "Friendly", "Balanced", "Patriotic"], "#2c5282", width=58, gap=12)
    parts.append(text(652, 400, "six marks of", 12, TEXT))
    parts.append(text(652, 418, "\"the amateur spirit\"", 12, TEXT))
    return svg(w, h, "\n".join(parts), "Two codes of conduct drawn as rows of pillars. Left, the Code of Ethics for Canadian Amateur Radio Operators by Bill Wilson, VE3NR, 1997: Responsible, Progressive, Helpful, Public Spirited. Right, The Radio Amateur's Code by Paul M. Segal, W9EEA, 1928: Considerate, Loyal, Progressive, Friendly, Balanced, Patriotic.")


def law_and_code():
    w, h = 820, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Two rulebooks: the one you must follow, and the one that keeps the bands worth using", 15, TEXT, weight="bold"))
    rows = (("The law", "Radiocommunication Act, RBR-4", "#c53030", "enforced by ISED",
             ["identify at least every 30 minutes", "stay inside your qualification's bands", "no music, no business, no secret codes"]),
            ("The codes", "Wilson 1997, Segal 1928", "#2f855a", "enforced by no one",
             ["listen before you transmit", "slow down for a beginner", "be ready to help in an emergency"]))
    for i, (title, sub, color, who, items) in enumerate(rows):
        base = 180 + i * 150
        parts += box3d(60, base, 170, 40, 80, color)
        parts.append(text(145, base - 46, title, 18, "#ffffff", weight="bold"))
        parts.append(text(145, base - 26, sub, 11, "#e2e8f0"))
        parts.append(text(145, base + 30, who, 12, AMBER_LIGHT if i == 0 else "#9ae6b4", weight="bold"))
        for k, it in enumerate(items):
            parts.append(text(300, base - 74 + k * 30, "· " + it, 14, TEXT, "start"))
    parts.append(text(w / 2, 418, "The law sets the floor. The codes describe the operator everyone hopes to meet on the air.", 13, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Two 3D books. The law, the Radiocommunication Act and RBR-4, enforced by ISED: identify at least every 30 minutes, stay inside your qualification's bands, no music, business, or secret codes. The codes, Wilson 1997 and Segal 1928, enforced by no one: listen before you transmit, slow down for a beginner, be ready to help in an emergency.")


FIGURES = {"two_codes.svg": two_codes, "law_and_code.svg": law_and_code}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
