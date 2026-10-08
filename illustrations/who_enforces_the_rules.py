#!/usr/bin/env python3
"""Figures for docs/who_enforces_the_rules.md.

Sources (Radiocommunication Act and Regulations, current to 2026-09-21,
fetched 2026-10-08):
- Act s. 2 ("Minister" means the Minister of Industry), s. 4(1) no operation
  except under a radio authorization, s. 5(1)(a), (d), (j), (l) Minister's
  powers, s. 5(2) suspension or revocation, s. 6(1) Governor in Council
  regulations, s. 8 inspectors (dwelling-houses, warrant, force, assistance,
  obstruction), s. 8.1 seizure, s. 9(1)(a), (b) prohibitions, s. 10(1)
  offences, s. 15.1 and 15.11(2) administrative monetary penalties.
- Regulations s. 2 (amateur radio service definition), s. 38 (48 hours),
  s. 45 (RBR-4 issued by the Minister).

Usage:
    python3 illustrations/who_enforces_the_rules.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "who_enforces_the_rules"
BLUE = "#4299e1"
PURPLE = "#9f7aea"
TEAL = "#38b2ac"


# 1. Where each rule comes from --------------------------------------------------------------------------
def authority():
    w, h = 900, 470
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Every amateur rule traces back to one Act", 17, AMBER_LIGHT, weight="bold"))
    # trunk
    parts += box3d(w / 2 - 150, 150, 300, 50, 45, PURPLE)
    parts.append(text(w / 2, 128, "Radiocommunication Act", 15, "#ffffff", weight="bold"))
    parts.append(text(w / 2, 172, "offences and penalties live here", 12, MUTED, italic=True))
    branches = [(230, "Governor in Council", "(the federal Cabinet), s. 6", BLUE, "Radiocommunication Regulations",
                 ["define the amateur radio service", "who may operate; what may be sent"]),
                (670, "the Minister, through ISED", "s. 5(1)", TEAL, "Standards, certificates, inspectors",
                 ["RBR-4 and RIC-3 (s. 5(1)(d))", "issues certificates; appoints inspectors"])]
    for cx, who, ref, col, product, lines in branches:
        parts.append(f'<path d="M {w / 2} 185 L {w / 2} 215 L {cx} 215 L {cx} 245" fill="none" stroke="{MUTED}" stroke-width="2.5"/>')
        parts.append(text(cx, 262, who, 14, AMBER_LIGHT, weight="bold"))
        parts.append(text(cx, 280, ref, 12, MUTED, italic=True))
        parts += box3d(cx - 140, 360, 280, 45, 40, col)
        parts.append(text(cx, 340, product, 13, "#ffffff", weight="bold"))
        for j, line in enumerate(lines):
            parts.append(text(cx, 392 + j * 22, line, 12, TEXT))
    return svg(w, h, "\n".join(parts), "A tree with the Radiocommunication Act at its root, where offences and penalties live. One branch: the Governor in Council, the federal Cabinet, makes the Radiocommunication Regulations under section 6; they define the amateur radio service, who may operate and what may be sent. The other branch: the Minister, through ISED, under section 5(1), establishes standards such as RBR-4 and RIC-3, issues certificates and appoints inspectors.")


# 2. What an inspector may do ----------------------------------------------------------------------------
def inspector():
    w, h = 900, 440
    parts = [common_defs()]
    cards = [("Most places", GREEN, "enter at a reasonable time",
              ["with reasonable grounds", "to believe something relevant", "is there; examine, copy,", "or remove it (s. 8(1))",
               "seize equipment used to", "break the rules (s. 8.1)"]),
             ("A home", AMBER, "consent, or a warrant",
              ["no entry without the", "occupant's consent, except", "with a warrant from a justice", "of the peace (s. 8(2)-(3))",
               "or when delay would", "endanger life or evidence"]),
             ("Force", RED, "only with a peace officer",
              ["and only when the warrant", "specifically authorizes it", "(s. 8(4))", "",
               "your side: assist, answer,", "don't obstruct or mislead (s. 8(5)-(6))"])]
    for k, (title, col, pl, lines) in enumerate(cards):
        x0 = 15 + k * 295
        cx = x0 + 140
        parts.append(panel(x0, 15, 280, h - 30))
        parts.append(text(cx, 50, title, 16, AMBER_LIGHT, weight="bold"))
        parts += box3d(cx - 50, 140, 100, 35, 55, col)
        parts += pill(cx, 178, pl, col, size=12, h=28, wpx=230)
        for j, line in enumerate(lines):
            parts.append(text(cx, 228 + j * 26, line, 12, MUTED if line.startswith("(") else TEXT,
                              italic=line.startswith("(")))
    return svg(w, h, "\n".join(parts), "Three panels on an inspector's powers under the Radiocommunication Act. Most places: an inspector may enter at a reasonable time with reasonable grounds to believe something relevant is there, examine, copy or remove it, under section 8(1), and seize equipment used to break the rules, under section 8.1. A home: no entry without the occupant's consent, except with a warrant from a justice of the peace, under sections 8(2) and 8(3), or when delay would endanger life or evidence. Force: only with a peace officer, and only when the warrant specifically authorizes it, under section 8(4). The person in charge must assist and answer reasonable requests, and must not obstruct or mislead the inspector.")


# 3. Suspension ------------------------------------------------------------------------------------------
def suspension():
    w, h = 900, 420
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Three ways the Minister may suspend or revoke a certificate (Act s. 5(2))", 16, AMBER_LIGHT, weight="bold"))
    routes = [(170, "With your consent", GREEN, ["you agree to it"], "nothing more needed"),
              (450, "After notice and a reply", AMBER, ["you broke the Act, the", "Regulations, or the", "certificate's conditions,",
                                                        "or you got it by", "misrepresentation"], "written notice + a chance to respond"),
              (730, "On notice alone", RED, ["you didn't pay fees", "or interest owed"], "written notice only")]
    for cx, title, col, lines, how in routes:
        parts += box3d(cx - 55, 150, 110, 40, 55, col)
        parts.append(text(cx, 185, title, 14, TEXT, weight="bold"))
        for j, line in enumerate(lines):
            parts.append(text(cx, 215 + j * 22, line, 12, TEXT))
        parts += pill(cx, 350, how, shade(col, -0.35), size=11, h=28, wpx=250)
    parts.append(text(w / 2, 394, "Never with no notice at all.", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Three routes to suspension or revocation under section 5(2) of the Radiocommunication Act. With the holder's consent. After written notice and a reasonable opportunity to make representations, where the holder broke the Act, the Regulations or the certificate's conditions, or obtained it by misrepresentation. On written notice alone, with no opportunity to make representations, where the holder failed to pay fees or interest owed. Never with no notice at all.")


# 4. Two kinds of penalty ----------------------------------------------------------------------------------
def penalties():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Two routes to a penalty, for an individual", 17, AMBER_LIGHT, weight="bold"))
    base, scale = 320, 0.0042
    bars = [(150, 5000, "$5,000", AMBER, "+ up to a year in prison"),
            (420, 25000, "$25,000", BLUE, "first violation"),
            (600, 50000, "$50,000", BLUE, "each later one")]
    for x, amt, lab, col, sub in bars:
        hh = amt * scale
        parts += box3d(x, base, 100, 40, hh, col)
        parts.append(text(x + 65, base - hh - 26, lab, 17, TEXT, weight="bold"))
        parts.append(text(x + 50, base + 26, sub, 12, TEXT))
    parts.append(text(200, 380, "Prosecution (s. 10(1)): a court, a conviction", 13, AMBER_LIGHT, weight="bold"))
    parts.append(text(200, 400, "e.g. unlicensed operation, interference, false distress", 11, MUTED, italic=True))
    parts.append(text(585, 380, "Administrative penalty (s. 15.1): no court", 13, BLUE, weight="bold"))
    parts.append(text(585, 400, "e.g. operating outside your authorization (s. 4(1)); \"to promote compliance\"", 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Two routes to a penalty for an individual under the Radiocommunication Act. Prosecution under section 10(1), through a court, for offences such as operating without authorization, interference or a false distress call: a fine up to 5,000 dollars, up to a year in prison, or both. Administrative monetary penalty under section 15.1, with no court, for violations such as operating outside your authorization under section 4(1): up to 25,000 dollars for a first violation and 50,000 dollars for each later one; its stated purpose is to promote compliance, not to punish.")


FIGURES = {"authority.svg": authority, "inspector.svg": inspector, "suspension.svg": suspension,
           "penalties.svg": penalties}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
