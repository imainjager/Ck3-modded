"""Eire Reborn decisions, v0.5 rewrite.

Rules (from the user):
  * nothing is clickable at game start: every decision sits behind a progression stage (realm size, titles,
    buildings built, earlier accomplishments);
  * costs are real (explicit gold, prestige, piety), because gold_value script values scale with income and
    are tiny for a tribal chieftain;
  * rewards match the effort: several effects at once, an unlock, a follow-up event, and often a downside;
  * traditions are never added, only UPGRADED (remove the vanilla Irish one, add the Eire one).
"""
from gen_decisions import D, IRISH

S1 = "eir_stage1_trigger = yes"
S2 = "eir_stage2_trigger = yes"
S3 = "eir_stage3_trigger = yes"
S4 = "eir_stage4_trigger = yes"
VIS = "eir_visible_stage1_trigger = yes"
FILI = "has_global_variable = eir_done_fili"
OENACH = "has_global_variable = eir_done_oenach"
CASHEL = "has_global_variable = eir_done_cashel"
BROTHER = "has_global_variable = eir_done_brotherhood"
MONK = "has_global_variable = eir_done_monastery"


def has_trad(t):
    return "culture = { has_cultural_tradition = %s }" % t


def blds(n):
    return "eir_irish_buildings_trigger = { COUNT = %d }" % n


def cost(gold=0, prestige=0, piety=0):
    out = []
    if gold:
        out.append("gold = %d" % gold)
    if prestige:
        out.append("prestige = %d" % prestige)
    if piety:
        out.append("piety = %d" % piety)
    return "\n".join(out)


def req(*lines):
    return "\n".join(l for l in lines if l)


# =============================================================================
# A. KINGSHIP
# =============================================================================
D("eir_hold_oenach_decision", "Hold the Great Óenach",
  "Summon the lords, poets, judges and champions of your people to a great assembly, with games, feasting and the settling of old quarrels. Only a ruler with a real realm, a hall to feast them in and vassals worth inviting can pull it off.",
  "Needs a duchy, 10 counties, an Irish building, three vassals. Opinion with every vassal, a county festival site, legitimacy-style prestige, and the way to Tara opens.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_oenach_afterglow_modifier years = 6 }
eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 12 }
capital_county ?= { add_county_modifier = { modifier = eir_oenach_ground_modifier years = 12 } }
if = {
	limit = { has_character_modifier = eir_throne_turmoil_modifier }
	remove_character_modifier = eir_throne_turmoil_modifier
}
add_prestige = 300
add_piety = 50
set_global_variable = eir_done_oenach
trigger_event = { id = eir.0051 days = 30 }""",
  valid=req(S2, blds(1), "any_vassal = { count >= 3 }", "NOT = { has_character_modifier = eir_oenach_afterglow_modifier }"),
  cost=cost(gold=350, prestige=350), cd=5475, pic="decision_activity")

D("eir_rebuild_tara_hall_decision", "Rebuild the Hall of Tara",
  "The Hill of Tara has been empty for centuries, a ring of banks and a standing stone. Raise a new hall of oak and thatch there, big enough for the kings of Ireland to sit in rank. It will take years and every cow you can spare.",
  "Needs the Duchy of Meath, the Óenach held and three Irish buildings. Unlocks the Hall of Tara special building and the road to the High Kingship.",
  IRISH + "\n" + VIS,
  """eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hall_modifier YEARS = 40 }
eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hill_modifier YEARS = 25 }
add_character_modifier = { modifier = eir_tara_vigil_modifier years = 12 }
add_prestige = 400
set_global_variable = eir_done_tara_hall""",
  valid=req(S2, OENACH, "has_title = title:d_meath", blds(3), "NOT = { has_global_variable = eir_done_tara_hall }"),
  cost=cost(gold=800, prestige=700), cd=36500, major=True, pic="decision_found_kingdom")

D("eir_crowned_at_tara_decision", "Be Crowned at Tara",
  "Ireland has had a thousand kings and a handful of High Kings. Only a ruler who holds the great duchies, sits in the rebuilt Hall, and can feed a hundred kings' retinues has a chance to be crowned on the Lia Fáil.",
  "Needs Meath and another duchy, the Hall of Tara, the Óenach and 20 counties. Creates the Kingdom of Ireland, the Ard Rí trait, the stone's blessing and a legend.",
  IRISH + "\n" + VIS,
  """eir_create_title_effect = { TITLE = k_ireland }
if = {
	limit = { NOT = { has_trait = eir_ard_ri } }
	add_trait = eir_ard_ri
}
add_character_modifier = { modifier = eir_ard_ri_modifier years = 25 }
add_character_modifier = { modifier = eir_lia_fail_blessing_modifier years = 10 }
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 40 } }
add_prestige = 1000
add_piety = 100
set_global_variable = eir_done_crowned
eir_legend_title_effect = { TITLE = title:k_ireland }
trigger_event = { id = eir.0110 days = 7 }""",
  valid=req(S3, "eir_holds_irish_duchies_trigger = { COUNT = 2 }", "has_global_variable = eir_done_tara_hall", OENACH,
            "is_independent_ruler = yes", "has_title = title:d_meath",
            "OR = {\n\thas_title = title:k_ireland\n\tNOT = { exists = title:k_ireland.holder }\n}"),
  cost=cost(gold=1500, prestige=1500), cd=7300, major=True, pic="decision_found_kingdom")

D("eir_end_fragmentation_decision", "End the Tanistic Fragmentation",
  "For centuries a king's realm died with him. The High King can end it: have the vassals swear that the high kingship passes to a single heir, as in the feudal courts overseas, and build a guard that will defend the heir against every cousin.",
  "Needs the High Kingship, the Circuit, the Provincial Oath, a feudal government and 25 counties. Abolishes the death of top titles, adds Stable High Kingship, unlocks the Guard of Tara.",
  IRISH + "\n" + S4 + "\nhas_global_variable = eir_done_crowned\neir_collapse_active_trigger = yes",
  """culture ?= {
	if = {
		limit = { has_cultural_tradition = tradition_eir_tanistic_fragmentation }
		remove_culture_tradition = tradition_eir_tanistic_fragmentation
	}
	if = {
		limit = { NOT = { has_cultural_tradition = tradition_eir_high_kingship } }
		add_culture_tradition = tradition_eir_high_kingship
	}
}
set_global_variable = eir_collapse_abolished
set_global_variable = eir_unlock_tara_guard
add_character_modifier = { modifier = eir_peace_of_tara_modifier years = 25 }
add_prestige = 1500
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 80 } }
trigger_event = { id = eir.0110 days = 7 }""",
  valid=req("government_has_flag = government_is_feudal", "eir_holds_irish_counties_trigger = { COUNT = 25 }", "is_independent_ruler = yes",
            "has_global_variable = eir_done_circuit", "has_global_variable = eir_done_oath"),
  cost=cost(gold=2000, prestige=3000), cd=36500, major=True, pic="decision_golden_age")

D("eir_circuit_of_ireland_decision", "Ride the Circuit of Ireland",
  "A king who is never seen is soon forgotten. Ride through your lands with your household for a season, eat at every lord's table, judge their quarrels in person and be seen.",
  "Needs a kingdom, the Óenach and peace. Every county gets a royal-visit bonus, vassals warm to you, chance of the Peacemaker of Tara trait. Starts the 'Circuit' incident.",
  IRISH + "\n" + VIS,
  """every_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_circuit_visit_modifier years = 6 }
}
add_character_modifier = { modifier = eir_royal_circuit_modifier years = 10 }
eir_vassal_opinion_effect = { MODIFIER = eir_circuit_host_opinion OPINION = 10 }
eir_trait_effect = { TRAIT = eir_peacemaker_of_tara OPPOSITE = wrathful CHANCE = 25 }
add_prestige = 200
set_global_variable = eir_done_circuit
trigger_event = { id = eir.0160 days = 45 }""",
  valid=req(S3, OENACH, "is_at_war = no"),
  cost=cost(gold=400, prestige=300), cd=3650, pic="decision_activity")

D("eir_provincial_oath_decision", "Take the Oath of the Provincial Kings",
  "Gather the great lords at the old place and have them swear on the relics, one by one, that they will follow you.",
  "Needs a kingdom and the Óenach. Dukes and above swear to you; legitimacy and levies grow. Required for ending the Fragmentation.",
  IRISH + "\n" + VIS,
  """every_vassal = {
	limit = { highest_held_title_tier >= tier_duchy }
	add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 20 }
}
add_character_modifier = { modifier = eir_provincial_oath_modifier years = 15 }
add_prestige = 250
set_global_variable = eir_done_oath""",
  valid=req(S3, OENACH, "any_vassal = {\n\thighest_held_title_tier >= tier_duchy\n\tcount >= 2\n}"),
  cost=cost(gold=400, prestige=400), cd=7300, pic="decision_legitimacy")

D("eir_feis_of_tara_decision", "Hold the Feis of Tara",
  "The Feis is the oldest festival of kingship: a week of feasting, law and marriage on the Hill of Tara, last held in the days before the Church.",
  "Needs the Hall of Tara, the Circuit and the Oath, and the High Kingship. Great prestige, a long glow, and a feast event.",
  IRISH + "\n" + S4,
  """add_character_modifier = { modifier = eir_feis_modifier years = 12 }
add_prestige = 600
eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 12 }
trigger_event = { id = eir.0051 days = 20 }""",
  valid=req("has_global_variable = eir_done_tara_hall", "has_global_variable = eir_done_circuit", "has_global_variable = eir_done_oath"),
  cost=cost(gold=1500, prestige=1200), cd=7300, major=True, pic="decision_golden_age")

D("eir_boramha_decision", "Demand the Bóramha Tribute",
  "The High King's right to the cow-tribute of Leinster is ancient, and unpopular. Send the collectors.",
  "A great sum of gold now, vassal resentment for eight years. Remit it later.",
  IRISH + "\n" + S4,
  """add_gold = major_gold_value
add_character_modifier = { modifier = eir_boramha_collected_modifier years = 8 }
eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -12 }
add_prestige = 50""",
  valid="NOT = { has_character_modifier = eir_boramha_collected_modifier }", cd=5475, pic="decision_spend_money")

D("eir_remit_tribute_decision", "Remit the Cow Tribute",
  "Forgive this year's cows. The vassals will remember, and the poets will say so.",
  "Removes the Bóramha modifier and mends opinion.",
  IRISH + "\nhas_character_modifier = eir_boramha_collected_modifier",
  """remove_character_modifier = eir_boramha_collected_modifier
eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 15 }
add_prestige = 50""", cost=cost(prestige=100), cd=1825, pic="decision_social")

D("eir_take_hostages_decision", "Take the Hostages of Tara",
  "Every Irish king knows that the surest oath is a son at the king's table. Ask each of your vassals for one.",
  "Needs a duchy and the Óenach. Prestige and a tight leash, but vassals resent you. Release them later with another decision.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_hostages_modifier years = 12 }
eir_vassal_opinion_effect = { MODIFIER = eir_hostage_taken_opinion OPINION = -12 }
add_prestige = 150""",
  valid=req(S2, OENACH, "any_vassal = { count >= 3 }", "NOT = { has_character_modifier = eir_hostages_modifier }"), cd=3650, pic="decision_prison")

D("eir_release_hostages_decision", "Release the Hostages",
  "The sons have grown. Send them home with gifts and an oath.",
  "Removes the Hostages modifier and mends vassal opinion. A freed hostage may become a loyal Fosterling.",
  IRISH + "\nhas_character_modifier = eir_hostages_modifier",
  """remove_character_modifier = eir_hostages_modifier
eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 12 }
add_prestige = 50
trigger_event = { id = eir.0170 days = 30 }""", cost=cost(gold=150), cd=1825, pic="decision_social")

D("eir_foster_heir_decision", "Foster Your Children Among Your Vassals",
  "A noble child raised in another lord's hall is bound to him by a tie stronger than blood. Send your children out, and take theirs in, and the great houses are knitted together.",
  "Needs 4 counties and three vassals. Vassals bond to you for 15 years; unlocks the Fosterage Hall building; a child may become a Foster-Brother.",
  IRISH + "\nany_child = { age >= 4 age < 15 is_alive = yes }",
  """add_character_modifier = { modifier = eir_foster_ties_modifier years = 15 }
add_character_modifier = { modifier = eir_naming_customs_modifier years = 15 }
eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 15 }
random_child = {
	limit = { age >= 4 age < 15 is_alive = yes }
	eir_trait_effect = { TRAIT = eir_foster_brother OPPOSITE = eir_foster_brother CHANCE = 60 }
}
add_prestige = 100
set_global_variable = eir_done_fosterage""",
  valid=req(S1, "any_vassal = { count >= 3 }", "NOT = { has_character_modifier = eir_foster_ties_modifier }"),
  cost=cost(gold=100, prestige=150), cd=5475, pic="decision_dynasty_house")

D("eir_name_tanaiste_decision", "Name Your Tánaiste",
  "Name your successor-in-waiting while you live, and the family will argue a little less when you are gone.",
  "Needs a living heir and a duchy. Legitimacy and vassal opinion; the heir is bound to you.",
  IRISH + "\nexists = primary_heir",
  """add_character_modifier = { modifier = eir_tanaiste_modifier years = 15 }
primary_heir ?= { add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 30 } }
eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 5 }
add_prestige = 100""", valid=S2, cost=cost(gold=150, prestige=300), cd=7300, pic="decision_dynasty_house")

D("eir_strike_claim_decision", "Strike a Claimant from the List",
  "A tanistry list is a list of everyone who might be king. There is a quiet way to make it shorter.",
  "A vassal loses his claim and hates you for it. Mend it by naming a Tánaiste.",
  IRISH + "\n" + VIS,
  """random_vassal = {
	add_opinion = { target = root modifier = eir_claim_revoked_opinion opinion = -30 }
}
add_character_modifier = { modifier = eir_tanistry_dispute_modifier years = 8 }
add_character_modifier = { modifier = eir_blinded_modifier years = 8 }
add_prestige = 75""", valid=req(S1, "any_vassal = { count >= 2 }"), cd=1825, pic="decision_prison")

D("eir_cain_tribute_decision", "Levy the Cáin Tribute",
  "Every free man owes his king a calf from the herd. Send out the collectors.",
  "Income now, vassal resentment for years. The Waive the Cáin decision undoes it.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_cain_tribute_modifier years = 8 }
add_gold = medium_gold_value
add_gold = medium_gold_value""", valid=req(S2, "NOT = { has_character_modifier = eir_cain_tribute_modifier }"), cd=1825, pic="decision_spend_money")

D("eir_waive_cain_decision", "Waive the Cáin",
  "Forgive this year's calves. The people will remember.",
  "Removes the Cáin Tribute modifier and mends opinion.",
  IRISH + "\nhas_character_modifier = eir_cain_tribute_modifier",
  """remove_character_modifier = eir_cain_tribute_modifier
eir_vassal_opinion_effect = { MODIFIER = eir_wergild_paid_opinion OPINION = 8 }
add_prestige = 50""", cost=cost(prestige=75), cd=1825, pic="decision_social")

D("eir_name_ollamh_decision", "Name an Ollamh Rígh",
  "The Ollamh Rígh is the royal chief poet, who remembers every king, every battle and every debt, and whose praise or satire can make or break a reign.",
  "Needs a duchy, the Filí's patronage and a learned ruler or an Ollamh in court. Learning and prestige for twenty years; chance of the Poet-Prince trait.",
  IRISH + "\n" + FILI + "\nNOT = { has_character_modifier = eir_royal_ollamh_modifier }",
  """add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 20 }
add_character_modifier = { modifier = eir_harper_modifier years = 20 }
if = {
	limit = { learning >= 12 }
	eir_trait_effect = { TRAIT = eir_poet_prince OPPOSITE = lazy CHANCE = 35 }
}
add_prestige = 200""",
  valid=req(S2, "OR = {\n\tlearning >= 12\n\tany_courtier = { has_trait = eir_ollamh }\n}"), cost=cost(gold=400, prestige=300), cd=7300, pic="decision_tale")

D("eir_call_slogad_decision", "Call a Slógad",
  "The sluagh-hosting is the oldest duty of free men: when the king calls, every farmer brings a spear and a week's meal. Call it too often and they stay home.",
  "Needs a duchy and peace. A free defensive army, a Great Hosting modifier; vassals grumble.",
  IRISH + "\n" + VIS,
  """eir_defender_levy_effect = yes
add_character_modifier = { modifier = eir_hosting_modifier years = 4 }
add_character_modifier = { modifier = eir_yew_bows_modifier years = 4 }
eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -5 }
add_prestige = 50""", valid=req(S2, "is_at_war = no"), cost=cost(gold=250, prestige=400), cd=7300, pic="decision_recruitment")

# =============================================================================
# B. CULTURE AND THE FOUR UPGRADE TRADITIONS (these REPLACE vanilla Irish traditions)
# =============================================================================
D("eir_patronise_fili_decision", "Patronise the Filí",
  "Poets are the memory and the conscience of Ireland. A king who feeds them is praised in every hall; one who does not is satirised. Open your hall, feed the schools and pay the master-poets.",
  "Needs 4 counties and a learned ruler or poet at court. Prestige, an Ollamh at court, and the first step toward the Schools of the Filí.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_fili_patron_modifier years = 10 }
add_prestige = 150
set_global_variable = eir_done_fili
random_courtier = {
	limit = { is_adult = yes learning >= 8 NOT = { has_trait = eir_ollamh } }
	add_trait = eir_ollamh
}""",
  valid=req(S1, "OR = {\n\tlearning >= 8\n\tany_courtier = { learning >= 10 }\n}", "NOT = { has_character_modifier = eir_fili_patron_modifier }"),
  cost=cost(gold=150, prestige=150), cd=3650, pic="decision_tale")

D("eir_found_bardic_schools_decision", "Charter the Schools of the Filí",
  "The Filí teach twelve years in the great schools: law, genealogy, history, satire. Give them a charter, endow their schools in every province, and the old tradition of poetry becomes a national institution.",
  "REPLACES the Poetry tradition with Schools of the Filí (keeps all its effects, adds more). Needs a duchy, learned ruler, the Filí's patronage and 3 Irish buildings. Unlocks Fianna warbands, Kern javelineers and the Bardic School building.",
  IRISH + "\n" + VIS,
  """eir_upgrade_tradition_effect = { OLD = tradition_poetry NEW = tradition_eir_bardic_schools }
set_global_variable = eir_unlock_bardic_school
set_global_variable = eir_unlock_fianna
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_poets_modifier years = 40 } }
add_character_modifier = { modifier = eir_tale_finn_modifier years = 10 }
add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 10 }
eir_held_county_modifier_effect = { MODIFIER = eir_gaelic_schooling_modifier YEARS = 25 }
add_prestige = 400
trigger_event = { id = eir.0130 days = 60 }""",
  valid=req(S2, FILI, blds(3), "OR = {\n\tlearning >= 12\n\tany_courtier = { has_trait = eir_ollamh }\n}", has_trad("tradition_poetry")),
  cost=cost(gold=600, prestige=900), cd=36500, major=True, pic="decision_culture")

D("eir_compile_brehon_laws_decision", "Compile the Brehon Laws",
  "The ancient laws are held in the heads of the judges. Gather them, write them down, and your courts will judge by a single code.",
  "Needs the Schools of the Filí, 4 Irish buildings and a learned ruler. Unlocks the Brehon Court building, legitimacy and court opinion for 20 years, a chance of the Brehon trait.",
  IRISH + "\n" + VIS,
  """set_global_variable = eir_unlock_brehon_court
add_character_modifier = { modifier = eir_brehon_laws_modifier years = 20 }
if = {
	limit = { learning >= 12 NOT = { has_trait = eir_brehon } }
	add_trait = eir_brehon
}
add_prestige = 250
trigger_event = { id = eir.0040 days = 40 }""",
  valid=req(S2, has_trad("tradition_eir_bardic_schools"), blds(4), "OR = {\n\tlearning >= 12\n\tany_courtier = { has_trait = eir_ollamh }\n}"),
  cost=cost(gold=500, prestige=600), cd=36500, pic="decision_legitimacy")

D("eir_revive_fianna_decision", "Raise the Fianna",
  "In the tales, Fionn's band lived by the hunt and fought like wolves. Gather the best of the young men, give them the forests of the marches and an oath of service, and they will be the best skirmishers in Ireland.",
  "Needs the Schools of the Filí, 3 Irish buildings and a fighter. A free Fianna warband, the Fianna spirit modifier, and chance of the Champion of the Fianna trait.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_fianna_spirit_modifier years = 12 }
add_character_modifier = { modifier = eir_champions_portion_modifier years = 12 }
add_prestige = 300
spawn_army = {
	levies = 0
	men_at_arms = {
		type = eir_fianna_warband
		stacks = 2
	}
	location = capital_province
	origin = capital_province
	inheritable = no
	name = eir_clan_muster_name
}
if = {
	limit = { prowess >= 12 NOT = { has_trait = eir_fennid } }
	add_trait = eir_fennid
}""",
  valid=req(S2, has_trad("tradition_eir_bardic_schools"), blds(3), "OR = {\n\tprowess >= 12\n\tmartial >= 14\n}"),
  cost=cost(gold=500, prestige=500), cd=36500, pic="decision_recruitment")

D("eir_adopt_cattle_wealth_decision", "Codify the Bó-aire",
  "A man's rank is his herd. The bó-aire, the 'cow-freemen', are the backbone of Irish society. Write down who owes whom how many cows, build the pastures and the enclosures, and the old herding tradition becomes the engine of a state.",
  "REPLACES the Pastoralists tradition with Bó-aire: The Cattle Lords. Needs 12 counties, 3 Irish buildings and a shrewd steward. Unlocks the Great Cattle Enclosure, big income, and a chance of the Cattle Lord trait.",
  IRISH + "\n" + VIS,
  """eir_upgrade_tradition_effect = { OLD = tradition_pastoralists NEW = tradition_eir_cattle_wealth }
add_character_modifier = { modifier = eir_cattle_rich_modifier years = 20 }
set_global_variable = eir_unlock_cattle_enclosure
if = {
	limit = { stewardship >= 10 NOT = { has_trait = eir_cattle_lord } }
	add_trait = eir_cattle_lord
}
add_prestige = 300
every_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_cattle_rich_county_modifier years = 15 }
}""",
  valid=req(S2, "eir_realm_size_trigger = { N = 12 }", blds(3), "stewardship >= 10", has_trad("tradition_pastoralists")),
  cost=cost(gold=500, prestige=700), cd=36500, major=True, pic="decision_spend_money")

D("eir_adopt_culdee_decision", "Endow the Monastic Cities",
  "In Ireland the monastery is a city: a thousand monks, a school, a market, a mint, and an abbot who sits among kings. Raise your abbeys to that rank, and the old tradition of monastic communities becomes the heart of the island.",
  "REPLACES the Monastic Communities tradition with Insular Monasticism. Needs 700 piety, a duchy, 3 Irish buildings (including a monastic one) and a monastery of your own. Piety, learning, clergy opinion and a saint's blessing.",
  IRISH + "\n" + VIS,
  """eir_upgrade_tradition_effect = { OLD = tradition_monastic_communities NEW = tradition_eir_culdee_christianity }
add_character_modifier = { modifier = eir_saints_blessing_modifier years = 15 }
add_piety = 400
add_prestige = 200
eir_held_county_modifier_effect = { MODIFIER = eir_monastic_city_modifier YEARS = 30 }""",
  valid=req(S2, "piety >= 700", MONK, blds(3), has_trad("tradition_monastic_communities")),
  cost=cost(gold=500, prestige=400, piety=400), cd=36500, major=True, pic="decision_personal_religious")

D("eir_adopt_sea_kings_decision", "Claim the Irish Sea",
  "The Irish Sea is a road to Chester, Bristol, Man, Wales and the Hebrides, and the Norse have held it too long. Build ports, take a great harbour, fill a fleet, and declare that the sea-kings of Ireland will carry the trade of the west.",
  "REPLACES Maritime Mercantilism with Kings of the Irish Sea. Needs a duchy, 3 ports, a great Irish harbour, 1000 prestige, and wealth (1000 gold) or a trade-wise ruler. Unlocks gallowglass, Irish Sea Quays and Longship Yards, and leads to the Thalassocracy.",
  IRISH + "\n" + VIS,
  """eir_upgrade_tradition_effect = { OLD = tradition_maritime_mercantilism NEW = tradition_eir_sea_kings }
set_global_variable = eir_unlock_sea_trade
set_global_variable = eir_unlock_gallowglass
add_character_modifier = { modifier = eir_sea_king_modifier years = 20 }
add_character_modifier = { modifier = eir_irish_sea_trade_modifier years = 20 }
every_held_title = {
	limit = {
		tier = tier_county
		is_coastal_county = yes
	}
	add_county_modifier = { modifier = eir_wooden_harbour_modifier years = 25 }
}
spawn_army = {
	levies = 0
	men_at_arms = {
		type = eir_gallowglass
		stacks = 1
	}
	location = capital_province
	origin = capital_province
	inheritable = no
	name = eir_gallowglass_company_name
}
add_prestige = 300
trigger_event = { id = eir.0190 days = 30 }""",
  valid=req(S2, "eir_ports_trigger = { N = 3 }", "eir_irish_port_trigger = yes", "prestige >= 1000",
            "OR = {\n\tgold >= 1000\n\tstewardship >= 16\n\thas_trait = shrewd\n}", has_trad("tradition_maritime_mercantilism")),
  cost=cost(gold=700, prestige=800), cd=36500, major=True, pic="decision_spend_money")

D("eir_thalassocracy_decision", "Proclaim the Sea-Kingdom",
  "Dublin, Man, the Isles, the Welsh coast: if one hand held all the harbours of the Irish Sea, it would hold the trade of the west. Build yards on every strand and let the sea-kings call you master.",
  "Needs the Irish Sea tradition, a kingdom, 6 ports, Dublin and two Quays. A sea-empire modifier for 30 years, claims on Man and Norse-held coasts, a legend, and a vast prestige reward.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_thalassocracy_modifier years = 30 }
add_character_modifier = { modifier = eir_island_fleet_modifier years = 30 }
set_global_variable = eir_done_thalassocracy
set_global_variable = eir_unlock_tara_guard
eir_grant_claims_non_celtic_effect = { TITLE = k_mann_the_isles }
eir_grant_claims_norse_effect = yes
every_held_title = {
	limit = {
		tier = tier_county
		is_coastal_county = yes
	}
	add_county_modifier = { modifier = eir_wooden_harbour_modifier years = 30 }
}
add_prestige = 1000
eir_legend_title_effect = { TITLE = primary_title }
trigger_event = { id = eir.0191 days = 30 }""",
  valid=req(S3, has_trad("tradition_eir_sea_kings"), "eir_ports_trigger = { N = 6 }", "any_sub_realm_county = { this = title:c_dublin }",
            "any_sub_realm_county = {\n\tcount >= 2\n\tany_county_province = { has_building = eir_sea_quay_01 }\n}",
            "NOT = { has_global_variable = eir_done_thalassocracy }"),
  cost=cost(gold=1500, prestige=2000), cd=36500, major=True, pic="decision_found_kingdom")

D("eir_gaelic_revival_decision", "The Gaelic Renaissance",
  "The poets, the abbots, the cattle lords and the sea-kings have each made a great thing of their craft. Now bind them together under one king and one language, and let a golden age of the Gael begin.",
  "Needs all four upgraded traditions, the Brehon Laws, a kingdom and 2500 prestige. A thirty-year golden-age modifier, prestige, a legend, and the way to the Empire.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 30 }
add_character_modifier = { modifier = eir_hearth_of_the_gael_modifier years = 30 }
add_character_modifier = { modifier = eir_gaelic_court_modifier years = 30 }
set_global_variable = eir_done_renaissance
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_poets_modifier years = 60 } }
add_prestige = 1500
add_piety = 300
eir_legend_title_effect = { TITLE = primary_title }""",
  valid=req(S3, has_trad("tradition_eir_bardic_schools"), has_trad("tradition_eir_cattle_wealth"), has_trad("tradition_eir_culdee_christianity"),
            has_trad("tradition_eir_sea_kings"), "has_global_variable = eir_unlock_brehon_court", "NOT = { has_global_variable = eir_done_renaissance }"),
  cost=cost(prestige=2500, gold=1000), cd=36500, major=True, pic="decision_golden_age")

D("eir_hold_tailteann_decision", "Hold the Tailteann Games",
  "The funeral games of Tailtiu, held every year in Meath since before memory: races, wrestling, matchmaking, trade and the great peace of the fair.",
  "Needs a duchy and the Óenach. Capital county festival, vassal opinion, prestige.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_tailteann_modifier years = 8 }
capital_county ?= { add_county_modifier = { modifier = eir_tailteann_county_modifier years = 12 } }
eir_held_county_modifier_effect = { MODIFIER = eir_hurling_fields_modifier YEARS = 20 }
eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 8 }
add_prestige = 250""", valid=req(S2, OENACH, "NOT = { has_character_modifier = eir_tailteann_modifier }"),
  cost=cost(gold=400, prestige=250), cd=5475, pic="decision_activity")

D("eir_ancient_sites_decision", "Restore the Ancient Royal Sites",
  "Uisneach, Rathcroghan, Emain Macha and Newgrange were old when the Romans were young. Clear the brush, raise the banks and hold ceremonies, and the kings of the island will remember where kingship began.",
  "Needs the Óenach, 15 counties and 4 Irish buildings. Four ancient-site county modifiers on your lands, prestige, and legend spread.",
  IRISH + "\n" + VIS,
  """eir_held_county_modifier_effect = { MODIFIER = eir_uisneach_modifier YEARS = 30 }
eir_held_county_modifier_effect = { MODIFIER = eir_rathcroghan_modifier YEARS = 30 }
eir_held_county_modifier_effect = { MODIFIER = eir_navan_fort_modifier YEARS = 30 }
eir_held_county_modifier_effect = { MODIFIER = eir_newgrange_modifier YEARS = 30 }
eir_held_county_modifier_effect = { MODIFIER = eir_ogham_stones_modifier YEARS = 30 }
capital_province ?= { add_province_modifier = { modifier = eir_standing_stone_province_modifier years = 30 } }
add_prestige = 400
set_global_variable = eir_done_sites""",
  valid=req(S2, OENACH, "eir_realm_size_trigger = { N = 15 }", blds(4), "NOT = { has_global_variable = eir_done_sites }"),
  cost=cost(gold=700, prestige=500), cd=36500, pic="decision_realm")

D("eir_raise_ringforts_decision", "Raise the Ringforts",
  "Every farm in Ireland sits inside a ringfort: a bank, a ditch and a stockade. Order your lords to build them properly, and teach the people to retreat there when the longships come.",
  "Needs 4 counties. Unlocks Ringfort, Crannóg and Cattle Enclosure buildings, a dún-builder modifier and a hill-fort at your capital.",
  IRISH + "\n" + VIS,
  """set_global_variable = eir_unlock_ringfort
set_global_variable = eir_unlock_crannog
set_global_variable = eir_unlock_cattle_enclosure
add_character_modifier = { modifier = eir_dun_builder_modifier years = 15 }
capital_province ?= { add_province_modifier = { modifier = eir_ringfort_province_modifier years = 30 } }
random_held_title = {
	limit = { tier = tier_county }
	title_province = { add_province_modifier = { modifier = eir_crannog_province_modifier years = 30 } }
}
eir_held_county_modifier_effect = { MODIFIER = eir_ringfort_country_modifier YEARS = 25 }
add_character_modifier = { modifier = eir_dun_drill_modifier years = 8 }
add_prestige = 100""", valid=req(S1, "NOT = { has_global_variable = eir_unlock_ringfort }"), cost=cost(gold=250, prestige=200), cd=36500, pic="decision_castle_view")

D("eir_commission_tale_decision", "Commission a Tale",
  "Your poets know a hundred tales. Choose the one your court will hear all year.",
  "Needs a duchy and the Filí's patronage. Choose among six tales for a different bonus each.",
  IRISH + "\n" + VIS,
  """trigger_event = { id = eir.0150 days = 5 }""", valid=req(S2, FILI), cost=cost(gold=300, prestige=200), cd=3650, pic="decision_tale")

# =============================================================================
# C. WAR, DEFENCE AND THE NORSE
# =============================================================================
D("eir_muster_the_gael_decision", "Muster the Gael",
  "A foreign lord holds Irish soil. Send word to every Irish king: the land will not be theirs for long.",
  "Needs a duchy and peace while a Norse lord holds an Irish county. Pressed claims on up to three Norse-held counties, vassal pride, and a muster.",
  IRISH + "\neir_norse_holds_irish_county_trigger = yes",
  """eir_grant_claims_norse_effect = yes
eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 12 }
eir_defender_levy_effect = yes
add_prestige = 100
set_global_variable = eir_done_muster""", valid=req(S2, "is_at_war = no"), cost=cost(prestige=500, gold=200), cd=1825, pic="decision_recruitment")

D("eir_reclaim_dublin_decision", "Reclaim Dublin",
  "The Norse longphort on the Black Pool has stood for generations. Declare that it belongs to the Gael, and prepare the host that will make it so.",
  "Needs a duchy, 800 prestige and peace while Dublin is Norse. A pressed claim on Dublin.",
  IRISH + "\ntitle:c_dublin = { holder ?= { culture ?= { has_cultural_pillar = heritage_north_germanic } } }",
  """add_pressed_claim = title:c_dublin
add_prestige = 100
set_global_variable = eir_dublin_claimed""", valid=req(S2, "OR = {\n\tprestige >= 800\n\thas_character_flag = eir_oath_to_reclaim\n}", "is_at_war = no"), cost=cost(gold=300, prestige=300), cd=1825, pic="decision_siege_warfare")

D("eir_dublin_reclaimed_decision", "Celebrate the Return of Dublin",
  "The Black Pool is Irish again. Hold a feast on the quays, raise your banners from the old ramparts and let every sea-king know whose harbour this is.",
  "Needs Dublin. A county modifier for 25 years, Norse-scourge reputation, great prestige, chance of Slayer of Norsemen, and Dublin's Quays open.",
  IRISH + "\nhas_title = title:c_dublin\nhas_global_variable = eir_dublin_claimed\nNOT = { has_global_variable = eir_done_dublin }",
  """title:c_dublin = { add_county_modifier = { modifier = eir_dublin_reclaimed_modifier years = 25 } }
add_character_modifier = { modifier = eir_norse_scourge_modifier years = 15 }
add_prestige = 500
eir_trait_effect = { TRAIT = eir_viking_slayer OPPOSITE = eir_viking_slayer CHANCE = 60 }
set_global_variable = eir_done_dublin""", cost=cost(gold=500), cd=36500, pic="decision_golden_age")

D("eir_dublin_garrison_decision", "Garrison Dublin",
  "A fortress on the Liffey is a gift and a burden. Fill it with men who know how to hold it.",
  "Needs Dublin. A gallowglass garrison for twenty years; a Norse champion may soon challenge you.",
  IRISH + "\nhas_global_variable = eir_done_dublin",
  """title:c_dublin ?= { add_county_modifier = { modifier = eir_gallowglass_garrison_modifier years = 20 } }
add_prestige = 100
trigger_event = { id = eir.0151 days = 90 }""", valid=S2, cost=cost(gold=500, prestige=200), cd=7300, pic="decision_castle_view")

D("eir_pay_danegeld_decision", "Pay the Danegeld",
  "Silver is cheaper than blood. Offer the sea-kings a sum to go and raid someone else.",
  "Gold and prestige lost; the raiders leave you alone for eight years, then come back hungrier. End it with another decision.",
  IRISH + "\neir_viking_age_trigger = yes",
  """add_character_modifier = { modifier = eir_danegeld_modifier years = 8 }
add_character_flag = { flag = eir_paid_danegeld years = 8 }
add_prestige = -100""", valid=req(VIS, "NOT = { has_character_flag = eir_paid_danegeld }"), cost=cost(gold=300), cd=3650, pic="decision_spend_money")

D("eir_end_danegeld_decision", "Refuse the Danegeld",
  "The Norse come each spring for their silver. This spring, send them back with iron.",
  "Needs 600 prestige. Ends the Danegeld, restores your name, chance of the Brave trait, and the longships come to test you.",
  IRISH + "\nhas_character_modifier = eir_danegeld_modifier",
  """remove_character_modifier = eir_danegeld_modifier
remove_character_flag = eir_paid_danegeld
add_prestige = 150
eir_trait_effect = { TRAIT = brave OPPOSITE = craven CHANCE = 20 }
trigger_event = { id = eir.0010 days = 30 }""", valid="prestige >= 600", cost=cost(prestige=200), cd=1825, pic="decision_siege_warfare")

D("eir_cattle_raid_decision", "Raid for Cattle",
  "The oldest sport in Ireland is stealing a neighbour's cows. Send the young men over the border and have a poem written about it.",
  "A neighbour loses cattle and hates you; you gain gold, prestige and a raider's reputation. Pay the éraic to clear it.",
  IRISH + "\nany_neighboring_and_across_water_top_liege_realm_owner = {\n\tculture = culture:irish\n\tNOT = { this = root }\n}",
  """random_neighboring_and_across_water_top_liege_realm_owner = {
	limit = {
		culture = culture:irish
		NOT = { this = root }
	}
	add_opinion = { target = root modifier = eir_satire_opinion opinion = -30 }
	random_realm_county = {
		add_county_modifier = { modifier = eir_cattle_raided_modifier years = 5 }
	}
}
add_gold = major_gold_value
add_prestige = 100
add_character_modifier = { modifier = eir_raider_infamy_modifier years = 8 }""",
  valid=req(VIS, "NOT = { has_character_modifier = eir_raider_infamy_modifier }", "is_at_war = no"), cd=5475, pic="decision_recruitment")

D("eir_pay_eraic_decision", "Pay the Éraic",
  "Brehon law counts every wrong in cattle. Pay what you owe, and the feud is over before it starts.",
  "Ends the Infamous Cattle-Raider reputation.",
  IRISH + "\nhas_character_modifier = eir_raider_infamy_modifier",
  """remove_character_modifier = eir_raider_infamy_modifier
add_prestige = 50""", cost=cost(gold=200), cd=1825, pic="decision_social")

D("eir_appease_satirists_decision", "Appease the Satirists",
  "A satire cannot be unsung, but it can be answered. Pay the poets a fair price, and ask them to find another subject.",
  "Removes the Satirised modifier by paying the poets.",
  IRISH + "\nhas_character_modifier = eir_satirised_modifier",
  """remove_character_modifier = eir_satirised_modifier
add_prestige = 50""", cost=cost(gold=150), cd=1825, pic="decision_social")

D("eir_wergild_decision", "Settle the Wergild",
  "Brehon law counts every killing in cows. Pay the honour-price, and the blood-feud is over.",
  "Removes Kin Strife and Infamous Cattle-Raider, and gives the Wergild Paid modifier.",
  IRISH + "\nOR = {\n\thas_character_modifier = eir_kin_strife_modifier\n\thas_character_modifier = eir_raider_infamy_modifier\n}",
  """if = {
	limit = { has_character_modifier = eir_kin_strife_modifier }
	remove_character_modifier = eir_kin_strife_modifier
}
if = {
	limit = { has_character_modifier = eir_raider_infamy_modifier }
	remove_character_modifier = eir_raider_infamy_modifier
}
add_character_modifier = { modifier = eir_wergild_peace_modifier years = 8 }
eir_vassal_opinion_effect = { MODIFIER = eir_wergild_paid_opinion OPINION = 8 }""", cost=cost(gold=250), cd=1825, pic="decision_social")

D("eir_norse_captain_decision", "Hire a Norse Sea-King",
  "Some Norse lords will fight for any Irish king who pays. They are expensive, and loyalty to them is a currency.",
  "Needs a duchy and a coast. A mercenary host for four years and a Norse-Gael tie.",
  IRISH + "\n" + VIS,
  """spawn_army = {
	levies = 600
	men_at_arms = {
		type = light_footmen
		stacks = 2
	}
	men_at_arms = {
		type = armored_footmen
		stacks = 1
	}
	location = capital_province
	origin = capital_province
	inheritable = no
	name = eir_viking_fleet_name
}
add_character_modifier = { modifier = eir_foreign_lords_modifier years = 4 }""",
  valid=req(S2, "eir_has_coast_trigger = yes"), cost=cost(gold=600), cd=3650, pic="decision_recruitment")

D("eir_four_provinces_decision", "Hosting of the Four Provinces",
  "Munster, Leinster, Connacht and Ulster, each under their king, behind a single banner.",
  "Needs a kingdom, the Óenach, the Muster and two duchies. Two hosts, a Great Hosting modifier and a legend.",
  IRISH + "\n" + VIS,
  """eir_defender_levy_effect = yes
eir_defender_levy_effect = yes
add_character_modifier = { modifier = eir_hosting_modifier years = 6 }
add_prestige = 500
eir_legend_title_effect = { TITLE = primary_title }
trigger_event = { id = eir.0172 days = 60 }""",
  valid=req(S3, "has_global_variable = eir_done_muster", OENACH, "eir_holds_irish_duchies_trigger = { COUNT = 2 }"),
  cost=cost(gold=1200, prestige=800), cd=14600, major=True, pic="decision_recruitment")

D("eir_single_combat_decision", "Issue a Challenge to Single Combat",
  "In the old days, two kings might settle a war between two champions. Send the challenge.",
  "A duel with a Norse champion. Win, and gain prestige and the Champion of Ulster trait. Lose, and bleed.",
  IRISH + "\n" + VIS,
  """trigger_event = { id = eir.0151 days = 5 }""", valid=req(S1, "prowess >= 10", "is_at_war = no"), cost=cost(prestige=150), cd=3650, pic="decision_knight_kneeling")

D("eir_coastal_watch_decision", "Post Watchmen on the Headlands",
  "Beacon fires on every headland will warn of a fleet while it is still at sea.",
  "Needs 3 ports. Coastal counties get the Coastal Watch modifier and a beacon in their province.",
  IRISH + "\n" + VIS,
  """every_held_title = {
	limit = {
		tier = tier_county
		is_coastal_county = yes
	}
	add_county_modifier = { modifier = eir_coast_watch_county_modifier years = 25 }
	title_province = { add_province_modifier = { modifier = eir_beacon_province_modifier years = 25 } }
}
add_character_modifier = { modifier = eir_watchtowers_modifier years = 15 }
add_prestige = 100""", valid=req(S1, "eir_ports_trigger = { N = 3 }"), cost=cost(gold=400, prestige=150), cd=7300, pic="decision_castle_view")

D("eir_ceithern_decision", "Raise the Royal Ceithern",
  "A king's ceithern are the picked men of his household, who eat at his table and die at his door.",
  "Needs a kingdom, the Oath of the Provincial Kings and four Irish buildings. Unlocks the Ceithern Retinue men-at-arms for all Gaelic rulers.",
  IRISH + "\n" + VIS,
  """set_global_variable = eir_unlock_ceithern
add_prestige = 250""",
  valid=req(S3, "has_global_variable = eir_done_oath", blds(4), "NOT = { has_global_variable = eir_unlock_ceithern }"),
  cost=cost(gold=800, prestige=600), cd=36500, pic="decision_recruitment")

D("eir_pacify_natives_decision", "Make Peace with the Native Irish",
  "A lord who learns the names of the local families, and pays what he owes, will be hated a little less.",
  "Every occupied Celtic county in your realm gets the Pacified modifier for ten years, which cancels native resistance there.",
  "eir_rules_occupied_land_trigger = yes\nis_ai = no",
  """every_sub_realm_county = {
	limit = { eir_county_occupied_trigger = yes }
	add_county_modifier = { modifier = eir_pacified_modifier years = 10 }
}
add_prestige = 50""", cost=cost(gold=600), cd=3650, pic="decision_social")

D("eir_burn_the_hills_decision", "Burn the Hills",
  "Some men are not won with gifts. Send the army through the hills and let the people remember why they should fear you.",
  "Quick gold now, but every occupied county gets a lasting Punitive Levy. Make peace later with the other decision.",
  "eir_rules_occupied_land_trigger = yes\nis_ai = no",
  """every_sub_realm_county = {
	limit = { eir_county_occupied_trigger = yes }
	add_county_modifier = { modifier = eir_punitive_levy_modifier years = 6 }
}
add_gold = major_gold_value
add_character_modifier = { modifier = eir_raider_infamy_modifier years = 10 }""", cd=1825, pic="decision_social")

# =============================================================================
# D. FAITH
# =============================================================================
D("eir_found_monastery_decision", "Found a Monastery",
  "A house of prayer, a scriptorium and a guest hall. The Church will bless your name, and the monks will bring the learning of the age.",
  "Needs 4 counties and 200 piety. A county monastery for 40 years, piety and clergy opinion, and the road to scriptoria and high crosses.",
  IRISH + "\n" + VIS,
  """eir_held_county_modifier_effect = { MODIFIER = eir_monastery_county_modifier YEARS = 40 }
eir_held_county_modifier_effect = { MODIFIER = eir_salmon_fisheries_modifier YEARS = 30 }
add_character_modifier = { modifier = eir_monastery_founder_modifier years = 15 }
add_piety = 250
set_global_variable = eir_done_monastery""",
  valid=req(S1, "piety >= 200", "any_held_title = { tier = tier_county }", "NOT = { has_global_variable = eir_done_monastery }"),
  cost=cost(gold=300, piety=200), cd=36500, pic="decision_personal_religious")

D("eir_found_scriptorium_decision", "Found a Great Scriptorium",
  "A house of copyists, illuminators and binders, producing gospel books that will be treasured for a thousand years.",
  "Needs a monastery, 400 piety and a duchy. Unlocks the Great Scriptorium, a saint's blessing, and a gospel book finishes in five years.",
  IRISH + "\n" + VIS,
  """set_global_variable = eir_unlock_scriptorium
add_character_modifier = { modifier = eir_saints_blessing_modifier years = 12 }
add_piety = 250
trigger_event = { id = eir.0080 years = 5 }""", valid=req(S2, MONK, "piety >= 400", "NOT = { has_global_variable = eir_unlock_scriptorium }"),
  cost=cost(gold=600, piety=300), cd=36500, pic="decision_tale")

D("eir_raise_high_crosses_decision", "Raise the High Crosses",
  "Stone crosses taller than three men, carved with scenes from the Bible. They preach to those who cannot read.",
  "Needs a monastery and a duchy. Unlocks the High Cross building; three of your counties gain High Crosses.",
  IRISH + "\n" + VIS,
  """set_global_variable = eir_unlock_high_cross
eir_held_county_modifier_effect = { MODIFIER = eir_high_cross_modifier YEARS = 25 }
eir_held_county_modifier_effect = { MODIFIER = eir_high_cross_modifier YEARS = 25 }
eir_held_county_modifier_effect = { MODIFIER = eir_high_cross_modifier YEARS = 25 }
add_piety = 200""", valid=req(S2, MONK, "NOT = { has_global_variable = eir_unlock_high_cross }"), cost=cost(gold=600, piety=150), cd=36500, pic="decision_personal_religious")

D("eir_found_round_towers_decision", "Raise the Round Towers",
  "A tall stone belfry that doubles as a treasury and a refuge. It rings the bell for prayer, and it rings the alarm when the longships are sighted.",
  "Needs a monastery and a duchy. Unlocks the Round Tower building and a warning beacon at your capital.",
  IRISH + "\n" + VIS,
  """set_global_variable = eir_unlock_round_tower
capital_province ?= { add_province_modifier = { modifier = eir_beacon_province_modifier years = 25 } }
random_held_title = {
	limit = { tier = tier_county }
	title_province = { add_province_modifier = { modifier = eir_round_tower_province_modifier years = 30 } }
}
add_piety = 100""", valid=req(S2, MONK, "NOT = { has_global_variable = eir_unlock_round_tower }"), cost=cost(gold=500, piety=100), cd=36500, pic="decision_castle_view")

D("eir_scriptorium_patron_decision", "Patronise the Scriptorium",
  "The monks need vellum, ink, gold leaf and peace. You can provide all four.",
  "Needs the Great Scriptorium. Learning and prestige. A small gospel book may be finished within three years.",
  IRISH + "\nhas_global_variable = eir_unlock_scriptorium",
  """add_character_modifier = { modifier = eir_scriptorium_patron_modifier years = 8 }
add_piety = 100
trigger_event = { id = eir.0153 years = 3 }""", valid=S2, cost=cost(gold=400, piety=100), cd=3650, pic="decision_tale")

D("eir_endow_cashel_decision", "Endow the Rock of Cashel",
  "The limestone crag of Cashel was the seat of the kings of Munster. Give it to the Church, and the Church will remember.",
  "Needs the Duchy of Munster, a monastery and 400 piety. A landmark county for 30 years, piety, and the saints' blessing.",
  IRISH + "\n" + VIS,
  """eir_capital_county_modifier_effect = { TITLE = d_munster MODIFIER = eir_cashel_rock_modifier YEARS = 30 }
add_piety = 350
add_character_modifier = { modifier = eir_saints_blessing_modifier years = 12 }
set_global_variable = eir_done_cashel""",
  valid=req(S2, "has_title = title:d_munster", MONK, "piety >= 400", "NOT = { has_global_variable = eir_done_cashel }"), cost=cost(gold=700, piety=300), cd=36500, pic="decision_personal_religious")

D("eir_synod_rath_breasail_decision", "Call the Synod of Ráth Breasail",
  "Bishops and abbots from all Ireland, deciding the island's church organisation. The reformers will be delighted. The monks of the old foundations will not.",
  "Needs a kingdom, Cashel's endowment and 800 piety. A reform modifier, but years of Culdee strife.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_synod_reform_modifier years = 15 }
add_character_modifier = { modifier = eir_culdee_strife_modifier years = 8 }
add_piety = 400
set_global_variable = eir_done_synod""", valid=req(S3, CASHEL, "piety >= 800", "NOT = { has_global_variable = eir_done_synod }"), cost=cost(piety=500), cd=36500, major=True, pic="decision_personal_religious")

D("eir_reconcile_culdees_decision", "Reconcile the Culdees",
  "Bring the old monasteries and the reformers to the same table, and pay for the peace.",
  "Removes Culdee strife.",
  IRISH + "\nhas_character_modifier = eir_culdee_strife_modifier",
  """remove_character_modifier = eir_culdee_strife_modifier
add_piety = 150""", cost=cost(gold=250, piety=100), cd=1825, pic="decision_social")

D("eir_pilgrimage_skellig_decision", "Pilgrimage to Skellig Michael",
  "A tower of rock off the Kerry coast, a ladder of 600 steps, a cluster of beehive cells. Climb, pray and come back changed.",
  "Needs a coast and 200 piety. Piety, a pilgrim's blessing for eight years.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_pilgrim_modifier years = 8 }
add_character_modifier = { modifier = eir_hermit_blessing_modifier years = 8 }
add_piety = 350""", valid=req(S1, "piety >= 200", "eir_has_coast_trigger = yes", "NOT = { has_character_modifier = eir_pilgrim_modifier }"), cost=cost(gold=200), cd=7300, pic="decision_personal_religious")

D("eir_armagh_primacy_decision", "Claim the Primacy for Armagh",
  "Armagh holds the relics of Saint Patrick, and the bishops of Armagh say they are the successors of Ireland's apostle. Back them against Cashel and Dublin.",
  "Needs the Duchy of Ulster, Cashel and 500 piety. Armagh's landmark bonus for 30 years, piety, and Armagh's cathedral and library open.",
  IRISH + "\n" + VIS,
  """eir_capital_county_modifier_effect = { TITLE = d_ulster MODIFIER = eir_armagh_see_modifier YEARS = 30 }
eir_held_county_modifier_effect = { MODIFIER = eir_armagh_library_modifier YEARS = 30 }
add_piety = 300
set_global_variable = eir_done_armagh""",
  valid=req(S2, "has_title = title:d_ulster", CASHEL, "piety >= 500", "NOT = { has_global_variable = eir_done_armagh }"), cost=cost(gold=800, piety=400), cd=36500, pic="decision_personal_religious")

D("eir_patronise_glendalough_decision", "Revive Glendalough",
  "The valley of two lakes, where Saint Kevin lived as a hermit, has grown into a great monastic city. Support it.",
  "Needs the Duchy of Leinster and Cashel's endowment. Glendalough's bonus for 30 years, piety.",
  IRISH + "\n" + VIS,
  """eir_capital_county_modifier_effect = { TITLE = d_leinster MODIFIER = eir_glendalough_modifier YEARS = 30 }
add_piety = 250
set_global_variable = eir_done_glendalough""",
  valid=req(S2, "has_title = title:d_leinster", CASHEL, "NOT = { has_global_variable = eir_done_glendalough }"), cost=cost(gold=600, piety=250), cd=36500, pic="decision_personal_religious")

D("eir_restore_clonmacnoise_decision", "Restore Clonmacnoise",
  "The monastic city on the Shannon, with its crosses, its scriptorium, and the tombs of the kings of Connacht.",
  "Needs the Duchy of Connacht and Cashel's endowment. A monastic city modifier for 30 years, piety.",
  IRISH + "\n" + VIS,
  """eir_capital_county_modifier_effect = { TITLE = d_connacht MODIFIER = eir_monastic_city_modifier YEARS = 30 }
add_piety = 250
set_global_variable = eir_done_clonmacnoise""",
  valid=req(S2, "has_title = title:d_connacht", CASHEL, "NOT = { has_global_variable = eir_done_clonmacnoise }"), cost=cost(gold=600, piety=250), cd=36500, pic="decision_personal_religious")

D("eir_cain_law_decision", "Proclaim a Cáin",
  "A cáin is a law sworn by king and bishop together. This one protects clerics, women and the poor, and grants sanctuary in every church.",
  "Needs Cashel's endowment, a kingdom and 600 piety. Piety, clergy opinion, the Right of Sanctuary; the law will be tested.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_cain_law_modifier years = 20 }
add_character_modifier = { modifier = eir_sanctuary_modifier years = 20 }
add_piety = 400
set_global_variable = eir_done_cain
trigger_event = { id = eir.0171 days = 90 }""", valid=req(S3, CASHEL, "piety >= 600", "NOT = { has_global_variable = eir_done_cain }"), cost=cost(piety=400), cd=36500, pic="decision_personal_religious")

D("eir_relic_procession_decision", "Carry the Relic Through the Land",
  "The shrine of a saint is carried from county to county, and the people kneel as it passes.",
  "Needs Cashel. Every held county gets a short bonus, piety.",
  IRISH + "\n" + VIS,
  """every_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_relic_procession_county_modifier years = 5 }
}
add_character_modifier = { modifier = eir_relic_procession_modifier years = 8 }
add_piety = 200""", valid=req(S2, CASHEL), cost=cost(piety=250, gold=200), cd=3650, pic="decision_personal_religious")

D("eir_penance_decision", "Do Public Penance",
  "Barefoot, in a plain shirt, on the church steps. The people watch, and some of them weep.",
  "Needs high stress. Lowers stress considerably; costs prestige.",
  IRISH + "\n" + VIS,
  """add_stress = -80
add_character_modifier = { modifier = eir_penance_done_modifier years = 6 }
add_prestige = -100
add_piety = 150""", valid="stress >= 50", cd=1825, pic="decision_personal_religious")

D("eir_rome_pilgrimage_decision", "Go on Pilgrimage to Rome",
  "A year's walk and a year's walk back. It is a long way to go to be forgiven.",
  "Needs 800 piety, peace and a duchy. A risky journey with a chance of the Saint-King trait.",
  IRISH + "\n" + VIS,
  """trigger_event = { id = eir.0152 days = 30 }""", valid=req(S2, "piety >= 800", "is_at_war = no"), cost=cost(gold=800), cd=36500, major=True, pic="decision_personal_religious")

D("eir_honour_saints_decision", "Honour the Saints of Ireland",
  "Brigid, Colmcille, Patrick: three saints, three cults, three kinds of blessing. Choose which will be the patron of your reign.",
  "Needs a monastery, a duchy and 400 piety. Choose among three saints for different bonuses, county shrines and cult events.",
  IRISH + "\n" + VIS,
  """trigger_event = { id = eir.0180 days = 5 }""", valid=req(S2, MONK, "piety >= 400"), cost=cost(gold=400, piety=300), cd=7300, pic="decision_personal_religious")

# =============================================================================
# E. KINGDOMS (each needs its own accomplishment)
# =============================================================================
def kingdom_decision(key, kingdom, duchy, name, desc, tip, unlock, accomplishment, extra=""):
    D(key, name, desc, tip, IRISH + "\n" + VIS,
      "eir_create_title_effect = { TITLE = %s }\nset_global_variable = %s\ndynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 30 } }\n"
      "add_prestige = 600\neir_legend_title_effect = { TITLE = title:%s }\ntrigger_event = { id = eir.0110 days = 7 }\n%s" % (kingdom, unlock, kingdom, extra),
      valid=req("eir_can_create_provincial_kingdom_trigger = { DUCHY = %s }" % duchy, "eir_realm_size_trigger = { N = 15 }", blds(2), OENACH, accomplishment,
                "NOT = { exists = title:%s.holder }" % kingdom),
      cost=cost(gold=1500, prestige=1200), cd=36500, major=True, pic="decision_found_kingdom")


kingdom_decision("eir_crown_king_of_munster_decision", "k_eir_munster", "d_munster", "Crown the King of Munster",
                 "Munster was a kingdom before there was a High King, and it gave Ireland Brian Boru. Take the crown of Cashel.",
                 "Needs Munster, 15 counties, Cashel's endowment and 2 Irish buildings. Creates the Kingdom of Munster and unlocks the Great Ringfort.",
                 "eir_unlock_ringfort", CASHEL)
kingdom_decision("eir_crown_king_of_ulster_decision", "k_eir_ulster", "d_ulster", "Crown the King of Ulster",
                 "The Ulaid of the Red Branch are older than Tara. Their heirs can still raise a king at Emain Macha.",
                 "Needs Ulster, 15 counties and Armagh's primacy. Creates the Kingdom of Ulster and unlocks the Crannóg Stronghold.",
                 "eir_unlock_crannog", "has_global_variable = eir_done_armagh")
kingdom_decision("eir_crown_king_of_leinster_decision", "k_eir_leinster", "d_leinster", "Crown the King of Leinster",
                 "The kings of Leinster have ruled the rich east for as long as there has been a Leinster. Place the crown on a new head.",
                 "Needs Leinster, 15 counties and a revived Glendalough. Creates the Kingdom of Leinster and unlocks the Great Cattle Enclosure.",
                 "eir_unlock_cattle_enclosure", "has_global_variable = eir_done_glendalough")
kingdom_decision("eir_crown_king_of_connacht_decision", "k_eir_connacht", "d_connacht", "Crown the King of Connacht",
                 "Connacht is a land of bogs, hills and fierce warriors, and its kings have raised many an Ard Rí.",
                 "Needs Connacht, 15 counties and a restored Clonmacnoise. Creates the Kingdom of Connacht and unlocks the High Cross.",
                 "eir_unlock_high_cross", "has_global_variable = eir_done_clonmacnoise")
kingdom_decision("eir_crown_king_of_meath_decision", "k_eir_meath", "d_meath", "Crown the King of Meath",
                 "The kings of Meath hold the middle of Ireland and the Hill of Tara, and the high kingship has been theirs more often than anyone's.",
                 "Needs Meath, 15 counties and the Hall of Tara. Creates the Kingdom of Meath and unlocks the Brehon Court.",
                 "eir_unlock_brehon_court", "has_global_variable = eir_done_tara_hall",
                 "eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hill_modifier YEARS = 25 }")

D("eir_crown_king_of_dal_riata_decision", "Crown the King of Dál Riata",
  "Gaelic kings once ruled both sides of the North Channel. Gather the old counties and put a crown on the old kingdom.",
  "Needs three counties in western Scotland and the Dál Riata reclaim. Creates the Kingdom of Dál Riata.",
  IRISH + "\neir_can_create_dal_riata_trigger = yes",
  """eir_create_title_effect = { TITLE = k_eir_dal_riata }
add_prestige = 700
add_character_modifier = { modifier = eir_pictish_memory_modifier years = 15 }
eir_held_county_modifier_effect = { MODIFIER = eir_dunadd_modifier YEARS = 30 }
""",
  valid=req("eir_can_create_dal_riata_trigger = yes", "eir_realm_size_trigger = { N = 12 }", "NOT = { exists = title:k_eir_dal_riata.holder }"),
  cost=cost(gold=1200, prestige=1000), cd=36500, major=True, pic="decision_found_kingdom")

# =============================================================================
# F. THE CELTIC WORLD
# =============================================================================
D("eir_celtic_brotherhood_decision", "Call the Celtic Brotherhood",
  "The Welsh, the Cornish, the Bretons and the Gaels of Alba are one people with five tongues. Write to all of them, and offer the hand of a king.",
  "Needs a kingdom, the Oath of the Provincial Kings and 3 ports. Brythonic rulers warm to you; unlocks every Celtic decision.",
  IRISH + "\n" + VIS,
  """every_ruler = {
	limit = {
		is_ai = yes
		culture ?= { has_cultural_pillar = heritage_brythonic }
	}
	add_opinion = { target = root modifier = eir_gael_pride_opinion opinion = 30 }
}
add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 15 }
add_prestige = 500
set_global_variable = eir_done_brotherhood""",
  valid=req(S3, "has_global_variable = eir_done_oath", "eir_ports_trigger = { N = 3 }", "NOT = { has_global_variable = eir_done_brotherhood }"),
  cost=cost(prestige=1200, gold=800), cd=36500, major=True, pic="decision_social")


def reclaim(key, name, desc, tip, effect, prestige, gold, cond=""):
    D(key, name, desc, tip, IRISH + "\n" + VIS, effect + "\nadd_prestige = 150",
      valid=req(S3, BROTHER, "is_at_war = no", "eir_ports_trigger = { N = 2 }", cond), cost=cost(gold=gold, prestige=prestige), cd=7300, pic="decision_legend")


reclaim("eir_reclaim_dal_riata_decision", "Reclaim Dál Riata",
        "Before there was a Scotland there was a Gaelic kingdom that spanned the North Channel. Its old counties are now ruled by strangers.",
        "Needs the Brotherhood, a kingdom and 2 ports. Pressed claims on up to nine counties across Albany, the Isles and the Western Isles held by non-Celtic rulers.",
        "eir_grant_claims_non_celtic_effect = { TITLE = d_albany }\neir_grant_claims_non_celtic_effect = { TITLE = d_the_isles }\n"
        "eir_grant_claims_non_celtic_effect = { TITLE = d_western_isles }\nset_global_variable = eir_done_dalriata", 900, 600)
reclaim("eir_reclaim_man_isles_decision", "Reclaim the Isle of Man",
        "Man sits in the middle of the Irish Sea, with a Norse-Gael king who answers to nobody. Declare it Irish.",
        "Needs the Brotherhood, a kingdom and 2 ports. Pressed claims on the Kingdom of Man and the Isles.",
        "eir_grant_claims_non_celtic_effect = { TITLE = k_mann_the_isles }", 700, 500)
reclaim("eir_reclaim_cornwall_decision", "Reclaim Cornwall",
        "The Cornish speak a Celtic tongue and trade tin with half of Europe. Their lords sit under foreign kings.",
        "Needs the Brotherhood, a kingdom and 2 ports. Pressed claims on up to three Cornish counties.",
        "eir_grant_claims_non_celtic_effect = { TITLE = d_cornwall }", 700, 500)
reclaim("eir_reclaim_armorica_decision", "Reclaim Armorica",
        "Brittany was settled by Britons fleeing the Saxons, and its tongue is cousin to Welsh. Its old nobility is under a foreign yoke.",
        "Needs the Brotherhood, a kingdom and 2 ports. Pressed claims on up to three Breton counties.",
        "eir_grant_claims_non_celtic_effect = { TITLE = d_brittany }", 900, 600)
reclaim("eir_reclaim_old_north_decision", "Reclaim the Old North",
        "The kingdoms of Rheged, Gododdin and Elmet fell to the English, but the Gaels remember them.",
        "Needs the Brotherhood, a kingdom and 2 ports. Pressed claims across Northumberland and Lothian.",
        "eir_grant_claims_non_celtic_effect = { TITLE = d_northumberland }\neir_grant_claims_non_celtic_effect = { TITLE = d_lothian }", 1000, 700)
reclaim("eir_stand_with_wales_decision", "Stand with Wales",
        "The Welsh are fighting for the same cause as the Irish. Declare that their wars are yours.",
        "Needs the Brotherhood, a kingdom and 2 ports. Pressed claims on up to six counties in Powys and Deheubarth.",
        "eir_grant_claims_non_celtic_effect = { TITLE = d_powys }\neir_grant_claims_non_celtic_effect = { TITLE = d_deheubarth }", 800, 500)

D("eir_pictish_memory_decision", "Honour the Memory of the Picts",
  "The painted people were here before the Gael, and their stones still stand in Alba. Honour them.",
  "Needs the Brotherhood, a kingdom and Dál Riata's reclaim. Prestige, and pressed claims on up to three Pictish-land counties.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_pictish_memory_modifier years = 15 }
eir_grant_claims_non_celtic_effect = { TITLE = k_scotland }
add_prestige = 250""", valid=req(S3, BROTHER, "has_global_variable = eir_done_dalriata"), cost=cost(gold=600, prestige=900), cd=14600, pic="decision_legend")

D("eir_gaulish_heritage_decision", "Remember the Gauls",
  "Before Rome, the Celts ruled from the Danube to the Atlantic. Some of that land should be remembered.",
  "Needs the Brotherhood, a kingdom and 3 ports. A prestige modifier and pressed claims on up to three counties of Anjou.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_gaulish_heritage_modifier years = 15 }
eir_grant_claims_non_celtic_effect = { TITLE = d_anjou }
add_prestige = 250""", valid=req(S3, BROTHER, "eir_ports_trigger = { N = 3 }"), cost=cost(gold=700, prestige=1000), cd=14600, pic="decision_legend")

D("eir_embassy_gwynedd_decision", "Send an Embassy to Gwynedd",
  "The princes of Gwynedd keep a hard, rocky land, and a fine tradition of poetry. Send them gifts and a proposal.",
  "Needs the Brotherhood, a duchy and a port. Fires the Gwynedd alliance event.",
  IRISH + "\n" + VIS,
  """add_prestige = 50
trigger_event = { id = eir.0154 days = 60 }""", valid=req(S2, BROTHER, "eir_ports_trigger = { N = 1 }"), cost=cost(gold=300, prestige=200), cd=3650, pic="decision_social")

D("eir_embassy_strathclyde_decision", "Send an Embassy to Strathclyde",
  "The last of the northern Britons hold a rock-fort on the Clyde. Treat them as kin.",
  "Needs the Brotherhood, a duchy and a port. Fires the Strathclyde alliance event.",
  IRISH + "\n" + VIS,
  """add_prestige = 50
trigger_event = { id = eir.0155 days = 60 }""", valid=req(S2, BROTHER, "eir_ports_trigger = { N = 1 }"), cost=cost(gold=300, prestige=200), cd=3650, pic="decision_social")

D("eir_breton_refuge_decision", "Offer Refuge to Breton Exiles",
  "Brittany has fallen to foreign lords again, and its nobles are looking for a safe harbour.",
  "Needs the Brotherhood and a port. A hospitality modifier. A Breton refugee will arrive in a year.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_breton_refuge_modifier years = 10 }
add_prestige = 100
trigger_event = { id = eir.0158 years = 1 }""", valid=req(S2, BROTHER, "eir_ports_trigger = { N = 1 }"), cost=cost(gold=250, prestige=150), cd=7300, pic="decision_social")

D("eir_armorica_voyage_decision", "Send a Ship to Armorica",
  "Ships can reach Brittany in four days with a fair wind and a stout hull.",
  "Needs the Brotherhood and 2 ports. A risky voyage; fires the Armorican Voyage event.",
  IRISH + "\n" + VIS,
  """add_prestige = 25
trigger_event = { id = eir.0157 days = 40 }""", valid=req(S2, BROTHER, "eir_ports_trigger = { N = 2 }"), cost=cost(gold=400, prestige=100), cd=3650, pic="decision_activity")

D("eir_hebridean_marriage_decision", "Arrange a Hebridean Marriage",
  "The galley-lords of the Isles will serve a king who marries into their families.",
  "Needs a duchy and a port. Fires the Hebridean marriage event.",
  IRISH + "\n" + VIS,
  """add_prestige = 25
trigger_event = { id = eir.0156 days = 45 }""", valid=req(S2, "eir_ports_trigger = { N = 1 }"), cost=cost(gold=300, prestige=150), cd=3650, pic="decision_social")

D("eir_britannia_restored_decision", "Restore Britannia",
  "The island of Britain was once all Celtic. A king who rules the Gaelic west, and calls the Welsh and Cornish kin, may reclaim it.",
  "Needs the High Kingship, the Brotherhood and Dál Riata's reclaim. Huge prestige and vassal opinion, claims on England, a great legend.",
  IRISH + "\n" + VIS,
  """add_character_modifier = { modifier = eir_britannia_modifier years = 25 }
eir_grant_claims_non_celtic_effect = { TITLE = k_england }
eir_legend_title_effect = { TITLE = primary_title }
add_prestige = 1000""", valid=req(S4, BROTHER, "has_global_variable = eir_done_dalriata", "NOT = { has_character_modifier = eir_britannia_modifier }"),
  cost=cost(gold=2500, prestige=3000), cd=36500, major=True, pic="decision_found_kingdom")

D("eir_proclaim_gaeldom_decision", "Proclaim the Empire of Gaeldom",
  "One High King of Ireland is a great thing. A king of kings over every Gaelic land from Cork to Caithness is greater still.",
  "Needs the High Kingship, the Brotherhood, the Gaelic Renaissance, 30 counties and a fortune. Creates the Empire of Gaeldom, a thirty-year emperor modifier, a vast prestige reward and a legend.",
  IRISH + "\n" + VIS,
  """eir_create_title_effect = { TITLE = e_eir_gaeldom }
add_character_modifier = { modifier = eir_gaeldom_emperor_modifier years = 30 }
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 60 } }
add_prestige = 2000
add_piety = 300
eir_legend_title_effect = { TITLE = title:e_eir_gaeldom }
trigger_event = { id = eir.0112 days = 7 }""",
  valid=req(S4, BROTHER, "has_global_variable = eir_done_renaissance", "eir_realm_size_trigger = { N = 30 }", "eir_can_create_gaeldom_trigger = yes",
            "NOT = { exists = title:e_eir_gaeldom.holder }"),
  cost=cost(gold=3000, prestige=4000), cd=36500, major=True, pic="decision_found_kingdom")
