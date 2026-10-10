"""Update 2 decisions (v0.8). Registered after dec_finalize, so costs here are final.
Chieftain rungs (cheap, early), the Norse struggle, conquest and culture in Britain, and the kings against each other.
Each follows the flavor loop: hook, gate, commitment, ceremony event, reaction, reward, risk and remedy, memory, follow-up."""
from gen_decisions import D, IRISH, GAEL
from evdsl import RL

S1 = "eir_stage1_trigger = yes"
S2 = "eir_stage2_trigger = yes"
S3 = "eir_stage3_trigger = yes"
VIS = "eir_visible_stage1_trigger = yes"
FILI = "has_global_variable = eir_done_fili"
BROTH = "has_global_variable = eir_done_brotherhood"
MONK = "has_global_variable = eir_done_monastery"
FOSTER = "has_global_variable = eir_done_fosterage"
OENACH = "has_global_variable = eir_done_oenach"
BHBROKEN = "has_global_variable = eir_black_host_broken"
UNION = "has_global_variable = eir_done_union"
CONQ = "random_sub_realm_county = {\n\tlimit = { eir_foreign_conquest_county_trigger = yes }\n\tsave_scope_as = eir_conq_county\n}"


def req(*lines):
    return "\n".join(l for l in lines if l)


def cost(gold=0, prestige=0, piety=0):
    return "\n".join(x for x in (("gold = %d" % gold) if gold else "", ("prestige = %d" % prestige) if prestige else "", ("piety = %d" % piety) if piety else "") if x)


def not_done(var):
    return "NOT = { has_global_variable = %s }" % var


# =============================================================================
# THE CHIEFTAIN'S RUNGS (shown from two counties; cheap, so the early game has something to do)
# =============================================================================
D("eir_swear_clan_oath_decision", "Swear the Clan Oath",
  "Your kinsmen are a loose crowd. Make them a clan: gather the four generations on the hill and have each man touch the sword and say the words.",
  "Needs three counties. A Clan Oath modifier for 12 years, vassal opinion and prestige, a hostage option for the doubtful. Every ten years the oath can be renewed.",
  GAEL + "\n" + VIS,
  """add_prestige = minor_prestige_gain
eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 4 }
trigger_event = eir.0544""",
  valid=req("eir_realm_size_trigger = { N = 3 }", "NOT = { has_character_modifier = eir_clan_oath_modifier }", "is_at_war = no"),
  cost=cost(gold=30, prestige=100), cd=3650, pic="decision_dynasty_house")

D("eir_hold_samhain_feast_decision", "Hold the Samhain Feast",
  "On the last night of October the veil between the living and the dead is thin. Hold the feast in your hall, light the bonfire on the hill and set a place for the ancestors.",
  "Only in October or November. A Samhain modifier for three years, a bonfire on the hill, a night of stories and a chance of a lifestyle trait. A little stress relief for the festive; the zealous will want it kept to the Mass. Every three years.",
  GAEL + "\n" + VIS,
  """add_prestige = minor_prestige_gain
add_stress = minor_stress_loss
capital_county ?= { add_county_modifier = { modifier = eir_samhain_county_modifier years = 3 } }
trigger_event = eir.0545""",
  valid=req("current_month >= 10", "current_month <= 11", "is_at_war = no", "eir_realm_size_trigger = { N = 2 }"),
  cost=cost(gold=40, prestige=40), cd=1095, pic="decision_activity")

D("eir_beat_the_bounds_decision", "Beat the Bounds",
  "Walk the whole boundary of your lands with the community. Name every stone, bank and ford, and make the boys remember where the ditch is.",
  "Needs two counties and peace. A Bounds Beaten modifier on the capital county (control and opinion), prestige, and a chance to set ogham pillars at the corners. Every five years.",
  GAEL + "\n" + VIS,
  """add_prestige = minor_prestige_gain
capital_county ?= { change_county_control = minor_county_control_gain }
trigger_event = eir.0546""",
  valid=req("eir_realm_size_trigger = { N = 2 }", "is_at_war = no"),
  cost=cost(gold=30, prestige=60), cd=1825, pic="decision_castle_view")

D("eir_grant_land_to_saint_decision", "Grant Land to a Saint",
  "A holy man with a bell has asked for a green hill and a spring. Give him the land, and the saint's good will comes with it.",
  "Needs piety and two counties. A hospice in the capital county, a saint's blessing, a chance at the first Hermitage. A priest keeps the memory of the gift. Every ten years.",
  GAEL + "\n" + VIS,
  """add_piety = minor_piety_gain
capital_county ?= { add_county_modifier = { modifier = eir_hospice_modifier years = 8 } }
trigger_event = eir.0547""",
  valid=req("piety >= 30", "eir_realm_size_trigger = { N = 2 }"),
  cost=cost(gold=40, piety=30), cd=3650, pic="decision_personal_religious")

D("eir_seal_pact_decision", "Seal a Pact with a Neighbouring Sept",
  "The chief of the next valley is tired of quarrelling. Meet him halfway, swear a pact and exchange a horse and a poet.",
  "Needs three counties, peace and a Gaelic neighbour. A Wergild Peace modifier for 10 years, prestige, hooks on the neighbour, and the option to exchange fosterlings. Beware the oath-breaker's reputation.",
  GAEL + "\n" + VIS,
  """add_prestige = minor_prestige_gain
trigger_event = eir.0548""",
  valid=req("eir_realm_size_trigger = { N = 3 }", "is_at_war = no", "eir_has_gael_neighbour_trigger = yes"),
  cost=cost(gold=50, prestige=100), cd=3650, pic="decision_social")

D("eir_raise_first_dun_decision", "Raise Your First Dún",
  "A chieftain is only as safe as his bank and ditch. Call the whole community together, carry earth and raise the great hill-fort at your seat.",
  "Needs two counties. A First Dún modifier in the capital county (defence and levies), prestige, and a poet who sings of it. Once per game, and it opens the Dún building chain.",
  GAEL + "\n" + VIS + "\n" + not_done("eir_unique_first_dun"),
  """add_prestige = medium_prestige_gain
capital_county ?= { add_county_modifier = { modifier = eir_first_dun_modifier years = 15 } }
set_global_variable = eir_unique_first_dun
trigger_event = eir.0549""",
  valid=req("eir_realm_size_trigger = { N = 2 }", "is_at_war = no"),
  cost=cost(gold=60, prestige=100), cd=36500, pic="decision_castle_view")

# =============================================================================
# THE NORSE: WATCH, DEFEND, BREAK
# =============================================================================
D("eir_light_beacon_chain_decision", "Light the Beacon Chain",
  "A hill-top fire every five miles, from headland to headland. A fleet can be seen at dusk and the whole coast can be roused by midnight.",
  "Needs a coastal county and the Viking age. Beacon modifiers on all coastal counties for 10 years (raid time, opinion), a ready-to-fire coast for your next landing event and a night of fires. Every 15 years.",
  GAEL + "\n" + VIS + "\neir_viking_age_trigger = yes",
  """every_realm_county = {
	limit = { is_coastal_county = yes }
	add_county_modifier = { modifier = eir_beacon_county_modifier years = 10 }
}
add_character_modifier = { modifier = eir_beacons_modifier years = 8 }
add_prestige = minor_prestige_gain
trigger_event = eir.0550""",
  valid=req("eir_ports_trigger = { N = 1 }", "is_at_war = no"),
  cost=cost(gold=80, prestige=80), cd=5475, pic="decision_siege_warfare")

D("eir_call_defensive_compact_decision", "Call the Defensive Compact",
  "The kings of Ireland have never held a line together. Summon them to the hill, and put a promise on the relics.",
  "Needs a duchy, the Great Óenach and a Norse presence or the Black Host. Defensive Compact modifier (levies and opinion) for 15 years, allied-king opinion, hostages round the table. Once per game.",
  GAEL + "\n" + VIS + "\n" + S2 + "\n" + not_done("eir_unique_compact"),
  """add_character_modifier = { modifier = eir_defensive_compact_modifier years = 15 }
add_prestige = major_prestige_gain
add_piety = minor_piety_gain
eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 6 }
set_variable = { name = eir_bh_alliance value = 2 }
set_global_variable = eir_unique_compact
trigger_event = eir.0551""",
  valid=req(S2, OENACH, "eir_norse_presence_trigger = yes", "any_vassal = { count >= 3 }", "is_at_war = no"),
  cost=cost(gold=150, prestige=400, piety=50), cd=36500, pic="decision_realm")

D("eir_hire_norse_fleet_decision", "Hire a Norse Fleet",
  "Set a Norse-Gael captain on your own side. His forty ships know every cove from Dublin to the Hebrides, and his price is high.",
  "Needs a chieftain and two ports. A Norse fleet modifier and a free mercenary company for four years. A one in four chance that he sells you out and keeps the pay. Every ten years.",
  GAEL + "\n" + VIS + "\neir_viking_age_trigger = yes",
  RL((75, "norse_fleet_loyal", "The captain keeps his word and his ships sail under your banner",
      [(10, "diplomacy >= 12")],
      """add_character_modifier = { modifier = eir_norse_fleet_modifier years = 4 }
spawn_army = {
	levies = 0
	men_at_arms = {
		type = armored_footmen
		stacks = 3
	}
	location = capital_province
	origin = capital_province
	inheritable = no
	name = eir_gallowglass_company_name
}
add_prestige = minor_prestige_gain"""),
     (25, "norse_fleet_sold", "The captain sells your plans to your enemy and keeps the silver",
      [],
      """add_prestige = minor_prestige_loss
add_stress = minor_stress_gain
add_character_modifier = { modifier = eir_raider_infamy_modifier years = 4 }""")) + "\ntrigger_event = eir.0552",
  valid=req("eir_ports_trigger = { N = 2 }", "is_at_war = no", "eir_realm_size_trigger = { N = 3 }"),
  cost=cost(gold=250, prestige=60), cd=3650, pic="decision_recruitment")

D("eir_redeem_captives_decision", "Redeem the Captives",
  "Norse slave pens are full of people from your coast. Send silver and monks to buy them out, one family at a time.",
  "Needs the Black Host to have come. Ransom costs gold and piety; the captives are fed, healed and settled. Opinion with the court and the Church, a Redeemed settlement in the capital county, a chance of the Compassionate trait. Every ten years.",
  GAEL + "\n" + VIS + "\nhas_global_variable = eir_bh_started",
  """add_prestige = medium_prestige_gain
add_piety = medium_piety_gain
eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 6 }
trigger_event = eir.0553""",
  valid=req("is_at_war = no", "eir_realm_size_trigger = { N = 2 }"),
  cost=cost(gold=200, piety=50), cd=3650, pic="decision_personal_religious")

D("eir_break_norse_yoke_decision", "Break the Norse Yoke",
  "If a Norse king has bled you of cattle, hostages and pride, there is one way out: refuse the next tax, and be ready to meet whoever comes to collect it.",
  "Needs a duchy, 10 Irish counties, 600 prestige and a Norse defeat on your record, or a paid Danegeld. Ends the Danegeld, grants claims on Norse-held land in Ireland, a Yoke Broken modifier for 20 years, and a ceremony of your choosing. The remedy that makes the old shame into a boast. Once per game.",
  GAEL + "\n" + VIS + "\n" + not_done("eir_unique_norse_yoke"),
  """add_prestige = major_prestige_gain
add_piety = minor_piety_gain
eir_end_danegeld_effect = yes
eir_grant_claims_norse_effect = yes
set_global_variable = eir_unique_norse_yoke
trigger_event = eir.0554""",
  valid=req(S2, "eir_holds_irish_counties_trigger = { COUNT = 10 }", "prestige >= 600", "is_at_war = no",
            "OR = {\nhas_variable = eir_bh_defeated\nhas_character_flag = eir_paid_danegeld\nhas_character_modifier = eir_danegeld_modifier\n}"),
  cost=cost(gold=250, prestige=500), cd=36500, major=True, pic="decision_found_kingdom")

D("eir_burn_longphort_decision", "Burn the Longphort",
  "The Norse camp on the river has sat there since your grandfather's time. Gather boats, move by night and light the sheds.",
  "Needs a duchy and a Norse-held county in Ireland, and either the Black Host broken or a peace with the Norse. Pressed claims on the Norse-held counties, prestige and dread, a Norse grudge, and a ceremony on the burned strand. Every 10 years.",
  GAEL + "\n" + VIS + "\neir_norse_holds_irish_county_trigger = yes",
  """add_prestige = major_prestige_gain
add_dread = minor_dread_gain
eir_grant_claims_norse_effect = yes
add_character_modifier = { modifier = eir_longphort_burner_modifier years = 12 }
trigger_event = eir.0555
trigger_event = { id = eir.0413 years = 2 }""",
  valid=req(S2, "is_at_war = no", "eir_norse_holds_irish_county_trigger = yes", "OR = {\nhas_global_variable = eir_black_host_broken\nhas_global_variable = eir_bh_ended\nhas_variable = eir_norse_enclave\n}"),
  cost=cost(gold=250, prestige=350), cd=3650, pic="decision_siege_warfare")

D("eir_assimilate_ostmen_decision", "Make Gaels of the Ostmen",
  "A generation of mixed marriages has softened the Norse towns of your coast. Give them hospitality, a church and an Irish name for the town, and let time do the rest.",
  "Needs a Norse-culture county of your own, fosterage and a Gaelic court. Converts one Norse county to your culture, an Ostmen quarter in the capital, fosterage bonds, a chance of the Compassionate trait. Every five years.",
  GAEL + "\n" + VIS + "\neir_holds_norse_county_trigger = yes",
  """random_sub_realm_county = {
	limit = { culture ?= { has_cultural_pillar = heritage_north_germanic } }
	save_scope_as = eir_conv_county
	set_county_culture = root.culture
	add_county_modifier = { modifier = eir_ostmen_quarter_modifier years = 15 }
}
add_prestige = medium_prestige_gain
add_piety = minor_piety_gain
eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 20 }
trigger_event = eir.0556""",
  valid=req(S1, FOSTER, "eir_holds_norse_county_trigger = yes", "is_at_war = no"),
  cost=cost(gold=100, prestige=150), cd=1825, pic="decision_culture")

D("eir_swear_norse_bane_oath_decision", "Swear the Oath of the Norse-Bane",
  "Stand on the strand where the Black Host died, with the relics in your hand, and swear that no raider will land here and live to boast.",
  "Needs the Black Host broken and 150 piety. Norse-Bane Oath modifier for 30 years, a House modifier for 50, the nickname 'Norse-Bane', and the Norse-Bane Axemen (a new men-at-arms type). Once per game.",
  GAEL + "\n" + VIS + "\n" + BHBROKEN + "\n" + not_done("eir_unique_norse_bane_oath"),
  """add_prestige = major_prestige_gain
add_piety = medium_piety_gain
set_global_variable = eir_unlock_norse_bane
set_global_variable = eir_unique_norse_bane_oath
eir_world_reacts_effect = yes
trigger_event = eir.0557""",
  valid=req("piety >= 150", "is_at_war = no"),
  cost=cost(prestige=300, piety=150), cd=36500, major=True, pic="decision_tale")

D("eir_found_walled_town_decision", "Found a Walled Town",
  "The Norse built towns and the Irish burned them. Build one of your own: a bank, a gate, a church, a market and a charter.",
  "Needs a duchy, a harbour, three regional buildings and peace. A chartered, walled capital county for 20 years (taxes, defence, opinion), a town charter for Irish and foreign merchants, and a ceremony. Once per game.",
  GAEL + "\n" + VIS + "\n" + S2 + "\n" + not_done("eir_unique_walled_town"),
  """add_prestige = major_prestige_gain
capital_county ?= { add_county_modifier = { modifier = eir_walled_town_modifier years = 20 } }
add_character_modifier = { modifier = eir_irish_sea_trade_modifier years = 8 }
set_global_variable = eir_unique_walled_town
trigger_event = eir.0558""",
  valid=req(S2, "eir_irish_buildings_trigger = { COUNT = 3 }", "eir_ports_trigger = { N = 1 }", "is_at_war = no"),
  cost=cost(gold=400, prestige=500), cd=36500, major=True, pic="decision_castle_view")

D("eir_raise_fallen_cairn_decision", "Raise the Cairn of the Fallen",
  "Three hundred men did not come home. Every family brings one stone to the strand where it ended, and the names are cut into a slab at the foot.",
  "Needs the Black Host broken. A Cairn modifier on the capital county for 25 years, piety and prestige, opinion with every widow's family, and a place to rally the next war. Once per game.",
  GAEL + "\n" + VIS + "\n" + BHBROKEN + "\n" + not_done("eir_unique_fallen_cairn"),
  """add_piety = medium_piety_gain
add_prestige = medium_prestige_gain
capital_county ?= { add_county_modifier = { modifier = eir_cairn_county_modifier years = 25 } }
eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 4 }
set_global_variable = eir_unique_fallen_cairn
trigger_event = eir.0559""",
  valid=req("is_at_war = no", "eir_realm_size_trigger = { N = 3 }"),
  cost=cost(gold=100, prestige=100), cd=36500, pic="decision_personal_religious")

D("eir_commission_victory_song_decision", "Commission the Victory Song",
  "Five provinces have five stories about the war. Gather their poets and make them agree on one.",
  "Needs the Filí and the Black Host broken. Prestige, a War-Poem modifier for 8 years, a legend, lifestyle XP, and the poets of five provinces in your debt. Once per game.",
  GAEL + "\n" + VIS + "\n" + FILI + "\n" + BHBROKEN + "\n" + not_done("eir_unique_victory_song"),
  """add_prestige = medium_prestige_gain
eir_legend_defence_effect = yes
set_global_variable = eir_unique_victory_song
trigger_event = eir.0560""",
  valid=req(FILI, "eir_realm_size_trigger = { N = 4 }", "is_at_war = no"),
  cost=cost(gold=80, prestige=80), cd=36500, pic="decision_tale")

# =============================================================================
# CONQUEST, TRIUMPH AND CULTURE IN BRITAIN
# =============================================================================
D("eir_hold_triumph_decision", "Hold a Triumph",
  "The old Irish kings took cattle and went home. You are taking cities and staying. March the whole host through a conquered gate and let the conquered watch.",
  "Needs a duchy and three foreign-held counties (Britain or Norse land). Prestige and dread, every foreign county sees a Triumph modifier for 10 years, vassals are impressed and the world answers. Choose to be crowned, to feed the city or to humble the lords. Every 20 years.",
  GAEL + "\n" + VIS + "\neir_foreign_conquests_trigger = { N = 2 }",
  CONQ + """
add_prestige = massive_prestige_gain
add_dread = minor_dread_gain
eir_triumph_glory_effect = yes
set_global_variable = eir_done_triumph
trigger_event = eir.0500""",
  valid=req(S2, "eir_foreign_conquests_trigger = { N = 3 }", "is_at_war = no"),
  cost=cost(gold=200, prestige=400), cd=7300, major=True, pic="decision_golden_age")

D("eir_raise_conquest_cairn_decision", "Raise a Victory Cairn",
  "Each man who fought carries one stone to the hill above the conquered town. In a hundred years it will be a hill of its own.",
  "Needs one foreign-held county. A Cairn modifier on that county for 20 years, piety and prestige, and a monument the poets can rally round. Every five years.",
  GAEL + "\n" + VIS + "\neir_foreign_conquests_trigger = { N = 1 }",
  CONQ + """
add_prestige = minor_prestige_gain
add_piety = minor_piety_gain
trigger_event = eir.0501""",
  valid=req("eir_foreign_conquests_trigger = { N = 1 }", "is_at_war = no"),
  cost=cost(gold=60, prestige=100), cd=1825, pic="decision_siege_warfare")

D("eir_plant_colonists_decision", "Plant Gaelic Colonists",
  "The conquered county is full of foreigners and empty of Gaels. Ship in three hundred families from the crowded septs of Antrim and Kerry, and let a generation turn them into neighbours.",
  "Needs a chieftain and a foreign-held county. A Settlers modifier now, and eight years later the county turns to your culture, with a ceremony each time. Less hasty than Reclaim the Tongue: more resentment, but permanent. Every five years.",
  GAEL + "\n" + VIS + "\neir_foreign_conquests_trigger = { N = 1 }",
  CONQ + """
scope:eir_conq_county = {
	add_county_modifier = { modifier = eir_gaelic_settlers_modifier years = 12 }
	save_scope_as = eir_colony
}
set_variable = {
	name = eir_colony_county
	value = scope:eir_conq_county
}
add_prestige = minor_prestige_gain
trigger_event = eir.0502
trigger_event = { id = eir.0503 years = 8 }""",
  valid=req(S1, "eir_foreign_conquests_trigger = { N = 1 }", "is_at_war = no", "NOT = { has_variable = eir_colony_county }"),
  cost=cost(gold=120, prestige=150), cd=1825, pic="decision_levy_outcasts")

D("eir_feast_of_three_peoples_decision", "Hold the Feast of the Three Peoples",
  "Seat the Gael, the Briton and the Saxon at the same table, and keep the knives in their sheaths until the third course.",
  "Needs the Celtic Brotherhood and a county in Britain. Prestige, a Two Peoples modifier for 10 years, resentment cleared, lifestyle XP, and the world watches. The feast may end badly if the host cannot keep the peace. Every 10 years.",
  GAEL + "\n" + VIS + "\n" + BROTH,
  """add_prestige = medium_prestige_gain
trigger_event = eir.0504""",
  valid=req(BROTH, "OR = {\neir_has_foreign_britain_counties_trigger = yes\neir_has_celtic_britain_counties_trigger = yes\n}", "is_at_war = no"),
  cost=cost(gold=250, prestige=300), cd=3650, pic="decision_activity")

D("eir_lebor_gabala_decision", "Commission the Book of Conquests",
  "The poets say the Gaels came out of Spain eight sons strong and took the island from the giants. Have the whole story written down, with your name at the end of it.",
  "Needs a duchy, the Filí and a learned ruler or an Ollamh. Prestige, a Book of Conquests modifier for 15 years, a legend, and pressed claims on English land from the genealogies. The poets will have improved the facts. Once per game.",
  GAEL + "\n" + VIS + "\n" + FILI + "\n" + not_done("eir_unique_book_conquests"),
  """add_prestige = major_prestige_gain
eir_legend_title_effect = { TITLE = primary_title }
eir_grant_claims_non_celtic_effect = { TITLE = k_england }
set_global_variable = eir_unique_book_conquests
trigger_event = eir.0505""",
  valid=req(S2, FILI, "OR = {\nlearning >= 12\nany_courtier = { has_trait = eir_ollamh }\n}", "is_at_war = no"),
  cost=cost(gold=150, prestige=400, piety=50), cd=36500, major=True, pic="decision_tale")

D("eir_proclaim_insular_union_decision", "Proclaim the Insular Union",
  "Gael, Briton and Pict are cousins who forgot it. Call their kings to the middle of the sea, put them in the same hall and swear a union that no king may break alone.",
  "Needs a kingdom, the Celtic Brotherhood, three reclaimed counties in Britain, six Celtic counties and little resentment. Adds the Union of the Insular Celts tradition to your culture, an Insular Union modifier for 30 years, the Insular Spearmen (a new men-at-arms), welcome of Welsh and Alban rulers, and a ceremony. Once per game.",
  GAEL + "\n" + VIS + "\n" + BROTH + "\n" + not_done("eir_done_union"),
  """add_prestige = massive_prestige_gain
add_piety = medium_piety_gain
eir_add_tradition_effect = { TRADITION = tradition_eir_insular_union }
set_global_variable = eir_done_union
set_global_variable = eir_unlock_insular_spears
eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }
eir_world_reacts_effect = yes
trigger_event = eir.0506""",
  valid=req(S3, BROTH, "eir_celtic_britain_counties_trigger = { N = 6 }", "var:eir_recelt >= 3", "is_at_war = no"),
  cost=cost(gold=500, prestige=1500, piety=250), cd=36500, major=True, pic="decision_found_kingdom")

D("eir_found_island_kingdom_decision", "Crown the King of the Island of the Mighty",
  "A crown for a kingdom that has never existed: the whole island, from Cape Wrath to Land's End, ruled from a hall on Man where the laws are read aloud once a year.",
  "Needs the Insular Union, a kingdom, six Celtic counties in Britain and the Isle of Man. Creates the Kingdom of the Island of the Mighty, a 40-year Island Crown modifier, the nickname 'Island-King', a legend and a coronation ceremony. Once per game.",
  GAEL + "\n" + VIS + "\n" + UNION + "\n" + not_done("eir_unique_island_kingdom"),
  """eir_create_title_effect = { TITLE = k_eir_ynys_prydain }
add_prestige = massive_prestige_gain
eir_legend_title_effect = { TITLE = k_eir_ynys_prydain }
set_global_variable = eir_unique_island_kingdom
trigger_event = eir.0509""",
  valid=req(S3, UNION, "eir_can_create_island_kingdom_trigger = yes", "NOT = { exists = title:k_eir_ynys_prydain.holder }", "is_at_war = no"),
  cost=cost(gold=700, prestige=2000, piety=300), cd=36500, major=True, pic="decision_found_kingdom")

D("eir_secure_bridgehead_decision", "Secure a Bridgehead in Britain",
  "Send forty men, a priest and two carpenters across the sea to a quiet cove on the British coast. In three days they will have a palisade. In a year, you may have a war.",
  "Needs a chieftain and two ports. Claims on a foreign coastal county, a free landing party there, supply modifiers for the crossing, and a ceremony. Every ten years.",
  GAEL + "\n" + VIS + "\neir_ports_trigger = { N = 2 }",
  """eir_grant_claims_non_celtic_effect = { TITLE = k_england }
add_prestige = minor_prestige_gain
trigger_event = eir.0510""",
  valid=req(S1, "eir_ports_trigger = { N = 2 }", "is_at_war = no", "current_year >= 868"),
  cost=cost(gold=150, prestige=200), cd=3650, pic="decision_siege_warfare")

D("eir_foster_british_princes_decision", "Foster the Sons of the British Princes",
  "Fosterage is how the Irish make peace. Ask the princes of Wales and Cornwall for a son each, and raise them as your own.",
  "Needs fosterage and the Celtic Brotherhood. Foster-Brother bonds for 15 years, Welsh opinion, a Welsh tongue at court, and three hostages who may one day become allies. Every ten years.",
  GAEL + "\n" + VIS + "\n" + BROTH + "\n" + FOSTER,
  """add_prestige = medium_prestige_gain
trigger_event = eir.0511""",
  valid=req(BROTH, FOSTER, "is_at_war = no"),
  cost=cost(gold=100, prestige=200), cd=3650, pic="decision_social")

D("eir_raid_saxon_coast_decision", "Raid the Saxon Coast",
  "A dozen boats, a night landing and a monastery with a lot of silver. The old kings would have been proud, and the new bishops will complain.",
  "Needs a chieftain and two ports. Gold and prestige from the plunder, dread, a Raider's Infamy modifier, and a one-in-three chance that the English or Britons answer with a landing a year later. Every three years.",
  GAEL + "\n" + VIS + "\neir_ports_trigger = { N = 2 }",
  """add_prestige = minor_prestige_gain
add_dread = minor_dread_gain
add_character_modifier = { modifier = eir_raider_infamy_modifier years = 3 }
random = {
	chance = 33
	trigger_event = { id = eir.0410 years = 1 }
}
trigger_event = eir.0513""",
  valid=req("eir_ports_trigger = { N = 2 }", "is_at_war = no", "current_year >= 868"),
  cost=cost(gold=60), cd=1095, pic="decision_recruitment")

D("eir_acclaim_conquered_capital_decision", "Be Acclaimed in a Conquered Capital",
  "A city that was your enemy's is singing your praises in its cathedral. Let the bishop crown the moment, and take the title the city offers.",
  "Needs a Triumph, a kingdom and five foreign-held counties. Prestige, piety, a Conqueror Crowned modifier for 20 years, every foreign county sees a Triumph modifier, and the world notices. Once per game.",
  GAEL + "\n" + VIS + "\n" + "has_global_variable = eir_done_triumph" + "\n" + not_done("eir_unique_acclaimed"),
  CONQ + """
add_prestige = massive_prestige_gain
add_piety = medium_piety_gain
eir_triumph_glory_effect = yes
set_global_variable = eir_unique_acclaimed
trigger_event = eir.0514""",
  valid=req(S3, "eir_foreign_conquests_trigger = { N = 5 }", "is_at_war = no"),
  cost=cost(prestige=800, piety=150), cd=36500, major=True, pic="decision_golden_age")

D("eir_open_sea_road_decision", "Open the Sea-Road to Alba",
  "The sea between Antrim and Kintyre can be crossed in a day, if two quays and a chain of beacons are kept. Pay for them, and charge for the crossing.",
  "Needs three ports and a British harbour of your own. A Sea-Road modifier for 15 years (trade and travel), beacons along the coast, pilgrims and merchants on both shores, and a ceremony. Once per game.",
  GAEL + "\n" + VIS + "\n" + not_done("eir_unique_sea_road"),
  """add_prestige = medium_prestige_gain
add_character_modifier = { modifier = eir_sea_road_modifier years = 15 }
every_realm_county = {
	limit = { is_coastal_county = yes }
	add_county_modifier = { modifier = eir_beacon_county_modifier years = 10 }
}
set_global_variable = eir_unique_sea_road
trigger_event = eir.0515""",
  valid=req(S1, "eir_ports_trigger = { N = 3 }", "eir_holds_british_port_trigger = yes", "is_at_war = no"),
  cost=cost(gold=250, prestige=250), cd=36500, pic="decision_spend_money")

# =============================================================================
# KINGS AGAINST KINGS
# =============================================================================
D("eir_produce_genealogy_decision", "Produce the Genealogy",
  "A good claim needs a good ancestor. Have the chief poet write down yours, back to a high king of the seventh century, and read it before a rival's poets can.",
  "Needs the Filí. Pedigree modifier for 10 years, prestige, a Genealogy ceremony, and pressed claims on Norse-held land. The poets will improve the facts; a rival's poets may notice. Every ten years.",
  GAEL + "\n" + VIS + "\n" + FILI,
  """add_prestige = medium_prestige_gain
trigger_event = eir.0561""",
  valid=req(S1, FILI, "is_at_war = no"),
  cost=cost(gold=100, prestige=150), cd=3650, pic="decision_tale")

D("eir_demand_rival_hostages_decision", "Demand Hostages from a Rival",
  "A rival king's sons in your hall are better than a rival king's armies in your field. Send for them, and explain why.",
  "Needs a duchy, the Óenach and 700 prestige. Two hostages in your hall, a Hostage Peace modifier, dread, and a rival who hates you more. They may be treated as guests, fostered or locked in a tower. Every ten years.",
  GAEL + "\n" + VIS + "\n" + S2,
  """add_prestige = medium_prestige_gain
add_dread = minor_dread_gain
trigger_event = eir.0562""",
  valid=req(S2, OENACH, "prestige >= 700", "is_at_war = no", "eir_has_gael_neighbour_trigger = yes"),
  cost=cost(gold=100, prestige=250), cd=3650, pic="decision_prison")

D("eir_judge_kings_quarrel_decision", "Sit in Judgement on a Quarrel",
  "Two septs have a quarrel nobody else can settle. Take the high seat and rule on it, with the brehons at your elbows.",
  "Needs three vassals and the Great Óenach, and costs only a little prestige because the gate is already hard. Vassal opinion, the Just trait, a Fair Lord modifier, and a precedent. Every three years.",
  GAEL + "\n" + VIS + "\n" + OENACH,
  """add_prestige = minor_prestige_gain
trigger_event = eir.0563""",
  valid=req(S2, "any_vassal = { count >= 3 }", "is_at_war = no"),
  cost=cost(prestige=50), cd=1095, pic="decision_legitimacy")

D("eir_end_blood_feud_decision", "End the Blood Feud",
  "You swore to avenge a death, and the vow has become a stone round your neck. Offer the eric, and let both houses sit at one table.",
  "Shown when you have a vow of vengeance. Pays the eric, clears the vow, Honour Restored for 10 years, a Wergild Peace modifier and the chance of the Just trait. The remedy for the cattle-raids and vengeance events; it leaves you better than before. Every five years.",
  GAEL + "\n" + VIS + "\nhas_character_flag = eir_vowed_vengeance",
  """remove_character_flag = eir_vowed_vengeance
add_prestige = medium_prestige_gain
add_character_modifier = { modifier = eir_honour_restored_modifier years = 10 }
trigger_event = eir.0564""",
  valid=req("has_character_flag = eir_vowed_vengeance", "is_at_war = no"),
  cost=cost(gold=150, piety=40), cd=1825, pic="decision_social")

D("eir_royal_stud_decision", "Establish the Royal Stud",
  "Irish hobbies are small, quick and sure-footed. Buy a famous stallion, mares from three provinces and a man who talks to horses.",
  "Needs a duchy. A Royal Stud modifier for 15 years (cavalry strength and prestige), the foals of the stud for your vassals, and trade in horses with England. Once per game.",
  GAEL + "\n" + VIS + "\n" + not_done("eir_unique_royal_stud"),
  """add_prestige = minor_prestige_gain
set_global_variable = eir_unique_royal_stud
trigger_event = eir.0565""",
  valid=req(S1, "is_at_war = no"),
  cost=cost(gold=200, prestige=150), cd=36500, pic="decision_recruitment")

D("eir_codify_kinship_decision", "Codify the Law of Kinship",
  "The Gaels of Alba hold that a man is his kindred. Have the elders write down who is a kinsman, who owes what, and who pays for a death.",
  "Replaces Strong Kinship with the Law of Kinship (keeps every parameter, adds more). Needs a duchy and the Strong Kinship tradition. House opinion and dynasty prestige, a new war-law clause, and a ceremony. Once per game.",
  GAEL + "\n" + VIS + "\nculture ?= { has_cultural_tradition = tradition_strong_kinship }",
  """eir_upgrade_tradition_effect = { OLD = tradition_strong_kinship NEW = tradition_eir_kinship_law }
add_prestige = major_prestige_gain
set_global_variable = eir_unique_kinship_law
trigger_event = eir.0566""",
  valid=req(S2, "culture = { has_cultural_tradition = tradition_strong_kinship }", not_done("eir_unique_kinship_law"), "is_at_war = no"),
  cost=cost(gold=250, prestige=700, piety=100), cd=36500, major=True, pic="decision_dynasty_house")

D("eir_codify_clan_war_decision", "Codify the Law of the Sword and the Clan",
  "The war-leaders of the Highlands have a custom for everything: how a clan musters, who leads, how spoil is divided. Put it in writing.",
  "Replaces Highland Warriors with the Law of the Sword and the Clan (keeps every parameter, adds more). Needs a duchy and the Highland Warriors tradition. Knight strength, war-law clauses, a cheaper army and a ceremony. Once per game.",
  GAEL + "\n" + VIS + "\nculture ?= { has_cultural_tradition = tradition_highland_warriors }",
  """eir_upgrade_tradition_effect = { OLD = tradition_highland_warriors NEW = tradition_eir_clan_war_law }
add_prestige = major_prestige_gain
set_global_variable = eir_unique_clan_war_law
trigger_event = eir.0567""",
  valid=req(S2, "culture = { has_cultural_tradition = tradition_highland_warriors }", not_done("eir_unique_clan_war_law"), "is_at_war = no"),
  cost=cost(gold=250, prestige=700, piety=100), cd=36500, major=True, pic="decision_recruitment")
