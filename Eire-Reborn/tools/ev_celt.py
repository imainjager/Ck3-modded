"""Update 6 (Return of the Celts): ceremonies 0950 (Mystical Celtic Warriors), 0951 (the Mainland), 0952-0956 (claims) and 0957-0961 (restorations)."""
from ev_h import *
import ev_h
from celt_data import REGIONS
EVENTS = ev_h.EVENTS = []


def ceremony(num, title, summary, body, options, theme="legend", gate=""):
    ev(num, title, summary, body, options, theme, guarded=False, gate=gate)


ceremony(950, "The Groves Are Planted Again",
         "The druids' oak-groves have been replanted across the island, and the Forest Warriors have come out of them.",
         "The first grove was planted by accident. A bard asked where the old gods had been worshipped, and a farmer pointed to a clearing. By midsummer there were forty. Men who have not worn paint since the Romans left are standing between the oaks with torcs on their necks and spears in their hands. They do not speak much. They do not need to.\n\nThe bishops are asking, politely, what you intend.",
         [
             O("Lead the first Beltane in the grove yourself.", PRESTIGE_L, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 8 }", PLOSS_S, "eir_trait_effect = { TRAIT = cynical OPPOSITE = zealous CHANCE = 25 }",
               st=S_CYN, ai=30, ai_mod=[("cynical", 20)]),
             O("Let the monks bless every grove and call it a hermitage.", PIETY_L, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 8 }", GOLD_S,
               gate="piety >= 100", st=S_ZEAL, ai=35, ai_mod=[("zealous", 20)]),
             O("Give the warriors lands and a charter, and keep them away from the priests.", GOLD_M, PRESTIGE_M, "eir_defender_levy_effect = yes", "add_dread = minor_dread_gain",
               st=S_BRAVE, ai=40, ai_mod=[("brave", 15)]),
             O("Say it is a hunting festival and say nothing more.", PRESTIGE_S, STRESS_DOWN, LOSS_S,
               st=S_SHREWD, ai=20, ai_mod=[("shrewd", 20)]),
         ], theme="legend", gate="has_global_variable = eir_done_mystic_celts")

ceremony(951, "The Heralds Cross the Water",
         "Your heralds have gone to the mainland to find the descendants of the old tribes.",
         "They took a ship, a harper and a list of names. The tribes' names are Latin: Aedui, Arverni, Boii, Galatae, Celtiberi. The heralds do not know how to pronounce them, and the people they find do not recognise them. A Gaulish monk is delighted. A Frankish count is not. A Bavarian peasant offers them cheese.\n\nIt is a start.",
         [
             O("Send gifts to every court that remembers a Celtic ancestor.", GOLD_M, PRESTIGE_M, "add_character_modifier = { modifier = eir_hospitality_modifier years = 6 }", "eir_world_reacts_effect = yes",
               st=S_GEN, ai=35, ai_mod=[("generous", 20)]),
             O("Send soldiers with the heralds, to be on the safe side.", "add_dread = medium_dread_gain", LOSS_S, "eir_defender_levy_effect = yes",
               st=S_BRAVE, ai=30, ai_mod=[("brave", 15)]),
             O("Have the poets compose a catalogue of the tribes.", PRESTIGE_M, xp("lifestyle_poet", 40), "add_character_modifier = { modifier = eir_insular_song_modifier years = 10 }",
               gate="has_global_variable = eir_done_fili", st=S_HUMBLE, ai=35),
             O("Call the heralds home. It was a silly idea.", LOSS_M, STRESS_DOWN,
               st=S_CONTENT, ai=10, ai_mod=[("content", 25)]),
         ], theme="diplomacy", gate="has_global_variable = eir_done_celts_mainland")

LINES = {
    "france": ("A druid's hill-fort in the Auvergne has sent a message: the Arverni have not forgotten Vercingetorix.",
               "The message is in Latin, in the handwriting of a monk who pretends to be a Gaul. It names a hill, a river and a vow. The count of the next county over has already sent a letter of his own, and it is considerably less friendly.",
               ["Pay the Auvergne chiefs to rise at the appointed hour.", "Send an envoy to the Breton Celts of the western tip.", "Raise the Gaulish claim in front of the Pope."]),
    "germany": ("In the Bavarian forest the old hill-forts have been unlocked.",
                "They were never really locked. The forest simply grew round them. A Bohemian woodcutter has brought word that the Boii tombs are intact. A German duke has noticed the same woodcutter and is making enquiries.",
                ["Ride into the Hercynian Forest with a small, loud escort.", "Offer the Bavarian highlanders a grove of their own.", "Send a gift to the Archbishop of Salzburg."]),
    "spain": ("A shepherd on the Meseta swears that the first Gaels left from a harbour in Galicia.",
              "He can name the harbour, the ship and the sons of Míl, and the monks of Compostela corroborate everything but the ship. The Irish annals say it too. For once the poets and the monks agree.",
              ["Send a pilgrimage to Santiago in the colours of Ireland.", "Claim kinship with the Celtiberian lords on the plateau.", "Pay the Galician fishermen to carry the message."]),
    "italy": ("In Milan an old man has found a stone with a name on it that sounds distinctly Irish.",
              "It is Insubrian, which is Celtic, which is close enough. The lords of Lombardy are annoyed, the cathedral chapter is intrigued and a Venetian merchant is selling copies. Nobody has asked what the stone says.",
              ["Buy the stone and put it in the Hall of Tara.", "Invite the Lombard nobility to a feast of the old Gaulish dishes.", "Remind the Pope who sacked Rome, once."]),
    "galatia": ("A priest in Ancyra writes that the Galatians still keep three words of the old tongue.",
                "One means river, one means oak, and one has been forgotten by everyone but a Greek grandmother. The Byzantine governor is nervous. Saint Paul, as always, is cited by both sides.",
                ["Send a delegation of monks with a Gaelic gospel book.", "Pay the Galatian hill-lords to hold their passes.", "Offer the Emperor a treaty and mean none of it."]),
}
for i, k in enumerate(["france", "germany", "spain", "italy", "galatia"]):
    r = REGIONS[k]
    summ, body, opts = LINES[k]
    ceremony(952 + i, "The Return of the Celts to %s" % r["name"], summ,
             body + "\n\nYour claim on %s has been spoken aloud. The country is listening." % r["area_name"],
             [
                 O(opts[0], GOLD_M, PRESTIGE_M, "add_dread = minor_dread_gain", st=S_GEN, ai=35, ai_mod=[("generous", 15)]),
                 O(opts[1], PRESTIGE_M, "add_character_modifier = { modifier = eir_welsh_ties_modifier years = 10 }", xp("lifestyle_poet", 20), st=S_HONEST, ai=35, ai_mod=[("honest", 15)]),
                 O(opts[2], PIETY_M, LOSS_S, "eir_world_reacts_effect = yes", st=S_ZEAL, ai=30, ai_mod=[("zealous", 15)]),
                 O("Wait. The claim will keep.", STRESS_DOWN, LOSS_S, st=S_PATIENT, ai=15, ai_mod=[("patient", 20)]),
             ], theme="war", gate="has_global_variable = eir_done_return_%s" % k)
    ceremony(957 + i, "The Celts Return to %s" % r["name"],
             "Half of the counties of %s now speak the tongue of the Gael." % r["area_name"],
             "It happened one village at a time. A priest preached in the old language, a mayor stopped answering in the new, a child wrote its name in ogham on a barn. By harvest the officials had stopped asking which language the taxes were collected in. Half the counties of %s answer to you now, and in the other half the oaks are leafing.\n\n%s" % (r["area_name"], r["story"]),
             [
                 O("Hold a feast in the largest of the converted counties.", GOLD_M, PRESTIGE_L, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }", xp("lifestyle_reveler", 30),
                   st=S_GEN, ai=35, ai_mod=[("generous", 20)]),
                 O("Plant a nemeton in every county you have converted.", GOLD_M, PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }",
                   st=S_ZEAL, ai=30, ai_mod=[("zealous", 15)]),
                 O("March the Forest Warriors through the streets of the old capital.", "add_dread = major_dread_gain", PRESTIGE_M, "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_hard_hand_modifier years = 8 }",
                   st=S_HARD, ai=30, ai_mod=[("sadistic", 15), ("wrathful", 10)]),
                 O("Let the old officials stay, and say nothing about language.", PRESTIGE_S, STRESS_DOWN, LOSS_S,
                   st=S_CONTENT, ai=20, ai_mod=[("content", 20)]),
             ], theme="legend", gate="has_global_variable = eir_done_celt_%s" % k)
