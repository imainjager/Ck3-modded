"""Update 8 events: the road tracker (0990), the Druidic revival (0991), the return to the Church (0992), the Culdee Reform (0993)."""
import re
from ev_h import *
import ev_h
import story_chain
EVENTS = ev_h.EVENTS = []

# ---------------------------------------------------------------------------------------------------------------- 0990 the tracker
# Registered after all decisions exist: the text is built from them, in the order of the purple road.


def _tracker_variants():
    import gen_decisions
    import dec_v14  # noqa: F401  (adds the step flags to the decisions)
    dec = {d["key"]: d for d in gen_decisions.DEC}
    out = []
    total = len(story_chain.STEP)
    for label, keys in story_chain.ACTS:
        for k in keys:
            key = "eir_%s_decision" % k
            d = dec[key]
            flag = "eir_story_done_" + k
            sets = [v for v in re.findall(r"set_global_variable = ([a-z_0-9]+)", d["effect"]) if v != flag and not v.startswith("eir_story_done_")]
            done = "has_global_variable = %s" % flag
            if sets:
                done = "OR = {\n\t%s\n\t%s\n}" % (done, "\n\t".join("has_global_variable = %s" % v for v in sets))
            step = story_chain.STEP[key]
            text = "%s, step %d of %d: %s.\n\n%s" % (label, step[1], total, d["name"], d["tip"].split(" Once per game.")[0])
            out.append(("NOT = {\n\t%s\n}" % done.replace("\n", "\n\t"), text))
    return out


ev(990, "Where Stands the Road?",
   "The chief poet unrolls the long tale of your reign and points to the line where it breaks off.",
   "The road is walked in four acts: Ireland, the Celtic world, Britain and the mainland. Every step on it is shown in purple in your list of decisions. The poet's finger rests on the next one.\n\nThe whole road is walked. The poets have run out of lines, and are looking for a new patron.",
   [
       O("Thank him, and press on.", STRESS_DOWN, PRESTIGE_S, st=S_PATIENT, ai=40),
       O("Pay the poet for his trouble.", GOLD_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 2 }", st=S_GEN, ai=30),
   ], "legend", guarded=False, variants=_tracker_variants())

# ---------------------------------------------------------------------------------------------------------------- 0991 the Druidic revival
ev(991, "The Fires on the Hill",
   "You have lit the quarter-day fire in public, and the oaks on the hill are full of watchers.",
   "The smoke rose straight as a spear. Behind you the poets recited the old genealogies in the voice of men who had not been allowed to for four hundred years. Below, at the edge of the clearing, a dozen monks with tonsures stood very still, not quite praying, not quite leaving.\n\nSomeone has sent for the abbot of the nearest house. He is walking up the hill now, slowly, with a stick and an extremely long face.",
   [
       O("Light the great fire and let every household take a brand home.", PRESTIGE_L, "add_character_modifier = { modifier = eir_hospitality_modifier years = 4 }", "eir_vassal_opinion_effect = { MODIFIER = eir_gael_pride_opinion OPINION = 5 }",
         st=S_ARROG, ai=40, ai_mod=[("arrogant", 15), ("cynical", 15)]),
       O("Meet the abbot on the path and tell him the fires are only fires.", GOLD_S, PIETY_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 4 }",
         st=S_SHREWD, ai=35, ai_mod=[("shrewd", 20)]),
       O("Close the monastery schools for a year to make a point.", "add_dread = medium_dread_gain", LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -5 }",
         st=S_HARD, ai=15, ai_mod=[("wrathful", 15), ("callous", 15)]),
       O("Put out half of the fires, quietly, before dawn.", LOSS_S, STRESS_DOWN, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }",
         st=S_CRAVEN, ai=10, ai_mod=[("craven", 20)]),
   ], "legend", guarded=False)

# ---------------------------------------------------------------------------------------------------------------- 0992 the return to the Church
ev(992, "Ashes in the Porch",
   "You have knelt in the porch of the old church, and the abbot has not decided what to do with you.",
   "He made you wait the length of a psalm. Then he came out with a bowl of ashes and a small, unreadable face, and asked you how many of the fires you had personally lit. You counted. It took a while.\n\nThe monks inside have gone quiet. Outside the poets, who followed you from the court out of curiosity, are writing it all down.",
   [
       O("Give the monastery the lands it asks for.", GOLD_M, PIETY_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }",
         st=S_GEN, ai=40, ai_mod=[("generous", 15), ("zealous", 15)]),
       O("Walk barefoot to the saint's grave and back.", PIETY_L, "add_stress = minor_stress_gain", "increase_wounds_effect = { REASON = fight }",
         st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
       O("Say it was a political decision and leave.", LOSS_M, STRESS_DOWN,
         st=S_CYN, ai=10, ai_mod=[("cynical", 25)]),
   ], "legend", guarded=False)

# ---------------------------------------------------------------------------------------------------------------- 0993 the Culdee Reform
ev(993, "The Poor Houses",
   "The first Culdee houses have opened, and the great abbots have taken it badly.",
   "They are small things: a wattle chapel, a vegetable garden, a well, and six men who call each other Brother and mean it. There is no gold on the altar. There is a very good copy of the Gospels, made by a monk who has had no wine in nine years.\n\nThe abbot of the great house down the valley has sent a long letter on very good vellum. It begins courteously and ends otherwise.",
   [
       O("Answer the abbot with a gift of cattle and a promise to leave his lands alone.", GOLD_M, PIETY_M, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 6 }",
         st=S_GEN, ai=35, ai_mod=[("generous", 15), ("shrewd", 10)]),
       O("Send the best of the Culdee scribes to the abbot's school.", PRESTIGE_M, xp("lifestyle_poet", 25), PIETY_S,
         st=S_HUMBLE, ai=35, ai_mod=[("humble", 15)]),
       O("Ignore the letter and found ten more houses.", GOLD_M, PIETY_L, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -3 }",
         st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
   ], "legend", guarded=False)
