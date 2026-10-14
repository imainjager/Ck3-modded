"""Update 6 decisions: the Return of the Celts. An Irish emperor who holds every county of Britannia:
  Mystical Celtic Warriors (a culture tradition + the Forest Warriors + a building)
  -> The Return of the Celts to the Mainland (hidden until the first is done)
  -> five claim decisions (France, Germany, Spain/Iberia, Italy, Galatia): a claim on the empire, a 500% culture boost, a county-share requirement
  -> five conquest decisions: half the counties of the region you hold take your culture."""
from gen_decisions import D, IRISH, GAEL
from dec_v10 import req, cost, HAS, not_done
from celt_data import REGIONS

MYSTIC, MAINLAND = "eir_done_mystic_celts", "eir_done_celts_mainland"
ORDER = ["france", "germany", "spain", "italy", "galatia"]

# ------------------------------------------------------------------------------------------------ 1
D("eir_mystic_celts_decision", "Mystical Celtic Warriors",
  "Britain is whole, and you wear the only crown it has. The druids' groves are overgrown, the old rites forgotten, and the Forest Warriors live on only in the poems. Plant the groves again, call the warriors out of the oaks and let the world see what the Celts were before Rome wrote about them.",
  "Needs an Irish emperor who holds every one of the 93 counties of the Empire of Britannia, 5000 prestige and peace. Adds the tradition Mystical Celtic Warriors to your culture: your people find it easier to hybridise and to diverge culture, faith conversion costs 40% less, +10 advantage in counties of your heritage, -20 opinion from those of other cultures. Unlocks the unique men-at-arms Forest Warriors (skirmishers: 35 damage, 20 toughness, 15 pursuit, 20 screen; +20 damage in forest and jungle, -20 in desert, +5 in plains, +10 in hills) and the Sacred Grove (Nemeton), a regional building worth +25% development growth. Every county of Britannia you hold gains +25% development growth and the forest penalty is lifted. Once per game.",
  IRISH + "\neir_irish_emperor_trigger = yes\n" + not_done(MYSTIC),
  """culture ?= {
	if = {
		limit = { NOT = { has_cultural_tradition = tradition_eir_forest_warriors } }
		add_culture_tradition = tradition_eir_forest_warriors
	}
}
set_global_variable = eir_unlock_nemeton
add_character_modifier = { modifier = eir_mystic_celts_modifier years = 50 }
add_prestige = massive_prestige_gain
add_piety = major_piety_gain
add_dread = medium_dread_gain
every_sub_realm_county = {
	limit = { empire = title:e_britannia }
	add_county_modifier = { modifier = eir_forest_dominion_modifier years = 2 }
}
eir_world_reacts_effect = yes
set_global_variable = eir_done_mystic_celts
trigger_event = eir.0950""",
  valid=req("eir_irish_emperor_trigger = yes", "eir_brit_100_trigger = yes", "prestige >= 5000", "is_at_war = no"),
  cost=cost(gold=2000, prestige=1000, piety=500), cd=36500, major=True, pic="decision_golden_age")

# ------------------------------------------------------------------------------------------------ 2
D("eir_celts_mainland_decision", "The Return of the Celts to the Mainland",
  "The Celts once held the land from the Atlantic to the Black Sea, and a thousand years of being forgotten have not changed their names. Send the heralds across the water and let the old tribes know that the Gael remembers.",
  "Appears after Mystical Celtic Warriors. Needs an Irish emperor, 3000 prestige, 1000 piety and peace. Gives the Celts Look to the Mainland modifier for 50 years and opens five decisions: the Return of the Celts to France, Germany, Spain (Iberia), Italy and Galatia. Once per game.",
  IRISH + "\n" + HAS(MYSTIC) + "\n" + not_done(MAINLAND),
  """add_character_modifier = { modifier = eir_celts_mainland_modifier years = 50 }
add_prestige = massive_prestige_gain
add_piety = medium_piety_gain
eir_world_reacts_effect = yes
set_global_variable = eir_done_celts_mainland
trigger_event = eir.0951""",
  valid=req("eir_irish_emperor_trigger = yes", HAS(MYSTIC), "prestige >= 3000", "piety >= 1000", "is_at_war = no"),
  cost=cost(gold=1000, prestige=1000, piety=250), cd=36500, major=True, pic="decision_found_kingdom")

# ------------------------------------------------------------------------------------------------ 3 + 4
for i, k in enumerate(ORDER):
    r = REGIONS[k]
    claim_var, conq_var = "eir_done_return_" + k, "eir_done_celt_" + k
    claim_cost, conq_cost = r["claim_cost"], r["conq_cost"]
    D("eir_return_%s_decision" % k, "The Return of the Celts to %s" % r["name"],
      "%s Send word to the %s tribes' heirs, put a claim in their name on %s, and let the old tongue be heard again." % (r["story"], r["adj"], r["area_name"]),
      "Needs the Return of the Celts to the Mainland, an Irish emperor, %d counties of %s (%d of %d), peace and %s. Gives you a claim on %s, and the modifier The Return of the Celts to %s for 50 years: every foreign county of %s in your realm has a 6%% chance a year to take your culture (five times the normal pace), and each one resists with -30 opinion for 15 years. Once per game."
      % (r["claim_n"], r["area_name"], r["claim_n"], r["n_area"], ", ".join(x.replace(">=", "at least").replace("_", " ") for x in r["claim_req"]), r["area_name"], r["name"], r["area_name"]),
      IRISH + "\n" + HAS(MAINLAND) + "\n" + not_done(claim_var),
      """add_pressed_claim = title:%s
add_character_modifier = { modifier = eir_return_%s_modifier years = 50 }
add_prestige = massive_prestige_gain
add_piety = medium_piety_gain
add_dread = minor_dread_gain
eir_world_reacts_effect = yes
set_global_variable = %s
trigger_event = eir.%04d""" % (r["empire"], k, claim_var, 952 + i),
      valid=req("eir_irish_emperor_trigger = yes", HAS(MAINLAND), "eir_celt_%s_claim_trigger = yes" % k, *(r["claim_req"] + ["is_at_war = no"])),
      cost=cost(gold=claim_cost[0], prestige=claim_cost[1], piety=claim_cost[2]), cd=36500, major=True, pic="decision_found_kingdom")
    D("eir_celt_%s_decision" % k, "The Celts Return to %s" % r["name"],
      "The claim has been made and the swords drawn, and the %s lands are in your hands. Now say the old tongue in the old places, build the groves, and let half of %s learn who they were." % (r["adj"], r["area_name"]),
      "Appears after the Return of the Celts to %s. Needs %d counties of %s (%d of %d), peace and %s. Half of the counties of %s in your realm that are not of your culture take your culture at once (each resists with -30 opinion for 15 years), plus The Celts Return to %s modifier for 50 years and a great deal of prestige. Once per game."
      % (r["name"], r["conq_n"], r["area_name"], r["conq_n"], r["n_area"], ", ".join(x.replace(">=", "at least").replace("_", " ") for x in r["conq_req"]), r["area_name"], r["name"]),
      IRISH + "\n" + HAS(claim_var) + "\n" + not_done(conq_var),
      """eir_celt_half_convert_%s_effect = yes
add_character_modifier = { modifier = eir_celt_%s_won_modifier years = 50 }
add_prestige = massive_prestige_gain
add_prestige = massive_prestige_gain
add_piety = major_piety_gain
add_legitimacy = major_legitimacy_gain
eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 8 }
eir_world_reacts_effect = yes
set_global_variable = %s
trigger_event = eir.%04d""" % (k, k, conq_var, 957 + i),
      valid=req("eir_irish_emperor_trigger = yes", HAS(claim_var), "eir_celt_%s_conquest_trigger = yes" % k, *(r["conq_req"] + ["is_at_war = no"])),
      cost=cost(gold=conq_cost[0], prestige=conq_cost[1], piety=conq_cost[2]), cd=36500, major=True, pic="decision_golden_age")
