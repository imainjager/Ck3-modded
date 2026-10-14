"""Update 8: draws the small pieces of art that the new systems look for, with Pillow. Original, procedural, uncompressed ARGB .dds files.
  gfx/interface/icons/activities/activity_eir_<k>.dds (80), ..._header.dds (164)
  gfx/interface/illustrations/activities/activity_eir_<k>.dds (796 x 424 scene)
  gfx/interface/icons/activity_phases/eir_<k>_phase.dds (140)
  gfx/interface/icons/activity_option_categories/eir_<k>_scale.dds, eir_<k>_focus.dds (96 x 120)
  gfx/interface/icons/court_position_types/eir_*_court_position.dds (70)
Run: python tools/make_icons.py   (needs Pillow; the files are committed, so this only has to be re-run to change the art)"""
import math
import os
import sys
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(__file__))
from eir_lib import ROOT

GREEN = (24, 66, 40, 255)
GOLD = (222, 184, 82, 255)
CREAM = (240, 230, 200, 255)
DARK = (14, 30, 22, 255)

ACTS = ["oenach", "festival", "feis", "pilgrimage", "hosting", "bardic"]
KIND = {"oenach": "tents", "festival": "fire", "feis": "hall", "pilgrimage": "mountain", "hosting": "spears", "bardic": "harp"}
COURT = {"eir_ollamh": "harp", "eir_brehon": "scales", "eir_druid": "oak", "eir_foster_father": "pair"}


def glyph(d, kind, cx, cy, r, col=CREAM):
    w = max(2, int(r * 0.12))
    if kind == "tents":
        for dx, s in ((-0.55, 0.7), (0.0, 1.0), (0.55, 0.7)):
            x, h = cx + dx * r, r * 0.9 * s
            d.polygon([(x - r * 0.45 * s, cy + r * 0.6), (x + r * 0.45 * s, cy + r * 0.6), (x, cy + r * 0.6 - h)], fill=col)
        d.line([(cx, cy - r * 0.5), (cx, cy - r * 1.0)], fill=GOLD, width=w)
        d.polygon([(cx, cy - r * 1.0), (cx + r * 0.4, cy - r * 0.85), (cx, cy - r * 0.7)], fill=GOLD)
    elif kind == "fire":
        d.polygon([(cx, cy - r), (cx + r * 0.55, cy + r * 0.2), (cx + r * 0.3, cy + r * 0.8), (cx - r * 0.3, cy + r * 0.8), (cx - r * 0.55, cy + r * 0.2)], fill=(236, 120, 40, 255))
        d.polygon([(cx, cy - r * 0.45), (cx + r * 0.28, cy + r * 0.25), (cx + r * 0.15, cy + r * 0.8), (cx - r * 0.15, cy + r * 0.8), (cx - r * 0.28, cy + r * 0.25)], fill=(250, 210, 90, 255))
        d.line([(cx - r * 0.7, cy + r * 0.9), (cx + r * 0.7, cy + r * 0.9)], fill=col, width=w)
    elif kind == "hall":
        d.polygon([(cx - r * 0.9, cy), (cx, cy - r * 0.9), (cx + r * 0.9, cy)], fill=col)
        d.rectangle([cx - r * 0.7, cy, cx + r * 0.7, cy + r * 0.8], fill=col)
        d.rectangle([cx - r * 0.18, cy + r * 0.25, cx + r * 0.18, cy + r * 0.8], fill=DARK)
        d.polygon([(cx - r * 0.35, cy - r * 1.05), (cx - r * 0.2, cy - r * 1.35), (cx, cy - r * 1.1), (cx + r * 0.2, cy - r * 1.35), (cx + r * 0.35, cy - r * 1.05)], fill=GOLD)
    elif kind == "mountain":
        d.polygon([(cx - r, cy + r * 0.8), (cx - r * 0.15, cy - r * 0.8), (cx + r * 0.3, cy - r * 0.1), (cx + r * 0.55, cy - r * 0.45), (cx + r, cy + r * 0.8)], fill=col)
        d.line([(cx - r * 0.15, cy - r * 0.8), (cx - r * 0.15, cy - r * 1.2)], fill=GOLD, width=w)
        d.line([(cx - r * 0.3, cy - r * 1.05), (cx, cy - r * 1.05)], fill=GOLD, width=w)
    elif kind == "spears":
        for dx in (-0.5, 0.0, 0.5):
            x = cx + dx * r
            d.line([(x, cy + r * 0.9), (x, cy - r * 0.7)], fill=col, width=w)
            d.polygon([(x - r * 0.12, cy - r * 0.7), (x + r * 0.12, cy - r * 0.7), (x, cy - r * 1.05)], fill=GOLD)
        d.arc([cx - r * 0.9, cy - r * 0.1, cx + r * 0.9, cy + r * 1.1], 200, 340, fill=col, width=w)
    elif kind == "harp":
        d.arc([cx - r * 0.9, cy - r * 0.9, cx + r * 0.3, cy + r * 0.9], 270, 90, fill=col, width=w + 1)
        d.line([(cx - r * 0.3, cy - r * 0.9), (cx + r * 0.5, cy + r * 0.8)], fill=col, width=w + 1)
        for i in range(5):
            t = i / 4
            d.line([(cx - r * 0.35 + t * r * 0.6, cy - r * 0.7 + t * r * 1.3), (cx - r * 0.05 + t * r * 0.45, cy - r * 0.75 + t * r * 1.55)], fill=GOLD, width=1)
    elif kind == "scales":
        d.line([(cx, cy - r * 0.9), (cx, cy + r * 0.8)], fill=col, width=w)
        d.line([(cx - r * 0.8, cy - r * 0.55), (cx + r * 0.8, cy - r * 0.55)], fill=col, width=w)
        for sx in (-0.8, 0.8):
            d.line([(cx + sx * r, cy - r * 0.55), (cx + sx * r, cy)], fill=col, width=1)
            d.pieslice([cx + sx * r - r * 0.4, cy - r * 0.2, cx + sx * r + r * 0.4, cy + r * 0.45], 0, 180, fill=GOLD)
        d.rectangle([cx - r * 0.35, cy + r * 0.75, cx + r * 0.35, cy + r * 0.9], fill=col)
    elif kind == "oak":
        d.rectangle([cx - r * 0.12, cy, cx + r * 0.12, cy + r * 0.9], fill=(120, 90, 50, 255))
        for dx, dy, rr in ((-0.4, -0.2, 0.5), (0.4, -0.2, 0.5), (0.0, -0.55, 0.55), (0.0, 0.0, 0.5)):
            d.ellipse([cx + dx * r - rr * r, cy + dy * r - rr * r, cx + dx * r + rr * r, cy + dy * r + rr * r], fill=(70, 150, 70, 255))
    elif kind == "pair":
        for dx in (-0.45, 0.45):
            d.ellipse([cx + dx * r - r * 0.28, cy - r * 0.7, cx + dx * r + r * 0.28, cy - r * 0.15], fill=col)
            d.polygon([(cx + dx * r - r * 0.4, cy + r * 0.85), (cx + dx * r + r * 0.4, cy + r * 0.85), (cx + dx * r, cy - r * 0.05)], fill=col)
    elif kind == "coins":
        for i, dy in enumerate((0.55, 0.15, -0.25)):
            d.ellipse([cx - r * 0.6, cy + dy * r - r * 0.25, cx + r * 0.6, cy + dy * r + r * 0.25], fill=GOLD, outline=DARK)
    elif kind == "star":
        pts = []
        for i in range(10):
            a = -math.pi / 2 + i * math.pi / 5
            rr = r if i % 2 == 0 else r * 0.45
            pts.append((cx + math.cos(a) * rr, cy + math.sin(a) * rr))
        d.polygon(pts, fill=GOLD)


def medallion(size, kind, ring=True):
    s = size * 4
    im = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([s * 0.04, s * 0.04, s * 0.96, s * 0.96], fill=GREEN, outline=GOLD, width=max(2, s // 28))
    if ring:
        d.ellipse([s * 0.12, s * 0.12, s * 0.88, s * 0.88], outline=(222, 184, 82, 120), width=max(1, s // 80))
    glyph(d, kind, s / 2, s / 2 + s * 0.03, s * 0.28)
    return im.resize((size, size), Image.LANCZOS)


def tall(w, h, kind):
    s = 4
    im = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([w * s * 0.04, h * s * 0.04, w * s * 0.96, h * s * 0.96], radius=w * s * 0.12, fill=GREEN, outline=GOLD, width=3 * s)
    glyph(d, kind, w * s / 2, h * s / 2, min(w, h) * s * 0.32)
    return im.resize((w, h), Image.LANCZOS)


def scene(w, h, kind, seed):
    im = Image.new("RGBA", (w, h))
    px = im.load()
    for y in range(h):
        t = y / h
        for x in range(w):
            px[x, y] = (int(20 + 90 * t), int(40 + 80 * t), int(60 + 50 * (1 - t)), 255)
    d = ImageDraw.Draw(im, "RGBA")
    d.ellipse([w * 0.72, h * 0.12, w * 0.72 + h * 0.2, h * 0.12 + h * 0.2], fill=(250, 235, 190, 220))
    # hills
    for i, (base, col) in enumerate(((0.62, (34, 74, 50)), (0.72, (24, 58, 38)), (0.84, (16, 42, 28)))):
        pts = [(0, h)]
        for x in range(0, w + 20, 20):
            pts.append((x, h * base + math.sin((x + seed * 40 + i * 90) / 130.0) * h * 0.06 + math.sin(x / 47.0 + i) * h * 0.02))
        pts.append((w, h))
        d.polygon(pts, fill=col + (255,))
    glyph(d, kind, w * 0.5, h * 0.55, h * 0.26, col=CREAM)
    return im.filter(ImageFilter.GaussianBlur(0.6))


def save(im, rel):
    path = os.path.join(ROOT, *rel.split("/"))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    im.convert("RGBA").save(path)


def build():
    n = 0
    for i, k in enumerate(ACTS):
        kind = KIND[k]
        save(medallion(80, kind), "gfx/interface/icons/activities/activity_eir_%s.dds" % k)
        save(medallion(164, kind), "gfx/interface/icons/activities/activity_eir_%s_header.dds" % k)
        save(scene(796, 424, kind, i), "gfx/interface/illustrations/activities/activity_eir_%s.dds" % k)
        save(medallion(140, kind), "gfx/interface/icons/activity_phases/eir_%s_phase.dds" % k)
        save(tall(96, 120, "coins"), "gfx/interface/icons/activity_option_categories/eir_%s_scale.dds" % k)
        save(tall(96, 120, "star"), "gfx/interface/icons/activity_option_categories/eir_%s_focus.dds" % k)
        n += 6
    for key, kind in COURT.items():
        save(medallion(70, kind), "gfx/interface/icons/court_position_types/%s_court_position.dds" % key)
        n += 1
    print("icons written: %d" % n)


if __name__ == "__main__":
    build()
