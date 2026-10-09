"""Native resistance (for foreign rulers of Celtic land) and Irish court life."""
from evdsl import *

EVENTS = []

OCC = "random_sub_realm_county = {\n\tlimit = { eir_county_occupied_trigger = yes }\n\tsave_scope_as = eir_resist_county\n}"
RES_TRIG = "is_ai = no\neir_rules_occupied_land_trigger = yes"

# -----------------------------------------------------------------------------
# 0120 Rapparees in the Hills
# -----------------------------------------------------------------------------
EVENTS.append(E(120, "Rapparees in the Hills",
    "Armed men from the old families are raiding your tax-collectors in the hills.",
    "They wear no livery and answer to no lord you know. They strike at dusk, take the grain, and leave a poem nailed to the church door in a language your stewards cannot read.\n\nThe local people feed them, hide them and lie about them.",
    [
        Opt("Send soldiers to burn their hiding places.",
            seq("remove_short_term_gold = minor_gold_value",
                "scope:eir_resist_county = { add_county_modifier = { modifier = eir_cattle_raided_modifier years = 3 } }",
                "add_prestige = 25"),
            stress="compassionate = minor_stress_impact_gain", ai=30),
        Opt("Ask the local chieftain to call them off.",
            RL((55, "rapp_calmed", "The raiders are calmed", [(10, "diplomacy >= 10")],
                "scope:eir_resist_county = { add_county_modifier = { modifier = eir_pacified_modifier years = 6 } }\nadd_prestige = 25"),
               (35, "rapp_refused", "The chieftain only laughs", [],
                "add_prestige = -25"),
               (10, "rapp_betrayed", "He sells your name to the raiders", [],
                "add_prestige = -50\nscope:eir_resist_county = { add_county_modifier = { modifier = eir_native_resistance_modifier years = 4 } }")),
            trigger="diplomacy >= 8", ai=40),
        Opt("Declare a tax holiday for the county.",
            seq("scope:eir_resist_county = { add_county_modifier = { modifier = eir_loyal_county_modifier years = 5 } }",
                "remove_short_term_gold = minor_gold_value"),
            stress="greedy = minor_stress_impact_gain", ai=30),
        Opt("Leave them alone. They are a nuisance, not a war.",
            "add_prestige = -10", ai=10),
    ],
    theme="war", cooldown=10, trigger=RES_TRIG, immediate=OCC))

# -----------------------------------------------------------------------------
# 0121 The Burned Hall
# -----------------------------------------------------------------------------
EVENTS.append(E(121, "The Burned Hall",
    "The hall of your reeve has been burned to the ground, and the people say it was the sídhe.",
    "The reeve says it was arson, and he says it was the Irish. The villagers say there was a storm, and a spark from the fire, and that it was nobody's fault but the good folk's.\n\nIt is, to be fair, the third hall burned this year.",
    [
        Opt("Fine the village until the culprit is found.",
            seq("add_gold = minor_gold_value",
                "scope:eir_resist_county = { add_county_modifier = { modifier = eir_punitive_levy_modifier years = 4 } }"),
            stress="compassionate = minor_stress_impact_gain", ai=25),
        Opt("Hold an inquiry, and let the local elders judge.",
            seq("scope:eir_resist_county = { add_county_modifier = { modifier = eir_loyal_county_modifier years = 4 } }", "add_prestige = 25"),
            trigger="learning >= 8", ai=40),
        Opt("Replace the reeve with a local man.",
            seq("scope:eir_resist_county = { add_county_modifier = { modifier = eir_pacified_modifier years = 8 } }", "remove_short_term_gold = minor_gold_value"),
            ai=35),
    ],
    theme="court", cooldown=10, trigger=RES_TRIG, immediate=OCC))

# -----------------------------------------------------------------------------
# 0122 The Chieftain's Petition
# -----------------------------------------------------------------------------
EVENTS.append(E(122, "The Chieftain's Petition",
    "A chieftain of the old kindred comes to ask that you respect the laws of his forefathers.",
    "He does not ask for the land, only for the right to keep his own law-courts and his poets. He has brought forty men with him, all unarmed, which is the most dangerous thing he could have done.\n\nHe does not look like a man who will take no for an answer.",
    [
        Opt("Grant him his courts, under your seal.",
            seq("scope:eir_resist_county = { add_county_modifier = { modifier = eir_pacified_modifier years = 10 } }", "add_prestige = 25",
                "add_character_modifier = { modifier = eir_brehon_laws_modifier years = 6 }"),
            ai=40),
        Opt("Refuse. The law of the realm applies everywhere.",
            seq("add_prestige = 25", "scope:eir_resist_county = { add_county_modifier = { modifier = eir_native_resistance_modifier years = 4 } }"),
            stress="compassionate = minor_stress_impact_gain", ai=30),
        Opt("Take his son as a foster-child.",
            seq("add_character_modifier = { modifier = eir_foster_ties_modifier years = 12 }",
                "scope:eir_resist_county = { add_county_modifier = { modifier = eir_loyal_county_modifier years = 8 } }"),
            ai=30),
    ],
    theme="diplomacy", cooldown=10, trigger=RES_TRIG, immediate=OCC))

# -----------------------------------------------------------------------------
# 0123 An Offer of Allegiance
# -----------------------------------------------------------------------------
EVENTS.append(E(123, "An Offer of Allegiance",
    "The Gaelic lords of your realm say they could be loyal subjects, if only you would try.",
    "They do not ask you to speak Irish. They would just like you to learn their names, and to pass one law that is not written in a foreign tongue.\n\nIt is a small request, and it will not be repeated.",
    [
        Opt("Learn their names and their laws.",
            seq("add_character_modifier = { modifier = eir_hospitality_modifier years = 6 }",
                "scope:eir_resist_county = { add_county_modifier = { modifier = eir_pacified_modifier years = 12 } }", "add_prestige = 25"),
            ai=40),
        Opt("Keep your own ways. You rule by right of conquest.",
            seq("add_prestige = 25", "scope:eir_resist_county = { add_county_modifier = { modifier = eir_native_resistance_modifier years = 3 } }"),
            stress="compassionate = minor_stress_impact_gain", ai=30),
        Opt("Take a Gaelic spouse for your heir.",
            seq("add_character_modifier = { modifier = eir_foster_ties_modifier years = 10 }",
                "scope:eir_resist_county = { add_county_modifier = { modifier = eir_loyal_county_modifier years = 10 } }"),
            ai=30),
    ],
    theme="diplomacy", cooldown=15, trigger=RES_TRIG, immediate=OCC))

# -----------------------------------------------------------------------------
# 0130 The Bardic Contest
# -----------------------------------------------------------------------------
EVENTS.append(E(130, "The Bardic Contest",
    "Two poets are competing for the chair of chief bard, and the whole court has bet on the outcome.",
    "One is old and learned. The other is young and cruel. Both have promised to write you a praise-poem, and both have promised to write your satire if they lose.\n\nThe hall is full and the ale is flowing.",
    [
        Opt("Give the chair to the old master.",
            seq("add_prestige = 50", "add_character_modifier = { modifier = eir_fili_patron_modifier years = 4 }"),
            ai=40),
        Opt("Give the chair to the young challenger.",
            RL((60, "bard_young_good", "He is as good as he boasts", [],
                "add_prestige = 75"),
               (40, "bard_young_bad", "He writes an insulting verse", [],
                "add_character_modifier = { modifier = eir_satirised_modifier years = 3 }")),
            ai=30),
        Opt("Judge the contest yourself.",
            seq("add_prestige = 75", "add_learning_lifestyle_xp = 50"),
            trigger="learning >= 10", ai=30),
        Opt("Let them both sing and give both a cow.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 25"), ai=20),
    ],
    theme="learning", cooldown=25,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_fili"))

# -----------------------------------------------------------------------------
# 0131 The Foster-Child Comes Home
# -----------------------------------------------------------------------------
EVENTS.append(E(131, "The Foster-Child Comes Home",
    "One of your children has come back after seven years in a vassal's hall.",
    "They left a child and returned with a different accent, a new set of friends, and a loyalty to the man who raised them. They also brought a gift: a cow, from the foster-father.\n\nThe bond of fosterage is held to be stronger than blood.",
    [
        Opt("Celebrate their return with a great feast.",
            seq("remove_short_term_gold = minor_gold_value", "add_character_modifier = { modifier = eir_foster_ties_modifier years = 10 }", "add_prestige = 50"),
            ai=40),
        Opt("Send a rich gift to the foster-father.",
            seq("remove_short_term_gold = minor_gold_value", "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 8 }"),
            ai=40),
        Opt("Test the child's loyalty with a hard question.",
            RL((60, "fost_loyal", "The child answers well", [], "add_prestige = 25"),
               (40, "fost_torn", "The child sides with the foster-father", [],
                "add_character_modifier = { modifier = eir_kin_strife_modifier years = 2 }")),
            ai=20),
    ],
    theme="family", cooldown=25,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_fosterage\nany_child = { is_adult = no }"))

# -----------------------------------------------------------------------------
# 0132 The Norse-Gael Merchant
# -----------------------------------------------------------------------------
EVENTS.append(E(132, "The Norse-Gael Merchant",
    "A merchant from the port towns speaks both Irish and Norse, and has something to sell.",
    "He has silver from the east, glass from the south, and slaves from everywhere. He offers a lot of everything, and each item will cost you an opinion.\n\nHe is also a reliable source of news.",
    [
        Opt("Buy silver and glass for the hall.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 50"), ai=40),
        Opt("Ask him what the Norse kings are planning.",
            seq("add_character_modifier = { modifier = eir_hospitality_modifier years = 4 }", "add_gold = minor_gold_value"),
            trigger="intrigue >= 8", ai=30),
        Opt("Refuse to deal with a slaver.",
            seq("add_piety = 50"), stress="greedy = minor_stress_impact_gain", ai=30),
    ],
    theme="court", cooldown=15,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\neir_has_coast_trigger = yes"))

# -----------------------------------------------------------------------------
# 0133 The Pilgrim of Lough Derg
# -----------------------------------------------------------------------------
EVENTS.append(E(133, "A Pilgrim from Lough Derg",
    "A pilgrim returns from the cave on the island in Lough Derg, and swears he saw the next world.",
    "He fasted three days, prayed on his knees on the cold stones, and then descended into the cave. He will tell no one what he saw, only that he will never be afraid again.\n\nThe local people are lining up for a blessing.",
    [
        Opt("Ask him to bless your household.",
            seq("add_piety = 100", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }"), ai=40),
        Opt("Make the pilgrimage yourself.",
            seq("add_piety = 200", "add_character_modifier = { modifier = eir_pilgrim_modifier years = 6 }", "remove_short_term_gold = minor_gold_value"),
            trigger="is_at_war = no", stress="craven = minor_stress_impact_gain", ai=30),
        Opt("Smile politely and send him home.",
            "add_prestige = 10", ai=30),
    ],
    theme="faith", cooldown=25,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\npiety >= 50"))
