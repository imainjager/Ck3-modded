"""Church, saints, and the Brehon courts."""
from evdsl import *

EVENTS = []

IRISH_PLAYER = "eir_is_irish_ruler_trigger = yes\nis_ai = no"

# -----------------------------------------------------------------------------
# 0040 The Brehon's Judgement
# -----------------------------------------------------------------------------
EVENTS.append(E(40, "The Brehon's Judgement",
    "Two of your subjects have come to court to settle a dispute over a stolen bull.",
    "The Brehon law has a rule for everything: a price for a stolen bull, a different price for a bull stolen at night, and a third price for a bull that is stolen and then eaten. The learned judge you appointed is out of town, so the case falls to you.\n\nBoth parties are listening carefully, because a king's judgement becomes the next precedent.",
    [
        Opt("Judge by the letter of the old laws.",
            RL((60, "law_clear", "The case is settled, and both sides accept the verdict.",
                [(20, "learning >= 12"), (15, "has_trait = eir_brehon")],
                seq("add_prestige = 75",
                    "add_character_modifier = { modifier = eir_brehon_laws_modifier years = 5 }",
                    "eir_court_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 8 }")),
               (30, "law_confused", "The law is older and more complicated than you remembered, and the verdict is mocked.",
                [],
                "add_prestige = -25")),
            trigger="learning >= 8",
            stress="lazy = miniscule_stress_impact_gain\ndiligent = miniscule_stress_impact_loss", ai=40),
        Opt("Decide by your own sense of fairness.",
            seq("add_prestige = 25", "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 15 }"),
            stress="arbitrary = miniscule_stress_impact_loss", ai=30),
        Opt("Take a gift from the wealthier party and rule for him.",
            seq("add_gold = minor_gold_value", "add_prestige = -50",
                "eir_court_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -8 }",
                "eir_trait_effect = { TRAIT = arbitrary OPPOSITE = just CHANCE = 25 }"),
            stress="honest = minor_stress_impact_gain\njust = minor_stress_impact_gain\ngreedy = miniscule_stress_impact_loss", ai=10),
        Opt("Send the case to a famous Brehon in another kingdom.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 50"),
            ai=20),
    ],
    theme="court", cooldown=8, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0041 The Honour-Price Dispute
# -----------------------------------------------------------------------------
EVENTS.append(E(41, "The Honour-Price Dispute",
    "Two vassals have come to blows over the honour-price of a murdered kinsman.",
    "[eir_dispute_a.GetShortUIName] killed the cousin of [eir_dispute_b.GetShortUIName] in a quarrel over a field boundary. The killer is willing to pay the éraic. The family says no price is high enough.\n\nIf you do not settle it, they will.",
    [
        Opt("Fix an honour-price you know both will accept.",
            RL((55, "price_agreed", "The two families agree, and the feud ends.",
                [(20, "diplomacy >= 14"), (10, "has_trait = eir_brehon")],
                seq("add_prestige = 100",
                    "scope:eir_dispute_a = { add_opinion = { target = root modifier = eir_trusts_justice_opinion opinion = 15 } }",
                    "scope:eir_dispute_b = { add_opinion = { target = root modifier = eir_trusts_justice_opinion opinion = 15 } }")),
               (35, "price_refused", "Neither side accepts, and each blames you.",
                [],
                seq("scope:eir_dispute_a = { add_opinion = { target = root modifier = eir_tribute_resentment_opinion opinion = -10 } }",
                    "scope:eir_dispute_b = { add_opinion = { target = root modifier = eir_tribute_resentment_opinion opinion = -10 } }"))),
            trigger="diplomacy >= 8", ai=40),
        Opt("Side with the stronger family.",
            seq("scope:eir_dispute_a = { add_opinion = { target = root modifier = eir_ard_ri_opinion opinion = 20 } }",
                "scope:eir_dispute_b = { add_opinion = { target = root modifier = eir_tribute_resentment_opinion opinion = -25 } }",
                "add_character_modifier = { modifier = eir_kin_strife_modifier years = 3 }"),
            stress="just = minor_stress_impact_gain\nhonest = miniscule_stress_impact_gain", ai=20),
        Opt("Let them fight it out. The survivor will respect the law.",
            seq("add_prestige = -25", "add_character_modifier = { modifier = eir_kin_strife_modifier years = 3 }",
                "eir_trait_effect = { TRAIT = callous OPPOSITE = compassionate CHANCE = 20 }"),
            stress="compassionate = minor_stress_impact_gain", ai=10),
        Opt("Pay the honour-price from your own treasury.",
            seq("remove_short_term_gold = medium_gold_value", "add_prestige = 50",
                "scope:eir_dispute_a = { add_opinion = { target = root modifier = eir_saved_by_ruler_opinion opinion = 20 } }",
                "scope:eir_dispute_b = { add_opinion = { target = root modifier = eir_saved_by_ruler_opinion opinion = 20 } }"),
            stress="greedy = minor_stress_impact_gain", ai=20),
    ],
    theme="vassal", cooldown=12,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nany_vassal = { count >= 2 }",
    immediate="""random_vassal = { save_scope_as = eir_dispute_a }
random_vassal = {
	limit = { NOT = { this = scope:eir_dispute_a } }
	save_scope_as = eir_dispute_b
}"""))

# -----------------------------------------------------------------------------
# 0042 The Healing Well
# -----------------------------------------------------------------------------
EVENTS.append(E(42, "The Healing Well",
    "A well in [eir_well_county.GetName] is said to have cured a blind child.",
    "The story is that a girl who had been blind from birth washed her face in the spring and saw her mother for the first time. Within a week there were two hundred pilgrims, and within a fortnight there was a stall selling bottles.\n\nThe local priest is not sure what to make of it. The local innkeeper is sure it is a miracle.",
    [
        Opt("Build a chapel and make it a place of pilgrimage.",
            seq("remove_short_term_gold = medium_gold_value", "add_piety = 100",
                "scope:eir_well_county = { add_county_modifier = { modifier = eir_holy_well_modifier years = 25 } }"),
            stress="zealous = miniscule_stress_impact_loss", ai=40),
        Opt("Send a learned priest to investigate before you commit.",
            RL((55, "well_real", "The priest reports a true wonder, and the pilgrims are right.",
                [(15, "learning >= 12")],
                seq("add_piety = 150", "scope:eir_well_county = { add_county_modifier = { modifier = eir_holy_well_modifier years = 25 } }")),
               (35, "well_fraud", "The priest finds a local trickster at work, and you are saved the embarrassment.",
                [],
                seq("add_prestige = 50"))),
            trigger="piety >= 30", ai=40),
        Opt("Tax the pilgrims and say nothing about miracles.",
            seq("add_gold = medium_gold_value", "add_piety = -25"),
            stress="zealous = minor_stress_impact_gain\ngreedy = miniscule_stress_impact_loss", ai=15),
    ],
    theme="faith", cooldown=20,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nany_realm_county = { count >= 1 }",
    immediate="random_realm_county = { save_scope_as = eir_well_county }"))

# -----------------------------------------------------------------------------
# 0043 The Saint's Bell
# -----------------------------------------------------------------------------
EVENTS.append(E(43, "The Saint's Bell",
    "A ploughman has found an iron bell in a field, and the monks say it is Saint Patrick's.",
    "It is a small square bell of beaten iron, rusted but sound, and it rings with a dull clang that the old monks say is the voice of the saint. Relics of Saint Patrick are among the most valuable in Ireland.\n\nEveryone wants it, and the ploughman wants to be paid.",
    [
        Opt("Keep it in your own chapel and set a shrine around it.",
            seq("add_character_modifier = { modifier = eir_relic_keeper_modifier years = 15 }",
                "add_piety = 100", "remove_short_term_gold = minor_gold_value"),
            stress="zealous = miniscule_stress_impact_loss", ai=40),
        Opt("Give it to the Church of Armagh.",
            seq("add_piety = 200", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }"),
            ai=30),
        Opt("Sell it to the highest bidder.",
            seq("add_gold = major_gold_value", "add_piety = -75"),
            stress="zealous = minor_stress_impact_gain\ngreedy = miniscule_stress_impact_loss", ai=10),
        Opt("Carry it in procession before your army.",
            seq("add_prestige = 150", "add_character_modifier = { modifier = eir_relic_keeper_modifier years = 5 }"),
            trigger="has_trait = zealous", ai=20),
    ],
    theme="faith", cooldown=30,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\npiety >= 30"))

# -----------------------------------------------------------------------------
# 0044 Culdee versus Roman
# -----------------------------------------------------------------------------
EVENTS.append(E(44, "Culdee versus Roman",
    "The old Irish monks and the Roman reformers are at each other's throats.",
    "The Culdees keep the old Irish customs: the tonsure, the Easter date, a church run by abbots instead of bishops. The reformers call it laxity and heresy. Each side has a good claim on holiness, and neither likes the other.\n\nA ruler who wants peace in the Church has to choose between them, or find a way to make them both listen.",
    [
        Opt("Back the old Irish customs.",
            seq("add_piety = 50", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
                "eir_add_tradition_effect = { TRADITION = tradition_eir_culdee_christianity }"),
            stress="zealous = miniscule_stress_impact_loss", ai=30),
        Opt("Back the reformers and the authority of Rome.",
            seq("add_character_modifier = { modifier = eir_synod_reform_modifier years = 8 }",
                "add_character_modifier = { modifier = eir_culdee_strife_modifier years = 5 }", "add_piety = 75"),
            ai=30),
        Opt("Call a synod and make both sides argue it out before the bishops.",
            RL((55, "synod_peace", "The synod finds a compromise both sides can live with.",
                [(20, "learning >= 12"), (10, "piety >= 300")],
                seq("add_piety = 150", "add_prestige = 100",
                    "add_character_modifier = { modifier = eir_synod_reform_modifier years = 8 }")),
               (35, "synod_fails", "The synod ends in a shouting match, and the strife deepens.",
                [],
                "add_character_modifier = { modifier = eir_culdee_strife_modifier years = 6 }")),
            trigger="learning >= 8", ai=40),
    ],
    theme="faith", cooldown=25,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\npiety >= 100"))

# -----------------------------------------------------------------------------
# 0045 A Hermit's Prophecy
# -----------------------------------------------------------------------------
EVENTS.append(E(45, "A Hermit's Prophecy",
    "A hermit comes down from his cave to tell you what he has seen.",
    "He is as thin as a rake, he smells like a bog and he has not spoken to another human in ten years. He says that in a vision he saw Ireland united under one king, and then broken again, and then united again.\n\nHe does not say whether the king was you.",
    [
        Opt("Feed him, house him, and ask about the vision.",
            seq("add_piety = 75", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 3 }",
                "add_learning_lifestyle_xp = 50"),
            stress="zealous = miniscule_stress_impact_loss", ai=40),
        Opt("Have the prophecy announced to the whole court.",
            seq("add_prestige = 150", "add_character_modifier = { modifier = eir_lia_fail_blessing_modifier years = 5 }"),
            trigger="has_trait = ambitious", stress="humble = minor_stress_impact_gain", ai=30),
        Opt("Send the hermit back to his cave and tell no one.",
            "add_piety = 25",
            stress="cynical = miniscule_stress_impact_loss", ai=30),
    ],
    theme="legend", cooldown=25, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0046 A Scholar from Iona
# -----------------------------------------------------------------------------
EVENTS.append(E(46, "A Scholar from the Great Monasteries",
    "A learned monk from one of the great monasteries asks for your patronage.",
    "He has read every book in his abbey's library, and several that were supposed to be lost. He is travelling from court to court, looking for a lord who will give him a quiet room and a steady supply of vellum.\n\nIn exchange, he promises to teach every child in your household.",
    [
        Opt("Give him a place in your household.",
            seq("add_character_modifier = { modifier = eir_fili_patron_modifier years = 8 }",
                "add_learning_lifestyle_xp = 100", "remove_short_term_gold = minor_gold_value",
                "add_piety = 50"),
            ai=50),
        Opt("Ask him to tutor your heir.",
            seq("add_character_modifier = { modifier = eir_brehon_laws_modifier years = 5 }",
                "random_child = {\n\tlimit = { age >= 4 age < 16 is_alive = yes }\n\tadd_learning_skill = 1\n}"),
            trigger="any_child = { age >= 4 age < 16 is_alive = yes }", ai=40),
        Opt("Send him away. Learning is a monk's business.",
            "add_prestige = -10",
            stress="lazy = miniscule_stress_impact_loss", ai=10),
    ],
    theme="learning", cooldown=15, trigger=IRISH_PLAYER))
