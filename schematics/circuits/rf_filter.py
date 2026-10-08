"""An RF filter on an audio input: a 1 mH choke in series with the lead and a
10 nF bypass capacitor from the amplifier side to ground. The choke has high
reactance at RF and low at audio; the capacitor the reverse, so RF is blocked
and shunted to ground while audio passes. Used in docs/reactance_and_impedance.md.
"""

import schemdraw.elements as elm

from style import dark_drawing


def build(path):
    with dark_drawing(file=str(path)) as d:
        d.config(margin=0.6)
        d.add(elm.Dot(open=True).label("audio + stray RF in", loc="left"))
        d.add(elm.Line().right(1.0))
        d.add(elm.Inductor2(loops=4).right().label("1 mH RF choke", loc="top"))
        node = d.add(elm.Dot())
        d.add(elm.Line().right(2.5))
        d.add(elm.Dot(open=True).label("to audio amplifier", loc="right"))
        d.add(elm.Capacitor().at(node.center).down().label("10 nF bypass", loc="bottom"))
        d.add(elm.Ground())
