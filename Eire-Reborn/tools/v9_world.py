"""Update 3 content pack: modifiers, nickname and names for the five Conquerors. Imported at the end of v8_world.py."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS
import v8_world
from conq_data import CONQ

v8_world.NICKS.append(("nick_eir_warlord_slayer", "the Warlord-Slayer", "Met a conqueror's great army in the field and sent it home beaten."))

C("eir_conqueror_modifier", "dread_mixed", {"advantage": 4, "levy_size": 0.2, "knight_effectiveness_mult": 0.1, "levy_reinforcement_rate": 0.2},
  "The Conqueror", "A king with nine thousand men and an idea about the map, and he does not plan to go home with either unused.")
C("eir_conqueror_emboldened_modifier", "dread_mixed", {"advantage": 3, "monthly_prestige": 0.2},
  "Emboldened", "He tested the Irish defences, found them wanting, and told his men so.")
C("eir_conq_tributary_modifier", "prestige_negative", {"monthly_prestige": -0.3, "general_opinion": -5, "vassal_opinion": -4, "dread_gain_mult": -0.1},
  "Paid the Conqueror", "You bought off a conqueror with silver, and every king in the island knows what you paid.")
C("eir_conq_resolve_modifier", "prestige_positive", {"stress_gain_mult": -0.1, "monthly_prestige": 0.2, "defender_advantage": 3},
  "Resolve to Rebuild", "You swore to put back every mill, church and ford that the war destroyed, and the people have heard you.")

K("eir_ravaged_modifier", "county_modifier_development_negative", {"tax_mult": -0.25, "development_growth_factor": -0.2, "county_opinion_add": -10, "monthly_county_control_growth_add": -0.3, "levy_size": -0.15},
  "Ravaged by a Conqueror", "Burned mills, taxed churches, driven herds and a new language on the charters. The rebuilding will take a generation, or a decision.")
K("eir_liberated_county_modifier", "county_modifier_opinion_positive", {"county_opinion_add": 10, "development_growth_factor": 0.1, "tax_mult": 0.05, "levy_size": 0.05, "monthly_county_control_growth_add": 0.3},
  "Liberated County", "The invader was beaten here, and the people have built a cairn and a legend on the strength of it.")
K("eir_rebuilt_county_modifier", "county_modifier_development_positive", {"development_growth_factor": 0.15, "county_opinion_add": 8, "tax_mult": 0.08, "monthly_county_control_growth_add": 0.2},
  "Rebuilt Stronger", "The mills are back, the church has a new roof, and the people say it is better than it was.")

for c in CONQ:
    k = c["id"]
    C(c["bane"], "prestige_positive", {"monthly_prestige": 0.5, "dread_gain_mult": 0.15, "advantage": 2, "general_opinion": 3, "vassal_opinion": 3},
      c["bane_name"], c["bane_desc"])
    ARTIFACT[c["sword"] + "_modifier"] = ("prowess_positive", {"prowess": 2, "monthly_prestige": 0.3, "knight_effectiveness_mult": 0.08, "dread_gain_mult": 0.1},
                                          c["sword_name"], c["sword_desc"])
    v8_world.LOC.append((c["sword"] + "_name", c["sword_name"]))
    v8_world.LOC.append((c["sword"] + "_desc", c["sword_desc"]))
    v8_world.LOC.append(("eir_conq%d_host_name" % k, c["army"]))
