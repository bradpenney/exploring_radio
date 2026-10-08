#!/usr/bin/env python3
"""Figures for docs/what_you_may_say.md.

Sources (fetched 2026-10-08):
- Radiocommunication Regulations (SOR/96-484, current to 2026-09-21):
  s. 46 participation under supervision; s. 47 communications limits (amateur
  stations only; no secret code or cipher; no music, commercially recorded
  material, broadcast programming, or business communications); s. 48
  emergency communications; s. 49 no remuneration.
- Radiocommunication Act (current to 2026-09-21): s. 9(1)(a) false distress,
  9(1)(b) interference, 9(2) intercept and divulge; s. 9.1 penalty up to
  $25,000 and/or one year (individual); s. 10(1) up to $5,000 and/or one year.
- RBR-4 Issue 3 section 8 and Schedule I Column III "*" (430-450 MHz,
  902-928 MHz: no interference to, no protection from, other services).
- ITU Radio Regulations No. 4.9 (station in distress may use any means).

Usage:
    python3 illustrations/what_you_may_say.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import (AMBER, AMBER_LIGHT, GREEN, MUTED, RED, TEXT, box3d,  # noqa: E402
                     common_defs, panel, pill, render_all, shade, svg, text)

OUT = HERE.parent / "docs" / "images" / "what_you_may_say"
BLUE = "#4299e1"


# 1. What's allowed on the air -----------------------------------------------------------------------
def allowed():
    w, h = 900, 440
    parts = [common_defs(), panel(15, 15, 425, h - 30), panel(460, 15, 425, h - 30)]
    cols = [(227, "Allowed", GREEN, ["talking with other amateur stations", "codes that aren't secret (Q-codes,",
                                     "  abbreviations, published digital modes)", "technical experiments and tests",
                                     "messages about a real or simulated", "  emergency, for people or relief agencies"]),
            (672, "Not allowed (Regulations s. 47, 49)", RED, ["music, or commercially recorded material",
                                                                "programming from a broadcaster",
                                                                "business or professional traffic",
                                                                "secret codes or ciphers",
                                                                "broadcasting to the general public",
                                                                "payment of any kind"])]
    for cx, title, col, lines in cols:
        parts.append(text(cx, 52, title, 16, shade(col, 0.2), weight="bold"))
        parts += box3d(cx - 170, 395, 340, 30, 300, shade(col, -0.55), shadow=True)
        for k, line in enumerate(lines):
            y = 130 + k * 42
            if not line.startswith("  "):
                parts.append(f'<circle cx="{cx - 145}" cy="{y - 5}" r="7" fill="{col}"/>')
            parts.append(text(cx - 128, y, line.strip(), 13, TEXT, "start"))
    return svg(w, h, "\n".join(parts), "Two panels. Allowed: talking with other amateur stations; codes that aren't secret, such as Q-codes, abbreviations and published digital modes; technical experiments and tests; and messages about a real or simulated emergency on behalf of people or relief agencies. Not allowed, under sections 47 and 49 of the Radiocommunication Regulations: music or commercially recorded material, programming from a broadcaster, business or professional traffic, secret codes or ciphers, broadcasting to the general public, and payment of any kind.")


# 2. Who may transmit ----------------------------------------------------------------------------------
def who_transmits():
    w, h = 900, 400
    parts = [common_defs()]
    cases = [("Certificate holder", "at the controls", True, "transmits within their own privileges"),
             ("Guest with a holder present", "the holder supervises", True, "Regulations s. 46: in the holder's presence"),
             ("Guest alone", "no holder present", False, "not allowed, even on the holder's radio")]
    for k, (title, sub, ok, note) in enumerate(cases):
        x0 = 15 + k * 295
        cx = x0 + 140
        col = GREEN if ok else RED
        parts.append(panel(x0, 15, 280, h - 30))
        parts.append(text(cx, 50, title, 14, AMBER_LIGHT, weight="bold"))
        parts.append(text(cx, 70, sub, 12, MUTED, italic=True))
        parts += box3d(cx - 60, 250, 120, 40, 60, "#4a5568")
        parts.append(text(cx, 222, "station", 12, "#ffffff", weight="bold"))
        figs = [(-40, "holder", BLUE)] if k == 0 else ([(-40, "guest", AMBER), (40, "holder", BLUE)] if k == 1 else [(0, "guest", AMBER)])
        for dx, lab, fc in figs:
            fx = cx + dx
            parts.append(f'<circle cx="{fx}" cy="98" r="13" fill="{fc}"/>')
            parts.append(f'<rect x="{fx - 13}" y="115" width="26" height="32" rx="10" fill="{fc}"/>')
            parts.append(text(fx, 164, lab, 11, TEXT))
        parts += pill(cx, 300, "allowed" if ok else "not allowed", col, size=13, h=30, wpx=130)
        parts.append(text(cx, 345, note, 11, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Three panels. A certificate holder at the controls transmits within their own privileges: allowed. A guest with a certificate holder present and supervising: allowed, under section 46 of the Regulations. A guest alone, with no holder present: not allowed, even on the holder's radio.")


# 3. Sharing bands ----------------------------------------------------------------------------------------
def sharing():
    w, h = 900, 400
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Two kinds of sharing on the amateur bands", 17, AMBER_LIGHT, weight="bold"))
    parts += box3d(90, 300, 300, 50, 160, "#4a5568")
    parts.append(text(240, 170, "another service", 14, "#ffffff", weight="bold"))
    parts.append(text(240, 190, "(primary)", 12, "#ffffff"))
    parts += box3d(110, 300, 260, 30, 50, BLUE, shadow=False)
    parts.append(text(240, 280, "amateur (secondary)", 13, "#ffffff", weight="bold"))
    parts.append(text(240, 340, "e.g. 430–450 MHz, 902–928 MHz (RBR-4 \"*\")", 12, MUTED))
    parts.append(text(240, 360, "must not interfere; not protected", 12, TEXT, weight="bold"))
    for k in range(2):
        parts += box3d(520 + k * 150, 300, 110, 40, 100, BLUE)
        parts.append(text(575 + k * 150, 236, "amateur", 13, "#ffffff", weight="bold"))
    parts.append(text(650, 262, "=", 30, AMBER_LIGHT, weight="bold"))
    parts.append(text(655, 340, "two amateurs on one frequency", 12, MUTED))
    parts.append(text(655, 360, "equal rights: share, don't jam", 12, TEXT, weight="bold"))
    return svg(w, h, "\n".join(parts), "Two kinds of sharing. Left: in bands such as 430 to 450 and 902 to 928 megahertz, marked with an asterisk in RBR-4, the amateur service is secondary to another, primary service: amateurs must not interfere with it and are not protected from it. Right: two amateur stations wanting the same frequency have equal rights, so they share rather than jam.")


# 4. Emergencies ------------------------------------------------------------------------------------------------
def emergencies():
    w, h = 900, 420
    parts = [common_defs()]
    cards = [("Distress", RED, ["a station in distress may use", "any means of radiocommunication", "(ITU Radio Regulations 4.9)",
                                "no power limit; any band;", "anyone may answer"]),
             ("Emergency or disaster", AMBER, ["amateur stations only, carrying", "messages for people, governments,",
                                               "or relief organizations", "(Regulations s. 48)", "real or simulated"]),
             ("Everyone else", BLUE, ["keep the net frequency clear;", "avoid needless transmissions", "on or near it",
                                      "false distress calls are", "an offence (Act s. 9(1)(a))"])]
    for k, (title, col, lines) in enumerate(cards):
        x0 = 15 + k * 295
        cx = x0 + 140
        parts.append(panel(x0, 15, 280, h - 30))
        parts += box3d(cx - 50, 150, 100, 30, 70, col)
        parts.append(text(cx, 50, title, 16, AMBER_LIGHT, weight="bold"))
        for j, line in enumerate(lines):
            parts.append(text(cx, 200 + j * 24, line, 13, TEXT if "(" not in line else MUTED))
    return svg(w, h, "\n".join(parts), "Three panels. Distress: a station in distress may use any means of radiocommunication, under ITU Radio Regulations 4.9, with no power limit, on any band, and anyone may answer. Emergency or disaster: amateur stations only, carrying messages for people, governments or relief organizations, under section 48 of the Regulations, in real or simulated emergencies. Everyone else: keep the net frequency clear and avoid needless transmissions on or near it; false distress calls are an offence under section 9(1)(a) of the Act.")


# 5. Penalties -------------------------------------------------------------------------------------------------
def penalties():
    w, h = 900, 410
    parts = [common_defs(), panel(15, 15, w - 30, h - 30)]
    parts.append(text(w / 2, 48, "Maximum penalties for an individual, Radiocommunication Act", 17, AMBER_LIGHT, weight="bold"))
    rows = [("Interfering, operating without authority,", "or a false distress call (s. 10(1))", 5000, AMBER),
            ("Intercepting and divulging others'", "radiocommunications (s. 9.1)", 25000, RED)]
    base, scale = 300, 0.007
    for k, (l1, l2, fine, col) in enumerate(rows):
        x = 200 + k * 330
        parts += box3d(x, base, 110, 40, fine * scale, col)
        parts.append(text(x + 70, base - fine * scale - 26, f"${fine:,}", 18, TEXT, weight="bold"))
        parts.append(text(x + 55, base + 26, l1, 12, TEXT, weight="bold"))
        parts.append(text(x + 55, base + 44, l2, 12, TEXT, weight="bold"))
    parts.append(text(w / 2, 378, "each: a fine up to this amount, up to a year in prison, or both", 12, MUTED, italic=True))
    return svg(w, h, "\n".join(parts), "Two 3D bars of the maximum penalties for an individual under the Radiocommunication Act. Interfering, operating without authority, or a false distress call, under section 10(1): a fine of up to 5,000 dollars. Intercepting and divulging other people's radiocommunications, under section 9.1: up to 25,000 dollars. Each can also bring up to a year in prison, or both.")


FIGURES = {"allowed.svg": allowed, "who_transmits.svg": who_transmits, "sharing.svg": sharing,
           "emergencies.svg": emergencies, "penalties.svg": penalties}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
