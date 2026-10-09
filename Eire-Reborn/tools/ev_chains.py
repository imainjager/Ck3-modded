"""Coronation chains, extra Celtic-world events, and extra artifacts."""
from evdsl import *

EVENTS = []

CROWNED = "eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_crowned"
BROTHER = "eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_brotherhood"

# -----------------------------------------------------------------------------
# 0110 The Coronation (fired by the kingdom decisions)
# -----------------------------------------------------------------------------
EVENTS.append(E(110, "The Coronation",
    "You have a new crown, and now you must decide how the island will see it worn.",
    "The crown is on the table. The bishops, the poets and the kings of the neighbouring lands are all looking at you, and none of them is looking kindly.\n\nA coronation is part law, part theatre, and part a promise you will have to keep.",
    [
        Opt("Hold a lavish coronation feast.",
            seq("remove_short_term_gold = medium_gold_value", "add_prestige = 200",
                "eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 8 }",
                "trigger_event = { id = eir.0111 years = 2 }"),
            stress="greedy = minor_stress_impact_gain", ai=40),
        Opt("Be anointed by the bishops.",
            seq("add_piety = 250", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }",
                "trigger_event = { id = eir.0111 years = 2 }"),
            stress="zealous = miniscule_stress_impact_loss", ai=30),
        Opt("Be crowned in the old way, with a poet to recite your line.",
            seq("add_prestige = 150", "add_character_modifier = { modifier = eir_fili_patron_modifier years = 8 }",
                "trigger_event = { id = eir.0111 years = 2 }"),
            trigger="has_global_variable = eir_done_fili", ai=40),
        Opt("Take the crown quietly, and save the gold.",
            seq("add_prestige = 50", "trigger_event = { id = eir.0111 years = 2 }"),
            stress="ambitious = minor_stress_impact_gain", ai=10),
    ],
    theme="court"))

# -----------------------------------------------------------------------------
# 0111 Neighbours react
# -----------------------------------------------------------------------------
EVENTS.append(E(111, "The Neighbours Take Notice",
    "Two years on, the other kings have decided what they think of your crown.",
    "Some of them send gifts. Some of them send spies. One of them has begun to talk about the proper order of kings, and which of them he thinks should wear the crown first.\n\nNone of it is surprising, and all of it needs an answer.",
    [
        Opt("Send gifts to the doubtful, and keep your army ready.",
            seq("remove_short_term_gold = minor_gold_value", "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 5 }",
                "eir_defender_levy_effect = yes"),
            ai=40),
        Opt("Boast of your lineage in front of the court.",
            RL((55, "reac_boast_good", "The court is impressed", [(10, "diplomacy >= 10")], "add_prestige = 100"),
               (45, "reac_boast_bad", "A rival laughs openly", [],
                "add_prestige = -50\nadd_character_modifier = { modifier = eir_satirised_modifier years = 2 }")),
            stress="humble = minor_stress_impact_gain", ai=30),
        Opt("Ask the other kings to a conference.",
            seq("add_prestige = 75", "add_character_modifier = { modifier = eir_oenach_afterglow_modifier years = 4 }"),
            trigger="diplomacy >= 9", ai=40),
    ],
    theme="diplomacy"))

# -----------------------------------------------------------------------------
# 0112 The Emperor of the Gael
# -----------------------------------------------------------------------------
EVENTS.append(E(112, "Emperor of the Gael",
    "No man has ever called himself Emperor of the Gael. The poets are writing the first verse.",
    "From Cork to Caithness, and across the sea to the Gaelic coasts, every Gael has heard the news. Some of them weep with joy. Some of them are already plotting.\n\nThe Pope, the Emperor and the kings of England are among the others.",
    [
        Opt("Be crowned at Tara, with the Stone of Destiny beneath your feet.",
            seq("add_prestige = 500", "add_piety = 100", "add_character_modifier = { modifier = eir_lia_fail_blessing_modifier years = 20 }"),
            stress="humble = minor_stress_impact_gain", ai=50),
        Opt("Ask the Pope to confirm the title.",
            seq("add_piety = 300", "add_prestige = 250", "remove_short_term_gold = major_gold_value"),
            ai=30),
        Opt("Declare it, and dare anyone to object.",
            seq("add_prestige = 300", "eir_defender_levy_effect = yes",
                "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 10 }"),
            stress="craven = miniscule_stress_impact_loss", ai=20),
    ],
    theme="legend"))

# -----------------------------------------------------------------------------
# 0076 Isle of Man
# -----------------------------------------------------------------------------
EVENTS.append(E(76, "A Crossroads of the Irish Sea",
    "The jarls of Man have realised that their island sits in the middle of everything.",
    "Ships from Dublin, Galloway, Wales and Norway cross at Man, and everyone who passes pays a toll. The jarls are rich, ambitious, and aware that you have the biggest army in the neighbourhood.\n\nThey have sent a polite delegation with a very generous offer.",
    [
        Opt("Accept their alliance and the trade that comes with it.",
            seq("add_gold = medium_gold_value", "add_character_modifier = { modifier = eir_sea_king_modifier years = 8 }"),
            ai=40),
        Opt("Ask them for ships rather than gold.",
            seq("eir_defender_levy_effect = yes", "add_prestige = 50"), ai=30),
        Opt("Demand their submission.",
            RL((40, "man_submits", "The jarls kneel", [(10, "prowess >= 12")], "add_prestige = 150"),
               (60, "man_refuses", "The jarls laugh and sail away", [], "add_prestige = -50")),
            stress="humble = minor_stress_impact_gain", ai=10),
    ],
    theme="diplomacy", cooldown=30,
    trigger=CROWNED + "\neir_has_coast_trigger = yes"))

# -----------------------------------------------------------------------------
# 0077 Cornish tin
# -----------------------------------------------------------------------------
EVENTS.append(E(77, "Tin from Cornwall",
    "Cornish traders arrive with ingots of tin, a rare metal, and a request for Irish gold.",
    "Their ancestors traded tin to the Phoenicians and to the Romans, and now they want to trade it to you. They claim Irish and Cornish folk are kin, and that kin should do business.\n\nThe tin is good, and the price is fair.",
    [
        Opt("Buy the tin and set up a bronze foundry.",
            seq("remove_short_term_gold = minor_gold_value", "add_character_modifier = { modifier = eir_cattle_rich_modifier years = 8 }"),
            ai=40),
        Opt("Offer a treaty of friendship with Cornwall.",
            seq("add_prestige = 75", "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 6 }"), ai=40),
        Opt("Decline politely.", "add_prestige = 5", ai=20),
    ],
    theme="diplomacy", cooldown=25, trigger=BROTHER))

# -----------------------------------------------------------------------------
# 0078 Breton rebirth
# -----------------------------------------------------------------------------
EVENTS.append(E(78, "The Breton Revival",
    "Poets in Brittany have begun singing in a tongue that sounds more like Welsh every year.",
    "The Breton nobles are weary of Frankish overlords and have begun to talk of the old kingdom. Their bards trade with yours, their saints are your saints, and their ships have begun to arrive in Irish ports.\n\nThey would like to know what you think.",
    [
        Opt("Send them an embassy and a gift of Irish gold.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 100", "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 5 }"),
            ai=40),
        Opt("Send them fighting men, quietly.",
            seq("remove_short_term_gold = medium_gold_value", "add_prestige = 75", "add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 4 }"),
            ai=30),
        Opt("Stay out of it.", "add_prestige = 5", ai=30),
    ],
    theme="diplomacy", cooldown=30, trigger=BROTHER))

# -----------------------------------------------------------------------------
# 0079 Welsh marcher troubles
# -----------------------------------------------------------------------------
EVENTS.append(E(79, "Marcher Troubles in Wales",
    "Anglo-Norman marcher lords are pushing deeper into Wales, and the Welsh kings are asking for help.",
    "Castles are going up in the river valleys. Welsh farmers are being turned off their land. The Welsh kings have sent an envoy across the sea to ask whether the Irish are willing to remember that their ancestors were kin.\n\nIt is not a small request.",
    [
        Opt("Send a company of Gallowglass.",
            seq("remove_short_term_gold = medium_gold_value", "add_prestige = 100", "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 6 }"),
            trigger="has_global_variable = eir_unlock_gallowglass", ai=40),
        Opt("Send gold and wise words.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 50"), ai=40),
        Opt("Tell them Ireland has troubles of its own.",
            seq("add_prestige = -25"), stress="compassionate = minor_stress_impact_gain", ai=20),
    ],
    theme="diplomacy", cooldown=30, trigger=BROTHER))

# -----------------------------------------------------------------------------
# 0084 The Cathach
# -----------------------------------------------------------------------------
EVENTS.append(E(84, "The Battle Psalter",
    "A psalter said to have been copied by a saint is offered to you as a talisman of victory.",
    "The monks say it was carried three times sunwise around the army before a great battle, and that the army won. The family that guards it is in debt, and would like to sell.\n\nIt is either a priceless relic or a rather clever fraud.",
    [
        Opt("Buy it, and carry it into battle.",
            seq("remove_short_term_gold = medium_gold_value",
                "eir_make_artifact_effect = { NAME = eir_cathach_name DESC = eir_cathach_desc TYPE = book VISUALS = book MODIFIER = eir_cathach_modifier }",
                "add_piety = 100"),
            ai=50),
        Opt("Persuade the monks to keep it, with a donation.",
            seq("remove_short_term_gold = minor_gold_value", "add_piety = 150"), ai=40),
        Opt("Refuse. A book does not win battles.",
            "add_prestige = 10", ai=10),
    ],
    theme="faith", cooldown=40,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_fili\ngold >= medium_gold_value"))

# -----------------------------------------------------------------------------
# 0085 The Tara Brooch
# -----------------------------------------------------------------------------
EVENTS.append(E(85, "The Great Brooch",
    "A goldsmith has made a brooch so large that it needs two hands to fasten.",
    "It is silver gilt, with gold filigree, amber and glass, and a pin the length of a man's forearm. It is utterly impractical, and every noble in Ireland will want one.\n\nThe goldsmith has made only one, and he has offered it to you first.",
    [
        Opt("Buy it and wear it at every feast.",
            seq("remove_short_term_gold = medium_gold_value",
                "eir_make_artifact_effect = { NAME = eir_tara_brooch_name DESC = eir_tara_brooch_desc TYPE = necklace VISUALS = necklace MODIFIER = eir_tara_brooch_modifier }",
                "add_prestige = 100"),
            ai=50),
        Opt("Commission a second one for your heir.", seq("remove_short_term_gold = medium_gold_value", "add_prestige = 150"), ai=30),
        Opt("Send him away. It is too much.", "add_prestige = 5", ai=20),
    ],
    theme="court", cooldown=40,
    trigger=CROWNED + "\ngold >= medium_gold_value"))

# -----------------------------------------------------------------------------
# 0086 The Cross of Cong
# -----------------------------------------------------------------------------
EVENTS.append(E(86, "A Cross for the Kings",
    "The abbot of a great monastery has commissioned a processional cross, and he wants your seal on it.",
    "It will be made of oak, covered with bronze and silver, and set with a crystal in the centre. It will contain a fragment of the True Cross, according to the abbot.\n\nHis request is for money and for your name at the foot of the inscription.",
    [
        Opt("Fund it, and be named as its patron.",
            seq("remove_short_term_gold = medium_gold_value",
                "eir_make_artifact_effect = { NAME = eir_cross_of_cong_name DESC = eir_cross_of_cong_desc TYPE = necklace VISUALS = necklace MODIFIER = eir_cross_of_cong_modifier }",
                "add_piety = 200"),
            ai=50),
        Opt("Give a smaller gift, without your name.", seq("remove_short_term_gold = minor_gold_value", "add_piety = 75"), ai=40),
        Opt("Decline politely.", "add_piety = -10", ai=10),
    ],
    theme="faith", cooldown=40,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_cashel\ngold >= medium_gold_value"))
