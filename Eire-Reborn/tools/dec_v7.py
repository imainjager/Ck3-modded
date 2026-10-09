"""v0.7 decisions. Registered after dec_finalize, so costs here are final (no automatic rescaling).
Each follows the flavor guide: a real gate, a cost (or none where the gate is the challenge), several kinds of reward,
a ceremony or follow-up event, and a risk or remedy."""
from gen_decisions import D, IRISH, GAEL

S1 = "eir_stage1_trigger = yes"
S2 = "eir_stage2_trigger = yes"
S3 = "eir_stage3_trigger = yes"
VIS = "eir_visible_stage1_trigger = yes"
FILI = "has_global_variable = eir_done_fili"
BROTH = "has_global_variable = eir_done_brotherhood"
MONK = "has_global_variable = eir_done_monastery"


def req(*lines):
    return "\n".join(l for l in lines if l)


def cost(gold=0, prestige=0, piety=0):
    return "\n".join(x for x in (("gold = %d" % gold) if gold else "", ("prestige = %d" % prestige) if prestige else "", ("piety = %d" % piety) if piety else "") if x)


# =============================================================================
# RE-CELTICISATION
# =============================================================================
D("eir_reclaim_tongue_decision", "Reclaim the Tongue",
  "A county in Britain that has spoken English for generations can be taught Gaelic or Welsh again: hedge-schools, new place-names, priests who say the Mass in the old speech. The old people remember. The young people are curious. The neighbours are watching.",
  "Needs the Celtic Brotherhood and a duchy. Turns one foreign-culture county of Britain to your culture, founds hedge-schools there, and fires a ceremony. Every conversion raises resentment in the remaining foreign counties; unrest events, a moot and a possible revolt follow. Repeatable every five years.",
  GAEL + "\n" + VIS + "\neir_has_foreign_britain_counties_trigger = yes\n" + BROTH,
  """random_sub_realm_county = {
	limit = { eir_foreign_britain_county_trigger = yes }
	save_scope_as = eir_conv_county
	set_county_culture = root.culture
	add_county_modifier = { modifier = eir_hedge_schools_modifier years = 15 }
}
eir_recelt_bump_effect = yes
every_sub_realm_county = {
	limit = {
		eir_foreign_britain_county_trigger = yes
		NOT = { this = scope:eir_conv_county }
	}
	add_county_modifier = { modifier = eir_cultural_resentment_modifier years = 8 }
}
add_prestige = medium_prestige_gain
add_piety = minor_piety_gain
trigger_event = eir.0300
trigger_event = { id = eir.0303 years = 2 }""",
  valid=req(S2, "is_at_war = no"),
  cost=cost(gold=150, prestige=400, piety=100), cd=1825, pic="decision_culture")

D("eir_grant_saxon_moot_decision", "Grant the Saxon Moot",
  "The thanes of the conquered counties ask for one thing: the right to meet under their own oak, in their own speech, and judge their own small quarrels. Give it, and the grumbling turns into a loyal complaint.",
  "Remedy for Re-Celticisation. Clears all cultural resentment, gives the foreign counties a Moot of Their Own, and leaves you Lord of Two Peoples, with a moot horn made by the thanes. It costs gold and a little pride.",
  GAEL + "\n" + VIS + "\nhas_variable = eir_resent\nvar:eir_resent >= 1",
  """eir_resent_clear_effect = yes
every_sub_realm_county = {
	limit = { eir_foreign_britain_county_trigger = yes }
	add_county_modifier = { modifier = eir_saxon_moot_modifier years = 15 }
}
add_character_modifier = { modifier = eir_two_peoples_modifier years = 12 }
eir_vassal_opinion_effect = { MODIFIER = eir_two_peoples_opinion OPINION = 5 }
add_prestige = minor_prestige_gain
eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 20 }
trigger_event = { id = eir.0337 days = 20 }""",
  valid=req("eir_has_foreign_britain_counties_trigger = yes", "is_at_war = no"),
  cost=cost(gold=250, prestige=100), cd=1825, pic="decision_social")

D("eir_restore_old_names_decision", "Restore the Old Names",
  "Every hill, ford and village in Britain had a Celtic name before it had an English one. Send the poets with the surveyors, and write the old names back into the charters.",
  "Needs the Filí's patronage and at least two conversions. Prestige, a modifier that lasts, a legend and (after three conversions) the nickname 'the Tongue-Giver'.",
  GAEL + "\n" + VIS + "\nhas_variable = eir_recelt",
  """add_character_modifier = { modifier = eir_tongue_restorer_modifier years = 15 }
eir_legend_title_effect = { TITLE = primary_title }
add_trait_xp = { trait = lifestyle_poet value = 40 }
add_prestige = medium_prestige_gain
if = {
	limit = {
		var:eir_recelt >= 3
		NOT = { has_any_nickname = yes }
	}
	give_nickname = nick_eir_tongue_giver
}
eir_world_reacts_effect = yes""",
  valid=req(S2, FILI, "var:eir_recelt >= 2", "NOT = { has_character_modifier = eir_tongue_restorer_modifier }"),
  cost=cost(gold=200, prestige=300), cd=3650, pic="decision_tale")

D("eir_britons_return_decision", "The Britons Return",
  "Five conversions, a peace made with the Saxon thanes, three Celtic counties in Britain and a hall full of poets: this is the day the poems have been promising since the Romans left.",
  "Needs a kingdom, five Reclaimed counties, little unrest left and the Brotherhood. Costs piety and prestige. Gives the Britons Return modifier for 30 years, a dynasty modifier, the nickname 'Restorer of Britain', claims on England, a legend, and a ceremony. Happens once per game.",
  GAEL + "\n" + VIS + "\nhas_variable = eir_recelt\n" + BROTH + "\nNOT = { has_global_variable = eir_unique_britons_return }",
  """add_character_modifier = { modifier = eir_britain_restored_modifier years = 30 }
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 50 } }
eir_grant_claims_non_celtic_effect = { TITLE = k_england }
eir_legend_title_effect = { TITLE = primary_title }
add_prestige = massive_prestige_gain
add_piety = major_piety_gain
set_global_variable = eir_unique_britons_return
trigger_event = eir.0307""",
  valid=req(S3, "var:eir_recelt >= 5", "has_variable = eir_resent", "var:eir_resent <= 1", "eir_has_celtic_britain_counties_trigger = yes"),
  cost=cost(prestige=600, piety=250), cd=36500, major=True, pic="decision_found_kingdom")

# =============================================================================
# THE KINDRED AND THE LAW
# =============================================================================
D("eir_call_derbfine_decision", "Call the Derbfine",
  "The derbfine is the council of every adult male in the royal kindred to four generations. In the old days it chose the next king. Summon it now, in daylight, and let it choose together instead of apart.",
  "Needs peace and a heir. Removes Throne Turmoil, gives legitimacy and vassal opinion for ten years, and a chance of the Peacemaker of Tara trait. Cousins who attend are bound by the result.",
  GAEL + "\n" + VIS + "\neir_collapse_active_trigger = yes",
  """if = {
	limit = { has_character_modifier = eir_throne_turmoil_modifier }
	remove_character_modifier = eir_throne_turmoil_modifier
}
add_character_modifier = { modifier = eir_derbfine_counsel_modifier years = 10 }
eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 8 }
add_legitimacy = medium_legitimacy_gain
add_prestige = minor_prestige_gain
eir_trait_effect = { TRAIT = eir_peacemaker_of_tara OPPOSITE = wrathful CHANCE = 20 }
primary_heir ?= { add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 15 } }""",
  valid=req(S1, "is_at_war = no", "exists = primary_heir", "any_vassal = { count >= 2 }", "NOT = { has_character_modifier = eir_derbfine_counsel_modifier }"),
  cost=cost(gold=100, prestige=150), cd=3650, pic="decision_dynasty_house")

D("eir_found_bardic_house_decision", "Found a Bardic House",
  "A dynasty that keeps its own poets, harpers and genealogists need never rely on a foreign scribe to praise it. Endow the posts, house the masters and let the verses be handed down from father to son.",
  "Needs the Schools of the Filí, a duchy and the Ollamh Rígh. A dynasty modifier for 60 years, a High Poet's Chain in two years, and learning. Happens once per game.",
  GAEL + "\n" + VIS + "\nNOT = { has_global_variable = eir_unique_bardic_house }",
  """dynasty ?= { add_dynasty_modifier = { modifier = eir_bardic_house_modifier years = 60 } }
add_character_modifier = { modifier = eir_fili_patron_modifier years = 10 }
add_trait_xp = { trait = lifestyle_poet value = 40 }
add_prestige = medium_prestige_gain
set_global_variable = eir_unique_bardic_house
trigger_event = { id = eir.0336 years = 2 }""",
  valid=req(S2, FILI, "culture = { has_cultural_tradition = tradition_eir_bardic_schools }", "has_character_modifier = eir_royal_ollamh_modifier"),
  cost=cost(gold=250, prestige=500), cd=36500, major=True, pic="decision_tale")

D("eir_winter_court_of_tales_decision", "Hold the Winter Court of Tales",
  "In the long dark the poets tell the great stories in the hall, one a night. Decide which will be told, and which will be left to the bards of the next king.",
  "Needs the Filí and a duchy. The Táin Retold modifier, poet XP, a legend, and a chance at a nickname. Repeatable every fifteen years.",
  GAEL + "\n" + VIS + "\n" + FILI,
  """add_character_modifier = { modifier = eir_tain_retold_modifier years = 8 }
add_trait_xp = { trait = lifestyle_poet value = 40 }
eir_legend_title_effect = { TITLE = primary_title }
add_prestige = medium_prestige_gain
eir_court_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 6 }""",
  valid=req(S2, "NOT = { has_character_modifier = eir_tain_retold_modifier }"),
  cost=cost(gold=200, prestige=200), cd=5475, pic="decision_tale")

# =============================================================================
# FAITH
# =============================================================================
D("eir_found_hospice_decision", "Found the Hospice of Brigid",
  "A house of nuns, herbalists and physicians for the sick and the dying, under the protection of the saint of cattle, healing and the hearth. The poor will walk for days to reach it.",
  "Needs a monastery and 300 piety. A county hospice modifier for twenty years, physician XP, a chance of the Compassionate trait, and a follow-up event in a year. Happens once per game.",
  GAEL + "\n" + VIS + "\n" + MONK + "\nNOT = { has_global_variable = eir_unique_hospice }",
  """random_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_hospice_modifier years = 20 }
}
add_trait_xp = { trait = lifestyle_physician value = 30 }
eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 25 }
add_piety = medium_piety_gain
add_prestige = minor_prestige_gain
set_global_variable = eir_unique_hospice
trigger_event = { id = eir.0333 years = 1 }""",
  valid=req(S2, "piety >= 300", "any_held_title = { tier = tier_county }"),
  cost=cost(gold=300, piety=200), cd=36500, major=True, pic="decision_personal_religious")

D("eir_send_missionaries_decision", "Send the Peregrini to Alba",
  "Irish monks have always walked into the sea for the love of God. Send twelve of them to Alba with a boat, a bell and a gospel, and see who comes back.",
  "Needs the Brotherhood, a monastery and 250 piety. Piety now, a Missionaries Return event in two to three years, a Patron of the Pilgrims modifier. Repeatable every ten years.",
  GAEL + "\n" + VIS + "\n" + BROTH + "\n" + MONK,
  """add_piety = minor_piety_gain
add_character_modifier = { modifier = eir_missionary_glory_modifier years = 4 }
add_trait_xp = { trait = lifestyle_mystic value = 20 }
trigger_event = { id = eir.0334 years = { 2 3 } }""",
  valid=req(S2, "piety >= 250", "is_at_war = no"),
  cost=cost(gold=150, piety=250), cd=3650, pic="decision_personal_religious")

# =============================================================================
# ECONOMY AND THE SEASONS
# =============================================================================
D("eir_buy_welsh_cattle_decision", "Buy Cattle from the Welsh",
  "The murrain has taken the herds. Welsh dealers across the water have healthy beasts and a high price. Pay it, and the poor will not sell their land.",
  "Remedy for the Murrain. Removes the Murrain from all counties, leaves you A Fair Lord, strengthens ties with Wales and leaves the herds richer than before.",
  GAEL + "\nany_sub_realm_county = { has_county_modifier = eir_murrain_modifier }",
  """every_sub_realm_county = {
	limit = { has_county_modifier = eir_murrain_modifier }
	remove_county_modifier = eir_murrain_modifier
	add_county_modifier = { modifier = eir_cattle_drive_modifier years = 6 }
}
add_character_modifier = { modifier = eir_fair_lord_modifier years = 8 }
add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 4 }
add_prestige = minor_prestige_gain""",
  valid=req("is_at_war = no"), cost=cost(gold=250), cd=1825, pic="decision_spend_money")

D("eir_summer_booleying_decision", "Go Up to the Summer Pastures",
  "Once the cattle are in the high pastures the whole household goes with them, to milk, make cheese and sing. A king who does this is remembered as a man of the people.",
  "Only between May and August, and only in peace. Stress relief, health, a county dairy bonus for ten years and a chance of a hill-pasture quarrel. Repeatable every year.",
  GAEL + "\n" + VIS + "\n" + "has_global_variable = eir_unlock_cattle_enclosure",
  """add_character_modifier = { modifier = eir_booley_modifier years = 3 }
random_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_booley_county_modifier years = 10 }
}
add_stress = medium_stress_loss
add_prestige = miniscule_prestige_gain
trigger_event = { id = eir.0343 days = { 20 60 } }""",
  valid=req(S1, "is_at_war = no", "current_month >= 5", "current_month <= 8", "NOT = { has_character_modifier = eir_booley_modifier }"),
  cost=cost(gold=60), cd=365, pic="decision_pet_dog")

D("eir_charter_port_decision", "Charter a Harbour Town",
  "A fishing village with a good harbour and no walls can become a market town if the king grants it liberties: freedom from tolls, a market court, and a charter.",
  "Needs the Irish Sea tradition, a duchy and a port. A chartered county for 25 years, income, diplomacy. Repeatable every ten years.",
  GAEL + "\n" + VIS + "\nhas_global_variable = eir_unlock_sea_trade",
  """random_held_title = {
	limit = {
		tier = tier_county
		is_coastal_county = yes
		NOT = { has_county_modifier = eir_chartered_town_modifier }
	}
	add_county_modifier = { modifier = eir_chartered_town_modifier years = 25 }
}
add_character_modifier = { modifier = eir_port_charter_modifier years = 15 }
add_prestige = minor_prestige_gain
add_trait_xp = { trait = lifestyle_traveler track = travel value = 10 }
eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 3 }""",
  valid=req(S2, "eir_ports_trigger = { N = 1 }", "any_held_title = {\n\ttier = tier_county\n\tis_coastal_county = yes\n\tNOT = { has_county_modifier = eir_chartered_town_modifier }\n}"),
  cost=cost(gold=400, prestige=150), cd=3650, pic="decision_spend_money")

# =============================================================================
# WAR AND THE CELTIC WORLD
# =============================================================================
D("eir_hire_welsh_archers_decision", "Hire Welsh Archers",
  "The longbowmen of the Welsh marches shoot twice as far as any Irish bow. Hire a company for a campaign and watch the English horse learn caution.",
  "Needs the Brotherhood and a duchy. A mercenary company of bowmen, a Welsh Longbows modifier for eight years, and a friendlier Wales. Repeatable every five years.",
  GAEL + "\n" + VIS + "\n" + BROTH,
  """spawn_army = {
	levies = 0
	men_at_arms = {
		type = bowmen
		stacks = 3
	}
	location = capital_province
	origin = capital_province
	inheritable = no
	name = eir_mercenary_company_name
}
add_character_modifier = { modifier = eir_welsh_archers_modifier years = 8 }
every_ruler = {
	limit = {
		is_ai = yes
		is_independent_ruler = yes
		culture ?= { has_cultural_pillar = heritage_brythonic }
		is_within_diplo_range = { CHARACTER = root }
	}
	add_opinion = { target = root modifier = eir_gwynedd_friend_opinion opinion = 8 }
}
add_prestige = miniscule_prestige_gain""",
  valid=req(S2, "is_at_war = no"), cost=cost(gold=350, prestige=50), cd=1825, pic="decision_recruitment")

D("eir_found_college_bangor_decision", "Found the College of Bangor",
  "Bangor has taught Europe's scholars before. Endow it with a library, a refectory and a staff of foreign masters, and students from three kingdoms will walk across the sea to study in Irish.",
  "Needs a kingdom, the Filí, a monastery and a scriptorium. A county college for 40 years, learning and diplomacy, a Patron of the College modifier for 30 years, and the nickname 'the Scholar'. Happens once per game.",
  GAEL + "\n" + VIS + "\n" + FILI + "\nNOT = { has_global_variable = eir_unique_college_bangor }",
  """random_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_college_county_modifier years = 40 }
}
add_character_modifier = { modifier = eir_college_of_bangor_modifier years = 30 }
add_trait_xp = { trait = lifestyle_poet value = 40 }
add_prestige = major_prestige_gain
add_piety = medium_piety_gain
if = {
	limit = { NOT = { has_any_nickname = yes } }
	give_nickname = nick_the_scholar
}
eir_world_reacts_effect = yes
set_global_variable = eir_unique_college_bangor""",
  valid=req(S3, MONK, "has_global_variable = eir_unlock_scriptorium", "learning >= 12"),
  cost=cost(gold=400, prestige=800, piety=300), cd=36500, major=True, pic="decision_tale")
