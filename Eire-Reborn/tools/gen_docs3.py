"""Writes docs/FLAVOR_v0.8.md (Update 2 content in plain language) and docs/UNLOCKS.md (how to get every unit and building)."""
import io
import os
import re
from eir_lib import ROOT
import gen_events as ge
import gen_decisions as gd
import dec_v2, dec_v7, dec_v8  # noqa: F401
import bld_data as B
import v8_world

DEC8 = re.findall(r'^D\("(eir_[a-z_0-9]+_decision)"', open(os.path.join(ROOT, "tools", "dec_v8.py"), encoding="utf-8").read(), re.M)


def w(path, text):
    io.open(os.path.join(ROOT, "docs", path), "w", encoding="utf-8", newline="").write(text)


def main():
    groups = ge.load_groups()
    evs = []
    for k in ("ev_v8a", "ev_v8b", "ev_v8c", "ev_v8d"):
        evs += [e for e in groups.get(k, []) if not e.hidden]
    hidden = sum(1 for k in ("ev_v8a", "ev_v8b", "ev_v8c", "ev_v8d") for e in groups.get(k, []) if e.hidden)
    out = ["# Eire Reborn v0.8 (Update 2): the Black Host, the Union and the chieftain's first years\n\n"
           "Every piece follows docs/FLAVOR_GUIDE.md. Counts: %d decisions, %d visible events (+%d hidden relays and timers), %d building families "
           "(each with a tribal and a feudal version), %d duchy chains, %d special buildings, 3 traditions, 2 men-at-arms, 1 kingdom, 4 nicknames, 6 artifacts.\n"
           % (len(DEC8), len(evs), hidden, len(B.FAMILIES), len(B.DUCHY), len(B.SPECIAL))]
    out.append("\n## The Black Host (a three-wave Norse invasion with real armies)\n"
               "Between 868 and 880 the first Gaelic player with a coastline gets **Smoke on the Horizon** (a 12% chance a year, certain from 880). "
               "You prepare (warn the kings, raise beacons, consult the seers, hire mercenaries who may betray you, pay Danegeld, or ignore it) and the "
               "fleet lands: **wave one**, then a **Council of the Kings**, **wave two** (a larger fleet, with a traitor at your table and a monastery in flames), "
               "and a **third, bigger wave** only if you have not already won two. The army sizes scale with your realm: 2,200 levies and about 10 regiments for a chieftain, "
               "up to 6,500 levies and 20+ regiments for a king. Win two waves and you are the **Breaker of the Black Host** (massive prestige, a legend, "
               "a sword, a fifteen-year Norse-Bane coast, and the Norse-Bane Axemen); lose and the Norse keep your coast, but the Break the Norse Yoke decision turns the shame into a boast.\n")
    out.append("\n## Lesser invasions (real armies)\nBritons, Albannach Gaels, Irish rival kings and Hebridean reavers land from time to time (events 0410-0413). "
               "Each can be met with spears, bought off, argued out of it by hospitality, a bishop, a brehon, a poet or fosterage, and each reports its result.\n")
    out.append("\n## Decisions (%d)\n| Decision | Cost | What it does |\n|---|---|---|\n" % len(DEC8))
    for d in gd.DEC:
        if d["key"] in DEC8:
            cost = d["cost"].replace("\n", ", ") or "free"
            out.append("| **%s**%s | %s | %s |\n" % (d["name"], " (major)" if d["major"] else "", cost, d["tip"].replace("|", "/")))
    out.append("\n## Events (%d)\n| # | Event | Summary |\n|---|---|---|\n" % len(evs))
    for e in sorted(evs, key=lambda x: x.num):
        out.append("| %04d | %s | %s |\n" % (e.num, e.title, e.summary.replace("|", "/")))
    out.append("\n## Traditions\n")
    for k, v in v8_world.TRADS.items():
        out.append("* **%s** - %s\n" % (v[5], v[6]))
    out.append("\n## Special buildings (%d)\n| Building | Where | Tier |\n|---|---|---|\n" % len(B.SPECIAL))
    for key, bar, gate, tier, prof, icon, name, desc in B.SPECIAL:
        out.append("| %s | %s | %d |\n" % (name, bar[2:].replace("_", " ").title(), tier))
    w("FLAVOR_v0.8.md", "".join(out))

    u = ["# How to get every unit and building (Eire Reborn v0.8)\n"]
    u.append("\n## Men-at-arms (7)\n| Unit | How to unlock it |\n|---|---|\n"
             "| Kern Javelineers | Open to every Gaelic culture from the start |\n"
             "| Fianna Warband | Decision *Charter the Schools of the Filí*, or the Schools of the Filí tradition |\n"
             "| Gallowglass | Decision *Claim the Irish Sea* (which also gives the *Kings of the Irish Sea* tradition) |\n"
             "| Guard of Tara | Decision *End the Tanistic Fragmentation* or *Proclaim the Sea-Kingdom* (or the Stable High Kingship tradition) |\n"
             "| Royal Ceithern | Decision *Raise the Royal Ceithern* (late game: needs the Oath of the Provincial Kings) |\n"
             "| Insular Spearmen | Decision *Proclaim the Insular Union* (adds the Union of the Insular Celts tradition) |\n"
             "| Norse-Bane Axemen | Break the Black Host (event), then decision *Swear the Oath of the Norse-Bane* |\n")
    u.append("\n## Regional buildings (24 families, tribal and feudal versions)\nTribal holdings use the 2-level tribal versions (75 gold + 200 prestige, then 100 gold + 350 prestige). "
             "Castle, city and church holdings use the 4-level feudal versions (150 / 250 / 340 / 500 gold). Open from the start: ")
    open_ = [f[1] for f in B.FAMILIES if not f[3]]
    gated = [(f[1], f[3]) for f in B.FAMILIES if f[3]]
    u.append(", ".join(open_) + ".\n\nUnlocked by a decision:\n\n| Building | Unlock |\n|---|---|\n")
    from gen_buildings3 import GATE_TEXT
    for n, g in gated:
        u.append("| %s | %s |\n" % (n, GATE_TEXT[g]))
    u.append("\n## Special buildings\nA special building can be built in one particular barony, by a tribal or feudal holder alike, "
             "once the gate is met (gates are shown greyed-out in the build menu). The Hall of Tara now stands at Trim, because the barony called Tara in the game files is in Siberia.\n")
    w("UNLOCKS.md", "".join(u))
    print("docs written")


main()
