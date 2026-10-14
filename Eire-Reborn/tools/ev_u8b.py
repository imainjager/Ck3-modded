"""Update 8 events, part 2: the four court positions (1001-1012), the two faiths (1013-1018), the three phases of the struggle (0997-0999).
Court and faith events are pulse events (fired from eir_court_pulse and eir_faith_pulse); the struggle events are fired by the struggle."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

HOLDER = "court_position:%s_court_position ?= { save_scope_as = eir_holder }"


def pos(key):
    return "employs_court_position = %s_court_position" % key


# ============================================================================== OLLAMH (1001-1003)
ev(1001, "The Ollamh Recites Your Descent",
   "Your ollamh has been rehearsing the line from Míl to you, and tonight he does it in front of everyone.",
   "It takes the better part of an hour. He names forty kings in the right order, four battles in the wrong, and one cow in a position of surprising importance. The hall is quiet. At the end he bows, and the whole room, which had not planned to, applauds.",
   [
       O("Reward him with a gift of cattle.", GOLD_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 6 }", st=S_GEN, ai=40, ai_mod=[("generous", 15)]),
       O("Have the whole line carved on a pillar stone.", GOLD_M, PRESTIGE_L, "add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 8 }", st=S_ARROG, ai=30, ai_mod=[("arrogant", 15)]),
       O("Ask him to cut the cow.", PRESTIGE_S, STRESS_UP, st=S_SHREWD, ai=15),
   ], "legend", gate=pos("eir_ollamh"), immediate=HOLDER % "eir_ollamh")

ev(1002, "A Satire in the Hall",
   "Your ollamh has composed a satire on a vassal, and the vassal is in the room.",
   "It is three verses long and the third is the cruel one. The vassal's face has gone the colour of tallow. The hall waits to see whether the king will allow it to be finished. By custom, a satire left half-recited leaves a blemish on the man it is about; a satire recited to the end leaves a blemish on both.",
   [
       O("Let him finish.", "add_dread = medium_dread_gain", "eir_vassal_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -6 }", PRESTIGE_S, st=S_HARD, ai=20, ai_mod=[("callous", 15), ("sadistic", 15)]),
       O("Stop him after the second verse.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 3 }", st=S_PATIENT, ai=40),
       O("Pay the vassal compensation in cattle and tell the poet to apologise.", GOLD_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_fair_dealing_opinion OPINION = 5 }", st=S_FORGIVE, ai=30, ai_mod=[("just", 15)]),
   ], "court", gate=pos("eir_ollamh"), immediate=HOLDER % "eir_ollamh")

ev(1003, "The Ollamh Asks for a Hall",
   "Your ollamh would like a house of his own, with a library, a school and a good fire.",
   "He has asked politely, which is how you know it matters. His predecessor asked for the same and was given a chamber over the stables. The new ollamh points out, without raising his voice, that the old one is remembered chiefly for the smell.",
   [
       O("Build him a proper hall.", GOLD_M, PRESTIGE_M, xp("lifestyle_poet", 30), "add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 12 }", st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Give him a small house and a promise.", GOLD_S, STRESS_UP, st=S_GREED, ai=30),
       O("Refuse: a poet's hall is the king's hall.", LOSS_S, "add_character_modifier = { modifier = eir_welsh_resentment_modifier years = 4 }", st=S_ARROG, ai=10, ai_mod=[("arrogant", 20)]),
   ], "court", gate=pos("eir_ollamh"), immediate=HOLDER % "eir_ollamh")

# ============================================================================== BREHON (1004-1006)
ev(1004, "The Case of the Three Cows",
   "Two farmers have brought the same three cows before your brehon, and each swears they are his.",
   "The brehon has heard the case for six hours. The cows have been looked at, patted, questioned and in one case sung to. He now turns to you, with the air of a man about to say something sensible and, if possible, unpopular.",
   [
       O("Let him judge by the old tracts.", PRESTIGE_M, "add_character_modifier = { modifier = eir_cain_law_modifier years = 6 }", st=S_HONEST, ai=40, ai_mod=[("just", 15)]),
       O("Have the cows driven between the two farms and see where they go.", PRESTIGE_S, STRESS_DOWN, st=S_SHREWD, ai=30),
       O("Take the cows into your own herd and fine both farmers.", GAIN_S, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -4 }", st=S_GREED, ai=10, ai_mod=[("greedy", 20), ("arbitrary", 15)]),
   ], "court", gate=pos("eir_brehon"), immediate=HOLDER % "eir_brehon")

ev(1005, "A Surety Not Paid",
   "A man who stood surety for a debt has refused to pay it.",
   "The old law is plain: a surety is bound as the debtor is. The surety, however, is your cousin, and the creditor is a man you particularly dislike. The brehon waits, with the slightly bored politeness of a man who has never met a good reason to bend a law.",
   [
       O("Enforce the law on your cousin.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 5 }", st=S_HONEST, ai=40, ai_mod=[("just", 20)]),
       O("Pay the debt yourself and say nothing.", GOLD_M, STRESS_DOWN, st=S_GEN, ai=30, ai_mod=[("generous", 15)]),
       O("Quietly lose the case.", LOSS_M, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -5 }", st=S_DECEIT, ai=10, ai_mod=[("deceitful", 20)]),
   ], "court", gate=pos("eir_brehon"), immediate=HOLDER % "eir_brehon")

ev(1006, "The Law Tracts Copied",
   "Your brehon proposes to have the law tracts copied in a clear hand, so that the lesser judges need not guess.",
   "There are four tracts of any importance and thirty of none. The brehon would copy the first four in a year and the rest in his lifetime. A scribe has been found who writes a clear hand and costs a good deal.",
   [
       O("Fund the work in full.", GOLD_M, PRESTIGE_M, xp("lifestyle_poet", 15), "add_character_modifier = { modifier = eir_cain_law_modifier years = 10 }", st=S_GEN, ai=40),
       O("Fund the four and ignore the thirty.", GOLD_S, PRESTIGE_S, st=S_SHREWD, ai=35),
       O("Say that the law should be remembered, not written.", STRESS_DOWN, LOSS_S, st=S_CYN, ai=10, ai_mod=[("cynical", 20)]),
   ], "court", gate=pos("eir_brehon"), immediate=HOLDER % "eir_brehon")

# ============================================================================== DRUID (1007-1009)
ev(1007, "The Druid Reads the Oak",
   "Your druid has walked into the wood at dawn and come back with a branch and an opinion.",
   "He will not say what he saw. He will say that the oak was uneasy, that the crows were arguing, and that the king should perhaps not cross a certain ford this month. He says it carefully, as though he knows this is the kind of advice a king ignores.",
   [
       O("Take the advice and avoid the ford.", STRESS_DOWN, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }", st=S_PATIENT, ai=40),
       O("Ask for the omen in writing.", PRESTIGE_S, xp("lifestyle_mystic", 20), st=S_SHREWD, ai=30),
       O("Cross the ford at once, to prove him wrong.", PRESTIGE_S, luck("t1007w", "The ford is quiet", "add_prestige = medium_prestige_gain", "t1007l", "The ford takes a horse and a rider", "increase_wounds_effect = { REASON = fight }\nadd_stress = minor_stress_gain", p=55), st=S_BRAVE, ai=15, ai_mod=[("brave", 15), ("arrogant", 10)]),
   ], "legend", gate=pos("eir_druid"), immediate=HOLDER % "eir_druid")

ev(1008, "A Herb for the Heir",
   "Your druid has brewed a draught for the heir's fever and wants you to try it.",
   "It smells of the bog and tastes, he says, of a long time ago. The court physician, if there is one, has been looking at it with some alarm. The child is hot, wide-eyed and very clear on the subject of not wanting to drink it.",
   [
       O("Give it to the child.", luck("t1008w", "The fever breaks by morning", "add_prestige = minor_prestige_gain\nadd_stress = minor_stress_loss", "t1008l", "The child is sicker for a week", "add_stress = medium_stress_gain", p=65, bonus=(15, "learning >= 10"))),
       O("Take a swallow of it yourself first.", "increase_wounds_effect = { REASON = fight }", PRESTIGE_S, st=S_BRAVE, ai=20),
       O("Send for the monks instead.", PIETY_S, STRESS_UP, st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
   ], "court", gate=pos("eir_druid"), immediate=HOLDER % "eir_druid")

ev(1009, "The Mistletoe Cut",
   "At the full moon your druid cuts the mistletoe from the oak, with a gold sickle and an audience.",
   "He is not a young man and the branch is high. A white cloth is spread below to catch it, two white bulls are tethered at the foot, and you are told that the bulls are the important part. The priests of the Church have sent an observer, who is writing very fast.",
   [
       O("Attend and take a sprig.", PRESTIGE_M, xp("lifestyle_mystic", 30), "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", "add_piety = minor_piety_loss", st=S_CYN, ai=30),
       O("Send the bulls to the monastery afterwards.", GOLD_S, PIETY_M, st=S_GEN, ai=30),
       O("Forbid it. The Church is watching.", LOSS_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 4 }", st=S_ZEAL, ai=20, ai_mod=[("zealous", 20)]),
   ], "legend", gate=pos("eir_druid"), immediate=HOLDER % "eir_druid")

# ============================================================================== AITE / FOSTER-FATHER (1010-1012)
ev(1010, "The Foster-Son Comes Home",
   "A boy you sent to your foster-father has come back for the winter, taller, quieter and extremely good at throwing a spear.",
   "He sits at your table and says very little. When he does speak it is in your foster-father's cadences, a touch of the west in the vowels. He will not say what he was taught, but he looks at the other children in the hall as though he is pricing their horses.",
   [
       O("Praise the foster-father in front of the court.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 4 }", "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 5 }", st=S_GEN, ai=40),
       O("Test the boy at the spear.", PRESTIGE_S, xp("lifestyle_blademaster", 15), st=S_BRAVE, ai=30, ai_mod=[("brave", 15)]),
       O("Quietly note that he sounds nothing like you.", STRESS_UP, st=S_SHREWD, ai=15, ai_mod=[("paranoid", 15)]),
   ], "family", gate=pos("eir_foster_father"), immediate=HOLDER % "eir_foster_father")

ev(1011, "The Foster-Brothers Quarrel",
   "Two foster-brothers raised in the same house have drawn on each other in your hall.",
   "One is your son. One is the son of your foster-father. They were raised on the same milk, taught by the same masters and have never been able to agree on anything since. The dispute is over a hawk. The hawk has left.",
   [
       O("Separate them and send both to the foster-father.", GOLD_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }", st=S_PATIENT, ai=40),
       O("Make them swear to a truce on the relics.", PIETY_S, "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 3 }", st=S_ZEAL, ai=30),
       O("Let them fight it out. It is the law of the hawk.", LOSS_S, "increase_wounds_effect = { REASON = fight }", st=S_WRATH, ai=10, ai_mod=[("wrathful", 15)]),
   ], "family", gate=pos("eir_foster_father"), immediate=HOLDER % "eir_foster_father")

ev(1012, "Gifts for the Foster-Father",
   "By custom a king gives his foster-father a gift each year, and this year your foster-father has expressed an opinion.",
   "Last year it was three cows and a bronze pin. He sent the pin back. This year he has been discreet about what he would like, but a chamberlain has overheard the word horse, and the word good, and a name that sounds like a stud in the west.",
   [
       O("Send the horse.", GOLD_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 5 }", st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Send three cows again, with a longer letter.", GOLD_S, STRESS_UP, st=S_GREED, ai=30),
       O("Send nothing; a foster-son owes nothing.", LOSS_M, "add_character_modifier = { modifier = eir_welsh_resentment_modifier years = 5 }", st=S_ARROG, ai=10, ai_mod=[("arrogant", 15)]),
   ], "family", gate=pos("eir_foster_father"), immediate=HOLDER % "eir_foster_father")

# ============================================================================== THE DRUIDIC FAITH (1013-1015)
DRUID = "faith = faith:eir_druidic"
ev(1013, "A Priest of the New Faith Visits the Fire",
   "A priest of the Church has come to your hearth-fire with a gentle smile and a long memory.",
   "He is polite. He says he is not here to argue; he only wishes to see the fire, as a scholar might see a lost script. He asks, in passing, how many of your court go to Mass, and how many of them go because they are afraid of you.",
   [
       O("Invite him to sit and eat.", GOLD_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 4 }", st=S_GEN, ai=40, ai_mod=[("gregarious", 15)]),
       O("Tell him the fire is older than his book.", PRESTIGE_M, "add_dread = minor_dread_gain", "add_piety = minor_piety_loss", st=S_ARROG, ai=25, ai_mod=[("arrogant", 15)]),
       O("Send him away with a gift and a warning.", GOLD_S, "add_dread = minor_dread_gain", st=S_SHREWD, ai=30),
   ], "legend", gate=DRUID)

ev(1014, "The Oak That Was Cut",
   "Someone has felled the great oak at the edge of the sacred grove, in the night, with an axe from the monastery.",
   "The stump is wet and the chips are still warm. The grove-keeper is weeping. The monks deny it and look at their feet. In the morning, two hundred armed men are standing in the clearing, waiting to be told what the king intends.",
   [
       O("Punish the monastery.", "add_dread = medium_dread_gain", "add_character_modifier = { modifier = eir_hard_hand_modifier years = 5 }", "add_character_modifier = { modifier = eir_welsh_resentment_modifier years = 5 }", st=S_HARD, ai=20, ai_mod=[("wrathful", 20), ("vengeful", 15)]),
       O("Plant an acorn at the stump, publicly, with the abbot present.", PRESTIGE_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", st=S_FORGIVE, ai=40, ai_mod=[("forgiving", 15), ("just", 10)]),
       O("Do nothing. Let the people be angry.", "add_stress = medium_stress_gain", "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 2 }", st=S_PATIENT, ai=10),
   ], "war", gate=DRUID)

ev(1015, "The Quarter-Day Fire Spreads",
   "Across your realm, every household has lit its own fire on the quarter-day, and nobody asked.",
   "The beacon at Tara is answered by the one at Uisneach, and that by the ones in the hills beyond, until the whole island has a rim of small fires along every ridge. The bishops sent messengers and then thought better of it. Tonight is not the night for them.",
   [
       O("Ride the circuit by firelight.", PRESTIGE_L, "add_character_modifier = { modifier = eir_royal_circuit_modifier years = 3 }", st=S_BRAVE, ai=40),
       O("Hold a feast on the hill.", GOLD_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 4 }", st=S_GEN, ai=35),
       O("Order a few of the fires put out, to show you are still in charge.", LOSS_S, "add_dread = minor_dread_gain", STRESS_UP, st=S_HARD, ai=10),
   ], "legend", gate=DRUID)

# ============================================================================== THE CULDEE REFORM (1016-1018)
CULDEE = "has_character_modifier = eir_culdee_reform_modifier"
ev(1016, "A Hermit Asks for a Cell",
   "A hermit has walked a hundred miles to ask for a cell on your land, near a spring and out of sight of any road.",
   "He is thin, shoeless and extraordinarily cheerful. He needs, he says, a stone to sleep on and a place to pray. In a year there will be three more hermits, in five years a school, and in twenty a monastery that will be rich enough to quarrel with your tax collector.",
   [
       O("Give him the spring and the field beside it.", GOLD_S, PIETY_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }", st=S_GEN, ai=40, ai_mod=[("zealous", 15)]),
       O("Give him a cell and no field.", PIETY_S, STRESS_DOWN, st=S_PATIENT, ai=30),
       O("Refuse; the spring is wanted for the cattle.", LOSS_S, "add_character_modifier = { modifier = eir_hunting_hounds_modifier years = 3 }", st=S_GREED, ai=10),
   ], "legend", gate=CULDEE)

ev(1017, "The Married Priest",
   "The Culdee priest at your door is married, has six children and is extremely good at his work.",
   "The bishop has written to say that this is irregular. The priest has written to say that it is not irregular in Ireland. The villagers have written nothing, which is the most eloquent response of the three.",
   [
       O("Support the priest and defend the Culdee custom.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_cain_law_modifier years = 5 }", st=S_ZEAL, ai=40, ai_mod=[("zealous", 15)]),
       O("Send the bishop a gift and a long letter of explanation.", GOLD_M, PIETY_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 5 }", st=S_SHREWD, ai=30),
       O("Quietly bar him from the abbey.", LOSS_S, "add_piety = minor_piety_loss", STRESS_UP, st=S_CRAVEN, ai=10),
   ], "legend", gate=CULDEE)

ev(1018, "A Pilgrim From the Continent",
   "A pilgrim from the Continent has arrived at the poor house and refuses to believe that the Church of the Irish is a real Church.",
   "He has seen the great basilicas of Rome and the gilded altars of Aachen. He looks at the wattle chapel, the cold well and the little brown loaf and announces, with the pleasure of a man discovering a rare animal, that it is all rather splendid.",
   [
       O("Show him the manuscripts.", PRESTIGE_M, xp("lifestyle_poet", 20), "add_character_modifier = { modifier = eir_insular_song_modifier years = 4 }", st=S_HUMBLE, ai=40),
       O("Tell him the Culdees have no need of Rome's approval.", PRESTIGE_S, "add_dread = minor_dread_gain", st=S_ARROG, ai=25, ai_mod=[("arrogant", 15)]),
       O("Let him leave with a hoard of silver and no impressions.", GOLD_M, STRESS_DOWN, st=S_GEN, ai=25),
   ], "legend", gate=CULDEE)

# ============================================================================== THE STRUGGLE (0997-0999), fired by the struggle itself
ev(997, "Kin-Strife",
   "The great houses of Ireland are at one another's throats again.",
   "A cattle-raid, an insult at the Óenach, a marriage that did not happen: nobody can say what began it. By the harvest, three kings have called out their men and one has called out his poets, which is worse.\n\nThe old men say it is the way of things. The old men are not the ones whose halls are burning.",
   [
       O("Take a side early and keep it.", "add_dread = minor_dread_gain", PRESTIGE_S, st=S_BRAVE, ai=40),
       O("Stay out of it and watch.", STRESS_DOWN, st=S_PATIENT, ai=30),
       O("Offer to mediate, for a fee.", GAIN_S, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 3 }", st=S_SHREWD, ai=25),
   ], "war", guarded=False)

ev(998, "The Rise of the Overkings",
   "One house after another is reaching for the kingship of Tara, and the smaller kings must choose whom to follow.",
   "The messages arrive at dawn. A king in the north has taken the oath of three provinces. A king in the south has married the daughter of a fourth. The lesser lords wait, as they always do, to see which way the cattle will walk.",
   [
       O("Declare your allegiance to the strongest house.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 4 }", st=S_SHREWD, ai=35),
       O("Put forward your own name at the next Óenach.", PRESTIGE_M, "add_dread = minor_dread_gain", STRESS_UP, st=S_AMBIT, ai=30, ai_mod=[("ambitious", 20)]),
       O("Keep your cattle at home and your spears sharp.", "eir_defender_levy_effect = yes", st=S_BRAVE, ai=30),
   ], "diplomacy", guarded=False)

ev(999, "The Truce of the Saints",
   "The abbots and the poets have brokered a truce, and the kings have sworn to keep it on the relics.",
   "Three days of speeches, four of fasting and a final night in which the bell of Patrick was carried slowly round the hill. When it was over, the kings stood in a ring and shook hands, for the first time since anyone could remember, without a knife in the other.\n\nIt will not last. But it will last a season, and in Ireland a season is a long time.",
   [
       O("Swear it on the relics.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 4 }", st=S_ZEAL, ai=40),
       O("Swear it, and keep your fingers crossed.", PRESTIGE_S, STRESS_UP, st=S_DECEIT, ai=25),
       O("Refuse to swear and hope no one notices.", LOSS_M, "add_dread = minor_dread_gain", st=S_ARROG, ai=10),
   ], "legend", guarded=False)
