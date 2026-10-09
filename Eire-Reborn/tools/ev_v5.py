"""v0.5 events: the saints, the Irish Sea."""
from evdsl import *

EVENTS = []

# ---------------------------------------------------------------------------
# 0180 Honour the Saints
# ---------------------------------------------------------------------------
EVENTS.append(E(180, "A Patron Saint for the Reign",
    "Three saints have a claim on your court, and you can honour only one properly.",
    "Brigid's nuns tend a fire that has not gone out since before the church. Colmcille's monks keep the psalters he copied by moonlight. Patrick's bishops carry his bell and his staff. Each will bless a king who honours them, and each notices if a king prefers another.",
    [
        Opt("Brigid: tend the flame at Kildare.",
            seq("add_character_modifier = { modifier = eir_brigid_cult_modifier years = 15 }",
                "eir_held_county_modifier_effect = { MODIFIER = eir_kildare_flame_modifier YEARS = 25 }",
                "add_piety = 300", "trigger_event = { id = eir.0031 days = 60 }"),
            stress="zealous = miniscule_stress_impact_loss", ai=40),
        Opt("Colmcille: endow the psalters and the island monasteries.",
            seq("add_character_modifier = { modifier = eir_colmcille_cult_modifier years = 15 }",
                "eir_held_county_modifier_effect = { MODIFIER = eir_monastery_county_modifier YEARS = 30 }",
                "add_piety = 300", "add_learning_lifestyle_xp = 100"),
            trigger="learning >= 8", ai=40),
        Opt("Patrick: raise a shrine at his bell and staff.",
            seq("add_character_modifier = { modifier = eir_patrick_cult_modifier years = 15 }",
                "eir_held_county_modifier_effect = { MODIFIER = eir_monasterboice_modifier YEARS = 30 }",
                "add_piety = 300", "trigger_event = { id = eir.0043 days = 60 }"),
            trigger="has_global_variable = eir_done_cashel", ai=40),
        Opt("Honour all three equally, and satisfy none.",
            seq("add_piety = 100", "add_prestige = -50", "add_stress = 10"),
            stress="zealous = minor_stress_impact_gain", ai=5),
    ],
    theme="faith"))

# ---------------------------------------------------------------------------
# 0190 The Sea-Kings Gather
# ---------------------------------------------------------------------------
EVENTS.append(E(190, "The Sea-Kings Come to Terms",
    "The Norse-Gael merchants of the Irish Sea have come to see what a sea-king of Ireland is worth.",
    "They are traders from Dublin, Man and the Hebrides, men who speak three languages and carry silver in their boots. For generations they have taken Irish cattle and slaves at their own prices. A king who builds quays and ships may finally set the price himself.",
    [
        Opt("Invite them to build quays in your harbours, on your terms.",
            seq("eir_held_county_modifier_effect = { MODIFIER = eir_wooden_harbour_modifier YEARS = 25 }",
                "add_gold = medium_gold_value", "add_prestige = 150",
                "add_character_modifier = { modifier = eir_hospitality_modifier years = 6 }"),
            trigger="diplomacy >= 10", ai=40),
        Opt("Charter an Irish merchant guild to compete with them.",
            seq("add_stewardship_lifestyle_xp = 100", "add_prestige = 100", "remove_short_term_gold = medium_gold_value",
                "add_character_modifier = { modifier = eir_irish_sea_trade_modifier years = 8 }"),
            trigger="stewardship >= 12", ai=40),
        Opt("Levy a toll on every foreign ship that enters.",
            RL((55, "toll_ok", "The merchants pay and grumble", [(10, "stewardship >= 14")],
                seq("add_gold = major_gold_value", "add_prestige = 50")),
               (45, "toll_boycott", "They sail to Wales instead", [],
                seq("add_gold = minor_gold_value", "add_prestige = -75",
                    "random_held_title = { limit = { tier = tier_county } add_county_modifier = { modifier = eir_cattle_raided_modifier years = 4 } }"))),
            ai=30),
        Opt("Buy longships from them and make your own fleet.",
            seq("remove_short_term_gold = major_gold_value", "eir_defender_levy_effect = yes", "add_prestige = 100",
                "add_character_modifier = { modifier = eir_sea_king_modifier years = 8 }"),
            ai=25),
        Opt("Send them away. The Gael have never needed the Norse.",
            seq("add_prestige = 50", "eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 5 }"),
            stress="greedy = minor_stress_impact_gain", ai=10),
    ],
    theme="diplomacy"))

# ---------------------------------------------------------------------------
# 0191 Master of the Irish Sea
# ---------------------------------------------------------------------------
EVENTS.append(E(191, "The Coast Takes Notice",
    "A year after you proclaimed yourself master of the Irish Sea, the rival coasts have decided how to answer.",
    "Chester has raised its harbour dues. The jarls of Man are courting the Welsh. A Bristol merchant has been caught smuggling hides past your customs. Your own captains are asking whether they may seize the next foreign ship that does not dip its flag.",
    [
        Opt("Hold a naval review off Dublin, and let the world see the fleet.",
            seq("remove_short_term_gold = medium_gold_value", "eir_defender_levy_effect = yes", "add_prestige = 300"),
            ai=40),
        Opt("Blockade a rival port until the dues are lowered.",
            RL((50, "block_win", "The port yields", [(15, "stewardship >= 14")],
                seq("add_prestige = 200", "add_gold = medium_gold_value")),
               (50, "block_fail", "The blockade is broken", [],
                seq("add_prestige = -100", "remove_short_term_gold = minor_gold_value"))),
            stress="compassionate = minor_stress_impact_gain", ai=30),
        Opt("Offer free passage to allies and hostages to the doubtful.",
            seq("add_prestige = 150", "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 6 }"),
            trigger="diplomacy >= 12", ai=40),
        Opt("Seize the smuggler's cargo and hang the man.",
            seq("add_gold = medium_gold_value", "add_prestige = 100", "add_character_modifier = { modifier = eir_raider_infamy_modifier years = 5 }"),
            stress="compassionate = minor_stress_impact_gain", ai=15),
    ],
    theme="war"))
