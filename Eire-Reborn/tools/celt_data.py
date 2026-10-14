"""Update 6 (v0.12): the Return of the Celts. One table drives the triggers, the decisions, the modifiers and the events.
region key: (display, empire, claim title, area trigger (county scope), claim count, conquest count, area name, claim minor reqs, conquest minor reqs)"""
import re
from eir_lib import GAME


def counts():
    t = re.sub(r"#[^\n]*", "", open(GAME + r"\common\landed_titles\00_landed_titles.txt", encoding="utf-8-sig").read())
    stack, mem = [], {}
    for m in re.finditer(r"\b([ekdcb]_[a-z0-9_\-']+)\s*=\s*\{|\{|\}", t):
        if m.group(1):
            stack.append(m.group(1))
            if m.group(1).startswith("c_"):
                for s in stack[:-1]:
                    if s and s[0] in "ek":
                        mem.setdefault(s, set()).add(m.group(1))
        elif m.group(0) == "{":
            stack.append(None)
        elif stack:
            stack.pop()
    return {k: len(v) for k, v in mem.items()}


N = counts()
import math


def pct(title, p):
    return math.ceil(p * N[title])


# key: dict
REGIONS = {
    "france": dict(name="France", adj="Gaulish", empire="e_france", area="empire = title:e_france", area_name="the Empire of France", n_area=N["e_france"],
                   claim_n=pct("e_france", 0.12), conq_n=pct("e_france", 0.27),
                   claim_req=["prestige >= 6000", "martial >= 22"], conq_req=["piety >= 1500"],
                   claim_cost=(2500, 3000, 400), conq_cost=(2500, 3500, 600),
                   story="Gaul is where the Celts were before they were Romans, and Franks, and French. The poets can recite the tribes in their order."),
    "germany": dict(name="Germany", adj="Hercynian", empire="e_germany", area="empire = title:e_germany", area_name="the Empire of Germany", n_area=N["e_germany"],
                    claim_n=pct("e_germany", 0.08), conq_n=pct("e_germany", 0.24),
                    claim_req=["prestige_level >= 4", "martial >= 26"], conq_req=["prestige >= 4000"],
                    claim_cost=(2800, 3500, 300), conq_cost=(3000, 3500, 500),
                    story="The Hercynian Forest was Celtic before it was German. The mountain tribes remembered the old names when the Romans came."),
    "spain": dict(name="Spain and Iberia", adj="Celtiberian", empire="e_spain", area="empire = title:e_spain", area_name="the Empire of Spain (Iberia)", n_area=N["e_spain"],
                  claim_n=pct("e_spain", 0.12), conq_n=pct("e_spain", 0.30),
                  claim_req=["piety >= 2500", "has_global_variable = eir_done_monastery"], conq_req=["stewardship >= 20"],
                  claim_cost=(2200, 2500, 900), conq_cost=(2400, 3000, 700),
                  story="The Celtiberians held the high plateau of Iberia, and the Irish chroniclers say that the first Gaels sailed from there."),
    "italy": dict(name="Italy", adj="Cisalpine", empire="e_italy", area="empire = title:e_italy", area_name="the Empire of Italy", n_area=N["e_italy"],
                  claim_n=pct("e_italy", 0.15), conq_n=pct("e_italy", 0.38),
                  claim_req=["diplomacy >= 24", "prestige >= 5000"], conq_req=["prestige >= 3000"],
                  claim_cost=(3000, 3000, 400), conq_cost=(3200, 3500, 500),
                  story="Cisalpine Gaul was Celtic from the Alps to the Po, and Rome burned for it once. The Gael remembers who sacked the city."),
    "galatia": dict(name="Galatia", adj="Galatian", empire="e_byzantium", area="kingdom = title:k_anatolia", area_name="the Kingdom of Anatolia (Galatia)", n_area=N["k_anatolia"],
                    claim_n=pct("k_anatolia", 0.30), conq_n=pct("k_anatolia", 0.63),
                    claim_req=["learning >= 20", "prestige >= 5000"], conq_req=["martial >= 24"],
                    claim_cost=(2600, 3200, 500), conq_cost=(2800, 3800, 600),
                    story="A Celtic people crossed the Bosphorus and held the heart of Anatolia for four hundred years. Saint Paul wrote to them."),
}
