"""The Viking age and the rise of Brian Boru, c. 867-1066. Each fires once, inside a window of years."""
from evdsl import *

EVENTS = []


def gate(start, end, flag, extra=""):
    t = ("eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= %d\ncurrent_year <= %d\n"
         "NOT = { has_global_variable = %s }" % (start, end, flag))
    return t + ("\n" + extra if extra else "")


# -----------------------------------------------------------------------------
# 0100 The Longphort at Duiblinn
# -----------------------------------------------------------------------------
EVENTS.append(E(100, "The Longphort at Duiblinn",
    "The Norse have built a fortified ship-camp at the Black Pool, and they are not leaving.",
    "It began as a place to beach longships and winter. Now there are palisades, a slave market and a smith's yard, and the Norse trade with anyone who will deal with them.\n\nThe local lords are uncertain whether to burn it or to sell it cattle.",
    [
        Opt("Burn the camp before it grows. (Raise a muster and add a Norse enemy.)",
            seq("eir_defender_levy_effect = yes", "add_prestige = 75", "set_global_variable = eir_hist_0867"),
            trigger="OR = {\nprowess >= 8\nmartial >= 10\n}", stress="craven = minor_stress_impact_gain", ai=40),
        Opt("Trade with them. Their silver is as good as anyone's.",
            seq("add_gold = medium_gold_value", "add_character_modifier = { modifier = eir_cattle_rich_modifier years = 8 }",
                "set_global_variable = eir_hist_0867"),
            stress="zealous = minor_stress_impact_gain\ngreedy = miniscule_stress_impact_loss", ai=40),
        Opt("Hire Norse axemen to fight your rivals.",
            seq("remove_short_term_gold = minor_gold_value", "eir_defender_levy_effect = yes",
                "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 4 }", "set_global_variable = eir_hist_0867"),
            ai=20),
        Opt("Ignore them. There are enough enemies nearer home.",
            "set_global_variable = eir_hist_0867", ai=10),
    ],
    theme="war", cooldown=100,
    trigger=gate(867, 940, "eir_hist_0867", "eir_has_coast_trigger = yes")))

# -----------------------------------------------------------------------------
# 0101 Cerball and the Norse
# -----------------------------------------------------------------------------
EVENTS.append(E(101, "The Cunning King of Osraige",
    "A king of Osraige plays the Norse against the Irish, and wins both ways.",
    "He takes Norse silver one season and sends Irish spears against them the next. His rivals are furious. His treasury is full.\n\nHe has sent you a messenger with a rather elegant offer.",
    [
        Opt("Take his offer, and learn his trick.",
            seq("add_character_modifier = { modifier = eir_hospitality_modifier years = 6 }", "add_prestige = 50",
                "set_global_variable = eir_hist_0870"),
            trigger="OR = {\ndiplomacy >= 10\nintrigue >= 10\n}", ai=40),
        Opt("Take his silver, and refuse his politics.",
            seq("add_gold = minor_gold_value", "set_global_variable = eir_hist_0870"),
            ai=30),
        Opt("Denounce him to the other Irish kings.",
            seq("add_prestige = 75", "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 5 }",
                "set_global_variable = eir_hist_0870"),
            stress="honest = miniscule_stress_impact_loss", ai=30),
    ],
    theme="diplomacy", cooldown=100,
    trigger=gate(870, 920, "eir_hist_0870")))

# -----------------------------------------------------------------------------
# 0102 The Norse return
# -----------------------------------------------------------------------------
EVENTS.append(E(102, "The Return of the Longships",
    "The Norse were driven out of Dublin, and now their ships are back in the bay.",
    "For fifteen years the Irish had the Black Pool to themselves. The Norse have spent that time in exile, hiring ships and nursing a grudge.\n\nThe new fleet is bigger than the old one, and its leaders are not the same men.",
    [
        Opt("Raise the host and meet them on the beach.",
            seq("eir_defender_levy_effect = yes", "add_prestige = 100", "set_global_variable = eir_hist_0917"),
            stress="craven = minor_stress_impact_gain", ai=40),
        Opt("Pay them to leave. (They will come back.)",
            seq("remove_short_term_gold = medium_gold_value", "add_character_modifier = { modifier = eir_danegeld_modifier years = 5 }",
                "set_global_variable = eir_hist_0917"),
            ai=20),
        Opt("Invite their lords to a feast and make them oaths.",
            seq("add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }", "add_prestige = 50",
                "set_global_variable = eir_hist_0917"),
            trigger="diplomacy >= 9", ai=40),
    ],
    theme="war", cooldown=100,
    trigger=gate(917, 960, "eir_hist_0917", "eir_has_coast_trigger = yes")))

# -----------------------------------------------------------------------------
# 0103 The Battle of Tara
# -----------------------------------------------------------------------------
EVENTS.append(E(103, "The Battle of Tara",
    "A High King of Tara is about to fight the Norse of Dublin on the old royal hill.",
    "Máel Sechnaill of Meath is calling his allies. The Norse of Dublin and the Isles have brought a fleet, a lot of axes and a greater confidence than they deserve.\n\nEvery king who has ever knelt at Tara has a reason to be there.",
    [
        Opt("March to Tara and fight beside the High King.",
            RL((60, "tara_victory", "The Norse are broken", [(10, "prowess >= 10")],
                seq("add_prestige = 250", "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 10 }",
                    "eir_trait_effect = { TRAIT = eir_viking_slayer OPPOSITE = craven CHANCE = 35 }")),
               (30, "tara_costly", "A bloody victory", [],
                seq("add_prestige = 100", "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 5 }",
                    "remove_short_term_gold = minor_gold_value")),
               (10, "tara_wounded", "You are badly hurt", [],
                seq("add_prestige = 50", "increase_wounds_effect = { REASON = battle }"))),
            "set_global_variable = eir_hist_0980",
            stress="craven = minor_stress_impact_gain", ai=50),
        Opt("Send men and gold, and stay at home.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 50", "set_global_variable = eir_hist_0980"),
            ai=30),
        Opt("Offer the Norse an alliance against the High King.",
            seq("add_gold = medium_gold_value", "add_prestige = -100", "set_global_variable = eir_hist_0980",
                "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 6 }"),
            stress="honest = minor_stress_impact_gain", ai=5),
    ],
    theme="war", cooldown=100,
    trigger=gate(980, 1010, "eir_hist_0980")))

# -----------------------------------------------------------------------------
# 0104 Brian Boru rises
# -----------------------------------------------------------------------------
EVENTS.append(E(104, "A Brother from Dál gCais",
    "A younger son of a minor Munster house has taken the kingship of Munster and wants more.",
    "His brother was murdered, so he avenged him. Then he took Cashel, then he took Limerick from the Norse. He is not a man with limits.\n\nHe has sent you a message, and it asks for your submission.",
    [
        Opt("Submit, and take a share of his triumph.",
            seq("add_prestige = 50", "add_character_modifier = { modifier = eir_hospitality_modifier years = 8 }",
                "set_global_variable = eir_hist_0976"),
            stress="arrogant = minor_stress_impact_gain", ai=30),
        Opt("Refuse, and rally the other kings against him.",
            seq("add_prestige = 100", "eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 5 }",
                "eir_defender_levy_effect = yes", "set_global_variable = eir_hist_0976"),
            stress="humble = minor_stress_impact_gain", ai=40),
        Opt("Offer a daughter in marriage and a fosterage.",
            seq("add_character_modifier = { modifier = eir_foster_ties_modifier years = 15 }", "add_prestige = 25",
                "set_global_variable = eir_hist_0976"),
            trigger="diplomacy >= 9", ai=30),
    ],
    theme="diplomacy", cooldown=100,
    trigger=gate(976, 1005, "eir_hist_0976")))

# -----------------------------------------------------------------------------
# 0105 Clontarf
# -----------------------------------------------------------------------------
EVENTS.append(E(105, "Good Friday at Clontarf",
    "The High King is marching on Dublin, and the Norse are bringing every ally they can.",
    "The Norse of Dublin, the Isles and Orkney will fight beside the men of Leinster. The High King will fight with Munster, Meath and Connacht.\n\nThere is a battle coming, on the shore at Clontarf, and every Irish ruler is expected to pick a side.",
    [
        Opt("March with the High King.",
            RL((55, "clontarf_victory", "The Norse are broken", [(10, "prowess >= 12")],
                seq("add_prestige = 400", "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 15 }",
                    "eir_trait_effect = { TRAIT = eir_viking_slayer OPPOSITE = craven CHANCE = 45 }")),
               (30, "clontarf_costly", "Victory at a terrible price", [],
                seq("add_prestige = 200", "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 8 }",
                    "add_character_modifier = { modifier = eir_kin_strife_modifier years = 3 }")),
               (15, "clontarf_wounded", "You fall in the shield-wall", [],
                seq("add_prestige = 100", "increase_wounds_effect = { REASON = battle }"))),
            "set_global_variable = eir_hist_1014",
            stress="craven = minor_stress_impact_gain", ai=50),
        Opt("Fight for Leinster and the Norse.",
            seq("add_prestige = 50", "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 5 }",
                "set_global_variable = eir_hist_1014"),
            stress="honest = minor_stress_impact_gain", ai=15),
        Opt("Stay at home and keep your army whole.",
            seq("add_prestige = -50", "set_global_variable = eir_hist_1014"),
            stress="brave = minor_stress_impact_gain", ai=30),
    ],
    theme="war", cooldown=100,
    trigger=gate(1014, 1025, "eir_hist_1014")))

# -----------------------------------------------------------------------------
# 0106 After Clontarf
# -----------------------------------------------------------------------------
EVENTS.append(E(106, "The Morning After Clontarf",
    "The High King is dead, and no one is strong enough to replace him.",
    "The old man and his son died on the same day, and half the kings of Munster died with them. The Norse of Dublin are still in Dublin.\n\nAll of Ireland is now asking the same question: who is next?",
    [
        Opt("Put yourself forward as the next High King.",
            seq("add_prestige = 150", "eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 4 }",
                "set_global_variable = eir_hist_1015"),
            stress="humble = minor_stress_impact_gain\nambitious = miniscule_stress_impact_loss", ai=40),
        Opt("Support Máel Sechnaill, who has taken the high kingship back.",
            seq("add_prestige = 75", "add_character_modifier = { modifier = eir_oenach_afterglow_modifier years = 4 }",
                "set_global_variable = eir_hist_1015"),
            ai=40),
        Opt("Carve out your own little kingdom while the great ones fight.",
            seq("add_gold = medium_gold_value", "add_character_modifier = { modifier = eir_lean_years_modifier years = 3 }",
                "set_global_variable = eir_hist_1015"),
            stress="content = miniscule_stress_impact_loss", ai=20),
    ],
    theme="court", cooldown=100,
    trigger=gate(1015, 1030, "eir_hist_1015")))

# -----------------------------------------------------------------------------
# 0107 The King of Leinster
# -----------------------------------------------------------------------------
EVENTS.append(E(107, "The Kingmaker of Leinster",
    "The king of Leinster has taken Dublin and wants to be a High King himself.",
    "He is a strong king, and the Norse of Dublin are his vassals. He has taken the Isle of Man too, and he lacks only the title.\n\nHe has asked for your support, with a hint of what happens to people who say no.",
    [
        Opt("Back his claim to the high kingship.",
            seq("add_prestige = 75", "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 4 }",
                "set_global_variable = eir_hist_1052"),
            ai=30),
        Opt("Refuse him, and prepare for his revenge.",
            seq("eir_defender_levy_effect = yes", "add_prestige = 50", "set_global_variable = eir_hist_1052"),
            stress="craven = minor_stress_impact_gain", ai=40),
        Opt("Offer a marriage alliance instead.",
            seq("add_character_modifier = { modifier = eir_foster_ties_modifier years = 8 }", "set_global_variable = eir_hist_1052"),
            trigger="diplomacy >= 9", ai=30),
    ],
    theme="diplomacy", cooldown=100,
    trigger=gate(1052, 1066, "eir_hist_1052")))
