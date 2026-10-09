"""Foreign lords (English, Norman, French) arriving in Ireland, usually at a rival's invitation."""
from evdsl import *

EVENTS = []

FOREIGN_AVAILABLE = """any_ruler = {
	is_ai = yes
	is_ruler = yes
	highest_held_title_tier >= tier_county
	culture ?= {
		OR = {
			has_cultural_pillar = heritage_west_germanic
			has_cultural_pillar = heritage_frankish
		}
	}
	is_at_war = no
	NOT = { has_truce = root }
	NOT = { this = root }
}"""

# -----------------------------------------------------------------------------
# 0020 Foreign Sails
# -----------------------------------------------------------------------------
EVENTS.append(E(20, "Foreign Sails",
    "[eir_foreign_lord.GetShortUIName] has landed a foreign host in [eir_target_county.GetName], at the invitation of one of your own rivals.",
    "A quarrelling Irish lord has done what Irish lords have always done: offered land and a daughter to the first strong foreigner who would fight for him. The foreigner has arrived with mailed horsemen and archers, and a letter that says he has come to bring order.\n\nThe Irish will have order, whether they want it or not.",
    [
        Opt("Gather the clans and meet them in the field.",
            "eir_foreign_invasion_effect = yes",
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=60),
        Opt("Call on the Celtic brotherhood for axes and archers.",
            seq("eir_defender_levy_effect = yes",
                "eir_defender_levy_effect = yes",
                "eir_foreign_invasion_effect = yes",
                "add_prestige = 50"),
            trigger="has_global_variable = eir_done_brotherhood",
            stress="shy = miniscule_stress_impact_gain", ai=40),
        Opt("Appeal to the Church to condemn the invaders.",
            RL((50, "church_condemns", "The bishops condemn the invasion, and the foreign lord withdraws.",
                [(20, "has_trait = zealous"), (10, "piety >= 300")],
                seq("add_piety = 100", "add_prestige = 100",
                    "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }")),
               (40, "church_silent", "The bishops mutter, and the foreign host marches.",
                [],
                seq("add_piety = -25", "eir_foreign_invasion_effect = yes"))),
            trigger="piety >= 100",
            stress="cynical = miniscule_stress_impact_gain", ai=15),
        Opt("Buy the foreign lord's loyalty with land and a title.",
            seq("remove_short_term_gold = major_gold_value",
                "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 8 }",
                "scope:eir_foreign_lord = { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 30 } }"),
            stress="arrogant = minor_stress_impact_gain", ai=10),
    ],
    theme="war",
    cooldown=15,
    trigger=f"""eir_is_irish_ruler_trigger = yes
is_ai = no
current_year >= 1090
eir_has_coast_trigger = yes
is_at_war = no
NOT = {{ has_character_flag = eir_foreign_cooldown }}
{FOREIGN_AVAILABLE}""",
    immediate="""eir_pick_foreign_invasion_effect = yes
add_character_flag = { flag = eir_foreign_cooldown years = 10 }""",
    portraits="left_portrait = {\n\tcharacter = scope:eir_foreign_lord\n\tanimation = personality_bold\n}"))

# -----------------------------------------------------------------------------
# 0021 Foreign Lords in Ireland   (attacker won)
# -----------------------------------------------------------------------------
EVENTS.append(E(21, "Foreign Lords in Ireland",
    "[eir_foreign_lord.GetShortUIName] has won, and [eir_target_county.GetName] now has a castle of stone.",
    "The foreign knights rode over the Irish levies like wheat, and their archers did the rest. A stone keep is going up on the hill, built by men who do not speak Irish and do not want to learn.\n\nThe castle is the first of many, if you let it be.",
    [
        Opt("Swear to drive them out. (Unlocks a decision.)",
            seq("add_prestige = 50",
                "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 8 }",
                "add_character_flag = eir_oath_to_reclaim"),
            stress="forgiving = miniscule_stress_impact_gain\nvengeful = miniscule_stress_impact_loss", ai=60),
        Opt("Do homage to the foreign lord for the county.",
            seq("add_prestige = -100",
                "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 10 }",
                "scope:eir_foreign_lord = { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 30 } }"),
            stress="arrogant = minor_stress_impact_gain\nbrave = minor_stress_impact_gain", ai=5),
        Opt("Raise a hundred clans and burn the castle before it is finished.",
            RL((45, "castle_burns", "The unfinished castle burns, and the masons flee.",
                [(15, "martial >= 14"), (10, "has_trait = brave")],
                seq("add_prestige = 150",
                    "scope:eir_target_county ?= { remove_county_modifier = eir_foreign_lords_county_modifier }",
                    "eir_trait_effect = { TRAIT = brave OPPOSITE = craven CHANCE = 30 }")),
               (40, "castle_holds", "The garrison holds, and the clans scatter with losses.",
                [],
                seq("add_prestige = -50", "add_character_modifier = { modifier = eir_throne_turmoil_modifier years = 2 }"))),
            trigger="""OR = {
	martial >= 10
	has_trait = brave
}""",
            stress="craven = minor_stress_impact_gain", ai=30),
    ],
    theme="war",
    immediate="""scope:eir_target_county ?= { add_county_modifier = { modifier = eir_foreign_lords_county_modifier years = 10 } }
add_character_modifier = { modifier = eir_foreign_lords_modifier years = 5 }""",
    portraits="left_portrait = {\n\tcharacter = scope:eir_foreign_lord\n\tanimation = schadenfreude\n}"))

# -----------------------------------------------------------------------------
# 0022 The Foreign Host Is Broken   (defender won)
# -----------------------------------------------------------------------------
EVENTS.append(E(22, "The Foreign Host Is Broken",
    "The foreign host has been broken, and [eir_foreign_lord.GetShortUIName] has fled.",
    "The mailed horsemen floundered in the bog, the archers ran out of arrows, and the Irish did what the Irish have always done to armies that come into their hills and woods.\n\nThe foreign lord is in flight, and every poet in the country is composing a victory song.",
    [
        Opt("Give thanks and ride home in triumph.",
            seq("add_prestige = 250", "add_piety = 50",
                "add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 8 }"),
            ai=50),
        Opt("Pursue the foreign lord and make an example of him.",
            seq("add_prestige = 150", "add_dread = minor_dread_gain",
                "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 10 }",
                "eir_trait_effect = { TRAIT = wrathful OPPOSITE = calm CHANCE = 20 }"),
            stress="forgiving = miniscule_stress_impact_gain\nwrathful = miniscule_stress_impact_loss", ai=30),
        Opt("Offer the foreign lord peace in exchange for a rich ransom.",
            seq("add_gold = major_gold_value", "add_prestige = 75",
                "scope:eir_foreign_lord = { add_opinion = { target = root modifier = eir_norse_defied_opinion opinion = -15 } }"),
            stress="greedy = miniscule_stress_impact_loss", ai=20),
    ],
    theme="war",
    portraits="left_portrait = {\n\tcharacter = scope:eir_foreign_lord\n\tanimation = fear\n}"))
