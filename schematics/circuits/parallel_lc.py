"""A parallel tuned circuit (a tank): a 10 uH inductor and a 50 pF capacitor
side by side across the same two points, resonant near 7.12 MHz. At resonance
its impedance is highest. Used in docs/resonance.md.
"""

import schemdraw.elements as elm

from style import dark_drawing


def build(path):
    with dark_drawing(file=str(path)) as d:
        d.config(margin=0.6)
        d.add(elm.Dot(open=True).label("A", loc="left"))
        d.add(elm.Line().right(1.2))
        top = d.add(elm.Dot())
        d.add(elm.Inductor2(loops=4).down().label("10 µH", loc="bottom"))
        bot = d.add(elm.Dot())
        d.add(elm.Line().left(1.2))
        d.add(elm.Dot(open=True).label("B", loc="left"))
        d.add(elm.Line().at(top.center).right(2.2))
        d.add(elm.Capacitor().down().toy(bot.center).label("50 pF", loc="bottom"))
        d.add(elm.Line().left().tox(bot.center))
