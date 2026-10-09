"""Writes docs/FLAVOR_v0.7.md: every new piece of flavor in the 'long look' pack, in plain language."""
import io, os
from eir_lib import ROOT
import gen_events as ge
import gen_decisions as gd
import dec_v2, dec_v7  # noqa: F401


def main():
    groups = ge.load_groups()
    evs = []
    for k in ("ev_v7a", "ev_v7b", "ev_v7c", "ev_v7d"):
        evs += groups.get(k, [])
    out = ["# Eire Reborn v0.7: the long-look flavor pack\n\nEvery piece is built to the flavor guide (docs/FLAVOR_GUIDE.md): trait-based stress, trait-shaped AI choice, several kinds of change per option, labelled risk, a flavor guard so events never flood.\n"]
    out.append("\n## Re-Celticisation: the culture-change system\nDecision **Reclaim the Tongue** converts one foreign-culture county in Britain to your culture. Each conversion raises resentment in the others. Unrest events (The Saxons Mutter, A Thane Calls the Moot, Fire in the Marches) escalate if you push. The remedy is **Grant the Saxon Moot**, which can leave you Lord of Two Peoples. Five conversions with peace unlock the unique **The Britons Return**.\n")
    out.append("\n## Decisions (14)\n| Decision | What it does |\n|---|---|\n")
    for d in gd.DEC:
        if d["key"] in ("eir_reclaim_tongue_decision", "eir_grant_saxon_moot_decision", "eir_restore_old_names_decision", "eir_britons_return_decision", "eir_call_derbfine_decision",
                        "eir_found_bardic_house_decision", "eir_winter_court_of_tales_decision", "eir_found_hospice_decision", "eir_send_missionaries_decision",
                        "eir_buy_welsh_cattle_decision", "eir_summer_booleying_decision", "eir_charter_port_decision", "eir_hire_welsh_archers_decision", "eir_found_college_bangor_decision"):
            out.append("| **%s** | %s |\n" % (d["name"], d["tip"].replace("|", "/")))
    out.append("\n## Events (%d)\n| # | Event | Summary | Chain / gate |\n|---|---|---|---|\n" % len(evs))
    for e in sorted(evs, key=lambda x: x.num):
        gate = "fired by a decision" if "guarded" not in str(e.trigger) and "eir_flavor_cd" not in (e.trigger or "") else "random flavor, behind the flavor guard, cooldown %s yr" % (e.cooldown or "-")
        out.append("| %04d | %s | %s | %s |\n" % (e.num, e.title, e.summary.replace("|", "/"), gate))
    io.open(os.path.join(ROOT, "docs", "FLAVOR_v0.7.md"), "w", encoding="utf-8", newline="").write("".join(out))
    print("written", len(evs), "events")


main()
