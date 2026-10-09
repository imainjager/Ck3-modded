"""Everyday Irish flavour: festivals, legends, animals, the land, and the people of the countryside."""
from evdsl import *

EVENTS = []

IRISH_PLAYER = "eir_is_irish_ruler_trigger = yes\nis_ai = no"

# -----------------------------------------------------------------------------
# 0030 Samhain Night
# -----------------------------------------------------------------------------
EVENTS.append(E(30, "Samhain Night",
    "On the last night of the year the veil between the worlds is thin.",
    "The fires are lit on every hill, the cattle are driven home, and the old people say the dead walk among the living until dawn. The priests say it is a pagan custom. The people do it anyway.\n\nWhat you do tonight will be remembered, one way or the other.",
    [
        Opt("Leave out milk and honey for the dead.",
            seq("add_piety = 25", "add_prestige = 25",
                "add_character_modifier = { modifier = eir_hospitality_modifier years = 1 }"),
            stress="zealous = miniscule_stress_impact_gain\ncynical = miniscule_stress_impact_gain", ai=40),
        Opt("Light the great fire and drive the cattle between the flames.",
            seq("add_prestige = 75",
                "add_character_modifier = { modifier = eir_cattle_rich_modifier years = 3 }"),
            stress="zealous = minor_stress_impact_gain", ai=30),
        Opt("Spend the night alone on a barrow-mound.",
            RL((50, "barrow_gift", "The dead speak to you kindly, and you wake at peace.",
                [(15, "has_trait = brave"), (10, "has_trait = zealous")],
                seq("add_character_modifier = { modifier = eir_sidhe_favour_modifier years = 5 }",
                    "add_prestige = 100")),
               (40, "barrow_dread", "Something followed you home, and it has not left.",
                [],
                seq("add_character_modifier = { modifier = eir_samhain_dread_modifier years = 3 }"))),
            trigger="""OR = {
	has_trait = brave
	has_trait = zealous
	prowess >= 10
}""",
            stress="craven = minor_stress_impact_gain", ai=15),
        Opt("Bar the door and say a prayer.",
            "add_piety = 25",
            stress="brave = miniscule_stress_impact_gain\nzealous = miniscule_stress_impact_loss", ai=15),
    ],
    theme="faith", cooldown=8, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0031 Saint Brigid's Day
# -----------------------------------------------------------------------------
EVENTS.append(E(31, "Saint Brigid's Day",
    "The first day of spring is the feast of Saint Brigid, patroness of the dairy and the hearth.",
    "Rushes are woven into crosses, a sheaf is left for the saint's white cow, and every dairy in the land is blessed with a drop of holy water. The old goddess and the saint are, somehow, still the same woman.\n\nThe people expect their king to join in.",
    [
        Opt("Join the procession and weave a cross with your own hands.",
            seq("add_piety = 50", "add_prestige = 25",
                "eir_vassal_opinion_effect = { MODIFIER = eir_gael_pride_opinion OPINION = 5 }"),
            stress="zealous = miniscule_stress_impact_loss\ncynical = miniscule_stress_impact_gain", ai=40),
        Opt("Bless the herds in the saint's name.",
            "add_character_modifier = { modifier = eir_cattle_rich_modifier years = 3 }\nadd_piety = 25",
            ai=40),
        Opt("Send a rich gift to Kildare and stay home.",
            "remove_short_term_gold = minor_gold_value\nadd_piety = 50",
            stress="greedy = miniscule_stress_impact_gain", ai=20),
    ],
    theme="faith", cooldown=10, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0032 The Beltane Fires
# -----------------------------------------------------------------------------
EVENTS.append(E(32, "The Beltane Fires",
    "On the first day of summer, twin fires are lit on every hill, and the herds are driven between them for luck.",
    "Priests grumble. Poets sing. The young people leap the embers hand in hand and are not always seen again until morning.\n\nThe festival is older than the Church and will outlast it, and a wise king knows better than to try to stop it.",
    [
        Opt("Light the royal fires and lead the dance.",
            "add_character_modifier = { modifier = eir_beltane_vigor_modifier years = 2 }\nadd_prestige = 50",
            stress="shy = minor_stress_impact_gain\ngregarious = miniscule_stress_impact_loss", ai=50),
        Opt("Forbid the fires as a pagan survival.",
            seq("add_piety = 75", "eir_court_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -8 }",
                "eir_trait_effect = { TRAIT = zealous OPPOSITE = cynical CHANCE = 15 }"),
            stress="cynical = minor_stress_impact_gain\nzealous = miniscule_stress_impact_loss", ai=10),
        Opt("Turn a blind eye and keep your own counsel.",
            "add_prestige = 10",
            ai=30),
    ],
    theme="family", cooldown=10, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0033 The Fair at Lughnasa
# -----------------------------------------------------------------------------
EVENTS.append(E(33, "The Fair at Lughnasa",
    "The harvest fair is held on the first day of August, with games, trading and matchmaking.",
    "Horse races, wrestling, harp contests and quarrels over cattle are all on the programme, and half the marriages in the country begin here.\n\nThe fair is a chance to meet every important man in your realm in one place and see what he wants.",
    [
        Opt("Host the fair on your own land and pay for the games.",
            seq("remove_short_term_gold = medium_gold_value",
                "add_prestige = 100",
                "capital_county ?= { add_county_modifier = { modifier = eir_tailteann_county_modifier years = 5 } }",
                "eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 6 }"),
            stress="greedy = miniscule_stress_impact_gain", ai=40),
        Opt("Enter the wrestling yourself.",
            RL((50, "wrestle_won", "You throw every challenger, and the crowd goes wild.",
                [(20, "prowess >= 14")],
                "add_prestige = 150\nadd_character_modifier = { modifier = eir_wolfhound_bond_modifier years = 3 }"),
               (40, "wrestle_lost", "You are thrown in the mud, and the crowd goes wild for a different reason.",
                [],
                "add_prestige = -50")),
            trigger="prowess >= 8",
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=20),
        Opt("Spend the fair arranging marriages between your kin and your vassals'.",
            seq("eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 8 }",
                "add_character_modifier = { modifier = eir_foster_ties_modifier years = 5 }"),
            trigger="diplomacy >= 8", ai=40),
    ],
    theme="family", cooldown=8, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0034 The Banshee's Wail
# -----------------------------------------------------------------------------
EVENTS.append(E(34, "The Banshee's Wail",
    "In the dead of night, an unearthly keening is heard outside your window.",
    "The servants swear it was a woman in white, combing her long hair beside the well. The dogs would not enter the yard. The priest says there is no such thing.\n\nIn Ireland the banshee only cries for those who are about to die, and the people have started to look at you strangely.",
    [
        Opt("Make your peace with God and settle your affairs.",
            seq("add_piety = 100", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 3 }"),
            stress="zealous = miniscule_stress_impact_loss\ncynical = minor_stress_impact_gain", ai=40),
        Opt("Laugh it off, and have a feast to prove it.",
            RL((60, "banshee_laugh_ok", "The omen passes, and your feast is remembered for its boldness.",
                [(10, "has_trait = brave")],
                "add_prestige = 75"),
               (30, "banshee_laugh_bad", "Ill luck follows. Someone close to you falls sick.",
                [],
                "eir_trait_effect = { TRAIT = eir_banshee_marked OPPOSITE = eir_banshee_marked CHANCE = 100 }")),
            stress="zealous = minor_stress_impact_gain\ncraven = miniscule_stress_impact_gain", ai=30),
        Opt("Summon the old woman who knows the signs.",
            seq("add_character_modifier = { modifier = eir_sidhe_favour_modifier years = 3 }",
                "add_learning_lifestyle_xp = 50"),
            trigger="learning >= 8",
            stress="cynical = miniscule_stress_impact_gain", ai=30),
    ],
    theme="death", cooldown=20,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nage >= 40"))

# -----------------------------------------------------------------------------
# 0035 The Stone Cried Out
# -----------------------------------------------------------------------------
EVENTS.append(E(35, "The Stone Cried Out",
    "The Lia Fáil on the Hill of Tara roared when you passed.",
    "No one has heard it roar in living memory. The stone is said to cry out beneath a rightful king, and every priest, poet and peasant on the hill heard it.\n\nThe poets are already writing it down, and the story will be told, whether you tell it or not.",
    [
        Opt("Take it as a sign and proclaim your right to the high kingship.",
            seq("add_character_modifier = { modifier = eir_lia_fail_blessing_modifier years = 10 }",
                "add_prestige = 200", "add_piety = 25",
                "eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 8 }"),
            stress="humble = minor_stress_impact_gain\narrogant = miniscule_stress_impact_loss", ai=40),
        Opt("Say little and let the poets spread the tale.",
            "add_character_modifier = { modifier = eir_fili_patron_modifier years = 5 }\nadd_prestige = 100",
            stress="humble = miniscule_stress_impact_loss", ai=40),
        Opt("Have the priests explain it as thunder.",
            "add_piety = 50\nadd_prestige = -25",
            stress="zealous = miniscule_stress_impact_loss\ncynical = miniscule_stress_impact_gain", ai=10),
    ],
    theme="legend", cooldown=25,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_title = title:d_meath"))

# -----------------------------------------------------------------------------
# 0036 The Salmon of Knowledge
# -----------------------------------------------------------------------------
EVENTS.append(E(36, "The Salmon of Knowledge",
    "A fisherman brings you a great salmon from the pool beneath the hazel tree.",
    "It is the biggest salmon he has ever seen, with spots like gold coins. The old story says that whoever eats the salmon of knowledge will know everything in the world.\n\nThe fisherman does not look like he believes the old stories. He is, however, very pleased with himself.",
    [
        Opt("Roast it yourself, and eat the first bite.",
            RL((50, "salmon_wisdom", "The first bite is surprisingly good, and the fish's wisdom stays with you.",
                [(15, "learning >= 12")],
                "add_learning_lifestyle_xp = 150\neir_trait_effect = { TRAIT = shrewd OPPOSITE = shrewd CHANCE = 30 }"),
               (40, "salmon_burn", "You burn your thumb, and the story ends there.",
                [],
                "add_prestige = 10")),
            stress="cynical = miniscule_stress_impact_gain", ai=40),
        Opt("Give it to your court poet.",
            "add_character_modifier = { modifier = eir_fili_patron_modifier years = 3 }\nadd_prestige = 25",
            trigger="any_courtier = { has_trait = eir_ollamh }", ai=40),
        Opt("Reward the fisherman and serve it at the feast.",
            "remove_short_term_gold = minor_gold_value\nadd_character_modifier = { modifier = eir_hospitality_modifier years = 2 }",
            ai=20),
    ],
    theme="learning", cooldown=20, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0037 The Fairy Mound
# -----------------------------------------------------------------------------
EVENTS.append(E(37, "The Fairy Mound",
    "A steward wants to plough under a green mound in [eir_mound_county.GetName] that the locals say is a fairy fort.",
    "The land beneath it is the best for miles, and the steward says the superstition is costing you money. The local people say the mound belongs to the good folk and will not be touched.\n\nThe good folk, they say, have a long memory.",
    [
        Opt("Leave the mound alone and leave an offering at its base.",
            seq("remove_short_term_gold = minor_gold_value",
                "scope:eir_mound_county = { add_county_modifier = { modifier = eir_sidhe_blessing_modifier years = 10 } }",
                "add_character_modifier = { modifier = eir_sidhe_favour_modifier years = 5 }"),
            stress="cynical = minor_stress_impact_gain", ai=40),
        Opt("Plough it under. Superstition costs gold.",
            seq("add_gold = medium_gold_value",
                "scope:eir_mound_county = { add_county_modifier = { modifier = eir_sidhe_curse_modifier years = 8 } }",
                "add_character_modifier = { modifier = eir_sidhe_anger_modifier years = 5 }"),
            stress="cynical = minor_stress_impact_gain", ai=30),
        Opt("Have the priest bless the mound and the field together.",
            seq("add_piety = 50",
                "scope:eir_mound_county = { add_county_modifier = { modifier = eir_holy_well_modifier years = 10 } }"),
            trigger="piety >= 30", ai=30),
    ],
    theme="legend", cooldown=15,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nany_realm_county = { count >= 1 }",
    immediate="random_realm_county = { save_scope_as = eir_mound_county }"))

# -----------------------------------------------------------------------------
# 0038 Treasure in the Bog
# -----------------------------------------------------------------------------
EVENTS.append(E(38, "Treasure in the Bog",
    "Peat-cutters in [eir_bog_county.GetName] have turned up something gold.",
    "It is a heavy twisted ring, the kind worn by kings before there was a Church, black with the peat and perfectly preserved. There may be more beneath it.\n\nThe bog gives and the bog takes, but this time it gave.",
    [
        Opt("Dig carefully and see what else the bog is hiding.",
            RL((50, "bog_rich", "The bog yields a hoard of old gold.",
                [(15, "stewardship >= 12")],
                seq("add_gold = major_gold_value",
                    "scope:eir_bog_county = { add_county_modifier = { modifier = eir_peat_wealth_modifier years = 15 } }",
                    "trigger_event = { id = eir.0082 days = 30 }")),
               (40, "bog_empty", "Nothing else turns up, but the gold ring is real.",
                [],
                "add_gold = medium_gold_value")),
            ai=40),
        Opt("Give the ring to the Church as a gift.",
            "add_piety = 150\nadd_character_modifier = { modifier = eir_saints_blessing_modifier years = 3 }",
            trigger="piety >= 30", ai=20),
        Opt("Melt it down for coin.",
            "add_gold = medium_gold_value",
            stress="cynical = minor_stress_impact_gain", ai=30),
    ],
    theme="legend", cooldown=20,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nany_realm_county = { count >= 1 }",
    immediate="random_realm_county = { save_scope_as = eir_bog_county }"))

# -----------------------------------------------------------------------------
# 0050 A Wolfhound Puppy
# -----------------------------------------------------------------------------
EVENTS.append(E(50, "A Wolfhound Puppy",
    "A vassal brings you a great Irish wolfhound puppy as a gift.",
    "The puppy is already the size of a calf, with a rough grey coat and eyes that follow everything. The old tales say the hounds of Ireland could kill a wolf and guard a king's sleep.\n\nIt is a very good gift, and a very large dog.",
    [
        Opt("Keep the puppy and train it yourself.",
            "add_character_modifier = { modifier = eir_wolfhound_bond_modifier years = 15 }",
            stress="lazy = miniscule_stress_impact_gain\ndiligent = miniscule_stress_impact_loss", ai=50),
        Opt("Give it to your champion as a mark of favour.",
            "add_prestige = 50\neir_vassal_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 4 }",
            ai=30),
        Opt("Send it to a foreign king as a diplomatic gift.",
            "add_prestige = 75\nadd_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 3 }",
            trigger="diplomacy >= 8", ai=20),
    ],
    theme="hunting", cooldown=20, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0051 Feast at the Ringfort
# -----------------------------------------------------------------------------
EVENTS.append(E(51, "Feast at the Ringfort",
    "A feast has been laid in your hall, and every guest has a story to tell.",
    "Beef and pork, ale and mead, harpers and storytellers. The Irish hall is a place where honour is measured by what is poured, and every chieftain in the district has come to see how well you pour.\n\nHospitality is the oldest of the Irish virtues, and the most expensive.",
    [
        Opt("Spare nothing. Let them talk of this feast for a generation.",
            seq("remove_short_term_gold = medium_gold_value",
                "add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }",
                "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 12 }",
                "add_prestige = 75"),
            stress="greedy = minor_stress_impact_gain\ngenerous = miniscule_stress_impact_loss", ai=40),
        Opt("A decent meal, no more.",
            "remove_short_term_gold = minor_gold_value\neir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }",
            ai=40),
        Opt("Let your steward serve the cheaper cuts and water the ale.",
            seq("add_gold = minor_gold_value", "eir_court_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -6 }",
                "add_prestige = -25"),
            stress="generous = minor_stress_impact_gain\ngreedy = miniscule_stress_impact_loss", ai=10),
    ],
    theme="feast_activity", cooldown=6, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0052 The Hunt of the Great Stag
# -----------------------------------------------------------------------------
EVENTS.append(E(52, "The Hunt of the Great Stag",
    "Your huntsmen report a stag of astonishing size in the forest.",
    "It is said to have twelve points on each antler and a coat so dark it looks black in the dusk. The old stories say that the Fianna hunted such beasts, and so did kings before them.\n\nYour huntsmen are begging you to lead the hunt.",
    [
        Opt("Lead the hunt yourself.",
            RL((50, "stag_taken", "You take the great stag after a day's chase.",
                [(20, "prowess >= 14"), (10, "has_trait = brave")],
                "add_prestige = 150\nadd_character_modifier = { modifier = eir_fianna_spirit_modifier years = 5 }"),
               (35, "stag_escapes", "The stag leads you a merry chase and escapes.",
                [],
                "add_prestige = -25\neir_trait_effect = { TRAIT = wrathful OPPOSITE = calm CHANCE = 10 }")),
            trigger="prowess >= 8",
            stress="craven = minor_stress_impact_gain\nbrave = miniscule_stress_impact_loss", ai=40),
        Opt("Send your huntsmen and wait for the result.",
            "add_prestige = 25",
            ai=30),
        Opt("Spare the stag. A creature so fine should live.",
            "add_piety = 50\nadd_character_modifier = { modifier = eir_sidhe_favour_modifier years = 3 }",
            stress="wrathful = miniscule_stress_impact_gain\ncompassionate = miniscule_stress_impact_loss", ai=30),
    ],
    theme="hunting", cooldown=15, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0053 A Bad Harvest
# -----------------------------------------------------------------------------
EVENTS.append(E(53, "A Bad Harvest",
    "The harvest has failed in [eir_famine_county.GetName].",
    "Rain in the hay-making and blight in the barley have done what no raider could. Granaries are half empty, and the poor are already eating next year's seed corn.\n\nThe people are looking to their lord, the way people always do.",
    [
        Opt("Open the granaries and feed the county from your own stores.",
            seq("remove_short_term_gold = medium_gold_value",
                "scope:eir_famine_county = { add_county_modifier = { modifier = eir_loyal_county_modifier years = 8 } }",
                "add_prestige = 50"),
            stress="greedy = minor_stress_impact_gain\ncompassionate = miniscule_stress_impact_loss", ai=40),
        Opt("Do nothing. Famine is the will of God.",
            seq("scope:eir_famine_county = { add_county_modifier = { modifier = eir_famine_modifier years = 4 } }",
                "add_character_modifier = { modifier = eir_lean_years_modifier years = 3 }"),
            stress="compassionate = minor_stress_impact_gain", ai=10),
        Opt("Raise the grain tax and sell the surplus elsewhere.",
            seq("add_gold = medium_gold_value",
                "scope:eir_famine_county = { add_county_modifier = { modifier = eir_famine_modifier years = 6 } }",
                "scope:eir_famine_county = { add_county_modifier = { modifier = eir_punitive_levy_modifier years = 3 } }"),
            stress="compassionate = minor_stress_impact_gain\ngreedy = miniscule_stress_impact_loss", ai=10),
        Opt("Lead a procession to the holy well.",
            RL((50, "well_answers", "The rains stop, and the people credit the procession.",
                [(15, "piety >= 200"), (10, "has_trait = zealous")],
                "add_piety = 100\nscope:eir_famine_county = { add_county_modifier = { modifier = eir_holy_well_modifier years = 10 } }"),
               (40, "well_silent", "The sky stays grey, and the people grow restless.",
                [],
                "scope:eir_famine_county = { add_county_modifier = { modifier = eir_famine_modifier years = 3 } }")),
            trigger="piety >= 50", ai=20),
    ],
    theme="realm", cooldown=12,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nany_realm_county = { count >= 1 }",
    immediate="random_realm_county = { save_scope_as = eir_famine_county }"))

# -----------------------------------------------------------------------------
# 0054 Cattle Raiders at the Border
# -----------------------------------------------------------------------------
EVENTS.append(E(54, "Cattle Raiders at the Border",
    "Raiders from a neighbouring clan have driven off a herd from [eir_raid_county.GetName].",
    "It is the oldest crime in Ireland and the oldest sport. A hundred head of cattle were gone by morning, and the raiders' trail leads straight back to a neighbour's hall.\n\nHonour demands an answer, and Brehon law has a very precise price.",
    [
        Opt("Ride in pursuit and take the cattle back.",
            RL((55, "cattle_recovered", "You catch the raiders and bring the herd home.",
                [(15, "martial >= 12"), (10, "has_trait = brave")],
                "add_prestige = 100\nadd_character_modifier = { modifier = eir_cattle_rich_modifier years = 3 }"),
               (35, "cattle_lost", "The raiders vanish into the hills with the herd.",
                [],
                "scope:eir_raid_county = { add_county_modifier = { modifier = eir_cattle_raided_modifier years = 4 } }\nadd_prestige = -25")),
            trigger="martial >= 8",
            stress="craven = minor_stress_impact_gain", ai=40),
        Opt("Demand the éraic through the Brehon courts.",
            seq("add_prestige = 25", "add_gold = minor_gold_value"),
            trigger="learning >= 8", ai=30),
        Opt("Raid them back, and then some.",
            seq("add_gold = medium_gold_value", "add_character_modifier = { modifier = eir_raider_infamy_modifier years = 5 }"),
            stress="forgiving = minor_stress_impact_gain\nvengeful = miniscule_stress_impact_loss", ai=20),
        Opt("Let it go. A king has bigger concerns.",
            "scope:eir_raid_county = { add_county_modifier = { modifier = eir_cattle_raided_modifier years = 4 } }\nadd_prestige = -50",
            stress="wrathful = minor_stress_impact_gain", ai=10),
    ],
    theme="war", cooldown=10,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nany_realm_county = { count >= 1 }",
    immediate="random_realm_county = { save_scope_as = eir_raid_county }"))

# -----------------------------------------------------------------------------
# 0055 The Poet's Satire
# -----------------------------------------------------------------------------
EVENTS.append(E(55, "The Poet's Satire",
    "A poet you wronged has composed a satire, and it is spreading.",
    "The verses are devastating, vulgar and very good. In Ireland a satire can blister a king's face and wither his crops, and everyone knows that the greatest fear of any Irish lord is a poet with a grudge.\n\nThe poet is waiting to see what you do.",
    [
        Opt("Pay the poet a king's ransom to compose a second poem unsaying the first.",
            seq("remove_short_term_gold = medium_gold_value", "add_prestige = -25",
                "add_character_modifier = { modifier = eir_fili_patron_modifier years = 3 }"),
            stress="greedy = minor_stress_impact_gain", ai=40),
        Opt("Compose a poem of your own in reply.",
            RL((55, "reply_lands", "Your reply is so good the poet withdraws his satire.",
                [(20, "learning >= 12")],
                "add_prestige = 100\nadd_character_modifier = { modifier = eir_fili_patron_modifier years = 3 }"),
               (35, "reply_falls", "Your reply is worse than the satire.",
                [],
                "add_character_modifier = { modifier = eir_satirised_modifier years = 5 }")),
            trigger="learning >= 8", ai=20),
        Opt("Have the poet silenced.",
            seq("add_character_modifier = { modifier = eir_satirised_modifier years = 8 }",
                "add_dread = minor_dread_gain",
                "eir_court_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -12 }",
                "eir_trait_effect = { TRAIT = callous OPPOSITE = compassionate CHANCE = 20 }"),
            stress="compassionate = minor_stress_impact_gain\nwrathful = miniscule_stress_impact_loss", ai=10),
        Opt("Let the poem run its course and endure the mockery.",
            "add_character_modifier = { modifier = eir_satirised_modifier years = 4 }",
            stress="arrogant = minor_stress_impact_gain\nhumble = miniscule_stress_impact_loss", ai=20),
    ],
    theme="learning", cooldown=20, trigger=IRISH_PLAYER))

# -----------------------------------------------------------------------------
# 0056 A Foster-Brother Asks a Favour
# -----------------------------------------------------------------------------
EVENTS.append(E(56, "A Foster-Brother Asks a Favour",
    "Your foster-brother has ridden three days to ask you for something.",
    "You were raised in the same hall, slept in the same bed and shared the same bread. He has never asked you for anything until today, and the thing he asks is not small.\n\nIn Ireland, a foster-brother's request is nearly an order.",
    [
        Opt("Grant it without question.",
            seq("add_character_modifier = { modifier = eir_foster_ties_modifier years = 10 }",
                "add_prestige = 25", "remove_short_term_gold = minor_gold_value"),
            stress="honest = miniscule_stress_impact_loss", ai=50),
        Opt("Grant half of it and explain why.",
            "add_prestige = 10\nadd_character_modifier = { modifier = eir_foster_ties_modifier years = 4 }",
            ai=30),
        Opt("Refuse, and risk the bond.",
            seq("eir_trait_effect = { TRAIT = arrogant OPPOSITE = humble CHANCE = 20 }",
                "add_prestige = -25", "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -4 }"),
            stress="honest = minor_stress_impact_gain\nforgiving = miniscule_stress_impact_gain", ai=10),
    ],
    theme="family", cooldown=15,
    trigger="eir_is_irish_ruler_trigger = yes\nis_ai = no\nhas_global_variable = eir_done_fosterage"))
