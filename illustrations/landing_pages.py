#!/usr/bin/env python3
"""Clickable transit maps for the radio topic landing pages. Stops mirror each
landing page's list: keep them in sync when an article is added. Hrefs are
built URLs relative to the landing page, because inlined HTML isn't rewritten
by MkDocs; htmlproofer checks them.

Usage:
    python3 illustrations/landing_pages.py
"""

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from transit import transit_map  # noqa: E402
from style3d import render_all  # noqa: E402

OUT = HERE.parent / "docs" / "images" / "landing"
AMBER, BLUE = "#f59e0b", "#4299e1"

LICENSED = [
    ("The certificate", AMBER, [
        (["Getting Your", "Certificate"], "../getting_your_certificate/")]),
    ("Using it", BLUE, [
        (["What You May", "Transmit"], "../what_you_may_transmit/"),
        (["What You May", "Say"], "../what_you_may_say/"),
        (["Across", "Borders"], "../across_borders/"),
        (["Who Enforces", "the Rules"], "../who_enforces_the_rules/"),
        (["Antennas and", "Neighbours"], "../antennas_and_neighbours/")]),
]


FUNDAMENTALS = [
    ("Describing a signal", BLUE, [
        (["What Is a", "Radio Wave?"], "../what_is_a_radio_wave/"),
        (["Decibels"], "../decibels/")]),
    ("Coils and capacitors", AMBER, [
        (["Reactance and", "Impedance"], "../reactance_and_impedance/"),
        (["Resonance"], "../resonance/")]),
]


def getting_licensed():
    stops = "; ".join(f"{name}: " + ", ".join(" ".join(l) for l, _ in s) for name, _, s in LICENSED)
    return transit_map("gl", "Getting Licensed reading order, as a transit map",
                       f"One line through six stops. {stops}. Every stop is a link to its article.", LICENSED, [6])


def radio_fundamentals():
    stops = "; ".join(f"{name}: " + ", ".join(" ".join(l) for l, _ in s) for name, _, s in FUNDAMENTALS)
    return transit_map("rf", "Radio Fundamentals reading order, as a transit map",
                       f"One line through four stops. {stops}. Every stop is a link to its article.", FUNDAMENTALS, [4])


FIGURES = {"getting_licensed.svg": getting_licensed, "radio_fundamentals.svg": radio_fundamentals}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
