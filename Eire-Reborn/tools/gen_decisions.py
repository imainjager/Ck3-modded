"""Generates common/decisions/eir_decisions.txt and its localization.

Unlock progress is stored in GLOBAL variables (eir_done_*, eir_unlock_*) so it survives from ruler to ruler.
Negative-effect decisions are paired with a remedy decision (the 40% rule in the design guide).
"""
from eir_lib import *

IRISH = "eir_is_irish_ruler_trigger = yes"
GAEL = "eir_is_gael_ruler_trigger = yes"

DEC = []


def D(key, name, desc, tip, shown, effect, valid="", cost="", cd=3650, major=False, pic="decision_misc"):
    DEC.append(dict(key=key, name=name, desc=desc, tip=tip, shown=shown, effect=effect, valid=valid,
                    cost=cost, cd=cd, major=major, pic=pic))


def ind(text, tabs):
    pad = "\t" * tabs
    return "".join(pad + line + "\n" if line.strip() else "\n" for line in text.strip("\n").split("\n"))


# =============================================================================
# PATH A - KINGSHIP AND STATECRAFT
# =============================================================================
D("eir_hold_oenach_decision", "Hold the Great Óenach",
  "Summon the lords, poets, judges and champions of your people to a great assembly, with games, feasting and the settling of old quarrels.",
  "Impress your vassals, ease any turmoil in your realm, and make a name as a unifier. Unlocks the path to being crowned at Tara.",
  f"{IRISH}\nhighest_held_title_tier >= tier_duchy",
  """add_character_modifier = { modifier = eir_oenach_afterglow_modifier years = 5 }
eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 10 }
capital_county ?= { add_county_modifier = { modifier = eir_oenach_ground_modifier years = 10 } }
if = {
	limit = { has_character_modifier = eir_throne_turmoil_modifier }
	remove_character_modifier = eir_throne_turmoil_modifier
}
add_prestige = 100
set_global_variable = eir_done_oenach
eir_trait_effect = { TRAIT = gregarious OPPOSITE = shy CHANCE = 10 }""",
  valid="NOT = { has_character_modifier = eir_oenach_afterglow_modifier }",
  cost="gold = medium_gold_value\nprestige = 50", cd=3650, pic="decision_social")

D("eir_crowned_at_tara_decision", "Be Crowned at Tara",
  "Ride to the Hill of Tara, where the kings of Ireland have been made for a thousand years, and put your hand on the Lia Fáil.",
  "Become High King of Ireland (Ard Rí), recreating the kingdom of Ireland if it was broken. Grants a trait, modifiers, and prestige.",
  f"{IRISH}\neir_holds_irish_duchies_trigger = {{ COUNT = 2 }}",
  """eir_create_title_effect = { TITLE = k_ireland }
if = {
	limit = { NOT = { has_trait = eir_ard_ri } }
	add_trait = eir_ard_ri
}
add_character_modifier = { modifier = eir_ard_ri_modifier years = 25 }
add_character_modifier = { modifier = eir_lia_fail_blessing_modifier years = 10 }
eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hill_modifier YEARS = 25 }
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 40 } }
eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 10 }
if = {
	limit = { has_character_modifier = eir_throne_turmoil_modifier }
	remove_character_modifier = eir_throne_turmoil_modifier
}
add_prestige = 500
add_piety = 100
set_global_variable = eir_done_crowned""",
  valid="""has_global_variable = eir_done_oenach
is_independent_ruler = yes
has_title = title:d_meath
OR = {
	has_title = title:k_ireland
	NOT = { exists = title:k_ireland.holder }
}""",
  cost="gold = major_gold_value\nprestige = 300", cd=7300, major=True, pic="decision_found_kingdom")

D("eir_end_fragmentation_decision", "End the Tanistic Fragmentation",
  "Ireland has always fallen apart when a great king died. You are in a position to change that. Proclaim that the high kingship will pass to your heir whole.",
  "Abolish the rule that destroys an Irish ruler's highest title on death. Replaces Tanistic Fragmentation with Stable High Kingship for the whole Irish culture.",
  f"{IRISH}\nhas_title = title:k_ireland\nhas_global_variable = eir_done_crowned\neir_collapse_active_trigger = yes",
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
add_character_modifier = { modifier = eir_peace_of_tara_modifier years = 20 }
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 60 } }
add_prestige = 500
add_legitimacy = 100""",
  valid="""government_has_flag = government_is_feudal
eir_holds_irish_counties_trigger = { COUNT = 8 }
is_independent_ruler = yes""",
  cost="gold = major_gold_value\nprestige = 500", cd=36500, major=True, pic="decision_golden_age")

D("eir_boramha_decision", "Demand the Bóramha Tribute",
  "The old cow-tribute of the kings of Ireland has not been paid in generations. A High King can demand it, and see who is brave enough to refuse.",
  "Collect a great sum of gold from your realm, at the cost of your vassals' goodwill. Remit the tribute later to win them back.",
  f"{IRISH}\nhas_trait = eir_ard_ri",
  """add_gold = major_gold_value
add_character_modifier = { modifier = eir_boramha_collected_modifier years = 8 }
eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -10 }
add_prestige = 50""",
  valid="NOT = { has_character_modifier = eir_boramha_collected_modifier }", cd=5475, pic="decision_spend_money")

D("eir_remit_tribute_decision", "Remit the Cow Tribute",
  "The tribute has made you rich and your vassals bitter. A generous High King can forgive it and be loved for it.",
  "Remove the Cow Tribute modifier and win your vassals' goodwill.",
  f"{IRISH}\nhas_character_modifier = eir_boramha_collected_modifier",
  """remove_character_modifier = eir_boramha_collected_modifier
eir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 15 }
add_prestige = 25""",
  cost="prestige = 50", cd=1825, pic="decision_social")

D("eir_foster_heir_decision", "Foster Your Children Among Your Vassals",
  "In Ireland a lord who fosters your child becomes closer to you than a brother. A king who fosters wisely never lacks friends.",
  "Bind your vassals to you with fosterage, gaining lasting opinion with them.",
  f"{IRISH}\nany_child = {{ age >= 4 age < 15 is_alive = yes }}",
  """add_character_modifier = { modifier = eir_foster_ties_modifier years = 15 }
eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 12 }
random_child = {
	limit = { age >= 4 age < 15 is_alive = yes }
	eir_trait_effect = { TRAIT = eir_foster_brother OPPOSITE = eir_foster_brother CHANCE = 60 }
}""",
  valid="NOT = { has_character_modifier = eir_foster_ties_modifier }",
  cost="gold = minor_gold_value", cd=5475, pic="decision_family_tree")

# =============================================================================
# PATH B - CULTURE AND LEARNING
# =============================================================================
D("eir_patronise_fili_decision", "Patronise the Filí",
  "Poets are the memory and the conscience of Ireland. A king who feeds them is praised. A king who does not is satirised.",
  "Gain prestige and legend reach, and a court Ollamh. Unlocks the Bardic Schools and the Brehon Laws.",
  IRISH,
  """add_character_modifier = { modifier = eir_fili_patron_modifier years = 10 }
add_prestige = 100
set_global_variable = eir_done_fili
random_courtier = {
	limit = { is_adult = yes learning >= 8 NOT = { has_trait = eir_ollamh } }
	add_trait = eir_ollamh
}""",
  valid="NOT = { has_character_modifier = eir_fili_patron_modifier }",
  cost="gold = medium_gold_value\nprestige = 50", cd=3650, pic="decision_culture")

D("eir_found_bardic_schools_decision", "Found the Bardic Schools",
  "Twelve years of study make a poet. Build a school where the sons of the learned classes can train, and your court will never lack voices.",
  "Add Bardic Schools to Irish culture, unlock the Bardic School building, and raise your house's standing.",
  f"{IRISH}\nhas_global_variable = eir_done_fili",
  """eir_add_tradition_effect = { TRADITION = tradition_eir_bardic_schools }
set_global_variable = eir_unlock_bardic_school
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_poets_modifier years = 40 } }
add_prestige = 150""",
  valid="learning >= 8", cost="gold = major_gold_value", cd=36500, pic="decision_culture")

D("eir_compile_brehon_laws_decision", "Compile the Brehon Laws",
  "The ancient laws live in the memories of the judges. Set them down, so that every dispute in Ireland is judged by the same rule.",
  "Add Brehon Law to Irish culture, unlock the Brehon Court building, and gain legitimacy.",
  f"{IRISH}\nhas_global_variable = eir_done_fili",
  """eir_add_tradition_effect = { TRADITION = tradition_eir_brehon_law }
set_global_variable = eir_unlock_brehon_court
add_character_modifier = { modifier = eir_brehon_laws_modifier years = 20 }
if = {
	limit = { learning >= 12 NOT = { has_trait = eir_brehon } }
	add_trait = eir_brehon
}
add_prestige = 100""",
  valid="""OR = {
	learning >= 10
	any_courtier = { has_trait = eir_ollamh }
}""", cost="gold = major_gold_value\nprestige = 100", cd=36500, pic="decision_legitimacy")

D("eir_revive_fianna_decision", "Revive the Fianna Tales",
  "Fionn and his hunter-warriors are not dead, say the bards, only sleeping. Raise a warband in their image and see how well the old tales fight.",
  "Add Fianna Heritage to Irish culture. Unlocks Fianna Warbands and Kern Javelineers for Irish rulers, and gives a martial modifier.",
  IRISH,
  """eir_add_tradition_effect = { TRADITION = tradition_eir_fianna_heritage }
set_global_variable = eir_unlock_fianna
set_global_variable = eir_unlock_kern
add_character_modifier = { modifier = eir_fianna_spirit_modifier years = 10 }
add_prestige = 100
if = {
	limit = { prowess >= 12 NOT = { has_trait = eir_fennid } }
	add_trait = eir_fennid
}""",
  valid="prestige >= 150", cost="gold = medium_gold_value", cd=36500, pic="decision_recruitment")

D("eir_found_scriptorium_decision", "Found the Great Scriptorium",
  "The monks of Ireland copy the gospels better than anyone in Christendom. Give them the walls and the vellum to make a masterpiece.",
  "Unlock the Great Scriptorium building. In five years the monks complete a work of art, and a famous gospel book may find its way to you.",
  f"{IRISH}\npiety >= 100",
  """set_global_variable = eir_unlock_scriptorium
add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }
add_piety = 100
trigger_event = { id = eir.0080 years = 5 }""",
  valid="piety >= 150", cost="gold = major_gold_value\npiety = 100", cd=36500, pic="decision_personal_religious")

D("eir_raise_high_crosses_decision", "Raise the High Crosses",
  "Carve the gospel in stone and set it up where all may see it. Ireland's great crosses are sermons that never end.",
  "Unlock the High Cross building and raise crosses in three of your counties.",
  f"{IRISH}\npiety >= 100",
  """set_global_variable = eir_unlock_high_cross
eir_held_county_modifier_effect = { MODIFIER = eir_high_cross_modifier YEARS = 25 }
eir_held_county_modifier_effect = { MODIFIER = eir_high_cross_modifier YEARS = 25 }
eir_held_county_modifier_effect = { MODIFIER = eir_high_cross_modifier YEARS = 25 }
add_piety = 100""",
  cost="gold = medium_gold_value", cd=7300, pic="decision_personal_religious")

D("eir_found_round_towers_decision", "Build the Round Towers",
  "The Norse come by sea and burn the churches. A tall stone tower with a door set high above the ground can save the monks and the relics.",
  "Unlock the Round Tower building and light a warning beacon at your capital.",
  f"{IRISH}\npiety >= 50",
  """set_global_variable = eir_unlock_round_tower
capital_province ?= { add_province_modifier = { modifier = eir_beacon_province_modifier years = 25 } }
add_piety = 50""",
  cost="gold = medium_gold_value", cd=7300, pic="decision_castle_view")

D("eir_hold_tailteann_decision", "Hold the Games of Tailtiu",
  "The funeral games of Tailtiu are the oldest festival in Ireland, with races, wrestling, matchmaking and a truce between every quarrelling clan.",
  "A fortnight of games gives prestige, relief from stress, and opinion with your vassals.",
  f"{IRISH}\nhighest_held_title_tier >= tier_duchy",
  """add_character_modifier = { modifier = eir_tailteann_modifier years = 8 }
capital_county ?= { add_county_modifier = { modifier = eir_tailteann_county_modifier years = 10 } }
eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 8 }
add_prestige = 150""",
  valid="NOT = { has_character_modifier = eir_tailteann_modifier }",
  cost="gold = medium_gold_value", cd=7300, pic="decision_activity")

D("eir_gaelic_revival_decision", "Proclaim a Gaelic Revival",
  "The Irish language, the Irish laws and the Irish way of war are old and good. Say so, loudly, in every court in the island.",
  "A lasting wave of Gaelic pride gives prestige and opinion among your own people. Requires patronage of the poets and the revival of the Fianna.",
  f"{IRISH}\nhas_global_variable = eir_done_fili",
  """add_character_modifier = { modifier = eir_gaelic_revival_modifier years = 15 }
add_character_modifier = { modifier = eir_hearth_of_the_gael_modifier years = 15 }
add_prestige = 200""",
  valid="has_global_variable = eir_unlock_fianna", cost="prestige = 200", cd=36500, pic="decision_legend")

D("eir_adopt_cattle_wealth_decision", "Embrace the Cattle Economy",
  "A man's worth is counted in cows. Make that the official policy of your realm, and reform the tribute system around it.",
  "Add Cattle Wealth to Irish culture and grant a Cattle Lord reputation.",
  IRISH,
  """eir_add_tradition_effect = { TRADITION = tradition_eir_cattle_wealth }
add_character_modifier = { modifier = eir_cattle_rich_modifier years = 15 }
set_global_variable = eir_unlock_cattle_enclosure
if = {
	limit = { stewardship >= 10 NOT = { has_trait = eir_cattle_lord } }
	add_trait = eir_cattle_lord
}""",
  valid="prestige >= 100", cost="prestige = 150", cd=36500, pic="decision_realm")

D("eir_adopt_fosterage_decision", "Make Fosterage the Law of the Land",
  "Every noble child in Ireland should be raised in a hall not their own. Let the bond of fosterage be the bond that holds your kingdom together.",
  "Add Bonds of Fosterage to Irish culture, lasting vassal opinion, and a fosterage modifier.",
  IRISH,
  """eir_add_tradition_effect = { TRADITION = tradition_eir_fosterage_bonds }
add_character_modifier = { modifier = eir_foster_ties_modifier years = 15 }
add_prestige = 50
set_global_variable = eir_done_fosterage""",
  valid="prestige >= 100", cost="prestige = 150", cd=36500, pic="decision_family_tree")

D("eir_adopt_culdee_decision", "Embrace the Celtic Church",
  "The Church of Ireland has its own saints, its own monks and its own way of calculating Easter. Let it be proud of that.",
  "Add Celtic Christianity to Irish culture and gain piety.",
  IRISH,
  """eir_add_tradition_effect = { TRADITION = tradition_eir_culdee_christianity }
add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }
add_piety = 150""",
  valid="piety >= 100", cost="prestige = 150", cd=36500, pic="decision_personal_religious")

D("eir_adopt_sea_kings_decision", "Claim the Irish Sea",
  "The Norse made the sea a road. Irish kings can sail it too, with ships of oak and hide, from Dublin to Man to Anglesey.",
  "Add Kings of the Irish Sea to Irish culture and gain a Sea-King's reputation.",
  f"{IRISH}\neir_has_coast_trigger = yes",
  """eir_add_tradition_effect = { TRADITION = tradition_eir_sea_kings }
add_character_modifier = { modifier = eir_sea_king_modifier years = 15 }
add_prestige = 100""",
  valid="prestige >= 100", cost="prestige = 150", cd=36500, pic="decision_siege_warfare")

# =============================================================================
# PATH C - WAR, THE NORSE, AND THE GALLOWGLASS
# =============================================================================
D("eir_muster_the_gael_decision", "Muster the Gael Against the Norse",
  "Foreign lords hold Irish land. Call every clan that has lost cattle, kin or churches to them, and march.",
  "Gain pressed claims on up to three Irish counties held by Norse rulers, and rally the Irish.",
  f"{IRISH}\neir_norse_holds_irish_county_trigger = yes",
  """eir_grant_claims_norse_effect = yes
eir_vassal_opinion_effect = { MODIFIER = eir_norse_defied_opinion OPINION = 10 }
add_prestige = 50
set_global_variable = eir_done_muster""",
  valid="is_at_war = no", cost="prestige = 100", cd=1825, pic="decision_siege_warfare")

D("eir_reclaim_dublin_decision", "Reclaim Dyflinn",
  "The Norse longphort at Dublin has been Ireland's richest city for two centuries. Take it back, and Ireland has a capital again.",
  "Gain a pressed claim on the county of Dublin. Taking it unlocks a further reward.",
  f"{IRISH}\ntitle:c_dublin = {{ holder ?= {{ culture ?= {{ has_cultural_pillar = heritage_north_germanic }} }} }}",
  """add_pressed_claim = title:c_dublin
add_prestige = 50
set_global_variable = eir_dublin_claimed""",
  valid="is_at_war = no", cost="gold = minor_gold_value", cd=1825, pic="decision_siege_warfare")

D("eir_dublin_reclaimed_decision", "Celebrate the Return of Dublin",
  "Dublin is Irish again. Declare a feast, rebuild the harbour, and let the world know what the Gael can do.",
  "Gain a Dublin Reclaimed county modifier, the Scourge of the Norse reputation, and prestige.",
  f"{IRISH}\nhas_title = title:c_dublin\nhas_global_variable = eir_dublin_claimed\nNOT = {{ has_global_variable = eir_done_dublin }}",
  """title:c_dublin = { add_county_modifier = { modifier = eir_dublin_reclaimed_modifier years = 25 } }
add_character_modifier = { modifier = eir_norse_scourge_modifier years = 15 }
add_prestige = 300
eir_trait_effect = { TRAIT = eir_viking_slayer OPPOSITE = eir_viking_slayer CHANCE = 60 }
set_global_variable = eir_done_dublin""",
  cost="gold = medium_gold_value", cd=36500, pic="decision_golden_age")

D("eir_hire_gallowglass_decision", "Hire the Gallowglass",
  "The axemen of the Isles and the Hebrides fight for whoever pays. Take a company into your pay and, in time, settle them on your land.",
  "Add Gallowglass Heritage to Irish culture, unlock Gallowglass men-at-arms, and gain a free company.",
  IRISH,
  """eir_add_tradition_effect = { TRADITION = tradition_eir_gallowglass_heritage }
set_global_variable = eir_unlock_gallowglass
add_character_modifier = { modifier = eir_gallowglass_paymaster_modifier years = 10 }
spawn_army = {
	levies = 0
	men_at_arms = {
		type = eir_gallowglass
		stacks = 2
	}
	location = capital_province
	origin = capital_province
	inheritable = no
	name = eir_gallowglass_company_name
}
random_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_gallowglass_garrison_modifier years = 15 }
}""",
  valid="prestige >= 100", cost="gold = major_gold_value", cd=36500, pic="decision_recruitment")

D("eir_pay_danegeld_decision", "Pay the Danegeld",
  "A great Norse fleet is on the way. Buy peace with silver, and hope that they spend the winter somewhere else.",
  "Suppress Viking invasions for eight years, at the cost of heavy gold and your vassals' pride. Refuse to pay later to end it.",
  f"{IRISH}\neir_viking_age_trigger = yes",
  """add_character_modifier = { modifier = eir_danegeld_modifier years = 8 }
add_character_flag = { flag = eir_paid_danegeld years = 8 }
add_prestige = -50""",
  valid="NOT = { has_character_flag = eir_paid_danegeld }", cost="gold = major_gold_value", cd=3650, pic="decision_spend_money")

D("eir_end_danegeld_decision", "Refuse to Pay the Norse",
  "No more silver for the men who burned the churches. If they want Irish gold, they can come and try to take it.",
  "End the Danegeld, restore your pride, and invite a Norse retaliation.",
  f"{IRISH}\nhas_character_modifier = eir_danegeld_modifier",
  """remove_character_modifier = eir_danegeld_modifier
remove_character_flag = eir_paid_danegeld
add_prestige = 100
eir_trait_effect = { TRAIT = brave OPPOSITE = craven CHANCE = 20 }
trigger_event = { id = eir.0010 days = 30 }""", cd=1825, pic="decision_siege_warfare")

D("eir_cattle_raid_decision", "Launch a Cattle Raid",
  "The Táin is the oldest story in Ireland, and every young warrior knows how it ends. Take your neighbour's herds.",
  "Gain a great sum of gold, but make an enemy and a name as a raider. Pay the blood-price later to repair the damage.",
  f"{IRISH}\nany_neighboring_and_across_water_top_liege_realm_owner = {{ culture = culture:irish NOT = {{ this = root }} }}",
  """random_neighboring_and_across_water_top_liege_realm_owner = {
	limit = { culture = culture:irish NOT = { this = root } }
	add_opinion = { target = root modifier = eir_satire_opinion opinion = -25 }
	random_realm_county = {
		add_county_modifier = { modifier = eir_cattle_raided_modifier years = 5 }
	}
}
add_gold = major_gold_value
add_character_modifier = { modifier = eir_raider_infamy_modifier years = 10 }
add_prestige = 75""",
  valid="""NOT = { has_character_modifier = eir_raider_infamy_modifier }
is_at_war = no""", cd=5475, pic="decision_recruitment")

D("eir_pay_eraic_decision", "Pay the Éraic",
  "Brehon law counts every wrong in cattle. Pay what you owe, and the feud is over before it starts.",
  "End the Infamous Cattle-Raider reputation by paying the honour-price.",
  f"{IRISH}\nhas_character_modifier = eir_raider_infamy_modifier",
  """remove_character_modifier = eir_raider_infamy_modifier
add_prestige = 25""",
  cost="gold = medium_gold_value", cd=1825, pic="decision_social")

D("eir_appease_satirists_decision", "Appease the Satirists",
  "A satire cannot be unsung, but it can be answered. Pay the poets a fair price, and ask them to find another subject.",
  "Remove the Satirised modifier by paying the poets.",
  f"{IRISH}\nhas_character_modifier = eir_satirised_modifier",
  """remove_character_modifier = eir_satirised_modifier
add_prestige = 25""",
  cost="gold = medium_gold_value", cd=1825, pic="decision_social")

# =============================================================================
# PATH X - FOR FOREIGN RULERS OF CELTIC LAND
# =============================================================================
D("eir_pacify_natives_decision", "Make Peace with the Natives",
  "A lord who learns the names of the local families, and pays what he owes, will be hated a little less.",
  "Every occupied Celtic county in your realm gets the Pacified modifier for ten years, which cancels native resistance there.",
  "eir_rules_occupied_land_trigger = yes\nis_ai = no",
  """every_sub_realm_county = {
	limit = { eir_county_occupied_trigger = yes }
	add_county_modifier = { modifier = eir_pacified_modifier years = 10 }
}
add_prestige = 25""",
  cost="gold = major_gold_value", cd=3650, pic="decision_social")

D("eir_harsh_pacification_decision", "Burn the Hills",
  "Some men are not won with gifts. Send the army through the hills and let the people remember why they should fear you.",
  "Quick gold now, but every occupied county gets a lasting Punitive Levy. Make peace later with the other decision.",
  "eir_rules_occupied_land_trigger = yes\nis_ai = no",
  """every_sub_realm_county = {
	limit = { eir_county_occupied_trigger = yes }
	add_county_modifier = { modifier = eir_punitive_levy_modifier years = 6 }
}
add_gold = major_gold_value
add_character_modifier = { modifier = eir_raider_infamy_modifier years = 10 }""",
  cd=1825, pic="decision_social")

# =============================================================================
# PATH D - THE CELTIC REVIVAL
# =============================================================================
D("eir_celtic_brotherhood_decision", "Call the Celtic Brotherhood",
  "The Welsh, the Cornish, the Bretons and the Gaels of Alba are one people with five tongues. Write to all of them, and offer the hand of a king.",
  "Brythonic rulers warm to you, and you gain the Celtic Brotherhood modifier. Unlocks the claims on Celtic lands.",
  f"{IRISH}\nhas_global_variable = eir_done_crowned",
  """every_ruler = {
	limit = {
		is_ai = yes
		culture ?= { has_cultural_pillar = heritage_brythonic }
	}
	add_opinion = { target = root modifier = eir_gael_pride_opinion opinion = 25 }
}
add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 15 }
add_prestige = 150
set_global_variable = eir_done_brotherhood""",
  cost="prestige = 150", cd=36500, major=True, pic="decision_social")

D("eir_reclaim_dal_riata_decision", "Reclaim Dál Riata",
  "Before there was a Scotland there was a Gaelic kingdom that spanned the North Channel. Its old counties are now ruled by strangers.",
  "Gain pressed claims on up to nine counties across Albany, the Isles and the Western Isles held by non-Celtic rulers.",
  f"{IRISH}\nhas_global_variable = eir_done_crowned",
  """eir_grant_claims_non_celtic_effect = { TITLE = d_albany }
eir_grant_claims_non_celtic_effect = { TITLE = d_the_isles }
eir_grant_claims_non_celtic_effect = { TITLE = d_western_isles }
add_prestige = 50
set_global_variable = eir_done_dalriata""",
  valid="is_at_war = no", cost="prestige = 200", cd=3650, pic="decision_destiny_goal")

D("eir_reclaim_man_isles_decision", "Reclaim Mann and the Isles",
  "The Isle of Man and the islands off the Scottish coast were Gaelic long before the Vikings came. They can be again.",
  "Gain pressed claims on up to three counties of Mann and the Isles held by non-Celtic rulers.",
  f"{IRISH}\nhas_global_variable = eir_done_crowned",
  """eir_grant_claims_non_celtic_effect = { TITLE = k_mann_the_isles }
add_prestige = 50""",
  valid="is_at_war = no", cost="prestige = 150", cd=3650, pic="decision_destiny_goal")

D("eir_reclaim_cornwall_decision", "Stand with Cornwall",
  "The Cornish speak a Celtic tongue and remember a time when the whole west was Celtic. Help them take their land back from English lords.",
  "Gain pressed claims on up to three counties of Cornwall held by non-Celtic rulers.",
  f"{IRISH}\nhas_global_variable = eir_done_brotherhood",
  """eir_grant_claims_non_celtic_effect = { TITLE = d_cornwall }
add_prestige = 50""",
  valid="is_at_war = no", cost="prestige = 150", cd=3650, pic="decision_destiny_goal")

D("eir_reclaim_armorica_decision", "Reclaim Armorica",
  "Brittany was settled by Britons fleeing the Saxons, and its tongue is cousin to Welsh and Cornish. Its lords look to Ireland for friendship.",
  "Gain pressed claims on up to three counties of Brittany held by non-Celtic rulers.",
  f"{IRISH}\nhas_global_variable = eir_done_brotherhood",
  """eir_grant_claims_non_celtic_effect = { TITLE = d_brittany }
add_prestige = 50""",
  valid="is_at_war = no", cost="prestige = 200", cd=3650, pic="decision_destiny_goal")

D("eir_reclaim_old_north_decision", "Reclaim the Old North",
  "Before the Angles came, the north of Britain spoke a Celtic tongue and had Celtic kings. Memory of the Hen Ogledd lives in every Welsh poem.",
  "Gain pressed claims on up to six counties in Northumberland and Lothian held by non-Celtic rulers.",
  f"{IRISH}\nhas_global_variable = eir_done_brotherhood",
  """eir_grant_claims_non_celtic_effect = { TITLE = d_northumberland }
eir_grant_claims_non_celtic_effect = { TITLE = d_lothian }
add_prestige = 50""",
  valid="is_at_war = no", cost="prestige = 250", cd=3650, pic="decision_destiny_goal")

D("eir_stand_with_wales_decision", "Stand with the Welsh",
  "The Welsh princes are Celtic kin, and the English crown presses on them from the east. A Gaelic king can take their side.",
  "Gain pressed claims on up to six Welsh-march counties held by non-Celtic rulers.",
  f"{IRISH}\nhas_global_variable = eir_done_brotherhood",
  """eir_grant_claims_non_celtic_effect = { TITLE = d_powys }
eir_grant_claims_non_celtic_effect = { TITLE = d_deheubarth }
add_prestige = 50""",
  valid="is_at_war = no", cost="prestige = 200", cd=3650, pic="decision_destiny_goal")

D("eir_proclaim_gaeldom_decision", "Proclaim the Empire of Gaeldom",
  "One High King of Ireland is a great thing. A king of kings over every Gaelic land from Cork to Caithness is greater still.",
  "Create the Empire of Gaeldom. Grants the Emperor of the Gael modifier, a huge prestige reward, and a dynasty modifier.",
  f"{IRISH}\nhas_title = title:k_ireland\nhas_global_variable = eir_done_brotherhood",
  """eir_create_title_effect = { TITLE = e_eir_gaeldom }
add_character_modifier = { modifier = eir_gaeldom_emperor_modifier years = 30 }
dynasty ?= { add_dynasty_modifier = { modifier = eir_house_high_kings_modifier years = 60 } }
add_prestige = 1000
add_piety = 200
eir_legend_title_effect = { TITLE = title:e_eir_gaeldom }
trigger_event = { id = eir.0112 days = 7 }""",
  valid="""eir_can_create_gaeldom_trigger = yes
NOT = { exists = title:e_eir_gaeldom.holder }""", cost="gold = major_gold_value\nprestige = 500", cd=36500, major=True, pic="decision_found_kingdom")

# =============================================================================
# PATH E - FAITH AND THE CHURCH
# =============================================================================
D("eir_endow_cashel_decision", "Endow the Rock of Cashel",
  "The limestone crag of Cashel was the seat of the kings of Munster. Give it to the Church, and the Church will remember.",
  "Raise the Rock of Cashel in the capital county of Munster, and gain piety and the blessing of the saints.",
  f"{IRISH}\nhas_title = title:d_munster",
  """eir_capital_county_modifier_effect = { TITLE = d_munster MODIFIER = eir_cashel_rock_modifier YEARS = 30 }
add_piety = 200
add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }
set_global_variable = eir_done_cashel""",
  valid="NOT = { has_global_variable = eir_done_cashel }", cost="gold = major_gold_value\npiety = 100", cd=36500, pic="decision_personal_religious")

D("eir_synod_rath_breasail_decision", "Convene the Synod of Ráth Breasail",
  "The Irish Church has no clear dioceses and no clear authority. Bring the bishops together and give it both.",
  "Reorganise the Irish Church for lasting clergy opinion and piety. The old Culdee monks will resent it.",
  f"{IRISH}\npiety >= 200",
  """add_character_modifier = { modifier = eir_synod_reform_modifier years = 15 }
add_character_modifier = { modifier = eir_culdee_strife_modifier years = 8 }
add_piety = 200
set_global_variable = eir_done_synod""",
  valid="NOT = { has_global_variable = eir_done_synod }", cost="piety = 200", cd=36500, major=True, pic="decision_major_religion")

D("eir_reconcile_culdees_decision", "Reconcile the Culdees and Rome",
  "The old monks and the Roman reformers have quarrelled for a generation. A generous gift to both might end it.",
  "Remove the Culdee Strife modifier and regain piety.",
  f"{IRISH}\nhas_character_modifier = eir_culdee_strife_modifier",
  """remove_character_modifier = eir_culdee_strife_modifier
add_piety = 100""",
  cost="gold = medium_gold_value", cd=1825, pic="decision_personal_religious")

D("eir_pilgrimage_skellig_decision", "Make the Pilgrimage to Skellig Michael",
  "Six hundred and fifty steps climb a sea-crag at the edge of the world. Monks have made the climb for centuries, and kings sometimes do.",
  "Gain piety, relief from stress, and the Pilgrim of Skellig modifier.",
  f"{IRISH}\npiety >= 50",
  """add_character_modifier = { modifier = eir_pilgrim_modifier years = 8 }
add_piety = 150""",
  valid="NOT = { has_character_modifier = eir_pilgrim_modifier }", cost="gold = minor_gold_value", cd=7300, pic="decision_personal_religious")

D("eir_armagh_primacy_decision", "Confirm the Primacy of Armagh",
  "Armagh is Saint Patrick's city, and the oldest see in Ireland. Declare its bishop first among all of them.",
  "Raise Armagh in the capital county of Ulster and gain piety.",
  f"{IRISH}\nhas_title = title:d_ulster",
  """eir_capital_county_modifier_effect = { TITLE = d_ulster MODIFIER = eir_armagh_see_modifier YEARS = 30 }
add_piety = 150
set_global_variable = eir_done_armagh""",
  valid="NOT = { has_global_variable = eir_done_armagh }", cost="gold = medium_gold_value\npiety = 100", cd=36500, pic="decision_personal_religious")

D("eir_patronise_glendalough_decision", "Patronise Glendalough",
  "Saint Kevin's valley is a place of pilgrimage and seclusion. A king's gift can make it a place of learning too.",
  "Raise Glendalough in the capital county of Leinster.",
  f"{IRISH}\nhas_title = title:d_leinster",
  """eir_capital_county_modifier_effect = { TITLE = d_leinster MODIFIER = eir_glendalough_modifier YEARS = 30 }
add_piety = 100""",
  cost="gold = medium_gold_value", cd=36500, pic="decision_personal_religious")

D("eir_restore_clonmacnoise_decision", "Restore Clonmacnoise",
  "On the banks of the Shannon, the greatest monastic city in Ireland has fallen into disrepair. Raise it again.",
  "Make the capital county of Connacht a monastic city.",
  f"{IRISH}\nhas_title = title:d_connacht",
  """eir_capital_county_modifier_effect = { TITLE = d_connacht MODIFIER = eir_monastic_city_modifier YEARS = 30 }
add_piety = 100""",
  cost="gold = medium_gold_value", cd=36500, pic="decision_personal_religious")

# =============================================================================
# PATH F - PROVINCIAL KINGDOMS AND SPECIAL PLACES
# =============================================================================
def kingdom_decision(key, kingdom, duchy, name, desc, tip, unlock, extra=""):
    D(key, name, desc, tip,
      f"{IRISH}\nhas_title = title:{duchy}",
      f"""eir_create_title_effect = {{ TITLE = {kingdom} }}
set_global_variable = {unlock}
dynasty ?= {{ add_dynasty_modifier = {{ modifier = eir_house_high_kings_modifier years = 25 }} }}
add_prestige = 200
eir_legend_title_effect = {{ TITLE = title:{kingdom} }}
trigger_event = {{ id = eir.0110 days = 7 }}
{extra}""",
      valid=f"""eir_can_create_provincial_kingdom_trigger = {{ DUCHY = {duchy} }}
NOT = {{ exists = title:{kingdom}.holder }}""",
      cost="gold = major_gold_value", cd=36500, major=True, pic="decision_found_kingdom")


kingdom_decision("eir_crown_king_of_munster_decision", "k_eir_munster", "d_munster",
                 "Crown the King of Munster",
                 "Munster was a kingdom before there was a High King, and it was a kingdom that gave Ireland Brian Boru. Take the crown of Cashel.",
                 "Create the Kingdom of Munster. Unlocks the Great Ringfort building.", "eir_unlock_ringfort")
kingdom_decision("eir_crown_king_of_ulster_decision", "k_eir_ulster", "d_ulster",
                 "Crown the King of Ulster",
                 "The Ulaid of the Red Branch are older than Tara. Their heirs can still raise a king at Emain Macha.",
                 "Create the Kingdom of Ulster. Unlocks the Crannóg Stronghold building.", "eir_unlock_crannog")
kingdom_decision("eir_crown_king_of_leinster_decision", "k_eir_leinster", "d_leinster",
                 "Crown the King of Leinster",
                 "The kings of Leinster have ruled the rich east for as long as there has been a Leinster. Place the crown on a new head.",
                 "Create the Kingdom of Leinster. Unlocks the Great Cattle Enclosure building.", "eir_unlock_cattle_enclosure")
kingdom_decision("eir_crown_king_of_connacht_decision", "k_eir_connacht", "d_connacht",
                 "Crown the King of Connacht",
                 "Connacht is a land of bogs, hills and fierce warriors, and its kings have raised many an Ard Rí.",
                 "Create the Kingdom of Connacht. Unlocks the High Cross building.", "eir_unlock_high_cross")
kingdom_decision("eir_crown_king_of_meath_decision", "k_eir_meath", "d_meath",
                 "Crown the King of Meath",
                 "The kings of Meath hold the middle of Ireland and the Hill of Tara, and the high kingship has been theirs more often than anyone's.",
                 "Create the Kingdom of Meath. Unlocks the Brehon Court building.", "eir_unlock_brehon_court",
                 "eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hill_modifier YEARS = 25 }")

D("eir_crown_king_of_dal_riata_decision", "Crown the King of Dál Riata",
  "Gaelic kings once ruled both sides of the North Channel. Gather the old counties and put a crown on the old kingdom.",
  "Create the Kingdom of Dál Riata, uniting your Irish and Scottish Gaelic lands.",
  f"{IRISH}\neir_can_create_dal_riata_trigger = yes",
  """eir_create_title_effect = { TITLE = k_eir_dal_riata }
add_prestige = 250
set_global_variable = eir_done_dalriata_crown""",
  valid="""eir_can_create_dal_riata_trigger = yes
NOT = { exists = title:k_eir_dal_riata.holder }""", cost="gold = major_gold_value", cd=36500, major=True, pic="decision_found_kingdom")

D("eir_raise_ringforts_decision", "Raise Ringforts Across the Land",
  "Every Irish lord lives in a ringfort, an earthen bank and ditch around a hall. Raise them in greater numbers, and in greater strength.",
  "Unlock the Great Ringfort, Crannóg Stronghold and Great Cattle Enclosure buildings, and gain the Builder of Dúns modifier.",
  IRISH,
  """set_global_variable = eir_unlock_ringfort
set_global_variable = eir_unlock_crannog
set_global_variable = eir_unlock_cattle_enclosure
add_character_modifier = { modifier = eir_dun_builder_modifier years = 15 }
capital_province ?= { add_province_modifier = { modifier = eir_ringfort_province_modifier years = 30 } }
add_prestige = 50""",
  cost="gold = major_gold_value", cd=36500, pic="decision_castle_view")

D("eir_claim_tara_hill_decision", "Keep the Vigil at Tara",
  "Spend a night alone on the Hill of Tara, where the kings of Ireland were once made, and see what the old place has to tell you.",
  "Raise the standing of Tara in your realm and gain the Vigil at Tara modifier.",
  f"{IRISH}\nhas_title = title:d_meath",
  """eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hill_modifier YEARS = 25 }
add_character_modifier = { modifier = eir_tara_vigil_modifier years = 10 }
add_prestige = 100
set_global_variable = eir_done_tara_vigil""",
  valid="NOT = { has_global_variable = eir_done_tara_vigil }", cost="prestige = 100", cd=36500, pic="decision_legend")


# =============================================================================
def build():
    import dec_extra  # noqa: F401  (registers the v0.3 decisions)
    L = Loc("eir_decisions_l_english.yml")
    out = ["# Eire Reborn - decisions. Generated by tools/gen_decisions.py\n\n"]
    for d in DEC:
        key = d["key"]
        out.append("%s = {\n" % key)
        out.append('\tpicture = {\n\t\treference = "gfx/interface/illustrations/decisions/%s.dds"\n\t}\n' % d["pic"])
        if d["major"]:
            out.append("\tdecision_group_type = major\n")
        out.append("\tai_check_interval = 0\n\tsort_order = 40\n")
        out.append("\tdesc = %s_desc\n\tselection_tooltip = %s_tooltip\n\tconfirm_text = %s_confirm\n\n" % (key, key, key))
        out.append("\tcooldown = { days = %d }\n\n" % d["cd"])
        out.append("\tis_shown = {\n%s\t}\n\n" % ind(d["shown"], 2))
        if d["valid"]:
            out.append("\tis_valid = {\n%s\t}\n\n" % ind(d["valid"], 2))
        out.append("\tis_valid_showing_failures_only = {\n\t\tis_available_adult = yes\n\t\tis_imprisoned = no\n\t}\n\n")
        if d["cost"]:
            out.append("\tcost = {\n%s\t}\n\n" % ind(d["cost"], 2))
        out.append("\teffect = {\n%s\t}\n\n" % ind(d["effect"], 2))
        out.append("\tai_will_do = {\n\t\tbase = 0\n\t}\n}\n\n")
        L.add(key, d["name"])
        L.add(key + "_desc", d["desc"])
        L.add(key + "_tooltip", d["tip"])
        L.add(key + "_confirm", d["name"])
    L.add("eir_gallowglass_company_name", "Gallowglass Company")
    write("common/decisions/eir_decisions.txt", "".join(out))
    L.write()
    print("decisions:", len(DEC))


if __name__ == "__main__":
    build()
