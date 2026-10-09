"""Artifacts and rewards that arrive as the story of Irish revival unfolds."""
from evdsl import *

EVENTS = []

# -----------------------------------------------------------------------------
# 0080 The Gospel Is Finished  (five years after founding the scriptorium)
# -----------------------------------------------------------------------------
EVENTS.append(E(80, "The Gospel Is Finished",
    "The monks of your scriptorium have completed a gospel book of astonishing beauty.",
    "Five years of work went into it: calfskin vellum, pigments from three continents, and ornamental pages so intricate that the artists went blind in their old age. It is a book that is more than a book.\n\nThe abbot has brought it to you himself, and he does not look like he wants to hand it over.",
    [
        Opt("Keep it in your own chapel.",
            seq("eir_make_artifact_effect = { NAME = eir_book_of_kells_name DESC = eir_book_of_kells_desc TYPE = book VISUALS = book MODIFIER = eir_book_of_kells_modifier }",
                "add_piety = 100", "add_prestige = 150"),
            ai=50),
        Opt("Give it back to the abbey and ask only that pilgrims may see it.",
            seq("add_piety = 300", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }",
                "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_monastic_city_modifier years = 25 }\n}"),
            ai=40),
        Opt("Present it to the Pope as a gift of the Irish Church.",
            seq("add_piety = 400", "add_prestige = 100", "add_character_modifier = { modifier = eir_synod_reform_modifier years = 8 }"),
            ai=10),
    ],
    theme="learning"))

# -----------------------------------------------------------------------------
# 0081 The Chalice
# -----------------------------------------------------------------------------
EVENTS.append(E(81, "A Silver Chalice in a Potato Field",
    "A boy digging in a field has found a silver chalice, buried with a hoard.",
    "It is a magnificent piece of silver and gold, ornamented with interlace patterns and set with amber and glass. It is also, by the law of the land, the property of whoever owns the field, which is you.\n\nThe boy is looking at you hopefully.",
    [
        Opt("Reward the boy and place the chalice on the altar of your chapel.",
            seq("eir_make_artifact_effect = { NAME = eir_ardagh_chalice_name DESC = eir_ardagh_chalice_desc TYPE = goblet VISUALS = goblet MODIFIER = eir_ardagh_chalice_modifier }",
                "remove_short_term_gold = minor_gold_value", "add_piety = 150"),
            ai=50),
        Opt("Give it to the Church.",
            "add_piety = 300\nadd_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }",
            ai=30),
        Opt("Melt it down.",
            "add_gold = major_gold_value\nadd_piety = -100",
            stress="zealous = minor_stress_impact_gain", ai=10),
    ],
    theme="faith", cooldown=40,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_cashel"))

# -----------------------------------------------------------------------------
# 0082 The Torc from the Bog
# -----------------------------------------------------------------------------
EVENTS.append(E(82, "The Torc from the Bog",
    "Among the hoard dug from the bog is a great gold torc, older than any king of Ireland.",
    "It is a heavy twisted collar of gold, finely made, with terminals shaped like beasts. It is the kind of thing a king of Tara would have worn, long before the Church, long before the Norse, long before anything the chroniclers remember.\n\nA man who wore it might feel the weight of every king before him.",
    [
        Opt("Wear it at your coronation, and at every great feast.",
            seq("eir_make_artifact_effect = { NAME = eir_torc_of_tara_name DESC = eir_torc_of_tara_desc TYPE = miscellaneous VISUALS = necklace MODIFIER = eir_torc_of_tara_modifier }",
                "add_prestige = 200", "add_character_modifier = { modifier = eir_lia_fail_blessing_modifier years = 5 }"),
            ai=50),
        Opt("Place it with the royal regalia, to be worn only by the High King.",
            seq("add_prestige = 100", "dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 15 } }"),
            ai=30),
        Opt("Melt it into coin.",
            "add_gold = major_gold_value\nadd_prestige = -50",
            stress="arrogant = minor_stress_impact_gain", ai=10),
    ],
    theme="legend"))

# -----------------------------------------------------------------------------
# 0083 A Sword for the Champion
# -----------------------------------------------------------------------------
EVENTS.append(E(83, "A Sword for the Champion",
    "A smith presents you with a sword the poets say belonged to a hero of the Red Branch.",
    "He swears it was found in a cairn in Ulster, buried with its owner, and that it still has the edge. The poets say it is Caladbolg, the sword that struck three hills flat. The smith would settle for a suitable reward.\n\nIt is certainly an extraordinary blade.",
    [
        Opt("Reward the smith and wear the sword yourself.",
            seq("eir_make_artifact_effect = { NAME = eir_caladbolg_name DESC = eir_caladbolg_desc TYPE = sword VISUALS = sword MODIFIER = eir_caladbolg_modifier }",
                "remove_short_term_gold = minor_gold_value", "add_prestige = 100"),
            trigger="prowess >= 8", ai=50),
        Opt("Present the sword to your champion.",
            seq("add_prestige = 75", "add_character_modifier = { modifier = eir_fianna_spirit_modifier years = 8 }"),
            ai=40),
        Opt("Hang it in the hall as a token of Ulster's heritage.",
            "add_prestige = 50\nadd_character_modifier = { modifier = eir_hearth_of_the_gael_modifier years = 8 }",
            ai=20),
    ],
    theme="martial", cooldown=40,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_unlock_fianna"))
