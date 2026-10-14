"""Update 7 (Celtic tenets) content pack: the boon modifier of every tenet decision, the Grail, the curse of a broken geis."""
from extra_world import C, K, CHAR, COUNTY, ARTIFACT, OPINIONS
from tenet_data import T, ORDER

NICKS = []
LOC = [("eir_grail_name", "The Vessel of the Island"),
       ("eir_grail_desc", "A plain cup of dark wood bound in silver, found at the end of a long ride. The land is a little greener where it is carried.")]

for k in ORDER:
    t = T[k]
    inv = t["inv"]
    C("eir_tn_%s_boon_modifier" % k, "prestige_positive", inv["boon"], inv["bname"], inv["bdesc"])

C("eir_geis_broken_modifier", "prestige_negative", {"monthly_prestige": -0.5, "stress_gain_mult": 0.2, "vassal_opinion": -5, "advantage": -2},
  "A Geis Broken", "You broke the taboo, and the omens were right. The strength it gave you has turned round and is looking at you.")
ARTIFACT["eir_grail_modifier"] = ("piety_positive", {"monthly_piety": 0.8, "monthly_prestige": 0.5, "health": 0.2, "general_opinion": 5},
    "The Vessel of the Island", "A cup that heals the land.")
