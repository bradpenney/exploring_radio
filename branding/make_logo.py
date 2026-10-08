"""Build the Exploring Radio mascot from the networking mascot.

Keeps the robot, the lens ring, and the "EXPLORING" line; replaces the lens
emblem with a lattice tower radiating waves, and "NETWORKING" with "RADIO".
"""
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

SRC = "/home/brad/notes/source_code/exploring_networking/docs/images/exploring_networking.png"
AMBER = (248, 202, 30, 255)
FONT = str(Path(__file__).with_name("Oswald.ttf"))  # OFL, github.com/google/fonts ofl/oswald
S = 4  # supersample factor for the drawn layers

im = Image.open(SRC).convert("RGBA")
W, H = im.size
px = im.load()
CX, CY = 611, 704.5

# 1. lens interior: repaint with the lens's own dark fill
dark = px[int(CX + 98), int(CY)]
for x in range(W):
    for y in range(H):
        if math.hypot(x - CX, y - CY) < 102.5:
            px[x, y] = dark

# 2. erase the second text line
for x in range(415, W):
    for y in range(392, 490):
        px[x, y] = (0, 0, 0, 0)

# 3. emblem, drawn supersampled
big = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
d = ImageDraw.Draw(big)
def P(x, y): return (x * S, y * S)
lw = 10 * S
top = (CX, CY - 40)
bl, br = (CX - 40, CY + 78), (CX + 40, CY + 78)
d.line([P(*bl), P(*top), P(*br)], fill=AMBER, width=lw, joint="curve")
# cross-bracing: horizontal rungs + X's between them
levels = [CY + 2, CY + 40, CY + 78]
def edge(y):
    t = (y - top[1]) / (bl[1] - top[1])
    return CX - 40 * t, CX + 40 * t
prev = None
for y in levels:
    l, r = edge(y)
    d.line([P(l, y), P(r, y)], fill=AMBER, width=int(lw * 0.7))
    if prev is not None:
        pl, pr = edge(prev)
        d.line([P(pl, prev), P(r, y)], fill=AMBER, width=int(lw * 0.55))
        d.line([P(pr, prev), P(l, y)], fill=AMBER, width=int(lw * 0.55))
    prev = y
# radiating element at the tip
tip = (CX, CY - 46)
r0 = 12
d.ellipse([P(tip[0] - r0, tip[1] - r0), P(tip[0] + r0, tip[1] + r0)], fill=AMBER)
# waves: arcs either side of the tip
for i, rad in enumerate((27, 44, 61)):
    box = [P(tip[0] - rad, tip[1] - rad), P(tip[0] + rad, tip[1] + rad)]
    d.arc(box, start=-40, end=40, fill=AMBER, width=int(lw * 0.8))
    d.arc(box, start=140, end=220, fill=AMBER, width=int(lw * 0.8))
emb = big.resize((W, H), Image.LANCZOS)
# clip emblem to the lens interior
mask = Image.new("L", (W, H), 0)
ImageDraw.Draw(mask).ellipse([CX - 100, CY - 100, CX + 100, CY + 100], fill=255)
clipped = Image.new("RGBA", (W, H), (0, 0, 0, 0))
clipped.paste(emb, (0, 0), Image.composite(emb.getchannel("A"), Image.new("L", (W, H), 0), mask))
im = Image.alpha_composite(im, clipped)

# 4. "RADIO", matched to line 1's cap height (305..383 -> 78 px)
font = ImageFont.truetype(FONT, 200 * S)
font.set_variation_by_name("Bold")
cap = font.getbbox("H")
size = int(200 * S * (78 * S) / (cap[3] - cap[1]))
font = ImageFont.truetype(FONT, size)
font.set_variation_by_name("Bold")
txt = Image.new("RGBA", (W * S, H * S), (0, 0, 0, 0))
bb = font.getbbox("RADIO")
ImageDraw.Draw(txt).text((432 * S - bb[0], 401 * S - bb[1]), "RADIO", font=font, fill=AMBER)
im = Image.alpha_composite(im, txt.resize((W, H), Image.LANCZOS))
im.save(str(Path(__file__).with_name("exploring_radio.png")), optimize=True)

# previews
Image.alpha_composite(Image.new("RGBA", (W, H), (26, 32, 44, 255)), im).convert("RGB").resize((800, 800)).save("/dev/null", format="PNG")
Image.alpha_composite(Image.new("RGBA", (W, H), (26, 32, 44, 255)), im).convert("RGB").resize((56, 56), Image.LANCZOS).resize((224, 224), Image.NEAREST).save("/dev/null", format="PNG")
