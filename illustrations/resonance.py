#!/usr/bin/env python3
"""Figures for docs/resonance.md.

Worked values (computed): 10 uH with 50 pF resonates at 7.12 MHz, where each
reactance is about 447 ohms. With 5 ohms of series resistance Q is about 89 and
the half-power bandwidth about 80 kHz; with 50 ohms, Q about 9 and about 800 kHz.
f = 1 / (2 pi sqrt(LC)); bandwidth = f / Q; Q = X / R for a series circuit.

Usage:
    python3 illustrations/resonance.py
"""

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "resonance"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"
L_H, C_F = 10e-6, 50e-12
FR = 1 / (2 * math.pi * math.sqrt(L_H * C_F))


def xl(f):
    return 2 * math.pi * f * L_H


def xc(f):
    return 1 / (2 * math.pi * f * C_F)


def plot_frame(parts, L, R, T, B, xlabels, ylabels, xlab):
    for y, lab in ylabels:
        parts.append(f'<line x1="{L}" y1="{y:.1f}" x2="{R}" y2="{y:.1f}" stroke="#3a4250" stroke-width="1"/>')
        parts.append(text(L - 8, y + 4, lab, 11, MUTED, "end"))
    for x, lab in xlabels:
        parts.append(text(x, B + 20, lab, 11, MUTED))
    parts.append(text((L + R) / 2, B + 40, xlab, 12, MUTED, italic=True))


# 1. The crossing ----------------------------------------------------------------------------------------------
def crossing():
    w, h = 900, 450
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Resonance: where the coil's reactance equals the capacitor's", 16, AMBER_LIGHT, weight="bold"))
    L, R, T, B = 110, 840, 85, 350
    f0, f1, y0, y1 = 2e6, 25e6, 100.0, 2000.0

    def X(f):
        return L + (math.log10(f) - math.log10(f0)) / (math.log10(f1) - math.log10(f0)) * (R - L)

    def Y(v):
        return B - (math.log10(v) - math.log10(y0)) / (math.log10(y1) - math.log10(y0)) * (B - T)

    plot_frame(parts, L, R, T, B, [(X(f * 1e6), f"{f:g} MHz") for f in (2, 3.5, 7, 14, 25)],
               [(Y(v), f"{v:g} Ω") for v in (100, 200, 500, 1000, 2000)], "frequency (logarithmic)")

    def line(fn, col):
        pts, f = [], f0
        while f <= f1:
            v = fn(f)
            if y0 <= v <= y1:
                pts.append(f"{X(f):.1f},{Y(v):.1f}")
            f *= 1.02
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="4"/>'

    parts.append(line(xl, AMBER))
    parts.append(line(xc, BLUE))
    parts.append(text(X(20e6), Y(xl(20e6)) + 28, "10 µH coil", 13, AMBER, weight="bold"))
    parts.append(text(X(2.1e6), Y(420), "50 pF capacitor", 13, BLUE, "start", weight="bold"))
    parts.append(f'<line x1="{X(FR):.1f}" y1="{T}" x2="{X(FR):.1f}" y2="{B}" stroke="{GREEN}" stroke-width="2" stroke-dasharray="6 5"/>')
    parts.append(f'<circle cx="{X(FR):.1f}" cy="{Y(xl(FR)):.1f}" r="8" fill="{GREEN}" stroke="#ffffff" stroke-width="2"/>')
    parts.append(text(X(FR) + 10, B - 14, "7.12 MHz: both 447 Ω", 13, GREEN, "start", weight="bold"))
    parts.append(text(w / 2, 420, "Below resonance the capacitor dominates; above it the coil does. At resonance they cancel.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A log-log graph from 2 to 25 megahertz. The reactance of a 10 microhenry coil rises and the reactance of a 50 picofarad capacitor falls; they cross at 7.12 megahertz, where both are 447 ohms. Below resonance the capacitor dominates, above it the coil does, and at resonance they cancel.")


# 2. Series vs parallel ----------------------------------------------------------------------------------------
def series_parallel():
    w, h = 900, 450
    parts = [common_defs(), panel(15, 15, 425, h - 30), panel(460, 15, 425, h - 30)]
    rs = 5.0

    def zs(f):
        return math.sqrt(rs ** 2 + (xl(f) - xc(f)) ** 2)

    def zp(f):
        # parallel tank, with the coil's 5 ohm loss resistance in series with L
        zl = complex(rs, xl(f))
        zc = complex(0, -xc(f))
        return abs(zl * zc / (zl + zc))

    for k, (title, fn, col, note1, note2, lo, hi) in enumerate([
        ("Series: impedance dips", zs, BLUE, "lowest impedance, greatest current", "at resonance: passes it", 1.0, 1e5),
        ("Parallel: impedance peaks", zp, PURPLE, "highest impedance", "at resonance: blocks it", 1.0, 1e5)]):
        x0 = 15 + k * 445
        L, R, T, B = x0 + 70, x0 + 400, 90, 330
        parts.append(text(x0 + 212, 50, title, 15, AMBER_LIGHT, weight="bold"))
        f0, f1 = 5e6, 10e6

        def X(f):
            return L + (f - f0) / (f1 - f0) * (R - L)

        def Y(v):
            return B - (math.log10(v) - math.log10(lo)) / (math.log10(hi) - math.log10(lo)) * (B - T)

        plot_frame(parts, L, R, T, B, [(X(f * 1e6), f"{f:g}") for f in (5, 6, 7, 8, 9, 10)],
                   [(Y(v), lab) for v, lab in ((1, "1 Ω"), (100, "100 Ω"), (1e4, "10 kΩ"))], "frequency (MHz)")
        pts, f = [], f0
        while f <= f1:
            v = max(min(fn(f), hi), lo)
            pts.append(f"{X(f):.1f},{Y(v):.1f}")
            f += 2e4
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="4"/>')
        parts.append(f'<line x1="{X(FR):.1f}" y1="{T}" x2="{X(FR):.1f}" y2="{B}" stroke="{GREEN}" stroke-width="1.5" stroke-dasharray="5 4"/>')
        parts.append(text(x0 + 212, 396, note1, 13, TEXT, weight="bold"))
        parts.append(text(x0 + 212, 414, note2, 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Two graphs of impedance against frequency from 5 to 10 megahertz, for a 10 microhenry coil and a 50 picofarad capacitor. Series: the impedance dips sharply to its lowest at the 7.12 megahertz resonance, where the current is greatest, so the circuit passes that frequency. Parallel: the impedance peaks sharply at the same frequency, so the circuit blocks it.")


# 3. Bandwidth -----------------------------------------------------------------------------------------------------
def bandwidth():
    w, h = 900, 450
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Bandwidth: resistance widens the response but doesn't move it", 16, AMBER_LIGHT, weight="bold"))
    L, R, T, B = 110, 840, 90, 350
    f0, f1 = 5.5e6, 8.7e6

    def X(f):
        return L + (f - f0) / (f1 - f0) * (R - L)

    def Y(v):
        return B - v * (B - T)

    plot_frame(parts, L, R, T, B, [(X(f * 1e6), f"{f:g} MHz") for f in (6, 6.5, 7, 7.5, 8, 8.5)],
               [(Y(v), lab) for v, lab in ((0, "0"), (0.5, "half power"), (1, "full"))], "frequency")
    for rs, col, lab in [(5, GREEN, "5 Ω: narrow, about 80 kHz"), (50, AMBER, "50 Ω: wide, about 800 kHz")]:
        pts, f = [], f0
        while f <= f1:
            p = rs ** 2 / (rs ** 2 + (xl(f) - xc(f)) ** 2)
            pts.append(f"{X(f):.1f},{Y(p):.1f}")
            f += 5e3
        parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="3.5"/>')
        bw = FR / (xl(FR) / rs)
        y = Y(0.5)
        parts.append(f'<line x1="{X(FR - bw / 2):.1f}" y1="{y:.1f}" x2="{X(FR + bw / 2):.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="5"/>')
        if rs == 5:
            parts.append(text(L + 12, 120, lab, 13, col, "start", weight="bold"))
        else:
            parts.append(text(X(FR) + 230, 190, lab, 13, col, "start", weight="bold"))
    parts.append(f'<line x1="{X(FR):.1f}" y1="{T}" x2="{X(FR):.1f}" y2="{B}" stroke="{TEXT}" stroke-width="1" stroke-dasharray="4 4"/>')
    parts.append(text(X(FR), T - 8, "7.12 MHz either way", 12, TEXT))
    parts.append(text(w / 2, 420, "Power delivered by a series tuned circuit; bandwidth measured between the half-power (−3 dB) points.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Power delivered by a series tuned circuit of 10 microhenries and 50 picofarads, against frequency from 5.5 to 8.7 megahertz, for two series resistances. With 5 ohms the response is a narrow spike about 80 kilohertz wide at the half-power points; with 50 ohms it is a broad hump about 800 kilohertz wide. Both are centred on 7.12 megahertz: resistance widens the response but doesn't move it.")


# 4. A trap dipole -----------------------------------------------------------------------------------------------
def trap_dipole():
    w, h = 900, 420
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "A trap: a parallel tuned circuit that cuts a wire off at one frequency", 16, AMBER_LIGHT, weight="bold"))
    for row, (y, band, inner_col, outer_col, note) in enumerate([
        (150, "On the trap's frequency", GREEN, shade(MUTED, -0.4), "the traps are high impedance: only the inner wires radiate"),
        (290, "On a lower band", GREEN, GREEN, "the traps pass the current on: the whole wire radiates")]):
        parts.append(text(80, y - 38, band, 14, AMBER_LIGHT, "start", weight="bold"))
        parts.append(f'<line x1="90" y1="{y}" x2="260" y2="{y}" stroke="{outer_col}" stroke-width="5"/>')
        parts.append(f'<line x1="300" y1="{y}" x2="430" y2="{y}" stroke="{inner_col}" stroke-width="5"/>')
        parts.append(f'<line x1="470" y1="{y}" x2="600" y2="{y}" stroke="{inner_col}" stroke-width="5"/>')
        parts.append(f'<line x1="640" y1="{y}" x2="810" y2="{y}" stroke="{outer_col}" stroke-width="5"/>')
        parts += box3d(260, y + 14, 40, 18, 28, PURPLE, shadow=False)
        parts += box3d(600, y + 14, 40, 18, 28, PURPLE, shadow=False)
        parts.append(f'<rect x="430" y="{y - 10}" width="40" height="20" rx="4" fill="#4a5568"/>')
        parts.append(f'<line x1="450" y1="{y + 10}" x2="450" y2="{y + 50}" stroke="#4a5568" stroke-width="4"/>')
        parts.append(text(450, y + 66, "feedline", 11, MUTED, italic=True))
        parts.append(text(280, y - 32, "trap", 11, PURPLE, weight="bold"))
        parts.append(text(620, y - 32, "trap", 11, PURPLE, weight="bold"))
        parts.append(text(450, y + 90, note, 12, TEXT))
    return svg(w, h, "\n".join(parts), "A dipole with a trap, a parallel coil and capacitor, partway along each side. Top: on the trap's own resonant frequency the traps are high impedance, so only the inner sections of wire radiate and the outer sections are cut off. Bottom: on a lower band the traps pass the current on, and the whole wire radiates. One antenna works on two bands.")


FIGURES = {"crossing.svg": crossing, "series_parallel.svg": series_parallel, "bandwidth.svg": bandwidth,
           "trap_dipole.svg": trap_dipole}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
