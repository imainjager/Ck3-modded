"""Historical events of twelfth-century Ireland. Each is dated, and fires once per game."""
from evdsl import *

EVENTS = []

IRISH_PLAYER = "eir_is_irish_ruler_trigger = yes\nis_ai = no"

# -----------------------------------------------------------------------------
# 0060 Munster Reaches for the High Kingship  (c. 1086)
# -----------------------------------------------------------------------------
EVENTS.append(E(60, "Munster Reaches for the High Kingship",
    "Your poets say the time has come for a king of Munster to be High King of Ireland.",
    "Brian Boru did it a lifetime ago, and the bards of Cashel have not let anyone forget it. Now they say that the line of Brian has a living heir with an army, an ambition and a good claim.\n\nThe other provinces have heard the poems too, and are sharpening their spears.",
    [
        Opt("Take the high kingship as Brian did.",
            seq("add_prestige = 250", "add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 10 }",
                "set_global_variable = eir_done_oenach", "set_global_variable = eir_hist_1086",
                "eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 8 }"),
            stress="humble = minor_stress_impact_gain\nambitious = miniscule_stress_impact_loss", ai=50),
        Opt("Be content to rule Munster, and see what comes.",
            seq("add_prestige = 50", "set_global_variable = eir_hist_1086"),
            stress="ambitious = minor_stress_impact_gain\ncontent = miniscule_stress_impact_loss", ai=30),
        Opt("Offer the high kingship to Meath and become its kingmaker.",
            seq("add_prestige = 100", "add_hook = { target = title:d_meath.holder type = favor_hook }", "set_global_variable = eir_hist_1086"),
            trigger="exists = title:d_meath.holder", ai=20),
    ],
    theme="legend", cooldown=200,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= 1086\nhas_title = title:d_munster\nNOT = { has_global_variable = eir_hist_1086 }"))

# -----------------------------------------------------------------------------
# 0061 The Gift of Cashel  (1101)
# -----------------------------------------------------------------------------
EVENTS.append(E(61, "The Gift of Cashel",
    "Your bishops suggest a gift to the Church that will be remembered for centuries.",
    "The Rock of Cashel has been the seat of the kings of Munster for generations. It is also a magnificent site for a cathedral. The Church would love it, and so would the archives of history.\n\nGiving away your capital fortress is, however, an unusual form of generosity.",
    [
        Opt("Give the Rock of Cashel to the Church.",
            seq("eir_capital_county_modifier_effect = { TITLE = d_munster MODIFIER = eir_cashel_rock_modifier YEARS = 40 }",
                "add_piety = 400", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 15 }",
                "set_global_variable = eir_done_cashel", "set_global_variable = eir_hist_1101"),
            stress="greedy = minor_stress_impact_gain\nzealous = miniscule_stress_impact_loss", ai=40),
        Opt("Offer a rich endowment instead of the fortress.",
            seq("remove_short_term_gold = major_gold_value", "add_piety = 200", "set_global_variable = eir_hist_1101"),
            ai=30),
        Opt("Politely decline.",
            seq("add_piety = -50", "set_global_variable = eir_hist_1101"),
            stress="zealous = minor_stress_impact_gain", ai=10),
    ],
    theme="faith", cooldown=200,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= 1101\nhas_title = title:d_munster\npiety >= 100\nNOT = { has_global_variable = eir_hist_1101 }"))

# -----------------------------------------------------------------------------
# 0062 The Synod of Ráth Breasail  (1111)
# -----------------------------------------------------------------------------
EVENTS.append(E(62, "The Synod of Ráth Breasail",
    "Bishops from across Ireland gather to divide the country into dioceses.",
    "For the first time in Irish history, the Church will have a clear structure: two archbishoprics, twenty-four dioceses, and a place for every abbot. The reformers are triumphant. The old monks are grim.\n\nThe king's blessing would help the reforms along, and cost him some friends.",
    [
        Opt("Support the reforms, and take part in the synod.",
            seq("add_character_modifier = { modifier = eir_synod_reform_modifier years = 15 }",
                "add_character_modifier = { modifier = eir_culdee_strife_modifier years = 6 }",
                "add_piety = 250", "set_global_variable = eir_done_synod", "set_global_variable = eir_hist_1111"),
            stress="zealous = miniscule_stress_impact_loss", ai=50),
        Opt("Attend, but speak for the old monasteries.",
            seq("add_piety = 100", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }",
                "set_global_variable = eir_hist_1111"),
            ai=30),
        Opt("Stay away. A king has no business in the Church's affairs.",
            seq("add_prestige = 25", "set_global_variable = eir_hist_1111"),
            ai=20),
    ],
    theme="faith", cooldown=200,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= 1111\npiety >= 100\nNOT = { has_global_variable = eir_hist_1111 }"))

# -----------------------------------------------------------------------------
# 0063 The Synod of Kells  (1152)
# -----------------------------------------------------------------------------
EVENTS.append(E(63, "The Synod of Kells",
    "A papal legate arrives with four palliums, one for each Irish archbishop.",
    "He speaks no Irish and has never seen a bog. He has come to confirm what the synods have been planning for forty years: Ireland divided into four archdioceses, answering to Rome.\n\nHe wants the support of every king he can reach, and he is willing to say so in writing.",
    [
        Opt("Receive the legate with full honours.",
            seq("add_piety = 250", "add_prestige = 100", "set_global_variable = eir_hist_1152"),
            stress="zealous = miniscule_stress_impact_loss", ai=50),
        Opt("Receive him politely but remind him whose land this is.",
            seq("add_prestige = 100", "set_global_variable = eir_hist_1152"),
            stress="humble = miniscule_stress_impact_gain", ai=30),
        Opt("Refuse to see him.",
            seq("add_prestige = 50", "add_piety = -100", "set_global_variable = eir_hist_1152",
                "add_character_modifier = { modifier = eir_culdee_strife_modifier years = 5 }"),
            stress="zealous = minor_stress_impact_gain", ai=10),
    ],
    theme="faith", cooldown=200,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= 1152\nNOT = { has_global_variable = eir_hist_1152 }"))

# -----------------------------------------------------------------------------
# 0064 An Exile Comes Seeking Help  (1166)
# -----------------------------------------------------------------------------
EVENTS.append(E(64, "An Exile Comes Seeking Help",
    "A deposed Irish king has arrived at your court, asking for men and shelter.",
    "He was driven from his kingdom by a rival and the High King's army, and he has nothing left but a good name and a grievance. He is already talking about sailing to Britain to look for allies, and the allies he has in mind are not Irish.\n\nHe is a clever and persuasive man, and he is going to be a problem whichever way you answer.",
    [
        Opt("Shelter him, give him a hall, and a quiet word of advice.",
            seq("add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }",
                "remove_short_term_gold = minor_gold_value", "add_prestige = 50",
                "set_global_variable = eir_hist_1166"),
            stress="paranoid = minor_stress_impact_gain\ncompassionate = miniscule_stress_impact_loss", ai=40),
        Opt("Give him an army and send him home to win it back.",
            seq("remove_short_term_gold = medium_gold_value", "eir_defender_levy_effect = yes",
                "add_prestige = 75", "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 4 }",
                "set_global_variable = eir_hist_1166"),
            stress="wrathful = miniscule_stress_impact_loss", ai=30),
        Opt("Send him away. Exiles bring trouble.",
            seq("add_prestige = -25", "set_global_variable = eir_hist_1166",
                "eir_trait_effect = { TRAIT = paranoid OPPOSITE = trusting CHANCE = 15 }"),
            stress="compassionate = minor_stress_impact_gain", ai=30),
    ],
    theme="diplomacy", cooldown=200,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= 1166\nNOT = { has_global_variable = eir_hist_1166 }"))

# -----------------------------------------------------------------------------
# 0065 Foreign Knights Gather in Wales  (1169)
# -----------------------------------------------------------------------------
EVENTS.append(E(65, "Foreign Knights Gather in Wales",
    "Traders report that mailed knights and archers are gathering at the Welsh ports, bound for Ireland.",
    "They are hungry younger sons with no land, led by a lord who has been promised a bride and a kingdom if he can win them. They carry stone-cutters' tools as well as swords.\n\nThey will not stay long on the beach.",
    [
        Opt("Raise the levies and prepare to meet them. (A foreign invasion will follow.)",
            seq("eir_defender_levy_effect = yes", "add_prestige = 50", "set_global_variable = eir_hist_1169"),
            stress="craven = minor_stress_impact_gain", ai=50),
        Opt("Seek allies among the other Irish kings.",
            seq("eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 8 }",
                "add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 4 }", "set_global_variable = eir_hist_1169"),
            trigger="diplomacy >= 8", ai=40),
        Opt("Hope it blows over.",
            seq("add_prestige = -25", "set_global_variable = eir_hist_1169"),
            stress="brave = miniscule_stress_impact_gain", ai=10),
    ],
    theme="war", cooldown=200,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\ncurrent_year >= 1169\nNOT = { has_global_variable = eir_hist_1169 }"))
