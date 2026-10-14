"""Update 7 (v0.13): fifteen Celtic tenets, personal AND faith level, locked until the Britannia / Return of the Celts decisions are taken.
Each entry: key -> dict(name, desc, icon, cost, unlock (the decision that unlocks it), fmod (faith character modifier), cmod (faith county modifier),
pmod (personal tenet modifier), fparams / pflags [(flag, text)], virtues / sins [(trait, weight, scale)],
inv = the decision that uses the tenet: name, desc, tip, cost (gold, prestige, piety), cd (years), boon (character modifier fields), years, extra effect lines)."""

ORDER = ["oak_rite", "wood_warden", "high_circuit", "brehon_peace", "gael_voice", "gaul_vow", "pilgrim_relic", "brennus",
         "galatian", "salt_hearth", "rage", "fianna", "grail", "geis", "heavy_crown"]

T = {}

T["oak_rite"] = dict(
    name="The Oak and the Rite", icon="tenet_mystical_birthright", cost="mid", unlock="eir_mystic_celts_decision",
    desc="Rulers keep the old groves, the quarter-day fires and the oaths sworn beneath the oak. The bishops tolerate it because the harvest is good.",
    fmod={"monthly_piety": 0.1, "lifestyle_mystic_xp_gain_mult": 0.25, "fertility": 0.05},
    cmod={"county_opinion_add": 2},
    pmod={"monthly_piety": 0.3, "lifestyle_mystic_xp_gain_mult": 0.5, "stress_gain_mult": -0.1},
    fparams=[("eir_tn_oak_rite", "Rulers of this faith can use the Sit Beneath the Oak decision")],
    pflags=[("eir_tn_oak_rite_p", "Can use the Sit Beneath the Oak decision")],
    virtues=[("lifestyle_mystic", 15, 2), ("zealous", 10, 1)], sins=[("cynical", 10, 1)],
    inv=dict(name="Sit Beneath the Oak", cost=(0, 0, 150), cd=10, years=8, boon={"monthly_piety": 0.4, "stress_gain_mult": -0.15, "monthly_prestige": 0.2},
             bname="Under the Oak", bdesc="You sat a night beneath the oak and the old rites came back to you. The court is a little afraid of how calm you are.",
             desc="Spend a night alone beneath the oldest oak in your lands, as the druids did, and let the old rites tell you what the monks never would.",
             tip="Costs 150 piety. Grants a Mystic trait experience boost and the Under the Oak modifier for 8 years (+piety, -stress), and a vision event whose last option can go badly.",
             extra="add_trait_xp = { trait = lifestyle_mystic value = 100 }"))

T["wood_warden"] = dict(
    name="Warden of the Wood", icon="tenet_natural_primitivism", cost="mid", unlock="eir_return_germany_decision",
    desc="The forest is a temple and its guardians are warriors. Foes who enter it do so by leave of the wardens, who are not generous.",
    fmod={"forest_advantage": 3, "hills_advantage": 2, "monthly_prestige": 0.05},
    cmod={"forest_development_growth_factor": 0.2, "county_opinion_add": 2},
    pmod={"forest_advantage": 8, "knight_effectiveness_mult": 0.1, "hills_advantage": 4},
    fparams=[("eir_tn_wood_warden", "Rulers of this faith can use the Call the Hunt decision")],
    pflags=[("eir_tn_wood_warden_p", "Can use the Call the Hunt decision")],
    virtues=[("brave", 15, 1), ("lifestyle_hunter", 10, 1)], sins=[("craven", 15, 1)],
    inv=dict(name="Call the Hunt", cost=(150, 0, 0), cd=8, years=6, boon={"forest_advantage": 6, "advantage": 3, "levy_size": 0.1},
             bname="The Hunt Is Called", bdesc="The wardens have gathered in the forest and no army will cross it unchallenged.",
             desc="Send the horn through every wood on your land. The wardens will gather, and for a season no foe will cross a forest without leaving a body in it.",
             tip="Costs 150 gold. Raises a levy of wardens and gives +advantage and +forest advantage for 6 years.",
             extra="eir_defender_levy_effect = yes"))

T["high_circuit"] = dict(
    name="The High King's Circuit", icon="tenet_pursuit_of_power", cost="high", unlock="eir_final_revenge_decision",
    desc="A king who is not seen is not king. The ruler rides the circuit of the realm, eats at every hall and hears every complaint, and is believed.",
    fmod={"vassal_opinion": 3, "monthly_prestige": 0.1},
    cmod={"county_opinion_add": 3},
    pmod={"vassal_opinion": 6, "legitimacy_gain_mult": 0.15, "monthly_prestige": 0.3},
    fparams=[("eir_tn_high_circuit", "Rulers of this faith can use the Ride the Circuit decision")],
    pflags=[("eir_tn_high_circuit_p", "Can use the Ride the Circuit decision")],
    virtues=[("just", 15, 1), ("gregarious", 10, 1)], sins=[("shy", 15, 1)],
    inv=dict(name="Ride the Circuit", cost=(300, 0, 0), cd=8, years=8, boon={"vassal_opinion": 8, "monthly_prestige": 0.3, "legitimacy_gain_mult": 0.15},
             bname="The Circuit Ridden", bdesc="You have been seen in every hall of the realm, and no one can say they were not heard.",
             desc="Ride the circuit of your realm from hall to hall, from the coast to the mountains, as the old kings did.",
             tip="Costs 300 gold. Raises vassal opinion and gives the Circuit Ridden modifier for 8 years. One stop on the road goes badly.",
             extra="eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }"))

T["brehon_peace"] = dict(
    name="Brehon's Peace", icon="tenet_legalism", cost="mid", unlock="eir_unite_gaelic_kingdoms_decision",
    desc="The quarrel is settled by the judge and not by the sword. A death costs a price in cattle, and a refuge cannot be violated.",
    fmod={"clergy_opinion": 5, "general_opinion": 2, "stress_gain_mult": -0.03},
    cmod={"county_opinion_add": 3, "tax_mult": 0.03},
    pmod={"stress_gain_mult": -0.1, "vassal_opinion": 4, "legitimacy_gain_mult": 0.1},
    fparams=[("eir_tn_brehon_peace", "Rulers of this faith can use the Pronounce a Judgement decision")],
    pflags=[("eir_tn_brehon_peace_p", "Can use the Pronounce a Judgement decision")],
    virtues=[("just", 15, 1), ("patient", 10, 1)], sins=[("arbitrary", 15, 1)],
    inv=dict(name="Pronounce a Judgement", cost=(0, 200, 0), cd=6, years=6, boon={"vassal_opinion": 6, "general_opinion": 4, "stress_gain_mult": -0.1},
             bname="The Judgement Stands", bdesc="You judged a quarrel that had run for three generations. Neither side liked it. Both obeyed.",
             desc="Sit in judgement on the oldest feud in your realm. The price will be set in cattle and silver, and nobody will leave the hall with all they came for.",
             tip="Costs 200 prestige. Settles feuds with a price and gives the Judgement Stands modifier for 6 years.",
             extra="add_character_modifier = { modifier = eir_wergild_peace_modifier years = 6 }"))

T["gael_voice"] = dict(
    name="Voice of the Gael", icon="tenet_ritual_hospitality", cost="mid", unlock="eir_celts_mainland_decision",
    desc="The language is the nation. Poets, harpers and hospitality carry it from hall to hall, and no stranger leaves without learning a verse.",
    fmod={"owned_legend_spread_mult": 0.2, "courtier_opinion": 5},
    cmod={"county_opinion_add": 2},
    pmod={"diplomacy": 2, "monthly_prestige": 0.3, "owned_legend_spread_mult": 0.3},
    fparams=[("eir_tn_gael_voice", "Rulers of this faith can use the Send Out the Poets decision")],
    pflags=[("eir_tn_gael_voice_p", "Can use the Send Out the Poets decision")],
    virtues=[("gregarious", 15, 1), ("generous", 10, 1)], sins=[("shy", 10, 1)],
    inv=dict(name="Send Out the Poets", cost=(250, 0, 0), cd=10, years=10, boon={"owned_legend_spread_mult": 0.3, "monthly_prestige": 0.3, "courtier_opinion": 5},
             bname="Poets Abroad", bdesc="Your poets are in every hall from the Hebrides to the Rhine, and they all sing the same verse.",
             desc="Send the poets out with a new verse in your praise and an old one that reminds the listener who he is descended from.",
             tip="Costs 250 gold. Spreads your legend and gives the Poets Abroad modifier for 10 years.",
             extra="add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 10 }"))

T["gaul_vow"] = dict(
    name="Vow of Vercingetorix", icon="tenet_armed_pilgrimages", cost="high", unlock="eir_return_france_decision",
    desc="Every free man swears on the hill that he will not yield the land. The oath is old, hard to keep and harder to break.",
    fmod={"defender_advantage": 3, "knight_effectiveness_mult": 0.05},
    cmod={"levy_size": 0.05},
    pmod={"defender_advantage": 6, "knight_effectiveness_mult": 0.1, "levy_size": 0.1},
    fparams=[("eir_tn_gaul_vow", "Rulers of this faith can use the Swear the Vow on the Hill decision")],
    pflags=[("eir_tn_gaul_vow_p", "Can use the Swear the Vow on the Hill decision")],
    virtues=[("brave", 15, 1), ("stubborn", 10, 1)], sins=[("craven", 15, 1)],
    inv=dict(name="Swear the Vow on the Hill", cost=(200, 0, 100), cd=12, years=6, boon={"defender_advantage": 8, "levy_size": 0.15, "advantage": 3},
             bname="The Vow Is Sworn", bdesc="Every free man in your lands has sworn on the hill. They will not yield, and they will not forgive those who do.",
             desc="Call every free man to the hill and let him swear that he will not yield the land to the foreigner while he can lift a spear.",
             tip="Costs 200 gold and 100 piety. Raises a host of oath-sworn men and gives the Vow Is Sworn modifier for 6 years.",
             extra="eir_defender_levy_effect = yes"))

T["pilgrim_relic"] = dict(
    name="Pilgrim and Relic", icon="tenet_pilgrimage_encouraged", cost="mid", unlock="eir_path_brooch_decision",
    desc="The road to the saint is a sacrament. Monks cross the sea to carry the faith, and the relics they bring home make the home they came from holier.",
    fmod={"monthly_piety": 0.1, "clergy_opinion": 3},
    cmod={"county_opinion_add": 2},
    pmod={"monthly_piety": 0.3, "monthly_prestige": 0.1, "general_opinion": 3},
    fparams=[("eir_tn_pilgrim_relic", "Rulers of this faith can use the Send a Monk Overseas decision")],
    pflags=[("eir_tn_pilgrim_relic_p", "Can use the Send a Monk Overseas decision")],
    virtues=[("zealous", 15, 1), ("humble", 10, 1)], sins=[("arrogant", 10, 1)],
    inv=dict(name="Send a Monk Overseas", cost=(150, 0, 100), cd=8, years=8, boon={"monthly_piety": 0.4, "clergy_opinion": 5, "monthly_prestige": 0.1},
             bname="The Monk's Return", bdesc="A monk has crossed the sea and come home with a relic and a story. You have the relic. The story has several versions.",
             desc="Fit out a currach and send a monk overseas with a fortnight's food and a Gospel book, and let him carry the faith where the winds take him.",
             tip="Costs 150 gold and 100 piety. After a voyage the monk returns with a gift, or does not.",
             extra="add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }"))

T["brennus"] = dict(
    name="Brennus' Reckoning", icon="tenet_cranial_trophies", cost="high", unlock="eir_return_italy_decision",
    desc="Rome was sacked once by Celts, and it paid in gold. Every city is a purse, every siege an invoice, and the rulers believe that nobody who can pay should be spared.",
    fmod={"dread_gain_mult": 0.1, "advantage": 2},
    cmod={"levy_size": 0.05},
    pmod={"dread_gain_mult": 0.25, "monthly_prestige": 0.2, "advantage": 3},
    fparams=[("eir_tn_brennus", "Rulers of this faith can use the Name the Ransom decision")],
    pflags=[("eir_tn_brennus_p", "Can use the Name the Ransom decision")],
    virtues=[("ambitious", 15, 1), ("wrathful", 10, 1)], sins=[("compassionate", 15, 1)],
    inv=dict(name="Name the Ransom", cost=(0, 0, 150), cd=10, years=8, boon={"dread_gain_mult": 0.3, "monthly_prestige": 0.2, "general_opinion": -4},
             bname="Woe to the Vanquished", bdesc="You have named a ransom that no one in the city could pay without selling the roof. They paid it.",
             desc="Name a price for a city that has just surrendered, and weigh it against your sword, in the manner of Brennus on the Capitol.",
             tip="Costs 150 piety. Gives a heavy purse of gold and the Woe to the Vanquished modifier for 8 years (+dread, -opinion).",
             extra="add_gold = major_gold_value"))

T["galatian"] = dict(
    name="Galatian Syncretism", icon="tenet_esotericism", cost="mid", unlock="eir_return_galatia_decision",
    desc="The Galatians kept the old gods in the shadow of the new faith for four hundred years, and the saints wear their faces. The clergy find it useful.",
    fmod={"learning": 1, "clergy_opinion": 3},
    cmod={"county_opinion_add": 2},
    pmod={"learning": 2, "monthly_piety": 0.2, "general_opinion": 3},
    fparams=[("eir_tn_galatian", "Rulers of this faith can use the Write to the Galatians decision")],
    pflags=[("eir_tn_galatian_p", "Can use the Write to the Galatians decision")],
    virtues=[("diligent", 10, 1), ("humble", 10, 1)], sins=[("stubborn", 10, 1)],
    inv=dict(name="Write to the Galatians", cost=(100, 0, 100), cd=10, years=10, boon={"learning": 2, "monthly_piety": 0.3, "general_opinion": 3},
             bname="Letters to the Galatians", bdesc="You wrote to the far-off cousins in a language they half remember, and they wrote back.",
             desc="Write a letter in the style of the Apostle, to the Galatians, reminding them who their grandfathers were and what they once believed.",
             tip="Costs 100 gold and 100 piety. Gives the Letters to the Galatians modifier for 10 years.",
             extra="add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 10 }"))

T["salt_hearth"] = dict(
    name="Salt, Silver and Hearth", icon="tenet_ritual_celebrations", cost="mid", unlock="eir_third_of_britannia_decision",
    desc="The wealth of the island is salt from the shore, silver from the hills and a fire that never goes out in the mead-hall. A ruler who keeps all three is rich.",
    fmod={"monthly_income": 0.5, "general_opinion": 1},
    cmod={"development_growth_factor": 0.1, "tax_mult": 0.05},
    pmod={"monthly_income": 1.5, "domain_tax_mult": 0.05, "courtier_opinion": 3},
    fparams=[("eir_tn_salt_hearth", "Rulers of this faith can use the Open the Salt Roads decision")],
    pflags=[("eir_tn_salt_hearth_p", "Can use the Open the Salt Roads decision")],
    virtues=[("greedy", 10, 1), ("diligent", 15, 1)], sins=[("lazy", 15, 1)],
    inv=dict(name="Open the Salt Roads", cost=(100, 0, 0), cd=10, years=10, boon={"monthly_income": 2, "domain_tax_mult": 0.05, "courtier_opinion": 3},
             bname="Salt Roads Open", bdesc="The salt roads are open, the silver is moving and the hearths are lit. For ten years the treasury will be happy.",
             desc="Open the old trade roads from the coast to the hills, and put a toll-house at every ford.",
             tip="Costs 100 gold. Pays a lump of gold, adds a modifier to your capital county and gives the Salt Roads Open modifier for 10 years.",
             extra="add_gold = major_gold_value\ncapital_county ?= { add_county_modifier = { modifier = eir_island_pride_modifier years = 10 } }"))

T["rage"] = dict(
    name="Hero's Fury", icon="tenet_miles_christi", cost="high", unlock="eir_path_armor_decision",
    desc="At the height of battle a hero turns into something else. The ruler's warriors believe it and fight as if they have seen it.",
    fmod={"prowess": 1, "knight_effectiveness_mult": 0.05},
    cmod={"levy_size": 0.05},
    pmod={"prowess": 3, "health": 0.1, "knight_effectiveness_mult": 0.1},
    fparams=[("eir_tn_rage", "Rulers of this faith can use the Take the Hero's Portion decision")],
    pflags=[("eir_tn_rage_p", "Can use the Take the Hero's Portion decision")],
    virtues=[("brave", 15, 2), ("wrathful", 10, 1)], sins=[("craven", 15, 1), ("calm", 10, 1)],
    inv=dict(name="Take the Hero's Portion", cost=(100, 0, 0), cd=10, years=6, boon={"prowess": 5, "knight_effectiveness_mult": 0.15, "advantage": 3, "stress_gain_mult": 0.1},
             bname="The Hero's Portion", bdesc="You took the champion's portion and the court has not stopped watching you since. You are, briefly, a hero.",
             desc="Take the best cut at the feast, as the hero does in the old tales, and let anyone who dares dispute it.",
             tip="Costs 100 gold. Gives the Hero's Portion modifier for 6 years (+prowess, +knight effectiveness, +stress). The feast can end in a fight.",
             extra="add_trait_xp = { trait = lifestyle_blademaster value = 60 }"))

T["fianna"] = dict(
    name="The Fianna Camp", icon="tenet_mountain_worship", cost="mid", unlock="eir_path_spear_decision",
    desc="The young nobles live a winter in the forest, hunting, fasting and fighting. They return trained, and they remember who fed them.",
    fmod={"men_at_arms_maintenance": -0.05, "levy_size": 0.03},
    cmod={"levy_size": 0.05},
    pmod={"men_at_arms_maintenance": -0.1, "knight_effectiveness_mult": 0.05, "monthly_prestige": 0.1},
    fparams=[("eir_tn_fianna", "Rulers of this faith can use the Raise the Fianna Camp decision")],
    pflags=[("eir_tn_fianna_p", "Can use the Raise the Fianna Camp decision")],
    virtues=[("brave", 10, 1), ("lifestyle_hunter", 15, 1)], sins=[("lazy", 10, 1)],
    inv=dict(name="Raise the Fianna Camp", cost=(200, 0, 0), cd=10, years=8, boon={"men_at_arms_maintenance": -0.15, "knight_effectiveness_mult": 0.1, "levy_size": 0.1},
             bname="The Fianna Camp", bdesc="A winter camp of young nobles has been trained in the forest. They are loyal, hungry and a little wild.",
             desc="Gather the sons of your vassals in a forest camp for a winter, to hunt, to fast and to fight, as the Fianna did in the old tales.",
             tip="Costs 200 gold. Raises a band of young warriors and gives the Fianna Camp modifier for 8 years.",
             extra="eir_defender_levy_effect = yes"))

T["grail"] = dict(
    name="The Grail Quest", icon="tenet_pursuit_of_knowledge", cost="high", unlock="eir_revive_arthur_decision",
    desc="Somewhere in the island is a vessel that heals the land. A ruler who sets out to find it is rarely rewarded, but never forgotten.",
    fmod={"learning": 1, "monthly_prestige": 0.1},
    cmod={"county_opinion_add": 2},
    pmod={"learning": 2, "monthly_piety": 0.3, "monthly_prestige": 0.3, "stress_gain_mult": -0.05},
    fparams=[("eir_tn_grail", "Rulers of this faith can use the Set Out on the Quest decision")],
    pflags=[("eir_tn_grail_p", "Can use the Set Out on the Quest decision")],
    virtues=[("zealous", 10, 1), ("brave", 10, 1)], sins=[("content", 15, 1)],
    inv=dict(name="Set Out on the Quest", cost=(300, 0, 200), cd=20, years=10, boon={"monthly_piety": 0.5, "monthly_prestige": 0.5, "learning": 2},
             bname="The Quest Begun", bdesc="You rode out in search of the vessel. Whatever you found, you are not the person who left.",
             desc="Ride out in search of the vessel that heals the land. Take few knights and no maps, and let the road decide who you are.",
             tip="Costs 300 gold and 200 piety. A long quest ends in a vessel, or in a long ride home.",
             extra="add_trait_xp = { trait = lifestyle_mystic value = 50 }"))

T["geis"] = dict(
    name="Geis and Omens", icon="tenet_astrology", cost="mid", unlock="eir_path_table_decision",
    desc="Every great ruler lives under a geis, a taboo that gives strength and carries a price. Omens warn of the day it will be broken.",
    fmod={"stress_gain_mult": -0.03, "monthly_prestige": 0.05},
    cmod={"county_opinion_add": 1},
    pmod={"monthly_prestige": 0.3, "stress_gain_mult": -0.05, "advantage": 2},
    fparams=[("eir_tn_geis", "Rulers of this faith can use the Take a Geis decision")],
    pflags=[("eir_tn_geis_p", "Can use the Take a Geis decision")],
    virtues=[("stubborn", 15, 1), ("honest", 10, 1)], sins=[("fickle", 15, 1)],
    inv=dict(name="Take a Geis", cost=(0, 150, 0), cd=12, years=12, boon={"monthly_prestige": 0.5, "advantage": 3, "stress_gain_mult": -0.1},
             bname="Bound by a Geis", bdesc="You have sworn a taboo, and it gives you strength. Your steward keeps a list of the ways it can be broken.",
             desc="Take a taboo on yourself, as the heroes did: never to refuse a guest, never to cross a certain river, never to eat a certain meat. It will make you stronger, and it will hurt.",
             tip="Costs 150 prestige. Gives the Bound by a Geis modifier for 12 years. A broken geis becomes a curse that fades after 8 years.",
             extra="add_character_modifier = { modifier = eir_foreknowledge_modifier years = 6 }"))

T["heavy_crown"] = dict(
    name="The Heavy Crown", icon="tenet_hedonistic", cost="massive", unlock="eir_path_crown_decision",
    desc="The crown that is worn is the crown that is feared, and the one who wears it is never again at ease. Prestige is great and the heirs resent it.",
    fmod={"legitimacy_gain_mult": 0.15, "vassal_opinion": -2},
    cmod={"county_opinion_add": 1},
    pmod={"monthly_prestige": 0.6, "legitimacy_gain_mult": 0.3, "vassal_opinion": -4, "dynasty_opinion": -10},
    fparams=[("eir_tn_heavy_crown", "Rulers of this faith can use the Wear the Heavy Crown decision")],
    pflags=[("eir_tn_heavy_crown_p", "Can use the Wear the Heavy Crown decision")],
    virtues=[("ambitious", 20, 2), ("arrogant", 10, 1)], sins=[("humble", 15, 1), ("content", 15, 1)],
    inv=dict(name="Wear the Heavy Crown", cost=(0, 0, 200), cd=15, years=15, boon={"monthly_prestige": 1.0, "legitimacy_gain_mult": 0.3, "vassal_opinion": -8, "stress_gain_mult": 0.15},
             bname="The Heavy Crown", bdesc="You wear the crown in public every day. The court admires it. The court's children have begun to hate it.",
             desc="Wear the crown at every hall, in every season and every weather. The whole realm will know exactly who rules it.",
             tip="Costs 200 piety. Gives a surge of prestige and legitimacy, and the Heavy Crown modifier for 15 years (+prestige, +legitimacy, -vassal opinion, +stress).",
             extra="add_legitimacy = major_legitimacy_gain\nadd_prestige = massive_prestige_gain"))
