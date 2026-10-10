"""Update 2, part A: THE BLACK HOST (a three-wave Norse invasion with real armies) and the lesser invasions
(Britons, Albans, Irish rivals, Hebridean reavers).

Black Host state lives on the player in `eir_bh_stage`:
  1 wave 1 landed, 2 wave 1 over, 3 wave 2 landed, 4 wave 2 over, 5 wave 3 landed, 6 everything over.
Counters: eir_bh_wins, eir_bh_losses, eir_bh_prep (0-4: how well the player prepared), eir_bh_alliance, eir_bh_relics_safe.
Wars end through the on_action hooks in eir_on_actions_v8.txt, which fire 0420 (wave beaten) or 0421 (wave won by the Norse).
"""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

NORSE_ANY = """any_ruler = {
	is_ai = yes
	is_ruler = yes
	highest_held_title_tier >= tier_county
	culture ?= { has_cultural_pillar = heritage_north_germanic }
	NOT = { has_truce = root }
	NOT = { this = root }
}"""
BH_PORT = "left_portrait = {\n\tcharacter = scope:eir_bh_lord\n\tanimation = personality_bold\n}"
FILI = "has_global_variable = eir_done_fili"
INV_PORT = "left_portrait = {\n\tcharacter = scope:eir_inv_lord\n\tanimation = personality_bold\n}"


def bh_intro(wave_fx):
    return seq("eir_bh_pick_effect = yes", wave_fx)


# =============================================================================
# 0400 SMOKE ON THE HORIZON  (the chain starts)
# =============================================================================
ev(400, "Smoke on the Horizon",
   "Fishermen say a fleet is gathering in the north, and a warlord has sworn to take Ireland.",
   "The word came down the coast from boat to boat: sixty ships at the Orkney anchorage, then eighty, and a king in the north who has promised his men the silver of every church in Ireland. They call his army the Black Host, for the tarred sails and for the colour of what it leaves behind.\n\nYou have a year, perhaps less. The question is what to do with it.",
   [
       O("Send riders to every king in Ireland with the warning.",
         "change_variable = { name = eir_bh_prep add = 1 }", "set_variable = { name = eir_bh_alliance value = 1 }", PRESTIGE_S,
         "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 4 }", xp("lifestyle_traveler", 15),
         gate="OR = {\ndiplomacy >= 10\nhas_trait = gregarious\nhas_trait = honest\n}", st=S_HONEST, ai=40, ai_mod=[("gregarious", 20), ("honest", 10)]),
       O("Raise beacons and watch-towers along the whole coast.",
         GOLD_M, "change_variable = { name = eir_bh_prep add = 1 }", "add_character_modifier = { modifier = eir_beacons_modifier years = 6 }",
         "every_realm_county = {\n\tlimit = { is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_beacon_county_modifier years = 8 }\n}",
         st=S_SHREWD, ai=45, ai_mod=[("shrewd", 15), ("diligent", 10)]),
       O("Ask the poets and the seers what the omens say.",
         luck("t400w", "The omens name the very beach", "change_variable = { name = eir_bh_prep add = 2 }\nadd_piety = minor_piety_gain\nadd_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }",
              "t400l", "The omens are muddy and the poets quarrel", "add_stress = minor_stress_gain\nadd_prestige = minor_prestige_loss", p=55, bonus=(15, "learning >= 12")),
         xp("lifestyle_mystic", 20),
         gate="OR = {\nlearning >= 9\nhas_trait = zealous\nhas_trait = lifestyle_mystic\n}", st=S_ZEAL, ai=25, ai_mod=[("zealous", 15)]),
       O("Hire a company of Norse-Gaelic mercenaries to meet them at sea.",
         GOLD_M,
         luck("t400m", "The company sails out under your banner", "change_variable = { name = eir_bh_prep add = 2 }\neir_defender_levy_effect = yes\nadd_prestige = minor_prestige_gain",
              "t400n", "The mercenaries take the other side's silver", "set_variable = { name = eir_bh_traitor value = 1 }\nadd_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain", p=70, bonus=(10, "intrigue >= 12")),
         gate="gold >= 200", st=S_GREED, ai=25),
       O("Pay for peace before the fleet sails. (Danegeld.)",
         "remove_short_term_gold = major_gold_value", LOSS_M, "add_character_flag = { flag = eir_paid_danegeld years = 3 }",
         "add_character_modifier = { modifier = eir_danegeld_modifier years = 3 }", "set_variable = { name = eir_bh_paid value = 1 }",
         gate="gold >= 150", st="brave = minor_stress_impact_gain\ncraven = minor_stress_impact_loss", ai=8, ai_mod=[("craven", 20)]),
       O("Trust in your swords and say nothing.",
         "add_character_modifier = { modifier = eir_shield_wall_modifier years = 2 }", PRESTIGE_S, "change_variable = { name = eir_bh_prep add = -1 }",
         st=S_BRAVE, ai=15, ai_mod=[("brave", 15), ("arrogant", 10)]),
   ],
   "war", gate=f"eir_is_gael_ruler_trigger = yes\nis_ai = no\nNOT = {{ has_global_variable = eir_bh_started }}\n{NORSE_ANY}", guarded=False,
   immediate="""set_global_variable = eir_bh_started
set_variable = { name = eir_bh_prep value = 0 }
set_variable = { name = eir_bh_wins value = 0 }
set_variable = { name = eir_bh_losses value = 0 }
set_variable = { name = eir_bh_stage value = 0 }
set_variable = { name = eir_bh_alliance value = 0 }
trigger_event = { id = eir.0399 days = 240 }""",
   variants=[("has_trait = brave", "You have fought the Norse before and you remember how they fight: in a wedge, silent, with the shields locked, as if the axe had grown from the arm. Brave men do not fear that wall. Brave men sometimes lose to it.")])

# hidden relays pick the warlord and county, then fire the real event with the scopes attached (or the fallback)
def relay(num, real, fallback_fx, setup=""):
    EVENTS.append(E(num, "", "", "", [], hidden=True, theme="war", trigger="",
                    immediate="eir_bh_pick_effect = yes\n" + setup + """if = {
	limit = { exists = scope:eir_bh_lord }
	trigger_event = eir.%04d
}
else = {
%s
}""" % (real, fallback_fx)))


# 0399: before wave one (a Danegeld payment delays the landing by about three years and costs the prepared edge)
EVENTS.append(E(399, "", "", "", [], hidden=True, theme="war", trigger="",
                immediate="""if = {
	limit = { has_variable = eir_bh_paid }
	remove_variable = eir_bh_paid
	change_variable = { name = eir_bh_prep add = -1 }
	trigger_event = { id = eir.0396 days = 1000 }
}
else = {
	trigger_event = { id = eir.0396 days = 1 }
}"""))
relay(396, 401, "\ttrigger_event = { id = eir.0430 days = 1 }")
relay(398, 404, "\tset_variable = { name = eir_bh_stage value = 4 }\n\ttrigger_event = { id = eir.0407 days = 30 }")
relay(397, 417, "\tset_variable = { name = eir_bh_stage value = 6 }\n\ttrigger_event = { id = eir.0407 days = 30 }")

# =============================================================================
# 0401 THE LONGSHIPS LAND  (wave one)
# =============================================================================
ev(401, "The Longships Land",
   "[eir_bh_lord.GetShortUIName]'s fleet has beached at [eir_target_county.GetName], and the Black Host is ashore.",
   "They came at dawn, in silence, forty ships on the strand and the sound of shields being locked. The fishermen who live there have already fled inland with their children. The monks of the nearest church are carrying their books to the hills.\n\nThere are more of them than you have ever seen in one place.",
   [
       O("Call out every man and meet them on the shore.",
         "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 2 }", PRESTIGE_S,
         "random = {\n\tchance = 15\n\tincrease_wounds_effect = { REASON = fight }\n}",
         st=S_BRAVE, ai=45, ai_mod=[("brave", 20), ("wrathful", 10)]),
       O("Fall back to the ringforts and bleed them in the hills.",
         "scope:eir_target_county = { add_county_modifier = { modifier = eir_scorched_earth_modifier years = 3 } }",
         "add_character_modifier = { modifier = eir_hill_war_modifier years = 3 }", xp("lifestyle_hunter", 15), STRESS_UP,
         gate="OR = {\nmartial >= 10\nhas_trait = patient\nhas_trait = shrewd\n}", st=S_PATIENT, ai=35, ai_mod=[("patient", 15), ("shrewd", 15)]),
       O("Send a champion to challenge their jarl to single combat.",
         luck("t401w", "Their jarl falls, and the host wavers", "scope:eir_bh_lord = { add_character_modifier = { modifier = eir_host_demoralised_modifier years = 2 } }\nadd_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_blademaster value = 25 }",
              "t401l", "Your champion dies, and their cheer carries to the hills", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain\nscope:eir_bh_lord = { add_character_modifier = { modifier = eir_black_host_modifier years = 2 } }",
              p=40, bonus=(25, "prowess >= 16")),
         gate="OR = {\nprowess >= 12\nhas_trait = brave\nhas_trait = lifestyle_blademaster\n}", st=S_BRAVE, ai=20, ai_mod=[("brave", 20)]),
       O("Hire a host of gallowglass out of the Isles.",
         GOLD_M, "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 3\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
         PRESTIGE_S, gate="gold >= 150", st=S_GREED, ai=30),
       O("Carry the relics and the books to a place of safety.",
         PIETY_M, "set_variable = { name = eir_bh_relics_safe value = 1 }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
         xp("lifestyle_mystic", 15), st=S_ZEAL, ai=25, ai_mod=[("zealous", 20)]),
       O("Pray with the monks and wait.",
         PIETY_S, "add_stress = minor_stress_gain", "scope:eir_target_county = { add_county_modifier = { modifier = eir_raided_county_modifier years = 8 } }",
         st=S_ZEAL, ai=5),
   ],
   "war", gate="has_variable = eir_bh_stage", guarded=False, portraits=BH_PORT,
   immediate="""eir_bh_landing_1_effect = yes
set_variable = { name = eir_bh_stage value = 1 }
trigger_event = { id = eir.0402 days = 1100 }
if = {
	limit = { var:eir_bh_prep >= 2 }
	eir_defender_levy_effect = yes
}
if = {
	limit = { has_variable = eir_bh_traitor }
	scope:eir_bh_lord = { add_character_modifier = { modifier = eir_black_host_modifier years = 3 } }
}""",
   variants=[("var:eir_bh_prep >= 2", "They came at dawn, forty ships on the strand, and this time you were not asleep. The beacons took the news from headland to headland in a night, and the riders were already waiting at the fords. [eir_bh_lord.GetShortUIName] had hoped for surprise. He will not have it.\n\nThere are still more of them than you have ever seen in one place.")])

# hidden timeouts: if a wave's war is neither won nor lost in three years, treat it as a draw and carry on
def timeout(num, stage, nxt_stage, nxt_event, days):
    EVENTS.append(E(num, "", "", "", [], hidden=True, theme="war", trigger="",
                    immediate="""if = {
	limit = { var:eir_bh_stage = %d }
	set_variable = { name = eir_bh_stage value = %d }
	trigger_event = { id = eir.%04d days = %d }
}""" % (stage, nxt_stage, nxt_event, days)))


timeout(402, 1, 2, 403, 30)
timeout(395, 3, 4, 407, 30)
timeout(394, 5, 6, 407, 30)

# =============================================================================
# 0403 THE COUNCIL OF THE KINGS
# =============================================================================
ev(403, "The Council of the Kings",
   "Every king in Ireland has been summoned to the hill, and they cannot agree on who goes first.",
   "The Norse have shown the kings what they came for. The kings are not stupid: they have all counted the ships. But a king who sits at another king's council has admitted that the other is his better, and nobody will say the words aloud.\n\nThe poets suggest that the fire in the middle of the circle be set so that nobody sits at its head.",
   [
       O("Appeal to the common blood and the saints.",
         luck("t403w", "The kings swear, and their hosts come", "set_variable = { name = eir_bh_alliance value = 2 }\nadd_character_modifier = { modifier = eir_allied_kings_modifier years = 6 }\nspawn_army = {\n\tlevies = 1500\n\tmen_at_arms = {\n\t\ttype = light_footmen\n\t\tstacks = 2\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_allied_kings_host_name\n}\nadd_prestige = medium_prestige_gain",
              "t403l", "The kings bicker over precedence and half of them leave", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain", p=50, bonus=(20, "diplomacy >= 14")),
         xp("lifestyle_traveler", 10), gate="OR = {\ndiplomacy >= 10\nhas_trait = zealous\nhas_trait = gregarious\n}",
         st=S_ZEAL, ai=40, ai_mod=[("gregarious", 15), ("zealous", 10)]),
       O("Pay each king's hosting with cattle and silver.",
         GOLD_M, "set_variable = { name = eir_bh_alliance value = 2 }", "add_character_modifier = { modifier = eir_allied_kings_modifier years = 4 }",
         "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 6 }", gate="gold >= 150", st=S_GEN, ai=35, ai_mod=[("generous", 20)]),
       O("Remind each king what the Norse will do to his hall.",
         "add_dread = minor_dread_gain", "set_variable = { name = eir_bh_alliance value = 1 }", PRESTIGE_S,
         luck("t403d", "The most stubborn king caves", "add_character_modifier = { modifier = eir_hostile_envoys_modifier years = 3 }\neir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 3 }",
              "t403e", "The kings resent being threatened", "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = -4 }", p=55, bonus=(15, "intrigue >= 12")),
         gate="OR = {\nintrigue >= 10\nhas_trait = callous\nhas_trait = sadistic\n}", st=S_HARD, ai=20, ai_mod=[("callous", 15), ("ambitious", 10)]),
       O("Offer to serve under the strongest king in the circle.",
         "set_variable = { name = eir_bh_alliance value = 2 }", "add_character_modifier = { modifier = eir_allied_kings_modifier years = 6 }", LOSS_S, "add_character_modifier = { modifier = eir_humble_service_modifier years = 4 }",
         st=S_HUMBLE, ai=15, ai_mod=[("humble", 25)]),
       O("Go it alone, and keep your honour.",
         PRESTIGE_M, "add_character_modifier = { modifier = eir_shield_wall_modifier years = 3 }", "add_stress = minor_stress_gain",
         st=S_ARROG, ai=20, ai_mod=[("arrogant", 15), ("brave", 10)]),
   ],
   "court", gate="has_variable = eir_bh_stage", guarded=False,
   immediate="trigger_event = { id = eir.0398 days = 210 }\ntrigger_event = { id = eir.0405 days = 90 }",
   variants=[("has_variable = eir_bh_losses\nvar:eir_bh_losses >= 1", "You have just lost a battle, which concentrates a king's mind wonderfully. They come to the hill in a quiet mood, and some of them have brought their sons. Nobody mentions precedence for nearly an hour.")])

# =============================================================================
# 0404 THE SECOND LANDING  (wave two)
# =============================================================================
ev(404, "The Second Landing",
   "A second fleet has been sighted, and it is larger than the first.",
   "You had begun to hope. The first landing had been beaten, or bled, or bought off, and the country was just starting to count its dead. Then the beacons on the southern headlands burst into flame one after another, and a rider came in with a face the colour of whey.\n\nThe Black Host has more ships than anyone knew.",
   [
       O("Split your army and hold both fords.",
         "add_character_modifier = { modifier = eir_split_command_modifier years = 2 }", PRESTIGE_S, "random = {\n\tchance = 20\n\tincrease_wounds_effect = { REASON = fight }\n}",
         gate="OR = {\nmartial >= 12\nhas_trait = strategist\n}", st=S_BRAVE, ai=35, ai_mod=[("strategist", 20)]),
       O("Raise the country, every sept, every spear.",
         "eir_defender_levy_effect = yes", "eir_defender_levy_effect = yes", GOLD_S, STRESS_UP, "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = -3 }",
         st=S_BRAVE, ai=40, ai_mod=[("brave", 10)]),
       O("Send ships to raid their homeland and draw them back.",
         luck("t404w", "The raiders return home in alarm", "scope:eir_bh_lord = { add_character_modifier = { modifier = eir_host_demoralised_modifier years = 2 } }\nadd_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_traveler value = 25 }",
              "t404l", "Your fleet is lost in a storm off the Isles", "add_prestige = minor_prestige_loss\nremove_short_term_gold = minor_gold_value", p=40, bonus=(20, "has_global_variable = eir_unlock_sea_trade")),
         gate="eir_ports_trigger = { N = 2 }", st=S_BRAVE, ai=15, ai_mod=[("brave", 15)]),
       O("Burn the bridges and flood the bog-roads.",
         "scope:eir_target_county = { add_county_modifier = { modifier = eir_scorched_earth_modifier years = 3 } }", "add_character_modifier = { modifier = eir_hill_war_modifier years = 3 }", xp("lifestyle_hunter", 15),
         "add_stress = minor_stress_gain", st=S_PATIENT, ai=30, ai_mod=[("patient", 15), ("shrewd", 10)]),
       O("Fast on the hilltop, and ask the saints for a sign.",
         PIETY_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", xp("lifestyle_mystic", 20),
         gate="piety >= 100", st=S_ZEAL, ai=25, ai_mod=[("zealous", 20)]),
   ],
   "war", gate="has_variable = eir_bh_stage", guarded=False, portraits=BH_PORT,
   immediate="""eir_bh_landing_2_effect = yes
set_variable = { name = eir_bh_stage value = 3 }
trigger_event = { id = eir.0395 days = 1100 }
trigger_event = { id = eir.0406 days = 75 }""")

# =============================================================================
# 0405 A TRAITOR IN THE HALL
# =============================================================================
ev(405, "A Traitor in the Hall",
   "One of your own has been taking Norse silver.",
   "It started as a rumour: a vassal who sold hides to the Dubliners and came back with Norse coins in his belt. Then a shepherd found a message in the hollow of a stone cross, in a hand your steward recognised. The Norse have been told which fords are guarded and which are not.\n\nThe man in question is at your table tonight, laughing.",
   [
       O("Confront him in front of the whole hall.",
         luck("t405w", "He breaks down and confesses", "scope:eir_traitor = { add_opinion = { target = root modifier = eir_traitor_unmasked_opinion opinion = -30 } }\nadd_prestige = medium_prestige_gain\nadd_hook = { target = scope:eir_traitor type = strong_hook }\neir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 6 }",
              "t405l", "He proves the message was forged, and the hall turns on you", "add_prestige = medium_prestige_loss\nscope:eir_traitor = { add_opinion = { target = root modifier = eir_traitor_unmasked_opinion opinion = -40 } }\nadd_stress = minor_stress_gain",
              p=55, bonus=(15, "intrigue >= 12")),
         st=S_HONEST, ai=35, ai_mod=[("honest", 15), ("just", 10)]),
       O("Have his house watched, and let him dig his own grave.",
         "change_variable = { name = eir_bh_prep add = 1 }", "scope:eir_traitor = { add_opinion = { target = root modifier = eir_traitor_unmasked_opinion opinion = -15 } }", PRESTIGE_S, STRESS_DOWN, gate="OR = {\nintrigue >= 10\nhas_trait = deceitful\nhas_trait = shrewd\n}", st=S_DECEIT, ai=35, ai_mod=[("deceitful", 20), ("shrewd", 10)]),
       O("Buy his loyalty back with a better price.",
         GOLD_M, "add_hook = { target = scope:eir_traitor type = favor_hook }", "scope:eir_traitor = { add_opinion = { target = root modifier = eir_bought_back_opinion opinion = 20 } }",
         PRESTIGE_S, gate="gold >= 120", st=S_GREED, ai=25, ai_mod=[("greedy", 15)]),
       O("Hang him from the nearest oak.",
         "add_dread = medium_dread_gain", "scope:eir_traitor = { death = { death_reason = death_execution killer = root } }", "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -6 }", PRESTIGE_S,
         "eir_trait_effect = { TRAIT = callous OPPOSITE = compassionate CHANCE = 20 }", st=S_HARD, ai=15, ai_mod=[("sadistic", 25), ("callous", 15), ("wrathful", 10)]),
       O("Pardon him in public, and make him your friend.",
         "scope:eir_traitor = { add_opinion = { target = root modifier = eir_bought_back_opinion opinion = 40 } }", "add_hook = { target = scope:eir_traitor type = loyalty_hook }", PRESTIGE_S,
         "eir_trait_effect = { TRAIT = forgiving OPPOSITE = vengeful CHANCE = 25 }", gate="OR = {\nhas_trait = forgiving\nhas_trait = compassionate\nhas_trait = just\n}", st=S_FORGIVE, ai=25, ai_mod=[("forgiving", 20), ("compassionate", 10)]),
   ],
   "intrigue", gate="has_variable = eir_bh_stage\nany_vassal = { is_adult = yes }", guarded=False,
   immediate="random_vassal = {\n\tlimit = { is_adult = yes }\n\tsave_scope_as = eir_traitor\n}",
   portraits="left_portrait = {\n\tcharacter = scope:eir_traitor\n\tanimation = scheme\n}")

# =============================================================================
# 0406 THE MONASTERY IN FLAMES (Black Host edition)
# =============================================================================
ev(406, "The Burning of the Great Monastery",
   "The Black Host has found the greatest monastery on your coast.",
   "The abbot had known for months that this day would come. The books were hidden in the round tower and the relics in a pit beneath the altar. But the Norse have been to a hundred monasteries and they know the shape of the pit. Smoke already rises from the scriptorium.",
   [
       O("Ride to its defence, whatever the cost.",
         luck("t406w", "You arrive in time to save the books", "add_piety = medium_piety_gain\nadd_prestige = medium_prestige_gain\nadd_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }",
              "t406l", "You arrive to find the church already alight", "add_piety = minor_piety_loss\neir_raid_county_effect = yes\nincrease_wounds_effect = { REASON = fight }", p=50, bonus=(20, "martial >= 12")),
         st=S_BRAVE, ai=40, ai_mod=[("brave", 20), ("zealous", 15)]),
       O("Pay the raiders to spare the shrine.",
         GOLD_M, PIETY_S, "eir_raid_county_effect = yes", "add_character_modifier = { modifier = eir_danegeld_modifier years = 2 }",
         gate="gold >= 150", st=S_GREED, ai=20),
       O("Vow vengeance on the altar-stone.",
         "add_character_flag = { flag = eir_vowed_vengeance years = 10 }", "add_dread = minor_dread_gain", PIETY_S, "eir_raid_county_effect = yes",
         st=S_WRATH, ai=30, ai_mod=[("vengeful", 25), ("wrathful", 15)]),
       O("Save the monks and leave the stones to burn.",
         PIETY_M, "eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 25 }", "eir_raid_county_effect = yes", "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }",
         st=S_KIND, ai=35, ai_mod=[("compassionate", 20)]),
   ],
   "faith", gate="has_variable = eir_bh_stage", guarded=False,
   variants=[("has_variable = eir_bh_relics_safe", "The Norse reached the monastery at noon. The abbot met them at the gate, and the pit under the altar was empty. They burned the thatch in rage and went away with a few cattle. The books are in the hills; the monks are praying for you.")])

# =============================================================================
# 0407 THE RECKONING  (hidden: decides the ending)
# =============================================================================
EVENTS.append(E(407, "", "", "", [], hidden=True, theme="war",
                immediate="""if = {
	limit = { var:eir_bh_wins >= 2 }
	trigger_event = { id = eir.0409 days = 10 }
}
else_if = {
	limit = {
		var:eir_bh_stage <= 4
		var:eir_bh_wins < 2
	}
	trigger_event = { id = eir.0397 days = 120 }
}
else_if = {
	limit = { var:eir_bh_wins = 1 }
	trigger_event = { id = eir.0418 days = 20 }
}
else = {
	trigger_event = { id = eir.0414 days = 20 }
}"""))

# =============================================================================
# 0408 THE CAPTIVE JARL
# =============================================================================
ev(408, "The Captive Jarl",
   "Your men have taken a Norse captain alive, and he has asked for you by name.",
   "He is not a king. He is the son of a king, and he has the cold courtesy of a man who has been told since childhood that he will be ransomed. He says his father will pay in silver, in slaves and in ships. He says it as a man who is making a statement of fact, not an offer.\n\nBehind him, your men are muttering about the monasteries.",
   [
       O("Ransom him for a king's price.",
         "add_gold = medium_gold_value", "add_gold = minor_gold_value", PRESTIGE_S, "scope:eir_norse_captain = { add_opinion = { target = root modifier = eir_fair_dealing_opinion opinion = 25 } }",
         st=S_GREED, ai=40, ai_mod=[("greedy", 20)]),
       O("Keep him as a hostage and a guest.",
         "add_hook = { target = scope:eir_norse_captain type = strong_hook }", PRESTIGE_M, "scope:eir_norse_captain = { add_opinion = { target = root modifier = eir_fair_dealing_opinion opinion = 20 } }",
         "add_character_modifier = { modifier = eir_norse_kin_modifier years = 8 }", gate="diplomacy >= 9", st=S_SHREWD, ai=35, ai_mod=[("calm", 15)]),
       O("Let the monks decide what to do with him.",
         PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }", xp("lifestyle_mystic", 20),
         "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }", gate="piety >= 80", st=S_ZEAL, ai=20, ai_mod=[("zealous", 20)]),
       O("Hang him from the round tower.",
         "add_dread = major_dread_gain", "scope:eir_norse_captain = { death = { death_reason = death_execution killer = root } }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -4 }",
         "add_character_modifier = { modifier = eir_raider_infamy_modifier years = 5 }", st=S_HARD, ai=15, ai_mod=[("sadistic", 25), ("vengeful", 20)]),
       O("Free him, with a message for his father.",
         PRESTIGE_M, "scope:eir_norse_captain = { add_opinion = { target = root modifier = eir_fair_dealing_opinion opinion = 40 } }", "add_character_modifier = { modifier = eir_honour_restored_modifier years = 5 }",
         "eir_trait_effect = { TRAIT = honest OPPOSITE = deceitful CHANCE = 20 }", gate="OR = {\nhas_trait = honest\nhas_trait = just\nhas_trait = forgiving\nhas_trait = arrogant\n}", st=S_HONEST, ai=20, ai_mod=[("honest", 15)]),
   ],
   "dungeon", gate="has_variable = eir_bh_stage", guarded=False,
   immediate="""create_character = {
	location = root.capital_province
	age = { 20 32 }
	gender_female_chance = 0
	culture = scope:eir_bh_lord.culture
	faith = scope:eir_bh_lord.faith
	random_traits = yes
	save_scope_as = eir_norse_captain
}""",
   portraits="left_portrait = {\n\tcharacter = scope:eir_norse_captain\n\tanimation = prisondungeon\n}")

# =============================================================================
# 0409 THE BLACK HOST IS BROKEN  (victory)
# =============================================================================
ev(409, "The Black Host Is Broken",
   "The last longship has cleared the headland, and for the first time in a generation the bell can be rung for joy.",
   "They are gone. Not all of them were killed, but enough, and enough of the ships were burned that the rest will have the stories told about them for a hundred years. The poets are already composing, and the monks are already writing, and every king in Ireland is deciding whether to claim a share of the credit.\n\nThey will not get it. You were there.",
   [
       O("Take the name the people are already calling you.",
         "give_nickname = nick_eir_host_breaker", "add_prestige = massive_prestige_gain", "add_character_modifier = { modifier = eir_black_host_broken_modifier years = 25 }",
         "eir_legend_defence_effect = yes", "eir_world_reacts_effect = yes",
         st=S_ARROG, ai=45, ai_mod=[("arrogant", 20), ("ambitious", 15)]),
       O("Raise a cairn and a high cross on the battlefield.",
         PRESTIGE_L, PIETY_L, "scope:eir_target_county ?= { add_county_modifier = { modifier = eir_cairn_county_modifier years = 20 } }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }",
         "eir_legend_defence_effect = yes", st=S_HUMBLE, ai=35, ai_mod=[("humble", 15), ("zealous", 15)]),
       O("Share the spoils among every king who stood with you.",
         PRESTIGE_L, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 15 }", "add_character_modifier = { modifier = eir_allied_kings_modifier years = 10 }",
         "eir_world_reacts_effect = yes", gate="OR = {\nvar:eir_bh_alliance >= 1\nhas_trait = generous\n}", st=S_GEN, ai=35, ai_mod=[("generous", 25)]),
       O("Commission the poets to make a saga of it.",
         PRESTIGE_L, "eir_legend_defence_effect = yes", xp("lifestyle_poet", 40), "eir_make_artifact_effect = { NAME = eir_black_jarl_sword_name DESC = eir_black_jarl_sword_desc TYPE = sword VISUALS = sword MODIFIER = eir_black_jarl_sword_modifier }",
         "eir_legend_title_effect = { TITLE = primary_title }", gate=FILI, st=S_HUMBLE, ai=35, ai_mod=[("ambitious", 10)]),
       O("Follow them to sea, and take what they left.",
         "eir_grant_claims_norse_effect = yes", PRESTIGE_M, "add_dread = minor_dread_gain", "add_character_flag = { flag = eir_oath_to_reclaim years = 15 }",
         st=S_BRAVE, ai=30, ai_mod=[("ambitious", 20), ("brave", 10)]),
   ],
   "legend", guarded=False,
   immediate="""var:eir_bh_lord_var ?= {
	save_scope_as = eir_bh_lord
}
var:eir_bh_lord_var ?= {
	save_scope_as = eir_norse_lord
}
var:eir_bh_county_var ?= {
	save_scope_as = eir_target_county
}
set_global_variable = eir_bh_ended
set_global_variable = eir_black_host_broken
set_global_variable = eir_unlock_norse_bane
set_variable = { name = eir_bh_stage value = 6 }
every_realm_county = {
	limit = { is_coastal_county = yes }
	add_county_modifier = { modifier = eir_norse_bane_country_modifier years = 15 }
}
trigger_event = { id = eir.0416 years = 3 }""",
   variants=[("var:eir_bh_losses >= 1", "You lost a battle, perhaps two, and the country has not forgotten. You also came back, and the Norse did not expect that. The silence on the strand is the sound of a host that has gone home to bury its dead, and the poets' favourite line will be that the Irish were beaten three times and won the war.")])

# =============================================================================
# 0414 THE BLACK HOST TRIUMPHS  (defeat)
# =============================================================================
ev(414, "The Black Host Triumphs",
   "The fighting is over, and the Norse are the lords of your coast.",
   "The longships are drawn up on the strand beneath a fort that used to be yours. The Black Host has taken what it came for: land, silver, hostages, and the right to say who may sail into your harbours. The monks are saying prayers for the dead; the poets are saying nothing.\n\nThere is still a country behind the hills, and it is not at peace with this.",
   [
       O("Accept the terms and pay the tribute.",
         "add_character_modifier = { modifier = eir_danegeld_modifier years = 5 }", "add_character_flag = { flag = eir_paid_danegeld years = 5 }", "add_stress = minor_stress_gain",
         "set_variable = { name = eir_bh_defeated value = 1 }", st="craven = minor_stress_impact_loss\nbrave = minor_stress_impact_gain", ai=30, ai_mod=[("craven", 25)]),
       O("Go into the hills and raise the country in secret.",
         "set_variable = { name = eir_bh_defeated value = 1 }", "add_character_modifier = { modifier = eir_hill_war_modifier years = 8 }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 4 }",
         xp("lifestyle_hunter", 20), st=S_BRAVE, ai=35, ai_mod=[("brave", 15), ("vengeful", 20)]),
       O("Marry a daughter into the Norse royal house.",
         "set_variable = { name = eir_bh_defeated value = 1 }", "add_character_modifier = { modifier = eir_norse_wife_modifier years = 15 }", PRESTIGE_S, "add_character_modifier = { modifier = eir_norse_kin_modifier years = 15 }",
         gate="any_child = { is_female = yes is_adult = yes is_married = no }", st=S_SHREWD, ai=25, ai_mod=[("ambitious", 10), ("shrewd", 10)]),
       O("Write to Rome and the kings of Francia for help.",
         "set_variable = { name = eir_bh_defeated value = 1 }", PIETY_M, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 6 }", PRESTIGE_S,
         gate="piety >= 80", st=S_ZEAL, ai=25, ai_mod=[("zealous", 15)]),
       O("Take the long sea-road into exile and come back stronger.",
         "set_variable = { name = eir_bh_defeated value = 1 }", "add_character_modifier = { modifier = eir_storm_survivor_modifier years = 8 }", xp("lifestyle_traveler", 30), "add_prestige = minor_prestige_loss",
         st=S_BRAVE, ai=10),
   ],
   "dungeon", guarded=False, gate="has_variable = eir_bh_stage",
   immediate="""var:eir_bh_lord_var ?= {
	save_scope_as = eir_bh_lord
}
var:eir_bh_lord_var ?= {
	save_scope_as = eir_norse_lord
}
var:eir_bh_county_var ?= {
	save_scope_as = eir_target_county
}
set_global_variable = eir_bh_ended
set_variable = { name = eir_bh_stage value = 6 }
trigger_event = { id = eir.0415 years = 2 }""")

# =============================================================================
# 0415 THE SETTLERS COME
# =============================================================================
ev(415, "The Settlers Come",
   "Norse families have begun to farm the land that the Black Host took.",
   "They came for silver and they stayed for the grass. The widows sold their holdings, the sons married Irish girls, and a Norse-Gaelic people with two names for everything has begun to settle on the estuaries. The first winter was hard; the second was peaceful.\n\nNobody knows yet whether this is a conquest or a new people.",
   [
       O("Let them stay, and tax them fairly.",
         "capital_county ?= { add_county_modifier = { modifier = eir_ostmen_quarter_modifier years = 20 } }", GAIN_M, PRESTIGE_S, "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 20 }",
         st=S_PATIENT, ai=35, ai_mod=[("just", 15)]),
       O("Foster their sons in your hall, and make Gaels of them.",
         "add_character_modifier = { modifier = eir_foster_bond_modifier years = 12 }", PRESTIGE_S, "set_variable = { name = eir_ostmen_fostered value = 1 }",
         "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 3 }", gate="has_global_variable = eir_done_fosterage", st=S_FORGIVE, ai=35, ai_mod=[("forgiving", 15), ("patient", 10)]),
       O("Drive them out before the roots take.",
         "add_dread = minor_dread_gain", PRESTIGE_S, "eir_raid_county_effect = yes", "eir_trait_effect = { TRAIT = wrathful OPPOSITE = patient CHANCE = 25 }",
         st=S_WRATH, ai=20, ai_mod=[("wrathful", 20), ("sadistic", 15)]),
       O("Set a tribute on every longhouse.",
         GAIN_M, "add_character_modifier = { modifier = eir_cain_tribute_modifier years = 6 }", "capital_county ?= { add_county_modifier = { modifier = eir_ostmen_quarter_modifier years = 8 } }",
         st=S_GREED, ai=30, ai_mod=[("greedy", 20)]),
   ],
   "court", guarded=False, gate="eir_norse_presence_trigger = yes")

# =============================================================================
# 0416 THE SAGA  (echo: three years after the victory)
# =============================================================================
ev(416, "The Saga of the Black Host",
   "A poet has finished the great song of the war, and he has asked to sing it in your hall.",
   "He has put in everything. The beacons, the broken ford, the traitor, the old abbot at the gate. He sings in the old style, with the long breath and the leap. The hall is silent.\n\nHe has also, as poets do, told some of it differently from how it happened.",
   [
       O("Let it be sung as it is, and reward him richly.",
         PRESTIGE_M, "add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 8 }", xp("lifestyle_poet", 25), GOLD_S,
         st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Ask him to put your allies in the song.",
         "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }", PRESTIGE_S, "eir_world_reacts_effect = yes",
         gate="var:eir_bh_alliance >= 1", st=S_HUMBLE, ai=35, ai_mod=[("humble", 15), ("gregarious", 10)]),
       O("Have him sing it truthfully, including the traitor.",
         PRESTIGE_S, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 6 }", "eir_trait_effect = { TRAIT = honest OPPOSITE = deceitful CHANCE = 25 }",
         gate="has_variable = eir_bh_traitor", st=S_HONEST, ai=30, ai_mod=[("honest", 20)]),
       O("Cut the verses that make you look foolish.",
         PRESTIGE_M, "add_character_modifier = { modifier = eir_false_pedigree_modifier years = 5 }", "eir_legend_defence_effect = yes",
         st=S_DECEIT, ai=15, ai_mod=[("arrogant", 20), ("deceitful", 15)]),
   ],
   "legend", guarded=False, gate="eir_bh_beaten_trigger = yes",
   immediate="""var:eir_bh_lord_var ?= {
	save_scope_as = eir_bh_lord
}
var:eir_bh_lord_var ?= {
	save_scope_as = eir_norse_lord
}
var:eir_bh_county_var ?= {
	save_scope_as = eir_target_county
}
""")

# =============================================================================
# 0417 THE GREAT HOSTING OF THE NORTH  (wave three)
# =============================================================================
ev(417, "The Great Hosting of the North",
   "The Black Host has come again, and this time the king himself has sailed.",
   "A hundred and twenty ships, and the banner of a king in the lead. They have burned every beacon from the north coast to the south, and the poets say the sea was black from Skerries to Howth. The jarls who followed the first two waves are dead or ransomed, but the king has not forgotten, and he has no one left to send.\n\nHe is coming himself.",
   [
       O("Summon every sept to the hill and fight to the last man.",
         "eir_defender_levy_effect = yes", "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 3 }", PRESTIGE_M, STRESS_UP,
         st=S_BRAVE, ai=40, ai_mod=[("brave", 20)]),
       O("Challenge the Norse king to single combat before the hosts.",
         luck("t417w", "He accepts, and he falls", "scope:eir_bh_lord = { add_character_modifier = { modifier = eir_host_demoralised_modifier years = 3 } }\nadd_prestige = major_prestige_gain\nadd_trait_xp = { trait = lifestyle_blademaster value = 50 }",
              "t417l", "He accepts, and he does not fall", "add_prestige = minor_prestige_loss\nincrease_wounds_effect = { REASON = fight }\nadd_stress = medium_stress_gain", p=35, bonus=(30, "prowess >= 18")),
         gate="OR = {\nprowess >= 14\nhas_trait = brave\nhas_trait = lifestyle_blademaster\n}", st=S_BRAVE, ai=15, ai_mod=[("brave", 20), ("arrogant", 10)]),
       O("Bring out the relics and march the monks before the army.",
         PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 2 }", xp("lifestyle_mystic", 30),
         gate="piety >= 150", st=S_ZEAL, ai=30, ai_mod=[("zealous", 25)]),
       O("Bribe the jarls beneath the king to turn on him.",
         "remove_short_term_gold = medium_gold_value",
         luck("t417b", "A jarl turns his ships around", "scope:eir_bh_lord = { add_character_modifier = { modifier = eir_host_demoralised_modifier years = 3 } }\nadd_prestige = medium_prestige_gain",
              "t417c", "The bribe is taken and the jarl stays loyal", "add_prestige = minor_prestige_loss", p=45, bonus=(20, "intrigue >= 14")),
         gate="gold >= 200", st=S_DECEIT, ai=25, ai_mod=[("deceitful", 20), ("greedy", 10)]),
       O("Hire every spear on the island.",
         GOLD_M, "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 5\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
         PRESTIGE_S, gate="gold >= 250", st=S_GREED, ai=30),
   ],
   "war", gate="has_variable = eir_bh_stage", guarded=False, portraits=BH_PORT,
   immediate="""eir_bh_landing_3_effect = yes
set_variable = { name = eir_bh_stage value = 5 }
trigger_event = { id = eir.0394 days = 1100 }""")

# =============================================================================
# 0418 THE TREATY OF THE LONGPHORT  (stalemate)
# =============================================================================
ev(418, "The Treaty of the Longphort",
   "Neither side could break the other, and the jarls are asking for terms.",
   "You beat them once. They beat you once. Both of you have counted the dead and the grain. The Norse have a fortified camp at the river-mouth that they call a longphort; you have a country that is slowly starving. A bishop has offered to carry the words.",
   [
       O("Let them keep the longphort and trade through it.",
         "set_variable = { name = eir_norse_enclave value = 1 }", "add_character_modifier = { modifier = eir_longphort_peace_modifier years = 10 }", GAIN_M, PRESTIGE_S,
         st=S_SHREWD, ai=40, ai_mod=[("greedy", 15)]),
       O("Insist on hostages, and give hostages in return.",
         "add_hook = { target = scope:eir_bh_lord type = strong_hook }", PRESTIGE_M, "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 8 }",
         gate="diplomacy >= 10", st=S_PATIENT, ai=30, ai_mod=[("calm", 10)]),
       O("Swear on the relics that the peace will last, and mean it.",
         PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 8 }", "set_variable = { name = eir_norse_enclave value = 1 }",
         gate="piety >= 60", st=S_ZEAL, ai=25, ai_mod=[("zealous", 15)]),
       O("Refuse. This is not over.",
         "set_variable = { name = eir_bh_defeated value = 1 }", "add_character_flag = { flag = eir_oath_to_reclaim years = 15 }", PRESTIGE_S, "add_character_modifier = { modifier = eir_hill_war_modifier years = 6 }",
         st=S_WRATH, ai=15, ai_mod=[("wrathful", 20), ("vengeful", 20)]),
   ],
   "court", guarded=False, gate="has_variable = eir_bh_stage",
   immediate="""var:eir_bh_lord_var ?= {
	save_scope_as = eir_bh_lord
}
var:eir_bh_lord_var ?= {
	save_scope_as = eir_norse_lord
}
var:eir_bh_county_var ?= {
	save_scope_as = eir_target_county
}
set_global_variable = eir_bh_ended
set_variable = { name = eir_bh_stage value = 6 }""", portraits=BH_PORT)

# =============================================================================
# 0430 THE FLEET PASSES  (fallback if there is no Norse warlord in the world)
# =============================================================================
ev(430, "The Fleet Passes",
   "The Black Host sailed south past your coast, and did not land.",
   "You spent a year building beacons, counting spears and sleeping with your boots on. The fleet passed by in the autumn mist, forty miles out, and was gone. The fishermen say it turned towards the English coast; the monks say the saints did it; your steward says the Norse have a long list and Ireland is not at the top of it.\n\nNobody expected to be spared.",
   [
       O("Give thanks to the saints and build a chapel.",
         PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }", st=S_ZEAL, ai=40, ai_mod=[("zealous", 20)]),
       O("Keep the beacons lit. They will come back.",
         PRESTIGE_S, "add_character_modifier = { modifier = eir_beacons_modifier years = 8 }", GOLD_S, st=S_SHREWD, ai=35, ai_mod=[("shrewd", 15)]),
       O("Send raiders after them in the dark.",
         PRESTIGE_M, "add_dread = minor_dread_gain", "random = {\n\tchance = 20\n\tincrease_wounds_effect = { REASON = fight }\n}", st=S_BRAVE, ai=15, ai_mod=[("brave", 20)]),
   ],
   "war", guarded=False, gate="has_variable = eir_bh_stage",
   immediate="""set_global_variable = eir_bh_ended
set_variable = { name = eir_bh_stage value = 6 }""")

# =============================================================================
# 0420 / 0421: a wave is beaten, a wave wins (fired by the war hooks)
# =============================================================================
ev(420, "The Wave Breaks",
   "The Norse host has been beaten and the survivors are running for their ships.",
   "The shield wall held. The Norse had never expected an Irish army to stand, and they discovered it in the same moment that their right flank collapsed. By evening the strand was littered with axes, and the tide was coming in.",
   [
       O("Hunt down their captains.",
         luck("t420w", "A captain is taken alive", "trigger_event = eir.0408\nadd_prestige = minor_prestige_gain",
              "t420l", "The captains reach their ships", "add_prestige = minor_prestige_gain\nadd_stress = miniscule_stress_gain", p=45, bonus=(20, "martial >= 12")),
         gate="OR = {\nmartial >= 8\nhas_trait = brave\n}", st=S_BRAVE, ai=40, ai_mod=[("brave", 15), ("wrathful", 10)]),
       O("Strip the dead of their silver and their arms.",
         GAIN_M, "add_character_modifier = { modifier = eir_norse_spoils_modifier years = 5 }", PRESTIGE_S, st=S_GREED, ai=30, ai_mod=[("greedy", 20)]),
       O("Bury every man, Norse and Irish, with the proper prayers.",
         PIETY_M, PRESTIGE_S, "eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 25 }", "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 3 }",
         st=S_KIND, ai=30, ai_mod=[("compassionate", 20), ("zealous", 10)]),
       O("March the captured standard through every village.",
         PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 3 }", "add_dread = minor_dread_gain",
         st=S_ARROG, ai=30, ai_mod=[("arrogant", 15), ("ambitious", 10)]),
   ],
   "battle", guarded=False, portraits=BH_PORT,
   variants=[("var:eir_bh_stage = 2", "The first landing is over. The Norse had never expected an Irish army to stand, and they discovered it in the same moment that their right flank collapsed. By evening the strand was littered with axes, and the tide was coming in. It would have been a good place to stop. You suspect it is only the beginning."),
             ("var:eir_bh_stage = 4", "The second landing is beaten, and this time the Norse did not run. They fought to the last of their shield-wall and then began to sing. Your men will not forget the sound of it, nor the silence afterwards."),
             ("var:eir_bh_stage = 6", "It is finished. The last Norse standard has fallen in the sea-grass, and the king's ship is limping out to the open water. There is no singing on the strand tonight, only the sound of oars.")],
   immediate="""if = {
	limit = { var:eir_bh_stage = 1 }
	set_variable = { name = eir_bh_stage value = 2 }
	trigger_event = { id = eir.0403 days = 60 }
}
else_if = {
	limit = { var:eir_bh_stage = 3 }
	set_variable = { name = eir_bh_stage value = 4 }
	trigger_event = { id = eir.0407 days = 45 }
}
else_if = {
	limit = { var:eir_bh_stage = 5 }
	set_variable = { name = eir_bh_stage value = 6 }
	trigger_event = { id = eir.0407 days = 45 }
}""")

ev(421, "The Wave Overwhelms You",
   "The Norse have won the field, and the county is theirs.",
   "You were outnumbered, and you knew it, and you stayed anyway. They came up the beach in a wedge, the way they do, and the line broke where they hit it. Now the survivors are in the hills, and the monks are counting what is left.\n\nIt is not over. Not yet.",
   [
       O("Rally the survivors in the hills.",
         "add_character_modifier = { modifier = eir_hill_war_modifier years = 4 }", PRESTIGE_S, xp("lifestyle_hunter", 15), "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 3 }",
         st=S_BRAVE, ai=40, ai_mod=[("brave", 20)]),
       O("Burn the harvest before it can be taken.",
         "scope:eir_target_county ?= { add_county_modifier = { modifier = eir_scorched_earth_modifier years = 3 } }", "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_hill_war_modifier years = 3 }",
         st=S_HARD, ai=25, ai_mod=[("callous", 15)]),
       O("Pay for the hostages' return before they are sold.",
         GOLD_M, PIETY_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 6 }", "eir_trait_effect = { TRAIT = generous OPPOSITE = greedy CHANCE = 20 }",
         gate="gold >= 120", st=S_KIND, ai=30, ai_mod=[("compassionate", 20)]),
       O("Swear vengeance before the saints.",
         "add_character_flag = { flag = eir_vowed_vengeance years = 10 }", PIETY_S, "add_stress = minor_stress_gain", "eir_trait_effect = { TRAIT = vengeful OPPOSITE = forgiving CHANCE = 25 }",
         st=S_WRATH, ai=25, ai_mod=[("vengeful", 25)]),
   ],
   "battle", guarded=False, portraits=BH_PORT,
   variants=[("var:eir_bh_stage = 2", "The first wave has taken the field, and the county with it. You were outnumbered, and you knew it, and you stayed anyway. They came up the beach in a wedge, the way they do, and the line broke where they hit it."),
             ("var:eir_bh_stage = 4", "A second defeat. You are beginning to understand what the poets mean when they say the Norse come in waves, as the sea comes: each one a little further up the shore."),
             ("var:eir_bh_stage = 6", "The Great Hosting has taken the field. The king's banner is planted in the dune, and the jarls are dividing the cattle. You are alive, which is more than many of your friends.")],
   immediate="""if = {
	limit = { var:eir_bh_stage = 1 }
	set_variable = { name = eir_bh_stage value = 2 }
	trigger_event = { id = eir.0403 days = 60 }
}
else_if = {
	limit = { var:eir_bh_stage = 3 }
	set_variable = { name = eir_bh_stage value = 4 }
	trigger_event = { id = eir.0407 days = 45 }
}
else_if = {
	limit = { var:eir_bh_stage = 5 }
	set_variable = { name = eir_bh_stage value = 6 }
	trigger_event = { id = eir.0407 days = 45 }
}""")

# =============================================================================
# THE LESSER INVASIONS (0410-0413 start them, 0422-0429 report their results)
# =============================================================================
def invasion(num, title, summary, body, kind, pick, levies, stacks, name, lord_any, opts_extra, variants=None):
    """a lesser invasion: the war is only launched if the player chooses to fight (or fails to avoid it)"""
    launch = "eir_inv_launch_effect = { KIND = %d LEVIES = %d STACKS = %d NAME = %s }" % (kind, levies, stacks, name)
    opts = [
        O("Meet them at the ford with every spear you have.", launch, "eir_defender_levy_effect = yes", PRESTIGE_S,
          st=S_BRAVE, ai=45, ai_mod=[("brave", 20), ("wrathful", 10)]),
        O("Pay the blood-price and send them home.", GOLD_M, LOSS_S, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 3 }",
          "add_character_flag = { flag = eir_invasion_cd years = 6 }", gate="gold >= 100", st=S_GREED, ai=15, ai_mod=[("craven", 15)]),
    ] + opts_extra
    ev(num, title, summary, body, opts, "war",
       gate="is_at_war = no\nNOT = { has_character_flag = eir_invasion_cd }\n" + lord_any, guarded=False, portraits=INV_PORT,
       immediate=pick + "\nadd_character_flag = { flag = eir_invasion_cd years = 6 }", variants=variants)


def any_ruler_with(culture_lines, extra=""):
    return "any_ruler = {\n\tis_ai = yes\n\tis_ruler = yes\n\thighest_held_title_tier >= tier_county\n\tNOT = { has_truce = root }\n\tNOT = { this = root }\n%s%s}" % (culture_lines, extra)


BRITON_ANY = any_ruler_with("\tculture ?= { has_cultural_pillar = heritage_brythonic }\n")
ALBAN_ANY = any_ruler_with("\tculture ?= { has_cultural_pillar = heritage_goidelic }\n\tNOT = { culture = culture:irish }\n")
RIVAL_ANY = any_ruler_with("\tis_independent_ruler = yes\n\tculture = culture:irish\n")
ISLES_ANY = any_ruler_with("\tculture ?= { has_cultural_pillar = heritage_north_germanic }\n\thighest_held_title_tier <= tier_duchy\n")

invasion(410, "The Britons Land",
         "[eir_inv_lord.GetShortUIName] has landed a war-band from across the sea, claiming an old debt in cattle.",
         "He says the debt is three hundred years old, from a king who raided his grandfather's coast, and that the Irish have never paid it. He says it very politely, in the tongue of the British Church, with an old monk at his elbow to record the claim. Behind him, a hundred men are drawing their boats up the shingle.",
         1, "eir_pick_briton_invader_effect = yes", 1400, 2, "eir_briton_host_name", BRITON_ANY,
         [O("Send the hospitality of a king, and hear his claim out.",
            luck("t410w", "He is satisfied, and sails home as a guest", "add_prestige = medium_prestige_gain\nadd_hook = { target = scope:eir_inv_lord type = favor_hook }\nadd_character_flag = { flag = eir_invasion_cd years = 6 }",
                 "t410l", "He takes your hospitality and your cattle and attacks anyway", "eir_inv_launch_effect = { KIND = 1 LEVIES = 1400 STACKS = 2 NAME = eir_briton_host_name }\nadd_prestige = minor_prestige_loss",
                 p=50, bonus=(25, "diplomacy >= 14")),
            xp("lifestyle_reveler", 15), gate="diplomacy >= 9", st=S_GEN, ai=35, ai_mod=[("gregarious", 20), ("generous", 10)]),
          O("Ask the bishop to judge between you.",
            luck("t410m", "The bishop finds for you", "add_piety = medium_piety_gain\nadd_character_flag = { flag = eir_invasion_cd years = 6 }\nadd_character_modifier = { modifier = eir_peace_with_church_modifier years = 4 }",
                 "t410n", "The bishop finds for him, and the war begins anyway", "eir_inv_launch_effect = { KIND = 1 LEVIES = 1400 STACKS = 2 NAME = eir_briton_host_name }\nadd_piety = minor_piety_loss",
                 p=50, bonus=(20, "piety >= 200")),
            gate="piety >= 60", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)])])

invasion(411, "The Albannach Cattle-Raid",
         "A cousin from across the sea has landed with a war-band, and says the cattle of this coast were promised to his house.",
         "The men of Alba and the men of Ireland share a language, a poet's school and, in the opinion of both, a proper claim to the same grass. The raiders come in at dawn, in a long line, and the first thing they do is take the herds.",
         2, "eir_pick_alban_invader_effect = yes", 1500, 2, "eir_alban_host_name", ALBAN_ANY,
         [O("Remind him that you are one people, and the cattle are his by right of guest.",
            luck("t411w", "He is shamed, and leaves with a gift instead of a victory", "add_prestige = medium_prestige_gain\nadd_character_flag = { flag = eir_invasion_cd years = 6 }\nadd_hook = { target = scope:eir_inv_lord type = favor_hook }",
                 "t411l", "He laughs, and the herds are already half driven away", "eir_inv_launch_effect = { KIND = 2 LEVIES = 1500 STACKS = 2 NAME = eir_alban_host_name }",
                 p=45, bonus=(25, "has_trait = gregarious")),
            gate="OR = {\ndiplomacy >= 10\nhas_trait = gregarious\nhas_trait = honest\n}", st=S_HONEST, ai=35, ai_mod=[("honest", 15)]),
          O("Challenge him to a cattle-judgement before the brehons.",
            luck("t411m", "The brehons find for you", "add_prestige = medium_prestige_gain\nadd_character_flag = { flag = eir_invasion_cd years = 6 }\nadd_character_modifier = { modifier = eir_honour_restored_modifier years = 4 }",
                 "t411n", "The brehons cannot decide, and he refuses to wait", "eir_inv_launch_effect = { KIND = 2 LEVIES = 1500 STACKS = 2 NAME = eir_alban_host_name }",
                 p=50, bonus=(20, "has_global_variable = eir_unlock_brehon_court")),
            gate="learning >= 8", st=S_PATIENT, ai=30, ai_mod=[("just", 15)])])

invasion(412, "The Rival King's Claim",
         "[eir_inv_lord.GetShortUIName] has called out his spears and says a county of yours belongs to his kindred.",
         "It is a very old quarrel, and a very Irish one. His grandfather's grandfather was driven from the hill by yours, and the genealogists on both sides have brought out their rolls. His is longer. Yours is more carefully written. The war will decide which is correct.",
         3, "eir_pick_rival_king_effect = yes", 1000, 2, "eir_rival_host_name", RIVAL_ANY,
         [O("Offer fosterage for his son, and let the quarrel become a friendship.",
            luck("t412w", "He accepts, and the claim is dropped", "add_prestige = medium_prestige_gain\nadd_character_flag = { flag = eir_invasion_cd years = 6 }\nadd_hook = { target = scope:eir_inv_lord type = favor_hook }\nadd_character_modifier = { modifier = eir_foster_bond_modifier years = 10 }",
                 "t412l", "He takes the boy and the war anyway", "eir_inv_launch_effect = { KIND = 3 LEVIES = 1000 STACKS = 2 NAME = eir_rival_host_name }\nadd_prestige = minor_prestige_loss",
                 p=50, bonus=(20, "has_global_variable = eir_done_fosterage")),
            gate="diplomacy >= 8", st=S_FORGIVE, ai=30, ai_mod=[("forgiving", 15), ("patient", 10)]),
          O("Put the genealogy before a poet and let the poet judge.",
            luck("t412m", "The poet finds for you, and the king backs down", "add_prestige = medium_prestige_gain\nadd_character_flag = { flag = eir_invasion_cd years = 6 }\nadd_character_modifier = { modifier = eir_fili_patron_modifier years = 4 }",
                 "t412n", "The poet finds against you", "eir_inv_launch_effect = { KIND = 3 LEVIES = 1000 STACKS = 2 NAME = eir_rival_host_name }\nadd_prestige = minor_prestige_loss",
                 p=45, bonus=(25, "has_global_variable = eir_done_fili")),
            gate="learning >= 9", st=S_HUMBLE, ai=30, ai_mod=[("humble", 10)])])

invasion(413, "Reavers from the Isles",
         "Galleys out of the Hebrides have come ashore, flying a banner you do not know.",
         "They are smaller than a Black Host and meaner. A Norse-Gaelic jarl with a hundred men, hungry for cattle and slaves, has found a beach with no beacon on it. In the old days he would have taken what he wanted and sailed home. These days there is a king in the hills, and he does not know that yet.",
         5, "eir_pick_isles_raider_effect = yes", 900, 1, "eir_isles_reavers_name", ISLES_ANY,
         [O("Burn their galleys while they are ashore.",
            luck("t413w", "The galleys burn, and the raiders are cut off", "add_prestige = medium_prestige_gain\nadd_dread = minor_dread_gain\nadd_character_flag = { flag = eir_invasion_cd years = 6 }",
                 "t413l", "The raiders see the smoke and rally", "eir_inv_launch_effect = { KIND = 5 LEVIES = 900 STACKS = 1 NAME = eir_isles_reavers_name }",
                 p=45, bonus=(25, "intrigue >= 12")),
            gate="OR = {\nintrigue >= 9\nhas_trait = brave\n}", st=S_BRAVE, ai=40, ai_mod=[("brave", 20), ("deceitful", 10)])])

# --- results of the lesser invasions: win / lose pairs (0422-0429)
def result_pair(win, lose, title_w, title_l, sum_w, body_w, sum_l, body_l, grp):
    ev(win, title_w, sum_w, body_w, [
        O("Take a share of the plunder.", GAIN_M, PRESTIGE_S, st=S_GREED, ai=30, ai_mod=[("greedy", 15)]),
        O("Spare the prisoners and send them home with a message.", PRESTIGE_M, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 4 }",
          "eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 20 }", st=S_KIND, ai=35, ai_mod=[("compassionate", 20)]),
        O("Have the poets sing it.", PRESTIGE_M, xp("lifestyle_poet", 20), "add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 4 }", gate=FILI, st=S_HUMBLE, ai=30),
        O("Hang the leaders as an example.", "add_dread = medium_dread_gain", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -2 }",
          st=S_HARD, ai=15, ai_mod=[("sadistic", 25), ("callous", 15)]),
    ], "battle", guarded=False, portraits=INV_PORT)
    ev(lose, title_l, sum_l, body_l, [
        O("Rebuild, and keep a better watch.", GOLD_S, "add_character_modifier = { modifier = eir_beacons_modifier years = 4 }", PRESTIGE_S, st=S_PATIENT, ai=40, ai_mod=[("patient", 15)]),
        O("Swear vengeance on the invader's house.", "add_character_flag = { flag = eir_vowed_vengeance years = 10 }", PIETY_S, "eir_trait_effect = { TRAIT = vengeful OPPOSITE = forgiving CHANCE = 20 }", st=S_WRATH, ai=25, ai_mod=[("vengeful", 25)]),
        O("Pay the blood-price and keep the peace.", GOLD_M, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 4 }", st=S_GREED, ai=20),
        O("Send the monks to ask for mercy for the survivors.", PIETY_M, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }", st=S_ZEAL, ai=25, ai_mod=[("zealous", 15)]),
    ], "war", guarded=False, portraits=INV_PORT)


FILI = "has_global_variable = eir_done_fili"
result_pair(422, 423, "The Britons Withdraw", "The Britons Hold the Coast",
            "The Britons have been driven back to their ships.", "Their prince sailed for home with a third of his men and a lesson about the long memory of the Irish.",
            "The Britons have taken the county, and they intend to keep it.", "They did not stay long, but they stayed long enough to build a hall and bring in a priest. When your army returned, the hall was a fort.", 1)
result_pair(424, 425, "The Albannach Retreat", "The Albans Keep the Herds",
            "The Gaels of Alba have been driven back across the sea.", "Their leader fought well, and everybody agrees on that. He lost, and everybody agrees on that too.",
            "The Albannach have taken the county's herds, and the county with them.", "They did what cousins do: they took the cattle first and asked afterwards.", 2)
result_pair(426, 427, "The Rival King Yields", "The Rival King Wins the Hill",
            "The rival king's spears have been broken, and his claim with them.", "His genealogists will find a reason, in time. For now, the hill is yours.",
            "The rival king has taken the hill, and a county with it.", "The claim was in the genealogy all along. Or so his poets say.", 3)
result_pair(428, 429, "The Reavers Are Broken", "The Reavers Sail Home Rich",
            "The reavers from the Isles have been broken on the strand.", "They had thought the country empty. They discovered otherwise.",
            "The reavers have taken what they came for and gone.", "Their galleys rode low in the water, which is the best tribute to how well they did.", 5)
