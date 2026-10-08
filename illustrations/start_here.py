#!/usr/bin/env python3
"""Figure for docs/start_here.md: the path from electricity to radio drawn as a
transit map. Three Exploring Electronics lines (foundations, AC and fields,
components) meet at the Radio Fundamentals interchange, and the radio line runs
on from there.

Every written stop is a link, so the SVG is inlined into the page with
pymdownx.snippets rather than placed as an <img> (links inside an <img> are
dead). That's also why every id here carries the "tm-" prefix: it shares the
page's id namespace.

Usage:
    python3 illustrations/start_here.py
"""

import sys
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from style3d import FONT, MUTED, TEXT, render_all, shade, text  # noqa: E402

OUT = HERE.parent / "docs" / "images" / "start_here"
E = "https://electronics.bradpenney.io/"

# (key, colour, label, site)
LINES = {
    "dc": ("#f59e0b", "Foundations line", "Exploring Electronics"),
    "ac": ("#9f7aea", "AC and fields line", "Exploring Electronics"),
    "parts": ("#48bb78", "Components line", "Exploring Electronics"),
    "radio": ("#4299e1", "Radio line", "Exploring Radio"),
}

# (number, label lines, url or None, x, y, label side)
STOPS = {
    "dc": [
        (1, ["Conductors"], E + "conductors_and_insulators/", 60, 130, "up"),
        (2, ["Prefixes"], E + "metric_prefixes/", 170, 130, "up"),
        (3, ["Voltage"], E + "voltage/", 280, 130, "up"),
        (4, ["Current"], E + "current/", 390, 130, "up"),
        (5, ["Resistance"], E + "resistance/", 500, 130, "up"),
        (6, ["Ohm's Law"], E + "ohms_law/", 610, 130, "up"),
        (7, ["Fuses"], E + "open_short_fuses/", 720, 130, "up"),
        (8, ["Series &", "Parallel"], E + "series_and_parallel/", 830, 130, "up"),
        (9, ["Batteries"], E + "batteries/", 940, 130, "up"),
    ],
    "ac": [
        (10, ["AC vs DC"], E + "ac_dc/", 520, 260, "down"),
        (11, ["Magnetism"], E + "magnetism/", 400, 260, "down"),
        (12, ["Capacitors"], E + "capacitors/", 280, 260, "down"),
        (13, ["Inductors"], E + "inductors/", 160, 260, "down"),
    ],
    "parts": [
        (14, ["Resistor Types"], E + "resistor_types/", 830, 210, "right"),
        (15, ["Diodes & LEDs"], E + "diodes_and_leds/", 830, 262, "right"),
        (16, ["Transistors"], E + "transistors/", 830, 314, "right"),
        (17, ["Vacuum Tubes"], E + "vacuum_tubes/", 830, 366, "right"),
        (18, ["Regulators"], E + "voltage_regulators/", 830, 418, "right"),
    ],
    "radio": [
        (None, ["Antennas &", "Feedlines"], None, 620, 580, "down"),
        (None, ["Propagation"], None, 760, 580, "down"),
        (None, ["On the Air"], "../amateurs_code/", 900, 580, "down"),
    ],
}

# Track geometry: each line's path, drawn before the stops.
TRACKS = {
    "dc": "M60,130 L940,130",
    "ac": "M610,130 L610,240 Q610,260 590,260 L100,260 Q80,260 80,280 L80,450 Q80,470 100,470 L400,470",
    "parts": "M830,130 L830,450 Q830,470 810,470 L600,470",
    "radio": "M500,490 L500,560 Q500,580 520,580 L900,580",
}
HUB = (500, 470)

STYLE = (
    "<style>"
    ".tm-stop .tm-ring{stroke:#1a202c;stroke-width:3;transition:stroke .15s}"
    ".tm-stop:hover .tm-ring,.tm-stop:focus-visible .tm-ring{stroke:#ffffff;stroke-width:4}"
    ".tm-stop:hover .tm-lbl,.tm-stop:focus-visible .tm-lbl{fill:#ffffff;text-decoration:underline}"
    ".tm-stop:focus{outline:none}"
    "</style>"
)


def defs():
    out = [STYLE, "<defs>",
           '<linearGradient id="tm-panel" x1="0" y1="0" x2="0" y2="1">'
           '<stop offset="0" stop-color="#2d3748" stop-opacity="0.45"/>'
           '<stop offset="1" stop-color="#1a202c" stop-opacity="0.15"/></linearGradient>',
           '<linearGradient id="tm-gloss" x1="0" y1="0" x2="0" y2="1">'
           '<stop offset="0" stop-color="#ffffff" stop-opacity="0.45"/>'
           '<stop offset="0.45" stop-color="#ffffff" stop-opacity="0.05"/>'
           '<stop offset="0.55" stop-color="#000000" stop-opacity="0"/>'
           '<stop offset="1" stop-color="#000000" stop-opacity="0.35"/></linearGradient>']
    for key, (color, _, _) in LINES.items():
        out.append(f'<radialGradient id="tm-ball-{key}" cx="35%" cy="32%" r="70%">'
                   f'<stop offset="0" stop-color="{shade(color, 0.6)}"/>'
                   f'<stop offset="0.45" stop-color="{color}"/>'
                   f'<stop offset="1" stop-color="{shade(color, -0.55)}"/></radialGradient>')
    out.append("</defs>")
    return out


def track(d, color):
    """A line drawn as a raised tube: drop shadow, body, highlight."""
    return [f'<path d="{d}" fill="none" stroke="#000000" stroke-opacity="0.45" stroke-width="12" '
            f'stroke-linecap="round" stroke-linejoin="round" transform="translate(2,4)"/>',
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>',
            f'<path d="{d}" fill="none" stroke="{shade(color, 0.5)}" stroke-opacity="0.55" stroke-width="3" '
            f'stroke-linecap="round" stroke-linejoin="round" transform="translate(-1,-2)"/>']


def label(x, y, lines, side, fill):
    size, lh = 15, 18
    if side == "up":
        ys = [y - 26 - lh * (len(lines) - 1 - i) for i in range(len(lines))]
        return [_lbl(x, yy, s, size, fill, "middle") for s, yy in zip(lines, ys)]
    if side == "down":
        return [_lbl(x, y + 36 + lh * i, s, size, fill, "middle") for i, s in enumerate(lines)]
    return [_lbl(x + 24, y + 5 + lh * i, s, size, fill, "start") for i, s in enumerate(lines)]


def _lbl(x, y, s, size, fill, anchor):
    return (f'<text class="tm-lbl" x="{x}" y="{y}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="bold">{escape(s)}</text>')


def stop(key, num, lines, url, x, y, side):
    color, _, site = LINES[key]
    name = " ".join(lines)
    if url is None:
        # Not written yet: an open ring, no link.
        return ([f'<circle cx="{x}" cy="{y}" r="11" fill="#1a202c" stroke="{color}" stroke-width="4"/>']
                + label(x, y, lines, side, MUTED))
    fg = "#ffffff" if key == "ac" else "#1a1a1a"
    aria = f"{num}. {name}, on {site}" if num else f"{name}, on {site}"
    parts = [f'<a class="tm-stop" href={quoteattr(url)} aria-label={quoteattr(aria)}>',
             f"<title>{escape(aria)}</title>",
             f'<circle cx="{x + 2}" cy="{y + 4}" r="15" fill="#000000" fill-opacity="0.4"/>',
             f'<circle class="tm-ring" cx="{x}" cy="{y}" r="15" fill="url(#tm-ball-{key})"/>']
    if num:
        parts.append(f'<text x="{x}" y="{y + 5}" font-size="13" fill="{fg}" text-anchor="middle" '
                     f'font-weight="bold">{num}</text>')
    parts += label(x, y, lines, side, TEXT)
    parts.append("</a>")
    return parts


def hub():
    x, y = HUB
    w, h = 200, 44
    color = LINES["radio"][0]
    return [f'<rect x="{x - w / 2 + 3}" y="{y - h / 2 + 5}" width="{w}" height="{h}" rx="22" fill="#000000" fill-opacity="0.4"/>',
            f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="22" fill="#1a202c" '
            f'stroke="{color}" stroke-width="4"/>',
            f'<rect x="{x - w / 2}" y="{y - h / 2}" width="{w}" height="{h}" rx="22" fill="url(#tm-gloss)" opacity="0.5"/>',
            text(x, y - 2, "Radio Fundamentals", 15, "#90cdf4", weight="bold"),
            text(x, y + 14, "decibels, reactance, resonance", 11, MUTED, italic=True)]


def legend():
    x, y = 40, 520
    out = [text(x, y, "Exploring Electronics", 13, MUTED, anchor="start", weight="bold")]
    rows = [("dc", y + 22), ("ac", y + 44), ("parts", y + 66)]
    for key, yy in rows:
        color, name, _ = LINES[key]
        out.append(f'<line x1="{x}" y1="{yy - 5}" x2="{x + 34}" y2="{yy - 5}" stroke="{color}" stroke-width="8" stroke-linecap="round"/>')
        out.append(text(x + 46, yy, name, 13, TEXT, anchor="start"))
    out.append(text(x, y + 94, "Exploring Radio", 13, MUTED, anchor="start", weight="bold"))
    out.append(f'<circle cx="{x + 17}" cy="{y + 111}" r="7" fill="#1a202c" stroke="{LINES["radio"][0]}" stroke-width="3"/>')
    out.append(text(x + 46, y + 116, "open stop: still being written", 13, TEXT, anchor="start"))
    return out


def transit_map():
    w, h = 1000, 670
    desc = ("A transit map of the path from electricity to radio. The amber Foundations line on Exploring "
            "Electronics runs through stops 1 to 9: conductors, prefixes, voltage, current, resistance, Ohm's law, "
            "fuses, series and parallel, and batteries. At Ohm's law the purple AC and fields line branches off "
            "through stops 10 to 13: AC vs DC, magnetism, capacitors, and inductors. At series and parallel the "
            "green Components line branches off through stops 14 to 18: resistor types, diodes and LEDs, "
            "transistors, vacuum tubes, and voltage regulators. The purple and green lines meet at the Radio Fundamentals interchange, where the blue "
            "Radio line on this site begins, running on to antennas and feedlines, propagation, and on the air. "
            "Every written stop is a link to its article.")
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
             f'style="max-width:100%;height:auto" role="group" aria-labelledby="tm-title tm-desc" '
             f'font-family="{FONT}">',
             '<title id="tm-title">The path from electricity to radio, as a transit map</title>',
             f'<desc id="tm-desc">{escape(desc)}</desc>']
    parts += defs()
    parts.append(f'<rect x="15" y="15" width="{w - 30}" height="{h - 30}" rx="14" fill="url(#tm-panel)" '
                 f'stroke="#4a5568" stroke-opacity="0.6"/>')
    parts.append(text(w / 2, 52, "Click any stop to open its article", 13, MUTED, italic=True))
    for key in ("ac", "parts", "radio", "dc"):
        parts += track(TRACKS[key], LINES[key][0])
    parts += hub()
    for key, stops in STOPS.items():
        for s in stops:
            parts += stop(key, *s)
    parts += legend()
    parts.append("</svg>")
    # One element per line and no blank lines, so Markdown keeps it a single raw HTML block.
    return "\n".join(parts) + "\n"


FIGURES = {"transit_map.svg": transit_map}

if __name__ == "__main__":
    render_all(FIGURES, OUT)
