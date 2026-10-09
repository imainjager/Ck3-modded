"""v0.3 events: tales, duels, pilgrimages, alliances, circuit incidents and extra artifacts."""
from evdsl import *

EVENTS = []

IR = "eir_is_irish_ruler_trigger = yes\nis_ai = no"
CROWNED = IR + "\nhas_global_variable = eir_done_crowned"

WELSH_PICK = """random_ruler = {
	limit = {
		is_ai = yes
		is_ruler = yes
		culture ?= { has_cultural_pillar = heritage_brythonic }
	}
	save_scope_as = eir_celtic_neighbour
}"""
WELSH_PORTRAIT = "left_portrait = {\n\tcharacter = scope:eir_celtic_neighbour\n\tanimation = personality_honorable\n}"

# ---------------------------------------------------------------------------
# 0150 Commission a Tale
# ---------------------------------------------------------------------------
EVENTS.append(E(150, "The Tale for the Year",
    "Your poets are ready to tell one great story, and you may choose which.",
    "A hundred tales are in the repertoire: raids and wooings, voyages and heroes, laments and quarrels. A court that hears a story all year absorbs its habits.\n\nThe chief poet has narrowed it to six.",
    [
        Opt("The Salmon of Knowledge.",
            "add_character_modifier = { modifier = eir_tale_salmon_modifier years = 6 }\nadd_learning_lifestyle_xp = 50",
            trigger="learning >= 8", ai=40),
        Opt("The Hound of Ulster.",
            seq("add_character_modifier = { modifier = eir_tale_cuchulainn_modifier years = 6 }", "eir_legend_title_effect = { TITLE = primary_title }"),
            trigger="prowess >= 8", ai=40),
        Opt("Finn and the Fianna.",
            seq("add_character_modifier = { modifier = eir_tale_finn_modifier years = 6 }", "set_global_variable = eir_tale_finn"),
            ai=40),
        Opt("Queen Medb and the Cattle-Raid.",
            "add_character_modifier = { modifier = eir_tale_medb_modifier years = 6 }",
            trigger="intrigue >= 8", ai=30),
        Opt("The Children of Lir.",
            "add_character_modifier = { modifier = eir_tale_lir_modifier years = 6 }\nadd_stress = -20",
            ai=30),
        Opt("The Voyage of Saint Brendan.",
            "add_character_modifier = { modifier = eir_tale_brendan_modifier years = 6 }\nadd_piety = 50",
            trigger="piety >= 100", ai=30),
    ],
    theme="learning"))

# ---------------------------------------------------------------------------
# 0151 Single combat
# ---------------------------------------------------------------------------
EVENTS.append(E(151, "The Champion Steps Forward",
    "A Norse champion has stepped out of the line and called a challenge across the field.",
    "Both armies have stopped to watch. He is huge, he is smiling, and he has a very large axe. The old customs say that the kings may settle a war between two men, or that they may refuse and be talked about for generations.",
    [
        Opt("Answer the challenge yourself.",
            RL((45, "duel_win", "You cut him down", [(15, "prowess >= 12"), (10, "has_trait = brave")],
                seq("add_prestige = 250", "add_character_modifier = { modifier = eir_champion_victor_modifier years = 10 }",
                    "eir_trait_effect = { TRAIT = eir_champion_of_ulster OPPOSITE = craven CHANCE = 40 }")),
               (35, "duel_draw", "You fight to a draw, and both walk away", [], "add_prestige = 75"),
               (20, "duel_loss", "He wounds you badly", [(-10, "prowess >= 14")],
                seq("add_prestige = -75", "increase_wounds_effect = { REASON = duel }"))),
            trigger="prowess >= 8", stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=40),
        Opt("Send your champion.",
            RL((55, "duel_proxy_win", "Your champion wins", [], "add_prestige = 120"),
               (45, "duel_proxy_loss", "Your champion falls", [], "add_prestige = -50")),
            ai=40),
        Opt("Refuse, and loose the arrows.",
            seq("add_prestige = -25"), stress="honest = minor_stress_impact_gain", ai=15),
        Opt("Offer him a place at your table instead.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 50", "add_character_modifier = { modifier = eir_foreign_lords_modifier years = 3 }"),
            trigger="diplomacy >= 9", ai=20),
    ],
    theme="war", cooldown=10,
    trigger=IR + "\nprowess >= 6\nis_at_war = no"))

# ---------------------------------------------------------------------------
# 0152 Pilgrimage to Rome
# ---------------------------------------------------------------------------
EVENTS.append(E(152, "The Road to Rome",
    "You set out for Rome on foot, as the pilgrim saints did.",
    "The road crosses sea, mountain and half of France. Pilgrims fall ill, are robbed, are blessed, are lost. The few who return talk about nothing else for the rest of their lives.\n\nHow will you go?",
    [
        Opt("On foot, in a plain cloak, begging for bread.",
            RL((50, "rome_holy", "You return transformed", [(10, "piety >= 400")],
                seq("add_piety = 600", "add_character_modifier = { modifier = eir_rome_pilgrim_modifier years = 15 }",
                    "eir_trait_effect = { TRAIT = eir_saint_king OPPOSITE = cynical CHANCE = 35 }")),
               (30, "rome_tired", "You return exhausted but forgiven", [],
                seq("add_piety = 300", "add_stress = 20")),
               (20, "rome_robbed", "Bandits strip you on the road", [],
                seq("add_piety = 150", "remove_short_term_gold = minor_gold_value"))),
            stress="zealous = miniscule_stress_impact_loss", ai=40),
        Opt("With a large retinue and gifts for the Pope.",
            seq("remove_short_term_gold = major_gold_value", "add_piety = 300", "add_prestige = 150"),
            ai=30),
        Opt("Send an envoy and a relic request in your place.",
            seq("remove_short_term_gold = minor_gold_value", "add_piety = 100"), ai=20),
        Opt("Turn back at Provence.",
            seq("add_piety = 20", "add_stress = 15"), stress="zealous = minor_stress_impact_gain", ai=5),
    ],
    theme="faith"))

# ---------------------------------------------------------------------------
# 0153 The little gospel book
# ---------------------------------------------------------------------------
EVENTS.append(E(153, "A Gospel for the Satchel",
    "The scriptorium has finished a small gospel book, small enough to be carried in a satchel.",
    "It is not as grand as the great books, but it is perfectly made. The abbot says it was meant for a missionary and that you might like to keep it.",
    [
        Opt("Keep it for your own use.",
            seq("eir_make_artifact_effect = { NAME = eir_dimma_name DESC = eir_dimma_desc TYPE = book VISUALS = book MODIFIER = eir_dimma_book_modifier }",
                "add_piety = 75"),
            ai=40),
        Opt("Send it with a missionary to Scotland.",
            seq("add_piety = 150", "add_prestige = 50"), ai=30),
        Opt("Give it to your heir.",
            seq("add_prestige = 50", "primary_heir ?= { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 15 } }"),
            trigger="exists = primary_heir", ai=30),
    ],
    theme="learning"))

# ---------------------------------------------------------------------------
# 0154 Gwynedd
# ---------------------------------------------------------------------------
EVENTS.append(E(154, "An Answer from Gwynedd",
    "The prince of Gwynedd has answered your embassy with a counter-proposal.",
    "He would be glad to be your ally. He would be even more glad to have an Irish princess in his hall, and an Irish army if the Normans press him.\n\nHe has also sent a young poet, to see what you are like.",
    [
        Opt("Offer a marriage and an alliance.",
            seq("add_character_modifier = { modifier = eir_gwynedd_alliance_modifier years = 12 }",
                "scope:eir_celtic_neighbour = { add_opinion = { target = root modifier = eir_gwynedd_friend_opinion opinion = 30 } }",
                "add_prestige = 100"),
            ai=40),
        Opt("Promise help against the Normans, but no marriage.",
            seq("add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 6 }", "add_prestige = 50"),
            ai=30),
        Opt("Send the poet back with a gift and polite words.",
            seq("add_prestige = 25", "remove_short_term_gold = minor_gold_value"), ai=30),
    ],
    theme="diplomacy", portraits=WELSH_PORTRAIT, immediate=WELSH_PICK,
    trigger=IR + "\nhas_global_variable = eir_done_brotherhood\nany_ruler = {\nis_ai = yes\nis_ruler = yes\nculture ?= { has_cultural_pillar = heritage_brythonic }\n}"))

# ---------------------------------------------------------------------------
# 0155 Strathclyde
# ---------------------------------------------------------------------------
EVENTS.append(E(155, "The Last Britons of the North",
    "A messenger from the rock on the Clyde has come to see you.",
    "They are the last of the old kingdom of the north, between the Picts and the Saxons. They speak a tongue that is somewhere between Welsh and Irish, they pay tribute to nobody, and they have asked for a friend.",
    [
        Opt("Promise them friendship and an annual gift.",
            seq("add_character_modifier = { modifier = eir_strathclyde_bond_modifier years = 12 }",
                "scope:eir_celtic_neighbour = { add_opinion = { target = root modifier = eir_gael_pride_opinion opinion = 25 } }",
                "remove_short_term_gold = minor_gold_value", "add_prestige = 75"),
            ai=40),
        Opt("Exchange poets and say little else.",
            seq("add_prestige = 50", "add_learning_lifestyle_xp = 25"), trigger="learning >= 8", ai=30),
        Opt("Turn them away. They are too far to help.",
            "add_prestige = 5", ai=20),
    ],
    theme="diplomacy", portraits=WELSH_PORTRAIT, immediate=WELSH_PICK,
    trigger=IR + "\nhas_global_variable = eir_done_brotherhood\nany_ruler = {\nis_ai = yes\nis_ruler = yes\nculture ?= { has_cultural_pillar = heritage_brythonic }\n}"))

# ---------------------------------------------------------------------------
# 0156 Hebridean marriage
# ---------------------------------------------------------------------------
EVENTS.append(E(156, "A Daughter of the Isles",
    "A galley-lord of the Isles offers his daughter's hand to your house.",
    "The galley-lords of the western seas are hard, practical men who like to know who their friends are. A marriage is the easiest way to be sure.",
    [
        Opt("Accept the marriage for your heir.",
            seq("add_character_modifier = { modifier = eir_hebridean_ties_modifier years = 15 }", "add_prestige = 75",
                "scope:eir_celtic_neighbour = { add_opinion = { target = root modifier = eir_hebridean_kin_opinion opinion = 30 } }"),
            ai=40),
        Opt("Offer a fosterage instead.",
            seq("add_character_modifier = { modifier = eir_foster_ties_modifier years = 8 }", "add_prestige = 25"), ai=30),
        Opt("Decline politely.", "add_prestige = 5", ai=20),
    ],
    theme="family", portraits="left_portrait = {\n\tcharacter = scope:eir_celtic_neighbour\n\tanimation = personality_bold\n}",
    immediate="""random_ruler = {
	limit = {
		is_ai = yes
		is_ruler = yes
		culture ?= { has_cultural_pillar = heritage_goidelic }
		NOT = { this = root }
	}
	save_scope_as = eir_celtic_neighbour
}""",
    trigger=IR + "\nany_ruler = {\nis_ai = yes\nis_ruler = yes\nculture ?= { has_cultural_pillar = heritage_goidelic }\nNOT = { this = root }\n}"))

# ---------------------------------------------------------------------------
# 0157 Armorica voyage
# ---------------------------------------------------------------------------
EVENTS.append(E(157, "The Ship Returns from Armorica",
    "The ship you sent to Brittany has returned, or something has.",
    "The captain stands on the quay with a sunburned face, a mended sail and a very careful expression. What he says will depend on what happened.",
    [
        Opt("Hear his report.",
            RL((50, "arm_silver", "He returns with silver and news", [],
                seq("add_gold = medium_gold_value", "add_character_modifier = { modifier = eir_armorica_voyage_modifier years = 8 }", "add_prestige = 75")),
               (30, "arm_storm", "A storm took half the cargo", [],
                seq("add_prestige = 10", "remove_short_term_gold = minor_gold_value")),
               (20, "arm_pirates", "Pirates took the rest", [(-5, "has_global_variable = eir_unlock_ringfort")],
                seq("add_prestige = -25"))),
            ai=50),
        Opt("Send him out again at once.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 25"), ai=30),
        Opt("Take his report privately.",
            seq("add_prestige = 25", "add_stress = -5"), ai=20),
    ],
    theme="diplomacy"))

# ---------------------------------------------------------------------------
# 0158 Breton refugee
# ---------------------------------------------------------------------------
EVENTS.append(E(158, "A Breton Comes to Court",
    "A Breton nobleman has arrived at your hall, with his family and nothing else.",
    "He speaks a Celtic language that you can almost follow. He was a count at home. Now he bows to everyone and eats whatever he is given.\n\nHe has a good story and a certain dignity. He would like a position.",
    [
        Opt("Give him a hall and an estate.",
            seq("remove_short_term_gold = minor_gold_value", "add_character_modifier = { modifier = eir_breton_refuge_modifier years = 8 }",
                "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 6 }"),
            ai=40),
        Opt("Make him your steward.",
            seq("add_prestige = 50", "add_learning_lifestyle_xp = 25"), trigger="learning >= 8", ai=30),
        Opt("Send him to Wales.", "add_prestige = 10", ai=20),
    ],
    theme="court"))

# ---------------------------------------------------------------------------
# 0160 Circuit incident
# ---------------------------------------------------------------------------
EVENTS.append(E(160, "A Quarrel at the Host's Table",
    "Halfway round the circuit, your host and his neighbour have started a quarrel over the seating.",
    "In the old halls, every man has his place by rank. This one's neighbour has moved the bench half an inch. It is not about the bench.",
    [
        Opt("Judge the matter in front of the court.",
            RL((55, "circ_judged", "Both accept your ruling", [(10, "learning >= 10")],
                seq("add_prestige = 100", "eir_vassal_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 4 }")),
               (45, "circ_bitter", "One leaves in a rage", [],
                seq("add_prestige = -25", "random_vassal = { add_opinion = { target = root modifier = eir_satire_opinion opinion = -15 } }"))),
            trigger="learning >= 6", ai=40),
        Opt("Move the bench yourself, and apologise to both.",
            seq("add_prestige = 25", "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }"),
            stress="arrogant = minor_stress_impact_gain", ai=40),
        Opt("Call for the poets to sing the quarrel into laughter.",
            seq("add_prestige = 75"), trigger="has_global_variable = eir_done_fili", ai=30),
        Opt("Ignore it, and finish your dinner.",
            seq("add_prestige = -10", "add_stress = 10"), ai=10),
    ],
    theme="court", cooldown=10))

# ---------------------------------------------------------------------------
# 0161 A Throne to Give
# ---------------------------------------------------------------------------
EVENTS.append(E(161, "A Throne to Give",
    "A provincial throne is empty, and the rival claimants have come to you for a ruling.",
    "A king has died and left two cousins and a brother. Each says the others have no claim. Each has brought gifts, men and a story. The kings of Ireland are watching to see who you pick.",
    [
        Opt("Back the eldest cousin.",
            seq("add_prestige = 75", "eir_trait_effect = { TRAIT = eir_kingmaker OPPOSITE = humble CHANCE = 20 }",
                "add_character_modifier = { modifier = eir_kingmaker_modifier years = 8 }"),
            ai=40),
        Opt("Back the brother.",
            RL((50, "king_brother_ok", "The brother holds the throne", [],
                seq("add_prestige = 100", "add_character_modifier = { modifier = eir_kingmaker_modifier years = 10 }")),
               (50, "king_brother_fails", "The cousins unite against him", [],
                seq("add_prestige = -50", "add_character_modifier = { modifier = eir_kin_strife_modifier years = 2 }"))),
            ai=30),
        Opt("Propose a split between them.",
            seq("add_prestige = 50", "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 4 }"),
            trigger="diplomacy >= 10", ai=30),
        Opt("Refuse to choose.", "add_prestige = -25", ai=10),
    ],
    theme="court", cooldown=25,
    trigger=CROWNED + "\nhas_global_variable = eir_done_oenach"))

# ---------------------------------------------------------------------------
# 0162 Exile King
# ---------------------------------------------------------------------------
EVENTS.append(E(162, "A King Without a Kingdom",
    "A deposed king rides up to your gate with twelve men and a harpist.",
    "He was driven off his throne by cousins, and by a sudden shortage of friends. He wants shelter, an army, and a chance to say 'I told you so' to everyone who betrayed him.\n\nThe harpist is very good.",
    [
        Opt("Give him a hall and a place at the high table.",
            seq("remove_short_term_gold = minor_gold_value", "add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }",
                "add_prestige = 50"),
            ai=40),
        Opt("Offer him men to take the throne back.",
            seq("eir_defender_levy_effect = yes", "remove_short_term_gold = medium_gold_value", "add_prestige = 75", "add_character_modifier = { modifier = eir_kingmaker_modifier years = 6 }"),
            ai=30),
        Opt("Send him away.", seq("add_prestige = -25", "add_character_modifier = { modifier = eir_exile_modifier years = 1 }"), stress="compassionate = minor_stress_impact_gain", ai=10),
        Opt("Hand him over to his enemies for a price.",
            seq("add_gold = medium_gold_value", "add_prestige = -100"), stress="honest = minor_stress_impact_gain", ai=5),
    ],
    theme="court", cooldown=25,
    trigger=IR + "\nhas_global_variable = eir_done_oenach"))

# ---------------------------------------------------------------------------
# 0163 Harp of Brian
# ---------------------------------------------------------------------------
EVENTS.append(E(163, "The Harp of the High King",
    "A harp is said to have belonged to Brian himself. A monastery now offers it to you.",
    "The harp is old. It has been carried in battle, mended three times, and its fittings are dull gold. A monk says that it plays by itself, once a year, in the dead of night. The monks do not say who has heard it.",
    [
        Opt("Keep it in your hall.",
            seq("add_character_modifier = { modifier = eir_harp_of_brian_modifier years = 20 }", "add_prestige = 100"), ai=40),
        Opt("Give it to your chief poet.",
            seq("add_character_modifier = { modifier = eir_fili_patron_modifier years = 8 }", "add_prestige = 50"), ai=30),
        Opt("Leave it with the monastery, and pay for a feast day.",
            seq("add_piety = 100", "remove_short_term_gold = minor_gold_value"), ai=30),
    ],
    theme="legend", cooldown=40,
    trigger=IR + "\nhas_global_variable = eir_hist_1014"))

# ---------------------------------------------------------------------------
# 0164 Bell shrine
# ---------------------------------------------------------------------------
EVENTS.append(E(164, "The Shrine for the Saint's Bell",
    "The saint's old iron bell is falling apart, and the monks want to make it a shrine.",
    "The bell has been rung for centuries. It is cracked, and the iron is flaking. A shrine of bronze and silver would preserve it, and the monks have asked who will pay.",
    [
        Opt("Pay for the shrine, and keep it in your chapel.",
            seq("remove_short_term_gold = medium_gold_value",
                "eir_make_artifact_effect = { NAME = eir_bell_shrine_name DESC = eir_bell_shrine_desc TYPE = goblet VISUALS = goblet MODIFIER = eir_bell_shrine_modifier }",
                "add_piety = 150"),
            ai=40),
        Opt("Pay for the shrine, and leave it with the monks.",
            seq("remove_short_term_gold = medium_gold_value", "add_piety = 250"), ai=40),
        Opt("Decline.", "add_piety = -25", ai=10),
    ],
    theme="faith", cooldown=40,
    trigger=IR + "\nhas_global_variable = eir_done_armagh\ngold >= medium_gold_value"))

# ---------------------------------------------------------------------------
# 0165 Lunula
# ---------------------------------------------------------------------------
EVENTS.append(E(165, "A Crescent of Gold",
    "A ploughman has turned up a gold crescent as wide as his hand.",
    "It is a thin sheet of beaten gold, shaped like a new moon, decorated with fine chevrons. It is far older than any king of Ireland. It is also exactly the kind of thing a king would want.",
    [
        Opt("Buy it, and wear it at feasts.",
            seq("remove_short_term_gold = minor_gold_value",
                "eir_make_artifact_effect = { NAME = eir_lunula_name DESC = eir_lunula_desc TYPE = necklace VISUALS = necklace MODIFIER = eir_lunula_modifier }",
                "add_prestige = 75"),
            ai=40),
        Opt("Reward the ploughman and let him keep it.", seq("remove_short_term_gold = minor_gold_value", "add_prestige = 50"), ai=30),
        Opt("Melt it into coin.", seq("add_gold = medium_gold_value", "add_prestige = -25"), stress="arrogant = minor_stress_impact_gain", ai=10),
    ],
    theme="legend", cooldown=40,
    trigger=IR + "\nhas_global_variable = eir_unlock_ringfort\ngold >= minor_gold_value"))

# ---------------------------------------------------------------------------
# 0166 Ogham blade
# ---------------------------------------------------------------------------
EVENTS.append(E(166, "A Blade with Letters",
    "A smith has made a sword with a line of ogham carved along the spine.",
    "He says the letters spell the name of a hero. Nobody in the hall can read ogham. The smith promises that the sword is real.",
    [
        Opt("Buy the blade for yourself.",
            seq("remove_short_term_gold = minor_gold_value",
                "eir_make_artifact_effect = { NAME = eir_ogham_blade_name DESC = eir_ogham_blade_desc TYPE = sword VISUALS = sword MODIFIER = eir_ogham_blade_modifier }",
                "add_prestige = 50"),
            trigger="prowess >= 6", ai=40),
        Opt("Give it to your champion.", seq("remove_short_term_gold = minor_gold_value", "add_prestige = 75"), ai=40),
        Opt("Send the smith away.", "add_prestige = 5", ai=10),
    ],
    theme="martial", cooldown=40,
    trigger=IR + "\nhas_global_variable = eir_unlock_fianna\ngold >= minor_gold_value"))

# ---------------------------------------------------------------------------
# 0167 Chieftain's torc
# ---------------------------------------------------------------------------
EVENTS.append(E(167, "A Lesser King's Torc",
    "A dying under-king leaves you his gold neck-ring in his will.",
    "He was nobody's friend and nobody's enemy. He says the torc has been worn by every chieftain of his line since the days of the Tuatha Dé. He asks that you wear it and remember him.",
    [
        Opt("Wear it, and remember him.",
            seq("eir_make_artifact_effect = { NAME = eir_chieftain_torc_name DESC = eir_chieftain_torc_desc TYPE = necklace VISUALS = necklace MODIFIER = eir_chieftain_torc_modifier }",
                "add_prestige = 75"),
            ai=50),
        Opt("Pass it to your heir.", seq("add_prestige = 50", "primary_heir ?= { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 20 } }"), trigger="exists = primary_heir", ai=30),
        Opt("Return it to the dead man's kindred.", seq("add_piety = 50", "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 3 }"), ai=20),
    ],
    theme="legend", cooldown=40,
    trigger=CROWNED + "\nprestige >= 300"))

# ---------------------------------------------------------------------------
# 0168 Bog butter
# ---------------------------------------------------------------------------
EVENTS.append(E(168, "Butter from the Bog",
    "A farmer has dug a keg of butter out of a bog, three hundred years old and still edible.",
    "It was buried against raiders, famine and Vikings. It is very old, and it tastes the way old butter tastes. The farmer wants to know whether it belongs to him or to you.",
    [
        Opt("Let him keep it.", seq("add_prestige = 10", "random_held_title = { limit = { tier = tier_county } add_county_modifier = { modifier = eir_loyal_county_modifier years = 3 } }"), ai=40),
        Opt("Buy it, and display it as a marvel.", seq("remove_short_term_gold = minor_gold_value", "add_prestige = 40"), ai=30),
        Opt("Order the bog drained to look for more.",
            RL((40, "bog_more", "A hoard of butter kegs and a gold ring", [],
                seq("add_gold = minor_gold_value", "random_held_title = { limit = { tier = tier_county } add_county_modifier = { modifier = eir_bog_butter_modifier years = 15 } }")),
               (60, "bog_mud", "Nothing but mud", [], "remove_short_term_gold = minor_gold_value")),
            ai=20),
    ],
    theme="court", cooldown=20, trigger=IR + "\nany_held_title = { tier = tier_county }"))

# ---------------------------------------------------------------------------
# 0169 Crozier
# ---------------------------------------------------------------------------
EVENTS.append(E(169, "The Abbot's Crozier",
    "An abbot lies dying and wants his crozier to go somewhere safe.",
    "It is a bronze crook with a hollow in the head for a holy relic. It has belonged to six abbots in a row. The monks are quarrelling over who should have it next.",
    [
        Opt("Take it into your own keeping.",
            seq("add_character_modifier = { modifier = eir_crozier_modifier years = 15 }", "add_piety = 100"),
            stress="zealous = miniscule_stress_impact_loss", ai=40),
        Opt("Give it to the monk the abbot named.", seq("add_piety = 150", "add_prestige = 25"), ai=40),
        Opt("Offer to settle the quarrel in court.",
            RL((60, "croz_settled", "The monks accept your ruling", [(10, "learning >= 10")], "add_piety = 200"),
               (40, "croz_unrest", "Two monasteries stop speaking to each other", [], "add_piety = -25")),
            ai=20),
    ],
    theme="faith", cooldown=40,
    trigger=IR + "\nhas_global_variable = eir_done_synod"))

# ---------------------------------------------------------------------------
# 0170 Hostage comes home
# ---------------------------------------------------------------------------
EVENTS.append(E(170, "A Hostage Returns",
    "A boy taken as a hostage years ago comes home as a man.",
    "He has been at your court since childhood. He knows your halls as well as his own, and he is not sure whom he is loyal to. His father is waiting at the gate with an expression you cannot read.",
    [
        Opt("Welcome him as a foster-son.",
            seq("random_vassal = { add_trait = eir_fosterling }", "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 5 }", "add_prestige = 50"),
            ai=40),
        Opt("Return him with gifts and thanks.",
            seq("remove_short_term_gold = minor_gold_value", "add_prestige = 25"), ai=30),
        Opt("Say little, and let him go quietly.",
            seq("random_vassal = { add_trait = eir_hostage_scarred }", "add_prestige = -10"), ai=20),
    ],
    theme="family"))

# ---------------------------------------------------------------------------
# 0171 Cain law incident
# ---------------------------------------------------------------------------
EVENTS.append(E(171, "The Cáin Is Tested",
    "A man has been dragged from sanctuary and killed on the steps of a church.",
    "The law you swore has been broken in front of a hundred witnesses. The killers are the household of a powerful lord. The bishop is waiting for your answer.",
    [
        Opt("Demand the honour-price in full.",
            seq("add_piety = 100", "random_vassal = { add_opinion = { target = root modifier = eir_claim_revoked_opinion opinion = -15 } }"),
            ai=40),
        Opt("Raise an army and burn the lord's hall.",
            seq("eir_defender_levy_effect = yes", "add_piety = 150", "add_prestige = 75", "add_character_modifier = { modifier = eir_raider_infamy_modifier years = 4 }"),
            stress="compassionate = minor_stress_impact_gain", ai=15),
        Opt("Accept a smaller fine, and move on.",
            seq("add_gold = minor_gold_value", "add_piety = -75"), stress="zealous = minor_stress_impact_gain", ai=30),
        Opt("Do penance in front of the church yourself.",
            seq("add_piety = 200", "add_prestige = -25", "add_stress = -10"), trigger="piety >= 100", ai=15),
    ],
    theme="faith"))

# ---------------------------------------------------------------------------
# 0172 Four provinces dispute
# ---------------------------------------------------------------------------
EVENTS.append(E(172, "Who Marches First?",
    "The four provincial kings cannot agree on who leads the van.",
    "Munster says it has always led. Leinster says that Munster has always lost. Connacht says it will go first or not at all. Ulster says nothing and looks at its sword.\n\nThe armies stand idle while the tent-poles are argued over.",
    [
        Opt("Put the Munstermen in the van.",
            seq("add_prestige = 50", "random_vassal = { add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 15 } }"), ai=30),
        Opt("Let the kings draw lots.",
            RL((60, "prov_lots_ok", "The lots are accepted", [], "add_prestige = 75"),
               (40, "prov_lots_bad", "A king claims the lots were rigged", [], "add_prestige = -25")),
            ai=40),
        Opt("Take the van yourself.",
            seq("add_prestige = 100", "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -4 }"),
            trigger="prowess >= 10", stress="humble = minor_stress_impact_gain", ai=25),
        Opt("Appeal to the poets to remind them of an earlier peace.",
            seq("add_prestige = 75", "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 5 }"),
            trigger="has_global_variable = eir_done_fili", ai=30),
    ],
    theme="war"))
