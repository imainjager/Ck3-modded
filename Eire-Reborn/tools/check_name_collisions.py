"""Lists top-level script objects of the mod whose name does not contain 'eir' (a risk of overriding the base game), and any object that
also exists in the same folder of the base game. Run: python tools/check_name_collisions.py"""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME = r"C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game"
TOP = re.compile(r"^([A-Za-z0-9_\-']+)\s*=\s*\{", re.M)

bad = 0
for fn in glob.glob(os.path.join(ROOT, "common", "**", "*.txt"), recursive=True):
    rel = os.path.relpath(fn, ROOT).replace("\\", "/")
    folder = rel.rsplit("/", 1)[0]
    text = re.sub(r"#[^\n]*", "", open(fn, encoding="utf-8-sig").read())
    names = TOP.findall(text)
    vfiles = glob.glob(os.path.join(GAME, *folder.split("/"), "**", "*.txt"), recursive=True)
    vnames = set()
    for vf in vfiles:
        try:
            vnames.update(TOP.findall(re.sub(r"#[^\n]*", "", open(vf, encoding="utf-8-sig", errors="replace").read())))
        except Exception:
            pass
    for n in set(names):
        if n in vnames:
            print("OVERRIDES base game object: %s in %s" % (n, rel))
            bad += 1
        elif "eir" not in n and not rel.startswith("common/landed_titles") and not rel.startswith("common/coat_of_arms") and not rel.startswith("common/holdings"):
            print("name without 'eir': %s in %s" % (n, rel))
            bad += 1
print("name check: %d concern(s)" % bad)
