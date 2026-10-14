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
