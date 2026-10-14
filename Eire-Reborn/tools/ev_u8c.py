"""Update 8 events, part 3: an opening and a closing story for each of the six Irish activities (1101-1112).
Fired by the activity itself (on_phase_active and on_end, for the host)."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

# ============================================================================== ÓENACH
ev(1101, "The Field Fills",
   "The first carts have come over the hill, and the Óenach has begun.",
   "By noon there are three thousand people on the field and four hundred tents. The brehons have set up their benches under the oak, the grooms are walking the horses down the race-course, and the traders are shouting the price of salt. Everyone looks to you to say what will happen first.",
   [
       O("Open with the court: let the brehons sit before the games begin.", PRESTIGE_S, "add_character_modifier = { modifier = eir_cain_law_modifier years = 3 }", st=S_HONEST, ai=40),
       O("Open with the horse-race and give the day to the young.", PRESTIGE_M, GOLD_S, st=S_GEN, ai=35),
       O("Open with the cattle fair and take a toll on every beast.", GAIN_M, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -3 }", st=S_GREED, ai=15, ai_mod=[("greedy", 20)]),
   ], "court", guarded=False)

ev(1102, "Counting the Cattle",
   "The Óenach is over, the field is a bog and the accounts are on your table.",
   "The steward reports that the beer ran out on the second night, that three tents were burned and one was married in, that a horse of unknown ownership won the great race and has not been claimed, and that the poets ate the king's portion twice.",
   [
       O("Pay the costs and call it generosity.", GOLD_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }", st=S_GEN, ai=40),
       O("Keep the unclaimed horse for the stud.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hunting_hounds_modifier years = 4 }", st=S_SHREWD, ai=30),
       O("Send the bill to the lords who started the brawl.", GAIN_S, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -4 }", st=S_GREED, ai=15),
   ], "court", guarded=False)

# ============================================================================== FESTIVAL
ev(1103, "Putting Out the Hearths",
   "On the eve of the quarter-day, every hearth in the land is put out, and you must light the first new one.",
   "A cold house is the strangest thing in the world. Even the dogs stand about with their ears down. The old men say that tonight is the night between, when the dead can walk and the living must be careful. In the dark, someone strikes a flint.",
   [
       O("Strike the first spark yourself.", PRESTIGE_M, xp("lifestyle_mystic", 20), st=S_BRAVE, ai=40),
       O("Hand the flint to the oldest woman in the hall.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }", st=S_HUMBLE, ai=35),
       O("Light it from a lamp and tell no one.", STRESS_DOWN, LOSS_S, st=S_CYN, ai=10, ai_mod=[("cynical", 20)]),
   ], "legend", guarded=False)

ev(1104, "Dawn After the Fire",
   "The great fire has burned down to coals, the dancers have gone, and a thin light is coming up behind the hill.",
   "The mead is gone, and so is half the harvest ale. Someone is asleep in the stable with a cow. The oldest priest in the district, who came to disapprove, is asleep against a wall with a smile on his face, and a mug.",
   [
       O("Walk the hill alone and give thanks.", PIETY_M, STRESS_DOWN, st=S_ZEAL, ai=40),
       O("Wake the household and send them home with a brand each.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }", st=S_GEN, ai=35),
       O("Leave quietly before anyone sees what you have been doing.", LOSS_S, STRESS_UP, st=S_SHREWD, ai=10),
   ], "legend", guarded=False)

# ============================================================================== FEIS OF TARA
ev(1105, "The Seating",
   "The kings are in the hall and the poets are looking at you for the order of the seats.",
   "Each king has a place his fathers held, and a hundred years of grievance about it. The hall has been laid out three times and rubbed out twice. The ollamh, who does not make suggestions, makes one with his eyebrows.",
   [
       O("Seat each king where his fathers sat.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 4 }", st=S_HONEST, ai=40),
       O("Seat your friends high and the rest by lot.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_slighted_envoy_opinion OPINION = -5 }", st=S_GREED, ai=20),
       O("Seat nobody and have the feast in the open, on the grass.", PRESTIGE_M, STRESS_UP, "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }", st=S_SHREWD, ai=20),
   ], "court", guarded=False)

ev(1106, "The Kings Depart",
   "The Feis is over, and the kings are riding home.",
   "They go in the order they came, with their poets behind them and their cattle ahead. Each rode in with a grievance and rides out with a promise. Whether the promises hold is a matter for the spring.",
   [
       O("Send each king home with a gift.", GOLD_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 4 }", st=S_GEN, ai=40),
       O("Take a son of each king as a foster-child.", PRESTIGE_S, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_hostages_modifier years = 6 }", st=S_SHREWD, ai=25),
       O("Let them go. The feast was the gift.", STRESS_DOWN, st=S_CONTENT, ai=25),
   ], "diplomacy", guarded=False)

# ============================================================================== PILGRIMAGE
ev(1107, "Barefoot at the Gate",
   "The company has reached the foot of the holy place, and the road ahead goes straight up.",
   "Somebody takes off his shoes. Somebody else is told by a monk that it would be better to keep them on. The stone is wet, the air is thin and above you, a small stone chapel hangs on the rock like a limpet.",
   [
       O("Go on barefoot like the saints.", PIETY_M, "increase_wounds_effect = { REASON = fight }", st=S_ZEAL, ai=40, ai_mod=[("zealous", 20)]),
       O("Keep your shoes and give the money saved to the poor.", GOLD_S, PIETY_S, st=S_GEN, ai=35),
       O("Stop at the gate and send a monk up with your offering.", PIETY_S, STRESS_UP, st=S_CRAVEN, ai=15),
   ], "legend", guarded=False)

ev(1108, "The Road Home",
   "The pilgrimage is over. The way back is the same road, but nobody seems to see it the same.",
   "The company is quieter. Somebody has stopped swearing. Somebody else has promised to marry the girl he met at the hospice and written to his father about it. The hermit's blessing has not worn off, and nobody feels like arguing about anything.",
   [
       O("Found a hospice at the foot of the hill.", GOLD_M, PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }", st=S_ZEAL, ai=40),
       O("Carry a relic stone home for your own chapel.", PIETY_M, PRESTIGE_S, st=S_SHREWD, ai=30),
       O("Walk home and say nothing to anyone of what you saw.", STRESS_DOWN, xp("lifestyle_mystic", 20), st=S_PATIENT, ai=25),
   ], "legend", guarded=False)

# ============================================================================== HOSTING
ev(1109, "The Host Assembles",
   "The lords are in the field with their spears, and the camp stretches from the stream to the wood.",
   "Eleven hundred men and a good many more cattle. The king's captain walks the lines with a face like a closed door. Someone has found a hill to stand on, and it is, for the moment, yours.",
   [
       O("Review the host and give the captains a feast.", GOLD_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_hosting_modifier years = 3 }", st=S_GEN, ai=40),
       O("Name a champion to lead the van, and promise him the best portion.", PRESTIGE_S, xp("lifestyle_blademaster", 15), st=S_BRAVE, ai=35),
       O("March at dawn and tell nobody where.", STRESS_UP, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 2 }", st=S_SHREWD, ai=20),
   ], "war", guarded=False)

ev(1110, "Dividing the Plunder",
   "The host has come home, and there is a pile of cattle, silver and arguments in the middle of the camp.",
   "The law gives the king a third and the captains a third and the rest to the host. The captains, who did the work, have views. The host, which did the dying, has more.",
   [
       O("Follow the law to the letter.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_fair_dealing_opinion OPINION = 4 }", st=S_HONEST, ai=40),
       O("Give the host more than the law says and keep the king's share small.", GOLD_M, PRESTIGE_L, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }", st=S_GEN, ai=30, ai_mod=[("generous", 25)]),
       O("Keep the best cattle for yourself and call it the king's right.", GAIN_M, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -5 }", st=S_GREED, ai=15, ai_mod=[("greedy", 25)]),
   ], "war", guarded=False)

# ============================================================================== BARDIC CONTEST
ev(1111, "The Poets Arrive",
   "The poets have come from all over the island, and they are not on speaking terms.",
   "A famous master from the south has refused to sit beside a young man from the north. A woman from Connacht has told the hall that her poems are better than the rest put together. In the corner, an old man with a harp is tuning, and everyone is quietly afraid of him.",
   [
       O("Seat the old harper at the head.", PRESTIGE_M, "add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 3 }", st=S_HUMBLE, ai=40),
       O("Seat them by the number of verses they know.", PRESTIGE_S, xp("lifestyle_poet", 20), st=S_HONEST, ai=30),
       O("Let them choose their own seats and watch the fight.", PRESTIGE_S, STRESS_UP, "eir_vassal_opinion_effect = { MODIFIER = eir_satire_opinion OPINION = -3 }", st=S_WRATH, ai=15),
   ], "court", guarded=False)

ev(1112, "The Chair Awarded",
   "The contest is done and the king must name the poet who will sit in the chief's chair.",
   "There is one candidate who was good, one who was clever and one who was very good indeed and made an enemy of half the room. The winners of the others' praise are hovering. The harp is still ringing.",
   [
       O("Name the best poet, whatever the room thinks.", PRESTIGE_M, xp("lifestyle_poet", 30), "add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 8 }", st=S_HONEST, ai=40),
       O("Name the clever one: he will be easier to manage.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 2 }", st=S_SHREWD, ai=25),
       O("Name nobody. Let them fight for it at the next contest.", STRESS_UP, LOSS_S, st=S_CRAVEN, ai=10),
   ], "court", guarded=False)

# ============================================================================== THE RAIDING LINE (1113-1114)
ev(1113, "The Young Men Ask for a Táin",
   "Your sons and the sons of your lords have asked for a táin of their own, and they are very polite about it.",
   "They stand in a row with their spears and their best cloaks, and the eldest does the talking. They want a herd, a ford, a story and a poet to tell it. In return they promise not to start a war. They promise it with the faces of young men who plan to start one anyway.",
   [
       O("Bless the raid and send your poet with them.", GOLD_S, PRESTIGE_M, xp("lifestyle_poet", 15), "add_character_modifier = { modifier = eir_hosting_modifier years = 4 }", st=S_BRAVE, ai=40, ai_mod=[("brave", 15)]),
       O("Give them a neighbour to raid, and a limit.", PRESTIGE_S, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }", st=S_SHREWD, ai=30),
       O("Let them go, and pay the damages later.", GOLD_M, STRESS_DOWN, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 3 }", st=S_GEN, ai=25),
   ], "war", guarded=False)

ev(1114, "The Fleet Puts Out",
   "Forty curraghs and a dozen longer ships are leaving the harbour, and the whole town has come to watch.",
   "The captains have drawn lots for the coasts. One is for Wales and another for the Isle of Man. One, a very young man, has announced he is going to Brittany and that he will bring back wine. The old sailors say nothing; they have seen the young captains go out and some of them come back.",
   [
       O("Send the fleet with your blessing and a priest in every ship.", GOLD_M, PIETY_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", st=S_ZEAL, ai=40),
       O("Take command of the greatest ship yourself.", PRESTIGE_L, "increase_wounds_effect = { REASON = fight }", st=S_BRAVE, ai=25, ai_mod=[("brave", 20)]),
       O("Keep half the fleet at home against the Norse.", "eir_defender_levy_effect = yes", LOSS_S, st=S_SHREWD, ai=30),
   ], "war", guarded=False)
