"""Shared helpers for the Eire Reborn generators.

Every generator writes game script plus the localization for it, so the two can never drift apart.
Run `python tools/build_all.py` from the mod folder to regenerate everything.
"""
import io
import os
import re
import glob

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME = r"C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game"


def path(*parts):
    return os.path.join(ROOT, *parts)


def write(rel, text, bom=True):
    full = path(*rel.split("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with io.open(full, "w", encoding="utf-8-sig" if bom else "utf-8", newline="\n") as f:
        f.write(text)


def num(v):
    if isinstance(v, str):
        return v
    s = "%g" % v
    return s


def esc(s):
    """Escape text for a localization value."""
    return s.replace('"', "'").replace("\r", "").replace("\n", "\\n")


class Loc:
    """Collects localization keys for one yml file."""

    def __init__(self, filename):
        self.filename = filename
        self.items = []
        self.keys = set()
        self.sections = []

    def section(self, title):
        self.items.append((None, title))

    def add(self, key, text):
        if key in self.keys:
            raise SystemExit("duplicate loc key: " + key)
        self.keys.add(key)
        self.items.append((key, esc(text)))

    def write(self):
        out = ["l_english:\n"]
        for k, v in self.items:
            if k is None:
                out.append("\n # ---------- %s ----------\n" % v)
            else:
                out.append(' %s:0 "%s"\n' % (k, v))
        write("localization/english/" + self.filename, "".join(out))


# ---------------------------------------------------------------------------
# Validation helpers: build the universe of modifier-field names the game knows.
# ---------------------------------------------------------------------------
_KEY_RE = re.compile(r"^\s+([a-z][a-z0-9_]+) = (-?[0-9.]+|@?[a-z_0-9]+)\s*(?:#.*)?$", re.M)


def known_modifier_keys():
    keys = set()
    for sub in ("modifiers", "traits", "culture/traditions", "buildings", "men_at_arms_types"):
        for fn in glob.glob(os.path.join(GAME, "common", sub.replace("/", os.sep), "*.txt")):
            try:
                text = io.open(fn, encoding="utf-8-sig").read()
            except Exception:
                continue
            for m in _KEY_RE.finditer(text):
                keys.add(m.group(1))
    for fn in glob.glob(os.path.join(GAME, "common", "modifier_definition_formats", "*.txt")):
        try:
            text = io.open(fn, encoding="utf-8-sig").read()
        except Exception:
            continue
        keys.update(re.findall(r"^([a-z][a-z0-9_]+) = \{", text, re.M))
    return keys


KNOWN_KEYS = None


def check_keys(owner, fields):
    global KNOWN_KEYS
    if KNOWN_KEYS is None:
        KNOWN_KEYS = known_modifier_keys()
    bad = [k for k in fields if k not in KNOWN_KEYS]
    if bad:
        raise SystemExit("%s uses modifier fields the game does not define: %s" % (owner, bad))


def fields_block(fields, indent="\t"):
    return "".join("%s%s = %s\n" % (indent, k, num(v)) for k, v in fields.items())
