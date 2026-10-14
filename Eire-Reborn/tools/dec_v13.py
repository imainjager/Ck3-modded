"""Update 7 decisions: the fifteen Celtic tenets.
 * every tenet is unlocked by one of the Britannia / Return of the Celts decisions (patched here: a global variable, a line of tooltip text,
   and a free personal tenet slot, if there is one, is filled with the new tenet),
 * every tenet has a decision that is shown only to a ruler whose faith has the tenet or who holds it personally."""
from gen_decisions import D, DEC, IRISH, GAEL
import dec_v12  # noqa: F401  (the unlocking decisions must already exist)
from dec_v10 import req, cost
from tenet_data import T, ORDER

for i, k in enumerate(ORDER):
    t = T[k]
    unlock = [d for d in DEC if d["key"] == t["unlock"]]
    assert len(unlock) == 1, t["unlock"]
    d = unlock[0]
    d["effect"] += ("\nset_global_variable = eir_tenet_%s\nif = {\n\tlimit = { free_personal_tenet_slots > 0 }\n\tset_personal_tenet = tenet:tenet_eir_%s\n}" % (k, k))
    d["tip"] += " Also unlocks the tenet %s, both as a personal tenet and for the tenets of a new or reformed faith (it fills a free personal tenet slot at once if you have one)." % t["name"]

    inv = t["inv"]
    g, pr, pi = inv["cost"]
    D("eir_tn_%s_decision" % k, inv["name"], inv["desc"],
      inv["tip"],
      "eir_tn_%s_trigger = yes" % k,
      """add_character_modifier = { modifier = eir_tn_%s_boon_modifier years = %d }
%s
add_prestige = medium_prestige_gain
eir_world_reacts_effect = yes
trigger_event = eir.%04d""" % (k, inv["years"], inv["extra"], 970 + i),
      valid=req("is_at_war = no"), cost=cost(gold=g, prestige=pr, piety=pi), cd=inv["cd"] * 365, pic="decision_personal_religious")
