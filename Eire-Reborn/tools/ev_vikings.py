"""The Norse: landings, ransoms, monasteries, and what comes after a victory or a defeat."""
from evdsl import *

EVENTS = []

NORSE_AVAILABLE = """any_ruler = {
	is_ai = yes
	is_ruler = yes
	highest_held_title_tier >= tier_county
	culture ?= { has_cultural_pillar = heritage_north_germanic }
	is_at_war = no
	NOT = { has_truce = root }
	NOT = { this = root }
}"""

# -----------------------------------------------------------------------------
# 0010 Longships on the Horizon
# -----------------------------------------------------------------------------
EVENTS.append(E(10, "Longships on the Horizon",
    "Longships under [eir_norse_lord.GetShortUIName]'s banner have been sighted off [eir_target_county.GetName].",
    "The dragon-prows came out of the morning haze, a dozen of them, then a dozen more. The fishermen are already running inland, and the monks of the nearest church are hiding what they can.\n\n[eir_norse_lord.GetShortUIName] has not sent envoys. [eir_norse_lord.GetSheHe|U] has sent men with axes.",
    [
        Opt("Gather the levies and meet them on the shore.",
            "eir_viking_invasion_effect = yes",
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=60),
        Opt("Hire Norse-Irish mercenaries and meet them with a larger force.",
            seq("remove_short_term_gold = medium_gold_value",
                "eir_defender_levy_effect = yes",
                "eir_viking_invasion_effect = yes"),
            stress="greedy = miniscule_stress_impact_gain", ai=20),
        Opt("Offer the jarl land and a share of the cattle.",
            RL((50, "jarl_accepts", "The jarl accepts your hospitality and sails on as a friend.",
                [(15, "diplomacy >= 14"), (10, "has_trait = generous")],
                seq("scope:eir_norse_lord = { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 30 } }",
                    "add_hook = { target = scope:eir_norse_lord type = favor_hook }",
                    "add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }")),
               (40, "jarl_refuses", "The jarl takes your gifts and your land.",
                [],
                seq("remove_short_term_gold = minor_gold_value",
                    "eir_viking_invasion_effect = yes"))),
            trigger="""OR = {
	diplomacy >= 12
	has_trait = gregarious
	has_trait = generous
}""",
            stress="paranoid = minor_stress_impact_gain\ntrusting = miniscule_stress_impact_loss", ai=20),
        Opt("Pay them to sail on. (Danegeld.)",
            seq("remove_short_term_gold = major_gold_value",
                "add_character_modifier = { modifier = eir_danegeld_modifier years = 3 }",
                "add_character_flag = { flag = eir_paid_danegeld years = 3 }",
                "add_prestige = -25"),
            stress="arrogant = minor_stress_impact_gain\nbrave = miniscule_stress_impact_gain", ai=5),
    ],
    theme="war",
    cooldown=4,
    trigger=f"""eir_is_irish_ruler_trigger = yes
is_ai = no
eir_viking_age_trigger = yes
eir_has_coast_trigger = yes
is_at_war = no
NOT = {{ has_character_flag = eir_paid_danegeld }}
NOT = {{ has_character_flag = eir_viking_cooldown }}
{NORSE_AVAILABLE}""",
    immediate="""eir_pick_norse_invasion_effect = yes
add_character_flag = { flag = eir_viking_cooldown years = 4 }""",
    portraits="left_portrait = {\n\tcharacter = scope:eir_norse_lord\n\tanimation = personality_bold\n}"))

# -----------------------------------------------------------------------------
# 0011 The Monastery in Flames
# -----------------------------------------------------------------------------
EVENTS.append(E(11, "The Monastery in Flames",
    "Smoke rises from the great monastery on your coast.",
    "Norse raiders have come ashore at the monastery, as they have come to a hundred before it. They will take the silver, the books and the monks, and burn what is left.\n\nIf riders go now, they may arrive in time.",
    [
        Opt("Ride to its defence.",
            RL((55, "monastery_saved", "You arrive in time and the raiders flee.",
                [(15, "martial >= 12"), (10, "has_trait = brave")],
                seq("add_piety = 100", "add_prestige = 50",
                    "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }")),
               (35, "monastery_lost", "You arrive too late. The monastery burns.",
                [],
                seq("add_piety = -50", "eir_raid_county_effect = yes"))),
            trigger="""OR = {
	martial >= 8
	has_trait = brave
}""",
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=40),
        Opt("Pay the raiders to spare the relics.",
            seq("remove_short_term_gold = medium_gold_value", "add_piety = 25",
                "eir_raid_county_effect = yes"),
            stress="greedy = minor_stress_impact_gain", ai=20),
        Opt("Move the relics to the round tower.",
            seq("add_piety = 100",
                "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }"),
            trigger="has_global_variable = eir_unlock_round_tower",
            ai=40),
        Opt("Pray for the monks and do nothing else.",
            seq("add_piety = -50", "eir_raid_county_effect = yes",
                "eir_trait_effect = { TRAIT = cynical OPPOSITE = zealous CHANCE = 20 }"),
            stress="zealous = minor_stress_impact_gain", ai=5),
    ],
    theme="war",
    cooldown=12,
    trigger="""eir_is_irish_ruler_trigger = yes
is_ai = no
eir_viking_age_trigger = yes
eir_has_coast_trigger = yes
piety >= 20
NOT = { has_character_flag = eir_paid_danegeld }
any_realm_county = { count >= 1 }"""))

# -----------------------------------------------------------------------------
# 0012 A Norse-Gael Lord's Bargain
# -----------------------------------------------------------------------------
EVENTS.append(E(12, "A Norse-Gael Lord's Bargain",
    "A Norse-Gael captain offers you his axes for a price.",
    "He is half Norse and half Irish, and he speaks both languages with the same accent. He has a hundred men with axes the length of a man's leg, and he says they are looking for a lord with cattle to pay for them.\n\nThe Isles breed such men by the score. They are not always loyal, but they are always good.",
    [
        Opt("Take his company into your pay.",
            seq("remove_short_term_gold = medium_gold_value",
                "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 2\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
                "add_character_modifier = { modifier = eir_gallowglass_paymaster_modifier years = 8 }"),
            stress="greedy = miniscule_stress_impact_gain", ai=40),
        Opt("Test his loyalty before you pay him.",
            RL((55, "captain_loyal", "The captain proves his word and joins you for less.",
                [(15, "diplomacy >= 12"), (15, "intrigue >= 12")],
                seq("remove_short_term_gold = minor_gold_value",
                    "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 2\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
                    "add_character_modifier = { modifier = eir_gallowglass_paymaster_modifier years = 8 }")),
               (35, "captain_leaves", "The captain takes offence and leaves, cursing your name.",
                [],
                "add_prestige = -25")),
            ai=20),
        Opt("Send him away. Irishmen will fight Ireland's wars.",
            "add_prestige = 25\neir_trait_effect = { TRAIT = arrogant OPPOSITE = humble CHANCE = 10 }",
            stress="humble = miniscule_stress_impact_gain", ai=10),
    ],
    theme="war",
    cooldown=15,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ngold >= medium_gold_value\nNOT = { has_global_variable = eir_unlock_gallowglass }"))

# -----------------------------------------------------------------------------
# 0013 Hostages for the Jarl
# -----------------------------------------------------------------------------
EVENTS.append(E(13, "Hostages for the Jarl",
    "[eir_norse_lord.GetShortUIName] demands hostages as the price of peace.",
    "The jarl sits at your table as if it were his own and names his price: two sons of your best families, to be raised in his hall until your good behaviour is proved.\n\nHostages bind a treaty better than any oath. They are also children.",
    [
        Opt("Send two noble children as hostages.",
            seq("add_character_modifier = { modifier = eir_danegeld_modifier years = 2 }",
                "scope:eir_norse_lord = { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 25 } }",
                "add_character_flag = { flag = eir_paid_danegeld years = 4 }",
                "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -5 }"),
            stress="compassionate = minor_stress_impact_gain", ai=30),
        Opt("Send livestock and silver instead.",
            seq("remove_short_term_gold = major_gold_value",
                "add_character_flag = { flag = eir_paid_danegeld years = 4 }"),
            ai=20),
        Opt("Send an insult, and prepare for war.",
            seq("add_prestige = 75", "eir_viking_invasion_effect = yes"),
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=30),
    ],
    theme="diplomacy",
    cooldown=10,
    trigger=f"""eir_is_irish_ruler_trigger = yes
is_ai = no
eir_viking_age_trigger = yes
eir_has_coast_trigger = yes
is_at_war = no
NOT = {{ has_character_flag = eir_paid_danegeld }}
{NORSE_AVAILABLE}""",
    immediate="eir_pick_norse_invasion_effect = yes"))

# -----------------------------------------------------------------------------
# 0015 The Norse Break on Your Shield   (defender won)
# -----------------------------------------------------------------------------
EVENTS.append(E(15, "The Norse Break on Your Shield",
    "The Norse host is shattered, and its jarl is your prisoner.",
    "They came out of the sea with axes and left it with rope around their necks. The bards are already composing, and the story improves with every singer.\n\n[eir_norse_lord.GetShortUIName] kneels in your camp, waiting to learn what a victorious Irish king will do.",
    [
        Opt("Hang him from the nearest oak.",
            seq("add_character_modifier = { modifier = eir_norse_scourge_modifier years = 15 }",
                "eir_trait_effect = { TRAIT = eir_viking_slayer OPPOSITE = eir_viking_slayer CHANCE = 50 }",
                "add_dread = minor_dread_gain", "add_prestige = 150",
                "eir_trait_effect = { TRAIT = callous OPPOSITE = compassionate CHANCE = 20 }"),
            stress="compassionate = minor_stress_impact_gain\nforgiving = miniscule_stress_impact_gain\nwrathful = miniscule_stress_impact_loss", ai=30),
        Opt("Ransom him back to his people.",
            seq("add_gold = major_gold_value",
                "add_character_modifier = { modifier = eir_norse_scourge_modifier years = 8 }",
                "add_prestige = 75",
                "scope:eir_norse_lord = { add_opinion = { target = root modifier = eir_norse_defied_opinion opinion = -15 } }"),
            stress="greedy = miniscule_stress_impact_loss", ai=40),
        Opt("Raise a cross on the battlefield and make a pilgrimage site of it.",
            seq("add_character_modifier = { modifier = eir_norse_scourge_modifier years = 10 }",
                "add_piety = 100", "add_prestige = 75",
                "scope:eir_target_county = { add_county_modifier = { modifier = eir_high_cross_modifier years = 25 } }"),
            trigger="piety >= 50",
            stress="zealous = miniscule_stress_impact_loss", ai=20),
        Opt("Offer him his freedom if his people swear to leave Ireland.",
            RL((55, "jarl_swears", "The jarl swears on his axe and sails away.",
                [(15, "diplomacy >= 14")],
                seq("add_character_modifier = { modifier = eir_norse_scourge_modifier years = 8 }",
                    "add_prestige = 100",
                    "scope:eir_norse_lord = { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 20 } }")),
               (35, "jarl_lies", "The jarl swears, then breaks his oath on the first fair wind.",
                [],
                seq("add_prestige = -25",
                    "scope:eir_norse_lord = { add_opinion = { target = root modifier = eir_norse_defied_opinion opinion = -30 } }"))),
            trigger="diplomacy >= 10",
            stress="vengeful = minor_stress_impact_gain\nforgiving = miniscule_stress_impact_loss", ai=10),
    ],
    theme="war",
    portraits="left_portrait = {\n\tcharacter = scope:eir_norse_lord\n\tanimation = shame\n}"))

# -----------------------------------------------------------------------------
# 0016 The Norse Hold Your Land   (attacker won)
# -----------------------------------------------------------------------------
EVENTS.append(E(16, "The Norse Hold Your Land",
    "[eir_norse_lord.GetShortUIName] has won, and [eir_target_county.GetName] is now a Norse county.",
    "Your army was beaten, and the longships that brought the raiders have been dragged up the beach and turned into roofs. The jarl has taken the hall, the herds and the harbour, and he says he intends to stay.\n\nThe people of the county still speak Irish. For now.",
    [
        Opt("Swear to take it back. (Unlocks a decision.)",
            seq("add_prestige = 25",
                "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 10 }",
                "add_character_flag = eir_oath_to_reclaim"),
            stress="vengeful = miniscule_stress_impact_loss\nforgiving = miniscule_stress_impact_gain", ai=60),
        Opt("Pay tribute and hope he is satisfied.",
            seq("remove_short_term_gold = major_gold_value",
                "add_character_modifier = { modifier = eir_danegeld_modifier years = 5 }",
                "add_character_flag = { flag = eir_paid_danegeld years = 5 }"),
            stress="arrogant = minor_stress_impact_gain", ai=10),
        Opt("Marry a kinswoman to the jarl and make him part of the family.",
            RL((50, "jarl_marries", "The jarl accepts the match and becomes a cautious ally.",
                [(15, "diplomacy >= 12")],
                seq("scope:eir_norse_lord = { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 40 } }",
                    "add_hook = { target = scope:eir_norse_lord type = favor_hook }",
                    "add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }")),
               (40, "jarl_scoffs", "The jarl takes the bride and the county.",
                [],
                "add_prestige = -50")),
            trigger="diplomacy >= 8",
            ai=20),
    ],
    theme="war",
    immediate="""scope:eir_target_county ?= { add_county_modifier = { modifier = eir_norse_garrison_modifier years = 10 } }
add_character_modifier = { modifier = eir_foreign_lords_modifier years = 5 }""",
    portraits="left_portrait = {\n\tcharacter = scope:eir_norse_lord\n\tanimation = schadenfreude\n}"))
