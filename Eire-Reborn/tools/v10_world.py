"""Update 4 (Britannia) content pack: stacking Ascendancy modifiers, the Arthurian items, the Saxon uprising modifier, nicknames and names."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS

NICKS = [
    ("nick_eir_once_future_king", "the Once and Future King", "Drew the sword of the Britons and made the old island whole again."),
    ("nick_eir_last_of_the_celts", "the Last Hope of the Celts", "Took back the whole island that the Celts had lost, and the poems say it was always meant to be so."),
]
LOC = [
    ("eir_arthur_sword_name", "Caliburn, Sword of the Island"),
    ("eir_arthur_sword_desc", "The sword that the poets say Britain's last great king drew from the stone, found again, and carried by the king who made the island whole."),
    ("eir_arthur_armor_name", "The Mail of the Pendragon"),
    ("eir_arthur_armor_desc", "A coat of ring-mail that never rusts, said to have been worn at Badon and kept in the rock at Tintagel until the right man came for it."),
    ("eir_arthur_crown_name", "The Crown of Britain"),
    ("eir_arthur_crown_desc", "A circlet of red gold set with a dragon, kept in the hall at Caerleon for a king who had not yet been born."),
    ("eir_arthur_brooch_name", "The Brooch of Avalon"),
    ("eir_arthur_brooch_desc", "A great silver brooch kept by the nuns of the Isle of Apples, which is said to have fastened the cloak of the king who sleeps."),
    ("eir_arthur_spear_name", "Rhongomyniad, the Spear"),
    ("eir_arthur_spear_desc", "A long ash spear with a bronze head, carried by the Pendragon at Camlann and recovered from the field a lifetime later."),
    ("eir_arthur_table_name", "The Round Table"),
    ("eir_arthur_table_desc", "A circular table of oak, big enough to seat a hundred and fifty, where no knight sits at the head."),
]

# ------------------------------------------------------------------ the Ascendancy: each decision adds a stacking modifier that drives the yearly culture change
C("eir_brit_ascendancy_1_modifier", "prestige_positive", {"monthly_prestige": 0.5, "vassal_opinion": 5, "general_opinion": 3, "legitimacy_gain_mult": 0.1},
  "Gaelic Ascendancy in Britannia", "A third of the island answers to a Gaelic king. The old tongue is coming back at five times the pace, and the English are muttering.")
C("eir_brit_ascendancy_2_modifier", "prestige_positive", {"monthly_prestige": 0.7, "vassal_opinion": 6, "general_opinion": 4, "knight_effectiveness_mult": 0.1, "dread_gain_mult": 0.1},
  "The Gaelic Kingdoms United", "Ireland and Scotland answer to one crown. The culture of the island turns faster, and the English do more than mutter.")
C("eir_brit_ascendancy_3_modifier", "prestige_positive", {"monthly_prestige": 1.0, "vassal_opinion": 8, "general_opinion": 5, "advantage": 3, "dread_gain_mult": 0.2},
  "The Last Revenge of the Celts", "Ninety-five parts in a hundred of the island answer to the Celts. The pace of the change is a rout.")
K("eir_saxon_uprising_modifier", "county_modifier_control_negative", {"county_opinion_add": -50, "monthly_county_control_growth_add": -0.6, "tax_mult": -0.2, "levy_size": -0.2},
  "Saxon Uprising", "The county's language was changed by royal decree and its people have taken to the hedges with scythes. Unrest here is certain.")

# ------------------------------------------------------------------ the Arthurian decisions
C("eir_arthur_reborn_modifier", "prestige_positive",
  {"monthly_prestige": 2.0, "prowess": 5, "martial": 5, "knight_effectiveness_mult": 0.25, "advantage": 5, "dread_gain_mult": 0.3, "owned_legend_spread_mult": 0.5, "vassal_opinion": 12, "general_opinion": 8, "stress_gain_mult": -0.2},
  "Arthur Reborn", "The legend is no longer a story the Britons tell about a king who sleeps under a hill. It is a story about you.")
ARTIFACT["eir_arthur_sword_modifier"] = ("prowess_positive",
  {"prowess": 10, "knight_effectiveness_mult": 0.3, "monthly_prestige": 1.5, "dread_gain_mult": 0.3, "advantage": 6, "owned_legend_spread_mult": 0.5, "vassal_opinion": 10, "general_opinion": 10},
  "Caliburn, Sword of the Island", "The sword of the king who never died.")
ARTIFACT["eir_arthur_armor_modifier"] = ("prowess_positive", {"prowess": 4, "health": 0.3, "defender_advantage": 8, "advantage": 4, "stress_gain_mult": -0.25, "monthly_prestige": 0.5},
  "The Mail of the Pendragon", "A coat of ring-mail that never rusts.")
ARTIFACT["eir_arthur_crown_modifier"] = ("prestige_positive", {"monthly_prestige": 2.0, "legitimacy_gain_mult": 0.5, "vassal_opinion": 15, "court_grandeur_baseline_add": 20, "general_opinion": 10},
  "The Crown of Britain", "A circlet of red gold set with a dragon.")
ARTIFACT["eir_arthur_brooch_modifier"] = ("learning_positive", {"diplomacy": 6, "stewardship": 4, "courtier_and_guest_opinion": 20, "monthly_income": 6, "monthly_piety": 0.8, "fertility": 0.15},
  "The Brooch of Avalon", "A great silver brooch from the Isle of Apples.")
ARTIFACT["eir_arthur_spear_modifier"] = ("prowess_positive", {"martial": 8, "knight_limit": 5, "knight_effectiveness_mult": 0.3, "monthly_prestige": 0.8, "advantage": 3},
  "Rhongomyniad, the Spear", "The Pendragon's long ash spear.")
ARTIFACT["eir_arthur_table_modifier"] = ("learning_positive", {"learning": 4, "vassal_opinion": 20, "monthly_piety": 1.0, "knight_limit": 4, "monthly_prestige": 1.0},
  "The Round Table", "A circular oak table where no knight sits at the head.")

C("eir_path_armor_modifier", "prowess_positive", {"defender_advantage": 6, "health": 0.2, "monthly_prestige": 0.4, "stress_gain_mult": -0.1},
  "Heir of Tintagel", "You hold Cornwall, and the fortress where the Pendragon was said to be conceived. The rock gives something back.")
C("eir_path_crown_modifier", "prestige_positive", {"legitimacy_gain_mult": 0.3, "vassal_opinion": 10, "monthly_prestige": 0.6, "general_opinion": 6},
  "Lord of Caerleon", "All of Wales answers to you, and the old Roman fortress is called Arthur's court again.")
C("eir_path_brooch_modifier", "piety_positive", {"monthly_piety": 0.8, "clergy_opinion": 15, "diplomacy": 3, "health": 0.15},
  "Keeper of Avalon", "The nuns of the Isle of Apples have chosen you, and the fog on the Somerset levels rises when you walk through it.")
C("eir_path_spear_modifier", "prowess_positive", {"knight_effectiveness_mult": 0.2, "martial": 4, "knight_limit": 3, "advantage": 3, "monthly_prestige": 0.4},
  "Victor of Badon", "You hold most of the island, and the army is the best one on it.")
C("eir_path_table_modifier", "learning_positive", {"vassal_opinion": 12, "knight_limit": 3, "monthly_prestige": 0.6, "learning": 3, "general_opinion": 6},
  "Lord of the Round Table", "A hundred knights, no head to the table and not a single quarrel. The poets have run out of adjectives.")
C("eir_final_revenge_modifier", "prestige_positive",
  {"monthly_prestige": 3.0, "legitimacy_gain_mult": 0.5, "vassal_opinion": 20, "general_opinion": 15, "advantage": 6, "knight_effectiveness_mult": 0.3, "dread_gain_mult": 0.4, "owned_legend_spread_mult": 0.6, "court_grandeur_baseline_add": 25},
  "Lord of the Whole Island", "From the Orkneys to the Cornish tin-mines the island answers to the Celts, and the Celts have a long memory.")
K("eir_island_pride_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 15, "development_growth_factor": 0.15, "tax_mult": 0.1, "monthly_county_control_growth_add": 0.4, "levy_size": 0.1},
  "Pride of the Island", "A king rules the whole island, and the county knows it was part of the reason.")
K("eir_arthur_site_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 10, "development_growth_factor": 0.1, "tax_mult": 0.08, "hostile_raid_time": 0.5},
  "Seat of the Pendragon's Memory", "Pilgrims from three kingdoms come to stand where the king is said to have stood.")
