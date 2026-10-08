#!/usr/bin/env python3
"""Figures for docs/reactance_and_impedance.md.

Worked values (computed): a 1 mH inductor is 6.28 ohms at 1 kHz and about
44 kilohms at 7 MHz; a 10 nF capacitor is about 15.9 kilohms at 1 kHz and
2.27 ohms at 7 MHz. Their reactances are equal near 50.3 kHz.
X_L = 2 pi f L, X_C = 1 / (2 pi f C); Z = sqrt(R^2 + X^2) for R and X in series.

Usage:
    python3 illustrations/reactance_and_impedance.py
"""

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "reactance_and_impedance"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"
L_H, C_F = 1e-3, 10e-9


def xl(f):
    return 2 * math.pi * f * L_H


def xc(f):
    return 1 / (2 * math.pi * f * C_F)


# 1. Reactance against frequency ------------------------------------------------------------------------------
def curves():
    w, h = 900, 470
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Reactance against frequency: a 1 mH coil and a 10 nF capacitor", 16, AMBER_LIGHT, weight="bold"))
    L, R, T, B = 120, 840, 90, 370
    f0, f1, x0, x1 = 100.0, 1e8, 0.1, 1e6

    def X(f):
        return L + (math.log10(f) - math.log10(f0)) / (math.log10(f1) - math.log10(f0)) * (R - L)

    def Y(x):
        return B - (math.log10(x) - math.log10(x0)) / (math.log10(x1) - math.log10(x0)) * (B - T)

    parts.append(f'<rect x="{L}" y="{T}" width="{X(20e3) - L:.1f}" height="{B - T}" fill="{shade(GREEN, -0.78)}"/>')
    parts.append(text((X(100) + X(20e3)) / 2, T + 18, "audio", 12, GREEN, weight="bold"))
    parts.append(f'<rect x="{X(3e6):.1f}" y="{T}" width="{X(30e6) - X(3e6):.1f}" height="{B - T}" fill="{shade(RED, -0.78)}"/>')
    parts.append(text((X(3e6) + X(30e6)) / 2, T + 18, "HF", 12, RED, weight="bold"))
    for x in (1, 100, 10000, 1000000):
        parts.append(f'<line x1="{L}" y1="{Y(x):.1f}" x2="{R}" y2="{Y(x):.1f}" stroke="#3a4250" stroke-width="1"/>')
        lab = {1: "1 Ω", 100: "100 Ω", 10000: "10 kΩ", 1000000: "1 MΩ"}[x]
        parts.append(text(L - 10, Y(x) + 4, lab, 11, MUTED, "end"))
    for f, lab in [(100, "100 Hz"), (1e3, "1 kHz"), (1e4, "10 kHz"), (1e5, "100 kHz"), (1e6, "1 MHz"), (1e7, "10 MHz"), (1e8, "100 MHz")]:
        parts.append(text(X(f), B + 20, lab, 11, MUTED))
    parts.append(text((L + R) / 2, B + 42, "frequency (logarithmic)", 12, MUTED, italic=True))

    def line(fn, col):
        pts = []
        f = f0
        while f <= f1:
            v = fn(f)
            if x0 <= v <= x1:
                pts.append(f"{X(f):.1f},{Y(v):.1f}")
            f *= 1.05
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="4"/>'

    parts.append(line(xl, AMBER))
    parts.append(line(xc, BLUE))
    parts.append(text(X(3e7) + 6, Y(xl(3e7)) + 26, "inductor: rises", 13, AMBER, "start", weight="bold"))
    parts.append(text(X(2500), Y(xc(2500)) - 14, "capacitor: falls", 13, BLUE, "start", weight="bold"))
    for f, fn, col in [(1e3, xl, AMBER), (7e6, xl, AMBER), (1e3, xc, BLUE), (7e6, xc, BLUE)]:
        parts.append(f'<circle cx="{X(f):.1f}" cy="{Y(fn(f)):.1f}" r="6" fill="{col}" stroke="#ffffff" stroke-width="1.5"/>')
    fr = 1 / (2 * math.pi * math.sqrt(L_H * C_F))
    parts.append(f'<circle cx="{X(fr):.1f}" cy="{Y(xl(fr)):.1f}" r="7" fill="none" stroke="{TEXT}" stroke-width="2"/>')
    parts.append(text(X(fr), Y(xl(fr)) - 14, "equal near 50 kHz", 11, TEXT))
    parts.append(text(w / 2, 448, "Both lines are straight on log axes: ten times the frequency, ten times the inductor's reactance, a tenth of the capacitor's.", 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A log-log graph of reactance against frequency from 100 hertz to 100 megahertz. The reactance of a 1 millihenry inductor rises in a straight line, from about 6 ohms at 1 kilohertz to about 44 kilohms at 7 megahertz. The reactance of a 10 nanofarad capacitor falls in a straight line, from about 16 kilohms at 1 kilohertz to about 2 ohms at 7 megahertz. The audio range and the HF range are shaded. The two lines cross near 50 kilohertz. Ten times the frequency gives ten times the inductor's reactance and a tenth of the capacitor's.")


# 2. Choke and bypass: audio vs RF -----------------------------------------------------------------------------
def choke_bypass():
    w, h = 900, 450
    parts = [common_defs(), panel(15, 15, 425, h - 30), panel(460, 15, 425, h - 30)]
    base, top = 320, 110

    def hgt(ohms):
        return (math.log10(ohms) + 0.5) / (math.log10(1e5) + 0.5) * (base - top)

    for k, (title, items, verdict, vcol) in enumerate([
        ("At 1 kHz (audio)", [("choke", xl(1e3), AMBER, "in series: low, audio passes"), ("bypass", xc(1e3), BLUE, "to ground: high, audio stays")], "audio reaches the amplifier", GREEN),
        ("At 7 MHz (RF)", [("choke", xl(7e6), AMBER, "in series: high, RF blocked"), ("bypass", xc(7e6), BLUE, "to ground: low, RF shunted")], "RF never gets there", RED)]):
        x0 = 15 + k * 445
        cx = x0 + 212
        parts.append(text(cx, 50, title, 16, AMBER_LIGHT, weight="bold"))
        for j, (name, ohms, col, note) in enumerate(items):
            x = x0 + 70 + j * 160
            hh = max(hgt(ohms), 6)
            parts += box3d(x, base, 90, 35, hh, col)
            val = f"{ohms / 1000:.0f} kΩ" if ohms >= 1000 else f"{ohms:.1f} Ω"
            parts.append(text(x + 55, base - hh - 24, val, 16, TEXT, weight="bold"))
            parts.append(text(x + 45, base + 24, name, 13, col, weight="bold"))
            parts.append(text(x + 45, base + 42, note, 10, MUTED, italic=True))
        parts += pill(cx, 395, verdict, vcol, size=13, h=30, wpx=260)
    return svg(w, h, "\n".join(parts), "Two panels comparing a 1 millihenry choke in series and a 10 nanofarad bypass capacitor to ground, on a log scale. At 1 kilohertz, audio: the choke is 6.3 ohms, low, so audio passes, and the bypass capacitor is 16 kilohms, high, so audio stays on the line; audio reaches the amplifier. At 7 megahertz, RF: the choke is 44 kilohms, high, so RF is blocked, and the capacitor is 2.3 ohms, low, so RF is shunted to ground; RF never gets there.")


# 3. Impedance triangle --------------------------------------------------------------------------------------------
def impedance():
    w, h = 900, 420
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Impedance: resistance and reactance combine at right angles", 16, AMBER_LIGHT, weight="bold"))
    ox, oy, s = 170, 330, 5.2
    rx, xy = 30 * s, 40 * s
    parts.append(f'<polygon points="{ox},{oy} {ox + rx},{oy} {ox + rx},{oy - xy}" fill="{shade(PURPLE, -0.7)}"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox + rx}" y2="{oy}" stroke="{GREEN}" stroke-width="7"/>')
    parts.append(f'<line x1="{ox + rx}" y1="{oy}" x2="{ox + rx}" y2="{oy - xy}" stroke="{AMBER}" stroke-width="7"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox + rx}" y2="{oy - xy}" stroke="{PURPLE}" stroke-width="7"/>')
    parts.append(f'<rect x="{ox + rx - 16}" y="{oy - 16}" width="16" height="16" fill="none" stroke="{TEXT}" stroke-width="1.5"/>')
    parts.append(text(ox + rx / 2, oy + 30, "resistance R = 30 Ω", 14, GREEN, weight="bold"))
    parts.append(text(ox + rx + 14, oy - xy / 2, "reactance X = 40 Ω", 14, AMBER, "start", weight="bold"))
    parts.append(text(ox + rx / 2 - 30, oy - xy / 2 - 10, "impedance Z = 50 Ω", 14, PURPLE, "end", weight="bold"))
    parts.append(text(640, 160, "Z = √(R² + X²)", 22, TEXT, weight="bold"))
    parts.append(text(640, 200, "√(30² + 40²) = √2,500 = 50 Ω", 14, TEXT))
    parts.append(text(640, 245, "not 30 + 40 = 70 Ω:", 13, RED, weight="bold"))
    parts.append(text(640, 267, "reactance is out of step with resistance", 12, MUTED, italic=True))
    parts.append(text(640, 289, "by a quarter-cycle, so they add like the", 12, MUTED, italic=True))
    parts.append(text(640, 311, "sides of a right triangle", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A right triangle. The horizontal side is resistance, 30 ohms; the vertical side is reactance, 40 ohms; the hypotenuse is impedance, 50 ohms. Impedance equals the square root of R squared plus X squared: the square root of 30 squared plus 40 squared is the square root of 2,500, which is 50 ohms, not 30 plus 40 equals 70, because reactance is a quarter-cycle out of step with resistance, so they add like the sides of a right triangle.")


FIGURES = {"curves.svg": curves, "choke_bypass.svg": choke_bypass, "impedance.svg": impedance}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
