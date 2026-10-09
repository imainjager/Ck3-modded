"""v0.7 part B: the kindred, the sea, the Church, cattle and law."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"

# =============================================================================
# THE KINDRED (tanistry politics)
# =============================================================================
ev(310, "The Derbfine Assembles",
   "The adult men of the royal kindred have come to your hall unasked, to talk about who comes after you.",
   "Four generations are in the room: uncles who remember the last king, cousins who remember nothing, and a pair of nephews who have not stopped looking at each other. The law says any of them might be named. The poets have started composing three different laments.",
   [
       O("Name your heir openly before them all.", "add_character_modifier = { modifier = eir_derbfine_counsel_modifier years = 10 }", PRESTIGE_S,
         "primary_heir ?= { add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 15 } }", STRESS_UP,
         gate="exists = primary_heir", st=S_BRAVE, ai=40, ai_mod=[("brave", 10), ("just", 10)]),
       O("Ask the Brehon to rule on the law of the succession.", "add_character_modifier = { modifier = eir_brehon_laws_modifier years = 4 }", PRESTIGE_S,
         "eir_vassal_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 4 }", PIETY_S, gate="has_global_variable = eir_unlock_brehon_court",
         st=S_HONEST, ai=35),
       O("Play the cousins against each other.", "add_character_modifier = { modifier = eir_kin_distrust_modifier years = 6 }",
         luck("t310w", "Each thinks he is your favourite", GAIN_S + "\nadd_prestige = minor_prestige_gain", "t310l", "They compare notes", LOSS_S + "\nadd_stress = minor_stress_gain", p=50, bonus=(15, "intrigue >= 12")),
         st=S_DECEIT, ai=15, ai_mod=[("deceitful", 20), ("paranoid", 15)]),
       O("Send the loudest cousin on pilgrimage.", PIETY_M, "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -3 }", PRESTIGE_S,
         xp("lifestyle_mystic", 10), st=S_ZEAL, ai=30),
       O("Break up the meeting and tell them to go home.", LOSS_S, STRESS_UP, "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -4 }",
         st=S_ARROG, ai=5),
   ],
   "court", gate="eir_collapse_active_trigger = yes\nexists = primary_heir", cooldown=15)

ev(311, "The Blinded Cousin",
   "A cousin with a good claim has been found with his eyes put out, and the court is looking at you.",
   "In the old law a blind man cannot be king, and everyone knows it. He was found in a barn two miles from your hall, and was carried in by a farmer who refuses to say who sent him. He says he knows who did it. He says he will say, if you promise something.",
   [
       O("Swear to find the culprit and take him to justice.", "eir_vassal_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 5 }", PRESTIGE_S, xp("lifestyle_physician", 10),
         STRESS_UP, st=S_HONEST, ai=40, ai_mod=[("just", 20)]),
       O("Offer him honour-price and a place in your household.", GOLD_M, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 6 }", "add_piety = minor_piety_gain",
         st=S_KIND, ai=35, ai_mod=[("compassionate", 20)]),
       O("Hush it up: the realm cannot afford this scandal.", "add_character_modifier = { modifier = eir_kin_distrust_modifier years = 8 }", GAIN_S, LOSS_S,
         st=S_DECEIT, ai=15, ai_mod=[("deceitful", 15)]),
       O("Take the cousin's word and accuse your own rival.", "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -6 }", PRESTIGE_S,
         luck("t311w", "The accused cannot answer", "add_prestige = minor_prestige_gain\nadd_dread = minor_dread_gain", "t311l", "The accusation collapses and the court laughs", "add_prestige = minor_prestige_loss\nadd_character_modifier = { modifier = eir_satirised_modifier years = 3 }", p=45, bonus=(15, "intrigue >= 12")),
         st=S_WRATH, ai=15, ai_mod=[("vengeful", 20), ("wrathful", 15)]),
   ],
   "intrigue", gate="eir_collapse_active_trigger = yes\nany_vassal = { count >= 2 }", cooldown=20)

ev(312, "The Foster-Brother Comes Calling",
   "A man you were raised beside has ridden half the island to ask a favour.",
   "He is thinner than you remember and wears a better cloak than he can afford. At the table he calls you by the name you used when you were nine. The bond of fosterage is stronger than blood, the law says, and he has come to find out how much stronger.",
   [
       O("Give him whatever he asks.", GOLD_M, "add_character_modifier = { modifier = eir_foster_bond_modifier years = 15 }", PRESTIGE_S, xp("lifestyle_reveler", 15),
         st=S_GEN, ai=40, ai_mod=[("generous", 20), ("compassionate", 10)]),
       O("Give him a post at court, and watch him.", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 8 }", PRESTIGE_S, STRESS_UP,
         "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }", st=S_SHREWD, ai=35),
       O("Refuse: a king has no foster-brothers.", LOSS_M, "add_stress = medium_stress_gain", "add_dread = minor_dread_gain",
         st=S_HARD, ai=5, ai_mod=[("callous", 15)]),
       O("Ask what he really wants.", PRESTIGE_S, xp("lifestyle_reveler", 10),
         luck("t312w", "He confesses a debt and asks only for time", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 12 }\nadd_prestige = minor_prestige_gain", "t312l", "He is a spy for your rival", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain", p=65, bonus=(15, "intrigue >= 10")),
         gate="has_global_variable = eir_done_fosterage", st=S_HONEST, ai=30),
   ],
   "family", gate="has_global_variable = eir_done_fosterage", cooldown=15)

ev(313, "A Pedigree Improved",
   "Your chief genealogist has found an ancestor you did not know you had.",
   "He is nine generations back, a king of the north, and the connecting names are very clear in the book. They are, in fact, in the genealogist's own hand, and in ink slightly newer than the vellum. The ancestor would give you a claim that nobody else can match.",
   [
       O("Accept the pedigree, and proclaim it.", PRESTIGE_M, "add_pressed_claim = title:d_ulster", "add_character_modifier = { modifier = eir_false_pedigree_modifier years = 8 }",
         st=S_DECEIT, ai=25, ai_mod=[("deceitful", 20), ("ambitious", 15)]),
       O("Have the genealogist check the sources properly.", xp("lifestyle_poet", 20), PRESTIGE_S, "add_character_modifier = { modifier = eir_fili_patron_modifier years = 4 }",
         gate=FILI, st=S_HONEST, ai=40, ai_mod=[("honest", 15)]),
       O("Pay the genealogist to say nothing and burn the page.", GOLD_S, STRESS_UP, "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }",
         st=S_GREED, ai=20),
       O("Use the pedigree in secret, only in private councils.", PRESTIGE_S,
         luck("t313w", "Nobody checks", "add_prestige = minor_prestige_gain\nadd_legitimacy = minor_legitimacy_gain", "t313l", "A rival poet exposes the fraud", "add_prestige = medium_prestige_loss\nadd_character_modifier = { modifier = eir_false_pedigree_modifier years = 6 }", p=55, bonus=(15, "intrigue >= 12")),
         st=S_DECEIT, ai=25),
   ],
   "learning", gate="NOT = { has_character_modifier = eir_false_pedigree_modifier }", cooldown=25)

ev(314, "The Oath-Breaker",
   "A vassal who swore on the relics has gone over to your enemy.",
   "He was at your table last winter, with his hand on a saint's bone. He has sent a message, politely worded and without apology, saying that the oath was to a different king than the one you have become. The bishops are watching to see whether an oath still means anything.",
   [
       O("Demand the honour-price in front of the court.", PRESTIGE_S, PIETY_S, "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 5 }", STRESS_UP,
         st=S_HONEST, ai=40, ai_mod=[("zealous", 10), ("just", 15)]),
       O("Ride to his hall and take hostages.", "add_dread = minor_dread_gain", PRESTIGE_S, "eir_defender_levy_effect = yes",
         luck("t314w", "He yields before you reach the gate", "add_prestige = minor_prestige_gain", "t314l", "He is ready, and your men are mauled", "add_prestige = minor_prestige_loss\nincrease_wounds_effect = { REASON = fight }", p=55, bonus=(10, "martial >= 12")),
         st=S_WRATH, ai=25, ai_mod=[("wrathful", 15), ("brave", 10)]),
       O("Offer to forgive him if he returns to the fold.", "add_character_modifier = { modifier = eir_honour_restored_modifier years = 6 }", PRESTIGE_S, PIETY_S,
         st=S_FORGIVE, ai=30, ai_mod=[("forgiving", 20)]),
       O("Ask the Church to curse him.", PIETY_M, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = -2 }", "add_dread = minor_dread_gain",
         gate="piety >= 100", st=S_ZEAL, ai=20, ai_mod=[("zealous", 20)]),
   ],
   "court", gate="any_vassal = { count >= 3 }", cooldown=12)

# =============================================================================
# THE SEA
# =============================================================================
ev(320, "Settlers from the Longships",
   "Forty Norse families have beached their ships and want to farm a stretch of your coast.",
   "They are not raiders: there are children, goats and a priest in a cloak of dubious allegiance. They have been driven from somewhere by someone, and they have silver. A reeve says they would double the yield of a county's worst land and that nobody will sleep soundly.",
   [
       O("Let them settle, and tax them.", GAIN_M, "random_held_title = {\n\tlimit = { tier = tier_county is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_settlers_county_modifier years = 15 }\n}",
         PRESTIGE_S, st=S_GREED, ai=40, ai_mod=[("greedy", 15)]),
       O("Let them settle, in exchange for oaths and a hostage each.", "add_character_modifier = { modifier = eir_norse_wife_modifier years = 8 }", PRESTIGE_S,
         "random_held_title = {\n\tlimit = { tier = tier_county is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_settlers_county_modifier years = 12 }\n}",
         gate="diplomacy >= 9", st=S_SHREWD, ai=35),
       O("Drive them off.", "eir_defender_levy_effect = yes", PRESTIGE_S, "add_dread = minor_dread_gain",
         luck("t320w", "They sail away at the sight of the host", "add_prestige = minor_prestige_gain", "t320l", "A Norse captain curses you from the deck", "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 3 }\nadd_stress = minor_stress_gain", p=70),
         st=S_HARD, ai=20),
       O("Have the priest baptise them and take them in.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
         "random_held_title = {\n\tlimit = { tier = tier_county is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_settlers_county_modifier years = 15 }\n}",
         st=S_ZEAL, ai=30),
   ],
   "diplomacy", gate="eir_has_coast_trigger = yes\ncurrent_year < 1100", cooldown=15)

ev(321, "Captives Brought Home",
   "A ship has landed with sixty Irish captives bought back from a Norse slave market.",
   "They are thin and sunburned and some will never speak of what they saw. They were taken from your own coasts, from monasteries, from farms you remember burning. The captain who bought them back wants nothing but the cost of the trip, and the right to say that he did it.",
   [
       O("Pay the captain and settle the captives on good land.", GOLD_M, PRESTIGE_M, PIETY_S, "eir_vassal_opinion_effect = { MODIFIER = eir_rescued_opinion OPINION = 6 }",
         st=S_KIND, ai=40, ai_mod=[("compassionate", 20), ("generous", 10)]),
       O("Take the strongest into your own household.", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 6 }", PRESTIGE_S, STRESS_UP,
         st=S_GREED, ai=20),
       O("Have the priests hear their stories, and write them down.", PIETY_M, xp("lifestyle_mystic", 15), "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
         "eir_legend_title_effect = { TITLE = primary_title }", gate="has_global_variable = eir_unlock_scriptorium", st=S_ZEAL, ai=35),
       O("Use the story to rally the lords against the Norse.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 6 }", STRESS_UP, "add_dread = minor_dread_gain",
         st=S_WRATH, ai=25, ai_mod=[("vengeful", 20)]),
   ],
   "faith", gate="eir_has_coast_trigger = yes\ncurrent_year < 1100", cooldown=20)

ev(322, "A Norse-Gael Bride",
   "A Norse-Gael lord of the coast wants to marry his sister into your house.",
   "She is called Gormlaith or Gormflaith or something very like it depending on whose scribe you ask. She is clever, she reads, and she has been widowed twice. Her brother holds the best harbour on the coast and a hundred ships, and would like a friend who is not also a rival.",
   [
       O("Take her as your own spouse.", "add_character_modifier = { modifier = eir_norse_wife_modifier years = 15 }", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }", STRESS_UP,
         gate="is_married = no", st=S_AMBIT, ai=30),
       O("Marry her to your heir.", "add_character_modifier = { modifier = eir_norse_wife_modifier years = 20 }", PRESTIGE_S, "primary_heir ?= { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 10 } }",
         gate="exists = primary_heir", st=S_SHREWD, ai=40),
       O("Refuse, but offer a foster-son as a pledge of friendship.", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 8 }", PRESTIGE_S, GOLD_S,
         st=S_PATIENT, ai=30),
       O("Refuse flatly.", LOSS_S, "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 4 }", STRESS_DOWN, st=S_ARROG, ai=10),
   ],
   "family", gate="eir_has_coast_trigger = yes\ncurrent_year < 1130", cooldown=20)

ev(323, "Storm off the Skerries",
   "Your ship has lost its mast in a gale, and the crew are drawing lots to see who will be thrown over first.",
   "The coast is ten miles off and invisible. The helmsman is praying in Norse, the monk is praying in Latin, and a very young deckhand is praying in Irish, loudest of all. The water is the colour of lead. Somebody has to decide.",
   [
       O("Pray aloud with the monk and set an example.", PIETY_M, xp("lifestyle_mystic", 20),
         luck("t323w", "The wind dies at dawn", "add_character_modifier = { modifier = eir_storm_survivor_modifier years = 8 }\nadd_prestige = minor_prestige_gain", "t323l", "The ship founders and you swim", "increase_wounds_effect = { REASON = fight }\nadd_prestige = minor_prestige_loss", p=65),
         st=S_ZEAL, ai=40, ai_mod=[("zealous", 20)]),
       O("Take the steering oar yourself.", PRESTIGE_M, STRESS_UP,
         luck("t323bw", "You hold her head to the wind", "add_character_modifier = { modifier = eir_storm_survivor_modifier years = 10 }\nadd_prestige = medium_prestige_gain", "t323bl", "The oar breaks your arm", "increase_wounds_effect = { REASON = fight }\nadd_prestige = minor_prestige_loss", p=50, bonus=(15, "prowess >= 12")),
         gate="prowess >= 8", st=S_BRAVE, ai=30, ai_mod=[("brave", 20)]),
       O("Throw the cargo over and save the people.", GOLD_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_storm_survivor_modifier years = 5 }",
         st=S_KIND, ai=40, ai_mod=[("compassionate", 15)]),
       O("Cut the ropes and let the sea decide.", STRESS_DOWN, LOSS_S,
         luck("t323cw", "The sea takes the mast and spares the ship", "add_prestige = minor_prestige_gain", "t323cl", "The sea takes a man you liked", "add_stress = medium_stress_gain\nadd_prestige = minor_prestige_loss", p=45),
         st=S_CRAVEN, ai=10),
   ],
   "travel", gate="eir_has_coast_trigger = yes", cooldown=15)
