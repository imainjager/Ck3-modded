"""Update 6 (Return of the Celts) content pack: the Forest Warriors, their tradition, the modifiers and the names."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS, MAA, TRADS
from celt_data import REGIONS

NICKS = []
LOC = []

# ------------------------------------------------------------------ the Forest Warriors
MAA["eir_forest_warriors"] = dict(
    base="skirmishers", damage=35, toughness=20, pursuit=15, screen=20,
    terrain={"forest": "damage = 20", "jungle": "damage = 20", "desert": "damage = -20", "plains": "damage = 5", "hills": "damage = 10"},
    counters="heavy_infantry = 1\n\t\tarchers = 1", icon="mountaineer", prov="infantry_moderate",
    param="eir_forest_warriors", flag="eir_unlock_forest_warriors", only_param=True,
    cost=("huscarls_recruitment_cost", "huscarls_low_maint_cost", "huscarls_high_maint_cost"),
    name="Forest Warriors",
    flavor="Painted warriors of the old Celtic revival, who fight best under the oaks and have never lost a wood to anyone.")

# ------------------------------------------------------------------ the tradition (added to the culture by the decision; hidden from the picker)
TRADS["tradition_eir_forest_warriors"] = ("martial", "forest.dds", None,
    {"eir_forest_warriors": "yes", "easier_to_hybridize": "yes", "cheaper_to_hybridize": "yes", "cheaper_convert_to_local_culture": "yes"},
    {"different_culture_opinion": -20, "same_heritage_county_advantage_add": 10, "faith_conversion_piety_cost_mult": -0.4,
     "forest_advantage": 5, "monthly_prestige_gain_mult": 0.05, "knight_effectiveness_mult": 0.05},
    "Mystical Celtic Warriors",
    "The druids' groves have been planted again and the Forest Warriors have come out of them. The culture finds it easier to hybridise, to diverge and to convert its neighbours, and holds its own lands with +10 advantage, but those outside the oaks like it much less. Unlocks the Forest Warriors and the Sacred Grove (Nemeton).")

# ------------------------------------------------------------------ county modifiers
K("eir_forest_dominion_modifier", "county_modifier_development_positive",
  {"development_growth_factor": 0.25, "forest_development_growth_factor": 0.5, "county_opinion_add": 3},
  "Realm of the Oaks", "The old forests of the island are being replanted and walked again, and what grows under the oaks no longer holds the county back.")
K("eir_mainland_resistance_modifier", "county_modifier_control_negative",
  {"county_opinion_add": -30, "monthly_county_control_growth_add": -0.4, "tax_mult": -0.15, "levy_size": -0.15},
  "Resisting the Celtic Revival", "The county was told to speak the old tongue of the Celts, and its people would rather not.")

# ------------------------------------------------------------------ character modifiers
C("eir_mystic_celts_modifier", "prestige_positive",
  {"monthly_prestige": 1.5, "knight_effectiveness_mult": 0.15, "advantage": 3, "monthly_piety": 0.5, "owned_legend_spread_mult": 0.3, "vassal_opinion": 8, "general_opinion": -5},
  "Emperor of the Oaks", "The druids' groves are planted again and the Forest Warriors walk out of them. Your men fear nothing, and everyone else is a little afraid of them.")
C("eir_celts_mainland_modifier", "prestige_positive",
  {"monthly_prestige": 1.0, "advantage": 3, "vassal_opinion": 6, "dread_gain_mult": 0.2, "stress_gain_mult": -0.1},
  "The Celts Look to the Mainland", "The island is whole. The poets have begun to recite the names of the tribes that lived across the sea.")
_RET = {
    "france": {"monthly_prestige": 0.6, "advantage": 3, "knight_effectiveness_mult": 0.1},
    "germany": {"monthly_prestige": 0.5, "advantage": 3, "martial": 2, "levy_size": 0.1},
    "spain": {"monthly_prestige": 0.5, "monthly_piety": 0.3, "advantage": 3, "diplomacy": 2},
    "italy": {"monthly_prestige": 0.6, "dread_gain_mult": 0.2, "advantage": 3, "stewardship": 2},
    "galatia": {"monthly_prestige": 0.6, "advantage": 3, "learning": 2, "owned_legend_spread_mult": 0.2},
}
_WON = {
    "france": {"monthly_prestige": 1.2, "vassal_opinion": 8, "knight_effectiveness_mult": 0.15, "general_opinion": 4},
    "germany": {"monthly_prestige": 1.2, "levy_size": 0.2, "martial": 3, "vassal_opinion": 8},
    "spain": {"monthly_prestige": 1.0, "monthly_piety": 0.6, "diplomacy": 3, "vassal_opinion": 8, "general_opinion": 4},
    "italy": {"monthly_prestige": 1.2, "dread_gain_mult": 0.3, "stewardship": 3, "monthly_income": 3},
    "galatia": {"monthly_prestige": 1.2, "learning": 3, "owned_legend_spread_mult": 0.3, "vassal_opinion": 8, "monthly_piety": 0.4},
}
for k, r in REGIONS.items():
    C("eir_return_%s_modifier" % k, "prestige_positive", _RET[k],
      "The Return of the Celts to %s" % r["name"],
      "The Gael has set a claim on %s, and every %s county in your realm hears the old tongue five times as often. %s" % (r["area_name"], r["adj"], r["story"]))
    C("eir_celt_%s_won_modifier" % k, "prestige_positive", _WON[k],
      "The Celts Return to %s" % r["name"],
      "Half of the counties of %s now speak your tongue. %s" % (r["area_name"], r["story"]))
