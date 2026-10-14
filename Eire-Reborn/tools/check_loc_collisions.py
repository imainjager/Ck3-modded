"""Finds localization keys that the mod defines twice, or that also exist in the base game (which would override the game's own text).
Run: python tools/check_loc_collisions.py"""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME = r"C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game"
KEY = re.compile(r'^ ([A-Za-z0-9_.\-]+):\d* "', re.M)

mine, dup = {}, []
for fn in sorted(glob.glob(os.path.join(ROOT, "localization", "english", "*.yml"))):
    for k in KEY.findall(open(fn, encoding="utf-8-sig").read()):
        if k in mine and mine[k] != os.path.basename(fn):
            dup.append((k, mine[k], os.path.basename(fn)))
        mine.setdefault(k, os.path.basename(fn))
vanilla = set()
for fn in glob.glob(os.path.join(GAME, "localization", "english", "**", "*.yml"), recursive=True):
    try:
        vanilla.update(KEY.findall(open(fn, encoding="utf-8-sig", errors="replace").read()))
    except Exception:
        pass
clash = sorted(k for k in mine if k in vanilla)
for k, a, b in dup:
    print("DUPLICATE in the mod: %s (%s and %s)" % (k, a, b))
for k in clash[:60]:
    print("OVERRIDES the base game: %s (%s)" % (k, mine[k]))
print("mod keys: %d, duplicates: %d, clashes with the base game: %d" % (len(mine), len(dup), len(clash)))
sys.exit(1 if dup or clash else 0)
