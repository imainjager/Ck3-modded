"""The tanistic collapse: what happens when an Irish king dies and his highest title dies with him."""
from evdsl import *

EVENTS = []

# -----------------------------------------------------------------------------
# 0001 The Kingdom Unravels  (fired at the heir by eir_collapse_top_title_effect)
# -----------------------------------------------------------------------------
EVENTS.append(E(1, "The Kingdom Unravels",
    "[eir_dead_king.GetShortUIName] is dead, and the title of [eir_collapsing_title.GetName] died with [eir_dead_king.GetHerHim].",
    "In Ireland a kingdom was a man, and the man is gone. The title that held it together is broken, and every kinsman who ever dreamed of a crown is already counting spearmen.\n\nWhat you do in the next few weeks will decide whether you inherit a realm or only a quarrel.",
    [
        Opt("Gather the kin at Tara before anyone else does.",
            RL((55, "kin_swear", "The kin swear to you at Tara.",
                [(15, "diplomacy >= 14"), (10, "has_trait = gregarious")],
                seq("remove_character_modifier = eir_throne_turmoil_modifier",
                    "add_character_modifier = { modifier = eir_peace_of_tara_modifier years = 5 }",
                    "add_prestige = 100")),
               (35, "kin_refuse", "The kin quarrel, and the turmoil deepens.",
                [],
                seq("add_character_modifier = { modifier = eir_kin_strife_modifier years = 5 }"))),
            trigger="""OR = {
	diplomacy >= 10
	has_trait = gregarious
	has_trait = diplomat
}""",
            stress="shy = minor_stress_impact_gain\ngregarious = miniscule_stress_impact_loss"),
        Opt("Buy the loyalty of your uncles with cattle and gold.",
            seq("remove_short_term_gold = medium_gold_value",
                "remove_character_modifier = eir_throne_turmoil_modifier",
                "random_close_family_member = {\n\tlimit = { is_adult = yes is_alive = yes }\n\tadd_opinion = { target = root modifier = eir_fostered_opinion opinion = 25 }\n}"),
            stress="greedy = minor_stress_impact_gain\ngenerous = miniscule_stress_impact_loss"),
        Opt("Let them squabble. The strongest will rule.",
            seq("add_character_modifier = { modifier = eir_kin_strife_modifier years = 5 }",
                "add_prestige = 100",
                "eir_trait_effect = { TRAIT = ambitious OPPOSITE = content CHANCE = 20 }",
                "trigger_event = { id = eir.0002 years = { 1 2 } }"),
            stress="compassionate = minor_stress_impact_gain\nforgiving = miniscule_stress_impact_gain\nambitious = miniscule_stress_impact_loss"),
    ],
    theme="dread",
    immediate="add_character_modifier = { modifier = eir_throne_turmoil_modifier years = 5 }"))

# -----------------------------------------------------------------------------
# 0002 The Tanist's Challenge
# -----------------------------------------------------------------------------
EVENTS.append(E(2, "The Tanist's Challenge",
    "[eir_rival.GetShortUIName] says the throne should have been [eir_rival.GetHerHis].",
    "Under the old law any man of the royal kin could be chosen, and your kinsman has never accepted that it was you. [eir_rival.GetSheHe|U] has friends, spears, and a poet who sings of [eir_rival.GetHerHis] claim.\n\nIf you let this fester, it will become a feud. If you crush it badly, it will become a legend.",
    [
        Opt("Give [eir_rival.GetShortUIName] a share of the realm.",
            seq("remove_short_term_gold = medium_gold_value",
                "scope:eir_rival = { add_opinion = { target = root modifier = grateful_opinion opinion = 30 } }",
                "if = {\n\tlimit = { has_character_modifier = eir_kin_strife_modifier }\n\tremove_character_modifier = eir_kin_strife_modifier\n}",
                "add_hook = { target = scope:eir_rival type = favor_hook }"),
            stress="greedy = miniscule_stress_impact_gain\ngenerous = miniscule_stress_impact_loss"),
        Opt("Meet the challenge on the field of honour.",
            RL((55, "challenge_won", "[eir_rival.GetShortUIName] yields before the whole court.",
                [(15, "martial >= 14"), (10, "prowess >= 14")],
                seq("add_prestige = 150",
                    "scope:eir_rival = { add_opinion = { target = root modifier = eir_ard_ri_opinion opinion = 15 } }",
                    "if = {\n\tlimit = { has_character_modifier = eir_kin_strife_modifier }\n\tremove_character_modifier = eir_kin_strife_modifier\n}")),
               (35, "challenge_lost", "You are bested, and the court whispers.",
                [],
                seq("add_prestige = -100",
                    "add_character_modifier = { modifier = eir_throne_turmoil_modifier years = 3 }"))),
            trigger="""OR = {
	martial >= 10
	has_trait = brave
	prowess >= 12
}""",
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss"),
        Opt("Have [eir_rival.GetShortUIName] quietly removed.",
            RL((60, "rival_removed", "[eir_rival.GetShortUIName] dies of a sudden fever.",
                [(15, "intrigue >= 14")],
                seq("scope:eir_rival = { death = { death_reason = death_murder killer = root } }",
                    "dynasty ?= { add_dynasty_modifier = { modifier = eir_house_kinslayers_modifier years = 20 } }",
                    "eir_vassal_opinion_effect = { MODIFIER = eir_kinslayer_opinion OPINION = -15 }",
                    "eir_trait_effect = { TRAIT = callous OPPOSITE = compassionate CHANCE = 30 }",
                    "if = {\n\tlimit = { has_character_modifier = eir_kin_strife_modifier }\n\tremove_character_modifier = eir_kin_strife_modifier\n}")),
               (30, "plot_exposed", "The plot is exposed, and your kin turn on you.",
                [],
                seq("add_character_modifier = { modifier = eir_kin_strife_modifier years = 8 }",
                    "scope:eir_rival = { add_opinion = { target = root modifier = eir_tanist_rival_opinion opinion = -50 } }",
                    "dynasty ?= { add_dynasty_modifier = { modifier = eir_house_kinslayers_modifier years = 10 } }"))),
            trigger="""OR = {
	intrigue >= 10
	has_trait = schemer
	has_trait = deceitful
}""",
            stress="honest = minor_stress_impact_gain\njust = minor_stress_impact_gain\ncompassionate = minor_stress_impact_gain\ndeceitful = miniscule_stress_impact_loss"),
        Opt("Send [eir_rival.GetShortUIName] to a monastery for the good of [eir_rival.GetHerHis] soul.",
            seq("remove_courtier_or_guest = scope:eir_rival",
                "scope:eir_rival = { add_opinion = { target = root modifier = eir_tanist_rival_opinion opinion = -20 } }",
                "add_piety = 50",
                "dynasty ?= { add_dynasty_modifier = { modifier = eir_house_exiles_modifier years = 10 } }"),
            stress="forgiving = miniscule_stress_impact_loss"),
    ],
    theme="family",
    trigger="""any_close_family_member = {
	is_adult = yes
	is_alive = yes
}""",
    immediate="random_close_family_member = {\n\tlimit = { is_adult = yes is_alive = yes NOT = { this = root } }\n\tsave_scope_as = eir_rival\n}",
    portraits="left_portrait = {\n\tcharacter = scope:eir_rival\n\tanimation = anger\n}"))

# -----------------------------------------------------------------------------
# 0003 A Poet's Lament
# -----------------------------------------------------------------------------
EVENTS.append(E(3, "A Poet's Lament",
    "A poet stands up in your hall to sing the lament of the fallen kingship.",
    "The old kingship is in pieces, and the poet is not shy about saying why. Every line is a little too accurate. Every pause is a little too long.\n\nThe court is watching to see what you do about it.",
    [
        Opt("Pay the poet handsomely and ask for a second verse about yourself.",
            seq("remove_short_term_gold = minor_gold_value",
                "add_character_modifier = { modifier = eir_fili_patron_modifier years = 5 }",
                "add_prestige = 75"),
            stress="greedy = miniscule_stress_impact_gain"),
        Opt("Have the poet thrown out of the hall.",
            seq("add_character_modifier = { modifier = eir_satirised_modifier years = 5 }",
                "eir_court_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -10 }",
                "eir_trait_effect = { TRAIT = wrathful OPPOSITE = calm CHANCE = 20 }"),
            stress="wrathful = miniscule_stress_impact_loss\ncalm = minor_stress_impact_gain"),
        Opt("Answer with a verse of your own.",
            seq(RL((60, "verse_lands", "The court roars its approval.",
                    [(15, "learning >= 12"), (10, "diplomacy >= 12")],
                    "add_prestige = 150\nadd_character_modifier = { modifier = eir_fili_patron_modifier years = 5 }"),
                   (30, "verse_falls", "Your verse is mocked, and the poet wins the crowd.",
                    [],
                    "add_character_modifier = { modifier = eir_satirised_modifier years = 3 }"))),
            trigger="learning >= 8",
            stress="shy = miniscule_stress_impact_gain"),
    ],
    theme="learning",
    cooldown=15,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no"))
