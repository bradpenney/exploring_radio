#!/usr/bin/env python3
"""Figures for docs/decibels.md.

Sources (fetched 2026-10-09):
- Decibel: ten times the base-10 logarithm of a power ratio (standard definition).
- S-meter: 6 dB per S-unit; S9 = -73 dBm on HF (IARU Region 1 HF Manager's
  Handbook, section 4.1.3; the question bank cites the IARU recommendation).
- Half-wave dipole gain 2.15 dBi (ideal dipole, gain 1.64 over isotropic).

Usage:
    python3 illustrations/decibels.py
"""

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "decibels"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"


# 1. The dB ruler ---------------------------------------------------------------------------------------------
def ruler():
    w, h = 900, 400
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "The decibel ruler: equal steps in dB are equal multiplications of power", 15, AMBER_LIGHT, weight="bold"))
    L, R, y = 80, 840, 210

    def X(db):
        return L + (db + 10) / 40 * (R - L)

    parts += box3d(L, y + 18, R - L, 30, 18, shade(PURPLE, -0.35), shadow=True)
    marks = [(-10, "÷10", "0.1×"), (-6, "÷4", "0.25×"), (-3, "÷2", "0.5×"), (0, "×1", "same"), (3, "×2", ""), (6, "×4", ""),
             (10, "×10", ""), (13, "×20", ""), (20, "×100", ""), (30, "×1000", "")]
    for db, ratio, sub in marks:
        x = X(db)
        big = db in (0, 3, 10, 20, 30, -3, -10)
        col = GREEN if db > 0 else (RED if db < 0 else TEXT)
        parts.append(f'<line x1="{x:.1f}" y1="{y - (26 if big else 16)}" x2="{x:.1f}" y2="{y}" stroke="{col}" stroke-width="{3 if big else 2}"/>')
        parts.append(text(x, y - (34 if big else 24), f"{db:+d} dB" if db else "0 dB", 13 if big else 11, col, weight="bold"))
        parts.append(text(x, y + 58, ratio, 13 if big else 11, TEXT, weight="bold"))
    parts.append(text(X(-6.5), 320, "losses: negative dB", 13, RED, weight="bold"))
    parts.append(text(X(16), 320, "gains: positive dB", 13, GREEN, weight="bold"))
    parts.append(text(w / 2, 365, "Learn two anchors, +3 dB = ×2 and +10 dB = ×10; every other line here is built by adding them.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A decibel ruler from minus 10 to plus 30 dB with the matching power ratios: minus 10 dB divides by 10, minus 6 dB divides by 4, minus 3 dB divides by 2, 0 dB is the same, plus 3 dB doubles, plus 6 dB is 4 times, plus 10 dB is 10 times, plus 13 dB is 20 times, plus 20 dB is 100 times and plus 30 dB is 1,000 times. Losses are negative dB, gains positive. Learn two anchors, plus 3 dB is times 2 and plus 10 dB is times 10; every other value is built by adding them.")


# 2. Chains add -------------------------------------------------------------------------------------------------
def chain():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "In decibels, a chain of gains and losses just adds up", 16, AMBER_LIGHT, weight="bold"))

    def stage(x, y, wd, label, sub, col):
        out = box3d(x, y, wd, 36, 46, col)
        out.append(text(x + wd / 2, y - 18, label, 13, "#ffffff", weight="bold"))
        out.append(text(x + wd / 2, y + 24, sub, 12, TEXT))
        return out

    def arrow(x1, x2, y):
        return [f'<line x1="{x1}" y1="{y}" x2="{x2 - 10}" y2="{y}" stroke="{MUTED}" stroke-width="3"/>',
                f'<path d="M {x2} {y} l -12 -7 l 0 14 z" fill="{MUTED}"/>']

    # row 1: handheld + amplifier
    y1 = 175
    parts += stage(70, y1, 150, "handheld", "2 W", BLUE)
    parts += arrow(245, 340, y1 - 25)
    parts += stage(345, y1, 170, "amplifier", "+9 dB = ×8", GREEN)
    parts += arrow(540, 640, y1 - 25)
    parts += pill(735, y1 - 28, "16 W", GREEN, size=17, h=40, wpx=130)
    parts.append(text(735, y1 + 20, "2 × 8 = 16", 12, MUTED, italic=True))
    # row 2: transmitter + feedline loss
    y2 = 345
    parts += stage(70, y2, 150, "transmitter", "100 W", AMBER)
    parts += arrow(245, 340, y2 - 25)
    parts += stage(345, y2, 170, "feedline", "−6 dB = ÷4", RED)
    parts += arrow(540, 640, y2 - 25)
    parts += pill(735, y2 - 28, "25 W at the antenna", RED, size=14, h=40, wpx=210)
    parts.append(text(735, y2 + 20, "100 ÷ 4 = 25", 12, MUTED, italic=True))
    parts.append(text(w / 2, 405, "With several stages, add their dB first (+20 − 3 − 2 = +15 dB), then convert once.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Two signal chains. A 2 watt handheld feeds an amplifier with plus 9 dB of gain, which is times 8, giving 16 watts. A 100 watt transmitter feeds a feedline with 6 dB of loss, which is divide by 4, leaving 25 watts at the antenna. With several stages, add their decibels first, for example plus 20 minus 3 minus 2 is plus 15 dB, then convert once.")


# 3. The S-meter --------------------------------------------------------------------------------------------------
def smeter():
    w, h = 900, 460
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "An S-meter: 6 dB per S-unit up to S9, then dB over S9", 16, AMBER_LIGHT, weight="bold"))
    cx, cy, r = 450, 330, 230
    # dial face
    parts.append(f'<path d="M {cx - r - 20} {cy} A {r + 20} {r + 20} 0 0 1 {cx + r + 20} {cy} Z" fill="#f5ecd5" stroke="#5a4a2a" stroke-width="3"/>')
    marks = [(f"S{n}", (n - 1) * 6) for n in range(1, 10, 2)] + [("+20", 48 + 20), ("+40", 48 + 40), ("+60", 48 + 60)]
    span = 108.0

    def ang(db):
        return math.pi - (db / span) * math.pi * 0.86 - math.pi * 0.07

    for lab, db in marks:
        a = ang(db)
        x1, y1 = cx + (r - 18) * math.cos(a), cy - (r - 18) * math.sin(a)
        x2, y2 = cx + r * math.cos(a), cy - r * math.sin(a)
        col = "#222" if lab.startswith("S") else "#c53030"
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="3"/>')
        lx, ly = cx + (r - 42) * math.cos(a), cy - (r - 42) * math.sin(a)
        parts.append(text(lx, ly + 5, lab, 15, col, weight="bold"))
    for n in range(2, 10, 2):
        a = ang((n - 1) * 6)
        x1, y1 = cx + (r - 10) * math.cos(a), cy - (r - 10) * math.sin(a)
        x2, y2 = cx + r * math.cos(a), cy - r * math.sin(a)
        parts.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#222" stroke-width="2"/>')
    a9 = ang(48)
    parts.append(f'<path d="M {cx + r * math.cos(a9):.1f} {cy - r * math.sin(a9):.1f} A {r} {r} 0 0 1 {cx + r:.1f} {cy - 0.0:.1f}" fill="none" stroke="#c53030" stroke-width="5" opacity="0.6"/>')
    # needle at S9
    an = ang(48)
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r - 30) * math.cos(an):.1f}" y2="{cy - (r - 30) * math.sin(an):.1f}" stroke="#1a202c" stroke-width="4"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="12" fill="#1a202c"/>')
    parts.append(text(cx, cy - 40, "S9", 20, "#1a202c", weight="bold"))
    parts.append(text(cx, cy + 40, "one S-unit = 6 dB = ×4 power", 14, TEXT, weight="bold"))
    parts.append(text(cx, cy + 62, "S9 at 100 W becomes S8 at 25 W; \"20 dB over S9\" at 150 W becomes \"10 over\" at 15 W", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "An S-meter dial marked S1 to S9 in black, then plus 20, plus 40 and plus 60 dB over S9 in red, with the needle at S9. One S-unit is 6 dB, four times the power. A station heard at S9 with 100 watts reads S8 at 25 watts; one heard at 20 dB over S9 with 150 watts reads 10 dB over S9 at 15 watts.")


# 4. dBi and dBd ----------------------------------------------------------------------------------------------------
def antenna_gain():
    w, h = 900, 430
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Antenna gain needs a reference: isotropic (dBi) or dipole (dBd)", 16, AMBER_LIGHT, weight="bold"))
    # isotropic: circle pattern
    cx1, cy = 230, 220
    parts.append(f'<circle cx="{cx1}" cy="{cy}" r="95" fill="{shade(TEAL, -0.5)}" stroke="{TEAL}" stroke-width="3"/>')
    parts.append(f'<circle cx="{cx1}" cy="{cy}" r="6" fill="#ffffff"/>')
    parts.append(text(cx1, 335, "isotropic radiator: 0 dBi", 14, TEAL, weight="bold"))
    parts.append(text(cx1, 353, "an ideal point, equal in every direction", 12, MUTED, italic=True))
    # dipole: figure-eight pattern, seen with the dipole vertical in the page

    def lobe(cx, sign):
        pts = []
        for i in range(0, 181):
            t = math.radians(i)
            rr = 120 * abs(math.sin(t)) ** 1.6
            pts.append(f"{cx + sign * rr * math.sin(t):.1f},{cy - rr * math.cos(t):.1f}")
        return pts

    cx2 = 640
    pts = lobe(cx2, 1) + lobe(cx2, -1)[::-1]
    parts.append(f'<polygon points="{" ".join(pts)}" fill="{shade(AMBER, -0.45)}" stroke="{AMBER}" stroke-width="3"/>')
    parts.append(f'<circle cx="{cx2}" cy="{cy}" r="95" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="6 5"/>')
    parts.append(f'<line x1="{cx2}" y1="{cy - 45}" x2="{cx2}" y2="{cy + 45}" stroke="#ffffff" stroke-width="5"/>')
    parts.append(text(cx2 + 132, cy - 6, "+2.15 dB", 14, AMBER_LIGHT, "start", weight="bold"))
    parts.append(text(cx2, 335, "half-wave dipole: 2.15 dBi = 0 dBd", 14, AMBER, weight="bold"))
    parts.append(text(cx2, 353, "energy pulled from its ends into its sides", 12, MUTED, italic=True))
    parts += pill(w / 2, 388, "dBi = dBd + 2.15", PURPLE, size=14, h=32, wpx=220)
    return svg(w, h, "\n".join(parts), "Two radiation patterns. An isotropic radiator, an ideal point radiating equally in every direction, has 0 dBi. A half-wave dipole, drawn vertically, pulls energy from its ends into its sides, forming a figure-eight pattern that reaches 2.15 dB beyond the isotropic circle: 2.15 dBi, which is 0 dBd. So dBi equals dBd plus 2.15.")


FIGURES = {"ruler.svg": ruler, "chain.svg": chain, "smeter.svg": smeter, "antenna_gain.svg": antenna_gain}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
