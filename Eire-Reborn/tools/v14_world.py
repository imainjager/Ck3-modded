"""Update 8 content pack (activities, court, culture, faith, law, war, struggle): modifiers, opinions and names shared by the generators."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS

NICKS = []
LOC = []

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
