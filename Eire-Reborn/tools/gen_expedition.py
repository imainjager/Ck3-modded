"""Update 9: Sponsor an Expedition. Writes:
  common/decisions/eir_expedition_decisions.txt      the decision (a vanilla option-list widget: 3 sizes x courtier / adventurer)
  common/casus_belli_types/eir_expedition_cb.txt     the war the expedition fights (a migration-style conquest of a duchy; script only)
  common/scripted_effects/eir_effects_expedition.txt launch and victory effects
  events/eir_ev_expedition.txt                       four short events (launch, victory, defeat, no landing found)
  localization/english/eir_expedition_l_english.yml
The base game's own conquest war does NOT change culture or faith, so the victory effect does it here: each conquered county has a 65% chance to take the
sponsor's culture and faith; the rest keep theirs and get a massive unrest modifier; every conquered county loses 5 development.
Only Gaelic and Brythonic rulers see the decision. The AI never uses it."""
from eir_lib import *

SIZES = [("small", 1000, 1000, "A small company"), ("medium", 5000, 3000, "A great host"), ("large", 10000, 5000, "A migration")]
LEADERS = [("courtier", "one of your courtiers", "Send one of your own courtiers to lead it."), ("adventurer", "a hardy adventurer", "Hire an unknown adventurer of your own faith and culture to lead it.")]


def build():
    L = Loc("eir_expedition_l_english.yml")
    L.section("the decision")
    L.add("eir_sponsor_expedition_decision", "Sponsor an Expedition")
    L.add("eir_sponsor_expedition_decision_desc",
          "The old stories say that the Gaels once sailed to Ireland from the far side of the world, and that the Britons were driven west across the sea from lands that were theirs. The ships are still in the harbour. Pay for a host and a leader, give them the sea and a blessing, and let them settle somewhere that will speak your tongue and pray in your way.")
    L.add("eir_sponsor_expedition_decision_tooltip",
          "Pay 1,000, 3,000 or 5,000 gold (a host of 1,000, 5,000 or 10,000 men). A courtier of yours, or an adventurer, lands in a random duchy in Europe and fights for it. If the expedition wins, the duchy takes your culture and faith in about two counties out of three, loses 5 development, and the counties that keep their old culture rise in massive unrest.")
    L.add("eir_sponsor_expedition_decision_confirm", "Send the ships")
    L.add("EIR_EXPEDITION_NEXT_STEP", "Choose the expedition")
    L.add("eir_expedition_celt_tt", "You are a ruler of a Gaelic or Brythonic culture")
    L.add("eir_exp_host_name", "The Expedition")
    items = ""
    for sk, men, gold, sname in SIZES:
        for lk, lname, ldesc in LEADERS:
            key = "eir_exp_%s_%s" % (sk, lk)
            L.add(key, "%s led by %s (%d gold)" % (sname, lname, gold))
            L.add(key + "_desc", "%s %d men, for %d gold. %s" % (sname, men, gold, ldesc))
            L.add(key + "_valid_tt", "You have at least %d gold%s" % (gold, " and an adult courtier who is not a ruler" if lk == "courtier" else ""))
            courtier = ("\n\t\t\t\t\tany_courtier = {\n\t\t\t\t\t\tis_adult = yes\n\t\t\t\t\t\tis_physically_able_adult = yes\n\t\t\t\t\t\tis_landed = no\n\t\t\t\t\t}") if lk == "courtier" else ""
            items += f"""		item = {{
			value = {key}
			is_valid = {{
				custom_tooltip = {{
					text = {key}_valid_tt
					gold >= {gold}{courtier}
				}}
			}}
			current_description = {key}_desc
			localization = {key}
			icon = "gfx/interface/icons/character_interactions/religious.dds"
			ai_chance = {{
				value = 0
			}}
		}}
"""
    effects = ""
    first = True
    for sk, men, gold, sname in SIZES:
        for lk, lname, ldesc in LEADERS:
            key = "eir_exp_%s_%s" % (sk, lk)
            effects += "\t\t%sif = {\n\t\t\tlimit = { scope:%s = yes }\n\t\t\teir_expedition_launch_effect = { SIZE = %d GOLD = %d COURTIER = %s }\n\t\t}\n" % ("" if first else "else_", key, men, gold, "yes" if lk == "courtier" else "no")
            first = False
    decision = f"""eir_sponsor_expedition_decision = {{
	picture = {{
		reference = "gfx/interface/illustrations/decisions/decision_found_kingdom.dds"
	}}
	decision_group_type = major
	desc = eir_sponsor_expedition_decision_desc
	selection_tooltip = eir_sponsor_expedition_decision_tooltip
	confirm_text = eir_sponsor_expedition_decision_confirm
	sort_order = 45

	cooldown = {{ years = 10 }}

	is_shown = {{
		eir_act_gael_host_trigger = yes
		is_independent_ruler = yes
	}}

	is_valid_showing_failures_only = {{
		is_available_adult = yes
		is_imprisoned = no
	}}

	is_valid = {{
		custom_tooltip = {{
			text = eir_expedition_celt_tt
			eir_raid_celt_trigger = yes
		}}
		gold >= 1000
		is_at_war = no
	}}

	widget = {{
		gui = "decision_view_widget_option_list_generic"
		controller = decision_option_list_controller
		decision_to_second_step_button = "EIR_EXPEDITION_NEXT_STEP"
		show_from_start = yes

{items}	}}

	effect = {{
{effects}	}}

	ai_check_interval = 0
	ai_will_do = {{
		base = 0
	}}
}}
"""
    write("common/decisions/eir_expedition_decisions.txt", "# Eire Reborn - Sponsor an Expedition. Generated by tools/gen_expedition.py\n\n" + decision)

    # ------------------------------------------------------------------------------------------------ scripted effects
    fx = """##########################################################################
# Eire Reborn - Update 9 expedition effects, generated by tools/gen_expedition.py
##########################################################################

# Character scope (the sponsor). Params: SIZE (men), GOLD (price), COURTIER (yes: one of the sponsor's courtiers leads; no: a new adventurer).
eir_expedition_launch_effect = {
	save_scope_as = eir_exp_sponsor
	# 1. a landing place: a coastal county of a European duchy that is held by somebody outside the Gaelic and Brythonic world
	random_county_in_region = {
		region = world_europe
		limit = {
			holder ?= {
				is_ai = yes
				NOT = { this = scope:eir_exp_sponsor }
				NOT = { top_liege = scope:eir_exp_sponsor.top_liege }
				NOT = { has_truce = scope:eir_exp_sponsor }
				culture ?= {
					NOR = {
						has_cultural_pillar = heritage_goidelic
						has_cultural_pillar = heritage_brythonic
					}
				}
			}
			NOT = { title_province = { geographical_region = world_europe_west_britannia } }
			title_province = { is_coastal = yes }
			exists = de_jure_liege
			de_jure_liege = { tier = tier_duchy }
		}
		save_scope_as = eir_exp_county
	}
	if = {
		limit = { exists = scope:eir_exp_county }
		scope:eir_exp_county.de_jure_liege = { save_scope_as = eir_exp_duchy }
		scope:eir_exp_county.holder.top_liege = { save_scope_as = eir_exp_target }
		add_gold = -$GOLD$
		# 2. a leader
		random_courtier = {
			limit = {
				always = $COURTIER$
				is_adult = yes
				is_physically_able_adult = yes
				is_landed = no
			}
			save_scope_as = eir_exp_leader
		}
		if = {
			limit = { NOT = { exists = scope:eir_exp_leader } }
			create_character = {
				location = scope:eir_exp_sponsor.capital_province
				age = { 26 42 }
				gender_female_chance = 10
				culture = scope:eir_exp_sponsor.culture
				faith = scope:eir_exp_sponsor.faith
				random_traits = yes
				save_scope_as = eir_exp_leader
			}
		}
		# 3. the landing: the leader seizes the beachhead county and stands independent
		create_title_and_vassal_change = {
			type = independency
			save_scope_as = eir_exp_change
			add_claim_on_loss = no
		}
		scope:eir_exp_county = {
			change_title_holder = {
				holder = scope:eir_exp_leader
				change = scope:eir_exp_change
			}
		}
		scope:eir_exp_leader = {
			becomes_independent = { change = scope:eir_exp_change }
		}
		resolve_title_and_vassal_change = scope:eir_exp_change
		scope:eir_exp_leader = {
			set_variable = {
				name = eir_exp_sponsor
				value = scope:eir_exp_sponsor
			}
			set_variable = {
				name = eir_exp_duchy
				value = scope:eir_exp_duchy
			}
			set_variable = {
				name = eir_exp_culture
				value = scope:eir_exp_sponsor.culture
			}
			set_variable = {
				name = eir_exp_faith
				value = scope:eir_exp_sponsor.faith
			}
			add_character_modifier = {
				modifier = eir_expedition_leader_modifier
				years = 10
			}
			add_pressed_claim = scope:eir_exp_duchy
			spawn_army = {
				levies = $SIZE$
				location = scope:eir_exp_county.title_province
				origin = capital_province
				inheritable = no
				uses_supply = no
				name = eir_exp_host_name
			}
			add_character_flag = temp_no_claim_war_cost
			start_war = {
				cb = eir_expedition_cb
				target = scope:eir_exp_target
				target_title = scope:eir_exp_duchy
			}
			remove_character_flag = temp_no_claim_war_cost
		}
		add_hook = {
			target = scope:eir_exp_leader
			type = favor_hook
		}
		add_prestige = medium_prestige_gain
		trigger_event = eir.1300
	}
	else = {
		trigger_event = eir.1303
	}
}

# Character scope (the leader): after the war is won, the duchy takes the sponsor's culture and faith in most of its counties
# (65% each), loses 5 development everywhere, and the counties that keep their old culture rise in unrest.
eir_expedition_victory_effect = {
	save_scope_as = eir_exp_leader
	var:eir_exp_duchy ?= { save_scope_as = eir_exp_duchy }
	every_sub_realm_county = {
		limit = {
			exists = scope:eir_exp_duchy
			de_jure_liege = scope:eir_exp_duchy
		}
		change_development_level = -5
		random_list = {
			65 = {
				set_county_culture = scope:eir_exp_leader.var:eir_exp_culture
				set_county_faith = scope:eir_exp_leader.var:eir_exp_faith
				add_county_modifier = {
					modifier = eir_expedition_settled_modifier
					years = 20
				}
			}
			35 = {
				add_county_modifier = {
					modifier = eir_expedition_unrest_modifier
					years = 30
				}
			}
		}
	}
	var:eir_exp_sponsor ?= { trigger_event = eir.1301 }
}
"""
    write("common/scripted_effects/eir_effects_expedition.txt", fx)

    # ------------------------------------------------------------------------------------------------ the casus belli
    cb = """eir_expedition_cb = {
	group = event
	icon = duchy_conquest_cb

	combine_into_one = yes
	should_show_war_goal_subview = yes
	mutually_exclusive_titles = { always = yes }
	allow_hostages = no
	white_peace_possible = no
	interface_priority = 80

	attacker_score_from_occupation_scale = 150
	attacker_score_from_battles_scale = 200
	defender_score_from_battles_scale = 200

	allowed_for_character = {
		always = yes
	}

	allowed_against_character = {
		always = yes
	}

	target_titles = all
	target_title_tier = duchy
	target_de_jure_regions_above = yes
	ignore_effect = change_title_holder
	valid_to_start = {
		always = yes
	}

	should_invalidate = {
		NOT = {
			any_in_list = {
				list = target_titles
				any_in_de_jure_hierarchy = {
					tier = tier_county
					holder = {
						target_is_same_character_or_above = scope:defender
					}
				}
			}
		}
	}

	on_invalidated_desc = eir_expedition_cb_invalidated_desc
	on_invalidated = {}

	cost = {}

	on_declaration = {
		on_declared_war = yes
	}

	on_victory_desc = {
		first_valid = {
			desc = eir_expedition_cb_victory_desc
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
			custom_tooltip = CONQUEST_CB_TITLE
			conquest_cb_title_transfer = {
				RELIGIOUS_WAR = no
			}
		}
		every_in_list = {
			list = vassals_taken
			change_liege = {
				liege = scope:attacker
				change = scope:change
			}
		}
		every_in_list = {
			list = titles_taken
			change_title_holder = {
				holder = scope:attacker
				change = scope:change
				take_baronies = yes
			}
		}
		resolve_title_and_vassal_change = scope:change
		scope:attacker = {
			eir_expedition_victory_effect = yes
			add_prestige = major_prestige_gain
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
			desc = eir_expedition_cb_defeat_desc
		}
	}

	on_white_peace = {
		add_truce_white_peace_effect = yes
	}

	on_defeat_desc = {
		first_valid = {
			desc = eir_expedition_cb_defeat_desc
		}
	}

	on_defeat = {
		scope:defender = {
			add_prestige_war_defender_effect = {
				PRESTIGE_VALUE = medium_prestige_value
			}
		}
		scope:attacker = {
			var:eir_exp_sponsor ?= { trigger_event = eir.1302 }
		}
		add_truce_attacker_defeat_effect = yes
		scope:attacker = {
			save_temporary_scope_as = loser
		}
	}

	transfer_behavior = transfer
	on_primary_attacker_death = inherit
	on_primary_defender_death = inherit
	attacker_allies_inherit = yes
	defender_allies_inherit = yes

	war_name = "EIR_EXPEDITION_WAR_NAME"
	war_name_base = "EIR_EXPEDITION_WAR_NAME_BASE"
	cb_name = "EIR_EXPEDITION_CB_NAME"

	use_de_jure_wargoal_only = yes
	attacker_wargoal_percentage = 0.8
	max_defender_score_from_occupation = 150
	max_attacker_score_from_occupation = 150
}
"""
    write("common/casus_belli_types/eir_expedition_cb.txt", "# Eire Reborn - the expedition war. Generated by tools/gen_expedition.py\n\n" + cb)
    L.section("the war")
    L.add("eir_expedition_cb", "Expedition")
    L.add("eir_expedition_cb_desc", "A people crossing the sea to take a new land.")
    L.add("EIR_EXPEDITION_CB_NAME", "Expedition against [DEFENDER.GetShortUIName]")
    L.add("EIR_EXPEDITION_WAR_NAME", "[ConcatIfNeitherEmpty('$ORDER|q$', ' ')][ATTACKER.GetPrimaryTitle.GetAdjective] Expedition to [TITLE.GetBaseName]")
    L.add("EIR_EXPEDITION_WAR_NAME_BASE", "[ATTACKER.GetPrimaryTitle.GetAdjective][DEFENDER.GetPrimaryTitle.GetName]")
    L.add("eir_expedition_cb_victory_desc", "The expedition takes the duchy. Most of its counties take the sponsor's culture and faith and lose 5 development; the rest keep their ways and rise in unrest.")
    L.add("eir_expedition_cb_defeat_desc", "The expedition is destroyed or turned back, and the sponsor's gold is lost.")
    L.add("eir_expedition_cb_invalidated_desc", "The [war.GetName] has ended: the defender no longer holds the land.")

    # ------------------------------------------------------------------------------------------------ events
    ev = """namespace = eir

# Eire Reborn - expedition events. Generated by tools/gen_expedition.py

eir.1300 = {
	type = character_event
	title = eir.1300.t
	desc = eir.1300.desc
	theme = diplomacy
	left_portrait = {
		character = root
		animation = personality_bold
	}
	right_portrait = {
		character = scope:eir_exp_leader
		animation = admiration
	}
	option = {
		name = eir.1300.a
		add_piety = minor_piety_gain
		add_stress = minor_stress_loss
	}
	option = {
		name = eir.1300.b
		add_prestige = minor_prestige_gain
	}
}

eir.1301 = {
	type = character_event
	title = eir.1301.t
	desc = eir.1301.desc
	theme = diplomacy
	left_portrait = {
		character = root
		animation = happiness
	}
	right_portrait = {
		character = scope:eir_exp_leader
		animation = personality_bold
	}
	option = {
		name = eir.1301.a
		add_prestige = major_prestige_gain
		add_piety = medium_piety_gain
	}
	option = {
		name = eir.1301.b
		add_gold = major_gold_value
		scope:eir_exp_leader ?= { add_opinion = { target = root modifier = eir_raid_grudge_opinion opinion = -15 } }
	}
	option = {
		name = eir.1301.c
		scope:eir_exp_leader ?= { add_opinion = { target = root modifier = eir_blood_price_paid_opinion opinion = 40 } }
		add_prestige = medium_prestige_gain
	}
}

eir.1302 = {
	type = character_event
	title = eir.1302.t
	desc = eir.1302.desc
	theme = war
	left_portrait = {
		character = root
		animation = sadness
	}
	option = {
		name = eir.1302.a
		add_prestige = minor_prestige_loss
		add_stress = minor_stress_gain
	}
	option = {
		name = eir.1302.b
		add_piety = medium_piety_gain
	}
}

eir.1303 = {
	type = character_event
	title = eir.1303.t
	desc = eir.1303.desc
	theme = diplomacy
	left_portrait = {
		character = root
		animation = worry
	}
	option = {
		name = eir.1303.a
		add_stress = minor_stress_gain
	}
}
"""
    write("events/eir_ev_expedition.txt", ev)
    for num, t, d, opts in [
        (1300, "The Ships Leave", "The tide turns at dawn and the ships go out, one after another, past the harbour mouth. The priests bless the sails; the poets compose a farewell; the leader stands at the stern and does not look back.\n\nIn the hall, nobody speaks for a time. Then somebody says what everyone is thinking: that it may be years before a ship comes home.", ["Say a prayer for them.", "Watch until the last sail is gone."]),
        (1301, "The Expedition Has Won", "The ships have come home with news. The leader holds a duchy overseas. The gods are spoken of in the old way there now, the tongue of the island is heard in the market, and the people of the land who were not changed are quiet and watchful.\n\nThe leader has sent a delegation to ask what is owed to the sponsor.", ["Ask for nothing but their prayers.", "Ask for a share of the first year's taxes.", "Ask only for an alliance of the two peoples."]),
        (1302, "The Expedition Is Lost", "A single ship has come back, with a boy at the helm and a story that nobody wants to hear. The landing was met, the host was beaten and the leader did not come off the beach. The sails are in the sea.", ["Mourn them as heroes.", "Pay for masses for the fallen."]),
        (1303, "No Landing Found", "The ships have been to the coast and come back: every shore they could reach was held by friends, by kinsmen or by strong lords. The gold has been returned. The captains are embarrassed and the poets are pretending not to be disappointed.", ["Put the gold away for next time."]),
    ]:
        L.add("eir.%d.t" % num, t)
        L.add("eir.%d.desc" % num, "#bold %s#!\n\n%s" % (t, d))
        for letter, o in zip("abc", opts):
            L.add("eir.%d.%s" % (num, letter), o)
    L.write()
    print("expedition written")


if __name__ == "__main__":
    build()
