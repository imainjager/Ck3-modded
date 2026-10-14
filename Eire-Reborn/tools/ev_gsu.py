"""Update 5: THE GREAT SAXON UPRISING (disaster, twice per game, 50 years apart).
0900 outbreak, 0901-0903 events in the middle of the disaster (each changes the leaders' strength), 0904/0905 the result of each war,
0910 crushed / 0912 partial / 0913 shattered, 0914 hidden router, 0915 hidden timeout."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

ACTIVE = "has_global_variable = eir_gsu_active"
LEADERS_DOWN = "every_in_list = {\n\tvariable = eir_gsu_leaders\n\tadd_character_modifier = { modifier = eir_host_demoralised_modifier years = %d }\n}"
LEADERS_UP = "every_in_list = {\n\tvariable = eir_gsu_leaders\n\tadd_character_modifier = { modifier = eir_conqueror_emboldened_modifier years = %d }\n}"
ONE_DOWN = "random_in_list = {\n\tvariable = eir_gsu_leaders\n\tadd_character_modifier = { modifier = eir_host_demoralised_modifier years = %d }\n}"

# =============================================================================
# 0900 THE OUTBREAK
# =============================================================================
ev(900, "The Great Saxon Uprising",
   "Every English duchy you hold has risen at once, each under a leader of its own, and the beacons are lit from the Tweed to the Channel.",
   "It was planned for years. A thane in each duchy, a priest to bless it, a brother-in-law with a spare horse. They met at the old stone circles at midsummer and swore, in English, that the island would not be ruled in Gaelic. Each of them seized a county in the night. By the morning there were armies on the roads, and every one of them had the same flag.\n\nYour stewards have counted the leaders. There are a good many.",
   [
       O("Call the hosting and meet them where they stand.", "eir_defender_levy_effect = yes", "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 4 }", PRESTIGE_S,
         st=S_BRAVE, ai=40, ai_mod=[("brave", 20), ("wrathful", 10)]),
       O("Send for the thanes and offer terms before the armies close.",
         luck("g900w", "Several leaders hesitate and their men melt away", LEADERS_DOWN % 2 + "\nadd_prestige = medium_prestige_gain",
              "g900l", "The thanes laugh, and the leaders grow bolder", LEADERS_UP % 2 + "\nadd_prestige = minor_prestige_loss", p=40, bonus=(25, "diplomacy >= 14")),
         gate="OR = {\ndiplomacy >= 11\nhas_trait = gregarious\nhas_trait = just\n}", st=S_FORGIVE, ai=25, ai_mod=[("forgiving", 15), ("gregarious", 10)]),
       O("Rally the loyal English lords and set them against the rebels.", "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 6 }",
         "add_character_modifier = { modifier = eir_allied_kings_modifier years = 4 }", "spawn_army = {\n\tlevies = 1800\n\tmen_at_arms = {\n\t\ttype = light_footmen\n\t\tstacks = 3\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_allied_kings_host_name\n}",
         st=S_SHREWD, ai=40, ai_mod=[("shrewd", 15), ("gregarious", 10)]),
       O("Hire every spear in the Isles.", "remove_short_term_gold = 400", "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 8\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
         PRESTIGE_S, gate="gold >= 400", st=S_GREED, ai=30),
       O("Order the bishops to preach against rebellion.", PIETY_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", LEADERS_DOWN % 1, xp("lifestyle_mystic", 20),
         gate="piety >= 100", st=S_ZEAL, ai=25, ai_mod=[("zealous", 25)]),
   ],
   "war", guarded=False, gate="eir_gsu_ready_trigger = yes", immediate="eir_gsu_start_effect = yes",
   variants=[("has_global_variable = eir_gsu_done_1\nhas_global_variable = eir_gsu_done_2",
              "You thought it was over. You had put the thanes down, hung the leaders and pardoned the sons, and the Church had called it a settled peace. The sons are grown. The old stone circles were visited again at midsummer, and again every duchy rose together, with better organisation and a longer memory.\n\nThey are calling it the Second Rising. They are not calling it a last one.")])

# =============================================================================
# 0901-0903: IN THE MIDDLE OF THE DISASTER (each one changes the leaders' strength)
# =============================================================================
ev(901, "The Beacons of Wessex",
   "The first campaign is under way, and the English are lighting beacons to call every hamlet to the colours.",
   "From the hills above Winchester you can count nine. They burn in a line to the coast. Each has a priest and a reeve beside it who have promised, by a wooden cross, that when the fire is lit they will send their men. The fires are the leaders' best weapon. They are also the only thing that stops the English from being a hundred villages.",
   [
       O("Proclaim a pardon for any man who lays down arms by Michaelmas.",
         luck("g901w", "Whole hundreds come in with their spears reversed", LEADERS_DOWN % 2 + "\nadd_prestige = medium_prestige_gain\neir_trait_effect = { TRAIT = forgiving OPPOSITE = vengeful CHANCE = 25 }",
              "g901l", "The pardon is read in the market and torn up", LEADERS_UP % 1 + "\nadd_prestige = minor_prestige_loss", p=50, bonus=(20, "diplomacy >= 13")),
         st=S_FORGIVE, ai=35, ai_mod=[("forgiving", 20), ("just", 10)]),
       O("Send agents to buy the reeves.", "remove_short_term_gold = 250", LEADERS_DOWN % 1, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }",
         gate="OR = {\nintrigue >= 10\nhas_trait = deceitful\nhas_trait = greedy\n}", st=S_DECEIT, ai=35, ai_mod=[("deceitful", 15), ("greedy", 10)]),
       O("Hang the watchmen and burn the beacons.", "add_dread = major_dread_gain", PRESTIGE_S, "add_character_modifier = { modifier = eir_hard_hand_modifier years = 8 }", "change_variable = { name = eir_resent add = 1 }",
         st=S_HARD, ai=15, ai_mod=[("sadistic", 25), ("callous", 15)]),
       O("Strengthen every garrison and sit tight.", "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 3 }", GOLD_S,
         st=S_PATIENT, ai=30, ai_mod=[("patient", 15)]),
   ],
   "war", guarded=False, gate=ACTIVE)

ev(902, "Treachery in the Rebel Camp",
   "Not every English leader is quite as loyal to the English as he says.",
   "It begins with a letter, as treachery does. A captain of one of the rebel hosts has written to say that his lord has been promised an earldom by the English crown if he wins, and nothing at all if he does not. A second captain has copied the letter. A third has asked for a safe-conduct. The camps are buzzing with rumour, and one of the rumours is true.",
   [
       O("Bribe the captains and have them leave before the next battle.",
         luck("g902w", "Two captains take the silver and their men follow them", ONE_DOWN % 3 + "\nremove_short_term_gold = 200\nadd_prestige = minor_prestige_gain",
              "g902l", "The captains take the silver and sell the news to their lord", "remove_short_term_gold = 200\n" + LEADERS_UP % 1, p=50, bonus=(25, "intrigue >= 13")),
         gate="gold >= 200", st=S_GREED, ai=35, ai_mod=[("greedy", 15), ("deceitful", 15)]),
       O("Forge a letter that sets two leaders against each other.",
         luck("g902f", "The leaders quarrel and one withdraws his men", ONE_DOWN % 4 + "\n" + ONE_DOWN % 2 + "\nadd_prestige = medium_prestige_gain",
              "g902g", "The forgery is spotted and the rebels rally", LEADERS_UP % 2 + "\nadd_prestige = minor_prestige_loss", p=40, bonus=(30, "intrigue >= 15")),
         gate="OR = {\nintrigue >= 12\nhas_trait = deceitful\n}", st=S_DECEIT, ai=25, ai_mod=[("deceitful", 25)]),
       O("Offer the strongest leader a county of his own to change sides.", GOLD_S, LOSS_S, ONE_DOWN % 5, "add_character_modifier = { modifier = eir_fair_lord_modifier years = 3 }",
         st=S_SHREWD, ai=30, ai_mod=[("shrewd", 15), ("ambitious", 10)]),
       O("Ignore the rumours. A man who wins does not need spies.", STRESS_DOWN, PRESTIGE_S, st=S_ARROG, ai=15, ai_mod=[("arrogant", 15), ("lazy", 10)]),
   ],
   "intrigue", guarded=False, gate=ACTIVE)

ev(903, "The Council at Winchester",
   "The rebel leaders have met at last, and they have chosen a single captain to speak for all of them.",
   "It took them a year and a half to do what the Irish kings have never done. They sat in the old hall at Winchester, nine men and a woman who had brought her father's sword, and they agreed that if they hang separately they will hang together. They have chosen a marshal. They have chosen a day. The next battle will be a battle between two armies, not an army and a mob.",
   [
       O("Strike the council before the marshal can organise it.",
         luck("g903w", "You catch the council in the hall and the alliance breaks", LEADERS_DOWN % 3 + "\nadd_prestige = major_prestige_gain\nadd_trait_xp = { trait = lifestyle_blademaster value = 30 }",
              "g903l", "The council has moved, and your column walks into a prepared ground", "add_prestige = medium_prestige_loss\nincrease_wounds_effect = { REASON = fight }\n" + LEADERS_UP % 2, p=40, bonus=(25, "martial >= 15")),
         gate="OR = {\nmartial >= 12\nhas_trait = brave\n}", st=S_BRAVE, ai=30, ai_mod=[("brave", 20)]),
       O("Parley with the marshal and offer a new charter of English rights.",
         luck("g903p", "The marshal accepts a truce on the field", LEADERS_DOWN % 2 + "\neir_resent_clear_effect = yes\nadd_character_modifier = { modifier = eir_two_peoples_modifier years = 10 }\nadd_prestige = medium_prestige_gain",
              "g903q", "The charter is not enough", "add_prestige = minor_prestige_loss", p=45, bonus=(25, "diplomacy >= 15")),
         gate="diplomacy >= 10", st=S_PATIENT, ai=30, ai_mod=[("patient", 15), ("just", 10)]),
       O("Burn the shires the council is meeting in.", "add_dread = major_dread_gain", "random_sub_realm_county = {\n\tlimit = { eir_foreign_britain_county_trigger = yes }\n\tadd_county_modifier = { modifier = eir_scorched_earth_modifier years = 3 }\n}",
         LEADERS_DOWN % 2, LOSS_S, st=S_HARD, ai=20, ai_mod=[("sadistic", 20), ("callous", 15)]),
       O("Hire a second company and call the Gaelic kings.", "remove_short_term_gold = 500", "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 10\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
         "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 5 }", gate="gold >= 500", st=S_SHREWD, ai=35),
   ],
   "war", guarded=False, gate=ACTIVE,
   immediate=LEADERS_UP % 3)

# =============================================================================
# 0904 / 0905: THE RESULT OF EACH WAR
# =============================================================================
ev(904, "A Duchy Holds",
   "The rising in [eir_up_duchy.GetName] has been put down, and its leader is in your hands.",
   "He was not a bad commander. He had a good position and a strong army, and he lost it by a day's march. He is thirty, with a broken nose and a family. The counties of the duchy are quiet again, and quiet in a way that suggests they have learned something.",
   [
       O("Hang him from the nearest oak as an example.", "add_dread = major_dread_gain", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -2 }",
         st=S_HARD, ai=20, ai_mod=[("sadistic", 25), ("callous", 20)]),
       O("Pardon him, take his sons as fosterlings and put him on your council.", PRESTIGE_M, "add_character_modifier = { modifier = eir_saxon_amnesty_modifier years = 8 }", "eir_resent_clear_effect = yes",
         "eir_trait_effect = { TRAIT = forgiving OPPOSITE = vengeful CHANCE = 25 }", gate="OR = {\nhas_trait = forgiving\nhas_trait = compassionate\nhas_trait = just\ndiplomacy >= 11\n}",
         st=S_FORGIVE, ai=30, ai_mod=[("forgiving", 25), ("compassionate", 15)]),
       O("Ransom him back to his family for a king's price.", "add_gold = medium_gold_value", PRESTIGE_S, "add_character_modifier = { modifier = eir_norse_spoils_modifier years = 3 }",
         st=S_GREED, ai=35, ai_mod=[("greedy", 20)]),
   ],
   "battle", guarded=False)

ev(905, "A Duchy Falls to the Saxons",
   "[eir_up_duchy.GetName] has gone over to the rebels, and its counties are burning.",
   "It is the sort of thing the English do very well, once they decide to. The hall has been taken, the mills burned for fuel, the churches stripped of their silver and the thane's household turned out into the lane. The people are being taught to answer in English. A good many are being taught it with a spear at their back.",
   [
       O("Swear before the saints to take it back.", "add_character_flag = { flag = eir_oath_to_reclaim years = 15 }", "add_character_flag = { flag = eir_vowed_vengeance years = 15 }", "add_character_modifier = { modifier = eir_hill_war_modifier years = 6 }",
         PIETY_S, st=S_WRATH, ai=40, ai_mod=[("vengeful", 25), ("brave", 10)]),
       O("Ransom your captured vassals before they are sold.", "remove_short_term_gold = medium_gold_value", PIETY_S, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 6 }", "eir_trait_effect = { TRAIT = generous OPPOSITE = greedy CHANCE = 20 }",
         gate="gold >= 150", st=S_KIND, ai=30, ai_mod=[("compassionate", 20), ("generous", 15)]),
       O("Pull the garrisons back and hold what remains.", "eir_defender_levy_effect = yes", STRESS_DOWN, "add_character_modifier = { modifier = eir_shield_wall_modifier years = 3 }",
         st=S_PATIENT, ai=30, ai_mod=[("patient", 15), ("craven", 10)]),
   ],
   "war", guarded=False)

# =============================================================================
# THE END: crushed / partial / shattered
# =============================================================================
ev(910, "The Saxons Are Crushed",
   "Every rebel host in England has been broken, and the Great Saxon Uprising is over.",
   "The last of them surrendered on a hill above the Thames at the end of a wet October. The marshal of the council gave up his sword himself. The thanes are in your hands, the rebel duchies have come home, and the English have discovered that a king who wins every war can afford to be generous. The question is how generous.",
   [
       O("Take the name the army is calling you.", "give_nickname = nick_eir_saxon_breaker", "add_character_modifier = { modifier = eir_saxon_subdued_modifier years = 40 }", PRESTIGE_L, "eir_legend_title_effect = { TITLE = title:k_england }",
         st=S_ARROG, ai=40, ai_mod=[("arrogant", 20), ("ambitious", 15)]),
       O("Hold a Moot of Reconciliation at Winchester and pardon the rest.", PRESTIGE_M, "add_character_modifier = { modifier = eir_saxon_amnesty_modifier years = 15 }", "eir_resent_clear_effect = yes",
         "add_character_modifier = { modifier = eir_two_peoples_modifier years = 15 }", "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 30 }",
         st=S_FORGIVE, ai=35, ai_mod=[("just", 20), ("forgiving", 15)]),
       O("Grant the rebel lands to the thanes who stayed loyal.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 8 }", "add_character_modifier = { modifier = eir_saxon_subdued_modifier years = 20 }", GOLD_S,
         st=S_GEN, ai=30, ai_mod=[("generous", 20)]),
       O("Raise a minster at the hill, with an altar for the dead of both sides.", PIETY_L, PRESTIGE_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }", "eir_resent_clear_effect = yes", xp("lifestyle_mystic", 30),
         st=S_ZEAL, ai=25, ai_mod=[("zealous", 25)]),
   ],
   "legend", guarded=False)

ev(912, "The Rising Is Put Down, At a Price",
   "The Great Saxon Uprising is over. Some duchies are yours again and some are not.",
   "It will be called a draw in the English chronicles and a victory in the Irish. Neither is wrong. The strongest of the rebel leaders won his duchy and kept it. The weakest are dead. The country between is a patchwork of burned villages and brand-new castles. There is a peace, signed by tired men on both sides.",
   [
       O("Consolidate what you hold and fortify the border.", "eir_defender_levy_effect = yes", PRESTIGE_S, "add_character_modifier = { modifier = eir_beacons_modifier years = 8 }", GOLD_S,
         st=S_SHREWD, ai=40, ai_mod=[("shrewd", 15), ("patient", 10)]),
       O("Promise to come back for the lost duchies.", "add_character_flag = { flag = eir_oath_to_reclaim years = 20 }", PRESTIGE_S, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_hill_war_modifier years = 6 }",
         st=S_WRATH, ai=30, ai_mod=[("vengeful", 20), ("ambitious", 15)]),
       O("Offer the rebels a lasting treaty of English rights.", PRESTIGE_M, "add_character_modifier = { modifier = eir_two_peoples_modifier years = 12 }", "eir_resent_clear_effect = yes", GOLD_S,
         gate="diplomacy >= 10", st=S_FORGIVE, ai=30, ai_mod=[("just", 15)]),
       O("Rebuild, and say as little as possible.", "add_character_modifier = { modifier = eir_conq_resolve_modifier years = 8 }", PRESTIGE_S, STRESS_DOWN,
         st=S_CONTENT, ai=25, ai_mod=[("content", 15)]),
   ],
   "court", guarded=False)

ev(913, "The Saxons Shatter Your Hold",
   "Most of England has gone over to the rebels, and the throne is in danger.",
   "The chroniclers call it the worst year of your reign. The duchies fell one after another, each to a leader nobody had heard of two years before. The English have not been so united since Alfred. They did it with ten thousand spears, a priest and a grievance, and the worst of it is that the grievance was a good one.",
   [
       O("Rebuild from the ground up. Every mill, every church, every ford.", "add_character_modifier = { modifier = eir_conq_resolve_modifier years = 12 }", "add_character_flag = { flag = eir_vowed_rebuild years = 12 }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 5 }",
         st=S_PATIENT, ai=40, ai_mod=[("diligent", 15), ("patient", 15)]),
       O("Withdraw to Ireland and Scotland and mass for the counter-stroke.", "add_character_flag = { flag = eir_oath_to_reclaim years = 20 }", "add_character_modifier = { modifier = eir_hill_war_modifier years = 8 }", xp("lifestyle_hunter", 30),
         st=S_BRAVE, ai=30, ai_mod=[("brave", 20), ("vengeful", 15)]),
       O("Pay the English what they ask and keep a corner of the island.", "remove_short_term_gold = 600", PRESTIGE_S, "add_character_modifier = { modifier = eir_saxon_shaken_modifier years = 10 }", STRESS_UP,
         gate="gold >= 600", st="brave = minor_stress_impact_gain\ncraven = minor_stress_impact_loss", ai=10, ai_mod=[("craven", 25)]),
       O("Send the relics and the books west and wait for a better day.", PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }", xp("lifestyle_mystic", 20),
         gate="piety >= 100", st=S_ZEAL, ai=20, ai_mod=[("zealous", 25)]),
   ],
   "dungeon", guarded=False, immediate="add_character_modifier = { modifier = eir_saxon_shaken_modifier years = 8 }")

# =============================================================================
# hidden: the router and the timeout
# =============================================================================
EVENTS.append(E(914, "", "", "", [], hidden=True, theme="war", trigger="",
                immediate="""if = {
	limit = { has_global_variable = eir_gsu_active }
	remove_global_variable = eir_gsu_active
	if = {
		limit = { var:eir_gsu_losses = 0 }
		trigger_event = eir.0910
	}
	else_if = {
		limit = { var:eir_gsu_wins >= var:eir_gsu_losses }
		trigger_event = eir.0912
	}
	else = {
		trigger_event = eir.0913
	}
	clear_variable_list = eir_gsu_leaders
}"""))
EVENTS.append(E(915, "", "", "", [], hidden=True, theme="war", trigger="",
                immediate="""if = {
	limit = { has_global_variable = eir_gsu_active }
	trigger_event = eir.0914
}"""))
