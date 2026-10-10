"""Lists events that are defined but never fired by an on_action, a decision or another event."""
import os
import re
import glob
import collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
text = ""
defined = set()
for f in glob.glob(os.path.join(ROOT, "events", "*.txt")) + glob.glob(os.path.join(ROOT, "common", "**", "*.txt"), recursive=True):
    t = open(f, encoding="utf-8-sig").read()
    text += t
    if os.path.basename(os.path.dirname(f)) == "events":
        defined |= set(re.findall(r"^eir\.(\d+) = \{", t, re.M))
cnt = collections.Counter(re.findall(r"eir\.(\d+)(?![.\d])", text))
dead = [d for d in sorted(defined) if cnt[d] <= 1]
print("%d events defined; %d never fired:" % (len(defined), len(dead)), " ".join(dead))
