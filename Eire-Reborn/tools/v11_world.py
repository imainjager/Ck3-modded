"""Update 5 (Great Saxon Uprising) content pack: modifiers, nickname and names."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS

NICKS = [("nick_eir_saxon_breaker", "the Saxon-Breaker", "Put down the greatest English rising since the Gaels took the island, and made the peace stick.")]
LOC = [("eir_gsu_host_name", "The Saxon Host")]

C("eir_saxon_rebel_modifier", "dread_mixed", {"advantage": 3, "levy_size": 0.2, "knight_effectiveness_mult": 0.05, "levy_reinforcement_rate": 0.2},
  "Leader of the Rising", "A thane the English chose on the hill, with a county, a banner and an army of men who have nothing left to lose.")
C("eir_saxon_subdued_modifier", "prestige_positive", {"monthly_prestige": 0.6, "vassal_opinion": 6, "dread_gain_mult": 0.2, "advantage": 2, "general_opinion": 3},
  "The Saxons Subdued", "You broke the Great Saxon Uprising, and the English have learned what the Gael is capable of.")
C("eir_saxon_shaken_modifier", "prestige_negative", {"monthly_prestige": -0.4, "vassal_opinion": -6, "levy_size": -0.1, "stress_gain_mult": 0.1},
  "Shaken by the Uprising", "The English took the duchies back, burned what they could not hold and left the throne with the smell of smoke on it.")
C("eir_saxon_amnesty_modifier", "family_positive", {"general_opinion": 5, "vassal_opinion": 3, "stress_gain_mult": -0.05, "monthly_prestige": 0.15},
  "The Winchester Amnesty", "You pardoned the leaders who laid down their arms, and the English remember who was merciful.")
