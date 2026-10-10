"""Update 2 content pack: modifiers, opinions, men-at-arms, traditions, the new kingdom, nicknames and names used by
ev_v8*.py, dec_v8.py and gen_script_v8.py. Imported at the end of extra_world.py."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS, MAA, TRADS, TITLES_X, TRAITS, DYNASTY_X

NICKS = [   # (key, name, description)
    ("nick_eir_host_breaker", "Breaker of the Black Host", "Met the great Norse fleet on the strand and sent it home in pieces."),
    ("nick_eir_triumphant", "the Triumphant", "Rode a Gaelic host through the gate of a conquered city."),
    ("nick_eir_island_king", "the Island-King", "Wore the crown of the Island of the Mighty."),
    ("nick_eir_longphort_burner", "Longphort-Burner", "Burned the Norse camp on the river and took its ships."),
]

LOC = [     # (key, text): army names and other plain strings
    ("eir_bh_wave1_name", "The Black Host"),
    ("eir_bh_wave2_name", "The Black Host (Second Landing)"),
    ("eir_bh_wave3_name", "The Great Hosting of the North"),
    ("eir_allied_kings_host_name", "Host of the Kings"),
    ("eir_briton_host_name", "British War-Band"),
    ("eir_alban_host_name", "Albannach Raiders"),
    ("eir_rival_host_name", "The Rival King's Spears"),
    ("eir_isles_reavers_name", "Reavers of the Isles"),
    ("eir_bridgehead_host_name", "The Bridgehead Party"),
    ("eir_black_jarl_sword_name", "The Black Jarl's Sword"),
    ("eir_black_jarl_sword_desc", "A heavy Norse sword with a silver-inlaid hilt, taken from the hand of a warlord who thought Ireland was a poor country."),
    ("eir_david_staff_name", "The Chalice of Saint David"),
    ("eir_david_staff_desc", "A silver chalice whose stem is made from a fragment of Saint David's staff, given by the monks of the west."),
    ("eir_hill_king_sword_name", "Caliburn of the Gael"),
    ("eir_hill_king_sword_desc", "A sword made to match a story that every people on the island tells about itself."),
    ("eir_hoard_cup_name", "The Raiders' Cup"),
    ("eir_hoard_cup_desc", "A cup melted from a pot of Norse hacksilver that a farmer found in a stony field."),
    ("eir_norse_blade_name", "The Pattern-Welded Blade"),
    ("eir_norse_blade_desc", "A sword whose steel flexes like a green branch and keeps an edge through a week of battle, made by a banished Norse smith."),
    ("eir_union_banner_name", "The Banner of the Three Crowns"),
    ("eir_union_banner_desc", "A banner of harp, dragon and chough bound in a ring, stitched by a seamstress who disagreed with the heralds."),
]

# ------------------------------------------------------------------ opinions
OPINIONS.update({
    "eir_allied_kings_opinion": "Stood with the kings",
    "eir_bought_back_opinion": "Bought back",
    "eir_fair_dealing_opinion": "Dealt fairly",
    "eir_hard_justice_opinion": "Hard justice",
    "eir_hosting_opinion": "Called a hosting",
    "eir_justice_done_opinion": "Justice done",
    "eir_norse_pact_opinion": "Made a pact with the Norse",
    "eir_shared_spoils_opinion": "Shared the spoils",
    "eir_slighted_envoy_opinion": "Slighted my envoy",
    "eir_traitor_unmasked_opinion": "Unmasked as a traitor",
    "eir_triumph_opinion": "Witnessed a triumph",
})

# ------------------------------------------------------------------ the Black Host and the Norse
C("eir_black_host_modifier", "dread_mixed", {"advantage": 4, "levy_size": 0.2, "knight_effectiveness_mult": 0.1},
  "The Black Host", "A king's whole war-fleet is behind him, and every man in it has sworn to take the silver of Ireland.")
C("eir_host_demoralised_modifier", "prestige_negative", {"advantage": -6, "levy_size": -0.15},
  "Host Demoralised", "The army has seen its leader humbled, and the tarred sails look a little less black than they did.")
C("eir_beacons_modifier", "prowess_positive", {"defender_advantage": 4, "monthly_prestige": 0.05},
  "Beacon Coast", "A fire on every headland, and the whole coast awake by midnight.")
C("eir_shield_wall_modifier", "prowess_positive", {"advantage": 4, "knight_effectiveness_mult": 0.05, "defender_advantage": 3},
  "The Shield Wall", "Irish spears, in a line, and the line holds.")
C("eir_hill_war_modifier", "prowess_positive", {"defender_advantage": 5, "knight_effectiveness_mult": 0.05, "movement_speed": 0.1},
  "War of the Hills", "Strike and fall back, strike and fall back: the hills are on your side.")
C("eir_split_command_modifier", "prowess_positive", {"advantage": 2, "movement_speed": 0.1, "levy_reinforcement_rate": 0.2},
  "Divided Command", "Two armies, two fords, and the enemy unsure which one is the real one.")
C("eir_foreknowledge_modifier", "learning_positive", {"defender_advantage": 3, "monthly_prestige": 0.05, "intrigue": 1},
  "Foreknowledge", "You know where they will land, how many there are and who is paying them.")
C("eir_allied_kings_modifier", "prestige_positive", {"vassal_opinion": 5, "levy_size": 0.1, "monthly_prestige": 0.15},
  "The Kings Stand Together", "For once, the kings of Ireland are looking in the same direction.")
C("eir_hostile_envoys_modifier", "prestige_negative", {"vassal_opinion": -3, "monthly_prestige": -0.05, "dread_gain_mult": 0.1},
  "Rattled Kings", "You threatened them with the Norse. They have not forgotten who said it.")
C("eir_humble_service_modifier", "family_positive", {"general_opinion": 5, "vassal_opinion": 3, "monthly_prestige": -0.05},
  "Willing to Serve", "You offered to stand beneath a stronger king, and the poets will not forget.")
C("eir_black_host_broken_modifier", "prestige_positive", {"monthly_prestige": 0.8, "dread_gain_mult": 0.2, "general_opinion": 5, "advantage": 2, "vassal_opinion": 5},
  "Breaker of the Black Host", "You met the greatest Norse fleet in a generation and sent it home in pieces.")
C("eir_norse_bane_oath_modifier", "prowess_positive", {"advantage": 4, "monthly_prestige": 0.4, "dread_gain_mult": 0.15, "knight_effectiveness_mult": 0.1},
  "Oath of the Norse-Bane", "You swore on the strand that no raider would land and live to boast of it.")
DYNASTY_X["eir_house_norse_bane_modifier"] = ("family_positive", {"monthly_dynasty_prestige": 0.3},
  "House of the Norse-Bane", "Your house swore the oath on the strand, and your descendants say it as grace before meals.")
C("eir_longphort_burner_modifier", "dread_mixed", {"dread_gain_mult": 0.2, "monthly_prestige": 0.3, "advantage": 2, "general_opinion": -2},
  "Longphort-Burner", "You burned the camp on the river, and the Norse have a long memory too.")
C("eir_longphort_peace_modifier", "economy_mixed", {"monthly_income": 1.5, "vassal_opinion": -2, "monthly_prestige": -0.05},
  "Peace of the Longphort", "The Norse pay the harbour dues, and your kings grumble about the foreigners on the strand.")
C("eir_yoke_broken_modifier", "prestige_positive", {"monthly_prestige": 0.5, "dread_gain_mult": 0.1, "vassal_opinion": 4, "advantage": 2},
  "The Yoke Broken", "You owed the Norse nothing in the end, and the kingdom knows it.")
C("eir_norse_fleet_modifier", "economy_positive", {"naval_movement_speed_mult": 0.25, "sea_travel_danger": -10, "levy_size": 0.05, "monthly_income": 1},
  "Norse Fleet in Your Pay", "Forty Norse ships fly your banner, and the Irish Sea is a little smaller.")
C("eir_norse_kin_modifier", "family_positive", {"general_opinion": 4, "levy_size": 0.05, "monthly_prestige": 0.1, "diplomacy": 1},
  "Norse Kinsman", "A Norse-Gael of your household speaks for you in the harbour towns.")
C("eir_norse_spoils_modifier", "economy_positive", {"monthly_income": 1.5, "monthly_prestige": 0.05},
  "Norse Spoils", "Silver, slaves and good swords, taken from the dead on the strand.")
C("eir_norse_steel_modifier", "prowess_positive", {"knight_effectiveness_mult": 0.08, "men_at_arms_maintenance": -0.03, "advantage": 1},
  "Pattern-Welded Steel", "Your smiths have learned a Norse trick, and the swords flex like green branches.")
C("eir_hostage_peace_modifier", "family_positive", {"stress_gain_mult": -0.05, "general_opinion": 3, "monthly_prestige": 0.05},
  "Hostages in Your Hall", "Their children eat at your table, so their fathers behave.")
C("eir_hunting_hounds_modifier", "prowess_positive", {"prowess": 1, "monthly_lifestyle_xp_gain_mult": 0.1, "health": 0.05},
  "Wolfhounds of the Gael", "Three of them, each taller than a pony, and each as brave as a knight.")
C("eir_kin_defended_modifier", "family_positive", {"general_opinion": 4, "vassal_opinion": 3, "monthly_prestige": 0.1},
  "Defender of Kin", "A cousin in need came to you, and you took his part.")
C("eir_poet_slighted_modifier", "prestige_negative", {"monthly_prestige": -0.15, "general_opinion": -3, "owned_legend_spread_mult": -0.05},
  "Poet Slighted", "You put a poet in the byre, and he has a long memory and a good rhyme for your name.")
C("eir_dun_well_modifier", "family_positive", {"health": 0.05, "stress_gain_mult": -0.05, "defender_advantage": 2},
  "A Deep Well", "The well in the dún has never failed, and the garrison sleeps easier for it.")
C("eir_ancestors_blessing_modifier", "family_positive", {"stress_gain_mult": -0.1, "health": 0.1, "monthly_piety": 0.1},
  "Blessing of the Ancestors", "A place was set for the dead at the table, and the living slept well.")
C("eir_samhain_modifier", "family_positive", {"stress_gain_mult": -0.1, "health": 0.05, "monthly_prestige": 0.1, "owned_legend_spread_mult": 0.05},
  "Samhain Night", "Stories, bonfires and a good deal of ale on the last night of the year.")
C("eir_clan_oath_modifier", "family_positive", {"vassal_opinion": 6, "levy_size": 0.08, "dynasty_house_opinion": 10, "monthly_prestige": 0.1},
  "Sworn Clan", "The kindred swore on the sword, and the oath still holds.")
C("eir_clan_war_law_modifier", "prowess_positive", {"knight_effectiveness_mult": 0.1, "men_at_arms_maintenance": -0.05, "vassal_opinion": 3},
  "Law of the Warband", "The war-leaders wrote down their customs, and the army is steadier for it.")
C("eir_defensive_compact_modifier", "dread_mixed", {"levy_size": 0.15, "vassal_opinion": 5, "defender_advantage": 3, "monthly_prestige": 0.15},
  "Defensive Compact", "The kings of Ireland swore on six saints' relics to stand together against the foreigner.")
C("eir_royal_stud_modifier", "prowess_positive", {"knight_effectiveness_mult": 0.08, "monthly_prestige": 0.1, "movement_speed": 0.1, "monthly_income": 0.5},
  "The Royal Stud", "Small grey horses that run all day, and the grooms who love them.")
C("eir_kinship_law_modifier", "family_positive", {"dynasty_house_opinion": 10, "vassal_opinion": 4, "monthly_dynasty_prestige_mult": 0.1},
  "Law of Kinship", "A man is his kindred, and the law now says so in writing.")
C("eir_pedigree_proclaimed_modifier", "prestige_positive", {"monthly_prestige": 0.25, "legitimacy_gain_mult": 0.1, "vassal_opinion": 2},
  "Pedigree Proclaimed", "Twelve generations in perfect order, read aloud in your own hall.")

# ------------------------------------------------------------------ Britain, culture and the union
C("eir_welsh_ties_modifier", "family_positive", {"general_opinion": 4, "diplomacy": 1, "monthly_prestige": 0.1},
  "Welsh Ties", "A Welsh prince eats at your table and sends you his best poems.")
C("eir_welsh_tongue_modifier", "learning_positive", {"diplomacy": 1, "courtier_and_guest_opinion": 4, "monthly_lifestyle_xp_gain_mult": 0.1},
  "Speaker of Welsh", "Your children have learned the tongue of the Britons, and are quietly insufferable about it.")
C("eir_welsh_resentment_modifier", "family_negative", {"general_opinion": -4, "vassal_opinion": -3},
  "Welsh Resentment", "You made them speak your language, and they remember.")
C("eir_insular_song_modifier", "learning_positive", {"owned_legend_spread_mult": 0.15, "courtier_and_guest_opinion": 5, "monthly_prestige": 0.1},
  "Song of the Island", "Poets of three peoples sing one song about you, in three accents.")
C("eir_book_of_conquests_modifier", "learning_positive", {"owned_legend_spread_mult": 0.2, "monthly_prestige": 0.3, "learning": 1, "vassal_opinion": 3},
  "The Book of Conquests", "Your line is traced back to Míl Espáine, and the poets are still arguing about the dates.")
C("eir_conqueror_crowned_modifier", "prestige_positive", {"monthly_prestige": 0.6, "legitimacy_gain_mult": 0.15, "vassal_opinion": 4, "dread_gain_mult": 0.1},
  "Acclaimed in the Cathedral", "A foreign city sang the Te Deum for you.")
C("eir_insular_union_modifier", "prestige_positive", {"monthly_prestige": 0.6, "vassal_opinion": 6, "general_opinion": 4, "diplomacy": 2, "legitimacy_gain_mult": 0.1},
  "The Insular Union", "Gael, Briton and Pict have sworn a union, and every one of them knows how fragile it is.")
C("eir_island_crown_modifier", "prestige_positive", {"monthly_prestige": 1, "legitimacy_gain_mult": 0.2, "vassal_opinion": 8, "general_opinion": 5, "court_grandeur_baseline_add": 8},
  "The Island Crown", "A crown of plain gold with three stones: green for Ireland, red for Britain, blue for the sea.")
C("eir_sea_road_modifier", "economy_positive", {"monthly_income": 3, "naval_movement_speed_mult": 0.15, "sea_travel_danger": -8, "diplomacy": 1, "monthly_piety": 0.1},
  "The Sea-Road to Alba", "A day's sailing from Antrim to Kintyre, with a quay at each end.")

# ------------------------------------------------------------------ county modifiers
K("eir_beacon_county_modifier", "county_modifier_opinion_positive", {"hostile_raid_time": 0.4, "county_opinion_add": 3, "monthly_county_control_growth_add": 0.1},
  "Beacon Headland", "A stack of tarred wood on the headland, and a watcher who is paid to look at the sea.")
K("eir_bounds_beaten_modifier", "county_modifier_opinion_positive", {"monthly_county_control_growth_add": 0.3, "county_opinion_add": 4, "tax_mult": 0.03},
  "Bounds Beaten", "Every stone on the boundary has been named, and every boy knows where the ditch is.")
K("eir_bridgehead_modifier", "county_modifier_control_negative", {"supply_limit_mult": 0.3, "monthly_county_control_growth_add": 0.2, "levy_size": 0.05},
  "A Foothold on the Coast", "A palisade, a harbour and a party of men with orders to dig in.")
K("eir_cairn_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 8, "monthly_county_control_growth_add": 0.2, "development_growth_factor": 0.03},
  "Cairn of the Fallen", "A hill of stones raised by the families of the dead.")
K("eir_first_dun_modifier", "county_modifier_opinion_positive", {"levy_size": 0.1, "monthly_county_control_growth_add": 0.3, "county_opinion_add": 5, "tax_mult": 0.03},
  "The First Dún", "A great bank and ditch round a timber hall, built by every pair of hands in the district.")
K("eir_gaelic_settlers_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.08, "tax_mult": 0.05, "county_opinion_add": -4, "levy_size": 0.05},
  "Gaelic Settlers", "Three hundred families from the crowded septs of Ireland have taken up land, and the neighbours are watching.")
K("eir_norse_bane_country_modifier", "county_modifier_opinion_positive", {"hostile_raid_time": 0.4, "county_opinion_add": 6, "levy_size": 0.08, "monthly_county_control_growth_add": 0.15},
  "Norse-Bane Country", "The coast where the Black Host died, and where nobody will sleep soundly again.")
K("eir_ogham_boundary_modifier", "county_modifier_opinion_positive", {"monthly_county_control_growth_add": 0.25, "county_opinion_add": 3, "tax_mult": 0.02},
  "Ogham Boundary", "Carved stones at the corners, and an inscription that nobody can argue with.")
K("eir_ostmen_quarter_modifier", "county_modifier_development_positive", {"tax_mult": 0.08, "development_growth_factor": 0.04, "county_opinion_add": -2},
  "Ostmen Quarter", "A district of Norse-Gaelic merchants with their own market, their own saints and their own accent.")
K("eir_redeemed_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 8, "development_growth_factor": 0.05, "levy_size": 0.04},
  "Redeemed Families", "Freed captives have settled here, and give thanks for it every Sunday.")
K("eir_roman_road_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.05, "tax_mult": 0.05, "supply_limit_mult": 0.2, "county_opinion_add": 2},
  "The Old Roman Road", "Four hundred years old, still straight, and still the best road in the county.")
K("eir_samhain_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 6, "tax_mult": 0.03, "monthly_county_control_growth_add": 0.1},
  "Samhain Bonfires", "Every hill is alight on the last night of October, and nobody has gone home early.")
K("eir_scorched_earth_modifier", "county_modifier_development_negative", {"tax_mult": -0.25, "supply_limit_mult": -0.5, "development_growth_factor": -0.1, "county_opinion_add": -4},
  "Scorched Earth", "The crops are burned, the wells are fouled and nothing remains for an invader to eat.")
K("eir_triumph_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 5, "monthly_county_control_growth_add": 0.4, "tax_mult": 0.05},
  "A Triumph Remembered", "The Gaelic host marched through the gate, and the town has not quite got over it.")
K("eir_walled_town_modifier", "county_modifier_development_positive", {"tax_mult": 0.1, "development_growth_factor": 0.06, "monthly_county_control_growth_add": 0.2, "county_opinion_add": 4},
  "Walled Town", "A bank, a gate, a church and a market: the first Irish town built by the Irish.")

# ------------------------------------------------------------------ artifacts
ARTIFACT["eir_black_jarl_sword_modifier"] = ("prowess_positive", {"prowess": 3, "monthly_prestige": 0.3, "knight_effectiveness_mult": 0.1, "dread_gain_mult": 0.1},
    "The Black Jarl's Sword", "A heavy Norse sword with a silver-inlaid hilt, taken from the hand of a warlord who thought Ireland was a poor country.")
ARTIFACT["eir_david_staff_modifier"] = ("piety_positive", {"monthly_piety": 0.4, "clergy_opinion": 5, "monthly_prestige": 0.1},
    "Chalice of Saint David", "A silver chalice with a fragment of the saint's staff in its stem.")
ARTIFACT["eir_hill_king_sword_modifier"] = ("prowess_positive", {"prowess": 2, "monthly_prestige": 0.3, "owned_legend_spread_mult": 0.1, "diplomacy": 1},
    "Caliburn of the Gael", "A sword made to match a story that every people on the island tells about itself.")
ARTIFACT["eir_hoard_cup_modifier"] = ("prestige_positive", {"monthly_prestige": 0.25, "monthly_income": 0.5},
    "The Raiders' Cup", "A cup melted from a pot of Norse hacksilver.")
ARTIFACT["eir_norse_blade_modifier"] = ("prowess_positive", {"prowess": 2, "knight_effectiveness_mult": 0.08, "advantage": 1},
    "Pattern-Welded Blade", "A sword whose steel flexes like a green branch.")
ARTIFACT["eir_union_banner_modifier"] = ("prestige_positive", {"monthly_prestige": 0.4, "vassal_opinion": 4, "general_opinion": 3},
    "Banner of the Three Crowns", "Harp, dragon and chough in a ring.")

# ------------------------------------------------------------------ men-at-arms
MAA["eir_insular_spears"] = dict(
    base="pikemen", damage=22, toughness=28, pursuit=0, screen=22,
    terrain={"hills": "damage = 4 toughness = 4", "forest": "damage = 3", "plains": "toughness = 3"},
    counters="heavy_cavalry = 1\n\t\tlight_cavalry = 1", icon="teulu", prov="infantry_moderate",
    param="eir_insular_union", flag="eir_unlock_insular_spears",
    cost=("huscarls_recruitment_cost", "huscarls_low_maint_cost", "huscarls_high_maint_cost"),
    name="Insular Spearmen",
    flavor="Welsh, Cornish, Pictish and Gaelic spearmen who have learned to stand in the same line.")
MAA["eir_norse_bane_axemen"] = dict(
    base="heavy_infantry", damage=52, toughness=26, pursuit=0, screen=22,
    terrain={"plains": "damage = 4", "wetlands": "damage = 4", "hills": "toughness = 4"},
    counters="skirmishers = 1\n\t\tarchers = 1", icon="danish_huskarls", prov="infantry_moderate",
    param="eir_norse_bane_oath", flag="eir_unlock_norse_bane",
    cost=("huscarls_recruitment_cost", "huscarls_low_maint_cost", "huscarls_high_maint_cost"),
    name="Norse-Bane Axemen",
    flavor="Axemen who stood on the strand, and who have never forgotten how a shield wall breaks.")

# ------------------------------------------------------------------ traditions
# key: (layers background, icon item, None, parameters, modifiers, name, description)
TRADS["tradition_eir_insular_union"] = ("diplo", "crown.dds", None,
    {"eir_insular_union": "yes"},
    {"vassal_opinion": 4, "monthly_prestige_gain_mult": 0.05, "diplomacy": 1, "legitimacy_gain_mult": 0.1, "general_opinion": 3},
    "Union of the Insular Celts",
    "Gael, Briton and Pict swore that they would hold the island together. The oath does not make them one people, but it makes their rulers kin. Unlocks the Insular Spearmen.")
TRADS["tradition_eir_kinship_law"] = ("martial", "conversation.dds", None,
    {"unlock_schiltron_innovation": "yes", "bonuses_from_patriarch_matriarch_trait": "yes", "cultural_house_personal_scheme_success_chance": "yes",
     "landing_house_members_give_prestige": "yes", "penalty_for_revoking_titles_from_house_members": "yes", "loyal_trait_more_common": "yes",
     "eir_kinship_law": "yes"},
    {"dynasty_house_opinion": 20, "opinion_of_liege": -5, "vassal_opinion": 3, "monthly_dynasty_prestige_mult": 0.1},
    "Law of Kinship",
    "A man is his kindred. The elders have written down who owes what, who pays for a death and who may speak for the house. Replaces Strong Kinship; keeps all its effects and softens its worst.")
TRADS["tradition_eir_clan_war_law"] = ("martial", "mountain.dds", None,
    {"rough_terrain_expert_trait_more_common": "yes", "hill_trait_bonuses": "yes", "can_recruit_hill_specialist": "yes",
     "hills_nomadic_cultrad_stationing_bonus": "yes", "eir_clan_war_law": "yes"},
    {"knight_effectiveness_mult": 0.1, "monthly_prestige_gain_mult": 0.05, "men_at_arms_maintenance": -0.05, "army_maintenance_mult": -0.05},
    "Law of the Sword and the Clan",
    "The war-leaders of the Highlands wrote down their customs: how a clan musters, who leads, how spoil is divided. Replaces Highland Warriors; keeps all its effects.")

# ------------------------------------------------------------------ the new kingdom
# key: (tier, capital, color rgb, can_create trigger, emblem, c1, c2, name, adj, pre)
TITLES_X["k_eir_ynys_prydain"] = ("k", "c_isle_of_man", (90, 140, 70), "eir_can_create_island_kingdom_trigger = yes",
    "ce_harp.dds", "green", "red", "the Island of the Mighty", "Insular", "Insular")
