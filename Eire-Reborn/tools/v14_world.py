"""Update 8 content pack (activities, court, culture, faith, law, war, struggle): modifiers, opinions and names shared by the generators."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS, TRADS

NICKS = []
LOC = []

# ---- the raiding line of the Irish: Pastoralists -> Bó-aire (raid over land) -> Táin Bó (raid at sea too) -> The Four Seas (every kind of raid)
_RAID_BASE = {"pastures_building_bonuses": "yes", "farm_estates_pastures_unlock": "yes", "better_herders_pasturalists": "yes",
              "eir_cattle_wealth": "yes", "eir_tributaries_inherited": "yes",
              "culture_can_raid_over_land_even_if_feudal": "yes", "not_tribal_raiding_malus": "yes"}
TRADS["tradition_eir_tain_bo"] = ("martial", "battle.dds", None,
    dict(_RAID_BASE, **{"culture_can_raid_at_sea_even_if_feudal": "yes", "eir_tain_bo": "yes"}),
    {"negate_health_penalty_add": 0.15, "prowess": 1, "stewardship": 1, "domain_tax_mult": 0.05, "monthly_income": 1,
     "max_loot_mult": 0.25, "raid_speed": 0.15, "naval_movement_speed_mult": 0.1},
    "Táin Bó: The Great Cattle Raid",
    "The old story of the Cattle Raid of Cooley is told at every hearth, and the young nobles want a táin of their own. Raiding is now a lord's honour, on land and across the water, with a quarter more loot. Replaces Bó-aire; keeps all of its effects. Next step: the Four Seas.")
TRADS["tradition_eir_four_seas"] = ("martial", "ship.dds", None,
    dict(_RAID_BASE, **{"culture_can_raid_at_sea_even_if_feudal": "yes", "culture_can_raid_over_land_even_if_feudal_no_restrictions": "yes",
                        "culture_can_raid_at_sea_even_if_feudal_no_restrictions": "yes", "eir_tain_bo": "yes", "eir_four_seas": "yes"}),
    {"negate_health_penalty_add": 0.15, "prowess": 1, "stewardship": 1, "domain_tax_mult": 0.05, "monthly_income": 1,
     "max_loot_mult": 0.5, "raid_speed": 0.3, "naval_movement_speed_mult": 0.2, "knight_effectiveness_mult": 0.05},
    "Raiders of the Four Seas",
    "From the Hebrides to Aquitaine, the Irish are known to be the best raiders of the Atlantic coast, and no kind of raid is closed to them: by land or sea, against Christian or heathen, in summer or winter. Half again as much loot. Replaces Táin Bó; keeps all of its effects.")

OPINIONS["eir_act_hosted_opinion"] = "Hosted a fine gathering"
OPINIONS["eir_act_insulted_opinion"] = "Insulted at the gathering"
OPINIONS["eir_act_brawl_opinion"] = "Brawled at the gathering"

# ---- casus belli
C("eir_cattle_plunder_modifier", "economy_positive", {"monthly_income": 1.0, "monthly_prestige": 0.1, "levy_reinforcement_rate": 0.05},
  "Cattle Plunder", "The herds of a neighbouring county are in your fields and the poets are already composing the story.")
C("eir_cain_received_modifier", "economy_positive", {"monthly_income": 1.5, "monthly_prestige": 0.15, "dread_gain_mult": 0.1},
  "The Cáin Received", "A neighbouring lord pays you the yearly cáin: cattle in autumn, silver in spring, and a very long face at the feast.")
C("eir_owes_cain_modifier", "economy_negative", {"monthly_income": -1.0, "vassal_opinion": -3, "general_opinion": -3},
  "Owes the Cáin", "Defeat has made you pay a yearly tribute to a stronger king. Your lords have noticed.")

# ---- religion
C("eir_fires_kindled_modifier", "piety_positive", {"monthly_piety": 0.3, "monthly_prestige": 0.2, "clergy_opinion": -15, "vassal_opinion": -3, "stress_gain_mult": 0.1},
  "The Fires Kindled", "You lit the quarter-day fires in public. The people sing, the monks write letters, and the vassals check where their own priests stand.")
C("eir_penitent_modifier", "piety_negative", {"monthly_prestige": -0.2, "clergy_opinion": 10, "stress_gain_mult": -0.05, "monthly_piety": 0.1},
  "Penitent", "You came back to the Church on your knees. The abbots are satisfied, the court is smirking and the people are confused.")
C("eir_culdee_reform_modifier", "piety_positive", {"monthly_piety": 0.4, "clergy_opinion": 8, "monthly_prestige": 0.1, "levy_size": -0.03},
  "Culdee Reform", "Your Church is a Church of hermits and small houses, and its abbots live on barley bread and good report. The great bishops are not happy.")

# ---- struggle
C("eir_end_of_strife_modifier", "prestige_positive", {"monthly_prestige": 0.5, "vassal_opinion": 8, "general_opinion": 4, "legitimacy_gain_mult": 0.15, "stress_gain_mult": -0.1},
  "The Strife Ended", "The great quarrel of the kings is over, and nobody now alive remembers who began it.")
