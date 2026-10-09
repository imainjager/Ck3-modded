"""v0.6: ceremony events for the big decisions (vanilla pattern), and risky options for events that had none."""
from evdsl import *

EVENTS = []
PATCH = {}   # event number -> list of Opt to append (applied in gen_events.load_groups)


def ceremony(num, title, summary, body, nick, nick_text, trait=None, church=True, theme="legend", gift="", extra_option=None):
    """A founder's ceremony in the vanilla style: take the nickname, or take more prestige, or share the glory."""
    opts = [
        Opt("Take the name '%s' and let the poets spread it." % nick_text,
            seq("give_nickname = %s" % nick, "add_prestige = 100", gift), ai=40),
        Opt("Refuse the title and take the people's gratitude instead.",
            seq("add_prestige = 300", gift), stress="arrogant = miniscule_stress_impact_loss", ai=30),
        Opt("Share the glory with your vassals at a great feast.",
            seq("eir_vassal_opinion_effect = { MODIFIER = eir_oenach_opinion OPINION = 10 }", "add_prestige = 150", "remove_short_term_gold = minor_gold_value", gift),
            ai=30),
    ]
    if church:
        opts.append(Opt("Give thanks in the church, and let the bishops bless it.",
                        seq("add_piety = 250", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }", gift), ai=25))
    if trait:
        t, chance = trait
        opts.append(Opt("Take the lesson of it to heart.",
                        seq("eir_trait_effect = { TRAIT = %s OPPOSITE = %s CHANCE = %d }" % (t[0], t[1], chance), "add_prestige = 100", "add_stress = -10", gift),
                        ai=15))
    if extra_option:
        opts.append(extra_option)
    EVENTS.append(E(num, title, summary, body, opts, theme=theme,
                    immediate="eir_world_reacts_effect = yes"))


ceremony(210, "The Gathering Departs",
    "The Óenach is over, and the kings are going home with full bellies and full memories.",
    "For a week the hills rang with horns and the fields were thick with tents. Quarrels were judged, marriages arranged, horses raced. The poets are already composing the account, and they ask what the king would like it to say.",
    "nick_eir_convener", "the Convener")
ceremony(211, "The Hall Stands on Tara",
    "The roof-tree is raised, and the Hall of Tara stands on the hill again.",
    "Carpenters from three kingdoms worked on it for years. It is longer than any hall in Ireland, with a bench for every province and a carved door facing the stone of the kings. Nobody has sat under that roof for six hundred years.",
    "nick_eir_tara_builder", "the Builder of Tara", trait=(("just", "arbitrary"), 30))
ceremony(212, "The Charter of the Filí",
    "The schools of the poets now have a charter, and a king has put his seal to it.",
    "The master-poets have walked to your hall in their coloured cloaks, one hue for each grade. They carry the oldest tales in their heads, and the charter means those tales can no longer be silenced by a petty king.",
    "nick_eir_poet_king", "the Poet-King", trait=(("poet", "illiterate"), 0) if False else None, church=False, theme="learning")
ceremony(213, "The Cattle Are Counted",
    "Every herd in the kingdom has been counted, and every cow has an owner.",
    "The bó-aire stand in a circle, each declaring the size of his herd to the judges. It takes three days. At the end, the lords of the cattle know exactly what they owe, and exactly what they are owed.",
    "nick_eir_cow_lord", "the Cow-Lord", trait=(("diligent", "lazy"), 30), church=False, theme="court")
ceremony(214, "The Monastic Cities Rise",
    "Your great abbeys have become what the abbots always said they were: cities.",
    "Under the round towers, monks, students, merchants and pilgrims crowd the lanes. The abbots, who hold more land than most kings, have asked to be received. They bring gifts, and a request for the king's protection.",
    "nick_eir_abbot_king", "the Abbot-King", trait=(("zealous", "cynical"), 30), theme="faith")
ceremony(215, "The Sea Belongs to You",
    "Your ships have taken the last of the Irish Sea, and the old sea-kings are asking what you will do with it.",
    "Dublin, Man, the Isles and the Welsh coast now send their dues. A Norse jarl who once raided your coast has come to your hall as a guest, and he is wondering aloud what a king of the Gael needs with so many ships.",
    "nick_eir_sea_master", "Master of the Western Sea", church=False, theme="war")
ceremony(216, "The Golden Age Begins",
    "Poets, abbots, cattle lords and sea-kings are all at your table, and for the first time they are speaking in the same tongue.",
    "The years of fighting have left Ireland with a new confidence. Books are being copied, crosses carved, ships built, and young men are learning the old tales not as memory but as promise. The poets say the age will be called after you.",
    "nick_eir_gael_father", "Father of the Gael", trait=(("gregarious", "shy"), 35))
ceremony(217, "The Kings Kneel",
    "For the first time in memory, the high kingship will pass from father to son without a war.",
    "The provincial kings stand in a half circle on the Hill of Tara. They have sworn the oath on the relics. The old men look uneasy and the young ones look relieved, because nobody there has ever seen a king's death that did not break the kingdom.",
    "nick_eir_unifier", "the Unifier", trait=(("patient", "wrathful"), 35))
ceremony(218, "The Celtic Congress Sits",
    "Envoys from Wales, Cornwall, Brittany and Alba are seated on benches beside your own.",
    "No one has seen the Celtic peoples around one table since the Romans. They argue about the date of Easter and the proper way to cut hair, and they agree on exactly one thing: the Gael and the Britons are brothers.",
    "nick_eir_celtic_brother", "Brother of the Celtic Peoples", church=False, theme="diplomacy")

# ---------------------------------------------------------------------------
# Risky extra options for events that offered no downside at all (flavor guide, rule 3 and section 8)
# ---------------------------------------------------------------------------
def gamble(text, win_label, win_text, win_fx, lose_label, lose_text, lose_fx, trigger="", stress="", p_win=55, bonus=None):
    mods = [bonus] if bonus else []
    return Opt(text,
               RL((p_win, win_label, win_text, mods, win_fx),
                  (100 - p_win, lose_label, lose_text, [], lose_fx)),
               trigger=trigger, stress=stress, ai=15)


PATCH[22] = [gamble("Chase the broken host into the hills.", "g22w", "You run them to ground", "add_prestige = 150\nadd_gold = minor_gold_value",
                    "g22l", "They turn and ambush your riders", "add_prestige = -50\nincrease_wounds_effect = { REASON = fight }", trigger="prowess >= 8", bonus=(10, "prowess >= 12"))]
PATCH[32] = [gamble("Lead your own herds between the fires.", "g32w", "The herds thrive for a year", "add_character_modifier = { modifier = eir_beltane_vigor_modifier years = 3 }\nadd_prestige = 50",
                    "g32l", "A spark catches the thatch of the barn", "add_prestige = -25\nremove_short_term_gold = minor_gold_value", p_win=60)]
PATCH[34] = [gamble("Follow the wail out into the dark.", "g34w", "You find what the banshee was warning of", "add_prestige = 75\nadd_piety = 50",
                    "g34l", "You come home shaken, and quiet", "add_stress = 20\neir_trait_effect = { TRAIT = paranoid OPPOSITE = trusting CHANCE = 25 }", trigger="brave >= 0" if False else "", p_win=45)]
PATCH[38] = [gamble("Order the bog drained to find more.", "g38w", "A second hoard, deeper still", "add_gold = medium_gold_value\nadd_prestige = 50",
                    "g38l", "The bank collapses on the diggers", "remove_short_term_gold = minor_gold_value\nadd_prestige = -50", p_win=45)]
PATCH[45] = [gamble("Ask the hermit when you will die.", "g45w", "He sees a long and honoured life", "add_stress = -20\nadd_piety = 75",
                    "g45l", "He names a year, and it is close", "add_stress = 25\neir_trait_effect = { TRAIT = depressed_1 OPPOSITE = content CHANCE = 20 }", p_win=50)]
PATCH[50] = [gamble("Raise the puppy in your own chamber.", "g50w", "A hound who will follow you into any hall", "add_character_modifier = { modifier = eir_wolfhound_bond_modifier years = 12 }",
                    "g50l", "It tears your best cloak and bites your hand", "increase_wounds_effect = { REASON = fight }\nadd_prestige = -10", p_win=65)]
PATCH[60] = [gamble("Declare yourself High King here and now.", "g60w", "The kings of the south cheer", "add_prestige = 300\neir_vassal_opinion_effect = { MODIFIER = eir_ard_ri_opinion OPINION = 5 }",
                    "g60l", "The Uí Néill laugh in your face", "add_prestige = -150\nadd_character_modifier = { modifier = eir_satirised_modifier years = 3 }", p_win=40)]
PATCH[72] = [gamble("Send a fleet to Alba to prove your word.", "g72w", "The Gaels of the north are overjoyed", "add_prestige = 200\nadd_character_modifier = { modifier = eir_celtic_brotherhood_modifier years = 6 }",
                    "g72l", "A storm scatters the ships off the Mull", "remove_short_term_gold = medium_gold_value\nadd_prestige = -50", p_win=50)]
PATCH[80] = [gamble("Carry the book through the streets in a procession.", "g80w", "The people weep and pray", "add_piety = 300\nadd_prestige = 100",
                    "g80l", "Rain falls on the vellum", "add_piety = -100\nadd_prestige = -50", p_win=60)]
PATCH[101] = [gamble("Play the Norse and the Irish against each other, as he does.", "g101w", "You come out richer and unhurt", "add_gold = medium_gold_value\nadd_prestige = 75",
                     "g101l", "Both sides learn you are a liar", "add_prestige = -100\neir_vassal_opinion_effect = { MODIFIER = eir_claim_revoked_opinion OPINION = -5 }",
                     trigger="intrigue >= 10", p_win=50, bonus=(10, "intrigue >= 14"))]
PATCH[104] = [gamble("Challenge the upstart to a duel.", "g104w", "You cut him down", "add_prestige = 300",
                     "g104l", "He is better than he looks", "add_prestige = -100\nincrease_wounds_effect = { REASON = duel }", trigger="prowess >= 10", p_win=40, bonus=(15, "prowess >= 14"))]
PATCH[106] = [gamble("Seize the silver the Norse left behind in Dublin.", "g106w", "A fat store of silver and no one to stop you", "add_gold = major_gold_value",
                     "g106l", "The bishops call it sacrilege", "add_piety = -150\nadd_prestige = -50", p_win=50)]
PATCH[122] = [gamble("Make him swear on the relics that he will keep the peace.", "g122w", "He swears, and means it", "add_piety = 100\neir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 4 }",
                     "g122l", "He takes it as an insult and leaves", "add_prestige = -50", p_win=55)]
PATCH[123] = [gamble("Ask for their sons as pledges of loyalty.", "g123w", "The lords hand over their sons without complaint", "add_character_modifier = { modifier = eir_hostages_modifier years = 8 }\nadd_prestige = 75",
                     "g123l", "They walk out of the hall", "add_prestige = -75", p_win=40)]
PATCH[153] = [gamble("Take the little book with you on campaign.", "g153w", "It is read aloud before every battle", "add_piety = 100\nadd_prestige = 50",
                     "g153l", "It is lost in a river crossing", "add_piety = -75\nadd_prestige = -25", p_win=60)]
PATCH[156] = [gamble("Ask for ships as the dowry.", "g156w", "Twelve galleys arrive in spring", "eir_defender_levy_effect = yes\nadd_prestige = 100",
                     "g156l", "He thinks you are greedy and says so", "add_prestige = -75", p_win=50)]
PATCH[167] = [gamble("Wear the torc into battle.", "g167w", "The old gold gleams, and your men follow it", "add_prestige = 200",
                     "g167l", "A blow knocks it off and it is lost in the mud", "add_prestige = -100\nincrease_wounds_effect = { REASON = battle }", trigger="prowess >= 8", p_win=50)]

# nickname choices on the existing ceremonies (vanilla: take the nickname, or take more prestige)
PATCH[110] = [Opt("Take the name 'the Crowned' and let it be sung.", "give_nickname = nick_eir_the_crowned\nadd_prestige = 100", ai=30)]
PATCH[112] = [Opt("Take the name 'Emperor of the Gael' and let it be sung.", "give_nickname = nick_eir_emperor_gael\nadd_prestige = 200", ai=30)]
PATCH[190] = [Opt("Take the name 'the Sea-King' from the merchants' toast.", "give_nickname = nick_eir_sea_king\nadd_prestige = 100", ai=25)]
