"""Audits every decision: prerequisites are hidden until met, every prerequisite can be reached, every event a decision fires exists.
Run: python tools/audit_decisions.py   (after build_all.py)"""
import os
import re
import sys
import glob
sys.path.insert(0, os.path.dirname(__file__))
import gen_decisions
from eir_lib import ROOT

import dec_v2, dec_v7, dec_v8, dec_v10, dec_v12, dec_v13  # noqa: F401,E401
DEC = gen_decisions.DEC
text = open(os.path.join(ROOT, "common", "decisions", "eir_decisions.txt"), encoding="utf-8-sig").read()
blocks = {}
for m in re.finditer(r"^(eir_[a-z0-9_]+_decision) = \{\n(.*?)\n\}\n", text, re.M | re.S):
    blocks[m.group(1)] = m.group(2)

events_def = set()
all_ev_text = ""
for fn in glob.glob(os.path.join(ROOT, "events", "*.txt")):
    t = open(fn, encoding="utf-8-sig").read()
    all_ev_text += t
    events_def.update(re.findall(r"^eir\.(\d+) = \{", t, re.M))
other_text = all_ev_text
for sub in ("scripted_effects", "on_action"):
    for fn in glob.glob(os.path.join(ROOT, "common", sub, "*.txt")):
        other_text += open(fn, encoding="utf-8-sig").read()

set_by = {}
for d in DEC:
    for v in re.findall(r"set_global_variable = ([a-z_0-9]+)", d["effect"]):
        set_by.setdefault(v, set()).add(d["key"])
set_elsewhere = set(re.findall(r"set_global_variable = \{?\s*(?:name = )?([a-z_0-9]+)", other_text))

problems = []


def section(block, name):
    m = re.search(r"\n\t%s = \{\n(.*?)\n\t\}\n" % name, "\n" + block, re.S)
    return m.group(1) if m else ""


prereq = {}
for d in DEC:
    key = d["key"]
    b = blocks.get(key)
    if b is None:
        problems.append("%s missing from the generated file" % key)
        continue
    shown, valid = section(b, "is_shown"), section(b, "is_valid")
    # variables the decision needs (any has_global_variable in is_valid, however wrapped), minus its own
    needs = set(re.findall(r"has_global_variable = ([a-z_0-9]+)", valid))
    needs -= {v for v, k in set_by.items() if key in k}   # its own done-flag is a guard, not a prerequisite
    prereq[key] = needs
    for v in needs:
        if v not in set_by and v not in set_elsewhere:
            problems.append("%s needs %s, which nothing sets" % (key, v))
        elif v in set_by and set_by[v] != {key} and ("has_global_variable = %s" % v) not in shown:
            problems.append("%s needs %s (set by %s) but is not hidden until then" % (key, v, sorted(set_by[v])))
    for e in re.findall(r"trigger_event = (?:\{ id = )?eir\.(\d+)", d["effect"]):
        if e not in events_def:
            problems.append("%s fires event %s, which does not exist" % (key, e))
    for ln in ("desc", "selection_tooltip", "confirm_text"):
        if ln + " = " not in b:
            problems.append("%s has no %s" % (key, ln))
    if not shown.strip():
        problems.append("%s has an empty is_shown" % key)
    own = set_by_own = [v for v, k in set_by.items() if key in k]
    if own and not any("NOT = { has_global_variable = %s }" % v in shown or "has_global_variable = %s" % v in shown for v in own) and d["cd"] < 36500:
        pass

# reachability: a decision can be done when every variable it needs is set by a decision that can be done (or by something else)
done, changed = set(), True
while changed:
    changed = False
    for d in DEC:
        key = d["key"]
        if key in done or key not in prereq:
            continue
        ok = True
        for v in prereq[key]:
            if v in set_by:
                if not (set_by[v] & done) and set_by[v] != {key}:
                    ok = False
        if ok:
            done.add(key)
            changed = True
for d in DEC:
    if d["key"] not in done:
        problems.append("%s can never be taken: its prerequisite chain is circular or broken" % d["key"])

print("decisions audited: %d, reachable: %d, problems: %d" % (len(DEC), len(done), len(problems)))
for p in problems:
    print("  PROBLEM", p)
