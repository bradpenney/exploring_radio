#!/usr/bin/env python3
"""Figures for docs/antennas_and_neighbours.md.

Sources (fetched 2026-10-08):
- CPC-2-0-03 Issue 6 (July 2022), live ISED page: s. 1.1 mandate, s. 4 land-use
  authority, s. 4.2 default public consultation (three times the tower height,
  at least 30 days for written comment, 14-day acknowledgement, 60-day written
  response, 21-day reply), dispute resolution (ISED final decision), s. 6
  exclusions (new systems under 15 m; cumulative increase of no more than 25%;
  temporary systems removed within three months), s. 7 general requirements.
- Health Canada Safety Code 6 (2015), Table 5 reference levels, uncontrolled
  environments: 20-48 MHz 58.07/f^0.25 V/m; 48-300 MHz 22.06 V/m;
  300-6000 MHz 3.142 f^0.3417 V/m (f in MHz).
- EMCAB-2 Issue 1 (June 1994): broadcasting receivers and associated equipment
  125 dBuV/m (1.83 V/m); radio-sensitive equipment 130 dBuV/m (3.16 V/m).

Usage:
    python3 illustrations/antennas_and_neighbours.py
"""

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "antennas_and_neighbours"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"


def node(cx, y, w, label, sub, col):
    parts = box3d(cx - w / 2, y, w, 30, 34, shade(col, -0.3), shadow=False)
    parts.append(text(cx, y - 12, label, 13, "#ffffff", weight="bold"))
    if sub:
        parts.append(text(cx, y + 22, sub, 11, MUTED, italic=True))
    return parts


def arrow(x1, y1, x2, y2, lab=None, lx=None, ly=None):
    parts = [f'<path d="M {x1} {y1} L {x2} {y2}" stroke="{MUTED}" stroke-width="2" marker-end="url(#arr)" fill="none"/>']
    if lab:
        parts.append(text(lx if lx is not None else (x1 + x2) / 2 + 8, ly if ly is not None else (y1 + y2) / 2, lab, 11, AMBER_LIGHT, "start", weight="bold"))
    return parts


ARR = f'<defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{MUTED}"/></marker></defs>'


# 1. Which process applies ------------------------------------------------------------------------------
def siting_process():
    w, h = 900, 520
    parts = [common_defs(), ARR, panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Which consultation does an antenna system need? (CPC-2-0-03)", 16, AMBER_LIGHT, weight="bold"))
    parts += node(450, 110, 360, "Proposed new or modified antenna system", None, PURPLE)
    parts += arrow(360, 125, 200, 180, "excluded (s. 6)", 190, 150)
    parts += arrow(540, 125, 700, 180, "not excluded", 640, 150)
    parts += node(200, 215, 300, "No consultation needed", "new and under 15 m; or a rise of 25% or less; or temporary", GREEN)
    parts += node(700, 215, 300, "Contact the land-use authority", "the municipality or other local authority", BLUE)
    parts += arrow(620, 245, 560, 300, "it has a process", 430, 280)
    parts += arrow(780, 245, 800, 300, "it has none", 805, 280)
    parts += node(540, 335, 250, "Follow its process", "it decides how to consult", BLUE)
    parts += node(790, 335, 170, "ISED default", "see the next figure", TEAL)
    parts += arrow(700, 365, 620, 415, "impasse with a stakeholder", 420, 400)
    parts += node(620, 450, 280, "ISED makes the final decision", "on request, not from the general public", AMBER)
    parts.append(text(200, 290, "Either way, Safety Code 6, EMCAB-2", 12, TEXT))
    parts.append(text(200, 310, "and the other general requirements", 12, TEXT))
    parts.append(text(200, 330, "(s. 7) always apply.", 12, TEXT))
    return svg(w, h, "\n".join(parts), "A decision tree from CPC-2-0-03. A proposed new or modified antenna system is either excluded under section 6 (new and under 15 metres, a cumulative height increase of 25 percent or less, or temporary), in which case no consultation is needed, or it is not, in which case you contact the land-use authority. If the authority has a process, you follow it and it decides how consultation takes place; if it has none, you follow ISED's default process. If a stakeholder other than the general public reaches an impasse with you, ISED makes the final decision. Either way, Safety Code 6, EMCAB-2 and the other general requirements always apply.")


# 2. ISED default process --------------------------------------------------------------------------------
def default_process():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "ISED's default public consultation (CPC-2-0-03 s. 4.2)", 16, AMBER_LIGHT, weight="bold"))
    # ground ellipse = notification radius
    cx, cy = 260, 300
    parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="200" ry="70" fill="{shade(TEAL, -0.6)}" stroke="{TEAL}" stroke-width="2" stroke-dasharray="8 6"/>')
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{cx}" y2="{cy - 170}" stroke="{TEXT}" stroke-width="5"/>')
    parts.append(f'<line x1="{cx - 40}" y1="{cy - 160}" x2="{cx + 40}" y2="{cy - 160}" stroke="{TEXT}" stroke-width="4"/>')
    parts.append(f'<line x1="{cx}" y1="{cy - 120}" x2="{cx - 110}" y2="{cy}" stroke="{MUTED}" stroke-width="1"/>')
    parts.append(f'<line x1="{cx}" y1="{cy - 120}" x2="{cx + 110}" y2="{cy}" stroke="{MUTED}" stroke-width="1"/>')
    parts.append(f'<path d="M {cx} {cy + 8} L {cx + 200} {cy + 8}" stroke="{AMBER_LIGHT}" stroke-width="2"/>')
    parts.append(text(cx + 100, cy + 28, "3 × tower height", 12, AMBER_LIGHT, weight="bold"))
    parts.append(text(cx + 12, cy - 175, "tower height h", 11, MUTED, "start", italic=True))
    for hx, hy in [(cx - 150, cy - 10), (cx + 120, cy - 30), (cx - 60, cy + 40)]:
        parts += box3d(hx, hy, 34, 22, 22, BLUE)
    parts += box3d(cx + 230, cy - 50, 34, 22, 22, "#4a5568")
    parts.append(text(cx + 247, cy - 85, "outside", 11, MUTED, italic=True))
    parts.append(text(cx, 395, "notify everyone inside, by mail or by hand", 12, TEXT))
    steps = [("1", "Notify", "public, land-use authority and ISED;", "at least 30 days for written comments"),
             ("2", "Respond", "acknowledge within 14 days; address", "reasonable and relevant concerns within 60"),
             ("3", "Reply", "the public has 21 days to reply;", "copies go to ISED")]
    for k, (n, t1, l1, l2) in enumerate(steps):
        y = 110 + k * 95
        parts += pill(560, y, n, TEAL, size=14, h=34, wpx=34)
        parts.append(text(590, y + 5, t1, 15, AMBER_LIGHT, "start", weight="bold"))
        parts.append(text(590, y + 28, l1, 12, TEXT, "start"))
        parts.append(text(590, y + 46, l2, 12, TEXT, "start"))
    return svg(w, h, "\n".join(parts), "ISED's default public consultation under section 4.2 of CPC-2-0-03. A tower of height h sits at the centre of a notification circle with a radius of three times the tower height; homes inside are notified by mail or by hand, homes outside are not. Three steps: notify the public, the land-use authority and ISED, allowing at least 30 days for written comments; acknowledge concerns within 14 days and address reasonable and relevant concerns in writing within 60 days; the public then has 21 days to reply, and copies go to ISED.")


# 3. Safety Code 6 reference levels -----------------------------------------------------------------------
def sc6_curve():
    w, h = 900, 460
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Safety Code 6: electric-field reference level, uncontrolled environments", 16, AMBER_LIGHT, weight="bold"))
    L, R, T, B = 110, 850, 90, 360
    fmin, fmax, emax = 20.0, 6000.0, 70.0

    def X(f):
        return L + (math.log10(f) - math.log10(fmin)) / (math.log10(fmax) - math.log10(fmin)) * (R - L)

    def Y(e):
        return B - e / emax * (B - T)

    def E(f):
        if f < 48:
            return 58.07 / f ** 0.25
        if f <= 300:
            return 22.06
        return 3.142 * f ** 0.3417

    parts.append(f'<rect x="{X(48)}" y="{T}" width="{X(300) - X(48)}" height="{B - T}" fill="{shade(RED, -0.75)}"/>')
    parts.append(text((X(48) + X(300)) / 2, T + 18, "48–300 MHz: lowest limit", 12, RED, weight="bold"))
    for e in (0, 20, 40, 60):
        parts.append(f'<line x1="{L}" y1="{Y(e)}" x2="{R}" y2="{Y(e)}" stroke="#3a4250" stroke-width="1"/>')
        parts.append(text(L - 10, Y(e) + 4, f"{e}", 11, MUTED, "end"))
    for f, lab in [(20, "20"), (50, "50"), (100, "100"), (300, "300"), (1000, "1000"), (3000, "3000"), (6000, "6000")]:
        parts.append(text(X(f), B + 20, lab, 11, MUTED))
    parts.append(text((L + R) / 2, B + 42, "frequency (MHz, logarithmic)", 12, MUTED, italic=True))
    parts.append(text(40, (T + B) / 2, "V/m", 12, MUTED, italic=True))
    pts = []
    f = fmin
    while f <= fmax:
        pts.append(f"{X(f):.1f},{Y(E(f)):.1f}")
        f *= 1.03
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{AMBER}" stroke-width="4"/>')
    for fb, lab in [(28.5, "10 m"), (52, "6 m"), (146, "2 m"), (221, "1.25 m"), (440, "70 cm"), (915, "33 cm")]:
        parts.append(f'<circle cx="{X(fb):.1f}" cy="{Y(E(fb)):.1f}" r="6" fill="{BLUE}" stroke="#ffffff" stroke-width="1.5"/>')
        parts.append(text(X(fb), Y(E(fb)) + 26 if lab != "1.25 m" else Y(E(fb)) - 12, lab, 11, TEXT, weight="bold"))
    parts.append(text(w / 2, 432, "Limits are field strengths at the person, whatever the source; no transmitter is exempt.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "A graph of the Safety Code 6 electric-field reference level for uncontrolled environments, from 20 megahertz to 6 gigahertz on a logarithmic scale. The limit falls from about 27 volts per metre at 20 megahertz to a flat minimum of 22.06 volts per metre from 48 to 300 megahertz, highlighted as the lowest limit, then rises to about 61 volts per metre at 6 gigahertz. Amateur bands are marked: 10 metres, 6 metres, 2 metres, 1.25 metres, 70 centimetres and 33 centimetres; 6, 2 and 1.25 metres fall in the lowest-limit range. Limits are field strengths at the person, whatever the source, and no transmitter is exempt.")


# 4. EMCAB-2 -----------------------------------------------------------------------------------------------
def emcab2():
    w, h = 900, 470
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Whose problem is it? EMCAB-2's field-strength test", 16, AMBER_LIGHT, weight="bold"))
    base, scale = 310, 42
    bars = [(140, 1.83, "125 dBµV/m", "Broadcasting receivers", "TV and radio receivers", BLUE),
            (390, 1.83, "125 dBµV/m", "Associated equipment", "amplifiers, CD players, recorders", PURPLE),
            (640, 3.16, "130 dBµV/m", "Radio-sensitive equipment", "other non-radio electronics", TEAL)]
    for x, v, db, t1, t2, col in bars:
        parts += box3d(x, base, 120, 40, v * scale, col)
        parts.append(text(x + 70, base - v * scale - 40, f"{v} V/m", 17, TEXT, weight="bold"))
        parts.append(text(x + 70, base - v * scale - 20, db, 11, MUTED))
        parts.append(text(x + 60, base + 28, t1, 13, AMBER_LIGHT, weight="bold"))
        parts.append(text(x + 60, base + 46, t2, 11, MUTED, italic=True))
    parts.append(text(w / 2, 385, "Measured on the premises of the affected equipment:", 12, TEXT))
    parts += pill(270, 420, "above the criterion: your transmission is the cause", RED, size=12, h=30, wpx=380)
    parts += pill(660, 420, "below it: the equipment's lack of immunity", GREEN, size=12, h=30, wpx=340)
    return svg(w, h, "\n".join(parts), "EMCAB-2's field-strength criteria. Broadcasting receivers such as TV and radio receivers: 125 dB microvolts per metre, 1.83 volts per metre. Associated equipment such as amplifiers, CD players and recorders: also 1.83 volts per metre. Radio-sensitive equipment, other non-radio electronics: 130 dB microvolts per metre, 3.16 volts per metre. Measured on the premises of the affected equipment: above the criterion, your transmission is deemed the cause; below it, the equipment's lack of immunity is.")


FIGURES = {"siting_process.svg": siting_process, "default_process.svg": default_process,
           "sc6_curve.svg": sc6_curve, "emcab2.svg": emcab2}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
