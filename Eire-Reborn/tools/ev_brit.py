"""Update 4 (Britannia): the Saxon Uprising (0800), the ceremonies of the Britannia decisions (0801-0803, 0811-0815, 0820)
and the reactions (0804-0806)."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"


def ceremony(num, title, summary, body, options, theme="legend", immediate="", variants=None, gate=""):
    ev(num, title, summary, body, options, theme, guarded=False, immediate=immediate, variants=variants, gate=gate)


# =============================================================================
# 0800 THE SAXONS RISE  (guaranteed: the county has already been shaken before you choose)
# =============================================================================
ev(800, "The Saxons Rise",
   "A county that was made to speak Gaelic has risen, and the beacons along the border are burning.",
   "It was always going to happen. The reeve was found in a ditch with a book of Gaelic grammar stuffed in his mouth. By dawn the thanes had called out their men, by noon the hedge-school was ash, and the border fort was sending to ask what the king wanted. Your steward is looking at the floor.\n\nThe county was not asked.",
   [
       O("Ride out with the host and break them in the field.", "eir_defender_levy_effect = yes",
         luck("t800w", "You catch them before they gather", "add_prestige = medium_prestige_gain\nscope:eir_unrest_county ?= { change_county_control = medium_county_control_gain }\neir_trait_effect = { TRAIT = brave OPPOSITE = craven CHANCE = 25 }",
              "t800l", "They scatter, burn the fort and hold the hills", "add_prestige = minor_prestige_loss\nscope:eir_unrest_county ?= { add_county_modifier = { modifier = eir_rebel_march_modifier years = 8 } }\nincrease_wounds_effect = { REASON = fight }",
              p=55, bonus=(15, "martial >= 12")),
         st=S_BRAVE, ai=40, ai_mod=[("brave", 15), ("wrathful", 10)]),
       O("Hear their grievances under a flag of truce.", "scope:eir_unrest_county ?= { add_county_modifier = { modifier = eir_saxon_moot_modifier years = 12 } }",
         "scope:eir_unrest_county ?= { remove_county_modifier = eir_saxon_uprising_modifier }", "eir_resent_clear_effect = yes", PRESTIGE_S, "add_character_modifier = { modifier = eir_two_peoples_modifier years = 10 }",
         gate="diplomacy >= 10", st=S_FORGIVE, ai=35, ai_mod=[("forgiving", 15), ("just", 10)]),
       O("Burn the villages that rose.", "add_dread = major_dread_gain", "add_character_modifier = { modifier = eir_hard_hand_modifier years = 12 }",
         "scope:eir_unrest_county ?= { add_county_modifier = { modifier = eir_rebel_march_modifier years = 12 } }", PLOSS_S,
         st=S_HARD, ai=10, ai_mod=[("sadistic", 25), ("callous", 15)]),
       O("Pay the thanes to keep their people quiet.", GOLD_M, "eir_resent_clear_effect = yes", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 3 }",
         st=S_GEN, ai=30),
       O("Withdraw the garrison and let the county go its own way.", LOSS_M, "scope:eir_unrest_county ?= { change_county_control = major_county_control_loss }", "eir_resent_clear_effect = yes", STRESS_DOWN,
         st=S_CRAVEN, ai=10, ai_mod=[("craven", 20)]),
   ],
   "war", guarded=False, gate="has_variable = eir_rising_county",
   immediate="""var:eir_rising_county ?= {
	save_scope_as = eir_unrest_county
	change_county_control = major_county_control_loss
	add_county_modifier = { modifier = eir_rebel_march_modifier years = 4 }
}
remove_variable = eir_rising_county""")

# =============================================================================
# CEREMONIES
# =============================================================================
ceremony(801, "A Third of the Island",
         "A Gaelic king now holds a third of the counties of Britannia, and the poets are counting.",
         "Twenty-eight counties of ninety-three. It took you a lifetime, and your father's, and his. The poets have taken to saying that the island has three corners and that you hold one of them. The English are saying that you hold none. The map, which has no opinion, is on the table, and it is mostly the colour of your banner.",
         [
             O("Proclaim it in Irish, in Welsh and in Latin.", PRESTIGE_L, "eir_legend_title_effect = { TITLE = primary_title }", xp("lifestyle_poet", 30), "eir_world_reacts_effect = yes",
               st=S_ARROG, ai=40, ai_mod=[("ambitious", 20), ("arrogant", 10)]),
             O("Hold a feast at the highest hall in the conquered lands.", GOLD_S, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 5 }", xp("lifestyle_reveler", 30),
               st=S_GEN, ai=35, ai_mod=[("generous", 20)]),
             O("Endow a monastery in every conquered diocese.", GOLD_M, PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }", "eir_resent_clear_effect = yes",
               gate="piety >= 100", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
             O("Say nothing, and let the army speak.", "add_dread = minor_dread_gain", PRESTIGE_M, STRESS_DOWN,
               st=S_PATIENT, ai=25, ai_mod=[("calm", 15)]),
         ])

ceremony(802, "The Gaelic Kingdoms United",
         "Ireland and Scotland answer to one crown for the first time since the poems began.",
         "The harpers of Tara and the pipers of Dunadd played the same march at the same hour, a hundred miles of sea apart, and it took them four attempts to get it in time. The bishops have drafted a letter. The jarls of the Isles have sent a polite complaint. Nobody in the English court has taken it seriously yet.",
         [
             O("Take the claim to Britannia aloud, and name the Saxon king in it.", PRESTIGE_L, "add_dread = minor_dread_gain", "eir_legend_title_effect = { TITLE = title:e_britannia }", "eir_world_reacts_effect = yes",
               st=S_ARROG, ai=40, ai_mod=[("ambitious", 20), ("arrogant", 10)]),
             O("Hold a joint Aonach at the Boyne and the Forth.", GOLD_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }", xp("lifestyle_reveler", 25),
               st=S_GEN, ai=35, ai_mod=[("gregarious", 20)]),
             O("Have the poets sing the two crowns as one.", PRESTIGE_M, xp("lifestyle_poet", 40), "add_character_modifier = { modifier = eir_insular_song_modifier years = 10 }",
               gate=FILI, st=S_HUMBLE, ai=30),
             O("Send the relics of Colmcille across the North Channel.", PIETY_L, PRESTIGE_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }",
               gate="piety >= 150", st=S_ZEAL, ai=25, ai_mod=[("zealous", 25)]),
         ])

ceremony(803, "Arthur Reborn",
         "The poets of three peoples say that the king who slept under the hill is awake, and has an Irish face.",
         "It was a Welsh bard who said it first, in a hall in Gwynedd where somebody had put a sword on the table for a joke. The Cornish picked it up, and then a Breton monk, and then every singer on the roads of Britain. The sword is real. It has a dragon on the hilt and no name. By the time it reached you it had acquired one.",
         [
             O("Take the sword, the name and the title.", "give_nickname = nick_eir_once_future_king", PRESTIGE_L, PIETY_M, "eir_legend_title_effect = { TITLE = title:e_britannia }",
               st=S_ARROG, ai=40, ai_mod=[("arrogant", 15), ("ambitious", 20)]),
             O("Carry the sword to Tara and swear on it before the kings.", PRESTIGE_L, "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 10 }", "eir_world_reacts_effect = yes",
               st=S_HUMBLE, ai=35, ai_mod=[("humble", 15), ("honest", 10)]),
             O("Have the Welsh bards carry the story across Britain.", PRESTIGE_M, xp("lifestyle_poet", 40), "add_character_modifier = { modifier = eir_welsh_ties_modifier years = 15 }",
               "add_character_modifier = { modifier = eir_insular_song_modifier years = 15 }", gate=FILI, st=S_GEN, ai=35),
             O("Bury the title and keep the sword.", PRESTIGE_S, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 6 }", STRESS_DOWN,
               st=S_SHREWD, ai=20, ai_mod=[("shrewd", 20)]),
         ])

ceremony(804, "The English Court Answers",
         "The English king has read the Gaelic proclamation, and he is not laughing.",
         "He had it read to him twice. The second reading was in front of the council, so that nobody could say afterwards that they had not been told. A tithe has been raised. The marshal has been sent for. The bishops have been asked whether the Irish are sound on the Easter question.",
         [
             O("Send back a courteous letter naming the fords you hold.", PRESTIGE_M, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 5 }", STRESS_UP,
               st=S_SHREWD, ai=35, ai_mod=[("shrewd", 15)]),
             O("Raise the border levies at once.", "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 3 }", GOLD_S,
               st=S_BRAVE, ai=40, ai_mod=[("brave", 15)]),
             O("Send the English a gift of Irish wolfhounds.", GOLD_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_hunting_hounds_modifier years = 5 }",
               st=S_GEN, ai=25, ai_mod=[("generous", 15), ("shrewd", 10)]),
             O("Ignore it. Words are for the losing side.", "add_dread = minor_dread_gain", PRESTIGE_S, STRESS_DOWN,
               st=S_ARROG, ai=20, ai_mod=[("arrogant", 15)]),
         ], theme="court", gate="has_global_variable = eir_done_brit30")

ceremony(805, "The Welsh Hear the News",
         "A Welsh prince has crossed the sea to ask whether the Gaelic crown means to be kind to the Britons.",
         "He has come in person, with a harper and a monk, because he does not trust letters. He has the stiff patience of a man who has lost land before. He would like to know whether the Gaelic king means to take Wales or to stand with it, and he would like the answer before the harp has been tuned.",
         [
             O("Swear an alliance of the Celts, and mean it.", PRESTIGE_M, "add_character_modifier = { modifier = eir_welsh_ties_modifier years = 15 }", "eir_world_reacts_effect = yes",
               gate="diplomacy >= 10", st=S_HONEST, ai=40, ai_mod=[("honest", 20), ("gregarious", 10)]),
             O("Offer him a place in the Gaelic army and a share of the plunder.", GAIN_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_gwynedd_alliance_modifier years = 8 }",
               st=S_GREED, ai=30, ai_mod=[("greedy", 15)]),
             O("Tell him Wales will be spared if it speaks no English.", PRESTIGE_S, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_welsh_resentment_modifier years = 8 }",
               st=S_ARROG, ai=15, ai_mod=[("arrogant", 20)]),
             O("Receive him with honours and say nothing.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 4 }", STRESS_DOWN,
               st=S_CONTENT, ai=25),
         ], theme="diplomacy", gate="has_global_variable = eir_done_gaelic_isles")

ceremony(806, "Merlin's Prophecy",
         "A blind prophet at the edge of your court is reciting a poem that nobody taught him.",
         "It is in no language the monks recognise, and it has the rhythm of a Welsh englyn and the images of an Irish rann. It describes a king who will gather the island, a sword that will not be drawn but found, five gifts to be taken from five places, and a revenge. The court has gone silent. The prophet bows, and asks for ale.",
         [
             O("Write every word down.", PRESTIGE_M, xp("lifestyle_poet", 30), xp("lifestyle_mystic", 30), "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 8 }",
               st=S_HUMBLE, ai=40, ai_mod=[("humble", 15)]),
             O("Make him your chief poet.", GOLD_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 15 }", "add_character_modifier = { modifier = eir_insular_song_modifier years = 10 }",
               st=S_GEN, ai=35, ai_mod=[("generous", 15)]),
             O("Have the monks check it for heresy.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 6 }",
               gate="piety >= 80", st=S_ZEAL, ai=25, ai_mod=[("zealous", 20)]),
             O("Laugh, and send him away with a coin.", STRESS_DOWN, PRESTIGE_S, "eir_trait_effect = { TRAIT = cynical OPPOSITE = zealous CHANCE = 25 }",
               st=S_CYN, ai=15, ai_mod=[("cynical", 25)]),
         ], theme="legend", gate="has_global_variable = eir_done_arthur")


def path_ceremony(num, title, summary, body, o1, o2, o3, gate_trait=""):
    ceremony(num, title, summary, body, [
        O(o1, PRESTIGE_L, PIETY_M, "eir_legend_title_effect = { TITLE = primary_title }", "eir_world_reacts_effect = yes", st=S_ARROG, ai=40, ai_mod=[("ambitious", 20), ("arrogant", 10)]),
        O(o2, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 8 }", "add_character_modifier = { modifier = eir_allied_kings_modifier years = 8 }", GOLD_S,
          st=S_GEN, ai=35, ai_mod=[("generous", 20)]),
        O(o3, PRESTIGE_M, PIETY_M, xp("lifestyle_mystic", 40), "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }", st=S_HUMBLE, ai=30, ai_mod=[("humble", 15), ("zealous", 15)]),
        O("Tell nobody, and let the item speak for itself.", PRESTIGE_S, STRESS_DOWN, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 6 }", st=S_SHREWD, ai=20, ai_mod=[("shrewd", 20)]),
    ])


path_ceremony(811, "The Mail of the Pendragon", "A coat of ring-mail has come out of the rock at Tintagel as bright as the day it went in.",
              "You went down into the cave at low tide with a torch and a priest. The sea was already coming in. At the back, behind a slab no man had moved in six hundred years, it lay on a stone shelf wrapped in sheepskin, and when the wool came off it did not smell of damp. The priest crossed himself. The mail fit.",
              "Wear it into the hall that evening.", "Display it at Tintagel and invite the Cornish to look.", "Take it to the altar of the nearest church and have it blessed.")
path_ceremony(812, "The Crown of Britain", "The red-gold circlet of the kings of Britain has been taken out of the hall at Caerleon, and a Gaelic king holds it.",
              "The hall is a ruin of Roman brick with a Welsh roof on it. The crown was kept in a chest under the dais, by a family who had been told to keep it for the right person and had not been told who. They held a vote. It was unanimous, and they were visibly relieved. The dragon on the circlet has been polished by six hundred years of hands.",
              "Be crowned with it at Caerleon.", "Give the Welsh princes a share in the coronation.", "Have the bishop of St David's bless the crown.")
path_ceremony(813, "The Brooch of Avalon", "The nuns of the Isle of Apples have given you the brooch of the king who sleeps.",
              "The mist on the Somerset levels is said to rise when the right person walks through it. It rose on the second morning. The abbess met you at the water's edge with the brooch wrapped in a grey cloth and no explanation. She said only that she had been told to wait, and that she was tired of it.",
              "Wear it at the altar of the abbey and take the vows of a protector.", "Give a gift of land to the nuns in return.", "Pray at the chapel of Joseph for the night.")
path_ceremony(814, "Rhongomyniad, the Spear of Badon", "A long ash spear has been put in your hand at a field near Bath, where a king once stopped the Saxons.",
              "You held most of the island by the end. The English crown had sent its best captains and been beaten at every ford. On the last day a Welsh farmer walked into your camp with a long package wrapped in oilcloth. He said it had been in his barn for as long as his family had a barn. It was an ash spear with a bronze head, and it was warm to touch.",
              "Ride at the head of the army with the spear.", "Give the farmer a county.", "Raise a cross on the field.")
path_ceremony(815, "The Round Table", "A table with no head has been built at Tara, and ten knights who have never quarrelled have sat down at it.",
              "The carpenter was Welsh, the oak was Irish and the design was the carpenter's, from a dream. It seats a hundred and fifty, and has no top or bottom. Ten knights sat down on the first night. Nothing was said for a long time, and then, to their considerable surprise, they began to laugh.",
              "Sit at the table as an equal and open the first feast.", "Invite every king on the island to take a seat.", "Hold the first session in silence, as a vigil.")

# =============================================================================
# 0820 THE LAST REVENGE OF THE CELTS  (choose where the great building stands)
# =============================================================================
SITE = "title:%s = {\n\tholder = { top_liege = root }\n}"
ev(820, "The Last Revenge of the Celts",
   "The island is yours, and the poets are asking where the great hall of the whole island should stand.",
   "It has been seven hundred years. The Romans left, and the Saxons came, and the Britons were pushed into the west, and the Gaels were pushed into the sea, and the poems said that it would not last. It did not. You hold the island from the Orkneys to the Cornish tin. The builders have drawn five plans. Each is a wonder. Only one can be built.\n\nThey have asked you to choose.",
   [
       O("At Winchester, where Alfred sat: the Hall of the Returned Kings.",
         "title:b_winchester.title_province = { add_building = eir_final_winchester_01 }", PRESTIGE_L, PIETY_M, "eir_legend_title_effect = { TITLE = title:e_britannia }",
         gate=SITE % "b_winchester", st=S_ARROG, ai=30, ai_mod=[("arrogant", 15), ("ambitious", 10)]),
       O("At York, the capital of the north: the Minster of the Celtic Kings.",
         "title:b_york.title_province = { add_building = eir_final_york_01 }", PRESTIGE_L, PIETY_L, "eir_legend_title_effect = { TITLE = title:e_britannia }",
         gate=SITE % "b_york", st=S_ZEAL, ai=30, ai_mod=[("zealous", 15)]),
       O("At Edinburgh, on the rock above the Forth: the Rock of the Gaelic Crown.",
         "title:b_edinburgh.title_province = { add_building = eir_final_edinburgh_01 }", PRESTIGE_L, "add_dread = minor_dread_gain", "eir_legend_title_effect = { TITLE = title:e_britannia }",
         gate=SITE % "b_edinburgh", st=S_BRAVE, ai=30, ai_mod=[("brave", 15)]),
       O("At Caernarfon, at the mouth of the Menai: the Citadel of the Pendragon.",
         "title:b_caernarfon.title_province = { add_building = eir_final_caernarfon_01 }", PRESTIGE_L, "add_character_modifier = { modifier = eir_welsh_ties_modifier years = 25 }", "eir_legend_title_effect = { TITLE = title:e_britannia }",
         gate=SITE % "b_caernarfon", st=S_HUMBLE, ai=30, ai_mod=[("humble", 15)]),
       O("At Bath, where the Britons stopped the Saxons: the Court of Badon.",
         "title:b_bath.title_province = { add_building = eir_final_bath_01 }", PRESTIGE_L, xp("lifestyle_mystic", 40), "eir_legend_title_effect = { TITLE = title:e_britannia }",
         gate=SITE % "b_bath", st=S_PATIENT, ai=30, ai_mod=[("patient", 15)]),
       O("Build no hall. Give the gold to the monasteries and the poets.",
         "add_gold = major_gold_value", PRESTIGE_L, PIETY_L, xp("lifestyle_poet", 50), "add_character_modifier = { modifier = eir_insular_song_modifier years = 25 }",
         st=S_GEN, ai=5),
   ], "legend", guarded=False)
