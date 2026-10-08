#!/usr/bin/env python3
"""Figures for docs/what_is_a_radio_wave.md.

Sources (fetched 2026-10-09):
- Band nomenclature (VLF 3-30 kHz ... EHF 30-300 GHz; HF 3-30 MHz,
  "decametric waves"): ITU Radio Regulations Article 2, No. 2.1, as
  reproduced in 47 CFR 2.101(a).
- Speed of light in vacuum, exactly 299 792 458 m/s: SI Brochure, 9th edition
  (BIPM), defining constant c.
- Amateur band edges: RBR-4 Issue 3, Schedule I.

Usage:
    python3 illustrations/what_is_a_radio_wave.py
"""

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "what_is_a_radio_wave"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"


# 1. The wave: two fields, one direction ------------------------------------------------------------------
def wave_fields():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "A radio wave: electric and magnetic fields, travelling together", 16, AMBER_LIGHT, weight="bold"))
    ox, oy = 110, 250          # origin
    length = 680               # along propagation (screen x)
    dz = (-0.55, 0.42)         # oblique direction for the depth axis

    def P(x, y, z):
        return ox + x + z * dz[0], oy - y + z * dz[1]

    # axis
    x0, y0 = P(0, 0, 0)
    x1, y1 = P(length, 0, 0)
    parts.append(f'<line x1="{x0}" y1="{y0}" x2="{x1 + 30}" y2="{y1}" stroke="{MUTED}" stroke-width="2"/>')
    parts.append(f'<path d="M {x1 + 30} {y1} l -12 -6 l 0 12 z" fill="{MUTED}"/>')
    parts.append(text(x1 + 20, y1 - 14, "direction of travel", 12, MUTED, "end", italic=True))
    cycles, amp = 2.0, 120
    e_pts, h_pts, e_fill, h_fill = [], [], [], []
    for i in range(0, 241):
        x = length * i / 240
        s = math.sin(2 * math.pi * cycles * i / 240)
        ex, ey = P(x, amp * s, 0)
        hx, hy = P(x, 0, amp * 1.15 * s)
        e_pts.append(f"{ex:.1f},{ey:.1f}")
        h_pts.append(f"{hx:.1f},{hy:.1f}")
        if i % 8 == 0:
            e_fill.append(f'<line x1="{P(x, 0, 0)[0]:.1f}" y1="{P(x, 0, 0)[1]:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{RED}" stroke-width="1" opacity="0.45"/>')
            h_fill.append(f'<line x1="{P(x, 0, 0)[0]:.1f}" y1="{P(x, 0, 0)[1]:.1f}" x2="{hx:.1f}" y2="{hy:.1f}" stroke="{BLUE}" stroke-width="1" opacity="0.45"/>')
    parts += h_fill
    parts.append(f'<polyline points="{" ".join(h_pts)}" fill="none" stroke="{BLUE}" stroke-width="3.5"/>')
    parts += e_fill
    parts.append(f'<polyline points="{" ".join(e_pts)}" fill="none" stroke="{RED}" stroke-width="3.5"/>')
    parts.append(text(P(85, amp + 18, 0)[0], P(85, amp + 18, 0)[1], "electric field (E)", 13, RED, weight="bold"))
    hx, hy = P(85, 0, amp * 1.15 + 30)
    parts.append(text(hx, hy + 6, "magnetic field (H)", 13, BLUE, weight="bold"))
    # wavelength bracket over one cycle (from first crest to second crest)
    c1, c2 = length / (cycles * 4), length / (cycles * 4) + length / cycles
    a = P(c1, amp + 40, 0)
    b = P(c2, amp + 40, 0)
    parts.append(f'<path d="M {a[0]} {a[1] + 8} L {a[0]} {a[1]} L {b[0]} {b[1]} L {b[0]} {b[1] + 8}" fill="none" stroke="{AMBER_LIGHT}" stroke-width="2"/>')
    parts.append(text((a[0] + b[0]) / 2, a[1] - 8, "one wavelength (λ): crest to crest", 13, AMBER_LIGHT, weight="bold"))
    parts.append(text(w / 2, 400, "The two fields are at right angles to each other and to the direction of travel, and move at the speed of light.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A radio wave drawn in three dimensions. A red sine wave, the electric field, oscillates in the vertical plane; a blue sine wave, the magnetic field, oscillates in the horizontal plane at right angles to it. Both travel together along an axis marked direction of travel. A bracket over one crest-to-crest cycle marks one wavelength. The two fields are at right angles to each other and to the direction of travel, and move at the speed of light.")


# 2. The spectrum ------------------------------------------------------------------------------------------------
def spectrum():
    w, h = 900, 470
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "The radio spectrum, in the ITU's decade bands", 16, AMBER_LIGHT, weight="bold"))
    bands = [("VLF", "3–30 kHz", "100–10 km"), ("LF", "30–300 kHz", "10–1 km"), ("MF", "0.3–3 MHz", "1 km–100 m"),
             ("HF", "3–30 MHz", "100–10 m"), ("VHF", "30–300 MHz", "10–1 m"), ("UHF", "0.3–3 GHz", "1 m–10 cm"),
             ("SHF", "3–30 GHz", "10–1 cm"), ("EHF", "30–300 GHz", "1 cm–1 mm")]
    cols = [shade(PURPLE, -0.2), shade(PURPLE, 0.0), TEAL, AMBER, GREEN, BLUE, shade(BLUE, -0.25), shade(RED, -0.2)]
    x0, bw = 70, 95
    for k, ((sym, fr, wl), col) in enumerate(zip(bands, cols)):
        x = x0 + k * bw
        hh = 70 if sym in ("HF", "VHF", "UHF") else 45
        parts += box3d(x, 260, bw - 8, 40, hh, col, shadow=(k == 0))
        parts.append(text(x + (bw - 8) / 2, 260 - hh / 2 + 5 - 12, sym, 15, "#ffffff", weight="bold"))
        parts.append(text(x + (bw - 8) / 2, 290, fr, 11, TEXT))
        parts.append(text(x + (bw - 8) / 2, 308, wl, 11, MUTED, italic=True))
    parts.append(text(x0 - 10, 290, "f", 12, MUTED, "end", italic=True))
    parts.append(text(x0 - 10, 308, "λ", 12, MUTED, "end", italic=True))
    # amateur band ticks, positioned on the log scale (3 kHz .. 300 GHz = 8 decades)

    def X(f_hz):
        return x0 + (math.log10(f_hz) - math.log10(3e3)) / 8 * (8 * bw - 8)

    ham = [(1.9e6, "160 m"), (3.75e6, "80 m"), (7.15e6, "40 m"), (14.2e6, "20 m"), (28.8e6, "10 m"),
           (52e6, "6 m"), (146e6, "2 m"), (440e6, "70 cm"), (1.27e9, "23 cm")]
    for k, (f, lab) in enumerate(ham):
        x = X(f)
        y = 158 - (k % 3) * 20
        parts.append(f'<line x1="{x:.1f}" y1="{y + 6}" x2="{x:.1f}" y2="196" stroke="{AMBER_LIGHT}" stroke-width="1.5" stroke-dasharray="3 3"/>')
        parts.append(text(x, y, lab, 11, AMBER_LIGHT, weight="bold"))
    parts.append(text(X(1e7), 96, "amateur bands named by wavelength", 12, AMBER_LIGHT, italic=True))
    # audio
    parts += pill(x0 + 40, 360, "audio: about 20 Hz–20 kHz", shade(MUTED, -0.4), size=11, h=26, wpx=200)
    parts.append(text(x0 - 5, 395, "below the radio spectrum; sound, not radio", 11, MUTED, "start", italic=True))
    parts += pill(560, 360, "7,125 kHz = 7.125 MHz: in HF", AMBER, size=12, h=28, wpx=260)
    parts.append(text(w / 2, 430, "Each band is ten times the frequency of the one before, and one-tenth the wavelength.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "The radio spectrum divided into the ITU's decade bands, each with its frequency and wavelength range: VLF 3 to 30 kilohertz, 100 to 10 kilometres; LF 30 to 300 kilohertz; MF 0.3 to 3 megahertz; HF 3 to 30 megahertz, 100 to 10 metres; VHF 30 to 300 megahertz, 10 to 1 metres; UHF 0.3 to 3 gigahertz; SHF 3 to 30 gigahertz; EHF 30 to 300 gigahertz, 1 centimetre to 1 millimetre. Amateur bands are marked on a log scale: 160, 80, 40, 20 and 10 metres in MF and HF, 6 and 2 metres in VHF, 70 and 23 centimetres in UHF. Audio, about 20 hertz to 20 kilohertz, sits below the radio spectrum. 7,125 kilohertz, or 7.125 megahertz, is in HF. Each band is ten times the frequency of the one before and one-tenth the wavelength.")


# 3. 300 over f -------------------------------------------------------------------------------------------------
def wavelength_bars():
    w, h = 900, 450
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Wavelength in metres = 300 ÷ frequency in megahertz", 17, AMBER_LIGHT, weight="bold"))
    rows = [(1.9, "160 m band"), (7.15, "40 m band"), (14.2, "20 m band"), (28.8, "10 m band"), (146, "2 m band"), (440, "70 cm band")]
    base, top = 330, 110
    for k, (f, lab) in enumerate(rows):
        lam = 300 / f
        hh = (math.log10(lam) + 0.5) / (math.log10(160) + 0.5) * (base - top)
        x = 95 + k * 125
        col = AMBER if f < 30 else (GREEN if f < 300 else BLUE)
        parts += box3d(x, base, 70, 35, hh, col)
        lamtxt = f"{lam:.0f} m" if lam >= 10 else (f"{lam:.2f} m" if lam >= 1 else f"{lam * 100:.0f} cm")
        parts.append(text(x + 47, base - hh - 22, lamtxt, 15, TEXT, weight="bold"))
        parts.append(text(x + 35, base + 26, f"{f:g} MHz", 12, TEXT))
        parts.append(text(x + 35, base + 44, lab, 11, MUTED, italic=True))
    parts.append(text(w / 2, 400, "Bar heights on a logarithmic scale. Double the frequency and the wavelength halves.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Bars on a logarithmic scale showing wavelength equals 300 divided by frequency in megahertz, for six amateur frequencies: 1.9 megahertz in the 160 metre band, 158 metres; 7.15 megahertz in the 40 metre band, 42 metres; 14.2 megahertz in the 20 metre band, 21 metres; 28.8 megahertz in the 10 metre band, 10.4 metres; 146 megahertz in the 2 metre band, 2.05 metres; 440 megahertz in the 70 centimetre band, 68 centimetres. Double the frequency and the wavelength halves.")


# 4. Phase and harmonics ----------------------------------------------------------------------------------------
def phase_harmonics():
    w, h = 900, 400
    parts = [common_defs(), panel(15, 15, 425, h - 30), panel(460, 15, 425, h - 30)]

    def wave(x0, y0, wid, amp, cyc, ph, col, sw=3, dash=None):
        pts = []
        for i in range(201):
            t = i / 200
            pts.append(f"{x0 + wid * t:.1f},{y0 - amp * math.sin(2 * math.pi * cyc * t + ph):.1f}")
        d = f' stroke-dasharray="{dash}"' if dash else ""
        return f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="{sw}"{d}/>'

    # phase panel
    parts.append(text(227, 50, "Phase: same frequency, shifted in time", 14, AMBER_LIGHT, weight="bold"))
    parts.append(f'<line x1="45" y1="200" x2="410" y2="200" stroke="{MUTED}" stroke-width="1"/>')
    parts.append(wave(45, 200, 365, 85, 2, 0, AMBER))
    parts.append(wave(45, 200, 365, 85, 2, -math.pi / 2, TEAL))
    x_a, x_b = 45 + 365 / 8, 45 + 365 / 8 + 365 / 8
    parts.append(f'<path d="M {x_a:.1f} 98 L {x_b:.1f} 98" stroke="{AMBER_LIGHT}" stroke-width="2"/>')
    parts.append(text((x_a + x_b) / 2, 90, "90°", 13, AMBER_LIGHT, weight="bold"))
    parts.append(text(227, 320, "Both complete a cycle in the same time;", 12, TEXT))
    parts.append(text(227, 340, "the teal wave peaks a quarter-cycle later.", 12, TEXT))
    # harmonics panel
    parts.append(text(672, 50, "Harmonics: whole-number multiples", 14, AMBER_LIGHT, weight="bold"))
    for k, (cyc, lab, col, y) in enumerate([(1, "fundamental: 2 kHz", AMBER, 120), (2, "2nd harmonic: 4 kHz", RED, 205), (3, "3rd harmonic: 6 kHz", PURPLE, 290)]):
        parts.append(f'<line x1="490" y1="{y}" x2="855" y2="{y}" stroke="#3a4250" stroke-width="1"/>')
        parts.append(wave(490, y, 365, 30, cyc * 1.5, 0, col, 2.5))
        parts.append(text(855, y - 38, lab, 12, col, "end", weight="bold"))
    parts.append(text(672, 345, "A transmitter on 7.1 MHz can leak 14.2, 21.3 MHz...", 12, TEXT))
    return svg(w, h, "\n".join(parts), "Two panels. Phase: two sine waves of the same frequency, one shifted a quarter-cycle, 90 degrees, after the other; both complete a cycle in the same time. Harmonics: a 2 kilohertz fundamental, a 4 kilohertz second harmonic and a 6 kilohertz third harmonic, whole-number multiples of the fundamental; a transmitter on 7.1 megahertz can leak energy at 14.2 and 21.3 megahertz.")


FIGURES = {"wave_fields.svg": wave_fields, "spectrum.svg": spectrum, "wavelength_bars.svg": wavelength_bars,
           "phase_harmonics.svg": phase_harmonics}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
