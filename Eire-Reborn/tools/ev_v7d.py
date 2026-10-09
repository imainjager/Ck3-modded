"""v0.7 part D: chain beats fired by the new decisions (ceremonies, follow-ups, artifacts)."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"

# 0307: ceremony for The Britons Return (unique capstone). Fired straight from the decision.
ev(307, "The Britons Return",
   "From the Clyde to the Tamar, the old island is speaking its old languages again, and you stand at the centre of it.",
   "The ceremony is held at a stone circle that predates everyone in it. Envoys have come from Wales, Cornwall, Brittany and Alba, and a very old monk from Iona has walked in barefoot. A boy is asked to read the new proclamation. He reads it in Welsh, then Irish, then Cornish, and nobody in the circle can say which language they were listening to.",
   [
       O("Take the name 'Restorer of Britain' and wear it.", "give_nickname = nick_eir_britain_restorer", PRESTIGE_L, "eir_world_reacts_effect = yes", xp("lifestyle_poet", 25),
         st=S_ARROG, ai=40),
       O("Refuse the title and raise a stone for every people who came.", PRESTIGE_L, "add_character_modifier = { modifier = eir_two_peoples_modifier years = 20 }", PIETY_M,
         "eir_vassal_opinion_effect = { MODIFIER = eir_two_peoples_opinion OPINION = 8 }", st=S_HUMBLE, ai=35),
       O("Hold a feast for every people on the island, Saxons included.", GOLD_M, PRESTIGE_M, "eir_resent_clear_effect = yes", "add_character_modifier = { modifier = eir_two_peoples_modifier years = 15 }",
         xp("lifestyle_reveler", 30), st=S_GEN, ai=30),
       O("Ask the poets to record it for the next thousand years.", PRESTIGE_M, "eir_legend_title_effect = { TITLE = primary_title }", xp("lifestyle_poet", 40), "add_character_modifier = { modifier = eir_fili_patron_modifier years = 10 }",
         gate=FILI, st=S_HUMBLE, ai=35),
   ],
   "legend", guarded=False)

# 0333: the hospice, a year on
ev(333, "The Hospice of Brigid Opens Its Doors",
   "The first winter of the new hospice has passed, and the nuns are asking what the king would like to see done with it.",
   "They have treated three hundred sick, buried forty and delivered eleven children. A herbalist has joined them, bringing a garden of remedies that are partly miracle and partly mint. Several noble families have been quietly sending their old women here to die in comfort.",
   [
       O("Endow a physician's school in the hospice.", GOLD_M, xp("lifestyle_physician", 40), PRESTIGE_S, "random_held_title = {\n\tlimit = { tier = tier_county }\n\tadd_county_modifier = { modifier = eir_hospice_modifier years = 20 }\n}",
         st=S_GEN, ai=40, ai_mod=[("compassionate", 20)]),
       O("Visit the sick yourself, and wash feet on Maundy Thursday.", PIETY_M, xp("lifestyle_mystic", 25), STRESS_DOWN, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }",
         st=S_HUMBLE, ai=35),
       O("Use the hospice to reward loyal servants.", PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 5 }", GOLD_S,
         st=S_SHREWD, ai=30),
       O("Reduce the funding: the realm has other needs.", GAIN_S, LOSS_S, PLOSS_S, st=S_GREED, ai=5),
   ],
   "faith", guarded=False)

# 0334: missionaries come home
ev(334, "The Missionaries Return",
   "The monks you sent across the sea to Alba have come home, and not all of them are the same men.",
   "Two died of a fever. One stayed behind to found a cell on an island in the north. A fourth has returned with a copy of a gospel in an unknown script, a talking raven that nobody else believes in and a Pictish convert who wants to see the king.",
   [
       O("Receive the Pictish convert at court and ask for his tale.", PIETY_M, PRESTIGE_M, "add_character_modifier = { modifier = eir_missionary_glory_modifier years = 10 }", xp("lifestyle_mystic", 20),
         st=S_ZEAL, ai=40),
       O("Pay for a new mission with twice as many monks.", GOLD_M, PIETY_L, "add_character_modifier = { modifier = eir_missionary_glory_modifier years = 15 }",
         st=S_GEN, ai=35),
       O("Have the gospel copied for your scriptorium.", PRESTIGE_S, "add_learning_lifestyle_xp = medium_lifestyle_xp", PIETY_S, "add_character_modifier = { modifier = eir_fili_patron_modifier years = 4 }",
         gate="has_global_variable = eir_unlock_scriptorium", st=S_HUMBLE, ai=30),
       O("Doubt the raven, and say so.", STRESS_DOWN, LOSS_S, st=S_CYN, ai=10),
   ],
   "faith", guarded=False)

# 0336: the poet's chain (artifact)
ev(336, "The High Poet's Chain",
   "The ollamh of your bardic house comes to the hall with a silver chain over his arm and a very serious face.",
   "In the old law the chain of silver was given by the chief poet of the island to a king he judged worthy of his verse. It is old and heavy, with small bells that ring when the wearer walks. He says he has judged. He has not told anyone his verdict, and nobody dares to ask.",
   [
       O("Receive the chain with honour and wear it at every feast.", PRESTIGE_M, "eir_make_artifact_effect = { NAME = eir_poets_chain_name DESC = eir_poets_chain_desc TYPE = necklace VISUALS = necklace MODIFIER = eir_poets_chain_modifier }",
         xp("lifestyle_poet", 25), st=S_HUMBLE, ai=40),
       O("Ask him to explain the judgement first.", PRESTIGE_S, xp("lifestyle_poet", 15), "add_character_modifier = { modifier = eir_fili_patron_modifier years = 5 }",
         st=S_HONEST, ai=35),
       O("Give the chain to your heir.", PRESTIGE_S, "primary_heir ?= { add_opinion = { target = root modifier = eir_hospitality_opinion opinion = 15 } add_trait_xp = { trait = lifestyle_poet value = 40 } }",
         gate="exists = primary_heir", st=S_GEN, ai=25),
       O("Refuse it: a king should earn praise, not wear it.", PIETY_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 5 }",
         st=S_HUMBLE, ai=15, ai_mod=[("humble", 20)]),
   ],
   "learning", guarded=False)

# 0337: the moot horn (artifact)
ev(337, "The Moot Horn Is Blown",
   "A carved horn, taken from the oak at the moot-hill, is brought to your hall.",
   "The thanes brought it in a cloth. It was blown to call the freemen together when your grandfathers' grandfathers were children, and it has been silent since the day you came. They want you to hold it. They want you to know that they know what it means.",
   [
       O("Keep the horn in your hall and blow it at the moot.", PRESTIGE_M, "eir_make_artifact_effect = { NAME = eir_moot_horn_name DESC = eir_moot_horn_desc TYPE = goblet VISUALS = goblet MODIFIER = eir_moot_horn_modifier }",
         "eir_vassal_opinion_effect = { MODIFIER = eir_two_peoples_opinion OPINION = 5 }", st=S_HUMBLE, ai=40),
       O("Hand the horn back to the thanes and swear to keep the peace.", PRESTIGE_S, "eir_resent_clear_effect = yes", "add_character_modifier = { modifier = eir_two_peoples_modifier years = 12 }",
         st=S_FORGIVE, ai=35),
       O("Hang the horn in a church where nobody can blow it.", PIETY_S, LOSS_S,
         "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 3 }", st=S_ZEAL, ai=10),
   ],
   "court", guarded=False)
