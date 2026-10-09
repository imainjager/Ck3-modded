"""v0.7 part A: Re-Celticisation (the culture-change system with its backlash) and the politics of the kindred."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"
BROTH = "has_global_variable = eir_done_brotherhood"

# =============================================================================
# RE-CELTICISATION
#   Decision "Reclaim the Tongue" converts a foreign-culture county in Britain to your culture and fires 0300.
#   Every conversion raises `eir_resent`; once it is high the Saxons mutter (0301), a leader rises (0302),
#   a revolt can follow (0304). Remedy: the Saxon Moot decision, which can leave you better off.
# =============================================================================

# 0300 ceremony (fired by the decision, saved scope: eir_conv_county)
ev(300, "The Old Tongue Returns",
   "A county in Britain that has spoken English for generations is learning Gaelic again, by your word.",
   "The reeve reads your decree in the market square in two languages. The older women understand the first, the children understand the second, and the poets are delighted that anyone cares about either. What happens next, the county will be telling for a hundred years.",
   [
       O("Hold a feast in the new Gaelic county.", PRESTIGE_M, xp("lifestyle_reveler", 20), GOLD_S,
         "eir_vassal_opinion_effect = { MODIFIER = eir_gael_pride_opinion OPINION = 6 }",
         st=S_GEN, ai=40),
       O("Let the poets compose the county's new name and story.", PRESTIGE_S, xp("lifestyle_poet", 25), "eir_legend_title_effect = { TITLE = scope:eir_conv_county }",
         "if = {\n\tlimit = { var:eir_recelt >= 3 NOT = { has_any_nickname = yes } }\n\tgive_nickname = nick_eir_tongue_giver\n}",
         gate=FILI, st=S_HUMBLE, ai=40),
       O("Send priests to say the Mass in the old tongue.", PIETY_M, xp("lifestyle_mystic", 15), "scope:eir_conv_county = { add_county_modifier = { modifier = eir_hedge_schools_modifier years = 8 } }",
         "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
         st=S_ZEAL, ai=30),
       O("Make an example of the old landlords.", "add_dread = minor_dread_gain", PRESTIGE_S, "scope:eir_conv_county = { change_county_control = minor_county_control_gain }",
         "change_variable = { name = eir_resent add = 1 }", "eir_trait_effect = { TRAIT = wrathful OPPOSITE = patient CHANCE = 25 }",
         st=S_HARD, ai=15, ai_mod=[("callous", 15), ("sadistic", 20)]),
       O("Say nothing, and let it settle quietly.", "change_variable = { name = eir_resent add = -1 }", PRESTIGE_S, STRESS_DOWN,
         st=S_PATIENT, ai=25, ai_mod=[("patient", 15)]),
   ],
   "legend", guarded=False,
   variants=[("has_trait = cynical", "Whatever the poets say, the reeve in the square is thinking about taxes. You are thinking about whether anyone will notice that the king has no authority over a word. The county, regardless, is tasting the old tongue again, and finds it has not forgotten the flavour.")])

# 0301 the Saxons mutter
ev(301, "The Saxons Mutter",
   "The people of the Saxon counties have begun to say that you are changing the law, the speech and the Church to please the Gael.",
   "The grumbling is in the alehouses first, then at the church door, then on the lips of the older thanes. A man whose grandfather held the same fields says that he asked for a king, not a schoolmaster. The reeves have started to count heads on market days.",
   [
       O("Grant them a moot under their own oak.", "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_saxon_moot_modifier years = 15 } }",
         "eir_resent_clear_effect = yes", "add_character_modifier = { modifier = eir_two_peoples_modifier years = 10 }", PRESTIGE_S,
         gate="diplomacy >= 8", st=S_FORGIVE, ai=40, ai_mod=[("forgiving", 15), ("just", 10)]),
       O("March a company through the market towns.", "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_hard_hand_modifier years = 6 }",
         "scope:eir_unrest_county = { change_county_control = minor_county_control_gain }", STRESS_UP,
         st=S_HARD, ai=20, ai_mod=[("callous", 15), ("wrathful", 10)]),
       O("Pay the thanes to keep their people quiet.", GOLD_M, "change_variable = { name = eir_resent add = -1 }",
         "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 3 }", PRESTIGE_S,
         st=S_GEN, ai=30),
       O("Take their sons as foster-children in your hall.", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 12 }",
         "change_variable = { name = eir_resent add = -2 }", "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 6 }",
         gate="has_global_variable = eir_done_fosterage", st=S_PATIENT, ai=35),
       O("Tell the doubters they are free to leave.", PRESTIGE_S, "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_cultural_resentment_modifier years = 8 } }",
         "trigger_event = { id = eir.0304 years = 1 }", "change_variable = { name = eir_resent add = 1 }",
         st=S_ARROG, ai=10, ai_mod=[("arrogant", 15)]),
   ],
   "court", gate="has_variable = eir_recelt\nvar:eir_resent >= 2\neir_has_foreign_britain_counties_trigger = yes", cooldown=8,
   immediate="eir_pick_unrest_county_effect = yes",
   variants=[("has_trait = compassionate", "You went out alone to listen, which your steward thought unwise. The people had not stopped being kind, they said. They were only worried that nobody would ever be kind to the next generation, who would have no word in the language their grandmothers taught them, and a lord who would not hear it.")])

# 0302 the thane raises the moot
ev(302, "A Thane Calls the Moot",
   "A grey-bearded thane has summoned the freemen of a county to an open-air moot, and he is not asking your leave.",
   "He stands on the barrow by the old road with a sword across his knees, which is how his ancestors did it. Four hundred men have come. They are not armed, which is a courtesy, and they are not leaving, which is a statement. The thane has sent a boy to ask whether the king will hear them.",
   [
       O("Ride out and sit on the barrow beside him.", PRESTIGE_M, "eir_resent_clear_effect = yes", "add_character_modifier = { modifier = eir_two_peoples_modifier years = 8 }", STRESS_UP,
         gate="OR = {\ndiplomacy >= 10\nhas_trait = brave\n}", st=S_BRAVE, ai=40, ai_mod=[("brave", 15), ("humble", 10)]),
       O("Have the thane seized at night.", "add_dread = medium_dread_gain",
                     luck("t302w", "The moot scatters without a fight", "add_prestige = minor_prestige_gain\nscope:eir_unrest_county = { change_county_control = medium_county_control_gain }",
                          "t302l", "The people close ranks and a guard is killed", "add_prestige = minor_prestige_loss\nscope:eir_unrest_county = { change_county_control = medium_county_control_loss }\nincrease_wounds_effect = { REASON = fight }",
                          p=45, bonus=(15, "intrigue >= 12")),
                     st=S_HARD, ai=15, ai_mod=[("deceitful", 15), ("sadistic", 15)]),
       O("Offer him a seat on your council for the marches.", "add_character_modifier = { modifier = eir_two_peoples_modifier years = 12 }", PRESTIGE_S,
         "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_saxon_moot_modifier years = 20 } }", GOLD_S,
         st=S_FORGIVE, ai=35),
       O("Send the poets to shame him in verse.", PRESTIGE_S, xp("lifestyle_poet", 25), "change_variable = { name = eir_resent add = -1 }",
         "add_character_modifier = { modifier = eir_fili_patron_modifier years = 4 }", gate=FILI, st=S_ARROG, ai=20),
   ],
   "war", gate="has_variable = eir_recelt\nvar:eir_resent >= 3\neir_has_foreign_britain_counties_trigger = yes", cooldown=12,
   immediate="eir_pick_unrest_county_effect = yes")

# 0303 the hedge school (chain beat, years after a conversion)
ev(303, "The Hedge-School Fills",
   "Two years after the old tongue returned to a British county, the hedge-school under the hawthorns has more pupils than the church school.",
   "The masters are poor, and they teach from memory: tales, genealogy, the names of rivers. The children recite them at night to their parents, who begin to correct the words. In the corner, a Saxon boy who came for the free bread has learned three poems.",
   [
       O("Fund the masters properly.", GOLD_S, xp("lifestyle_poet", 15), "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_hedge_schools_modifier years = 10 } }", PRESTIGE_S,
         st=S_GEN, ai=40),
       O("Send your heir to study there for a season.", PRESTIGE_S, "add_character_modifier = { modifier = eir_tongue_restorer_modifier years = 8 }",
         "primary_heir ?= { add_trait_xp = { trait = lifestyle_poet value = 25 } }", STRESS_UP,
         gate="exists = primary_heir", st=S_HUMBLE, ai=35, ai_mod=[("humble", 10)]),
       O("Invite the Saxon children to learn beside the Gaelic ones.", "change_variable = { name = eir_resent add = -1 }",
         "add_character_modifier = { modifier = eir_two_peoples_modifier years = 6 }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_two_peoples_opinion OPINION = 4 }",
         st=S_FORGIVE, ai=30),
       O("Close it: the masters preach sedition.", "add_dread = minor_dread_gain", LOSS_S, "scope:eir_unrest_county = { change_county_control = minor_county_control_loss }",
         "add_character_modifier = { modifier = eir_hard_hand_modifier years = 4 }", st=S_HARD, ai=5),
   ],
   "learning", gate="has_variable = eir_recelt\neir_has_celtic_britain_counties_trigger = yes", guarded=False,
   immediate="random_sub_realm_county = {\n\tlimit = {\n\t\ttitle_province ?= { geographical_region = world_europe_west_britannia }\n\t\thas_county_modifier = eir_hedge_schools_modifier\n\t}\n\tsave_scope_as = eir_unrest_county\n}\nif = {\n\tlimit = { NOT = { exists = scope:eir_unrest_county } }\n\trandom_sub_realm_county = {\n\t\tlimit = {\n\t\t\ttitle_province ?= { geographical_region = world_europe_west_britannia }\n\t\t\tculture ?= { OR = { has_cultural_pillar = heritage_goidelic has_cultural_pillar = heritage_brythonic } }\n\t\t}\n\t\tsave_scope_as = eir_unrest_county\n\t}\n}")

# 0304 the revolt in the marches
ev(304, "Fire in the Marches",
   "A county of foreign-speaking freemen has risen, and the beacons are burning along the border.",
   "It began with a tax-collector found in a ditch. By dawn the thanes had called out their men, by noon the hedge-school was ash, and by evening the border fort was sending to ask what the king wanted done. A boy rides in with soot on his face.",
   [
       O("Ride out with the host and break them in the field.", "eir_defender_levy_effect = yes",
         luck("t304w", "You catch them before they gather", "add_prestige = medium_prestige_gain\nscope:eir_unrest_county = { change_county_control = medium_county_control_gain }\neir_trait_effect = { TRAIT = brave OPPOSITE = craven CHANCE = 25 }",
              "t304l", "They scatter and burn the fort behind you", "add_prestige = minor_prestige_loss\nscope:eir_unrest_county = { add_county_modifier = { modifier = eir_rebel_march_modifier years = 8 } }\nincrease_wounds_effect = { REASON = fight }",
              p=55, bonus=(15, "martial >= 12")),
         gate="", st=S_BRAVE, ai=40, ai_mod=[("brave", 15), ("wrathful", 10)]),
       O("Offer to hear their grievances under a flag of truce.", "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_saxon_moot_modifier years = 12 } }",
         "eir_resent_clear_effect = yes", PRESTIGE_S, "add_character_modifier = { modifier = eir_two_peoples_modifier years = 10 }",
         gate="diplomacy >= 9", st=S_FORGIVE, ai=35),
       O("Burn the villages that rose.", "add_dread = major_dread_gain", "add_character_modifier = { modifier = eir_hard_hand_modifier years = 12 }",
         "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_rebel_march_modifier years = 12 } }", PIETY_S.replace("gain", "loss"),
         "eir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -5 }",
         st=S_HARD, ai=5, ai_mod=[("sadistic", 25), ("callous", 15)]),
       O("Withdraw the garrison and let the county go its own way.", LOSS_M, "scope:eir_unrest_county = { change_county_control = major_county_control_loss }",
         "eir_resent_clear_effect = yes", STRESS_DOWN, st=S_CRAVEN, ai=10, ai_mod=[("craven", 20)]),
   ],
   "war", gate="has_variable = eir_recelt\nvar:eir_resent >= 4\neir_has_foreign_britain_counties_trigger = yes", cooldown=15,
   immediate="eir_pick_unrest_county_effect = yes")

# 0305 a Welsh bard hears of it
ev(305, "A Welsh Bard Hears the News",
   "A bard from Gwynedd has walked across Britain to hear the old tongue spoken in a county that lost it.",
   "He has a harp with eleven strings, which is two more than is customary, and a voice that makes the dogs go quiet. He says the Welsh have been telling a story for four hundred years about a day when the island would speak again, and he would like to be told it is true.",
   [
       O("Seat him at the high table and give him a gift.", GOLD_S, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_poet_gift_opinion OPINION = 4 }",
         xp("lifestyle_poet", 15), st=S_GEN, ai=40),
       O("Ask him to teach the county's children the Welsh songs.", "add_character_modifier = { modifier = eir_tongue_restorer_modifier years = 6 }",
         "add_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 4 }", xp("lifestyle_poet", 20), st=S_HUMBLE, ai=35),
       O("Have him carry a letter to the Welsh princes.", PRESTIGE_S,
                   luck("t305w", "The princes answer with an alliance offer", "add_character_modifier = { modifier = eir_gwynedd_alliance_modifier years = 8 }\nadd_prestige = minor_prestige_gain",
                        "t305l", "The letter is read, mocked, and not answered", "add_prestige = minor_prestige_loss", p=60, bonus=(10, "diplomacy >= 10")),
                   gate=BROTH, st=S_AMBIT, ai=30),
       O("Thank him, but keep your plans to yourself.", STRESS_DOWN, PRESTIGE_S, st=S_SHREWD, ai=15),
   ],
   "diplomacy", gate="has_variable = eir_recelt\neir_has_celtic_britain_counties_trigger = yes", cooldown=12)

# 0306 a mixed marriage
ev(306, "A Thane's Daughter",
   "The oldest Saxon thane in a conquered county has offered his granddaughter as a bride for your heir.",
   "He says it is a fitting match. His own sons died in the old wars, his remaining land is poor, and he would like the child he cannot fight for to be queen of someone he cannot fight. The girl has a plain face, a great deal of land, and a reputation for reading.",
   [
       O("Accept, and marry her to your heir.", "primary_heir ?= { add_opinion = { target = root modifier = eir_two_peoples_opinion opinion = 10 } }", "eir_resent_clear_effect = yes",
         "add_character_modifier = { modifier = eir_two_peoples_modifier years = 15 }", PRESTIGE_M,
         gate="exists = primary_heir", st=S_FORGIVE, ai=40, ai_mod=[("forgiving", 15), ("content", 10)]),
       O("Take her into your household as a ward.", "change_variable = { name = eir_resent add = -1 }", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 8 }",
         PRESTIGE_S, GOLD_S, st=S_KIND, ai=35),
       O("Decline, and insult the thane's lineage.", PRESTIGE_S, "change_variable = { name = eir_resent add = 1 }", LOSS_S,
         "scope:eir_unrest_county = { add_county_modifier = { modifier = eir_cultural_resentment_modifier years = 6 } }",
         st=S_ARROG, ai=10, ai_mod=[("arrogant", 20)]),
   ],
   "family", gate="has_variable = eir_recelt\nvar:eir_resent >= 1\neir_has_foreign_britain_counties_trigger = yes", cooldown=15,
   immediate="eir_pick_unrest_county_effect = yes")
