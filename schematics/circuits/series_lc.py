"""A series tuned circuit: an AC source drives a 10 uH inductor and a 50 pF
capacitor in series, resonant near 7.12 MHz. At resonance the two reactances
cancel, the impedance is lowest and the current greatest. Used in
docs/resonance.md.
"""

import schemdraw.elements as elm

from style import dark_drawing


def build(path):
    with dark_drawing(file=str(path)) as d:
        d.config(margin=0.6)
        src = d.add(elm.SourceSin().up().label("AC source", loc="left"))
        d.add(elm.Inductor2(loops=4).right().label("10 µH", loc="top"))
        d.add(elm.Capacitor().down().toy(src.start).label("50 pF", loc="bottom"))
        d.add(elm.Line().left().tox(src.start))
