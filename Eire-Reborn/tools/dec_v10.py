"""Update 4 decisions: Britannia. A Gaelic ruler's road to the whole island:
  1 claim a third of Britannia -> 2 unite the Gaelic kingdoms -> 3 revive the Arthurian legend -> five hard paths (one Arthurian item each)
  -> the Last Revenge of the Celts (95% of the island, a super special building). Registered after dec_finalize: costs are final."""
from gen_decisions import D, IRISH, GAEL

S3 = "eir_stage3_trigger = yes"


def req(*lines):
    return "\n".join(l for l in lines if l)


def cost(gold=0, prestige=0, piety=0):
    return "\n".join(x for x in (("gold = %d" % gold) if gold else "", ("prestige = %d" % prestige) if prestige else "", ("piety = %d" % piety) if piety else "") if x)


def HAS(var):
    return "has_global_variable = %s" % var


def not_done(var):
    return "NOT = { has_global_variable = %s }" % var


KING = GAEL + "\neir_gael_king_trigger = yes"
DONE1, DONE2, DONE3 = "eir_done_brit30", "eir_done_gaelic_isles", "eir_done_arthur"

# ------------------------------------------------------------------------------------------------ 1
D("eir_third_of_britannia_decision", "A Third of the Island",
  "An Irish king who holds a third of the island of Britannia has done what the Irish kings never did: made the island's quarrel an Irish one. Say so aloud, in the old tongue, and let the counties hear it.",
  "Needs to be an Irish king who holds 28 of the 93 counties of the Empire of Britannia (30%). Gives the Gaelic Ascendancy modifier for 50 years: foreign counties of Britannia in your realm take your culture at five times the pace (1% a year, up to 6%). Every conversion raises the Saxon unrest chain and the county takes -50 opinion for 20 years. Also prestige, piety, opinion and a Pride of the Island modifier in every Britannic county you hold. Once per game.",
  IRISH + "\neir_irish_king_trigger = yes\n" + not_done(DONE1),
  """add_character_modifier = { modifier = eir_brit_ascendancy_1_modifier years = 50 }
add_prestige = massive_prestige_gain
add_piety = medium_piety_gain
add_dread = minor_dread_gain
eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }
every_sub_realm_county = {
	limit = { empire = title:e_britannia }
	add_county_modifier = { modifier = eir_island_pride_modifier years = 15 }
}
eir_world_reacts_effect = yes
set_global_variable = eir_done_brit30
trigger_event = eir.0801
trigger_event = { id = eir.0804 days = 90 }""",
  valid=req("eir_irish_king_trigger = yes", "eir_brit_30_trigger = yes", "is_at_war = no"),
  cost=cost(gold=300, prestige=800, piety=100), cd=36500, major=True, pic="decision_golden_age")

# ------------------------------------------------------------------------------------------------ 2
D("eir_unite_gaelic_kingdoms_decision", "The Gaelic Kingdoms United",
  "Ireland and Scotland have shared a language, a saint and a quarrel for a thousand years. Put one crown over both, and call yourself what the poets always said the Gael would be: lord of the north and the west.",
  "Needs the first decision, a Gaelic culture and both the Kingdom of Ireland and the Kingdom of Scotland. Stacks the Ascendancy (another +5, up to 11% a year), converts half of the non-Gaelic counties of Ireland and Scotland you hold to your culture right away (each takes -50 opinion for 20 years and feeds the unrest chain), gives you a claim on the Empire of Britannia, and a United Kingdoms modifier for 50 years. Once per game.",
  GAEL + "\n" + HAS(DONE1) + "\n" + not_done(DONE2),
  """add_character_modifier = { modifier = eir_brit_ascendancy_2_modifier years = 50 }
add_prestige = massive_prestige_gain
add_piety = medium_piety_gain
add_pressed_claim = title:e_britannia
eir_brit_isles_convert_effect = yes
eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 8 }
eir_world_reacts_effect = yes
set_global_variable = eir_done_gaelic_isles
trigger_event = eir.0802
trigger_event = { id = eir.0805 days = 60 }""",
  valid=req("eir_gael_king_trigger = yes", "eir_holds_both_kingdoms_trigger = yes", HAS(DONE1), "is_at_war = no"),
  cost=cost(gold=500, prestige=1500, piety=250), cd=36500, major=True, pic="decision_found_kingdom")

# ------------------------------------------------------------------------------------------------ 3
D("eir_revive_arthur_decision", "Revive the Arthurian Legend",
  "Every people on the island says that Britain's last great king sleeps under a hill and will return when the island needs him. Let the poets say it is you, and give them a sword to prove it.",
  "Needs the Gaelic Kingdoms United, a kingdom, prestige level 4 and 1000 piety. Creates a mythical heroic legend, the unique sword Caliburn (a super-powered artifact), the Arthur Reborn modifier for 40 years, and opens five hard paths that each win one more item of the king's regalia. Once per game.",
  GAEL + "\n" + HAS(DONE2) + "\n" + not_done(DONE3),
  """add_character_modifier = { modifier = eir_arthur_reborn_modifier years = 40 }
add_prestige = massive_prestige_gain
add_piety = major_piety_gain
add_trait_xp = { trait = lifestyle_poet value = 100 }
eir_arthur_legend_effect = yes
eir_make_artifact_effect = { NAME = eir_arthur_sword_name DESC = eir_arthur_sword_desc TYPE = sword VISUALS = sword MODIFIER = eir_arthur_sword_modifier }
eir_world_reacts_effect = yes
set_global_variable = eir_done_arthur
trigger_event = eir.0803
trigger_event = { id = eir.0806 days = 120 }""",
  valid=req("eir_gael_king_trigger = yes", HAS(DONE2), "prestige_level >= 4", "piety >= 1000", "is_at_war = no"),
  cost=cost(gold=800, prestige=2500, piety=500), cd=36500, major=True, pic="decision_legend")

# ------------------------------------------------------------------------------------------------ the five paths (shown after the second decision, usable after the third)
PATH_SHOWN = GAEL + "\n" + HAS(DONE2)


def path(key, name, desc, tip, var, valid_extra, cost_, effect, evt, pic="decision_legend"):
    D("eir_path_%s_decision" % key, name, desc, tip, PATH_SHOWN + "\n" + not_done(var),
      effect + "\nset_global_variable = %s\ntrigger_event = eir.%04d" % (var, evt),
      valid=req(HAS(DONE3), *valid_extra, "is_at_war = no"), cost=cost_, cd=36500, major=True, pic=pic)


path("armor", "The Mail of the Pendragon",
     "Tintagel is where the poets say the Pendragon was conceived, on a rock above the western sea. Hold Cornwall, raise the old fortress and go down to the cave to take back what was left in it.",
     "Needs the Arthurian legend, Cornwall, the Fortress of Tintagel built and prestige level 4. Gives the unique armor The Mail of the Pendragon, the Heir of Tintagel modifier for 30 years and a Seat of the Pendragon's Memory in Cornwall. Once per game.",
     "eir_path_armor_done", ["eir_holds_cornwall_trigger = yes", "eir_tintagel_built_trigger = yes", "prestige_level >= 4"],
     cost(gold=1200, prestige=2500, piety=300),
     """add_character_modifier = { modifier = eir_path_armor_modifier years = 30 }
add_prestige = massive_prestige_gain
eir_make_artifact_effect = { NAME = eir_arthur_armor_name DESC = eir_arthur_armor_desc TYPE = armor_mail VISUALS = armor MODIFIER = eir_arthur_armor_modifier }
title:c_cornwall ?= { add_county_modifier = { modifier = eir_arthur_site_modifier years = 25 } }""", 811)

path("crown", "The Crown of Britain",
     "A crown of red gold has been waiting in the hall at Caerleon for a king who is not a Roman, a Saxon or a Norman. Hold all of Wales, restore the old fortress and put it on.",
     "Needs the Arthurian legend, every county of Wales, the Caerleon fortress built and 3500 prestige. Gives the unique crown The Crown of Britain, the Lord of Caerleon modifier for 30 years and a Seat of the Pendragon's Memory at Caerleon. Once per game.",
     "eir_path_crown_done", ["eir_wales_all_trigger = yes", "eir_caerleon_built_trigger = yes", "prestige >= 3500"],
     cost(gold=1500, prestige=3500, piety=400),
     """add_character_modifier = { modifier = eir_path_crown_modifier years = 30 }
add_prestige = massive_prestige_gain
eir_make_artifact_effect = { NAME = eir_arthur_crown_name DESC = eir_arthur_crown_desc TYPE = regalia VISUALS = crown MODIFIER = eir_arthur_crown_modifier }
title:c_monmouthshire ?= { add_county_modifier = { modifier = eir_arthur_site_modifier years = 25 } }""", 812)

path("brooch", "The Brooch of Avalon",
     "The nuns of the Isle of Apples keep a brooch that is said to have fastened the cloak of the king who sleeps. They will give it to a lord of the Somerset levels who has earned the saints' regard.",
     "Needs the Arthurian legend, Somerset, a monastery of your own and 3000 piety. Gives the unique brooch The Brooch of Avalon, the Keeper of Avalon modifier for 30 years and a Seat of the Pendragon's Memory in Somerset. Once per game.",
     "eir_path_brooch_done", ["eir_holds_somerset_trigger = yes", "has_global_variable = eir_done_monastery", "piety >= 3000"],
     cost(gold=800, prestige=1500, piety=800),
     """add_character_modifier = { modifier = eir_path_brooch_modifier years = 30 }
add_prestige = major_prestige_gain
add_piety = massive_piety_gain
eir_make_artifact_effect = { NAME = eir_arthur_brooch_name DESC = eir_arthur_brooch_desc TYPE = brooch VISUALS = brooch MODIFIER = eir_arthur_brooch_modifier }
title:c_somerset ?= { add_county_modifier = { modifier = eir_arthur_site_modifier years = 25 } }""", 813, "decision_personal_religious")

path("spear", "Rhongomyniad, the Spear of Badon",
     "The Pendragon beat the Saxons so thoroughly at Badon that they did not attempt the west for a generation. Do the same to the English crown, and the ash spear he carried will be put in your hand.",
     "Needs the Arthurian legend, 60% of the counties of Britannia (56 of 93), prestige level 4 and Martial 24. Gives the unique spear Rhongomyniad, the Victor of Badon modifier for 30 years and a Seat of the Pendragon's Memory at Bath. Once per game.",
     "eir_path_spear_done", ["eir_brit_60_trigger = yes", "prestige_level >= 4", "martial >= 24"],
     cost(gold=2000, prestige=3000, piety=300),
     """add_character_modifier = { modifier = eir_path_spear_modifier years = 30 }
add_prestige = massive_prestige_gain
eir_make_artifact_effect = { NAME = eir_arthur_spear_name DESC = eir_arthur_spear_desc TYPE = spear VISUALS = spear MODIFIER = eir_arthur_spear_modifier }
title:c_somerset ?= { add_county_modifier = { modifier = eir_arthur_site_modifier years = 25 } }""", 814, "decision_siege_warfare")

path("table", "The Round Table",
     "A table with no head, big enough for a hundred and fifty. Build it at Tara, seat ten knights who have never quarrelled, and the old story will start telling itself.",
     "Needs the Arthurian legend, ten knights, the Hall of Tara built and Diplomacy 22. Gives the unique Round Table, the Lord of the Round Table modifier for 30 years and a Seat of the Pendragon's Memory in your capital. Once per game.",
     "eir_path_table_done", ["eir_ten_knights_trigger = yes", "eir_tara_built_trigger = yes", "diplomacy >= 22"],
     cost(gold=2500, prestige=2000, piety=300),
     """add_character_modifier = { modifier = eir_path_table_modifier years = 30 }
add_prestige = massive_prestige_gain
eir_make_artifact_effect = { NAME = eir_arthur_table_name DESC = eir_arthur_table_desc TYPE = tapestry VISUALS = tapestry MODIFIER = eir_arthur_table_modifier }
capital_county ?= { add_county_modifier = { modifier = eir_arthur_site_modifier years = 25 } }""", 815, "decision_invite_knights")

# ------------------------------------------------------------------------------------------------ the final decision
D("eir_final_revenge_decision", "The Last Revenge of the Celts",
  "Seven hundred years ago the Britons lost the island. Hold all but a handful of its counties, take your seat in the oldest hall of the Saxon kings, and tell the world the debt is paid.",
  "Needs the Arthurian legend, a Gaelic king and 95% of the counties of Britannia (89 of 93). Gives the Lord of the Whole Island modifier for 50 years, a third and final Ascendancy (up to 17% a year, every conversion with the -50 opinion Saxon uprising), the nickname 'the Last Hope of the Celts', prestige and legitimacy, Pride of the Island in every county, and a super-powered special building (about 2.5 times a wonder) that you place yourself at Winchester, York, Edinburgh, Caernarfon or Bath. Once per game.",
  GAEL + "\n" + HAS(DONE3) + "\n" + not_done("eir_done_final_revenge"),
  """add_character_modifier = { modifier = eir_brit_ascendancy_3_modifier years = 50 }
add_character_modifier = { modifier = eir_final_revenge_modifier years = 50 }
add_prestige = massive_prestige_gain
add_prestige = massive_prestige_gain
add_piety = major_piety_gain
add_legitimacy = major_legitimacy_gain
add_dread = medium_dread_gain
give_nickname = nick_eir_last_of_the_celts
every_sub_realm_county = {
	limit = { empire = title:e_britannia }
	add_county_modifier = { modifier = eir_island_pride_modifier years = 25 }
}
eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 12 }
eir_world_reacts_effect = yes
set_global_variable = eir_done_final_revenge
trigger_event = eir.0820""",
  valid=req("eir_gael_king_trigger = yes", HAS(DONE3), "eir_brit_95_trigger = yes", "is_at_war = no"),
  cost=cost(gold=2000, prestige=5000, piety=800), cd=36500, major=True, pic="decision_found_kingdom")
