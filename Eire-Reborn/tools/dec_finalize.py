"""Post-processing applied to every decision (flavor guide v1):
  * tribal-first costs: gold is halved, prestige leads, major decisions also cost piety (vanilla pattern);
  * one-time decisions are unique per game (global variable) unless the mod's own rule keeps destroying their result;
  * every big decision fires a ceremony event (nickname-or-prestige choice) and the world reacts;
  * remedies for negative decisions leave the player better than before.
"""
import re
import gen_decisions as g

DEC = g.DEC

# --- 1. remove decisions vanilla already covers -------------------------------------------------------------
DROP = {"eir_britannia_restored_decision"}
DEC[:] = [d for d in DEC if d["key"] not in DROP]

# --- 2. ceremonies: decision -> event number ----------------------------------------------------------------
CEREMONY = {
    "eir_hold_oenach_decision": 210,
    "eir_rebuild_tara_hall_decision": 211,
    "eir_found_bardic_schools_decision": 212,
    "eir_adopt_cattle_wealth_decision": 213,
    "eir_adopt_culdee_decision": 214,
    "eir_thalassocracy_decision": 215,
    "eir_gaelic_revival_decision": 216,
    "eir_end_fragmentation_decision": 217,
    "eir_celtic_brotherhood_decision": 218,
}

# --- 3. remedies that beat the penalty ----------------------------------------------------------------------
REMEDY_BONUS = {
    "eir_pay_eraic_decision": "add_character_modifier = { modifier = eir_honour_restored_modifier years = 8 }\n"
                              "eir_vassal_opinion_effect = { MODIFIER = eir_wergild_paid_opinion OPINION = 6 }\n"
                              "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 25 }",
    "eir_appease_satirists_decision": "add_character_modifier = { modifier = eir_honour_restored_modifier years = 6 }\n"
                                      "eir_court_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 10 }\nadd_prestige = 100",
    "eir_waive_cain_decision": "add_character_modifier = { modifier = eir_fair_lord_modifier years = 10 }",
    "eir_remit_tribute_decision": "add_character_modifier = { modifier = eir_fair_lord_modifier years = 10 }",
    "eir_release_hostages_decision": "add_character_modifier = { modifier = eir_fair_lord_modifier years = 8 }",
    "eir_end_danegeld_decision": "add_character_modifier = { modifier = eir_honour_restored_modifier years = 10 }\n"
                                 "if = {\n\tlimit = { NOT = { has_any_nickname = yes } }\n\tgive_nickname = nick_eir_norse_bane\n}",
    "eir_reconcile_culdees_decision": "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 12 }",
    "eir_wergild_decision": "add_character_modifier = { modifier = eir_honour_restored_modifier years = 8 }",
    "eir_pacify_natives_decision": "add_character_modifier = { modifier = eir_fair_lord_modifier years = 10 }\nadd_prestige = 150",
    "eir_name_tanaiste_decision": "if = {\n\tlimit = { has_character_modifier = eir_tanistry_dispute_modifier }\n\tremove_character_modifier = eir_tanistry_dispute_modifier\n}\n"
                                  "if = {\n\tlimit = { has_character_modifier = eir_blinded_modifier }\n\tremove_character_modifier = eir_blinded_modifier\n}\n"
                                  "add_character_modifier = { modifier = eir_fair_lord_modifier years = 8 }",
}

# --- 4. repeatable on purpose --------------------------------------------------------------------------------
NOT_UNIQUE = {"eir_crowned_at_tara_decision"}   # the tanistic collapse destroys the crown on each death until it is ended


def round_to(x, step=25):
    return int(round(x / float(step)) * step)


for d in DEC:
    key = d["key"]
    short = key.replace("eir_", "").replace("_decision", "")

    # costs: tribal-first
    lines = [l for l in d["cost"].split("\n") if l.strip()]
    cost = {}
    for l in lines:
        m = re.match(r"\s*(gold|prestige|piety) = (\d+)\s*$", l)
        if m:
            cost[m.group(1)] = int(m.group(2))
        else:
            cost.setdefault("_raw", []).append(l)
    if "gold" in cost:
        cost["gold"] = max(50, round_to(cost["gold"] * 0.5))
    if d["major"] and "piety" not in cost and d["cd"] >= 7300:
        p = cost.get("prestige", 0)
        cost["piety"] = 500 if p >= 2500 else 300 if p >= 1000 else 200
    out = []
    for k in ("gold", "prestige", "piety"):
        if k in cost:
            out.append("%s = %d" % (k, cost[k]))
    out += cost.get("_raw", [])
    d["cost"] = "\n".join(out)

    # decisions only appear once the player is close to the previous stage (keeps the list clean at game start)
    if "eir_stage4_trigger" in d["valid"] and "eir_stage3_trigger" not in d["shown"]:
        d["shown"] = d["shown"].rstrip("\n") + "\neir_stage3_trigger = yes"
    elif "eir_stage3_trigger" in d["valid"] and "eir_stage2_trigger" not in d["shown"]:
        d["shown"] = d["shown"].rstrip("\n") + "\neir_stage2_trigger = yes"
    elif "eir_stage2_trigger" in d["valid"] and "eir_stage1_trigger" not in d["shown"]:
        d["shown"] = d["shown"].rstrip("\n") + "\neir_stage1_trigger = yes"

    # ceremony + world reaction
    if key in CEREMONY:
        d["effect"] = d["effect"].rstrip("\n") + "\ntrigger_event = { id = eir.%04d days = 10 }" % CEREMONY[key]

    # remedy bonuses
    if key in REMEDY_BONUS:
        d["effect"] = d["effect"].rstrip("\n") + "\n" + REMEDY_BONUS[key]
        d["tip"] = d["tip"].rstrip(".") + ". It leaves you better off than before."

    # unique once per game
    if d["cd"] >= 36500 and key not in NOT_UNIQUE:
        var = "eir_unique_" + short
        d["shown"] = d["shown"].rstrip("\n") + "\nNOT = { has_global_variable = %s }" % var
        d["effect"] = d["effect"].rstrip("\n") + "\nset_global_variable = %s" % var
        d["tip"] = d["tip"].rstrip(".") + ". Happens only once per game."
