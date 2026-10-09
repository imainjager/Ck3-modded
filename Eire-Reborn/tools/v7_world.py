"""v0.7 'long look' content pack: modifiers, nicknames, artifact modifiers used by ev_v7 and dec_v7.

Imported at the end of extra_world.py, which gen_world.py merges into its dictionaries.
"""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS

# ---------------------------------------------------------------- Re-Celticisation
K("eir_hedge_schools_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 8, "development_growth_factor": 0.04},
  "Hedge Schools", "Under hawthorn hedges, in the open air, children learn the old tongue from wandering masters.")
K("eir_cultural_resentment_modifier", "county_modifier_control_negative", {"county_opinion_add": -12, "monthly_county_control_growth_add": -0.3},
  "Cultural Resentment", "The people here watch their neighbours' language and customs change by royal decree, and they do not like it.")
K("eir_saxon_moot_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 10, "monthly_county_control_growth_add": 0.3},
  "A Moot of Their Own", "The thanes meet under their own oak by the king's leave, and are calmer for it.")
K("eir_rebel_march_modifier", "county_modifier_control_negative", {"county_opinion_add": -15, "tax_mult": -0.15, "levy_size": -0.1},
  "Burned Marches", "A revolt left the fields blackened and the beacons cold.")
C("eir_tongue_restorer_modifier", "prestige_positive", {"monthly_prestige": 0.3, "owned_legend_spread_mult": 0.15, "diplomacy": 1},
  "Restorer of the Tongue", "Poets in three countries sing that you gave the old speech back to its children.")
C("eir_two_peoples_modifier", "family_positive", {"vassal_opinion": 6, "general_opinion": 4, "monthly_prestige": 0.15},
  "Lord of Two Peoples", "Gael and Saxon alike say you were fair, and each is a little surprised to say it.")
C("eir_britain_restored_modifier", "prestige_positive", {"monthly_prestige": 0.6, "vassal_opinion": 5, "legitimacy_gain_mult": 0.15, "monthly_piety": 0.2},
  "The Britons Return", "The old island speaks again in the old languages, and you stood at the door when it did.")
C("eir_hard_hand_modifier", "dread_mixed", {"monthly_prestige": 0.1, "vassal_opinion": -5, "general_opinion": -4},
  "A Hard Hand", "You crushed the marches quickly. Nobody there will forget how.")

# ---------------------------------------------------------------- tanistry politics
C("eir_derbfine_counsel_modifier", "legitimacy_positive", {"legitimacy_gain_mult": 0.15, "vassal_opinion": 4},
  "Counsel of the Derbfine", "The adult men of the royal kindred sat down together and agreed, and the realm is steadier for it.")
C("eir_kin_distrust_modifier", "family_negative", {"vassal_opinion": -6, "stress_gain_mult": 0.1},
  "Distrust of Kin", "You now look at every cousin as a possible knife.")
C("eir_foster_bond_modifier", "family_positive", {"general_opinion": 5, "diplomacy": 1},
  "Foster-Brother's Bond", "A man raised in your hall at your table would walk into fire for you.")
C("eir_false_pedigree_modifier", "prestige_negative", {"monthly_prestige": -0.2, "general_opinion": -4},
  "Exposed Pedigree", "Everyone knows the genealogy was improved. Nobody says so to your face.")

# ---------------------------------------------------------------- sea and Norse
C("eir_norse_wife_modifier", "family_positive", {"general_opinion": 3, "levy_size": 0.04, "monthly_prestige": 0.1},
  "Norse Kin by Marriage", "A Norse-Gael bride tied two peoples together at the high table.")
K("eir_settlers_county_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.05, "tax_mult": 0.05, "county_opinion_add": -3},
  "Longship Settlers", "Norse families have begun farming here. The fields are better, and the neighbours are wary.")
C("eir_storm_survivor_modifier", "prestige_positive", {"monthly_prestige": 0.15, "stress_gain_mult": -0.1},
  "Survivor of the Storm", "You came back from the open sea alive, and the sailors drink to it.")

# ---------------------------------------------------------------- faith
C("eir_iona_relic_modifier", "piety_positive", {"monthly_piety": 0.4, "clergy_opinion": 6},
  "Relic of Iona", "A fragment of Colmcille's cloak rests in your chapel.")
K("eir_hospice_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.05, "county_opinion_add": 6},
  "Hospice of Brigid", "The nuns of Brigid tend the sick here, and the poor come from far away.")
C("eir_missionary_glory_modifier", "piety_positive", {"monthly_piety": 0.3, "monthly_prestige": 0.15},
  "Patron of the Pilgrims", "Your monks carried the faith to Alba and came back with stories.")
C("eir_easter_rift_modifier", "piety_negative" if False else "prestige_negative", {"clergy_opinion": -8, "monthly_piety": -0.15},
  "The Easter Rift", "You sided in the Easter quarrel, and half the monasteries now think you wrong.")
C("eir_heresy_hunter_modifier", "piety_positive", {"monthly_piety": 0.2, "clergy_opinion": 4, "general_opinion": -2},
  "Defender of the Rule", "You put down a heretical monk, and the bishops thank you in church.")

# ---------------------------------------------------------------- law, cattle, seasons
C("eir_fasting_justice_modifier", "legitimacy_positive", {"legitimacy_gain_mult": 0.1, "courtier_and_guest_opinion": 5},
  "Heeded the Fast", "You paid a debt rather than let a man starve at your door, and the law was glad.")
K("eir_murrain_modifier", "county_modifier_development_negative", {"tax_mult": -0.2, "development_growth_factor": -0.1},
  "Murrain in the Herds", "The cattle sicken, die and rot in the byre.")
K("eir_cattle_drive_modifier", "county_modifier_development_positive", {"tax_mult": 0.1, "levy_size": 0.05},
  "The Great Drive", "The herds went to market together and came back with silver.")
C("eir_booley_modifier", "family_positive", {"stress_gain_mult": -0.15, "health": 0.1, "monthly_prestige": 0.05},
  "Summer on the Hills", "You spent the season in the hill pastures, and it did you good.")
K("eir_booley_county_modifier", "county_modifier_development_positive", {"tax_mult": 0.06, "development_growth_factor": 0.02},
  "Booleying", "The herds follow the grass up the mountains each summer, and the dairies prosper.")

# ---------------------------------------------------------------- martial
C("eir_war_poem_modifier", "prowess_positive", {"knight_effectiveness_mult": 0.1, "monthly_prestige": 0.1},
  "War-Poem Sung", "The army marched to a poem, and it fought like one.")
C("eir_welsh_archers_modifier", "prowess_positive", {"archers_damage_add": 3, "monthly_prestige": 0.05},
  "Welsh Longbows", "Archers from the Welsh marches stand behind the shield wall.")
C("eir_ford_champion_modifier", "prowess_positive", {"prowess": 2, "monthly_prestige": 0.25},
  "Champion of the Ford", "You held a river crossing alone against a champion, and it is still being told.")
C("eir_gallowglass_lands_modifier", "dread_mixed", {"levy_size": 0.05, "vassal_opinion": -3},
  "Land for Gallowglass", "You settled hard Hebridean captains on good ground. They are loyal, and the neighbours are not happy.")

# ---------------------------------------------------------------- Celtic world
C("eir_mediator_of_wales_modifier", "prestige_positive", {"diplomacy": 1, "monthly_prestige": 0.2, "general_opinion": 3},
  "Mediator of the Welsh", "Two Welsh princes accepted your judgement.")
K("eir_tin_market_modifier", "county_modifier_development_positive", {"tax_mult": 0.1},
  "Cornish Tin Market", "Tin from Cornwall is traded here under your seal.")
K("eir_exile_quarter_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.04, "county_opinion_add": 3},
  "Breton Quarter", "Breton craftsmen and priests settled here and brought new customs.")
C("eir_pictish_stone_modifier", "learning_positive", {"learning": 1, "owned_legend_spread_mult": 0.1, "monthly_prestige": 0.1},
  "The Stone with Beasts", "A carved stone of the northern peoples stands in your court.")
C("eir_galloway_allies_modifier", "prestige_positive", {"monthly_prestige": 0.15, "levy_size": 0.04},
  "Friends of Galloway", "The Gaels of Galloway fight on your side.")
C("eir_college_of_bangor_modifier", "learning_positive", {"learning": 2, "diplomacy": 1, "monthly_prestige": 0.25},
  "Patron of the College of Bangor", "The monastery school at Bangor teaches half of Europe under your name.")
K("eir_college_county_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.08, "county_opinion_add": 5},
  "College of Bangor", "Students from three kingdoms crowd the town.")

# ---------------------------------------------------------------- court, house, legend
C("eir_child_prodigy_modifier", "learning_positive", {"monthly_prestige": 0.1, "owned_legend_spread_mult": 0.1},
  "Patron of a Prodigy", "A child of astonishing talent grows up in your hall.")
C("eir_isles_wedding_modifier", "family_positive", {"monthly_prestige": 0.2, "levy_size": 0.04, "general_opinion": 3},
  "Wedding of the Isles", "Half the Hebrides came to the feast, and drank to your health for a week.")
C("eir_hounds_ghost_modifier", "prowess_positive", {"prowess": 1, "stress_gain_mult": -0.1, "monthly_prestige": 0.1},
  "Touched by the Hound's Ghost", "At Samhain you saw the Hound of Ulster, and he nodded.")
C("eir_omen_comet_modifier", "prestige_negative", {"stress_gain_mult": 0.15, "general_opinion": -2},
  "Under the Comet", "A bright star with a tail crossed the sky, and nobody can agree what it meant.")
C("eir_harpers_curse_modifier", "prestige_negative", {"monthly_prestige": -0.3, "general_opinion": -4},
  "The Harper's Curse", "A wronged harper cursed you in your own hall, and the court is uneasy.")
C("eir_bardic_house_modifier", "learning_positive", {"monthly_dynasty_prestige": 0.08, "owned_legend_spread_mult": 0.1},
  "A Bardic House", "Your house keeps its own poets, harpers and genealogists.")
C("eir_port_charter_modifier", "economy_positive", {"monthly_income": 1.5, "diplomacy": 1},
  "Chartered Harbour", "A new market-town on the shore pays dues to your treasury.")
K("eir_chartered_town_modifier", "county_modifier_development_positive", {"tax_mult": 0.1, "development_growth_factor": 0.05},
  "Chartered Port", "A grant of liberties made a market out of a fishing village.")
C("eir_tain_retold_modifier", "learning_positive" if False else "prestige_positive", {"owned_legend_spread_mult": 0.25, "monthly_prestige": 0.2, "prowess": 1},
  "The Táin Retold", "Your poets told the Cattle-Raid of Cooley in a new version, and it spread across the Irish Sea.")

# ---------------------------------------------------------------- artifacts
ARTIFACT["eir_iona_reliquary_modifier"] = ("piety_positive", {"monthly_piety": 0.35, "clergy_opinion": 5, "stress_gain_mult": -0.05},
    "Reliquary of Iona", "A bronze and silver shrine with a scrap of Colmcille's cloak.")
ARTIFACT["eir_poets_chain_modifier"] = ("prestige_positive", {"monthly_prestige": 0.2, "diplomacy": 1, "owned_legend_spread_mult": 0.1},
    "The Poet's Chain", "A silver chain given by a high poet to a king he thought worthy.")
ARTIFACT["eir_moot_horn_modifier"] = ("prestige_positive", {"vassal_opinion": 3, "monthly_prestige": 0.15},
    "The Moot Horn", "A carved horn blown to call the thanes to their open-air assembly.")

# ---------------------------------------------------------------- opinions
OPINIONS["eir_saxon_grievance_opinion"] = "Resents the loss of old customs"
OPINIONS["eir_two_peoples_opinion"] = "Treated both peoples fairly"
OPINIONS["eir_poet_gift_opinion"] = "Rewarded a poet generously"
OPINIONS["eir_rescued_opinion"] = "Was rescued from captivity"
OPINIONS["eir_cousin_blinded_opinion"] = "Blinded a kinsman"
