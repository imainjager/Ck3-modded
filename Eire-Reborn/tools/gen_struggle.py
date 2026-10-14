"""Update 8, stage 5: The Fragmentation of Ireland (a struggle). Writes (all with BOM):
  common/struggle/struggles/eir_struggle.txt          the struggle, three phases and two endings
  common/decisions/eir_struggle_decisions.txt         two ending decisions (High Kingship, Concord of the Saints)
  common/scripted_effects/eir_effects_struggle.txt    ending effect
  common/on_action/eir_on_actions_struggle.txt        the yearly check that starts it for a player who does not yet rule half of Ireland
  events/eir_ev_struggle.txt                          the yearly catalyst event (hidden, scope = struggle), the ending notices
  localization/english/eir_struggle_l_english.yml
Built on the structure of the vanilla Iranian Intermezzo. It needs the Fate of Iberia feature (the struggle system), and all of its content is guarded by that."""
from eir_lib import *

DLC = "has_dlc_feature = the_fate_of_iberia"

STRUGGLE = """eir_irish_struggle = {
	illustration = "gfx/interface/illustrations/event_story/fp2_struggle_start.dds"

	cultures = {
		irish
		gaelic
	}
	faiths = {
		christian_faith
		catholic
		eir_druidic
	}
	regions = {
		custom_ireland
	}

	involvement_prerequisite_percentage = 0.5

	on_start = {
		trigger_event = eir.0994
	}

	transition_state_duration = { months = 6 }

	start_phase = eir_struggle_phase_kin_strife

	phase_list = {

		eir_struggle_phase_kin_strife = {
			duration = { points = 400 }

			future_phases = {
				eir_struggle_phase_over_kings = {
					catalysts = {
						catalyst_win_any_war_within_the_region = medium_struggle_catalyst_gain
						catalyst_winning_large_conquest_war = major_struggle_catalyst_gain
						catalyst_vassalize_independent_ruler = major_struggle_catalyst_gain
						catalyst_enforcing_de_jure_claims = minor_struggle_catalyst_gain
						catalyst_raided_involved = minor_struggle_catalyst_gain
						catalyst_yearly_influential_house_is_harmonious_minor = minor_struggle_catalyst_gain
						catalyst_yearly_influential_house_is_harmonious_medium = medium_struggle_catalyst_gain
						catalyst_coronation_event_stabilization = minimal_struggle_catalyst_gain
					}
				}
			}

			war_effects = {
				name = WAR_EFFECTS_NAME

				involved_character_modifier = {
					levy_size = 0.15
					vassal_opinion = -5
					army_maintenance_mult = -0.1
				}

				interloper_character_modifier = {
					army_maintenance_mult = -0.05
				}
			}

			culture_effects = {
				name = CULTURE_EFFECTS_NAME

				involved_character_modifier = {
					same_culture_opinion = 5
					dynasty_house_opinion = -10
				}
			}

			other_effects = {
				name = OTHER_EFFECTS_NAME

				involved_county_modifier = {
					monthly_county_control_decline_at_war_add = 0.02
				}

				involved_character_modifier = {
					owned_hostile_scheme_success_chance_add = 10
				}
			}
		}

		eir_struggle_phase_over_kings = {
			duration = { points = 400 }

			future_phases = {
				eir_struggle_phase_kin_strife = {
					catalysts = {
						catalyst_yearly_influential_house_is_antagonistic_minor = minor_struggle_catalyst_gain
						catalyst_yearly_influential_house_is_antagonistic_medium = medium_struggle_catalyst_gain
						catalyst_yearly_influential_house_is_antagonistic_major = major_struggle_catalyst_gain
						catalyst_cadet_branch_created = major_struggle_catalyst_gain
						catalyst_becomes_rival_with_involved = minor_struggle_catalyst_gain
						catalyst_unnatural_death_important_character = medium_struggle_catalyst_gain
						catalyst_execute_important = medium_struggle_catalyst_gain
						catalyst_independence_from_non_dejure_vassal = major_struggle_catalyst_gain
					}
				}
				eir_struggle_phase_truce_of_saints = {
					catalysts = {
						catalyst_passing_of_time = minor_struggle_catalyst_gain
						catalyst_bought_important_truce = medium_struggle_catalyst_gain
						catalyst_truce_was_enforced = minor_struggle_catalyst_gain
						catalyst_sign_truce_outside_war = minor_struggle_catalyst_gain
						catalyst_forming_alliance_between_independent_involved_rulers = medium_struggle_catalyst_gain
						catalyst_new_building_in_temple = minor_struggle_catalyst_gain
						catalyst_yearly_influential_house_is_harmonious_major = major_struggle_catalyst_gain
					}
				}
			}

			war_effects = {
				name = WAR_EFFECTS_NAME

				involved_character_modifier = {
					knight_effectiveness_mult = 0.05
					led_by_owner_extra_advantage_add = 3
				}
			}

			culture_effects = {
				name = CULTURE_EFFECTS_NAME

				involved_character_modifier = {
					same_culture_opinion = 10
					opinion_of_same_culture = 5
				}
			}

			other_effects = {
				name = OTHER_EFFECTS_NAME

				all_county_modifier = {
					build_speed = -0.1
				}

				involved_character_modifier = {
					vassal_opinion = 5
					monthly_prestige = 0.1
				}
			}

			ending_decisions = {
				eir_struggle_end_high_kingship_decision
				eir_struggle_end_concord_decision
			}
		}

		eir_struggle_phase_truce_of_saints = {
			duration = { points = 400 }

			future_phases = {
				eir_struggle_phase_kin_strife = {
					catalysts = {
						catalyst_yearly_influential_house_is_antagonistic_medium = medium_struggle_catalyst_gain
						catalyst_yearly_influential_house_is_antagonistic_major = major_struggle_catalyst_gain
						catalyst_raided_involved = medium_struggle_catalyst_gain
						catalyst_unnatural_death_important_character = major_struggle_catalyst_gain
						catalyst_broke_truce_against_important_character = major_struggle_catalyst_gain
					}
				}
			}

			faith_effects = {
				name = FAITH_EFFECTS_NAME

				involved_character_modifier = {
					clergy_opinion = 10
					monthly_piety = 0.1
				}
			}

			culture_effects = {
				name = CULTURE_EFFECTS_NAME

				involved_character_modifier = {
					same_culture_opinion = 10
				}
			}

			other_effects = {
				name = OTHER_EFFECTS_NAME

				all_county_modifier = {
					monthly_county_control_growth_add = 0.1
				}

				involved_character_modifier = {
					stress_gain_mult = -0.1
				}
			}

			ending_decisions = {
				eir_struggle_end_high_kingship_decision
				eir_struggle_end_concord_decision
			}
		}
	}
}
"""

DECISIONS = """eir_struggle_end_high_kingship_decision = {
	decision_group_type = major
	title = eir_struggle_end_high_kingship
	picture = {
		reference = "gfx/interface/illustrations/decisions/decision_found_kingdom.dds"
	}
	extra_picture = "gfx/interface/illustrations/struggle_decision_buttons/fp2_decision_hostility.dds"
	desc = eir_struggle_end_high_kingship_decision_desc
	selection_tooltip = eir_struggle_end_high_kingship_tooltip
	confirm_click_sound = "event:/DLC/FP2/SFX/UI/fp2_struggle_ending_decision_confirm"
	is_invisible = yes
	sort_order = 80

	is_valid_showing_failures_only = {
		is_available_adult = yes
		top_liege = this
	}

	is_valid = {
		custom_tooltip = {
			text = eir_struggle_ending_involved_tt
			any_character_struggle = {
				involvement = involved
				is_struggle_type = eir_irish_struggle
			}
		}
		highest_held_title_tier >= tier_kingdom
		custom_tooltip = {
			text = eir_struggle_end_high_kingship_region_tt
			any_county_in_region = {
				region = custom_ireland
				percent >= 0.7
				holder.top_liege = root
			}
		}
		prestige_level >= 3
	}

	effect = {
		eir_struggle_ending_effect = { ENDING = eir_struggle_end_high_kingship_decision EVENT = eir.0995 }
	}

	ai_check_interval = 0
	ai_will_do = {
		base = 0
	}
}

eir_struggle_end_concord_decision = {
	decision_group_type = major
	title = eir_struggle_end_concord
	picture = {
		reference = "gfx/interface/illustrations/decisions/decision_personal_religious.dds"
	}
	extra_picture = "gfx/interface/illustrations/struggle_decision_buttons/fp2_decision_conciliation.dds"
	desc = eir_struggle_end_concord_decision_desc
	selection_tooltip = eir_struggle_end_concord_tooltip
	confirm_click_sound = "event:/DLC/FP2/SFX/UI/fp2_struggle_ending_decision_confirm"
	is_invisible = yes
	sort_order = 70

	is_valid_showing_failures_only = {
		is_available_adult = yes
		top_liege = this
	}

	is_valid = {
		custom_tooltip = {
			text = eir_struggle_ending_involved_tt
			any_character_struggle = {
				involvement = involved
				is_struggle_type = eir_irish_struggle
			}
		}
		highest_held_title_tier >= tier_duchy
		custom_tooltip = {
			text = eir_struggle_end_concord_region_tt
			any_county_in_region = {
				region = custom_ireland
				percent >= 0.3
				holder.top_liege = root
			}
		}
		piety >= 500
		is_at_war = no
	}

	effect = {
		eir_struggle_ending_effect = { ENDING = eir_struggle_end_concord_decision EVENT = eir.0996 }
	}

	ai_check_interval = 0
	ai_will_do = {
		base = 0
	}
}
"""

EFFECTS = """##########################################################################
# Eire Reborn - Update 8 struggle effects, generated by tools/gen_struggle.py
##########################################################################

# Character scope: the ruler ends the Fragmentation of Ireland.
eir_struggle_ending_effect = {
	set_global_variable = eir_struggle_done
	add_prestige = massive_prestige_gain
	add_piety = major_piety_gain
	add_character_modifier = {
		modifier = eir_end_of_strife_modifier
		years = 30
	}
	struggle:eir_irish_struggle ?= { end_struggle = $ENDING$ }
}
"""

ONACTION = """##########################################################################
# Eire Reborn - Update 8 struggle on_action, generated by tools/gen_struggle.py
# Hooked into random_yearly_playable_pulse in eir_on_actions.txt
##########################################################################

# A player of a Gaelic culture who does not yet rule half of Ireland sees the Fragmentation of Ireland begin.
eir_struggle_pulse = {
	trigger = {
		%(dlc)s
		is_ruler = yes
		is_ai = no
		eir_is_gael_ruler_trigger = yes
		NOT = { exists = struggle:eir_irish_struggle }
		NOT = { has_global_variable = eir_struggle_done }
		NOT = { has_global_variable = eir_struggle_started }
		current_year >= 868
		NOT = {
			any_county_in_region = {
				region = custom_ireland
				percent >= 0.5
				holder.top_liege = root
			}
		}
	}
	effect = {
		set_global_variable = eir_struggle_started
		start_struggle = {
			struggle_type = eir_irish_struggle
			start_phase = eir_struggle_phase_kin_strife
		}
	}
}
""" % dict(dlc=DLC)

EVENTS = """namespace = eir

# Eire Reborn - the Fragmentation of Ireland. Generated by tools/gen_struggle.py

# 0994: yearly catalyst check (hidden, scope = struggle): the passage of time and the temper of the great houses.
eir.0994 = {
	hidden = yes
	scope = struggle

	immediate = {
		if = {
			limit = { phase_has_catalyst = catalyst_passing_of_time }
			activate_struggle_catalyst = catalyst_passing_of_time
		}
		trigger_event = {
			id = eir.0994
			years = 1
		}
	}
}

# 0995: ending - the High Kingship
eir.0995 = {
	type = character_event
	title = eir.0995.t
	desc = eir.0995.desc
	theme = diplomacy
	left_portrait = {
		character = root
		animation = personality_bold
	}

	trigger = {
		always = yes
	}

	option = {
		name = eir.0995.a
		add_prestige = medium_prestige_gain
	}
}

# 0996: ending - the Concord of the Saints
eir.0996 = {
	type = character_event
	title = eir.0996.t
	desc = eir.0996.desc
	theme = diplomacy
	left_portrait = {
		character = root
		animation = happiness
	}

	trigger = {
		always = yes
	}

	option = {
		name = eir.0996.a
		add_piety = medium_piety_gain
	}
}
"""


def build():
    L = Loc("eir_struggle_l_english.yml")
    L.section("struggle")
    L.add("eir_irish_struggle", "The Fragmentation of Ireland")
    L.add("eir_irish_struggle_desc", "Ireland has a hundred kings and a title for one. The High Kingship of Tara is a seat for the strongest of the great houses, and between each strong king and the next there is a generation of cattle raids, burned halls and quarrels over precedence. The island could be one, or it could remain a hundred; and the Church, the poets and the Norse each have their own opinion.")
    L.add("game_concept_eir_irish_struggle", "$eir_irish_struggle$")
    L.add("game_concept_eir_irish_struggle_desc", "$eir_irish_struggle_desc$")
    phases = [
        ("eir_struggle_phase_kin_strife", "Kin-Strife", "The kings fight over cattle, tribute and precedence, and every victory only makes the loser angrier. Armies are cheap, vassals are sour and no peace lasts through a harvest."),
        ("eir_struggle_phase_over_kings", "Rise of the Overkings", "One house after another reaches for the High Kingship, and the weaker kings must decide which of them to follow. Armies are better led, vassals more loyal and the cattle-raids rarer, until the next king dies."),
        ("eir_struggle_phase_truce_of_saints", "Truce of the Saints", "The abbots and the poets have brokered a truce that the kings have sworn on the relics. For a few seasons the roads are safe, the fairs full and the churches rich."),
    ]
    for key, name, desc in phases:
        L.add(key, name)
        L.add(key + "_desc", desc)
        L.add("game_concept_" + key, name)
        L.add("game_concept_%s_desc" % key, desc)
    L.add("eir_struggle_ending_involved_tt", "You are #V involved#! in the Fragmentation of Ireland")
    L.add("eir_struggle_end_high_kingship", "The High Kingship")
    L.add("eir_struggle_end_high_kingship_decision_desc", "One house has the strength to hold the kingship of Tara. Sit in the old hall, count the kings who bring their cattle to the Hill, and end the Fragmentation of Ireland by force of name and army.")
    L.add("eir_struggle_end_high_kingship_tooltip", "Make yourself High King and end the strife by holding the island.")
    L.add("eir_struggle_end_high_kingship_decision_confirm", "Take the High Kingship")
    L.add("eir_struggle_end_high_kingship_region_tt", "You hold at least #V 70%#! of the counties of Ireland")
    L.add("eir_struggle_end_concord", "The Concord of the Saints")
    L.add("eir_struggle_end_concord_decision_desc", "The kings are tired and the abbots are patient. Gather them at a holy place, put the relics on the table and have each of them swear that he will hold no more land than his fathers held. A king at peace is not a High King, but he keeps his head.")
    L.add("eir_struggle_end_concord_tooltip", "Swear a lasting peace on the relics and end the strife without conquering the island.")
    L.add("eir_struggle_end_concord_decision_confirm", "Swear the Concord")
    L.add("eir_struggle_end_concord_region_tt", "You hold at least #V 30%#! of the counties of Ireland")
    L.add("eir.0995.t", "The Hill of Tara Is Full")
    L.add("eir.0995.desc", "#bold The strife has ended.#!\n\nThe kings came to the Hill with their cattle and their poets and sat in the order of their fathers. Nobody drew a knife. In the evening the chief poet recited the line of the High Kings, and at the end of it there was your name.")
    L.add("eir.0995.a", "Let the harpers play.")
    L.add("eir.0996.t", "The Relics on the Table")
    L.add("eir.0996.desc", "#bold The strife has ended.#!\n\nThey swore on the bell of Patrick and on the bones of Brigid and on the cross of Columba, and the abbot of each of the three churches put his hand over the hand of the nearest king. Nobody is High King. Everybody is at peace.")
    L.add("eir.0996.a", "Let the bells be rung.")
    L.write()
    write("common/struggle/struggles/eir_struggle.txt", "# Eire Reborn - struggle. Generated by tools/gen_struggle.py\n\n" + STRUGGLE)
    write("common/decisions/eir_struggle_decisions.txt", "# Eire Reborn - struggle ending decisions. Generated by tools/gen_struggle.py\n\n" + DECISIONS)
    write("common/scripted_effects/eir_effects_struggle.txt", EFFECTS)
    write("common/on_action/eir_on_actions_struggle.txt", ONACTION)
    write("events/eir_ev_struggle.txt", EVENTS)
    print("struggle written (3 phases, 2 endings)")


if __name__ == "__main__":
    build()
