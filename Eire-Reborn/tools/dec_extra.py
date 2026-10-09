"""v0.3 decisions. Imported at the end of gen_decisions.py (before build())."""
from gen_decisions import D, IRISH, GAEL

CROWNED = IRISH + "\nhas_global_variable = eir_done_crowned"
FILI = IRISH + "\nhas_global_variable = eir_done_fili"
BROTHER = IRISH + "\nhas_global_variable = eir_done_brotherhood"
CASHEL = IRISH + "\nhas_global_variable = eir_done_cashel"
COAST = IRISH + "\neir_has_coast_trigger = yes"


def site(key, name, desc, tip, gate, county_mod, years, extra="", cost="gold = medium_gold_value", cd=7300, pic="decision_realm"):
    D(key, name, desc, tip, gate,
      "eir_held_county_modifier_effect = { MODIFIER = %s YEARS = %d }\nadd_prestige = 50\n%s" % (county_mod, years, extra),
      valid="any_held_title = { tier = tier_county }", cost=cost, cd=cd, pic=pic)


# =============================================================================
# STATECRAFT
# =============================================================================
D("eir_circuit_of_ireland_decision", "Ride the Circuit of Ireland",
  "A king who is never seen is soon forgotten. Ride through your lands with your household, eat at the lords' tables and be seen.",
  "Your counties and vassals warm to you. Chance of the Peacemaker of Tara trait. Starts the 'Circuit' incident chain.",
  CROWNED,
  """every_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_circuit_visit_modifier years = 5 }
}
add_character_modifier = { modifier = eir_royal_circuit_modifier years = 8 }
eir_vassal_opinion_effect = { MODIFIER = eir_circuit_host_opinion OPINION = 8 }
eir_trait_effect = { TRAIT = eir_peacemaker_of_tara OPPOSITE = wrathful CHANCE = 20 }
set_global_variable = eir_done_circuit
trigger_event = { id = eir.0160 days = 45 }""",
  valid="is_at_war = no", cost="gold = medium_gold_value", cd=3650, pic="decision_activity")

D("eir_take_hostages_decision", "Take the Hostages of Tara",
  "Every Irish king knows that the surest oath is a son at the king's table. Ask each of your vassals for one.",
  "Prestige and a tight leash, but vassals resent you. Release them later with another decision.",
  CROWNED + "\nNOT = { has_character_modifier = eir_hostages_modifier }",
  """add_character_modifier = { modifier = eir_hostages_modifier years = 12 }
eir_vassal_opinion_effect = { MODIFIER = eir_hostage_taken_opinion OPINION = -10 }
add_prestige = 100
set_global_variable = eir_done_hostages""", cd=3650, pic="decision_prison")

D("eir_release_hostages_decision", "Release the Hostages",
  "The sons have grown. Send them home with gifts and an oath.",
  "Removes the Hostages modifier and mends vassal opinion. Chance that a freed hostage becomes a Fosterling.",
  IRISH + "\nhas_character_modifier = eir_hostages_modifier",
  """remove_character_modifier = eir_hostages_modifier
eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 10 }
add_prestige = 25
trigger_event = { id = eir.0170 days = 30 }""", cost="gold = minor_gold_value", cd=1825, pic="decision_social")

D("eir_cain_law_decision", "Proclaim a Cáin",
  "A cáin is a law sworn by king and bishop together. This one protects clerics, women and the poor.",
  "Piety, clergy opinion, and the Cain Law modifier. Unlocks the Right of Sanctuary decision.",
  CASHEL + "\nNOT = { has_global_variable = eir_done_cain }",
  """add_character_modifier = { modifier = eir_cain_law_modifier years = 20 }
add_piety = 200
set_global_variable = eir_done_cain
trigger_event = { id = eir.0171 days = 90 }""", cost="piety = 150", cd=36500, pic="decision_personal_religious")

D("eir_provincial_oath_decision", "Take the Oath of the Provincial Kings",
  "Gather the great lords at the old place and have them swear on the relics.",
  "Dukes and above swear to you (+opinion) and your legitimacy grows.",
  CROWNED,
  """every_vassal = {
	limit = { highest_held_title_tier >= tier_duchy }
	add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 15 }
}
add_character_modifier = { modifier = eir_provincial_oath_modifier years = 12 }
add_prestige = 100""", cost="gold = medium_gold_value", cd=3650, pic="decision_legitimacy")

D("eir_feis_of_tara_decision", "Hold the Feis of Tara",
  "The Feis is the oldest festival of kingship: a week of feasting, law and marriage on the Hill of Tara.",
  "Needs the Hall of Tara rebuilt. Big prestige, long glow, and a feast event.",
  CROWNED + "\nhas_global_variable = eir_done_tara_hall",
  """add_character_modifier = { modifier = eir_feis_modifier years = 10 }
add_prestige = 250
eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 8 }
trigger_event = { id = eir.0051 days = 20 }""", cost="gold = major_gold_value", cd=7300, major=True, pic="decision_golden_age")

D("eir_rebuild_tara_hall_decision", "Rebuild the Hall of Tara",
  "The Hill of Tara has been empty for centuries. Raise a new hall of oak and thatch on the old banks.",
  "Needs the Duchy of Meath. A rebuilt-Hall county modifier. Unlocks the Feis and strengthens coronations.",
  CROWNED + "\nhas_title = title:d_meath\nNOT = { has_global_variable = eir_done_tara_hall }",
  """eir_capital_county_modifier_effect = { TITLE = d_meath MODIFIER = eir_tara_hall_modifier YEARS = 40 }
add_prestige = 150
set_global_variable = eir_done_tara_hall""", cost="gold = major_gold_value", cd=36500, major=True, pic="decision_found_kingdom")

D("eir_name_tanaiste_decision", "Name Your Tánaiste",
  "Name your successor-in-waiting while you live, and the family will argue a little less when you are gone.",
  "Needs a living heir. Legitimacy and vassal opinion.",
  IRISH + "\nexists = primary_heir",
  """add_character_modifier = { modifier = eir_tanaiste_modifier years = 15 }
primary_heir ?= { add_opinion = { target = root modifier = eir_oath_sworn_opinion opinion = 25 } }
add_prestige = 25""", cost="prestige = 50", cd=7300, pic="decision_dynasty_house")

D("eir_strike_claim_decision", "Strike a Claimant from the List",
  "A tanistry list is a list of everyone who might be king. There is a quiet way to make it shorter.",
  "A vassal loses his claim and hates you for it. Gives you a Tanistry Dispute modifier. Mend it with Name Your Tánaiste.",
  IRISH + "\nany_vassal = { count >= 1 }",
  """random_vassal = {
	add_opinion = { target = root modifier = eir_claim_revoked_opinion opinion = -25 }
}
add_character_modifier = { modifier = eir_tanistry_dispute_modifier years = 8 }
add_prestige = 50""", cd=1825, pic="decision_prison")

D("eir_cain_tribute_decision", "Levy the Cáin Tribute",
  "Every free man owes his king a calf from the herd. Send out the collectors.",
  "Income now, vassal resentment for years. The Waive the Cáin decision undoes it.",
  CROWNED + "\nNOT = { has_character_modifier = eir_cain_tribute_modifier }",
  """add_character_modifier = { modifier = eir_cain_tribute_modifier years = 8 }
add_gold = medium_gold_value""", cd=1825, pic="decision_spend_money")

D("eir_waive_cain_decision", "Waive the Cáin",
  "Forgive this year's calves. The people will remember.",
  "Removes the Cáin Tribute modifier and mends opinion.",
  IRISH + "\nhas_character_modifier = eir_cain_tribute_modifier",
  """remove_character_modifier = eir_cain_tribute_modifier
eir_vassal_opinion_effect = { MODIFIER = eir_wergild_paid_opinion OPINION = 6 }
add_prestige = 25""", cd=1825, pic="decision_social")

D("eir_wergild_decision", "Settle the Wergild",
  "Brehon law counts every killing in cows. Pay the honour-price, and the blood-feud is over.",
  "Removes Kin Strife and Infamous Cattle-Raider, and gives the Wergild Paid modifier.",
  IRISH + "\nOR = {\nhas_character_modifier = eir_kin_strife_modifier\nhas_character_modifier = eir_raider_infamy_modifier\n}",
  """if = {
	limit = { has_character_modifier = eir_kin_strife_modifier }
	remove_character_modifier = eir_kin_strife_modifier
}
if = {
	limit = { has_character_modifier = eir_raider_infamy_modifier }
	remove_character_modifier = eir_raider_infamy_modifier
}
add_character_modifier = { modifier = eir_wergild_peace_modifier years = 8 }
eir_vassal_opinion_effect = { MODIFIER = eir_wergild_paid_opinion OPINION = 6 }""", cost="gold = medium_gold_value", cd=1825, pic="decision_social")

D("eir_gaelic_court_decision", "Dress the Court in the Old Way",
  "Brooches, mantles, harps and long speeches. Make your hall look like the halls in the stories.",
  "Prestige and courtier opinion for ten years.",
  IRISH,
  """add_character_modifier = { modifier = eir_gaelic_court_modifier years = 10 }
add_prestige = 50
eir_court_opinion_effect = { MODIFIER = eir_poet_praise_opinion OPINION = 8 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_culture")

D("eir_name_ollamh_decision", "Name an Ollamh Rígh",
  "The Ollamh Rígh is the royal chief poet, who remembers every king, every battle and every debt.",
  "Learning and prestige for twenty years. Chance of the Poet-Prince trait if you are learned.",
  FILI + "\nNOT = { has_character_modifier = eir_royal_ollamh_modifier }",
  """add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 20 }
if = {
	limit = { learning >= 12 }
	eir_trait_effect = { TRAIT = eir_poet_prince OPPOSITE = lazy CHANCE = 30 }
}
add_prestige = 75""", cost="gold = medium_gold_value", cd=7300, pic="decision_tale")

D("eir_call_slogad_decision", "Call a Slógad",
  "The sluagh-hosting is the oldest duty of free men: when the king calls, every farmer brings a spear.",
  "Raises a free defensive army and a Great Hosting modifier.",
  IRISH + "\nis_at_war = no",
  """eir_defender_levy_effect = yes
add_character_modifier = { modifier = eir_hosting_modifier years = 4 }
add_prestige = 25""", cost="prestige = 75", cd=3650, pic="decision_recruitment")

D("eir_sanctuary_decision", "Grant the Right of Sanctuary",
  "No man may be seized within the bounds of a church, whatever he has done.",
  "Piety and clergy opinion, at a cost of some vassal opinion.",
  IRISH + "\nhas_global_variable = eir_done_cain",
  """add_character_modifier = { modifier = eir_sanctuary_modifier years = 15 }
add_piety = 100
eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -3 }""", cd=7300, pic="decision_personal_religious")

# =============================================================================
# CULTURE AND PLACES
# =============================================================================
D("eir_naming_customs_decision", "Revive the Old Names",
  "Name the children for saints and heroes, as the ancestors did: Brigid, Colmán, Fionn, Étaín.",
  "Opinion and dynastic prestige for twenty years.",
  IRISH,
  """add_character_modifier = { modifier = eir_naming_customs_modifier years = 20 }
add_prestige = 50""", cost="prestige = 50", cd=7300, pic="decision_dynasty_house")

D("eir_bardic_circuit_decision", "Send Out the Bardic Circuit",
  "Send poets to every hall in the land, carrying your name in their poems.",
  "Prestige and legend spread. Fires the Bardic Contest event.",
  FILI,
  """add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 10 }
add_prestige = 100
trigger_event = { id = eir.0130 days = 60 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_tale")

D("eir_harper_decision", "Appoint a Master Harper",
  "A king's harper plays the three strains: the sleep-strain, the sorrow-strain and the laughter-strain.",
  "Diplomacy and courtier opinion.",
  FILI,
  """add_character_modifier = { modifier = eir_harper_modifier years = 15 }
add_prestige = 25""", cost="gold = minor_gold_value", cd=7300, pic="decision_culture")

D("eir_teach_gaelic_decision", "Found Schools of the Gaelic Tongue",
  "Children learn to read in Irish as well as Latin.",
  "A held county gets a schooling modifier for twenty years.",
  IRISH,
  """eir_held_county_modifier_effect = { MODIFIER = eir_gaelic_schooling_modifier YEARS = 20 }
add_piety = 25""", valid="any_held_title = { tier = tier_county }", cost="gold = medium_gold_value", cd=3650, pic="decision_culture")

D("eir_sidhe_hosting_decision", "Honour the Hosting of the Sídhe",
  "Leave out milk on Samhain and speak of the good folk with respect.",
  "A modest prestige modifier, and the fairy-mound event may follow.",
  IRISH,
  """add_character_modifier = { modifier = eir_sidhe_hosting_modifier years = 6 }
add_prestige = 25
trigger_event = { id = eir.0037 days = 30 }""", cd=1825, pic="decision_legend")

D("eir_cult_brigid_decision", "Tend the Flame of Brigid",
  "At Kildare, the nuns of Brigid have kept a fire alight since before the church was built.",
  "The Flame of Brigid modifier and a county of the Flame of Kildare. Fires the Brigid event.",
  IRISH,
  """add_character_modifier = { modifier = eir_brigid_cult_modifier years = 15 }
eir_held_county_modifier_effect = { MODIFIER = eir_kildare_flame_modifier YEARS = 25 }
add_piety = 75
trigger_event = { id = eir.0031 days = 30 }""", valid="any_held_title = { tier = tier_county }", cost="gold = minor_gold_value", cd=7300, pic="decision_personal_religious")

D("eir_cult_colmcille_decision", "Honour Colmcille",
  "The saint of Iona, of Derry and of Kells. Every monastery he founded keeps his feast.",
  "Learning and piety. Needs a scriptorium.",
  IRISH + "\nhas_global_variable = eir_unlock_scriptorium",
  """add_character_modifier = { modifier = eir_colmcille_cult_modifier years = 15 }
add_piety = 100""", cost="piety = 50", cd=7300, pic="decision_personal_religious")

D("eir_cult_patrick_decision", "Honour Patrick of Armagh",
  "The apostle of Ireland, whose crozier and bell are kept at Armagh.",
  "Piety and clergy opinion. Needs Armagh's primacy.",
  IRISH + "\nhas_global_variable = eir_done_armagh",
  """add_character_modifier = { modifier = eir_patrick_cult_modifier years = 15 }
add_piety = 100
trigger_event = { id = eir.0043 days = 60 }""", cost="piety = 50", cd=7300, pic="decision_personal_religious")

D("eir_salmon_fisheries_decision", "Build the Salmon Weirs",
  "Stone weirs in the rivers trap the autumn run of salmon, and every table is richer.",
  "A held county gets Salmon Fisheries for 30 years. The Salmon of Knowledge may come up.",
  IRISH,
  """eir_held_county_modifier_effect = { MODIFIER = eir_salmon_fisheries_modifier YEARS = 30 }
add_prestige = 25
trigger_event = { id = eir.0036 days = 45 }""", valid="any_held_title = { tier = tier_county }", cost="gold = minor_gold_value", cd=7300, pic="decision_realm")

D("eir_yew_bows_decision", "Cut Yew for Bows",
  "The yew groves of the south make good bows, and an archer behind a shield-wall is a danger to any enemy.",
  "A modest archer damage bonus.",
  IRISH,
  """add_character_modifier = { modifier = eir_yew_bows_modifier years = 15 }""", cost="gold = minor_gold_value", cd=5475, pic="decision_smith")

D("eir_hurling_decision", "Lay Out the Hurling Fields",
  "Two parishes play against each other on a field half a mile long. By evening they are all friends.",
  "Opinion in a held county.",
  IRISH,
  """eir_held_county_modifier_effect = { MODIFIER = eir_hurling_fields_modifier YEARS = 20 }
add_prestige = 25""", valid="any_held_title = { tier = tier_county }", cost="gold = minor_gold_value", cd=5475, pic="decision_activity")

D("eir_peat_rights_decision", "Grant Peat-Cutting Rights",
  "The bogs give fuel, and sometimes more. Allow the farmers to cut turf in the common bog.",
  "A county gets Peat Wealth. A bog treasure may turn up.",
  IRISH,
  """eir_held_county_modifier_effect = { MODIFIER = eir_peat_wealth_modifier YEARS = 25 }
trigger_event = { id = eir.0038 days = 40 }""", valid="any_held_title = { tier = tier_county }", cost="gold = minor_gold_value", cd=5475, pic="decision_realm")

D("eir_wolfhound_kennels_decision", "Build the Wolfhound Kennels",
  "A great Irish wolfhound is worth the price of a good farm. Breed them to guard, to hunt and to impress.",
  "Prowess and prestige. Fires the Wolfhound event.",
  IRISH,
  """add_character_modifier = { modifier = eir_wolfhound_kennels_modifier years = 15 }
add_prestige = 25
trigger_event = { id = eir.0050 days = 20 }""", cost="gold = medium_gold_value", cd=5475, pic="decision_pet_dog")

site("eir_uisneach_decision", "Light the Fire at Uisneach",
     "The Hill of Uisneach is the navel of Ireland, where the first Beltane fire was lit.",
     "Uisneach modifier on a held county.", IRISH, "eir_uisneach_modifier", 30)
site("eir_newgrange_decision", "Protect Newgrange",
     "A passage tomb older than the pyramids, aligned to the midwinter sunrise.",
     "Newgrange modifier on a held county.", IRISH, "eir_newgrange_modifier", 30)
site("eir_rathcroghan_decision", "Restore Rathcroghan",
     "The ritual capital of Connacht, where Queen Medb once held court.",
     "Rathcroghan modifier on a held county.", IRISH, "eir_rathcroghan_modifier", 30)
site("eir_navan_decision", "Restore Emain Macha",
     "The old royal site of the Ulaid, with its ditch and its mound and its stories.",
     "Navan Fort modifier on a held county.", IRISH, "eir_navan_fort_modifier", 30)
site("eir_dunadd_decision", "Restore Dunadd",
     "The rock-fort of Dál Riata, where kings put their feet in a carved footprint.",
     "Dunadd modifier on a held county. Needs the Dál Riata reclaim.", IRISH + "\nhas_global_variable = eir_done_dalriata",
     "eir_dunadd_modifier", 30)
site("eir_monasterboice_decision", "Raise the Crosses of Monasterboice",
     "A monastery whose high crosses are carved from top to bottom with scenes from scripture.",
     "Monasterboice modifier on a held county. Needs the high crosses.", IRISH + "\nhas_global_variable = eir_unlock_high_cross",
     "eir_monasterboice_modifier", 30)
site("eir_armagh_library_decision", "Fill the Library of Armagh",
     "Armagh's library is the greatest in Ireland, and scholars come from the Continent to read in it.",
     "Armagh's Library modifier on a held county. Needs Armagh's primacy.", IRISH + "\nhas_global_variable = eir_done_armagh",
     "eir_armagh_library_modifier", 30)
site("eir_wooden_harbours_decision", "Build the Wooden Harbours",
     "Quays and warehouses of oak timber for the trading ships.",
     "Wooden Harbours modifier on a held county. Needs a coast.", COAST, "eir_wooden_harbour_modifier", 30)

# =============================================================================
# MILITARY
# =============================================================================
D("eir_ceithern_decision", "Raise the Royal Ceithern",
  "A king's ceithern are the picked men of his household, who eat at his table and die at his door.",
  "Unlocks the Ceithern Retinue men-at-arms for all Gaelic rulers.",
  CROWNED + "\nNOT = { has_global_variable = eir_unlock_ceithern }",
  """set_global_variable = eir_unlock_ceithern
add_prestige = 100""", cost="gold = medium_gold_value", cd=36500, pic="decision_recruitment")

D("eir_coastal_watch_decision", "Post Watchmen on the Headlands",
  "Beacon fires on every headland will warn of a fleet while it is still at sea.",
  "Coastal counties get a Coastal Watch modifier and the beacon on their provinces.",
  COAST,
  """every_held_title = {
	limit = {
		tier = tier_county
		is_coastal_county = yes
	}
	add_county_modifier = { modifier = eir_coast_watch_county_modifier years = 25 }
	title_province = { add_province_modifier = { modifier = eir_beacon_province_modifier years = 25 } }
}
add_character_modifier = { modifier = eir_watchtowers_modifier years = 15 }""", cost="gold = medium_gold_value", cd=7300, pic="decision_castle_view")

D("eir_border_muster_decision", "Call the Border Muster",
  "Call the farmers on the march to man the old ditch-and-bank line.",
  "A free defensive army at your capital.",
  IRISH + "\nis_at_war = no",
  """eir_defender_levy_effect = yes
add_prestige = 10""", cost="gold = minor_gold_value", cd=1825, pic="decision_recruitment")

D("eir_hillfort_decision", "Rebuild the Hill-Forts",
  "Every ridge in Ireland has a ringfort, and many are in ruin. Clear them, dig the banks and cut new stakes.",
  "A ringfort province modifier in a held county.",
  IRISH,
  """random_held_title = {
	limit = { tier = tier_county }
	title_province = { add_province_modifier = { modifier = eir_ringfort_province_modifier years = 40 } }
}
add_prestige = 25""", valid="any_held_title = { tier = tier_county }", cost="gold = medium_gold_value", cd=5475, pic="decision_castle_view")

D("eir_dublin_garrison_decision", "Garrison Dublin",
  "A fortress on the Liffey is a gift and a burden. Fill it with men who know how to hold it.",
  "Dublin gets a gallowglass garrison for twenty years. A Norse champion may soon challenge you.",
  IRISH + "\nhas_global_variable = eir_done_dublin",
  """title:c_dublin ?= { add_county_modifier = { modifier = eir_gallowglass_garrison_modifier years = 20 } }
add_prestige = 50
trigger_event = { id = eir.0151 days = 90 }""", cost="gold = medium_gold_value", cd=7300, pic="decision_castle_view")

D("eir_norse_captain_decision", "Hire a Norse Sea-King",
  "Some Norse lords will fight for any Irish king who pays. They are expensive, and loyalty to them is a currency.",
  "Spawns a mercenary host and raises your Norse-Gael ties for four years.",
  COAST,
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
add_character_modifier = { modifier = eir_foreign_lords_modifier years = 4 }""", cost="gold = major_gold_value", cd=3650, pic="decision_recruitment")

D("eir_champions_portion_decision", "Award the Champion's Portion",
  "The best cut of the roast goes to the greatest warrior in the hall. He earns it, and he often has to fight for it.",
  "Prowess and prestige for eight years.",
  IRISH,
  """add_character_modifier = { modifier = eir_champions_portion_modifier years = 8 }""", cost="gold = minor_gold_value", cd=3650, pic="decision_smith")

D("eir_dun_drill_decision", "Drill the Garrisons",
  "Behind the ringfort banks, every spring, men practise spear and shield.",
  "Martial and knight effectiveness for six years.",
  IRISH,
  """add_character_modifier = { modifier = eir_dun_drill_modifier years = 6 }""", cost="gold = minor_gold_value", cd=2190, pic="decision_recruitment")

D("eir_four_provinces_decision", "Hosting of the Four Provinces",
  "Munster, Leinster, Connacht and Ulster, each under their king, behind a single banner.",
  "Two defensive hosts, a Great Hosting modifier and a legend. Needs the Óenach and the Muster.",
  CROWNED + "\nhas_global_variable = eir_done_muster\nhas_global_variable = eir_done_oenach",
  """eir_defender_levy_effect = yes
eir_defender_levy_effect = yes
add_character_modifier = { modifier = eir_hosting_modifier years = 6 }
add_prestige = 250
eir_legend_title_effect = { TITLE = primary_title }
trigger_event = { id = eir.0172 days = 60 }""", cost="gold = major_gold_value", cd=14600, major=True, pic="decision_recruitment")

D("eir_single_combat_decision", "Issue a Challenge to Single Combat",
  "In the old days, two kings might settle a war between two champions. Send the challenge.",
  "A duel with a Norse champion. Win, and gain prestige and the Champion of Ulster trait. Lose, and bleed.",
  IRISH + "\nprowess >= 10",
  """trigger_event = { id = eir.0151 days = 5 }""", valid="is_at_war = no", cost="prestige = 50", cd=3650, pic="decision_knight_kneeling")

# =============================================================================
# FAITH
# =============================================================================
D("eir_found_monastery_decision", "Found a Monastery",
  "A house of prayer, a scriptorium and a guest hall. The Church will bless your name.",
  "A county gets a New Monastery modifier. Piety and clergy opinion.",
  IRISH,
  """eir_held_county_modifier_effect = { MODIFIER = eir_monastery_county_modifier YEARS = 40 }
add_character_modifier = { modifier = eir_monastery_founder_modifier years = 15 }
add_piety = 200""", valid="any_held_title = { tier = tier_county }", cost="gold = major_gold_value", cd=7300, pic="decision_personal_religious")

D("eir_scriptorium_patron_decision", "Patronise the Scriptorium",
  "The monks need vellum, ink, gold leaf and peace. You can provide all four.",
  "Learning and prestige. A small gospel book may be finished within three years.",
  IRISH + "\nhas_global_variable = eir_unlock_scriptorium",
  """add_character_modifier = { modifier = eir_scriptorium_patron_modifier years = 8 }
add_piety = 50
trigger_event = { id = eir.0153 years = 3 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_tale")

D("eir_hermit_cell_decision", "Endow a Hermit's Cell",
  "Some men live alone on the edge of the world, praying. Pay for one, and he may bless you.",
  "A small blessing. The Hermit's Prophecy event may follow.",
  IRISH,
  """add_character_modifier = { modifier = eir_hermit_blessing_modifier years = 5 }
add_piety = 75
trigger_event = { id = eir.0045 days = 120 }""", cost="gold = minor_gold_value", cd=3650, pic="decision_personal_religious")

D("eir_relic_procession_decision", "Carry the Relic Through the Land",
  "The shrine of a saint is carried from county to county, and the people kneel as it passes.",
  "Every held county gets a short Relic Passed Through modifier. Needs the Rock of Cashel.",
  CASHEL,
  """every_held_title = {
	limit = { tier = tier_county }
	add_county_modifier = { modifier = eir_relic_procession_county_modifier years = 5 }
}
add_character_modifier = { modifier = eir_relic_procession_modifier years = 8 }
add_piety = 100""", cost="piety = 75", cd=3650, pic="decision_personal_religious")

D("eir_penance_decision", "Do Public Penance",
  "Barefoot, in a plain shirt, on the church steps. The people watch, and some of them weep.",
  "Lowers stress considerably and gives the Penance Done modifier. Costs prestige.",
  IRISH + "\nstress >= 50",
  """add_stress = -80
add_character_modifier = { modifier = eir_penance_done_modifier years = 6 }
add_prestige = -75
add_piety = 100""", cd=1825, pic="decision_personal_religious")

D("eir_rome_pilgrimage_decision", "Go on Pilgrimage to Rome",
  "A year's walk and a year's walk back. It is a long way to go to be forgiven.",
  "A risky journey with a chance of the Saint-King trait. Fires the Pilgrim to Rome event.",
  IRISH + "\npiety >= 200",
  """trigger_event = { id = eir.0152 days = 30 }""", valid="is_at_war = no", cost="gold = major_gold_value", cd=36500, major=True, pic="decision_personal_religious")

# =============================================================================
# CELTIC WORLD
# =============================================================================
D("eir_embassy_gwynedd_decision", "Send an Embassy to Gwynedd",
  "The princes of Gwynedd keep a hard, rocky land, and a fine tradition of poetry. Send them gifts and a proposal.",
  "Fires the Gwynedd alliance event. Needs the Celtic Brotherhood.",
  BROTHER,
  """add_prestige = 25
trigger_event = { id = eir.0154 days = 60 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_social")

D("eir_embassy_strathclyde_decision", "Send an Embassy to Strathclyde",
  "The last of the northern Britons hold a rock-fort on the Clyde. Treat them as kin.",
  "Fires the Strathclyde alliance event. Needs the Celtic Brotherhood.",
  BROTHER,
  """add_prestige = 25
trigger_event = { id = eir.0155 days = 60 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_social")

D("eir_pictish_memory_decision", "Honour the Memory of the Picts",
  "The painted people were here before the Gael, and their stones still stand in Alba. Honour them.",
  "Prestige, and pressed claims on up to three Pictish-land counties held by non-Celtic rulers.",
  BROTHER,
  """add_character_modifier = { modifier = eir_pictish_memory_modifier years = 15 }
eir_grant_claims_non_celtic_effect = { TITLE = k_scotland }
add_prestige = 100""", cost="gold = medium_gold_value", cd=14600, pic="decision_legend")

D("eir_breton_refuge_decision", "Offer Refuge to Breton Exiles",
  "Brittany has fallen to foreign lords again, and its nobles are looking for a safe harbour.",
  "A hospitality modifier. A Breton refugee will arrive in a year.",
  BROTHER,
  """add_character_modifier = { modifier = eir_breton_refuge_modifier years = 10 }
add_prestige = 75
trigger_event = { id = eir.0158 years = 1 }""", cost="gold = minor_gold_value", cd=7300, pic="decision_social")

D("eir_armorica_voyage_decision", "Send a Ship to Armorica",
  "Ships can reach Brittany in four days with a fair wind and a stout hull.",
  "A risky voyage. Fires the Armorican Voyage event.",
  BROTHER + "\neir_has_coast_trigger = yes",
  """add_prestige = 10
trigger_event = { id = eir.0157 days = 40 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_activity")

D("eir_gaulish_heritage_decision", "Remember the Gauls",
  "Before Rome, the Celts ruled from the Danube to the Atlantic. Some of that land should be remembered.",
  "A prestige modifier and pressed claims on up to three counties of Anjou held by non-Celtic rulers.",
  BROTHER,
  """add_character_modifier = { modifier = eir_gaulish_heritage_modifier years = 15 }
eir_grant_claims_non_celtic_effect = { TITLE = d_anjou }
add_prestige = 100""", cost="gold = medium_gold_value", cd=14600, pic="decision_legend")

D("eir_britannia_restored_decision", "Restore Britannia",
  "The island of Britain was once all Celtic. A king who rules the Gaelic west, and calls the Welsh and Cornish kin, may reclaim it.",
  "Huge prestige and vassal opinion. Pressed claims on up to three counties of England. A great legend. Needs the Brotherhood, the Dál Riata reclaim and a crown.",
  BROTHER + "\nhas_global_variable = eir_done_dalriata\nhas_global_variable = eir_done_crowned",
  """add_character_modifier = { modifier = eir_britannia_modifier years = 25 }
eir_grant_claims_non_celtic_effect = { TITLE = k_england }
eir_legend_title_effect = { TITLE = primary_title }
add_prestige = 500""", cost="gold = major_gold_value\nprestige = 300", cd=36500, major=True, pic="decision_found_kingdom")

D("eir_isles_fleet_decision", "Build the Fleet of the Isles",
  "The galleys of the Hebrides carry sixty oars. Build twenty.",
  "Income and prestige. Needs a coast.",
  COAST,
  """add_character_modifier = { modifier = eir_island_fleet_modifier years = 15 }
add_prestige = 50""", cost="gold = major_gold_value", cd=7300, pic="decision_spend_money")

D("eir_hebridean_marriage_decision", "Arrange a Hebridean Marriage",
  "The galley-lords of the Isles will serve a king who marries into their families.",
  "Fires the Hebridean marriage event.",
  COAST,
  """trigger_event = { id = eir.0156 days = 45 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_social")

D("eir_commission_tale_decision", "Commission a Tale",
  "Your poets know a hundred tales. Choose the one your court will hear all year.",
  "Choose among six tales (Salmon, Cú Chulainn, Finn, Medb, Lir, Brendan) for a different bonus each.",
  FILI,
  """trigger_event = { id = eir.0150 days = 5 }""", cost="gold = medium_gold_value", cd=3650, pic="decision_tale")
