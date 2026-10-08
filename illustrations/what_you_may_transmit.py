#!/usr/bin/env python3
"""Figures for docs/what_you_may_transmit.md.

Sources (fetched 2026-10-08):
- RBR-4 Issue 3 (July 2022): Schedule I bands, maximum bandwidths (Column II)
  and qualifications (Column IV); section 4 (bandwidth measured 26 dB below
  the signal's maximum); section 9 (identification); section 10 (power); note
  C21 (60 m channels: 2.8 kHz, 100 W ERP PEP, designators 2K80J3E telephony,
  150HA1A CW).
- Wavelength band names use wavelength (m) = 300 / f (MHz).

Usage:
    python3 illustrations/what_you_may_transmit.py
"""

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "what_you_may_transmit"
BLUE = "#4299e1"

# (name, low MHz, high MHz, bandwidth kHz) from RBR-4 Schedule I
HF = [("160 m", 1.8, 2.0, 6), ("80 m", 3.5, 4.0, 6), ("60 m", 5.3305, 5.4065, 2.8), ("40 m", 7.0, 7.3, 6),
      ("30 m", 10.1, 10.15, 1), ("20 m", 14.0, 14.35, 6), ("17 m", 18.068, 18.168, 6), ("15 m", 21.0, 21.45, 6),
      ("12 m", 24.89, 24.99, 6), ("10 m", 28.0, 29.7, 20)]
VU = [("6 m", 50, 54, 30), ("2 m", 144, 148, 30), ("1.25 m", 219, 225, 100), ("70 cm", 430, 450, 12000),
      ("33 cm", 902, 928, 12000)]


# 1. The band map ----------------------------------------------------------------------------------
def band_map():
    w, h = 900, 430
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Canada's amateur bands from 1.8 to 928 MHz (RBR-4 Schedule I), log scale", 17, AMBER_LIGHT, weight="bold"))
    L, R = 60, 860
    lo, hi = math.log10(1.5), math.log10(1100)
    xf = lambda f: L + (math.log10(f) - lo) / (hi - lo) * (R - L)
    y = 230
    parts.append(f'<rect x="{L}" y="{y - 3}" width="{R - L}" height="6" rx="3" fill="#4a5568"/>')
    for k, (name, a, b, _) in enumerate(HF + VU):
        x0, x1 = xf(a), xf(b)
        col = GREEN if b <= 30 else BLUE
        hgt = 70
        parts += box3d(x0, y, max(x1 - x0, 5), 14, hgt, col, shadow=False)
        up = k % 2 == 0
        ty = y - hgt - 30 if up else y + 34
        parts.append(text((x0 + x1) / 2 + 4, ty, name, 11, TEXT, weight="bold"))
    x30 = xf(30)
    parts.append(f'<line x1="{x30:.1f}" y1="100" x2="{x30:.1f}" y2="330" stroke="{RED}" stroke-width="2" stroke-dasharray="6 4"/>')
    parts.append(text(x30, 94, "30 MHz", 13, RED, weight="bold"))
    for f in (2, 5, 10, 20, 50, 100, 200, 500, 1000):
        parts.append(text(xf(f), y + 76, f"{f:g} MHz", 10, MUTED))
    parts.append(f'<rect x="200" y="350" width="14" height="14" rx="3" fill="{GREEN}"/>')
    parts.append(text(222, 362, "below 30 MHz: Honours, Morse, or Advanced (with Basic)", 12, TEXT, "start"))
    parts.append(f'<rect x="200" y="374" width="14" height="14" rx="3" fill="{BLUE}"/>')
    parts.append(text(222, 386, "above 30 MHz: Basic", 12, TEXT, "start"))
    return svg(w, h, "\n".join(parts), "Canada's amateur bands from 1.8 to 928 megahertz on a logarithmic frequency scale, from RBR-4 Schedule I. Below the 30 megahertz line, in green, the HF bands named by wavelength: 160, 80, 60, 40, 30, 20, 17, 15, 12 and 10 metres, which need Honours, Morse, or Advanced with Basic. Above it, in blue, the 6 metre, 2 metre, 1.25 metre, 70 centimetre and 33 centimetre bands, open to Basic. The microwave bands above 1 gigahertz continue off the right edge.")


# 2. How wide a signal may be ------------------------------------------------------------------------
def bandwidths():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Maximum bandwidth by band (RBR-4 Column II), and where a 2.8 kHz voice signal fits", 16, AMBER_LIGHT, weight="bold"))
    rows = [("30 m", 1), ("most HF bands", 6), ("10 m", 20), ("6 m and 2 m", 30), ("1.25 m", 100), ("70 cm, 33 cm", 12000)]
    L, R = 230, 840
    lo, hi = math.log10(0.1), math.log10(20000)
    xb = lambda k: L + (math.log10(k) - lo) / (hi - lo) * (R - L)
    for k, (name, bw) in enumerate(rows):
        y = 110 + k * 46
        ok = bw >= 2.8
        parts.append(text(L - 12, y + 6, name, 13, TEXT, "end", weight="bold"))
        parts.append(f'<rect x="{L}" y="{y - 10}" width="{xb(bw) - L:.1f}" height="22" rx="6" fill="{GREEN if ok else RED}" fill-opacity="0.8"/>')
        parts.append(f'<rect x="{L}" y="{y - 10}" width="{xb(bw) - L:.1f}" height="22" rx="6" fill="url(#gloss)" opacity="0.4"/>')
        lab = f"{bw:g} kHz" if bw < 1000 else f"{bw / 1000:g} MHz"
        parts.append(text(xb(bw) + 8, y + 6, lab, 13, TEXT, "start", weight="bold"))
    x28 = xb(2.8)
    parts.append(f'<line x1="{x28:.1f}" y1="88" x2="{x28:.1f}" y2="370" stroke="{AMBER_LIGHT}" stroke-width="2" stroke-dasharray="6 4"/>')
    parts.append(text(x28, 386, "single-sideband voice: 2.8 kHz", 12, AMBER_LIGHT, weight="bold"))
    x15 = xb(0.15)
    parts.append(f'<line x1="{x15:.1f}" y1="88" x2="{x15:.1f}" y2="370" stroke="#90cdf4" stroke-width="2" stroke-dasharray="6 4"/>')
    parts.append(text(x15 + 4, 404, "Morse (CW): 150 Hz", 12, "#90cdf4", weight="bold"))
    parts.append(text(w / 2, 424, "voice and CW widths from the emission designators in RBR-4 note C21; bar length on a log scale", 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Bars of the maximum bandwidth RBR-4 allows by band, on a logarithmic scale: 1 kilohertz on 30 metres, 6 kilohertz on most HF bands, 20 on 10 metres, 30 on 6 and 2 metres, 100 on 1.25 metres, and 12 megahertz on 70 and 33 centimetres. A dashed line at 2.8 kilohertz, the width of single-sideband voice, crosses every bar except 30 metres, where voice is too wide to fit. Morse code at 150 hertz fits everywhere.")


# 3. A signal at the band edge -------------------------------------------------------------------------
def band_edge():
    w, h = 900, 380
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Upper-sideband voice near the top of the 20 m band (edge 14.350 MHz)", 17, AMBER_LIGHT, weight="bold"))
    L, R = 80, 820
    f0, f1 = 14.343, 14.353
    xf = lambda f: L + (f - f0) / (f1 - f0) * (R - L)
    edge = xf(14.350)
    parts.append(f'<rect x="{edge:.1f}" y="90" width="{R - edge:.1f}" height="230" fill="{RED}" fill-opacity="0.12"/>')
    parts.append(f'<line x1="{edge:.1f}" y1="90" x2="{edge:.1f}" y2="320" stroke="{RED}" stroke-width="3"/>')
    parts.append(text(edge + 8, 108, "outside the band", 12, RED, "start", weight="bold"))
    for k, (carrier, col, verdict) in enumerate([(14.346, GREEN, "14.346 MHz: occupies to 14.3488, inside"),
                                                (14.348, RED, "14.348 MHz: occupies to 14.3508, over the edge")]):
        y = 190 + k * 90
        x0, x1 = xf(carrier), xf(carrier + 0.0028)
        parts += box3d(x0, y, x1 - x0, 20, 50, col, shadow=False)
        parts.append(f'<line x1="{x0:.1f}" y1="{y - 60}" x2="{x0:.1f}" y2="{y + 6}" stroke="{TEXT}" stroke-width="2"/>')
        parts.append(text(x0 - 6, y - 20, verdict, 12, TEXT, "end", weight="bold"))
    for f in (14.344, 14.346, 14.348, 14.350, 14.352):
        parts.append(text(xf(f), 352, f"{f:.3f}", 11, MUTED))
    return svg(w, h, "\n".join(parts), "Two upper-sideband voice signals, each 2.8 kilohertz wide, near the 14.350 megahertz top edge of the 20 metre band. One with its carrier at 14.346 megahertz occupies up to 14.3488, inside the band. One at 14.348 occupies up to 14.3508, crossing the edge into the shaded region outside the band.")


# 4. Power limits ---------------------------------------------------------------------------------------------
def power_limits():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Power limits by qualification (RBR-4 section 10)", 17, AMBER_LIGHT, weight="bold"))
    groups = [("DC input to the final stage", 250, 1000), ("SSB output, peak envelope power", 560, 2250),
              ("other modes, carrier power", 190, 750)]
    base, scale = 330, 0.1
    for k, (name, basic, adv) in enumerate(groups):
        x = 110 + k * 260
        for j, (val, col, lab) in enumerate([(basic, BLUE, "Basic"), (adv, AMBER, "Advanced")]):
            bx = x + j * 90
            parts += box3d(bx, base, 66, 30, val * scale, col)
            parts.append(text(bx + 42, base - val * scale - 24, f"{val:,} W", 14, TEXT, weight="bold"))
            parts.append(text(bx + 33, base + 22, lab, 11, MUTED))
        parts.append(text(x + 78, base + 46, name, 12, TEXT, weight="bold"))
    parts.append(text(w / 2, 410, "An amplifier may not be capable of more than 3 dB (twice) these limits (section 10.1).", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Three pairs of 3D bars for the RBR-4 power limits. DC input to the final stage: Basic 250 watts, Advanced 1,000. Single-sideband output as peak envelope power: Basic 560 watts, Advanced 2,250. Carrier power for other modes: Basic 190 watts, Advanced 750. An amplifier at the station may not be capable of more than 3 decibels, twice, those limits.")


# 5. When to identify -------------------------------------------------------------------------------------------
def identification():
    w, h = 900, 330
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "A 75-minute contact: when the call sign must be sent (RBR-4 section 9)", 17, AMBER_LIGHT, weight="bold"))
    L, R, y = 90, 810, 170
    xt = lambda t: L + t / 75 * (R - L)
    parts.append(f'<rect x="{L}" y="{y - 14}" width="{R - L}" height="28" rx="14" fill="#2d3748"/>')
    parts.append(f'<rect x="{L}" y="{y - 14}" width="{R - L}" height="28" rx="14" fill="{BLUE}" fill-opacity="0.35"/>')
    marks = [(0, "start"), (30, "30 min"), (60, "60 min"), (75, "end")]
    for t, lab in marks:
        x = xt(t)
        parts.append(f'<circle cx="{x:.1f}" cy="{y}" r="16" fill="url(#vball)"/>')
        parts.append(text(x, y + 5, "ID", 11, "#1a1a1a", weight="bold"))
        parts.append(text(x, y + 42, lab, 13, TEXT, weight="bold"))
    for t in range(0, 76, 15):
        parts.append(text(xt(t), y - 26, f"{t}", 10, MUTED))
    parts.append(text(w / 2, 262, "at the beginning and end of each exchange or test, and at intervals of no more than 30 minutes", 13, TEXT))
    parts.append(text(w / 2, 284, "each station sends its own call sign, in English or French", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A timeline of a 75-minute contact with the call sign sent at the start, at 30 minutes, at 60 minutes, and at the end: at the beginning and end of each exchange or test, and at intervals of no more than 30 minutes, each station sending its own call sign in English or French.")


FIGURES = {"band_map.svg": band_map, "bandwidths.svg": bandwidths, "band_edge.svg": band_edge,
           "power_limits.svg": power_limits, "identification.svg": identification}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
