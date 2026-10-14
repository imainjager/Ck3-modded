"""Update 8 decisions: the two Irish faiths and the road tracker.
  Kindle the Old Fires      - a Gaelic ruler (after the Filí and the ancient sites) turns to the Druidic faith
  Return to the Cross       - the remedy: go back to the Church (and pay for it)
  Found the Culdee Reform   - a Christian Gaelic ruler founds the Culdee rite (monastery and Cashel done)
  Where Stands the Road?    - lists the next step of the purple road
Registered after dec_v13; costs are final."""
from gen_decisions import D, DEC, GAEL, IRISH
from dec_v10 import req, cost, HAS, not_done
import story_chain

# ------------------------------------------------------------------------------------------------ the Druidic faith
D("eir_kindle_old_fires_decision", "Kindle the Old Fires",
  "The Church has had the island for four hundred years. The oaks still stand. Light the quarter-day fires in public, beneath the old hills, and let the druids come out of the woods.",
  "Needs a Gaelic ruler who is not yet Druidic, the Filí chartered, the ancient sites restored, 400 piety and peace. You, your capital county and your close household convert to the Druidic faith. Big prestige and piety, the Fires Kindled modifier for 30 years (+piety, +prestige, -clergy opinion, -vassal opinion) and a stress shock. A remedy, Return to the Cross, is always open.",
  GAEL + "\n" + "NOT = { faith = faith:eir_druidic }\n" + HAS("eir_done_fili") + "\n" + HAS("eir_done_sites"),
  """set_global_variable = eir_done_druidic_revival
set_character_faith_with_conversion = faith:eir_druidic
capital_county ?= { set_county_faith = faith:eir_druidic }
add_character_modifier = { modifier = eir_fires_kindled_modifier years = 30 }
add_prestige = massive_prestige_gain
add_piety = major_piety_gain
add_stress = major_stress_gain
eir_world_reacts_effect = yes
trigger_event = eir.0991""",
  valid=req("eir_is_gael_ruler_trigger = yes", HAS("eir_done_fili"), HAS("eir_done_sites"), "piety >= 400", "is_at_war = no"),
  cost=cost(gold=300, piety=400), cd=3650, major=True, pic="decision_personal_religious")

D("eir_return_to_the_cross_decision", "Return to the Cross",
  "The fires have burned low, the bishops have written, and the abbots are waiting at the gate with a sack of ashes. Kneel in the porch of the oldest church in your lands, and let the Church take you back.",
  "Appears if you follow the Druidic faith. You return to the Christian faith (Catholic, after the Schism of 1054), pay in gold and piety and lose prestige; the Fires Kindled modifier ends and a Penitent modifier lasts 10 years.",
  GAEL + "\nfaith = faith:eir_druidic",
  """if = {
	limit = { current_year >= 1054 }
	set_character_faith_with_conversion = faith:catholic
}
else = {
	set_character_faith_with_conversion = faith:christian_faith
}
capital_county ?= {
	if = {
		limit = { current_year >= 1054 }
		set_county_faith = faith:catholic
	}
	else = {
		set_county_faith = faith:christian_faith
	}
}
remove_character_modifier = eir_fires_kindled_modifier
add_character_modifier = { modifier = eir_penitent_modifier years = 10 }
add_prestige = major_prestige_loss
add_piety = medium_piety_gain
trigger_event = eir.0992""",
  valid=req("faith = faith:eir_druidic", "is_at_war = no"),
  cost=cost(gold=150, piety=100), cd=3650, pic="decision_personal_religious")

# ------------------------------------------------------------------------------------------------ the Culdee Reform
D("eir_found_culdee_reform_decision", "Found the Culdee Reform",
  "The great monasteries have grown rich and the abbots have grown proud. In the old days the holy men lived in huts of wattle and prayed up to their necks in the cold lake. Gather the hermits, found the new poor houses and let the Church of the Irish return to its roots.",
  "Needs a Christian Gaelic ruler, a monastery of your own, the Rock of Cashel endowed, 500 piety and peace. Creates the Culdee Reform, a rite of your faith (poor abbots, married priests, pilgrimage), which you and your court and capital take up at once. Once per game.",
  GAEL + "\n" + HAS("eir_done_monastery") + "\n" + HAS("eir_done_cashel") + "\n" + not_done("eir_culdee_rite_created")
  + "\nfaith.religion = religion:christianity_religion",
  """set_global_variable = eir_culdee_rite_created
if = {
	limit = { faith = faith:catholic }
	create_rite_from_type = { type = eir_culdee_rite_catholic save_scope_as = new_rite convert = yes }
}
else = {
	create_rite_from_type = { type = eir_culdee_rite save_scope_as = new_rite convert = yes }
}
set_character_rite = scope:new_rite
capital_county ?= { set_county_rite = scope:new_rite }
every_courtier_or_guest = {
	limit = { is_physically_able_ai = yes }
	set_character_rite = scope:new_rite
}
add_character_modifier = { modifier = eir_culdee_reform_modifier years = 25 }
add_prestige = major_prestige_gain
add_piety = massive_piety_gain
eir_world_reacts_effect = yes
trigger_event = eir.0993""",
  valid=req("eir_is_gael_ruler_trigger = yes", HAS("eir_done_monastery"), HAS("eir_done_cashel"), "piety >= 500", "is_at_war = no"),
  cost=cost(gold=500, piety=500), cd=36500, major=True, pic="decision_personal_religious")

# ------------------------------------------------------------------------------------------------ the road tracker
D("eir_story_road_decision", "Where Stands the Road?",
  "The poets say that a king should always know which road he is on. Send for the chief poet and ask him how much of the old story is told, and how much remains.",
  "Free. Shows the next step of the purple road, with what it needs.",
  GAEL,
  "trigger_event = eir.0990",
  valid="is_at_war = no", cost="", cd=30, pic="decision_golden_age")

# every step of the road leaves a flag, so that the tracker can tell what is done
for key in story_chain.STEP:
    d = [x for x in DEC if x["key"] == key]
    var = "eir_story_done_" + key[4:-9]
    if d and ("set_global_variable = " + var) not in d[0]["effect"]:
        d[0]["effect"] += "\nset_global_variable = " + var
