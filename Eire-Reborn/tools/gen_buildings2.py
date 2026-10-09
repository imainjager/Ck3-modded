"""Regular, duchy-capital and special buildings for Eire Reborn (v0.4).

Costs lean on prestige rather than gold, to fit a prestige-and-honour culture.
Output: common/buildings/eir_more_buildings.txt + localization/english/eir_buildings2_l_english.yml
"""
from eir_lib import *

GAEL = "scope:holder = {\n\t\tculture = { has_cultural_pillar = heritage_goidelic }\n\t}"
CELT = ("scope:holder = {\n\t\tculture = {\n\t\t\tOR = {\n\t\t\t\thas_cultural_pillar = heritage_goidelic\n"
        "\t\t\t\thas_cultural_pillar = heritage_brythonic\n\t\t\t}\n\t\t}\n\t}")


def gv(name):
    return "has_global_variable = " + name


# ---------------------------------------------------------------------------
# REGULAR buildings: (key, holding, gate, gold tier, prestige, icon, province, county, character, name, desc)
# ---------------------------------------------------------------------------
REGULAR = [
    ("eir_dun_01", "castle_holding", GAEL, 1, 60, "icon_building_hill_forts.dds",
     {"defender_holding_advantage": 4, "monthly_income": 0.15}, {"levy_size": 0.04}, {"knight_effectiveness_mult": 0.02},
     "Dún", "A hill-fort in the old Irish style: a ring of banks, a timber hall and a stout gate."),
    ("eir_booley_pastures_01", "castle_holding", GAEL, 1, 40, "icon_building_hillside_grazing.dds",
     {"monthly_income": 0.35}, {"tax_mult": 0.03, "development_growth_factor": 0.01}, {},
     "Booley Pastures", "Summer pastures in the hills, where the herds go with the first good weather."),
    ("eir_fosterage_hall_01", "castle_holding", GAEL + "\n\t" + gv("eir_done_fosterage"), 2, 90, "icon_building_hall_of_heroes.dds",
     {"monthly_income": 0.1}, {"county_opinion_add": 3}, {"monthly_prestige": 0.05, "vassal_opinion": 1},
     "Fosterage Hall", "A long hall where the sons of the vassals are raised beside the lord's own children."),
    ("eir_bruidhean_01", "city_holding", GAEL, 2, 80, "icon_building_guild_halls.dds",
     {"monthly_income": 0.3}, {"county_opinion_add": 3, "development_growth_factor": 0.01}, {"monthly_prestige": 0.05},
     "Bruidhean", "A hostel of open doors, where any traveller must be fed and sheltered by ancient law."),
    ("eir_aonach_01", "city_holding", GAEL, 1, 50, "icon_building_market_villages.dds",
     {"monthly_income": 0.45}, {"tax_mult": 0.04}, {},
     "Aonach Fair Ground", "A fair ground where the clans meet to trade, wrestle and quarrel."),
    ("eir_goibniu_smithy_01", "city_holding", GAEL, 2, 70, "icon_building_smiths.dds",
     {"monthly_income": 0.2}, {"levy_size": 0.03}, {"knight_effectiveness_mult": 0.04},
     "Smithy of Goibniu", "A forge that claims descent from the divine smith, and makes bronze and iron to match."),
    ("eir_irish_stables_01", "castle_holding", GAEL, 1, 40, "icon_building_stables.dds",
     {"monthly_income": 0.15}, {"levy_size": 0.03}, {"knight_effectiveness_mult": 0.03},
     "Hobby Stables", "Small, quick Irish horses bred for the hills and the bog."),
    ("eir_holy_well_01", "church_holding", GAEL, 1, 50, "icon_building_graveyard.dds",
     {"monthly_income": 0.2}, {"county_opinion_add": 4}, {"monthly_piety": 0.08},
     "Holy Well Shrine", "A spring said to heal the sick, now ringed with offerings of rags and ribbons."),
    ("eir_monastic_school_01", "church_holding", GAEL, 2, 90, "icon_building_monastic_schools.dds",
     {"monthly_income": 0.2}, {"development_growth_factor": 0.03}, {"learning": 1, "monthly_piety": 0.05},
     "Monastic School", "Students from Britain and the Continent come to read, copy and argue."),
    ("eir_hermitage_01", "church_holding", GAEL, 1, 40, "icon_building_graveyard.dds",
     {"monthly_income": 0.1}, {"county_opinion_add": 3}, {"monthly_piety": 0.1, "stress_gain_mult": -0.02},
     "Hermitage", "A beehive cell on a lonely rock, where a holy man prays and the locals bring him food."),
    ("eir_pilgrim_hospice_01", "church_holding", GAEL, 1, 50, "icon_building_guild_halls.dds",
     {"monthly_income": 0.3}, {"county_opinion_add": 2, "tax_mult": 0.03}, {"monthly_piety": 0.05},
     "Pilgrim Hospice", "A guest house at a holy place, where pilgrims rest and pay what they can."),
    ("eir_sea_quay_01", "any", GAEL + "\n\t\tis_coastal = yes\n\t\t" + gv("eir_unlock_sea_trade"), 3, 150, "icon_building_market_villages.dds",
     {"monthly_income": 0.8}, {"tax_mult": 0.05, "development_growth_factor": 0.02}, {"monthly_income": 0.3, "stewardship": 1},
     "Irish Sea Quay", "A timber quay where Irish cattle, hides and slaves are sold to the merchants of Bristol, Chester and Dublin."),
    ("eir_shipyard_01", "any", GAEL + "\n\t\tis_coastal = yes\n\t\t" + gv("eir_unlock_sea_trade"), 3, 200, "icon_building_stables.dds",
     {"monthly_income": 0.4, "supply_limit_mult": 0.1}, {"levy_size": 0.04}, {"knight_effectiveness_mult": 0.03, "monthly_prestige": 0.05},
     "Longship Yard", "A sheltered cove where sea-kings build and mend the long galleys."),
    ("eir_ogham_stones_01", "castle_holding", GAEL, 1, 30, "icon_building_watchtowers.dds",
     {"monthly_income": 0.1}, {"county_opinion_add": 2}, {"owned_legend_spread_mult": 0.02},
     "Ogham Pillar Field", "Standing stones cut with notches that name the dead and the lands they held."),
]

# ---------------------------------------------------------------------------
# DUCHY CAPITAL buildings: (key, duchy or None, culture gate, gold tier, prestige, icon, county(all de jure counties), character, name, desc)
# ---------------------------------------------------------------------------
DUCHY = [
    ("eir_rightech_01", None, CELT, 3, 300, "icon_building_hall_of_heroes.dds",
     {"county_opinion_add": 3, "development_growth_factor": 0.02},
     {"court_grandeur_baseline_add": 3, "monthly_prestige": 0.1, "vassal_opinion": 2},
     "Ríghteach", "The great hall of a king, with room for a thousand guests and every poet in the province."),
    ("eir_munster_seat_01", "d_munster", GAEL, 4, 500, "icon_building_hill_forts.dds",
     {"county_opinion_add": 3, "levy_size": 0.05},
     {"court_grandeur_baseline_add": 4, "monthly_prestige": 0.15, "knight_effectiveness_mult": 0.03},
     "Seat of the Eóganachta", "The ancient seat of the kings of Munster, on a limestone rock above the plain."),
    ("eir_meath_court_01", "d_meath", GAEL, 4, 500, "icon_building_tax_assessor.dds",
     {"county_opinion_add": 3, "tax_mult": 0.03},
     {"court_grandeur_baseline_add": 4, "legitimacy_gain_mult": 0.05, "vassal_opinion": 3},
     "Court of the Ard Rí", "The court that judges the quarrels of the kings, in the heart of Ireland."),
    ("eir_ulster_fortress_01", "d_ulster", GAEL, 4, 500, "icon_building_palisades.dds",
     {"county_opinion_add": 3, "defender_holding_advantage": 0},
     {"court_grandeur_baseline_add": 4, "monthly_prestige": 0.1, "prowess": 1},
     "Fortress of the Ulaid", "A great earthwork in the north, with a hall where the Red Branch is remembered."),
    ("eir_connacht_seat_01", "d_connacht", GAEL, 4, 500, "icon_building_barracks.dds",
     {"county_opinion_add": 3, "levy_size": 0.06},
     {"court_grandeur_baseline_add": 4, "monthly_prestige": 0.1, "martial": 1},
     "Seat of Cruachan", "The royal seat of Connacht, with its ring of banks and its tales of Medb."),
    ("eir_leinster_dun_01", "d_leinster", GAEL, 4, 500, "icon_building_stables.dds",
     {"county_opinion_add": 3, "tax_mult": 0.04},
     {"court_grandeur_baseline_add": 4, "monthly_income": 0.5, "stewardship": 1},
     "Dún of Leinster", "The rich eastern kingdom's hill-fort, with a view of the whole plain."),
    ("eir_albany_stone_01", "d_albany", GAEL, 4, 500, "icon_building_hall_of_heroes.dds",
     {"county_opinion_add": 3, "development_growth_factor": 0.02},
     {"court_grandeur_baseline_add": 4, "monthly_prestige": 0.15, "diplomacy": 1},
     "Crowning Stone of Alba", "A sacred stone on which the kings of the Gael are inaugurated."),
    ("eir_isles_galley_yard_01", "d_the_isles", CELT, 3, 400, "icon_building_stables.dds",
     {"county_opinion_add": 2, "levy_size": 0.04},
     {"court_grandeur_baseline_add": 3, "monthly_income": 0.4, "knight_effectiveness_mult": 0.02},
     "Galley Yard of the Isles", "Where the sixty-oared galleys of the Isles are built."),
    ("eir_gwynedd_stronghold_01", "d_gwynedd", CELT, 4, 500, "icon_building_hill_forts.dds",
     {"county_opinion_add": 3, "defender_holding_advantage": 0},
     {"court_grandeur_baseline_add": 4, "monthly_prestige": 0.15, "prowess": 1},
     "Stronghold of Snowdonia", "A mountain stronghold from which the princes of Gwynedd defy all comers."),
    ("eir_cornwall_stannary_01", "d_cornwall", CELT, 3, 350, "icon_building_smiths.dds",
     {"county_opinion_add": 2, "tax_mult": 0.05},
     {"court_grandeur_baseline_add": 3, "monthly_income": 0.6},
     "Stannary Hall", "The hall where the tinners of Cornwall meet to set the price of tin."),
]

# ---------------------------------------------------------------------------
# SPECIAL buildings: (key, barony, gate, gold tier, prestige, icon, province, county, character, name, desc)
# ---------------------------------------------------------------------------
SPECIAL = [
    ("eir_hall_of_tara_01", "b_tara", gv("eir_done_tara_hall"), 5, 1000, "icon_structure_cologne_cathedral.dds",
     {"monthly_income": 1.0}, {"county_opinion_add": 8, "development_growth_factor": 0.05},
     {"monthly_prestige": 0.6, "legitimacy_gain_mult": 0.1, "vassal_opinion": 5, "court_grandeur_baseline_add": 6},
     "Hall of Tara", "The royal hall of the High Kings, rebuilt on the Hill of Tara."),
    ("eir_armagh_cathedral_01", "b_armagh", gv("eir_done_armagh"), 5, 800, "icon_structure_canterbury_cathedral.dds",
     {"monthly_income": 1.2}, {"county_opinion_add": 6, "tax_mult": 0.08},
     {"monthly_piety": 0.6, "clergy_opinion": 8, "learning": 1},
     "Cathedral of Armagh", "The primatial church of Ireland, with its famous library and bell shrine."),
    ("eir_rathcroghan_01", "b_cruachu", GAEL, 4, 600, "icon_building_hall_of_heroes.dds",
     {"monthly_income": 0.6}, {"county_opinion_add": 5, "levy_size": 0.06},
     {"monthly_prestige": 0.35, "martial": 1},
     "Royal Site of Rathcroghan", "A vast complex of mounds and ditches, the ritual capital of Connacht."),
    ("eir_slemish_shrine_01", "b_slemish", GAEL, 3, 400, "icon_building_graveyard.dds",
     {"monthly_income": 0.5}, {"county_opinion_add": 5, "tax_mult": 0.04},
     {"monthly_piety": 0.35, "clergy_opinion": 4},
     "Patrick's Hill", "The mountain where the slave-boy Patrick herded sheep and heard his call."),
    ("eir_uisneach_fires_01", "b_uisneach", gv("eir_done_oenach"), 4, 500, "icon_building_watchtowers.dds",
     {"monthly_income": 0.5}, {"county_opinion_add": 5, "development_growth_factor": 0.04},
     {"monthly_prestige": 0.3, "diplomacy": 1},
     "Fires of Uisneach", "The navel of Ireland, where the first Beltane fire was lit."),
    ("eir_kildare_flame_01", "b_kildare", GAEL, 4, 500, "icon_building_graveyard.dds",
     {"monthly_income": 0.6}, {"county_opinion_add": 6, "development_growth_factor": 0.03},
     {"monthly_piety": 0.4, "health": 0.1},
     "Fire of Brigid", "A perpetual flame tended by nuns, in honour of the saint and the goddess."),
    ("eir_emly_monastery_01", "b_emly", GAEL, 3, 350, "icon_building_monastic_schools.dds",
     {"monthly_income": 0.5}, {"county_opinion_add": 4, "development_growth_factor": 0.03},
     {"monthly_piety": 0.3, "learning": 1},
     "Monastery of Ailbe", "A great Munster monastery with a fine school and a famous bell."),
    ("eir_kincora_01", "b_kincora", GAEL, 4, 500, "icon_building_hall_of_heroes.dds",
     {"monthly_income": 0.7}, {"county_opinion_add": 5, "levy_size": 0.05},
     {"monthly_prestige": 0.4, "knight_effectiveness_mult": 0.04},
     "Palace of Kincora", "The hall of Brian Boru, where a new High King once feasted his captains."),
    ("eir_black_pool_quays_01", "b_dublin", gv("eir_done_dublin"), 4, 450, "icon_building_market_villages.dds",
     {"monthly_income": 1.6}, {"tax_mult": 0.1, "development_growth_factor": 0.05},
     {"monthly_income": 1.0, "diplomacy": 1},
     "Black Pool Quays", "The great Norse-Gael harbour on the Liffey, now in Irish hands."),
    ("eir_waterford_harbour_01", "b_waterford", GAEL, 3, 350, "icon_building_market_villages.dds",
     {"monthly_income": 1.2}, {"tax_mult": 0.08, "development_growth_factor": 0.04},
     {"monthly_income": 0.6},
     "Harbour of Waterford", "A Norse harbour that now flies Irish colours and trades with Bristol and Bordeaux."),
    ("eir_cork_quays_01", "b_cork", GAEL, 3, 350, "icon_building_market_villages.dds",
     {"monthly_income": 1.0}, {"tax_mult": 0.08, "development_growth_factor": 0.03},
     {"monthly_income": 0.5},
     "Quays of Cork", "Quays built by Norse merchants beside the monastery of Saint Finbarr."),
    ("eir_limerick_longphort_01", "b_limerick", GAEL, 3, 350, "icon_building_barracks.dds",
     {"monthly_income": 0.8, "defender_holding_advantage": 5}, {"tax_mult": 0.06, "levy_size": 0.05},
     {"martial": 1, "monthly_prestige": 0.15},
     "Longphort of Limerick", "A Norse river-fortress that commands the Shannon."),
    ("eir_derry_oakgrove_01", "b_derry", GAEL, 3, 400, "icon_building_graveyard.dds",
     {"monthly_income": 0.5}, {"county_opinion_add": 5, "development_growth_factor": 0.03},
     {"monthly_piety": 0.3, "learning": 1},
     "Oakgrove of Colmcille", "The saint's oak-wood monastery, the cradle of the Columban church."),
    ("eir_downpatrick_01", "b_downpatrick", GAEL, 3, 400, "icon_building_graveyard.dds",
     {"monthly_income": 0.5}, {"county_opinion_add": 5, "tax_mult": 0.04},
     {"monthly_piety": 0.3, "clergy_opinion": 5},
     "Grave of the Three Saints", "Where Patrick, Brigid and Colmcille are said to lie together."),
    ("eir_bangor_school_01", "b_bangor", gv("eir_done_fili"), 3, 400, "icon_building_library.dds",
     {"monthly_income": 0.5}, {"development_growth_factor": 0.05, "county_opinion_add": 3},
     {"learning": 2, "monthly_prestige": 0.15},
     "School of Bangor", "A monastery whose scholars once taught half of Europe to read."),
    ("eir_trim_school_01", "b_trim", GAEL, 3, 350, "icon_building_library.dds",
     {"monthly_income": 0.5}, {"development_growth_factor": 0.04, "county_opinion_add": 3},
     {"learning": 1, "monthly_prestige": 0.15},
     "Church of Trim", "A monastic church beside the Boyne, with a school of renown."),
    ("eir_kilkenny_monastery_01", "b_kilkenny", GAEL, 3, 350, "icon_building_monastic_schools.dds",
     {"monthly_income": 0.5}, {"development_growth_factor": 0.04, "county_opinion_add": 3},
     {"monthly_piety": 0.25, "learning": 1},
     "Monastery of Canice", "A major monastic centre of Ossory, with a round tower and a famous scriptorium."),
    ("eir_tuam_cross_01", "b_tuam", gv("eir_done_cashel"), 3, 400, "icon_building_graveyard.dds",
     {"monthly_income": 0.5}, {"county_opinion_add": 4, "tax_mult": 0.05},
     {"monthly_piety": 0.3, "clergy_opinion": 4},
     "High Cross of Tuam", "A carved cross with scenes of kings and saints, raised by the kings of Connacht."),
    ("eir_ferns_seat_01", "b_ferns", GAEL, 3, 350, "icon_building_hill_forts.dds",
     {"monthly_income": 0.5, "defender_holding_advantage": 5}, {"county_opinion_add": 4, "levy_size": 0.04},
     {"monthly_prestige": 0.2, "vassal_opinion": 2},
     "Royal Seat of Ferns", "The seat of the kings of Leinster, above the Slaney valley."),
]


def costs(gold_tier, prestige):
    return "\tcost_gold = normal_building_tier_%d_cost\n\tcost_prestige = %d\n" % (gold_tier, prestige)


def mods(province, county, character):
    out = ""
    for name, d in (("province_modifier", province), ("county_modifier", county), ("character_modifier", character)):
        d = {k: v for k, v in d.items() if v != 0}
        if d:
            out += "\t%s = {\n%s\t}\n" % (name, fields_block(d, "\t\t"))
    return out


def build():
    L = Loc("eir_buildings2_l_english.yml")
    out = ["# Eire Reborn - more buildings (regular, duchy capital and special). Generated by tools/gen_buildings2.py\n"
           "# Costs favour prestige over gold: this is a culture of honour.\n\n"]

    L.section("regular buildings")
    for key, hold, gate, tier, pres, icon, prov, county, char, name, desc in REGULAR:
        for d in (prov, county, char):
            check_keys(key, d)
        out.append("%s = {\n\tconstruction_time = slow_construction_time\n\n" % key)
        out.append("\tis_enabled = {\n\t\t%s\n\t}\n\n" % gate)
        if hold == "any":
            holdcond = ("OR = {\n\t\t\thas_holding_type = tribal_holding\n\t\t\thas_holding_type = castle_holding\n"
                        "\t\t\thas_holding_type = city_holding\n\t\t\thas_holding_type = church_holding\n\t\t}")
        else:
            holdcond = "OR = {\n\t\t\thas_holding_type = tribal_holding\n\t\t\thas_holding_type = %s\n\t\t}" % hold
        out.append("\tcan_construct_potential = {\n\t\t%s\n\t\t%s\n\t}\n\n" % (holdcond, gate))
        out.append("\tcan_construct_showing_failures_only = {\n\t\tscope:holder = { is_at_war = no }\n\t}\n\n")
        out.append(costs(tier, pres) + "\n")
        out.append(mods(prov, county, char) + "\n")
        out.append('\ttype_icon = "%s"\n\n\tai_value = {\n\t\tbase = 4\n\t}\n}\n\n' % icon)
        L.add("building_" + key, name)
        L.add("building_%s_desc" % key, desc)

    L.section("duchy capital buildings")
    for key, duchy, gate, tier, pres, icon, county, char, name, desc in DUCHY:
        for d in (county, char):
            check_keys(key, d)
        where = ("\t\tcounty = { duchy = title:%s }\n" % duchy) if duchy else ""
        out.append("%s = {\n\tconstruction_time = slow_construction_time\n\n" % key)
        out.append("\tcan_construct_potential = {\n\t\t%s\n%s\t}\n\n" % (gate, where))
        out.append("\tis_enabled = {\n\t\tcounty.holder = { has_title = prev.duchy }\n\t}\n\tshow_disabled = yes\n\n")
        out.append(costs(tier, pres) + "\n")
        c = {k: v for k, v in county.items() if v != 0}
        if c:
            out.append("\tduchy_capital_county_modifier = {\n%s\t}\n" % fields_block(c, "\t\t"))
        ch = {k: v for k, v in char.items() if v != 0}
        out.append("\tcharacter_modifier = {\n%s\t}\n\n" % fields_block(ch, "\t\t"))
        out.append('\ttype_icon = "%s"\n\n\ttype = duchy_capital\n\n\tai_value = {\n\t\tbase = 6\n\t}\n}\n\n' % icon)
        L.add("building_" + key, name)
        L.add("building_%s_desc" % key, desc)

    L.section("special buildings")
    for key, bar, gate, tier, pres, icon, prov, county, char, name, desc in SPECIAL:
        for d in (prov, county, char):
            check_keys(key, d)
        out.append("%s = {\n\tconstruction_time = very_slow_construction_time\n\n" % key)
        out.append("\tcan_construct_potential = {\n\t\tbarony ?= title:%s\n\t}\n\n" % bar)
        reqs = GAEL if gate == GAEL else GAEL + "\n\t\t" + gate
        out.append("\tcan_construct = {\n\t\t%s\n\t}\n\n" % reqs)
        out.append("\tis_enabled = {\n\t\tbarony ?= title:%s\n\t}\n\tshow_disabled = yes\n\n" % bar)
        out.append("\tcan_construct_showing_failures_only = {\n\t\tscope:holder = { is_at_war = no }\n\t}\n\n")
        out.append(costs(tier, pres) + "\n")
        out.append(mods(prov, county, char) + "\n")
        out.append('\ttype_icon = "%s"\n\n\ttype = special\n\n\tai_value = {\n\t\tbase = 8\n\t}\n}\n\n' % icon)
        L.add("building_" + key, name)
        L.add("building_%s_desc" % key, desc)

    write("common/buildings/eir_more_buildings.txt", "".join(out))

    # scripted trigger: the realm contains at least COUNT counties with one of these buildings
    keys = [r[0] for r in REGULAR]
    cond = "".join("\t\t\t\thas_building = %s\n" % k for k in keys)
    trig = ("# Generated by tools/gen_buildings2.py\n"
            "eir_irish_buildings_trigger = {\n\tany_sub_realm_county = {\n\t\tcount >= $COUNT$\n"
            "\t\tany_county_province = {\n\t\t\tOR = {\n%s\t\t\t}\n\t\t}\n\t}\n}\n" % cond)
    write("common/scripted_triggers/eir_building_triggers.txt", trig)
    L.write()
    print("buildings2: %d regular, %d duchy capital, %d special" % (len(REGULAR), len(DUCHY), len(SPECIAL)))


if __name__ == "__main__":
    build()
