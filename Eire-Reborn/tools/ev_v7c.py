"""v0.7 part C: the Church, cattle and law, war, the Celtic neighbours, the court and the legends."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"

# =============================================================================
# THE CHURCH
# =============================================================================
ev(330, "A Relic Comes from Iona",
   "A monk from Iona has crossed the sea with a scrap of Colmcille's cloak in a silver box.",
   "The island has been raided three times in his lifetime, and the community has decided that the saint's belongings are no longer safe in the one place the Norse know to look. He asks only that you keep it in a church where the bell is rung at the right hours, and that the cloak never be sold.",
   [
       O("Receive it with honour and keep it in your chapel.", PIETY_L, "eir_make_artifact_effect = { NAME = eir_iona_reliquary_name DESC = eir_iona_reliquary_desc TYPE = goblet VISUALS = goblet MODIFIER = eir_iona_reliquary_modifier }",
         "add_character_modifier = { modifier = eir_iona_relic_modifier years = 15 }", xp("lifestyle_mystic", 25),
         st=S_ZEAL, ai=40, ai_mod=[("zealous", 20)]),
       O("Give it to the largest monastery in your lands.", PIETY_M, PRESTIGE_S, "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_monastery_county_modifier years = 25 }\n}",
         "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }", st=S_HUMBLE, ai=35),
       O("Parade it around the realm to bless the harvest.", PIETY_S, PRESTIGE_M,
         luck("t330w", "A good harvest follows", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_cattle_drive_modifier years = 5 }\n}", "t330l", "Rain falls on the procession and the crops rot", "add_piety = minor_piety_loss\nadd_prestige = minor_prestige_loss", p=60),
         st=S_ARROG, ai=25),
       O("Keep it safe, but say nothing.", PIETY_S, STRESS_DOWN, "add_character_modifier = { modifier = eir_iona_relic_modifier years = 6 }",
         st=S_PATIENT, ai=20),
   ],
   "faith", gate="piety >= 150\nhas_global_variable = eir_unlock_round_tower", cooldown=25)

ev(331, "The Monk Who Disagreed",
   "A learned monk has been preaching that the Easter reckoning of the Roman Church is a heresy, and that the Irish dating is the true one.",
   "He is not wrong about the dates, which have been argued for two hundred years. He is, however, very loud about it, and the new bishops want him silenced. Half the abbots in your lands quietly agree with him.",
   [
       O("Silence him, and protect the unity of the Church.", PIETY_M, "add_character_modifier = { modifier = eir_heresy_hunter_modifier years = 8 }", "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -3 }",
         gate="piety >= 100", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
       O("Hold a synod where both sides may argue.", PIETY_S, PRESTIGE_M, xp("lifestyle_mystic", 15), STRESS_UP,
         gate="learning >= 9", st=S_FORGIVE, ai=40, ai_mod=[("patient", 10), ("forgiving", 10)]),
       O("Side with the monk, and defend the old ways.", "add_character_modifier = { modifier = eir_easter_rift_modifier years = 10 }", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_gael_pride_opinion OPINION = 6 }",
         st=S_CYN, ai=20, ai_mod=[("stubborn", 15)]),
       O("Send him on pilgrimage to Rome to settle it himself.", PIETY_S, PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 2 }",
         st=S_SHREWD, ai=35),
   ],
   "faith", gate="piety >= 100", cooldown=20)

ev(332, "The Pilgrims Arrive",
   "A hundred pilgrims have walked into your capital, singing, and the monastery cannot feed them.",
   "They are from Britain and Gaul, in grey cloaks, with staves. They want to walk the pilgrim's road to Croagh Patrick and Skellig. They say the Irish roads are the safest in the world, and they are asking whether it is still true.",
   [
       O("Feed them from your own table.", GOLD_M, PIETY_M, PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 5 }", xp("lifestyle_reveler", 15),
         st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Give them an escort and a safe-conduct.", GOLD_S, PRESTIGE_S, PIETY_S,
         "add_character_modifier = { modifier = eir_pilgrim_modifier years = 4 }", st=S_SHREWD, ai=35),
       O("Charge a toll at the ford.", GAIN_M, LOSS_S, STRESS_UP,
         st=S_GREED, ai=15, ai_mod=[("greedy", 20)]),
       O("Ask them to carry your name to the churches of Britain.", PRESTIGE_M, "add_character_modifier = { modifier = eir_missionary_glory_modifier years = 4 }", PIETY_S,
         gate="has_global_variable = eir_done_cashel", st=S_AMBIT, ai=35),
   ],
   "faith", gate="piety >= 100", cooldown=15)

# =============================================================================
# CATTLE, LAW AND THE SEASONS
# =============================================================================
ev(340, "A Man Fasts at the Door",
   "A freeman is sitting on your threshold, refusing food, until you pay a debt you owe him.",
   "It is the ancient remedy called distraint by fasting, and the law is clear: a lord who lets a man starve at his door, over a debt, loses his honour-price. The man is quiet and does not beg. The debt, you find, is real, and is eleven years old.",
   [
       O("Pay the debt in full and give him a feast.", GOLD_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_fasting_justice_modifier years = 8 }", "eir_court_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 4 }",
         st=S_HONEST, ai=40, ai_mod=[("just", 20), ("honest", 10)]),
       O("Fast beside him until the Brehon decides.", PIETY_S, PRESTIGE_M, xp("lifestyle_mystic", 15), STRESS_UP, "add_stress = minor_stress_gain",
         gate="has_global_variable = eir_unlock_brehon_court", st=S_HUMBLE, ai=25, ai_mod=[("humble", 20), ("zealous", 10)]),
       O("Haggle: pay half, and swear the rest to be paid by Easter.", GOLD_S, PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 2 }",
         st=S_GREED, ai=30),
       O("Have him carried off the threshold.", LOSS_M, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_satirised_modifier years = 3 }",
         st=S_HARD, ai=5, ai_mod=[("callous", 15), ("arrogant", 10)]),
   ],
   "court", cooldown=15)

ev(341, "The Murrain Comes",
   "A sickness is going through the herds, and the cattle are dying in the byres.",
   "The first cows died in the west and the disease went east along the cattle roads. Farmers are burning carcasses and praying. A Welsh dealer has come across the sea with healthy beasts and a high price. The poorest freemen have already begun to sell their land.",
   [
       O("Buy cattle for the poorest from the Welsh dealer.", GOLD_M, "add_character_modifier = { modifier = eir_fair_lord_modifier years = 5 }", PRESTIGE_S,
         "eir_vassal_opinion_effect = { MODIFIER = eir_wergild_paid_opinion OPINION = 5 }", st=S_GEN, ai=40, ai_mod=[("generous", 20), ("compassionate", 15)]),
       O("Order the herds burned and the infected fields left fallow.", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_murrain_modifier years = 4 }\n}", PRESTIGE_S, STRESS_UP,
         "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -3 }", st=S_HARD, ai=30),
       O("Ask the saints, and carry the relics through the fields.", PIETY_M, xp("lifestyle_mystic", 15),
         luck("t341w", "The sickness fades by midsummer", "add_prestige = minor_prestige_gain\nadd_piety = minor_piety_gain", "t341l", "The sickness spreads into the next county", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_murrain_modifier years = 6 }\n}", p=45),
         gate="piety >= 80", st=S_ZEAL, ai=30),
       O("Close the borders and let the sickness burn itself out.", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_murrain_modifier years = 5 }\n}", GAIN_S, LOSS_S,
         st=S_PATIENT, ai=15),
   ],
   "court", gate="eir_stage1_trigger = yes", cooldown=15)

ev(342, "The Great Cattle Drive",
   "Every herd in your lands is going to the autumn market together, and your reeve asks whether the king will ride with them.",
   "It is the biggest drive in a generation: eleven thousand head, forty drovers, a priest to bless the ford and a poet to compose a verse about each. The roads are narrow and the Welsh raiders are rumoured. The market at the end is worth a fortune.",
   [
       O("Ride at the head of the drive.", PRESTIGE_M, xp("lifestyle_reveler", 20), STRESS_UP,
         luck("t342w", "The herds reach market whole", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_cattle_drive_modifier years = 6 }\n}\nadd_gold = medium_gold_value", "t342l", "Raiders cut out a thousand head", "add_prestige = minor_prestige_loss\nincrease_wounds_effect = { REASON = fight }", p=60, bonus=(15, "prowess >= 12")),
         gate="prowess >= 8", st=S_BRAVE, ai=40),
       O("Send an armed escort and stay home.", GOLD_S, "eir_defender_levy_effect = yes", GAIN_M, PRESTIGE_S,
         st=S_SHREWD, ai=40),
       O("Sell the cattle where they stand and spare the risk.", GAIN_M, LOSS_S, STRESS_DOWN, st=S_GREED, ai=25),
       O("Hold a feast at the market and invite the Welsh dealers.", GOLD_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 4 }", xp("lifestyle_reveler", 15),
         st=S_GEN, ai=30),
   ],
   "court", gate="has_global_variable = eir_unlock_cattle_enclosure\neir_stage1_trigger = yes", cooldown=10)

ev(343, "A Quarrel in the Summer Pastures",
   "Two clans have met on the same hill pasture, and neither will leave first.",
   "The booleys have gone up the mountains for the summer with the herds and the dairymaids. The pasture is common land by law and nobody can remember which clan came first. There are ten boys on each side, a bad-tempered bull and a brehon three days away.",
   [
       O("Ride up and judge it yourself.", PRESTIGE_S, "add_character_modifier = { modifier = eir_fasting_justice_modifier years = 4 }", STRESS_UP,
         "eir_court_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 3 }", gate="learning >= 8", st=S_HONEST, ai=40, ai_mod=[("just", 20)]),
       O("Divide the pasture and put a stone marker between them.", GOLD_S, PRESTIGE_S, "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_booley_county_modifier years = 10 }\n}",
         st=S_PATIENT, ai=35),
       O("Make both clans pay a fine for the trouble.", GAIN_M, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -3 }",
         st=S_GREED, ai=20),
       O("Join the herdsmen for the summer yourself.", "add_character_modifier = { modifier = eir_booley_modifier years = 3 }", PRESTIGE_S, STRESS_DOWN, PIETY_S,
         st=S_CONTENT, ai=25, ai_mod=[("content", 15)]),
   ],
   "court", gate="eir_stage1_trigger = yes", cooldown=10)

ev(344, "The Harper Who Was Not Paid",
   "A harper played all night at your feast, and your steward gave him a cup of ale and a thin coin.",
   "Harpers are protected by law, and the law is old. A poet or musician unpaid or insulted may cast a curse or compose a satire that follows a king to his grave. This one is looking at the door, and at you, and has not yet put the harp away.",
   [
       O("Call him back and pay him in front of the hall.", GOLD_M, PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 6 }", xp("lifestyle_poet", 15),
         st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Give him a ring from your own hand.", GOLD_S, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_poet_gift_opinion OPINION = 4 }",
         st=S_HUMBLE, ai=35),
       O("Order the steward to explain himself.", PRESTIGE_S, STRESS_UP,
         luck("t344w", "The steward pays, and apologises", "add_prestige = minor_prestige_gain", "t344l", "The harper curses the hall and leaves", "add_character_modifier = { modifier = eir_harpers_curse_modifier years = 5 }", p=60, bonus=(10, "diplomacy >= 10")),
         st=S_HONEST, ai=25),
       O("Let him go. A coin is a coin.", LOSS_S, "add_character_modifier = { modifier = eir_harpers_curse_modifier years = 5 }", STRESS_DOWN,
         st=S_GREED, ai=5),
   ],
   "court", gate="eir_stage1_trigger = yes", cooldown=15)

# =============================================================================
# WAR
# =============================================================================
ev(350, "The War-Poet Sings the Host Out",
   "On the eve of a march, the war-poet asks to sing a verse before the whole army.",
   "He is old, bald, and has served three kings. The verse is about the ancestors who held this ford, and each line ends with a name. The men are listening. He only wants the king's leave, and perhaps an answering verse, and a cup of the good mead.",
   [
       O("Answer him in verse of your own.", PRESTIGE_M, xp("lifestyle_poet", 30), "add_character_modifier = { modifier = eir_war_poem_modifier years = 3 }",
         gate="learning >= 8", st=S_HUMBLE, ai=40, ai_mod=[("gregarious", 15)]),
       O("Let him sing, and ride at the head of the column.", "add_character_modifier = { modifier = eir_war_poem_modifier years = 4 }", PRESTIGE_S, STRESS_DOWN,
         st=S_BRAVE, ai=40, ai_mod=[("brave", 20)]),
       O("Cut him short: the army has a march to make.", LOSS_S, "add_dread = minor_dread_gain", STRESS_UP,
         st=S_HARD, ai=10),
       O("Give the poet a share of the spoil in advance.", GOLD_M, "add_character_modifier = { modifier = eir_war_poem_modifier years = 3 }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_poet_gift_opinion OPINION = 3 }",
         st=S_GEN, ai=25),
   ],
   "war", gate="is_at_war = yes", cooldown=8)

ev(351, "The Gallowglass Captain Wants Land",
   "The captain of your gallowglass has asked for a place in the hills, a wife and a hall.",
   "He is called by a name that means 'foreign-warrior' in your language, and his axe has two hundred notches. He says his men are tired of being hired. They would like to be useful in a different way, and their sons would like not to be killed.",
   [
       O("Grant him lands on the border.", "add_character_modifier = { modifier = eir_gallowglass_lands_modifier years = 15 }", PRESTIGE_S, "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_gallowglass_garrison_modifier years = 20 }\n}",
         st=S_GEN, ai=40),
       O("Marry him to a noblewoman of your court.", "add_character_modifier = { modifier = eir_norse_wife_modifier years = 12 }", PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = -2 }",
         st=S_SHREWD, ai=30),
       O("Refuse. A warrior is not a lord.", LOSS_S, "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 4 }", STRESS_UP,
         st=S_ARROG, ai=10),
       O("Give him gold instead and send his men home.", GOLD_M, PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 2 }",
         st=S_GREED, ai=25),
   ],
   "war", gate="has_global_variable = eir_unlock_gallowglass", cooldown=15)

ev(352, "The Hostage Exchange",
   "Two hostages are to be exchanged on a bridge, and someone has brought a knife.",
   "You and your rival have agreed to swap sons at the midpoint of the ford. The boys are walking toward each other in the sunshine. A nervous guardsman on your side has put a hand to his sword, and across the water a man has done the same.",
   [
       O("Walk onto the bridge yourself, unarmed.", PRESTIGE_M, STRESS_UP, "add_character_modifier = { modifier = eir_ford_champion_modifier years = 4 }",
         luck("t352w", "Both sides lower their hands", "add_prestige = minor_prestige_gain", "t352l", "A knife flashes and you are cut", "increase_wounds_effect = { REASON = fight }", p=70, bonus=(10, "diplomacy >= 10")),
         gate="has_trait = brave", st=S_BRAVE, ai=30),
       O("Order your men to stand down, loudly.", PRESTIGE_S, STRESS_DOWN, "eir_court_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 3 }",
         st=S_PATIENT, ai=45),
       O("Strike first and settle it.", "add_dread = minor_dread_gain", LOSS_S, "eir_defender_levy_effect = yes",
         luck("t352bw", "You catch them off guard", "add_prestige = minor_prestige_gain", "t352bl", "The boys are caught in the melee", "add_stress = medium_stress_gain\nadd_prestige = medium_prestige_loss", p=40),
         st=S_WRATH, ai=10, ai_mod=[("wrathful", 25)]),
   ],
   "diplomacy", gate="any_vassal = { count >= 2 }", cooldown=15)

ev(353, "A Champion at the Ford",
   "An enemy champion has taken the ford and will not let your army cross unless you send a man to fight him.",
   "He is enormous, has the shoulders of a smith and is eating an apple. He says he will sit there until sunset or until somebody beats him, and the army behind you is beginning to think that the first is cheaper. The poets are already finding rhymes for 'ford'.",
   [
       O("Fight him yourself.", PRESTIGE_M, "add_character_modifier = { modifier = eir_ford_champion_modifier years = 8 }",
         luck("t353w", "He falls into the water", "add_prestige = major_prestige_gain\neir_trait_effect = { TRAIT = eir_champion_of_ulster OPPOSITE = craven CHANCE = 30 }", "t353l", "He breaks your shield and your pride", "add_prestige = medium_prestige_loss\nincrease_wounds_effect = { REASON = duel }", p=45, bonus=(20, "prowess >= 14")),
         gate="prowess >= 9", st=S_BRAVE, ai=35, ai_mod=[("brave", 25), ("wrathful", 10)]),
       O("Send your champion.", PRESTIGE_S, luck("t353cw", "Your champion wins", "add_prestige = minor_prestige_gain", "t353cl", "Your champion dies on the ford", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain", p=55),
         st=S_SHREWD, ai=40),
       O("Find another ford.", STRESS_DOWN, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -2 }", st=S_CRAVEN, ai=10),
       O("Offer him gold to step aside.", GOLD_M, STRESS_UP, PRESTIGE_S, st=S_GREED, ai=25),
   ],
   "war", gate="is_at_war = yes", cooldown=10)

# =============================================================================
# THE CELTIC NEIGHBOURS
# =============================================================================
ev(360, "Two Welsh Princes Quarrel",
   "Two princes of the Welsh have come to you separately, each swearing the other cheated him of a cantref.",
   "The border between them was drawn by a monk with a stick and a bad memory. Each has a lawyer, an army of sorts, and a cousin on the throne of England who might be asked for help. They would both rather have a Celtic arbiter, if the Celtic arbiter is fair.",
   [
       O("Hear both and rule yourself.", PRESTIGE_M, "add_character_modifier = { modifier = eir_mediator_of_wales_modifier years = 10 }", STRESS_UP,
         gate="diplomacy >= 10", st=S_HONEST, ai=40, ai_mod=[("just", 20)]),
       O("Arrange a marriage between the two houses.", PRESTIGE_S, "add_character_modifier = { modifier = eir_mediator_of_wales_modifier years = 8 }", GOLD_S, "eir_vassal_opinion_effect = { MODIFIER = eir_gael_pride_opinion OPINION = 2 }",
         st=S_SHREWD, ai=35),
       O("Back the stronger prince in return for a tribute of horses.", GAIN_M, PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = -2 }",
         st=S_GREED, ai=25),
       O("Stay out of it.", STRESS_DOWN, LOSS_S, st=S_CRAVEN, ai=10),
   ],
   "diplomacy", gate="has_global_variable = eir_done_brotherhood", cooldown=15)

ev(361, "The Cornish Tinners Strike",
   "The tinners of Cornwall have stopped digging, and the smelters of three kingdoms are asking why.",
   "A new overlord has doubled their dues. They want a protector with a treasury and no particular grudge, and they have sent their best speaker across the sea to ask whether the Irish king might be that man.",
   [
       O("Take the tinners under your protection and open a market.", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_tin_market_modifier years = 15 }\n}", PRESTIGE_S, GOLD_S,
         "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 4 }", st=S_GEN, ai=40),
       O("Buy their tin at a fair price and say nothing else.", GOLD_M, GAIN_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_cattle_rich_modifier years = 6 }",
         st=S_SHREWD, ai=35),
       O("Press their overlord to ease the dues.", PRESTIGE_M, STRESS_UP, "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 2 }",
         luck("t361w", "The overlord yields", "add_prestige = minor_prestige_gain", "t361l", "The overlord ignores you", "add_prestige = minor_prestige_loss", p=45, bonus=(15, "diplomacy >= 12")),
         gate="has_global_variable = eir_done_brotherhood", st=S_AMBIT, ai=25),
       O("Decline. The tinners must fend for themselves.", LOSS_S, STRESS_DOWN, st=S_CONTENT, ai=10),
   ],
   "diplomacy", gate="has_global_variable = eir_done_brotherhood", cooldown=20)

ev(362, "Breton Exiles Settle",
   "Thirty Breton families, priests, weavers and a cider-maker among them, have asked for land.",
   "They left a country that no longer wants their language and carry a few relics, an unusual breed of dog and a very convincing claim of descent from the kings of Armorica. They are courteous, hungry and clever, and one of them has a recipe for a bread that does not go stale.",
   [
       O("Give them a quarter of a town.", "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_exile_quarter_modifier years = 20 }\n}", PRESTIGE_S, PIETY_S,
         "add_character_modifier = { modifier = eir_breton_refuge_modifier years = 6 }", st=S_KIND, ai=40, ai_mod=[("compassionate", 15)]),
       O("Make the cider-maker a court brewer.", PRESTIGE_S, xp("lifestyle_reveler", 25), GOLD_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }",
         st=S_CONTENT, ai=30),
       O("Ask what they know about the Frankish courts.", PRESTIGE_S, "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 3 }", STRESS_UP,
         gate="intrigue >= 9", st=S_DECEIT, ai=25),
       O("Settle them in the poorest land and say nothing.", LOSS_S, GAIN_S, st=S_GREED, ai=10),
   ],
   "court", gate="has_global_variable = eir_done_brotherhood", cooldown=20)

ev(363, "A Stone with Beasts",
   "Workmen digging a drain in the north have found a carved stone with a serpent, a mirror and a crescent on it.",
   "The Picts left them everywhere and nobody knew what they meant even then. The monks want to smash it as a pagan idol. The poets want to put it in the hall. The workmen would like to be paid.",
   [
       O("Set it up in your hall.", PRESTIGE_S, "add_character_modifier = { modifier = eir_pictish_stone_modifier years = 12 }", xp("lifestyle_poet", 15),
         st=S_CONTENT, ai=40),
       O("Let the monks bury it under the chapel floor.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 3 }",
         st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
       O("Have a scholar copy the symbols for study.", PRESTIGE_S, "add_learning_lifestyle_xp = medium_lifestyle_xp", "add_character_modifier = { modifier = eir_pictish_stone_modifier years = 6 }",
         gate="learning >= 10", st=S_SHREWD, ai=35),
       O("Sell it to a passing merchant.", GAIN_M, LOSS_S, st=S_GREED, ai=10),
   ],
   "learning", gate="has_global_variable = eir_done_dalriata", cooldown=25)

ev(364, "Galloway Asks for Help",
   "The Gaels of Galloway, a long way across the water, have sent a boat with an urgent message.",
   "A foreign lord is building a castle on the headland and has begun to charge for the use of the beach. The men of Galloway speak your language, bury their dead in the way yours do and ask whether the High King of Ireland can be called an ally or only a poem.",
   [
       O("Send a hundred warriors in ships.", GOLD_M, "eir_defender_levy_effect = yes", PRESTIGE_M, "add_character_modifier = { modifier = eir_galloway_allies_modifier years = 10 }",
         st=S_BRAVE, ai=35),
       O("Send gold and a letter to their overlord.", GOLD_S, PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_gael_pride_opinion OPINION = 3 }", STRESS_UP,
         gate="diplomacy >= 9", st=S_SHREWD, ai=40),
       O("Invite their chief to your court as a guest.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 4 }", xp("lifestyle_reveler", 15),
         st=S_GEN, ai=30),
       O("Regretfully decline.", LOSS_S, STRESS_UP, st=S_CRAVEN, ai=10),
   ],
   "war", gate="has_global_variable = eir_done_dalriata", cooldown=20)

# =============================================================================
# COURT, LEGEND AND OMEN
# =============================================================================
ev(370, "A Prodigy at the Harp",
   "A six-year-old in your household has just played a lament that made a hardened old warrior weep.",
   "She learned it by listening through a wall. She cannot read, is unusually serious, and has asked, politely, whether she might have lessons. The harper of the court has gone quiet in a way that suggests he has just realised something.",
   [
       O("Give her the best master in the land.", GOLD_M, "add_character_modifier = { modifier = eir_child_prodigy_modifier years = 15 }", PRESTIGE_S, xp("lifestyle_poet", 20),
         st=S_GEN, ai=40, ai_mod=[("generous", 15)]),
       O("Send her to be fostered with the bardic school.", GOLD_S, "add_character_modifier = { modifier = eir_foster_bond_modifier years = 10 }", PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 3 }",
         gate="has_global_variable = eir_unlock_bardic_school", st=S_PATIENT, ai=40),
       O("Keep the talent in your household as a secret weapon.", PRESTIGE_S, STRESS_UP, "add_character_modifier = { modifier = eir_child_prodigy_modifier years = 8 }",
         st=S_DECEIT, ai=20),
       O("Say harp-playing is not for noble girls.", LOSS_S, STRESS_DOWN, st=S_ARROG, ai=5),
   ],
   "family", gate="any_child = { age < 12 }", cooldown=25)

ev(371, "The Wedding Feast of the Isles",
   "A galley-lord from the Hebrides has invited you to his daughter's wedding, and he does not take refusal well.",
   "Ten days of feasting, a fleet of galleys drawn up on the shore, and a bride who will inherit half an island. Everyone who matters in the western seas will be there. So will several people who would like to see you humiliated in the dancing.",
   [
       O("Attend in your best cloak and bring a rich gift.", GOLD_M, PRESTIGE_M, "add_character_modifier = { modifier = eir_isles_wedding_modifier years = 8 }", xp("lifestyle_reveler", 25),
         gate="eir_has_coast_trigger = yes", st=S_GEN, ai=40, ai_mod=[("gregarious", 15)]),
       O("Send your heir as your representative.", GOLD_S, PRESTIGE_S, "primary_heir ?= { add_trait_xp = { trait = lifestyle_reveler value = 25 } }", "eir_vassal_opinion_effect = { MODIFIER = eir_hebridean_kin_opinion OPINION = 3 }",
         gate="exists = primary_heir", st=S_PATIENT, ai=35),
       O("Challenge the groom's brother to a drinking contest.", PRESTIGE_S, xp("lifestyle_reveler", 40),
         luck("t371w", "He falls under the table and you do not", "add_prestige = minor_prestige_gain\nadd_character_modifier = { modifier = eir_isles_wedding_modifier years = 5 }", "t371l", "You are carried to bed by two gallowglass", "add_prestige = minor_prestige_loss\nadd_trait_xp = { trait = lifestyle_reveler value = 10 }", p=50),
         st=S_ARROG, ai=20, ai_mod=[("gluttonous", 15), ("gregarious", 10)]),
       O("Decline with a courteous letter.", LOSS_S, STRESS_DOWN, st=S_CONTENT, ai=10),
   ],
   "feast_activity", gate="eir_has_coast_trigger = yes", cooldown=20)

ev(372, "A Ghost at Samhain",
   "At Samhain, on the night the dead walk, a tall man in a green cloak is standing in your hall's doorway.",
   "He has no shadow. He is tall, scarred and smiling a little. Nobody else seems to see him. He says nothing, but he is looking at your sword, and at you, and the dogs have gone silent. In the stories, the Hound of Ulster comes to those who must make a choice.",
   [
       O("Salute him and offer him a cup.", xp("lifestyle_mystic", 30), "add_character_modifier = { modifier = eir_hounds_ghost_modifier years = 10 }", PRESTIGE_S,
         st=S_BRAVE, ai=40, ai_mod=[("brave", 20)]),
       O("Cross yourself, and call for the priest.", PIETY_M, STRESS_DOWN, xp("lifestyle_mystic", 10),
         st=S_ZEAL, ai=35, ai_mod=[("zealous", 20)]),
       O("Draw your sword and challenge him.", PRESTIGE_S,
         luck("t372w", "He bows and fades", "add_prestige = minor_prestige_gain\nadd_character_modifier = { modifier = eir_hounds_ghost_modifier years = 6 }", "t372l", "The cold knocks you down", "increase_wounds_effect = { REASON = fight }\nadd_stress = minor_stress_gain", p=50, bonus=(15, "prowess >= 12")),
         gate="prowess >= 8", st=S_BRAVE, ai=25),
       O("Pretend you saw nothing, and drink more mead.", STRESS_DOWN, xp("lifestyle_reveler", 15), LOSS_S,
         st=S_CRAVEN, ai=20),
   ],
   "legend", gate="has_global_variable = eir_unlock_fianna\ncurrent_month = 11", cooldown=20)

ev(373, "The Star with a Tail",
   "A bright star with a long pale tail hangs in the sky every night, and nobody can agree on what it means.",
   "The monks say it is a warning. The poets say it is a sign that a king will fall, which is the usual thing to say. The old women say it is a sign that a baby will be born who will change the island. The reeves say that the harvest was good anyway.",
   [
       O("Call it a sign of divine favour.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 3 }",
         st=S_ZEAL, ai=35),
       O("Call it a warning, and order a fast.", PIETY_L, "add_character_modifier = { modifier = eir_omen_comet_modifier years = 3 }", STRESS_UP,
         st=S_ZEAL, ai=25),
       O("Ask the poets for a verse that fits any outcome.", PRESTIGE_S, xp("lifestyle_poet", 25), "add_character_modifier = { modifier = eir_fili_patron_modifier years = 3 }",
         gate=FILI, st=S_DECEIT, ai=40),
       O("Laugh at it and go hunting.", STRESS_DOWN, PRESTIGE_S, "add_character_modifier = { modifier = eir_omen_comet_modifier years = 3 }",
         st=S_CYN, ai=20, ai_mod=[("cynical", 20)]),
   ],
   "legend", cooldown=40)

ev(374, "The Satire Against the Steward",
   "A court poet has composed a savage satire against your steward, and the steward is weeping in the hall.",
   "It is witty, cruel, and entirely accurate. The poet is a favourite of the court and the steward is the man who keeps the realm solvent. Both of them are looking at you, and each has in mind a different ending.",
   [
       O("Pay the poet to compose a second poem, a praise-poem of the steward.", GOLD_M, PRESTIGE_S, xp("lifestyle_poet", 15), "eir_court_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 3 }",
         st=S_GEN, ai=40),
       O("Banish the poet from court for a year.", LOSS_S, "add_character_modifier = { modifier = eir_harpers_curse_modifier years = 3 }", STRESS_UP,
         st=S_HARD, ai=10),
       O("Laugh at the poem, and let the steward be laughed at too.", PRESTIGE_S, STRESS_DOWN, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = -2 }",
         st=S_CONTENT, ai=30),
       O("Raise the steward's pay and add a title.", GOLD_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 3 }", PRESTIGE_S,
         st=S_SHREWD, ai=35),
   ],
   "court", gate="eir_stage1_trigger = yes", cooldown=15)

ev(375, "The Tale of the Cattle-Raid Retold",
   "Your master-poet has asked leave to retell the Táin in the evenings of the winter court.",
   "It has not been told in the great hall for a generation, because the old version is long, bloody and sympathetic to Queen Medb. The master-poet's plan is to alter some details, add a few of your ancestors, and finish with a stanza about the present king. It takes a month to recite.",
   [
       O("Grant the winter, and attend every evening.", GOLD_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_tain_retold_modifier years = 8 }", xp("lifestyle_poet", 30),
         "eir_legend_title_effect = { TITLE = primary_title }", gate=FILI, st=S_HUMBLE, ai=40),
       O("Grant the winter, but ask for a version more flattering to the High King.", PRESTIGE_M, "add_character_modifier = { modifier = eir_tain_retold_modifier years = 5 }",
         luck("t375w", "The poet obliges, subtly", "add_prestige = minor_prestige_gain", "t375l", "The poet's satire shows through", "add_character_modifier = { modifier = eir_satirised_modifier years = 3 }", p=55, bonus=(10, "diplomacy >= 10")),
         gate=FILI, st=S_ARROG, ai=25),
       O("Forbid it: the old tale glorifies cattle thieves.", PIETY_S, LOSS_S, STRESS_UP, st=S_ZEAL, ai=10),
   ],
   "learning", gate="has_global_variable = eir_done_fili\neir_stage2_trigger = yes", cooldown=25)
