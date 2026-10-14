"""Update 9: the three casus belli that answer a raid. Writes:
  common/casus_belli_types/eir_casus_belli_raids.txt   Avenge the Raid, Demand the Blood-Price, Drive Out the Settlers
  localization/english/eir_cb2_l_english.yml
They use the variable eir_revenge_target (set on the victim by the raid events, 10-20 years) and the county modifier eir_raider_settlement_modifier
(set by the Settle the Raided Land event). The AI never uses them."""
from eir_lib import *
from gen_cb import HEAD_ALLOWED, COMMON_DESC

# every war boilerplate that the three share
TAIL_COMMON = """	on_primary_attacker_death = inherit
	on_primary_defender_death = inherit
	attacker_allies_inherit = yes
	defender_allies_inherit = yes
"""

AVENGE = """eir_raid_revenge_cb = {
	group = conquest
	icon = county_conquest_cb
	ai = no

	combine_into_one = yes
	should_show_war_goal_subview = yes
	mutually_exclusive_titles = { always = yes }
	interface_priority = 75

	attacker_score_from_occupation_scale = 150
	attacker_score_from_battles_scale = 150
	defender_score_from_battles_scale = 150

	allowed_for_character = {
		is_landed = yes
		has_variable = eir_revenge_target
		NOT = { government_has_flag = government_is_landless_adventurer }
	}

	allowed_for_character_display_regardless = {
		tgp_japan_offensive_wars_ban_trigger = yes
	}

	allowed_against_character = {
		scope:attacker = {
			has_variable = eir_revenge_target
			var:eir_revenge_target = scope:defender
		}
	}

	target_titles = all
	target_title_tier = county
	ignore_effect = change_title_holder

	valid_to_start = {
		scope:target = {
			is_landless_type_title = no
			neighboring_county_or_viking_conquest_trigger = { CHARACTER = root }
		}
	}

	should_invalidate = {
		NOT = {
			any_in_list = {
				list = target_titles
				any_in_de_jure_hierarchy = {
					tier = tier_county
					holder = {
						OR = {
							this = scope:defender
							target_is_liege_or_above = scope:defender
						}
					}
				}
			}
		}
	}

	on_invalidated_desc = eir_raid_revenge_cb_invalidated_desc
	on_invalidated = {}

	cost = {
		prestige = {
			value = minor_prestige_value
			multiply = common_cb_prestige_cost_multiplier
		}
	}

%(decl)s
	on_victory_desc = {
		first_valid = {
			triggered_desc = {
				trigger = { scope:attacker = { is_local_player = yes } }
				desc = eir_raid_revenge_cb_victory_desc_attacker
			}
			desc = eir_raid_revenge_cb_victory_desc
		}
	}

	on_victory = {
		add_legitimacy_attacker_victory_effect = yes
		scope:attacker = {
			add_gold = medium_gold_value
			add_prestige = medium_prestige_gain
			remove_variable = eir_revenge_target
			remove_character_modifier = eir_revenge_vow_modifier
		}
		scope:defender = {
			remove_short_term_gold = minor_gold_value
		}
		create_title_and_vassal_change = {
			type = conquest
			save_scope_as = change
			add_claim_on_loss = yes
		}
		every_in_list = {
			list = target_titles
			change_title_holder = {
				holder = scope:attacker
				change = scope:change
			}
		}
		resolve_title_and_vassal_change = scope:change
		every_in_list = {
			list = target_titles
			change_development_level = -2
		}
		modify_allies_of_participants_fame_values = {
			WINNER = scope:attacker
			FAME_BASE = minor_prestige_value
			IS_RELIGIOUS_WAR = no
			WINNER_ALLY_FAME_SCALE = 1
			LOSER_ALLY_FAME_SCALE = 1
		}
		add_truce_attacker_victory_effect = yes
	}

	on_white_peace_desc = {
		first_valid = {
			desc = eir_raid_revenge_cb_white_peace_desc
		}
	}

	on_white_peace = {
		scope:attacker = {
			add_prestige = {
				value = minor_prestige_value
				multiply = -1.0
			}
		}
		add_truce_white_peace_effect = yes
	}

	on_defeat_desc = {
		first_valid = {
			desc = eir_raid_revenge_cb_defeat_desc
		}
	}

	on_defeat = {
		add_legitimacy_attacker_defeat_effect = yes
		scope:defender = {
			add_prestige_war_defender_effect = {
				PRESTIGE_VALUE = medium_prestige_value
			}
		}
		scope:attacker = {
			pay_short_term_gold_reparations_effect = {
				GOLD_VALUE = 1
			}
			add_prestige = medium_prestige_loss
		}
		add_truce_attacker_defeat_effect = yes
		scope:attacker = {
			save_temporary_scope_as = loser
		}
		on_lost_aggression_war_discontent_loss = yes
	}

	transfer_behavior = transfer
%(tail)s
	war_name = "EIR_RAID_REVENGE_WAR_NAME"
	war_name_base = "EIR_RAID_REVENGE_WAR_NAME_BASE"
	cb_name = "EIR_RAID_REVENGE_CB_NAME"

	use_de_jure_wargoal_only = yes
	attacker_wargoal_percentage = 0.8
	max_defender_score_from_occupation = 150
	max_attacker_score_from_occupation = 150
}

"""

BLOOD_PRICE = """eir_blood_price_cb = {
	group = subjugation
	icon = make_tributary_cb
	ai = no
	ai_only_against_neighbors = yes

	attacker_score_from_occupation_scale = 150
	attacker_score_from_battles_scale = 150
	defender_score_from_battles_scale = 150

	allowed_for_character = {
		is_landed = yes
		has_variable = eir_revenge_target
		NOT = { government_has_flag = government_is_landless_adventurer }
	}

	allowed_for_character_display_regardless = {
		tgp_japan_offensive_wars_ban_trigger = yes
	}

	allowed_against_character = {
		scope:attacker = {
			has_variable = eir_revenge_target
			var:eir_revenge_target = scope:defender
		}
		scope:defender = {
			is_landed = yes
		}
	}

	cost = {
		prestige = {
			value = minor_prestige_value
			multiply = common_cb_prestige_cost_multiplier
		}
	}

	should_invalidate = {
		scope:defender = {
			is_landed = no
		}
	}

%(decl)s
	on_invalidated_desc = eir_blood_price_cb_invalidated_desc
	on_invalidated = {}

	on_victory_desc = {
		first_valid = {
			triggered_desc = {
				trigger = { scope:attacker = { is_local_player = yes } }
				desc = eir_blood_price_cb_victory_desc_attacker
			}
			desc = eir_blood_price_cb_victory_desc
		}
	}

	on_victory = {
		scope:attacker = {
			add_gold = major_gold_value
			add_prestige = medium_prestige_gain
			remove_variable = eir_revenge_target
			remove_character_modifier = eir_revenge_vow_modifier
			add_hook = {
				target = scope:defender
				type = favor_hook
			}
		}
		scope:defender = {
			remove_short_term_gold = medium_gold_value
			add_prestige = minor_prestige_loss
			add_character_modifier = {
				modifier = eir_owes_cain_modifier
				years = 5
			}
		}
		modify_allies_of_participants_fame_values = {
			WINNER = scope:attacker
			FAME_BASE = medium_prestige_value
			IS_RELIGIOUS_WAR = no
			WINNER_ALLY_FAME_SCALE = 1
			LOSER_ALLY_FAME_SCALE = 1
		}
		add_truce_attacker_victory_effect = yes
	}

	on_white_peace_desc = {
		first_valid = {
			desc = eir_blood_price_cb_white_peace_desc
		}
	}

	on_white_peace = {
		scope:attacker = {
			add_prestige = {
				value = minor_prestige_value
				multiply = -1.0
			}
		}
		add_truce_white_peace_effect = yes
	}

	on_defeat_desc = {
		first_valid = {
			desc = eir_blood_price_cb_defeat_desc
		}
	}

	on_defeat = {
		scope:defender = {
			add_prestige_war_defender_effect = {
				PRESTIGE_VALUE = medium_prestige_value
			}
		}
		scope:attacker = {
			pay_short_term_gold_reparations_effect = {
				GOLD_VALUE = 2
			}
			add_prestige = major_prestige_loss
		}
		add_truce_attacker_defeat_effect = yes
		scope:attacker = {
			save_temporary_scope_as = loser
		}
		on_lost_aggression_war_discontent_loss = yes
	}

%(tail)s
	war_name = "EIR_BLOOD_PRICE_WAR_NAME"
	war_name_base = "EIR_BLOOD_PRICE_WAR_NAME_BASE"
	cb_name = "EIR_BLOOD_PRICE_CB_NAME"
	interface_priority = 57

	ticking_war_score_targets_entire_realm = yes
	max_defender_score_from_occupation = 150
	max_attacker_score_from_occupation = 150
	attacker_ticking_warscore = 0
	attacker_wargoal_percentage = 0.8
	max_ai_diplo_distance_to_title = 500
}

"""

SETTLERS = """eir_reclaim_settled_cb = {
	group = conquest
	icon = county_conquest_cb
	ai = no

	combine_into_one = yes
	should_show_war_goal_subview = yes
	mutually_exclusive_titles = { always = yes }
	interface_priority = 76

	attacker_score_from_occupation_scale = 150
	attacker_score_from_battles_scale = 150
	defender_score_from_battles_scale = 150

	allowed_for_character = {
%(head)s	}

	allowed_for_character_display_regardless = {
		tgp_japan_offensive_wars_ban_trigger = yes
	}

	allowed_against_character = {
		scope:attacker = {
			ALL_FALSE = {
				top_liege = scope:defender.top_liege
				liege = scope:defender
			}
		}
		scope:defender = {
			any_sub_realm_county = {
				has_county_modifier = eir_raider_settlement_modifier
			}
		}
	}

	target_titles = all
	target_title_tier = county
	ignore_effect = change_title_holder

	valid_to_start = {
		scope:target = {
			is_landless_type_title = no
			has_county_modifier = eir_raider_settlement_modifier
		}
	}

	should_invalidate = {
		NOT = {
			any_in_list = {
				list = target_titles
				any_in_de_jure_hierarchy = {
					tier = tier_county
					holder = {
						OR = {
							this = scope:defender
							target_is_liege_or_above = scope:defender
						}
					}
				}
			}
		}
	}

	on_invalidated_desc = eir_reclaim_settled_cb_invalidated_desc
	on_invalidated = {}

	cost = {
		prestige = {
			value = minor_prestige_value
			multiply = common_cb_prestige_cost_multiplier
		}
	}

%(decl)s
	on_victory_desc = {
		first_valid = {
			triggered_desc = {
				trigger = { scope:attacker = { is_local_player = yes } }
				desc = eir_reclaim_settled_cb_victory_desc_attacker
			}
			desc = eir_reclaim_settled_cb_victory_desc
		}
	}

	on_victory = {
		add_legitimacy_attacker_victory_effect = yes
		create_title_and_vassal_change = {
			type = conquest
			save_scope_as = change
			add_claim_on_loss = yes
		}
		every_in_list = {
			list = target_titles
			change_title_holder = {
				holder = scope:attacker
				change = scope:change
			}
		}
		resolve_title_and_vassal_change = scope:change
		every_in_list = {
			list = target_titles
			remove_county_modifier = eir_raider_settlement_modifier
			set_county_culture = scope:attacker.culture
			set_county_faith = scope:attacker.faith
		}
		scope:attacker = {
			add_prestige = medium_prestige_gain
			add_piety = minor_piety_gain
		}
		modify_allies_of_participants_fame_values = {
			WINNER = scope:attacker
			FAME_BASE = minor_prestige_value
			IS_RELIGIOUS_WAR = no
			WINNER_ALLY_FAME_SCALE = 1
			LOSER_ALLY_FAME_SCALE = 1
		}
		add_truce_attacker_victory_effect = yes
	}

	on_white_peace_desc = {
		first_valid = {
			desc = eir_reclaim_settled_cb_white_peace_desc
		}
	}

	on_white_peace = {
		scope:attacker = {
			add_prestige = {
				value = minor_prestige_value
				multiply = -1.0
			}
		}
		add_truce_white_peace_effect = yes
	}

	on_defeat_desc = {
		first_valid = {
			desc = eir_reclaim_settled_cb_defeat_desc
		}
	}

	on_defeat = {
		add_legitimacy_attacker_defeat_effect = yes
		scope:defender = {
			add_prestige_war_defender_effect = {
				PRESTIGE_VALUE = medium_prestige_value
			}
		}
		scope:attacker = {
			pay_short_term_gold_reparations_effect = {
				GOLD_VALUE = 1
			}
			add_prestige = medium_prestige_loss
		}
		add_truce_attacker_defeat_effect = yes
		scope:attacker = {
			save_temporary_scope_as = loser
		}
		on_lost_aggression_war_discontent_loss = yes
	}

	transfer_behavior = transfer
%(tail)s
	war_name = "EIR_RECLAIM_SETTLED_WAR_NAME"
	war_name_base = "EIR_RECLAIM_SETTLED_WAR_NAME_BASE"
	cb_name = "EIR_RECLAIM_SETTLED_CB_NAME"

	use_de_jure_wargoal_only = yes
	attacker_wargoal_percentage = 0.8
	max_defender_score_from_occupation = 150
	max_attacker_score_from_occupation = 150
}
"""

TEXT = [
    ("eir_raid_revenge_cb", "RAID_REVENGE", "Avenge the Raid",
     "You swore on the relics to repay a raid. Now you may march into the raider's land and take a county from him, with a blood-price in gold, and he will lose development there.",
     "Avenge the Raid on [DEFENDER.GetShortUIName]", "[ATTACKER.GetPrimaryTitle.GetAdjective] Revenge on [TITLE.GetBaseNameNoTier]",
     "You take the contested [titles|E], a blood-price in gold, and the county loses development.", "[attacker.GetShortUIName|U] avenges the raid and takes the contested [title|E].",
     "The war ends in a truce and the vow is not repaid. The poets will remember.", "[defender.GetShortUIName|U] keeps the contested [title|E]. The vow is not repaid.",
     "The [war.GetName] has ended: [defender.GetShortUIName] no longer [Select_CString( defender.IsLocalPlayer, 'control', 'controls' )] the County."),
    ("eir_blood_price_cb", "BLOOD_PRICE", "Demand the Blood-Price",
     "The old law says that a raid is a debt. A king who was raided may demand the price in cattle and silver, and the raider cannot refuse without shame.",
     "Demand the Blood-Price of [DEFENDER.GetShortUIName]", "[ATTACKER.GetPrimaryTitle.GetAdjective] Blood-Price from [DEFENDER.GetPrimaryTitle.GetName]",
     "[defender.GetShortUIName|U] pays the blood-price in gold now, owes tribute for five years and gives you a hook.", "[attacker.GetShortUIName|U] collects the blood-price from [defender.GetShortUIName|U].",
     "The demand is dropped and nothing is paid.", "The demand is refused and the army beaten. You lose [prestige|E] and pay compensation.",
     "The [war.GetName] has ended: [defender.GetShortUIName] is no longer a landed ruler."),
    ("eir_reclaim_settled_cb", "RECLAIM_SETTLED", "Drive Out the Settlers",
     "Raiders have settled on land that was yours or your kin's, and given it their language and their gods. Drive them out and put the old names back.",
     "Drive Out the Settlers of [TITLE.GetBaseNameNoTier]", "[ATTACKER.GetPrimaryTitle.GetAdjective] Reclamation of [TITLE.GetBaseName]",
     "You take back the settled county: the settlement ends, and its culture and faith return to yours.", "[attacker.GetShortUIName|U] drives out the settlers and takes back the contested [title|E].",
     "The settlers keep the county for now.", "[defender.GetShortUIName|U] keeps the settled county. Its people do not forgive.",
     "The [war.GetName] has ended: the county is no longer a raiders' settlement."),
]


def build():
    L = Loc("eir_cb2_l_english.yml")
    L.section("casus belli that answer a raid")
    fmt = dict(decl=COMMON_DESC, tail=TAIL_COMMON, head=HEAD_ALLOWED)
    text = "# Eire Reborn - casus belli that answer a raid. Generated by tools/gen_cb2.py\n\n" + (AVENGE % fmt) + (BLOOD_PRICE % fmt) + (SETTLERS % fmt)
    for key, up, name, desc, cbn, warn, vatt, vgen, wp, de, inv in TEXT:
        U = "EIR_" + up
        L.add(key, name)
        L.add(key + "_desc", desc)
        L.add(U + "_CB_NAME", cbn)
        L.add(U + "_WAR_NAME", "[ConcatIfNeitherEmpty('$ORDER|q$', ' ')]" + warn)
        L.add(U + "_WAR_NAME_BASE", "[ATTACKER.GetPrimaryTitle.GetAdjective][DEFENDER.GetPrimaryTitle.GetName]")
        L.add(key + "_victory_desc_attacker", vatt)
        L.add(key + "_victory_desc", vgen)
        L.add(key + "_white_peace_desc", wp)
        L.add(key + "_defeat_desc", de)
        L.add(key + "_invalidated_desc", inv)
    write("common/casus_belli_types/eir_casus_belli_raids.txt", text)
    L.write()
    print("casus belli (raids) written (3)")


if __name__ == "__main__":
    build()
