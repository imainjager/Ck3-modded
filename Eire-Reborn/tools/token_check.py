"""Safety net for effects and triggers that the game would reject: every `word =` used in the mod's script must also be
used somewhere in the base game's own script (or be defined by the mod). Catches typos and invented effects.
Run: python tools/token_check.py
"""
import os
import re
import glob
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME = r"C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game"
TOKEN = re.compile(r"(?<![A-Za-z0-9_:\.$@])([a-z_][a-z0-9_]*)\s*(?:\?=|>=|<=|=|<|>)", re.M)


def read(f):
    try:
        return open(f, encoding="utf-8-sig", errors="replace").read()
    except Exception:
        return ""


def strip_comments(t):
    return re.sub(r"#[^\n]*", "", t)


def tokens_of(path_globs):
    out = set()
    for g in path_globs:
        for f in glob.glob(g, recursive=True):
            out.update(TOKEN.findall(strip_comments(read(f))))
    return out


def main():
    vanilla = tokens_of([GAME + r"\events\**\*.txt", GAME + r"\common\**\*.txt", GAME + r"\history\**\*.txt"])
    # everything the mod ships: events, every folder under common/ (Update 8 added activities, religion, culture, laws, ...) and history
    mine_dirs = [ROOT + r"\events\*.txt", ROOT + r"\common\**\*.txt", ROOT + r"\history\**\*.txt"]
    defined = set()
    for g in mine_dirs:
        for f in glob.glob(g, recursive=True):
            defined.update(re.findall(r"^\s*([a-z_][a-z0-9_]*) = \{", strip_comments(read(f)), re.M))
    bad = {}
    for g in mine_dirs:
        for f in glob.glob(g, recursive=True):
            for tok in set(TOKEN.findall(strip_comments(read(f)))):
                if tok in vanilla or tok in defined:
                    continue
                bad.setdefault(tok, set()).add(os.path.basename(f))
    for tok in sorted(bad):
        print("UNKNOWN TOKEN %-40s in %s" % (tok, ", ".join(sorted(bad[tok]))))
    print("%d unknown tokens" % len(bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
