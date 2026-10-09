"""Generates: modifiers, traits, opinion modifiers, culture traditions, men-at-arms, buildings, titles.
All field names are validated against what the vanilla game files already use.
"""
from eir_lib import *

# =============================================================================
# MODIFIERS
# =============================================================================
# name: (icon, fields, display name, description)
CHAR = {
    "eir_ard_ri_modifier": ("prestige_positive",
        {"monthly_prestige": 0.5, "vassal_opinion": 5, "legitimacy_gain_mult": 0.15},
        "High King of Ireland", "You were crowned at Tara, and the whole island knows it."),
    "eir_lia_fail_blessing_modifier": ("legend_positive",
        {"monthly_prestige_gain_mult": 0.1, "monthly_piety": 0.2},
        "The Stone Cried Out", "The Lia Fáil roared beneath you, as it is said to for a rightful king."),
    "eir_oenach_afterglow_modifier": ("social_positive",
        {"general_opinion": 5, "monthly_prestige": 0.2},
        "Afterglow of the Óenach", "The great assembly was a success, and people still speak warmly of it."),
    "eir_boramha_collected_modifier": ("economy_mixed",
        {"monthly_income": 2, "vassal_opinion": -8},
        "The Cow Tribute", "You collect the old Bóramha tribute. The gold is welcome, and the vassals are not."),
    "eir_brehon_laws_modifier": ("legitimacy_positive",
        {"legitimacy_gain_mult": 0.1, "courtier_and_guest_opinion": 5},
        "Judge of the Brehon Laws", "Your courts follow the ancient laws, and your subjects trust them."),
    "eir_fili_patron_modifier": ("learning_positive",
        {"monthly_prestige_gain_mult": 0.1, "owned_legend_spread_mult": 0.15},
        "Patron of the Filí", "The poets of Ireland sing your praises from Tara to Kerry."),
    "eir_satirised_modifier": ("prestige_negative",
        {"monthly_prestige": -0.3, "general_opinion": -5},
        "Satirised in Verse", "A poet's satire has made you a laughing stock. Satire can wither a king."),
    "eir_foster_ties_modifier": ("family_positive",
        {"vassal_opinion": 5, "direct_vassal_opinion": 5},
        "Bound by Fosterage", "Your vassals' sons were raised in your hall, and they remember it."),
    "eir_cattle_rich_modifier": ("economy_positive",
        {"domain_tax_mult": 0.05, "monthly_income": 1},
        "Cattle-Rich", "Your herds are great, and so is your wealth."),
    "eir_raider_infamy_modifier": ("dread_mixed",
        {"independent_ruler_opinion": -10, "monthly_prestige": 0.1},
        "Infamous Cattle-Raider", "Your raids are famous. Your neighbours do not find it as amusing as you do."),
    "eir_norse_scourge_modifier": ("martial_positive",
        {"monthly_prestige": 0.4, "knight_effectiveness_mult": 0.1},
        "Scourge of the Norse", "You drove the Norsemen back into the sea, and the songs have already started."),
    "eir_danegeld_modifier": ("economy_negative",
        {"monthly_income_mult": -0.1, "vassal_opinion": -5},
        "Paying Danegeld", "You pay the Norse to stay away. They do not stay away for long."),
    "eir_gallowglass_paymaster_modifier": ("martial_positive",
        {"men_at_arms_maintenance": -0.1},
        "Gallowglass Paymaster", "You have learned how to keep the island's most feared axemen in your pay."),
    "eir_fianna_spirit_modifier": ("prowess_positive",
        {"prowess": 2, "knight_effectiveness_mult": 0.1},
        "Spirit of the Fianna", "The old warrior-hunters of the tales ride again in your hall."),
    "eir_celtic_brotherhood_modifier": ("diplomacy_positive",
        {"different_culture_opinion": 5, "monthly_prestige": 0.2},
        "Celtic Brotherhood", "The Celtic peoples of the isles see you as a friend and a leader."),
    "eir_gaeldom_emperor_modifier": ("prestige_positive",
        {"monthly_prestige": 1, "legitimacy_gain_mult": 0.2, "vassal_opinion": 5},
        "Emperor of the Gael", "The Gaelic world has its emperor at last."),
    "eir_saints_blessing_modifier": ("piety_positive",
        {"monthly_piety": 0.5, "clergy_opinion": 5},
        "Blessing of the Saints", "The saints of Ireland smile on your reign."),
    "eir_synod_reform_modifier": ("piety_positive",
        {"clergy_opinion": 10, "monthly_piety": 0.3},
        "Reformed Dioceses", "You reorganised the Irish Church, and the clergy are grateful."),
    "eir_culdee_strife_modifier": ("piety_negative",
        {"clergy_opinion": -10, "monthly_piety": -0.2},
        "Culdee Strife", "The old Irish monks and the Roman reformers quarrel in your realm."),
    "eir_kin_strife_modifier": ("family_negative",
        {"courtier_and_guest_opinion": -10, "dynasty_house_opinion": -10},
        "Kin-Strife", "Your own kin plot over the succession, and the court takes sides."),
    "eir_throne_turmoil_modifier": ("prestige_negative",
        {"vassal_opinion": -10, "monthly_prestige": -0.3, "legitimacy_gain_mult": -0.2},
        "Throne in Turmoil", "The old king's titles lie in pieces, and every kinsman has a claim."),
    "eir_peace_of_tara_modifier": ("legitimacy_positive",
        {"vassal_opinion": 8, "legitimacy_gain_mult": 0.1},
        "Peace of Tara", "The kin of the old king have sworn to you at Tara."),
    "eir_gaelic_revival_modifier": ("prestige_positive",
        {"same_culture_opinion": 10, "monthly_prestige": 0.3},
        "Gaelic Revival", "A new pride in the Gaelic name stirs in Ireland."),
    "eir_dun_builder_modifier": ("stewardship_positive",
        {"holding_build_gold_cost": -0.1, "holding_build_speed": -0.1},
        "Builder of Dúns", "You raise ringforts and halls faster and cheaper than other kings."),
    "eir_sea_king_modifier": ("martial_positive",
        {"naval_movement_speed_mult": 0.2, "embarkation_cost_mult": -0.25},
        "Sea-King", "Your fleets ply the Irish Sea as the Norse once did."),
    "eir_tailteann_modifier": ("social_positive",
        {"stress_loss_mult": 0.15, "monthly_prestige": 0.2},
        "Games of Tailtiu", "You held the old funeral games, and the island feasted for a fortnight."),
    "eir_samhain_dread_modifier": ("stress_negative",
        {"stress_gain_mult": 0.15},
        "Samhain Dread", "The veil was thin on Samhain night, and something followed you home."),
    "eir_beltane_vigor_modifier": ("health_positive",
        {"health": 0.1, "fertility": 0.1},
        "Beltane Vigor", "The Beltane fires have left you hale and hopeful."),
    "eir_wolfhound_bond_modifier": ("prowess_positive",
        {"prowess": 1, "monthly_lifestyle_xp_gain_mult": 0.05},
        "Bond of the Wolfhound", "A great Irish wolfhound never leaves your side."),
    "eir_hospitality_modifier": ("feast_positive",
        {"courtier_and_guest_opinion": 10, "monthly_income_mult": -0.02},
        "Famed Hospitality", "No guest ever left your hall hungry or sober."),
    "eir_lean_years_modifier": ("economy_negative",
        {"monthly_income_mult": -0.05},
        "Lean Years", "A string of bad harvests has emptied the granaries."),
    "eir_pilgrim_modifier": ("piety_positive",
        {"monthly_piety": 0.4, "stress_loss_mult": 0.1},
        "Pilgrim of Skellig", "You climbed the Skellig steps, and the climb changed you."),
    "eir_relic_keeper_modifier": ("piety_positive",
        {"monthly_piety": 0.3, "clergy_opinion": 5},
        "Keeper of the Bell", "You hold an ancient saint's bell, and pilgrims come to see it."),
    "eir_sidhe_favour_modifier": ("fertility_positive",
        {"monthly_prestige": 0.1, "fertility": 0.1},
        "Favour of the Sídhe", "You left the good people their due, and they remember."),
    "eir_sidhe_anger_modifier": ("health_negative",
        {"health": -0.1, "stress_gain_mult": 0.1},
        "Anger of the Sídhe", "You disturbed a fairy mound, and ill luck has followed."),
    "eir_foreign_lords_modifier": ("diplomacy_negative",
        {"independent_ruler_opinion": -5, "monthly_prestige": -0.1},
        "Foreign Lords on Irish Soil", "Strangers with castles have landed, and your name suffers for every county they take."),
    "eir_hearth_of_the_gael_modifier": ("family_positive",
        {"monthly_dynasty_prestige": 0.3, "same_culture_opinion": 5},
        "Hearth of the Gael", "Your hall is where the Irish come to be Irish."),
    "eir_broken_hostage_modifier": ("hostage_negative",
        {"vassal_opinion": -6, "general_opinion": -5},
        "Hostage-Breaker", "You broke the sacred law of hostages, and no lord will give you one again without a fight."),
    "eir_tara_vigil_modifier": ("legend_positive",
        {"monthly_prestige": 0.3, "monthly_piety": 0.1},
        "Vigil at Tara", "You kept the old vigil on the Hill of Tara."),
}

COUNTY = {
    "eir_tara_hill_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 10, "development_growth_factor": 0.1, "tax_mult": 0.05},
        "Hill of Tara", "The seat of the High Kings draws pilgrims and petitioners alike."),
    "eir_cashel_rock_modifier": ("county_modifier_control_positive",
        {"county_opinion_add": 5, "tax_mult": 0.1, "defender_holding_advantage": 5},
        "Rock of Cashel", "A fortress and a cathedral on a single limestone crag."),
    "eir_armagh_see_modifier": ("county_modifier_development_positive",
        {"tax_mult": 0.1, "development_growth_factor": 0.1},
        "Primatial See of Armagh", "The seat of Saint Patrick, and the Church's pride in Ireland."),
    "eir_monastic_city_modifier": ("county_modifier_development_positive",
        {"development_growth_factor": 0.15, "tax_mult": 0.05},
        "Monastic City", "A great monastery has grown into a city of scholars, scribes and traders."),
    "eir_dublin_reclaimed_modifier": ("county_modifier_development_positive",
        {"tax_mult": 0.1, "county_opinion_add": 5, "travel_danger": -5},
        "Dublin Reclaimed", "The Norse longphort is Irish again, and the harbour is busy."),
    "eir_norse_garrison_modifier": ("county_modifier_control_negative",
        {"county_opinion_add": -15, "monthly_county_control_growth_add": -0.3},
        "Norse Garrison", "Foreign soldiers sit in the hall, and the locals do not love them."),
    "eir_raided_county_modifier": ("county_modifier_development_negative",
        {"development_growth_factor": -0.2, "county_opinion_add": -10},
        "Viking-Raided", "Longships came, and the fires burned for days."),
    "eir_high_cross_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 5, "development_growth_factor": 0.05},
        "High Crosses", "Carved stone crosses watch over the roads and the market."),
    "eir_cattle_raided_modifier": ("county_modifier_development_negative",
        {"tax_mult": -0.2, "county_opinion_add": -5},
        "Cattle Raided", "Raiders have driven off the herds. The county's wealth walked away."),
    "eir_oenach_ground_modifier": ("county_modifier_opinion_positive",
        {"tax_mult": 0.1, "county_opinion_add": 5},
        "Site of the Óenach", "The great assembly was held here, and the county profits from the memory."),
    "eir_famine_modifier": ("county_modifier_development_negative",
        {"development_growth_factor": -0.2, "county_opinion_add": -10},
        "Bad Harvest", "The fields failed, and the people are hungry."),
    "eir_holy_well_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 5, "development_growth_factor": 0.05},
        "Holy Well", "A well said to heal the sick draws visitors from far away."),
    "eir_sidhe_blessing_modifier": ("county_fertility_positive",
        {"county_fertility_growth_mult": 0.2, "county_opinion_add": 5},
        "Sídhe-Blessed", "The fields here are green, and the people say the good folk are to thank."),
    "eir_sidhe_curse_modifier": ("county_fertility_negative",
        {"development_growth_factor": -0.1, "county_fertility_decline_mult": 0.2},
        "Sídhe-Cursed", "Ill luck clings to this land since the mound was disturbed."),
    "eir_peat_wealth_modifier": ("county_modifier_development_positive",
        {"tax_mult": 0.05, "build_gold_cost": -0.05},
        "Peat Wealth", "The bogs give fuel, and now and then something older."),
    "eir_gallowglass_garrison_modifier": ("county_modifier_control_positive",
        {"levy_size": 0.1, "garrison_size": 0.1, "defender_holding_advantage": 5},
        "Gallowglass Garrison", "Hard Hebridean axemen guard this land."),
    "eir_tailteann_county_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 10, "development_growth_factor": 0.05},
        "Tailtiu Fair", "The old funeral games are held here, and the whole county profits."),
    "eir_glendalough_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 5, "tax_mult": 0.1},
        "Valley of Two Lakes", "Pilgrims follow Saint Kevin's footsteps to a remote monastic valley."),
    "eir_ringfort_country_modifier": ("county_modifier_control_positive",
        {"defender_holding_advantage": 5, "travel_danger": -5},
        "Ringfort Country", "Ringforts dot the hills, and every farm has a refuge within reach."),
    "eir_foreign_lords_county_modifier": ("county_modifier_control_negative",
        {"county_opinion_add": -10, "monthly_county_control_growth_add": -0.2},
        "Foreign Lords", "Strangers rule here, and speak no Irish."),
    "eir_loyal_county_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 10, "tax_mult": 0.05},
        "Grateful County", "The people remember who fed them in the hungry year."),
    "eir_punitive_levy_modifier": ("county_modifier_control_negative",
        {"county_opinion_add": -10, "tax_mult": 0.1},
        "Punitive Levy", "The king took grain from hungry people, and they have not forgotten."),
    "eir_native_resistance_modifier": ("county_modifier_control_negative",
        {"county_opinion_add": -15, "monthly_county_control_growth_add": -0.3, "levy_size": -0.1},
        "Irish Resistance", "The Gael have never loved a foreign lord, and they remember every wrong."),
    "eir_native_resistance_lite_modifier": ("county_modifier_control_negative",
        {"county_opinion_add": -8, "monthly_county_control_growth_add": -0.15},
        "Celtic Resistance", "The old tongue is spoken in secret here, and the old stories are not forgotten."),
    "eir_pacified_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 10, "monthly_county_control_growth_add": 0.2},
        "Pacified", "A hard-won peace holds here, for now."),
    "eir_reclaimed_land_modifier": ("county_modifier_opinion_positive",
        {"county_opinion_add": 10, "monthly_county_control_growth_add": 0.3},
        "Reclaimed Land", "After long years, the land is back in Irish hands."),
}

PROVINCE = {
    "eir_ringfort_province_modifier": ("county_modifier_control_positive",
        {"fort_level": 1, "defender_holding_advantage": 5},
        "Ringfort", "An earthen ringfort on the hill."),
    "eir_crannog_province_modifier": ("county_modifier_control_positive",
        {"defender_holding_advantage": 10, "supply_limit_mult": 0.1},
        "Crannóg", "A fortified island in the lake, reachable only by boat or hidden causeway."),
    "eir_round_tower_province_modifier": ("county_modifier_control_positive",
        {"defender_holding_advantage": 5, "fort_level": 1},
        "Round Tower", "A tall belfry that doubles as a refuge when raiders come."),
    "eir_beacon_province_modifier": ("county_modifier_control_positive",
        {"travel_danger": -5},
        "Warning Beacon", "A beacon on the headland warns of ships on the horizon."),
    "eir_standing_stone_province_modifier": ("economy_positive",
        {"monthly_income": 0.5},
        "Standing Stone", "An old standing stone draws small offerings and curious travellers."),
}

DYNASTY = {
    "eir_house_high_kings_modifier": ("family_positive",
        {"monthly_dynasty_prestige": 0.3},
        "House of the High Kings", "Your house gave Ireland a high king."),
    "eir_house_kinslayers_modifier": ("family_negative",
        {"monthly_dynasty_prestige": -0.2},
        "House of Kinslayers", "Your house took a crown by killing kin, and the island remembers."),
    "eir_house_poets_modifier": ("learning_positive",
        {"monthly_dynasty_prestige": 0.1},
        "House of Poets", "Your house is known for its bards and scholars."),
    "eir_house_exiles_modifier": ("family_negative",
        {"monthly_dynasty_prestige": -0.15},
        "House of Exiles", "Your house lost a kingdom, and its sons wander foreign courts."),
}

ARTIFACT = {
    "eir_book_of_kells_modifier": ("learning_positive",
        {"learning": 2, "monthly_piety": 0.3},
        "Illuminated Gospel", "A gospel book of astonishing beauty."),
    "eir_ardagh_chalice_modifier": ("piety_positive",
        {"monthly_piety": 0.4, "clergy_opinion": 5},
        "Silver Chalice", "A chalice of silver and gold, blessed by many bishops."),
    "eir_torc_of_tara_modifier": ("prestige_positive",
        {"monthly_prestige": 0.4, "vassal_opinion": 3},
        "Gold Torc", "A heavy gold neck-ring worn by the kings of Tara."),
    "eir_cathach_modifier": ("piety_positive",
        {"monthly_piety": 0.3, "prowess": 1, "knight_effectiveness_mult": 0.05},
        "Battle Psalter", "A psalter carried around the army three times before battle, so the story goes."),
    "eir_tara_brooch_modifier": ("prestige_positive",
        {"monthly_prestige": 0.3, "diplomacy": 2},
        "Silver Penannular Brooch", "An enormous brooch of silver and gold, worn by a lord who wished to be seen."),
    "eir_cross_of_cong_modifier": ("piety_positive",
        {"monthly_piety": 0.4, "clergy_opinion": 5, "monthly_prestige": 0.1},
        "Processional Cross", "A reliquary cross of oak and bronze, carried to bless the high kings."),
    "eir_caladbolg_modifier": ("prowess_positive",
        {"prowess": 3, "knight_effectiveness_mult": 0.1},
        "Hero's Sword", "A sword that the bards say belonged to a hero of the Red Branch."),
}

# =============================================================================
# FAME TRAITS
# =============================================================================
# name: (icon trait file, fields, display name, description)
TRAITS = {
    "eir_ard_ri": ("just", {"monthly_prestige": 0.5, "vassal_opinion": 5, "legitimacy_gain_mult": 0.1},
        "Ard Rí", "Crowned High King of Ireland at Tara."),
    "eir_ollamh": ("shrewd", {"learning": 2, "diplomacy": 1, "owned_legend_spread_mult": 0.1, "general_opinion": 3},
        "Ollamh", "Master of poetry, genealogy and the old tales."),
    "eir_fennid": ("brave", {"prowess": 4, "martial": 1, "knight_effectiveness_mult": 0.1},
        "Champion of the Fianna", "A warrior-hunter in the old Gaelic tradition."),
    "eir_brehon": ("just", {"learning": 1, "diplomacy": 1, "courtier_opinion": 5},
        "Brehon", "Learned in the ancient laws of Ireland."),
    "eir_viking_slayer": ("brave", {"prowess": 2, "martial": 1, "monthly_prestige": 0.2},
        "Slayer of Norsemen", "Has defeated Viking armies in the field."),
    "eir_foster_brother": ("honest", {"general_opinion": 5, "diplomacy": 1},
        "Foster-Brother", "Raised in another lord's hall and loyal to the bond."),
    "eir_banshee_marked": ("compassionate", {"health": -0.2, "intrigue": 1, "stress_gain_mult": 0.1},
        "Banshee-Marked", "The wail of the banshee has been heard at this character's door."),
    "eir_cattle_lord": ("diligent", {"stewardship": 1, "domain_tax_mult": 0.05},
        "Cattle Lord", "Master of the herds on which Irish wealth rests."),
}

# =============================================================================
# OPINION MODIFIERS
# =============================================================================
OPINIONS = {
    "eir_ard_ri_opinion": "Respects the High King",
    "eir_kinslayer_opinion": "Took a crown over a kinsman's corpse",
    "eir_fostered_opinion": "Bound by fosterage",
    "eir_tribute_resentment_opinion": "Resents the cow tribute",
    "eir_tanist_rival_opinion": "Rival claimant to the succession",
    "eir_poet_praise_opinion": "Praised in verse",
    "eir_satire_opinion": "Satirised in verse",
    "eir_gael_pride_opinion": "Shares Gaelic pride",
    "eir_hospitality_opinion": "Enjoyed your hospitality",
    "eir_norse_defied_opinion": "Defied the Norsemen",
    "eir_oenach_opinion": "Met at the great Óenach",
    "eir_exile_aid_opinion": "Aided in exile",
    "eir_trusts_justice_opinion": "Trusts the king's justice",
    "eir_saved_by_ruler_opinion": "Rescued by the ruler",
}

# =============================================================================
# CULTURE TRADITIONS
# =============================================================================
TRAD_COST = """	cost = {
		prestige = {
			add = {
				value = tradition_base_cost
				desc = BASE
				format = "BASE_VALUE_FORMAT"
			}
			multiply = tradition_replacement_cost_if_relevant
		}
	}
"""

# key: (layers, shown/pick trigger, params, modifier fields, name, desc)
TRADITIONS = {
    "tradition_eir_tanistic_fragmentation": ("martial", "shield.dds", None,
        {"eir_title_collapse_on_death": "yes", "eir_tanistic_culture": "yes"},
        {"levy_size": 0.1, "monthly_prestige_gain_mult": 0.05},
        "Tanistic Fragmentation",
        "In Ireland a kingdom was a man, not a throne. When the king died his realm fell apart, and the next strong claimant had to put it together again. Rulers of this culture lose their highest title on death (duchy or above), but their warbands are fierce and their pride is great."),
    "tradition_eir_high_kingship": ("diplo", "crown.dds", None,
        {"eir_stable_kingship": "yes"},
        {"legitimacy_gain_mult": 0.15, "vassal_opinion": 5, "monthly_prestige": 0.2},
        "Stable High Kingship",
        "The Irish have finally learned to keep a throne after the king who holds it is dead. The high kingship passes to the heir intact, and the lords of Ireland have grown used to bowing to it."),
    "tradition_eir_bardic_schools": ("learning", "quill.dds", None,
        {"eir_bardic_schools": "yes", "poet_trait_gives_bonuses": "yes", "poet_trait_more_common": "yes"},
        {"owned_legend_spread_mult": 0.1, "monthly_prestige_gain_mult": 0.05},
        "Bardic Schools",
        "Poets train for years in the schools of the Filí, learning genealogy, law and satire. A king without a poet is a king who will be forgotten, or mocked."),
    "tradition_eir_brehon_law": ("diplo", "council.dds", None,
        {"eir_brehon_law": "yes"},
        {"legitimacy_gain_mult": 0.1, "courtier_and_guest_opinion": 5},
        "Brehon Law",
        "Disputes are settled by learned judges according to laws older than the Church, with honour-prices for every crime and kin responsible for kin."),
    "tradition_eir_fosterage_bonds": ("diplo", "hostages.dds", None,
        {"eir_fosterage_bonds": "yes"},
        {"vassal_opinion": 5, "direct_vassal_opinion": 5},
        "Bonds of Fosterage",
        "Noble children are raised in other lords' halls, and the bond between foster-brothers is sometimes stronger than blood."),
    "tradition_eir_cattle_wealth": ("steward", "farmland.dds", None,
        {"eir_cattle_wealth": "yes"},
        {"domain_tax_mult": 0.05, "monthly_income": 1},
        "Cattle Wealth",
        "A man's worth is counted in cows. Cattle are wealth, tribute, dowry and the cause of half the island's wars."),
    "tradition_eir_gallowglass_heritage": ("martial", "swords.dds", None,
        {"eir_unlock_gallowglass": "yes"},
        {"men_at_arms_maintenance": -0.05},
        "Gallowglass Heritage",
        "Irish lords hire the hard axemen of the Hebrides and the Isles to serve as the core of their armies, and in time the warriors settle."),
    "tradition_eir_fianna_heritage": ("martial", "hunter.dds", None,
        {"eir_unlock_fianna": "yes"},
        {"knight_effectiveness_mult": 0.1},
        "Fianna Heritage",
        "The tales of Fionn mac Cumhaill and his band of hunter-warriors shape how young nobles fight. A warband that lives by the hunt is hard to catch and hard to beat."),
    "tradition_eir_culdee_christianity": ("learning", "temple.dds", None,
        {"eir_culdee_christianity": "yes"},
        {"monthly_piety_gain_mult": 0.1, "clergy_opinion": 5},
        "Celtic Christianity",
        "Irish monasteries, scriptoria and wandering saints give the Christianity of this culture a flavour all its own."),
    "tradition_eir_sea_kings": ("martial", "ship.dds", None,
        {"eir_sea_kings": "yes"},
        {"naval_movement_speed_mult": 0.25, "embarkation_cost_mult": -0.25},
        "Kings of the Irish Sea",
        "The Irish Sea belongs to everyone who dares sail it, and Irish kings have decided it is time to dare."),
}

# =============================================================================
# MEN-AT-ARMS
# =============================================================================
MAA = {
    "eir_gallowglass": dict(
        base="heavy_infantry", damage=44, toughness=30, pursuit=0, screen=20,
        terrain={"hills": "damage = 8 toughness = 4", "forest": "damage = 6", "wetlands": "damage = -5"},
        counters="pikemen = 1\n\t\tarchers = 1", icon="danish_huskarls", prov="infantry_moderate",
        param="eir_unlock_gallowglass", flag="eir_unlock_gallowglass",
        cost=("huscarls_recruitment_cost", "huscarls_low_maint_cost", "huscarls_high_maint_cost"),
        name="Gallowglass",
        flavor="Hard Hebridean axemen who sell their lives dearly and their services dearer."),
    "eir_fianna_warband": dict(
        base="skirmishers", damage=18, toughness=18, pursuit=20, screen=20,
        terrain={"forest": "damage = 8 toughness = 6", "hills": "damage = 6 toughness = 4", "mountains": "damage = 4 toughness = 4"},
        counters="heavy_infantry = 1\n\t\tarchers = 1", icon="mountaineer", prov="infantry_cheap",
        param="eir_unlock_fianna", flag="eir_unlock_fianna",
        cost=("skirmisher_recruitment_cost", "skirmisher_low_maint_cost", "skirmisher_high_maint_cost"),
        name="Fianna Warband",
        flavor="Hunter-warriors who live in the forest and strike like the heroes of the old tales."),
    "eir_kern_javelineers": dict(
        base="skirmishers", damage=14, toughness=12, pursuit=16, screen=12,
        terrain={"forest": "damage = 6", "hills": "damage = 4", "wetlands": "damage = 4"},
        counters="heavy_cavalry = 1", icon="light_cavalry", prov="infantry_cheap",
        param="eir_unlock_fianna", flag="eir_unlock_kern",
        cost=("skirmisher_recruitment_cost", "skirmisher_low_maint_cost", "skirmisher_high_maint_cost"),
        name="Kern Javelineers",
        flavor="Light-footed javelin throwers of the Irish hills, hard to pin down and quick to run."),
    "eir_tara_guard": dict(
        base="heavy_infantry", damage=36, toughness=34, pursuit=0, screen=26,
        terrain={"plains": "damage = 6", "hills": "toughness = 4"},
        counters="light_cavalry = 1\n\t\tpikemen = 1", icon="palace_guards", prov="infantry_moderate",
        param="eir_stable_kingship", flag="eir_unlock_tara_guard",
        cost=("huscarls_recruitment_cost", "huscarls_low_maint_cost", "huscarls_high_maint_cost"),
        name="Guard of Tara",
        flavor="The household troops of the High King, sworn to defend the kingship itself."),
}

# =============================================================================
# BUILDINGS
# =============================================================================
# key: (holding, flag, icon, modifiers dict by section, name, desc)
BUILDINGS = {
    "eir_ringfort_01": ("castle", "eir_unlock_ringfort", "icon_building_hill_forts.dds",
        {"province": {"defender_holding_advantage": 5, "monthly_income": 0.2},
         "county": {"levy_size": 0.05},
         "character": {"knight_effectiveness_mult": 0.02}},
        "Great Ringfort", "A mighty earthen ringfort in the old Irish style, ringed by banks and ditches."),
    "eir_crannog_01": ("castle", "eir_unlock_crannog", "icon_building_palisades.dds",
        {"province": {"defender_holding_advantage": 10, "supply_limit_mult": 0.1},
         "county": {"monthly_county_control_growth_add": 0.2},
         "character": {}},
        "Crannóg Stronghold", "A fortified artificial island in a lake, reachable only by boat or a hidden causeway."),
    "eir_round_tower_01": ("church", "eir_unlock_round_tower", "icon_building_watchtowers.dds",
        {"province": {"defender_holding_advantage": 5, "monthly_income": 0.2},
         "county": {"county_opinion_add": 3},
         "character": {"monthly_piety": 0.1}},
        "Round Tower", "A tall stone belfry that doubles as a refuge and treasury when raiders come."),
    "eir_high_cross_01": ("church", "eir_unlock_high_cross", "icon_building_graveyard.dds",
        {"province": {"monthly_income": 0.2},
         "county": {"county_opinion_add": 5, "development_growth_factor": 0.02},
         "character": {"monthly_piety": 0.15}},
        "High Cross", "A carved stone cross, taller than three men, covered in scenes from scripture."),
    "eir_scriptorium_01": ("church", "eir_unlock_scriptorium", "icon_building_library.dds",
        {"province": {"monthly_income": 0.3},
         "county": {"development_growth_factor": 0.04},
         "character": {"monthly_piety": 0.1, "learning": 1}},
        "Great Scriptorium", "Monks copy and illuminate gospel books in the old Irish style."),
    "eir_brehon_court_01": ("city", "eir_unlock_brehon_court", "icon_building_tax_assessor.dds",
        {"province": {"monthly_income": 0.3},
         "county": {"county_opinion_add": 4, "monthly_county_control_growth_add": 0.2},
         "character": {"legitimacy_gain_mult": 0.01}},
        "Brehon Court", "A court where learned judges apply the ancient laws to every dispute."),
    "eir_bardic_school_01": ("city", "eir_unlock_bardic_school", "icon_building_monastic_schools.dds",
        {"province": {"monthly_income": 0.2},
         "county": {"county_opinion_add": 3},
         "character": {"monthly_prestige": 0.1, "owned_legend_spread_mult": 0.02}},
        "Bardic School", "A school where poets train for twelve years before they may recite before a king."),
    "eir_cattle_enclosure_01": ("castle", "eir_unlock_cattle_enclosure", "icon_building_hillside_grazing.dds",
        {"province": {"monthly_income": 0.5},
         "county": {"tax_mult": 0.03},
         "character": {"domain_tax_mult": 0.01}},
        "Great Cattle Enclosure", "Walled fields where the herds that make up a lord's wealth are kept safe from raiders."),
}

# =============================================================================
# TITLES
# =============================================================================
# key: (tier, capital, color rgb, can_create trigger, emblem, c1, c2, name, adj, pre)
TITLES = {
    "k_eir_munster": ("k", "c_ormond", (210, 150, 20), "eir_can_create_provincial_kingdom_trigger = { DUCHY = d_munster }",
        "ce_harp.dds", "red", "yellow", "Munster", "Munster", "Munster"),
    "k_eir_ulster": ("k", "c_ulster", (160, 20, 20), "eir_can_create_provincial_kingdom_trigger = { DUCHY = d_ulster }",
        "ce_hand.dds", "yellow", "red", "Ulster", "Ulster", "Ulster"),
    "k_eir_leinster": ("k", "c_leinster", (30, 120, 60), "eir_can_create_provincial_kingdom_trigger = { DUCHY = d_leinster }",
        "ce_harp.dds", "green", "white", "Leinster", "Leinster", "Leinster"),
    "k_eir_connacht": ("k", "c_connacht", (40, 90, 160), "eir_can_create_provincial_kingdom_trigger = { DUCHY = d_connacht }",
        "ce_harp.dds", "blue", "white", "Connacht", "Connacht", "Connacht"),
    "k_eir_meath": ("k", "c_dublin", (110, 60, 130), "eir_can_create_provincial_kingdom_trigger = { DUCHY = d_meath }",
        "ce_harp.dds", "purple", "yellow", "Meath", "Meath", "Meath"),
    "k_eir_dal_riata": ("k", "c_ailech", (30, 150, 140), "eir_can_create_dal_riata_trigger = yes",
        "ce_harp.dds", "blue", "yellow", "Dál Riata", "Dál Riatan", "Dál Riato"),
    "e_eir_gaeldom": ("e", "c_dublin", (10, 110, 40), "eir_can_create_gaeldom_trigger = yes",
        "ce_harp.dds", "green", "yellow", "Gaeldom", "Gaelic", "Gaelo"),
}


def build():
    # ---------------------------------------------------------------- modifiers
    L = Loc("eir_world_l_english.yml")
    out = ["# Eire Reborn - modifiers. Generated by tools/gen_world.py\n"]
    for label, group in (("character", CHAR), ("county", COUNTY), ("province", PROVINCE),
                         ("dynasty / house", DYNASTY), ("artifact", ARTIFACT)):
        out.append("\n##### %s modifiers #####\n\n" % label)
        L.section(label + " modifiers")
        for name, (icon, fields, disp, desc) in group.items():
            check_keys(name, fields)
            out.append("%s = {\n\ticon = %s\n%s}\n\n" % (name, icon, fields_block(fields)))
            L.add(name, disp)
            L.add(name + "_desc", desc)
    write("common/modifiers/eir_modifiers.txt", "".join(out))

    # ---------------------------------------------------------------- traits
    out = ["# Eire Reborn - fame traits\n\n"]
    L.section("traits")
    for name, (icon, fields, disp, desc) in TRAITS.items():
        check_keys(name, fields)
        out.append("%s = {\n\tcategory = fame\n%s\n\tshown_in_ruler_designer = no\n" % (name, fields_block(fields)))
        out.append('\ticon = {\n\t\tfirst_valid = {\n\t\t\tdesc = "gfx/interface/icons/traits/%s.dds"\n\t\t}\n\t}\n}\n\n' % icon)
        L.add("trait_" + name, disp)
        L.add("trait_%s_desc" % name, desc)
        L.add("trait_%s_character_desc" % name, desc)
    write("common/traits/eir_traits.txt", "".join(out))

    # ---------------------------------------------------------------- opinions
    out = ["# Eire Reborn - opinion modifiers\n\n"]
    L.section("opinion modifiers")
    for name, disp in OPINIONS.items():
        out.append("%s = {\n\tmonthly_change = 0.1\n\tdecaying = yes\n\tstacking = yes\n}\n\n" % name)
        L.add(name, disp)
    write("common/opinion_modifiers/eir_opinion_modifiers.txt", "".join(out))

    # ---------------------------------------------------------------- traditions
    out = ["# Eire Reborn - culture traditions\n\n"]
    L.section("culture traditions")
    for key, (bg, item, _x, params, mods, disp, desc) in TRADITIONS.items():
        check_keys(key, mods)
        hidden = key in ("tradition_eir_tanistic_fragmentation", "tradition_eir_high_kingship")
        out.append("%s = {\n\tcategory = regional\n\n\tlayers = {\n\t\t0 = %s\n\t\t1 = western\n\t\t4 = %s\n\t}\n\n" % (key, bg, item))
        if hidden:
            out.append("\tis_shown = {\n\t\talways = no\n\t}\n\tcan_pick = {\n\t\talways = no\n\t}\n\n")
        else:
            out.append("\tis_shown = {\n\t\thas_cultural_pillar = heritage_goidelic\n\t}\n\tcan_pick = {\n\t\thas_cultural_pillar = heritage_goidelic\n\t}\n\n")
        out.append("\tparameters = {\n" + "".join("\t\t%s = %s\n" % (k, v) for k, v in params.items()) + "\t}\n\n")
        out.append("\tcharacter_modifier = {\n%s\t}\n\n" % fields_block(mods, "\t\t"))
        out.append(TRAD_COST + "\n\tai_will_do = {\n\t\tvalue = 20\n\t}\n}\n\n")
        L.add(key + "_name", disp)
        L.add(key + "_desc", desc)
    write("common/culture/traditions/eir_traditions.txt", "".join(out))

    # ---------------------------------------------------------------- men-at-arms
    out = ["# Eire Reborn - men-at-arms\n\n"]
    L.section("men-at-arms")
    for key, d in MAA.items():
        b, l, h = d["cost"]
        terr = "".join("\t\t%s = { %s }\n" % (t, v) for t, v in d["terrain"].items())
        prov = {"infantry_cheap": 3, "infantry_moderate": 7}[d["prov"]]
        out.append("""%(key)s = {
	type = %(base)s

	damage = %(damage)d
	toughness = %(toughness)d
	pursuit = %(pursuit)d
	screen = %(screen)d

	terrain_bonus = {
%(terr)s	}

	counters = {
		%(counters)s
	}

	can_recruit = {
		OR = {
			culture ?= { has_cultural_parameter = %(param)s }
			AND = {
				culture ?= { has_cultural_pillar = heritage_goidelic }
				has_global_variable = %(flag)s
			}
		}
	}

	buy_cost = { gold = %(b)s }
	low_maintenance_cost = { gold = %(l)s }
	high_maintenance_cost = { gold = %(h)s }
	provision_cost = %(prov)d

	stack = 100
	ai_quality = { value = 20 }
	icon = %(icon)s
}

""" % dict(key=key, base=d["base"], damage=d["damage"], toughness=d["toughness"], pursuit=d["pursuit"],
           screen=d["screen"], terr=terr, counters=d["counters"], param=d["param"], flag=d["flag"],
           b=b, l=l, h=h, prov=prov, icon=d["icon"]))
        L.add(key, d["name"])
        L.add(key + "_flavor", "#F " + d["flavor"] + "#!")
    write("common/men_at_arms_types/eir_maa_types.txt", "".join(out))

    # ---------------------------------------------------------------- buildings
    out = ["# Eire Reborn - unique Irish buildings. Each needs a character flag set by a decision or event.\n\n"]
    L.section("buildings")
    hold = {"castle": "castle_holding", "church": "church_holding", "city": "city_holding"}
    for key, (h, flag, icon, mods, disp, desc) in BUILDINGS.items():
        for sect in mods.values():
            check_keys(key, sect)

        def blk(name, d):
            return "" if not d else "\t%s = {\n%s\t}\n" % (name, fields_block(d, "\t\t"))
        out.append("""%(key)s = {
	construction_time = slow_construction_time

	is_enabled = {
		has_global_variable = %(flag)s
	}

	can_construct_potential = {
		has_holding_type = %(hold)s
		has_global_variable = %(flag)s
	}

	can_construct_showing_failures_only = {
		scope:holder = { is_at_war = no }
	}

	cost_gold = normal_building_tier_1_cost

%(prov)s%(cty)s%(chr)s
	type_icon = "%(icon)s"

	ai_value = {
		base = 5
	}
}

""" % dict(key=key, flag=flag, hold=hold[h], icon=icon, prov=blk("province_modifier", mods["province"]),
           cty=blk("county_modifier", mods["county"]), chr=blk("character_modifier", mods["character"])))
        L.add("building_" + key, disp)
        L.add("building_%s_desc" % key, desc)
    write("common/buildings/eir_buildings.txt", "".join(out))

    # ---------------------------------------------------------------- titles
    out = ["# Eire Reborn - new titles (de jure empty; created by their holders)\n\n"]
    coa = ["# Eire Reborn - coats of arms for the new titles\n\n"]
    L.section("titles")
    for key, (tier, cap, rgb, trig, emblem, c1, c2, name, adj, pre) in TITLES.items():
        out.append("""%(key)s = {
	color = { %(r)d %(g)d %(b)d }
	capital = %(cap)s

	can_create = {
		%(trig)s
	}

	can_be_named_after_dynasty = no
}

""" % dict(key=key, r=rgb[0], g=rgb[1], b=rgb[2], cap=cap, trig=trig))
        coa.append("""%s = {
	pattern = "pattern_solid.dds"
	color1 = "%s"
	color2 = "%s"
	colored_emblem = {
		texture = "%s"
		color1 = "%s"
		color2 = "%s"
		instance = { position = { 0.5 0.5 } scale = { 0.8 0.8 } }
	}
}

""" % (key, c1, c2, emblem, c2, c2))
        L.add(key, name)
        L.add(key + "_adj", adj)
        L.add(key + "_pre", pre)
    write("common/landed_titles/eir_titles.txt", "".join(out))
    write("common/coat_of_arms/coat_of_arms/eir_titles.txt", "".join(coa))
    L.write()
    print("world: %d char, %d county, %d province, %d dynasty, %d artifact modifiers; %d traits; %d traditions; %d maa; %d buildings; %d titles"
          % (len(CHAR), len(COUNTY), len(PROVINCE), len(DYNASTY), len(ARTIFACT), len(TRAITS), len(TRADITIONS), len(MAA), len(BUILDINGS), len(TITLES)))


if __name__ == "__main__":
    build()
