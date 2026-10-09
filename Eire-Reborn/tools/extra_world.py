"""Extra modifiers, traits, opinion modifiers and men-at-arms for the v0.3 content pack.

gen_world.py merges these dicts into its own before building.
"""

CHAR = {}
COUNTY = {}
PROVINCE = {}
ARTIFACT = {}
TRAITS = {}
OPINIONS = {}
MAA = {}


def C(name, icon, fields, disp, desc):
    CHAR[name] = (icon, fields, disp, desc)


def K(name, icon, fields, disp, desc):
    COUNTY[name] = (icon, fields, disp, desc)


# ---------------------------------------------------------------- statecraft
C("eir_royal_circuit_modifier", "prestige_positive", {"monthly_prestige": 0.25, "vassal_opinion": 5},
  "Royal Circuit", "You have ridden through your lands, eaten at every lord's table, and been seen.")
C("eir_hostages_modifier", "dread_mixed", {"monthly_prestige": 0.2, "vassal_opinion": -6},
  "Hostages of Tara", "The sons of your vassals sit at your table. They keep your vassals quiet, and bitter.")
C("eir_cain_law_modifier", "piety_positive", {"clergy_opinion": 10, "monthly_piety": 0.3},
  "Cain Law", "A law of sanctuary and protection, sworn by the bishops and the kings.")
C("eir_provincial_oath_modifier", "legitimacy_positive", {"vassal_opinion": 4, "legitimacy_gain_mult": 0.1},
  "Sworn Provincial Kings", "The provincial kings have sworn on the relics, and the oath still holds.")
C("eir_feis_modifier", "prestige_positive", {"monthly_prestige": 0.4, "courtier_opinion": 5},
  "Feis of Tara", "The great feast is remembered in song.")
C("eir_tanaiste_modifier", "legitimacy_positive", {"vassal_opinion": 4, "legitimacy_gain_mult": 0.1},
  "Named Tánaiste", "An heir-apparent has been named, and the succession is a little clearer than usual.")
C("eir_cain_tribute_modifier", "economy_mixed", {"monthly_income": 2, "vassal_opinion": -5},
  "The Cáin Tribute", "The levy is collected. The cattle-owners are not pleased.")
C("eir_wergild_peace_modifier", "family_positive", {"stress_gain_mult": -0.1, "general_opinion": 3},
  "Wergild Paid", "A feud was settled with cattle instead of blood.")
C("eir_gaelic_court_modifier", "prestige_positive", {"monthly_prestige": 0.2, "courtier_opinion": 5},
  "A Court in the Old Style", "Harpers, poets and judges fill your hall.")
C("eir_royal_ollamh_modifier", "learning_positive", {"monthly_prestige": 0.3, "learning": 1},
  "Ollamh of the King", "A chief poet sits at your right hand and remembers everything.")
C("eir_hosting_modifier", "dread_mixed", {"levy_size": 0.1, "monthly_prestige": 0.1},
  "A Great Hosting", "The tribes are gathered, and every man knows his place.")
C("eir_sanctuary_modifier", "piety_positive", {"clergy_opinion": 5, "monthly_piety": 0.2},
  "Right of Sanctuary", "Churches shelter those who flee, and the clergy bless you for it.")
C("eir_tanistry_dispute_modifier", "prestige_negative", {"vassal_opinion": -6, "monthly_prestige": -0.1},
  "A Claim Revoked", "You struck a name from the list of heirs, and the family has not forgotten.")

# ---------------------------------------------------------------- culture
C("eir_naming_customs_modifier", "family_positive", {"general_opinion": 3, "monthly_dynasty_prestige": 0.05},
  "Gaelic Names", "Your children are named for saints and heroes, as the ancestors were.")
C("eir_bardic_circuit_modifier", "learning_positive", {"monthly_prestige": 0.2, "owned_legend_spread_mult": 0.1},
  "Bardic Circuit", "Poets walk from hall to hall, carrying your name.")
C("eir_harper_modifier", "learning_positive", {"diplomacy": 1, "courtier_opinion": 3},
  "A Harper at Court", "A master harper plays in your hall every evening.")
C("eir_brigid_cult_modifier", "piety_positive", {"health": 0.1, "fertility": 0.1},
  "Flame of Brigid", "A perpetual flame burns for Brigid, goddess and saint.")
C("eir_colmcille_cult_modifier", "learning_positive", {"learning": 1, "monthly_piety": 0.2},
  "Heir of Colmcille", "The saint of Iona is honoured in your court.")
C("eir_patrick_cult_modifier", "piety_positive", {"monthly_piety": 0.3, "clergy_opinion": 4},
  "Patrick's Faithful", "The apostle of Ireland is honoured above every other saint.")
C("eir_yew_bows_modifier", "dread_positive" if False else "prowess_positive", {"archers_damage_add": 2},
  "Yew Bows", "Your levies carry bows of Irish yew.")
C("eir_champions_portion_modifier", "prowess_positive", {"prowess": 2, "monthly_prestige": 0.1},
  "Champion's Portion", "The best cut of the meat goes to your champion, and his arm is the stronger for it.")
C("eir_dun_drill_modifier", "prowess_positive", {"martial": 1, "knight_effectiveness_mult": 0.1},
  "Dún Drill", "The garrison trains behind the earthen walls every spring.")
C("eir_watchtowers_modifier", "dread_mixed", {"fort_level": 0, "monthly_prestige": 0.05} if False else {"monthly_prestige": 0.05},
  "Coastal Watch", "Watchmen stand on every headland.")
C("eir_island_fleet_modifier", "economy_positive", {"monthly_income": 1, "monthly_prestige": 0.1},
  "Fleet of the Isles", "Your galleys sail the western seas.")

# ---------------------------------------------------------------- faith
C("eir_monastery_founder_modifier", "piety_positive", {"monthly_piety": 0.3, "clergy_opinion": 3},
  "Founder of a Monastery", "You have given the Church a new house of prayer.")
C("eir_scriptorium_patron_modifier", "learning_positive", {"learning": 1, "monthly_prestige": 0.1},
  "Patron of the Scriptorium", "Your monks copy gospel books by candlelight.")
C("eir_hermit_blessing_modifier", "piety_positive", {"stress_gain_mult": -0.1, "monthly_piety": 0.2},
  "A Hermit's Blessing", "A holy man gave you his blessing, and a silence.")
C("eir_relic_procession_modifier", "piety_positive", {"clergy_opinion": 5, "monthly_piety": 0.2},
  "Relic Procession", "A relic was carried through your lands, and the people were comforted.")
C("eir_penance_done_modifier", "piety_positive", {"stress_gain_mult": -0.15, "monthly_piety": 0.1},
  "Penance Done", "You stood barefoot in the snow. You feel lighter.")
C("eir_rome_pilgrim_modifier", "piety_positive", {"monthly_piety": 0.4, "monthly_prestige": 0.1},
  "Pilgrim to Rome", "You walked to Rome and back.")

# ---------------------------------------------------------------- Celtic
C("eir_gwynedd_alliance_modifier", "diplomacy_positive" if False else "prestige_positive", {"diplomacy": 1, "monthly_prestige": 0.15},
  "Friend of Gwynedd", "The princes of Gwynedd count you a friend.")
C("eir_strathclyde_bond_modifier", "prestige_positive", {"monthly_prestige": 0.15, "general_opinion": 2},
  "Brother of Strathclyde", "The northern Britons call you kin.")
C("eir_pictish_memory_modifier", "prestige_positive", {"monthly_prestige": 0.15, "owned_legend_spread_mult": 0.05},
  "Pictish Memory", "You honour the old peoples of the north.")
C("eir_breton_refuge_modifier", "prestige_positive", {"monthly_prestige": 0.2, "general_opinion": 3},
  "Refuge of Brittany", "Breton exiles bless your name.")
C("eir_armorica_voyage_modifier", "prestige_positive", {"monthly_prestige": 0.2},
  "Voyage to Armorica", "A ship returned from Brittany, with news and silver.")
C("eir_gaulish_heritage_modifier", "prestige_positive", {"monthly_prestige": 0.15, "diplomacy": 1},
  "Gaulish Heritage", "The Celts once ruled from the Danube to the Atlantic.")
# ---------------------------------------------------------------- tales & misc
C("eir_tale_salmon_modifier", "learning_positive", {"learning": 2},
  "Tale of the Salmon of Knowledge", "Your court tells the story of the salmon, and learns from it.")
C("eir_tale_cuchulainn_modifier", "prowess_positive", {"prowess": 2},
  "Tale of Cú Chulainn", "Your warriors want to be the Hound of Ulster.")
C("eir_tale_finn_modifier", "prowess_positive", {"prowess": 1, "monthly_prestige": 0.15},
  "Tale of Finn and the Fianna", "The hunter-warriors of the old stories inspire your knights.")
C("eir_tale_medb_modifier", "prestige_positive", {"intrigue": 1, "monthly_prestige": 0.15},
  "Tale of Queen Medb", "A formidable queen of the old tales is on everyone's mind.")
C("eir_tale_lir_modifier", "family_positive", {"general_opinion": 3, "stress_gain_mult": -0.05},
  "Tale of the Children of Lir", "A song of grief that makes people kinder.")
C("eir_tale_brendan_modifier", "piety_positive", {"monthly_piety": 0.3, "monthly_prestige": 0.1},
  "Tale of Saint Brendan", "A voyage story that makes the western sea seem close.")
C("eir_harp_of_brian_modifier", "prestige_positive", {"monthly_prestige": 0.3, "diplomacy": 1},
  "Harp of the High King", "A harp said to have belonged to Brian himself.")
C("eir_crozier_modifier", "piety_positive", {"monthly_piety": 0.3, "clergy_opinion": 4},
  "Crozier of the Abbot", "A bishop's staff of bronze and enamel.")
C("eir_kingmaker_modifier", "prestige_positive", {"vassal_opinion": 5, "monthly_prestige": 0.2},
  "Kingmaker", "You placed a king on a throne, and everyone remembers.")
C("eir_exile_modifier", "prestige_negative", {"monthly_prestige": -0.2, "general_opinion": -3},
  "In Exile", "You lost a kingdom, and you remember it daily.")
C("eir_blinded_modifier", "prestige_negative", {"monthly_prestige": -0.1, "learning": -1},
  "Struck from the List", "A rival was blinded to bar him from the throne. The act is not forgiven.")
C("eir_champion_victor_modifier", "prowess_positive", {"prowess": 2, "monthly_prestige": 0.25},
  "Victor in Single Combat", "You beat a champion in front of two armies.")

# ---------------------------------------------------------------- county modifiers
K("eir_ogham_stones_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5, "development_growth_factor": 0.03},
  "Ogham Stones", "Old stones carved with letters of strokes mark the boundaries of the old kindreds.")
K("eir_gaelic_schooling_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5, "development_growth_factor": 0.04},
  "Gaelic Schooling", "Children are taught to read, write and recite in the old tongue.")
K("eir_salmon_fisheries_modifier", "county_modifier_development_positive", {"tax_mult": 0.08},
  "Salmon Fisheries", "The weirs fill each autumn.")
K("eir_hurling_fields_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 6},
  "Hurling Fields", "Whole parishes play against one another, and are friends after.")
K("eir_tara_hall_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 8, "tax_mult": 0.05},
  "Rebuilt Hall of Tara", "The great hall stands again on the hill of the kings.")
K("eir_uisneach_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5, "development_growth_factor": 0.03},
  "Hill of Uisneach", "The navel of Ireland, where the fires were lit at Beltane.")
K("eir_newgrange_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 4, "tax_mult": 0.05},
  "Newgrange", "A passage tomb older than the pyramids, lit by the midwinter sun.")
K("eir_rathcroghan_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5, "levy_size": 0.05},
  "Rathcroghan", "The ancient ritual centre of Connacht.")
K("eir_navan_fort_modifier", "county_modifier_control_positive", {"defender_holding_advantage": 5, "county_opinion_add": 3},
  "Emain Macha", "The old capital of the Ulaid, ditch and mound.")
K("eir_dunadd_modifier", "county_modifier_control_positive", {"defender_holding_advantage": 5, "county_opinion_add": 3},
  "Dunadd", "The rock-fort where the kings of Dál Riata were crowned.")
K("eir_kildare_flame_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5, "development_growth_factor": 0.03},
  "Flame of Kildare", "The nuns of Brigid keep the fire burning.")
K("eir_monasterboice_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 4, "tax_mult": 0.05},
  "Monasterboice", "A monastery of high crosses and a pilgrim's road.")
K("eir_armagh_library_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.05, "county_opinion_add": 3},
  "Armagh's Library", "Scholars from across Europe come to read in Armagh.")
K("eir_wooden_harbour_modifier", "county_modifier_development_positive", {"tax_mult": 0.08, "development_growth_factor": 0.03},
  "Wooden Harbours", "Quays of oak timber, and trading ships at anchor.")
K("eir_monastery_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 4, "development_growth_factor": 0.03},
  "A New Monastery", "A monastery has been founded here, and pilgrims already come.")
K("eir_relic_procession_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 6},
  "Relic Passed Through", "A relic was carried through the county.")
K("eir_circuit_visit_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5},
  "Visited by the King", "The king came here, ate here, and slept here.")
K("eir_bog_butter_modifier", "county_modifier_development_positive", {"tax_mult": 0.04},
  "Bog Butter", "Butter buried in the bog in wooden kegs for a hungry winter.")
K("eir_coast_watch_county_modifier", "county_modifier_control_positive", {"defender_holding_advantage": 3, "county_opinion_add": 2},
  "Coastal Watchtowers", "Beacons and watchmen guard the shore.")

# ---------------------------------------------------------------- artifacts
ARTIFACT["eir_bell_shrine_modifier"] = ("piety_positive", {"monthly_piety": 0.3, "clergy_opinion": 4},
    "Bell Shrine", "A bronze and silver shrine for the bell of a saint.")
ARTIFACT["eir_lunula_modifier"] = ("prestige_positive", {"monthly_prestige": 0.25, "diplomacy": 1},
    "Gold Lunula", "A thin crescent of beaten gold, older than the kings.")
ARTIFACT["eir_ogham_blade_modifier"] = ("prowess_positive", {"prowess": 2, "knight_effectiveness_mult": 0.05},
    "Ogham-Marked Blade", "A blade with a line of ogham letters on the spine.")
ARTIFACT["eir_chieftain_torc_modifier"] = ("prestige_positive", {"monthly_prestige": 0.2, "vassal_opinion": 2},
    "Chieftain's Torc", "A twisted gold collar worn by a lesser king.")
ARTIFACT["eir_dimma_book_modifier"] = ("learning_positive", {"learning": 1, "monthly_piety": 0.2},
    "Little Gospel Book", "A small gospel book, small enough to put in a satchel.")

# ---------------------------------------------------------------- traits (fame)
TRAITS["eir_champion_of_ulster"] = ("brave", {"prowess": 3, "monthly_prestige": 0.2, "knight_effectiveness_mult": 0.1},
    "Champion of Ulster", "A champion in the manner of the Red Branch.")
TRAITS["eir_poet_prince"] = ("poet", {"learning": 2, "diplomacy": 1, "owned_legend_spread_mult": 0.1},
    "Poet-Prince", "A ruler who is also a poet of the first rank.")
TRAITS["eir_saint_king"] = ("zealous", {"monthly_piety": 0.4, "clergy_opinion": 8, "stress_gain_mult": -0.05},
    "Saint-King", "A ruler of such piety that the Church speaks of sainthood.")
TRAITS["eir_fosterling"] = ("honest", {"general_opinion": 3, "diplomacy": 1},
    "Fosterling", "Raised in another lord's hall.")
TRAITS["eir_exile_king"] = ("craven", {"monthly_prestige": -0.1, "intrigue": 1},
    "Exile King", "A king without a kingdom, living on others' charity.")
TRAITS["eir_kingmaker"] = ("shrewd", {"diplomacy": 2, "vassal_opinion": 4},
    "Kingmaker", "Known for crowning others.")
TRAITS["eir_peacemaker_of_tara"] = ("just", {"diplomacy": 2, "general_opinion": 5, "monthly_prestige": 0.15},
    "Peacemaker of Tara", "Brought the feuding kings to the same table.")
TRAITS["eir_hostage_scarred"] = ("paranoid", {"stress_gain_mult": 0.1, "intrigue": 1},
    "Hostage-Scarred", "Held captive in youth, and never quite free.")

# ---------------------------------------------------------------- opinions
for k, v in {
    "eir_circuit_host_opinion": "Hosted the king on his circuit",
    "eir_hostage_taken_opinion": "Holds my son hostage",
    "eir_oath_sworn_opinion": "Swore an oath to the king",
    "eir_wergild_paid_opinion": "Paid the honour-price",
    "eir_claim_revoked_opinion": "Struck my claim from the list",
    "eir_kingmaker_opinion": "Placed me on the throne",
    "eir_gwynedd_friend_opinion": "Friend of Gwynedd",
    "eir_breton_refuge_opinion": "Sheltered my family",
    "eir_hebridean_kin_opinion": "Married into the Isles",
}.items():
    OPINIONS[k] = v

# ---------------------------------------------------------------- men-at-arms
MAA["eir_ceithern"] = dict(
    base="heavy_infantry", damage=30, toughness=28, pursuit=0, screen=22,
    terrain={"hills": "damage = 4 toughness = 4", "forest": "damage = 3"},
    counters="light_cavalry = 1", icon="palace_guards", prov="infantry_moderate",
    param="eir_stable_kingship", flag="eir_unlock_ceithern",
    cost=("huscarls_recruitment_cost", "huscarls_low_maint_cost", "huscarls_high_maint_cost"),
    name="Ceithern Retinue",
    flavor="The picked household troops of a king, who eat at his table and die at his door.")

# ---------------------------------------------------------------- v0.5 additions
C("eir_irish_sea_trade_modifier", "economy_positive", {"stewardship": 2, "monthly_income": 2, "diplomacy": 1},
  "Master of the Sea Lanes", "Your captains know every harbour from Chester to Bordeaux, and your name is known there too.")
C("eir_thalassocracy_modifier", "prestige_positive",
  {"monthly_income": 5, "monthly_prestige": 0.6, "stewardship": 2, "naval_movement_speed_mult": 0.3, "knight_effectiveness_mult": 0.05, "vassal_opinion": 5},
  "Sea-King of the West", "Every harbour on the Irish Sea pays you in one coin or another.")
K("eir_cattle_rich_county_modifier", "county_modifier_development_positive", {"tax_mult": 0.08, "levy_size": 0.05},
  "Bó-aire Country", "The cow-freemen of this county keep large herds and larger grudges.")

# ---------------------------------------------------------------- v0.6 additions
OPINIONS["eir_celebrates_crown_opinion"] = "Celebrates your great deed"
OPINIONS["eir_resents_crown_opinion"] = "Resents your great deed"
C("eir_honour_restored_modifier", "prestige_positive", {"monthly_prestige": 0.3, "general_opinion": 5, "stress_gain_mult": -0.05},
  "Honour Restored", "You paid what you owed, and more. The poets now say you are a man who settles his debts.")
C("eir_fair_lord_modifier", "family_positive", {"vassal_opinion": 6, "monthly_income": 1, "monthly_prestige": 0.1},
  "A Fair Lord", "You gave up what the law allowed you, and your people remember it fondly.")
C("eir_peace_with_church_modifier", "piety_positive", {"clergy_opinion": 8, "monthly_piety": 0.3, "monthly_prestige": 0.1},
  "Peace with the Church", "The monks and the reformers sit at one table because you paid for the meal.")

C("eir_hebridean_ties_modifier", "family_positive", {"general_opinion": 3, "levy_size": 0.05},
  "Hebridean Kinship", "The galley-lords of the Isles are bound to you by marriage.")

import v7_world  # noqa: E402,F401  (v0.7 content pack)
