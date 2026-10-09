"""The wider Celtic world: Wales, Cornwall, Brittany, Alba and the Isles."""
from evdsl import *

EVENTS = []

CROWNED = "eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_crowned"

# -----------------------------------------------------------------------------
# 0070 A Welsh Prince Seeks Your Friendship
# -----------------------------------------------------------------------------
EVENTS.append(E(70, "A Welsh Prince Seeks Your Friendship",
    "A prince of Gwynedd has crossed the Irish Sea with a gift of Welsh gold.",
    "He says his people and yours share a past that the Saxons and the Normans would like to forget, and that the High King of Ireland is the only man who can give the Celts a fair hearing. He has brought a harp as a gift, and a request.\n\nThe request is large.",
    [
        Opt("Offer him an alliance and a safe port on the Irish coast.",
            seq("add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 8 }",
                "add_prestige = 100", "add_hook = { target = scope:eir_welsh_prince type = favor_hook }"),
            ai=40),
        Opt("Send him home with gifts but no promises.",
            "add_prestige = 25\nscope:eir_welsh_prince = { add_opinion = { target = root modifier = eir_gael_pride_opinion opinion = 15 } }",
            ai=40),
        Opt("Ask for Welsh archers in return for Irish cattle.",
            seq("remove_short_term_gold = minor_gold_value",
                "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = bowmen\n\t\tstacks = 3\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_mercenary_company_name\n}"),
            trigger="diplomacy >= 8", ai=30),
    ],
    theme="diplomacy", cooldown=20,
    trigger=CROWNED + """
any_ruler = {
	is_ai = yes
	culture ?= { has_cultural_pillar = heritage_brythonic }
}""",
    immediate="""random_ruler = {
	limit = {
		is_ai = yes
		culture ?= { has_cultural_pillar = heritage_brythonic }
	}
	save_scope_as = eir_welsh_prince
}""",
    portraits="left_portrait = {\n\tcharacter = scope:eir_welsh_prince\n\tanimation = personality_honorable\n}"))

# -----------------------------------------------------------------------------
# 0071 A Breton Exile
# -----------------------------------------------------------------------------
EVENTS.append(E(71, "A Breton Exile",
    "A Breton nobleman asks for refuge at your court.",
    "His family has held land in Brittany for ten generations, and now they hold none. He speaks a language that is nearly your own, and he tells you stories of the old kings of Armorica that sound like stories you already know.\n\nHe wants a hall, and maybe someday an army.",
    [
        Opt("Give him a hall and a place at the high table.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 75",
                "add_character_modifier = { modifier = eir_hospitality_modifier years = 4 }"),
            ai=50),
        Opt("Help him plan to retake his lands.",
            seq("remove_short_term_gold = medium_gold_value", "add_prestige = 100",
                "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 5 }"),
            trigger="has_global_variable = eir_done_brotherhood", ai=30),
        Opt("Direct him to the Welsh instead.",
            "add_prestige = 10",
            ai=20),
    ],
    theme="diplomacy", cooldown=25,
    trigger=CROWNED))

# -----------------------------------------------------------------------------
# 0072 The Pictish Memory
# -----------------------------------------------------------------------------
EVENTS.append(E(72, "Voices from the North",
    "Gaelic lords from Alba have sent word that they would welcome an Irish high king.",
    "The Gaels of the Scottish coast and the Hebrides never forgot their descent from Ireland. They are tired of Lowland and Norse overlords, and they would prefer a king they can understand.\n\nThey ask for neither crown nor conquest, only your recognition.",
    [
        Opt("Recognise them as kin and promise protection.",
            seq("add_prestige = 150", "add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 8 }",
                "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 5 }"),
            ai=50),
        Opt("Send a poet to bind the two peoples with verse.",
            seq("add_character_modifier = { modifier = eir_fili_patron_modifier years = 5 }", "add_prestige = 75"),
            trigger="has_global_variable = eir_done_fili", ai=30),
        Opt("Accept their homage and demand tribute in return.",
            seq("add_gold = medium_gold_value", "add_prestige = 50",
                "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -4 }"),
            stress="generous = miniscule_stress_impact_gain", ai=20),
    ],
    theme="diplomacy", cooldown=25,
    trigger=CROWNED))

# -----------------------------------------------------------------------------
# 0073 Axemen from the Isles
# -----------------------------------------------------------------------------
EVENTS.append(E(73, "Axemen from the Isles",
    "A fleet of galleys arrives from the Hebrides, full of hard men with long axes.",
    "They are the gallowglass, warrior-families of mixed Norse and Gaelic blood who sell their swords from Skye to Kerry. They have heard of a king who pays well and keeps his word, and they have come to ask for a place in his army.\n\nThey are expensive, and they are terrifying.",
    [
        Opt("Hire a full company.",
            seq("remove_short_term_gold = major_gold_value",
                "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = eir_gallowglass\n\t\tstacks = 3\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
                "add_character_modifier = { modifier = eir_gallowglass_paymaster_modifier years = 10 }"),
            ai=50),
        Opt("Settle them on frontier land as a permanent garrison.",
            seq("remove_short_term_gold = medium_gold_value",
                "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_gallowglass_garrison_modifier years = 20 }\n}"),
            ai=30),
        Opt("Thank them and turn them away.",
            "add_prestige = 10",
            ai=10),
    ],
    theme="war", cooldown=15,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_unlock_gallowglass\ngold >= major_gold_value"))

# -----------------------------------------------------------------------------
# 0074 A Cornish Bard
# -----------------------------------------------------------------------------
EVENTS.append(E(74, "A Cornish Bard Comes to Court",
    "A bard from Cornwall sings a song in a tongue you almost understand.",
    "He has walked the whole length of Britain with a harp on his back, singing songs about Arthur and the lost kingdoms of the west. His Cornish is cousin to Irish and Welsh, and every few verses he stops to ask if you follow.\n\nThe court is spellbound.",
    [
        Opt("Reward him lavishly and ask for a second night.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 75",
                "add_character_modifier = { modifier = eir_fili_patron_modifier years = 4 }"),
            ai=50),
        Opt("Ask him to teach your own bards his songs.",
            seq("add_learning_lifestyle_xp = 100", "add_prestige = 25"),
            trigger="learning >= 8", ai=30),
        Opt("Thank him and send him on his way.",
            "add_prestige = 10",
            ai=20),
    ],
    theme="learning", cooldown=20,
    trigger=CROWNED))

# -----------------------------------------------------------------------------
# 0075 The Celtic Congress
# -----------------------------------------------------------------------------
EVENTS.append(E(75, "The Celtic Congress",
    "Delegates from Wales, Cornwall, Brittany and Alba have come to Tara.",
    "No one has seen the Celtic peoples gathered under one roof since the time of the Romans. They argue about the Easter date and the proper way to shave a chin, and they agree on one thing: that a Celtic people with a High King at its head can no longer be ignored.\n\nIt is a very Celtic congress.",
    [
        Opt("Declare a perpetual friendship among the Celtic peoples.",
            seq("add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 15 }",
                "add_prestige = 250", "add_piety = 50"),
            ai=50),
        Opt("Propose a joint war against the Norman advance.",
            seq("add_prestige = 150", "eir_defender_levy_effect = yes",
                "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 8 }"),
            stress="craven = minor_stress_impact_gain", ai=30),
        Opt("Take the opportunity to quarrel with the Welsh over Easter.",
            seq("add_piety = 50", "add_prestige = -50"),
            stress="zealous = miniscule_stress_impact_loss", ai=10),
    ],
    theme="diplomacy", cooldown=40,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_brotherhood"))
