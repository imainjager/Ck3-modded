"""Update 9 events: 26 raid events that happen only to Gaelic and Brythonic characters (the base game has 13 in raid_events.txt).
 1201-1211 the raider, when a raid action ends        1212-1219 the lord who was raided
 1220-1223 the raider, when the loot comes home       1224-1225 a raid army is beaten (raider, defender)
 1226      a revenge vow is remembered
Saved scopes (from the relay events in eir_ev_raid_relay.txt): scope:eir_raider, scope:eir_victim (may be missing), scope:eir_county, scope:eir_barony.
Raiding costs the land development: from -1 up to -5 (the settle event)."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []


def LOOT(tier, dev):
    """loot goes to the raid army (the base game's add_loot) and is delivered when the raiders come home; more devastation, more loot"""
    return "scope:eir_raid_army ?= { add_loot = eir_raid_loot_%s%d }" % (tier, dev)


def DEV(n):
    return "scope:eir_county ?= { change_development_level = -%d }" % n


# the victim notices, and can swear revenge (the Avenge the Raid and Blood-Price casus belli need this variable)
GRUDGE = ("scope:eir_victim ?= {\n\tadd_opinion = { target = scope:eir_raider modifier = eir_raid_grudge_opinion opinion = -40 }\n"
          "\tset_variable = { name = eir_revenge_target value = scope:eir_raider years = 15 }\n}")
LIGHT_GRUDGE = "scope:eir_victim ?= { add_opinion = { target = scope:eir_raider modifier = eir_raid_grudge_opinion opinion = -20 } }"
VOW = "set_variable = { name = eir_revenge_target value = scope:eir_raider years = 15 }\nadd_character_modifier = { modifier = eir_revenge_vow_modifier years = 10 }"
FAME = "add_character_modifier = { modifier = eir_raider_glory_modifier years = 5 }"
HOOK = "if = {\n\tlimit = { exists = scope:eir_victim }\n\tadd_hook = { target = scope:eir_victim type = favor_hook }\n}"

# ============================================================================================== THE RAIDER (1201-1211)
ev(1201, "The Herds of the Border",
   "The raid has gathered more cattle than your men can drive, and the borderers are watching from the ridge.",
   "They are good cattle: red-flecked, long-horned, fed on the lush grass of the river meadows. Your men have been gathering them since dawn and are now arguing about which of them to eat. The lord of the land has not answered the smoke, and nobody can say whether that is cowardice or patience.",
   [
       O("Drive every beast home.", LOOT("m", 1), PRESTIGE_S, DEV(1), FAME, LIGHT_GRUDGE, st=S_GREED, ai=40, ai_mod=[("greedy", 15)]),
       O("Slaughter half of them and feast on the spot.", LOOT("s", 2), xp("lifestyle_reveler", 15), STRESS_DOWN, DEV(2), LIGHT_GRUDGE, st=S_GEN, ai=30),
       O("Leave a tithe of the herd at the church door.", PIETY_M, LOOT("s", 1), DEV(1), st=S_ZEAL, ai=30, ai_mod=[("zealous", 15)]),
   ], "war", guarded=False)

ev(1202, "Burn the Fields",
   "The standing grain in the valley is ripe, and your captains are looking at it the way a smith looks at iron.",
   "A match, a wind from the south and an hour's patience would take a year of the valley's bread. Some of your men think it is good policy. Others have farms of their own.",
   [
       O("Burn everything that will burn.", DEV(3), LOOT("m", 3), "scope:eir_county ?= { add_county_modifier = { modifier = eir_scorched_county_modifier years = 10 } }", "add_dread = major_dread_gain", PRESTIGE_S, GRUDGE,
         st=S_HARD, ai=15, ai_mod=[("sadistic", 25), ("wrathful", 15)]),
       O("Burn the barns and spare the fields.", DEV(2), LOOT("s", 2), "add_dread = minor_dread_gain", LIGHT_GRUDGE, st=S_SHREWD, ai=35),
       O("Spare the harvest and carry it home.", LOOT("m", 1), DEV(1), st=S_GREED, ai=30),
   ], "war", guarded=False)

ev(1203, "The Satire",
   "Your poet has composed a satire on the lord of the burned land, and he is asking whether he may sing it.",
   "It is four verses, and the third rhymes the lord's name with something the lord's mother would not have liked. A Gaelic satire is a serious weapon: it can raise blisters on a man's face and take the shine off a name. The poet is looking at you with the fixed expression of an artist who knows he has done well.",
   [
       O("Let him sing it at every fire between here and home.", PRESTIGE_M, "add_dread = minor_dread_gain", LIGHT_GRUDGE, xp("lifestyle_poet", 15), st=S_ARROG, ai=40, ai_mod=[("arrogant", 15), ("callous", 10)]),
       O("Have it sung in the lord's own hall, by the lord's own poet.", PRESTIGE_L, GRUDGE, "scope:eir_victim ?= { add_character_modifier = { modifier = eir_raid_lament_modifier years = 4 } }", st=S_HARD, ai=15, ai_mod=[("vengeful", 20)]),
       O("Pay the poet to keep it to himself.", GOLD_S, STRESS_DOWN, st=S_GEN, ai=30, ai_mod=[("just", 10)]),
   ], "court", guarded=False)

ev(1204, "Hostages at the Ford",
   "Your raiders have taken a few of the lord's kin at the ford, and they are sitting in a row with their hands tied.",
   "There is a girl of about twelve who has not stopped glaring at you. There is a boy of about six who has not stopped crying. There is an old nurse who has not stopped talking. The raiders are, it seems, as unsettled as the hostages.",
   [
       O("Take the lord's youngest son as a foster-child and a hostage.", PRESTIGE_S, HOOK, GRUDGE, "add_character_modifier = { modifier = eir_hostages_modifier years = 8 }", st=S_HARD, ai=30, ai_mod=[("callous", 15)]),
       O("Take cattle in place of the hostages.", LOOT("m", 1), DEV(1), LIGHT_GRUDGE, st=S_GREED, ai=30),
       O("Free them and send them home with a gift.", GOLD_S, PIETY_M, PRESTIGE_S, "scope:eir_victim ?= { add_opinion = { target = scope:eir_raider modifier = eir_blood_price_paid_opinion opinion = 25 } }", st=S_KIND, ai=25, ai_mod=[("compassionate", 25)]),
   ], "war", guarded=False)

ev(1205, "Settle the Raided Land",
   "The raid has done more than anyone expected, and your captains are suggesting that the land might as well be yours.",
   "The lord's levy has gone. The hall stands empty. The fields are fat and the villagers are, on the evidence, willing to be told what language they speak. A priest from your court points out, with a certain diffidence, that there is a church in the next valley that might be put to good use.\n\nThe raid could simply end here. Or it could become something else entirely.",
   [
       O("Settle your own people here. The land is yours now.",
         "scope:eir_county ?= {\n\tchange_development_level = -5\n\tset_county_culture = scope:eir_raider.culture\n\tset_county_faith = scope:eir_raider.faith\n\tadd_county_modifier = { modifier = eir_raider_settlement_modifier years = 25 }\n}",
         "add_pressed_claim = scope:eir_county", LOOT("m", 5), PRESTIGE_L, "add_dread = medium_dread_gain", FAME, GRUDGE, "add_piety = minor_piety_loss",
         st=S_ARROG, ai=20, ai_mod=[("ambitious", 25), ("callous", 10)]),
       O("Burn it to the ground and leave it empty.", DEV(5), LOOT("m", 5), "scope:eir_county ?= { add_county_modifier = { modifier = eir_scorched_county_modifier years = 15 } }", "add_dread = major_dread_gain", GRUDGE,
         st=S_HARD, ai=15, ai_mod=[("sadistic", 25), ("wrathful", 15)]),
       O("Take the county's tribute for a year and go home.", LOOT("m", 1), DEV(1), LIGHT_GRUDGE, st=S_GREED, ai=40, ai_mod=[("greedy", 20)]),
       O("Withdraw. A raid is a raid.", STRESS_DOWN, st=S_PATIENT, ai=20),
   ], "war", guarded=False)

ev(1206, "The Church Is Burning",
   "The raiders have broken into the church, and the monks are standing in front of the altar with their arms folded.",
   "There is silver on the altar, a gospel book in a shrine and a very large abbot. The abbot is pointing out, in a clear voice, that the saint buried here was a king's son and a friend of Columba. A young raider is considering the silver with great attention.",
   [
       O("Strip the altar and burn the roof.", LOOT("m", 2), DEV(2), "add_dread = medium_dread_gain", "add_piety = major_piety_loss", GRUDGE, st=S_HARD, ai=10, ai_mod=[("sadistic", 20), ("cynical", 20)]),
       O("Take the silver only and leave the saint alone.", LOOT("s", 1), "add_piety = minor_piety_loss", DEV(1), LIGHT_GRUDGE, st=S_GREED, ai=30),
       O("Leave the church untouched and ask the abbot for a blessing.", PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }", st=S_ZEAL, ai=30, ai_mod=[("zealous", 25)]),
   ], "legend", guarded=False)

ev(1207, "The Slave Train",
   "Your men are bringing a line of captives down the road, tied at the neck, and they are expecting you to say what happens next.",
   "There are two hundred of them: farmhands, a few craftsmen, a priest and a very angry woman who is the village's brewer. The slave-traders from Dublin and Bristol are already hovering at the edge of the camp.",
   [
       O("Sell them to the merchants.", LOOT("m", 2), DEV(2), "add_piety = minor_piety_loss", LIGHT_GRUDGE, st=S_GREED, ai=30, ai_mod=[("greedy", 20), ("callous", 15)]),
       O("Settle them as workers on your own land.", PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_island_pride_modifier years = 6 } }", DEV(2), GRUDGE, st=S_SHREWD, ai=25),
       O("Free the priest and the monks and ransom the rest.", LOOT("s", 1), PIETY_M, DEV(1), st=S_KIND, ai=25, ai_mod=[("compassionate", 20)]),
   ], "war", guarded=False)

ev(1208, "The Ogham of the Raid",
   "Your poet suggests that the raid deserves a stone: the names of the fallen, and of the land that has been taken.",
   "In Ireland and Wales a pillar stone is a legal document. An ogham stone that names a boundary names a claim, and a claim that is cut in stone is very hard to argue with. The stone-cutter, who has been standing very patiently with his chisel, says it will take three days.",
   [
       O("Cut your name and the name of the land on the stone.", PRESTIGE_M, "add_pressed_claim = scope:eir_county", DEV(1), GRUDGE, st=S_ARROG, ai=35, ai_mod=[("ambitious", 15)]),
       O("Cut only the names of the fallen.", PRESTIGE_S, PIETY_S, st=S_HUMBLE, ai=35),
       O("Leave no stone: a raid is not a boundary.", STRESS_DOWN, st=S_PATIENT, ai=20),
   ], "legend", guarded=False)

ev(1209, "The Champion at the Ford",
   "The lord's champion has come down to the ford alone and is calling you out by name.",
   "He is large, he is unarmoured and he is whistling. Your men have gone quiet. By old custom, a champion who calls a king out at a ford cannot be refused without shame, and cannot be refused with honour either.",
   [
       O("Fight him at the ford.", luck("t1209w", "You strike him down and the ford is yours", "add_prestige = major_prestige_gain\nadd_trait_xp = { trait = lifestyle_blademaster value = 40 }", "t1209l", "He nearly kills you before your men intervene", "increase_wounds_effect = { REASON = fight }\nadd_prestige = medium_prestige_loss", p=55, bonus=(25, "prowess >= 14")), st=S_BRAVE, ai=40, ai_mod=[("brave", 20)]),
       O("Offer to settle it by wrestling.", PRESTIGE_S, STRESS_UP, st=S_SHREWD, ai=30),
       O("Order the archers to shoot him.", LOSS_M, "add_dread = minor_dread_gain", st=S_CRAVEN, ai=10, ai_mod=[("craven", 20)]),
   ], "war", guarded=False)

ev(1210, "Poets at the Fire",
   "That night, in the camp, the poets want their share of the spoils, and a say in the story.",
   "They have been with the host since the river. They have seen the cattle driven, the barns burned and the champion fall. A good poet will make a raid into a saga; a poor one, or a hurt one, will make it into a joke.",
   [
       O("Give each poet a share of the spoils.", GOLD_M, PRESTIGE_L, xp("lifestyle_poet", 20), "add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 5 }", st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Give them a feast and a few cows.", GOLD_S, PRESTIGE_M, st=S_SHREWD, ai=30),
       O("Give them nothing: poets are paid in praise.", LOSS_S, "add_character_modifier = { modifier = eir_raid_lament_modifier years = 3 }", st=S_GREED, ai=10, ai_mod=[("greedy", 15)]),
   ], "court", guarded=False)

ev(1211, "The Captain Wants More",
   "One of your captains has come to your tent in the evening and, politely, has asked about his share.",
   "He led the van and took the ford. He lost his brother in the first charge. He does not raise his voice, which is how you know he has thought about this on the walk across the camp.",
   [
       O("Give him a double share and the best of the herd.", GOLD_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 5 }", st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
       O("Give him the share the law allows.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_fair_dealing_opinion OPINION = 2 }", st=S_HONEST, ai=35),
       O("Tell him his brother's blood was part of the bargain.", LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -6 }", st=S_HARD, ai=10, ai_mod=[("callous", 20)]),
   ], "war", guarded=False)

# ============================================================================================== THE LORD WHO WAS RAIDED (1212-1219)
ev(1212, "Smoke on the Border",
   "Smoke is rising from your border county, and the horn has been sounded on the hill.",
   "The shepherd who brought the news is out of breath and has lost a boot. The raiders came at dawn, took the herds, burned the barns and left. They did not come for land; they came to say they could. Your steward is looking at the ground and your captain is looking at you.",
   [
       O("Swear on the relics to avenge it.", VOW, PRESTIGE_S, st=S_WRATH, ai=40, ai_mod=[("vengeful", 25), ("wrathful", 15)]),
       O("Call out the levy and ride to the ford.", "eir_defender_levy_effect = yes", PRESTIGE_S, STRESS_UP, st=S_BRAVE, ai=35),
       O("Pay the raiders to go home.", GOLD_M, LOSS_S, st=S_CRAVEN, ai=10, ai_mod=[("craven", 25)]),
       O("Send a poet to the raider's court with a message.", "scope:eir_raider ?= { add_character_modifier = { modifier = eir_raid_lament_modifier years = 3 } }", PRESTIGE_S, st=S_SHREWD, ai=25),
   ], "war", gate="exists = scope:eir_raider", guarded=False)

ev(1213, "A Burned Hall",
   "The hall at the border has been burned to the ground, and the lord of the hall has come to you with ash on his cloak.",
   "He does not ask for justice. He asks for roofs. He has a wife, six children and sixty tenants, and the first frost is five weeks away. The Brehon who has come with him is pointing out that the old law provides for such a case, and that the price is called the blood-price.",
   [
       O("Rebuild the hall and the farms at your own cost.", GOLD_M, PRESTIGE_S, "scope:eir_county ?= { change_development_level = 1 }", "eir_vassal_opinion_effect = { MODIFIER = eir_trusts_justice_opinion OPINION = 4 }", st=S_GEN, ai=40, ai_mod=[("generous", 15), ("just", 10)]),
       O("Demand the blood-price from the raider by right.", VOW, "add_prestige = minor_prestige_gain", st=S_WRATH, ai=30, ai_mod=[("vengeful", 20)]),
       O("Tell him to rebuild it himself.", LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -5 }", st=S_GREED, ai=10, ai_mod=[("greedy", 20)]),
   ], "court", gate="exists = scope:eir_raider", guarded=False)

ev(1214, "The Lament",
   "Your poet has composed a lament for the burned land, and every hall on the island is going to hear it.",
   "It is not a satire: it names no names. It describes the smoke, the herds, the widows and the boy who stood at the gate. It is beautiful. By the end of the third verse the whole hall is silent and your steward has, unprofessionally, wiped his eyes.",
   [
       O("Send it round the courts of Ireland.", PRESTIGE_M, "scope:eir_raider ?= { add_character_modifier = { modifier = eir_raid_lament_modifier years = 5 } }", "add_piety = minor_piety_gain", st=S_SHREWD, ai=40),
       O("Keep it for your own hall.", STRESS_DOWN, PRESTIGE_S, st=S_HUMBLE, ai=30),
       O("Have the poet add a curse on the raider's line.", "scope:eir_raider ?= { add_character_modifier = { modifier = eir_raid_lament_modifier years = 8 } }", "add_piety = minor_piety_loss", STRESS_UP, st=S_WRATH, ai=15, ai_mod=[("vengeful", 25)]),
   ], "court", gate="exists = scope:eir_raider", guarded=False)

ev(1215, "The Stolen Herds",
   "Your men have found the trail of the stolen cattle: a broad churned track through the heather, leading west.",
   "It will be at least two days' ride. The raiders will drive the herd slowly, since cattle are not fast, and they will stop to rest at the river. A small, quick force might catch them. A larger one will not be quick.",
   [
       O("Send the best riders and hurry.", luck("t1215w", "The riders catch the raiders at the river and take the herds back", "add_gold = medium_gold_value\nadd_prestige = medium_prestige_gain", "t1215l", "The riders are caught in an ambush at the river", "add_prestige = medium_prestige_loss\nincrease_wounds_effect = { REASON = fight }", p=55, bonus=(15, "martial >= 12")), st=S_BRAVE, ai=40),
       O("Send a heavy force and take the long road.", GOLD_S, PRESTIGE_S, "eir_defender_levy_effect = yes", st=S_PATIENT, ai=30),
       O("Let the herds go and rebuild your stock.", GOLD_M, STRESS_UP, st=S_CRAVEN, ai=10),
   ], "war", gate="exists = scope:eir_raider", guarded=False)

ev(1216, "The Captive Kin",
   "Some of your relatives were taken in the raid, and the raiders' herald is waiting at the gate with a price.",
   "He is courteous in the way of men who are about to be rude. He says the captives are well and have been fed. He says the price is thirty cows, a bronze cauldron and a pledge that you will not pursue. He has, he notes, a very long way to go home.",
   [
       O("Pay the ransom in full.", GOLD_M, STRESS_DOWN, "scope:eir_raider ?= { add_gold = minor_gold_value }", st=S_GEN, ai=35, ai_mod=[("generous", 15)]),
       O("Refuse, and ride to rescue them.", luck("t1216w", "The rescue succeeds", "add_prestige = major_prestige_gain\nadd_dread = minor_dread_gain", "t1216l", "The rescue fails and the captives are moved", "add_prestige = medium_prestige_loss\nadd_stress = medium_stress_gain", p=50, bonus=(20, "martial >= 14")), VOW, st=S_BRAVE, ai=30),
       O("Abandon them: some debts are not worth paying.", LOSS_M, STRESS_UP, st=S_CRAVEN, ai=5, ai_mod=[("callous", 20)]),
   ], "family", gate="exists = scope:eir_raider", guarded=False)

ev(1217, "The Raider Offers Terms",
   "A herald from the raider has arrived with an offer: a share of the plunder, in exchange for peace.",
   "It is a good offer, as such offers go: a third of the herd, an apology in the old form, a vow not to return for seven years. The only thing that seems to be missing is any sign of remorse.",
   [
       O("Accept the terms and the cattle.", GAIN_M, LOSS_S, "scope:eir_raider ?= { add_opinion = { target = root modifier = eir_blood_price_paid_opinion opinion = 15 } }", st=S_PATIENT, ai=35),
       O("Refuse the offer in front of the whole court.", PRESTIGE_M, VOW, st=S_WRATH, ai=30, ai_mod=[("vengeful", 20)]),
       O("Demand the full blood-price or nothing.", PRESTIGE_S, STRESS_UP, "set_variable = { name = eir_revenge_target value = scope:eir_raider years = 10 }", st=S_ARROG, ai=30),
   ], "diplomacy", gate="exists = scope:eir_raider", guarded=False)

ev(1218, "A Meeting at the Ford",
   "The raider has sent word that he is willing to meet you at the ford, alone, at dawn.",
   "A ford is neutral ground in Ireland and Wales: no weapons, no priests, one witness each. The raider arrives on a grey horse. He sits on a stone, takes off his hat, and says that he has come to say what happened.",
   [
       O("Swear peace on the stone.", PRESTIGE_S, STRESS_DOWN, "scope:eir_raider ?= { add_opinion = { target = root modifier = eir_blood_price_paid_opinion opinion = 20 } }", "remove_variable = eir_revenge_target", st=S_FORGIVE, ai=30, ai_mod=[("forgiving", 25)]),
       O("Demand a price and a hostage.", GAIN_M, HOOK, st=S_SHREWD, ai=35),
       O("Spit on the stone and ride away.", LOSS_S, "add_dread = minor_dread_gain", VOW, st=S_WRATH, ai=20, ai_mod=[("wrathful", 20)]),
   ], "diplomacy", gate="exists = scope:eir_raider", guarded=False)

ev(1219, "Revenge Raid?",
   "Your captains have gathered in the hall, with their spears, to ask for leave to answer the raid.",
   "They all speak at once, until the oldest of them clears his throat. He says that the law of the hawk allows a man to take back what was taken, and a little more for the trouble. He says the borderlands of the raider are lightly held. He says nothing about the poets, who are very quiet.",
   [
       O("Give them leave and your blessing.", VOW, "eir_defender_levy_effect = yes", PRESTIGE_S, st=S_WRATH, ai=40, ai_mod=[("wrathful", 20), ("vengeful", 20)]),
       O("Tell them to wait for the spring.", STRESS_DOWN, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 2 }", st=S_PATIENT, ai=35),
       O("Forbid it, in the name of the peace.", PIETY_S, LOSS_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -3 }", st=S_FORGIVE, ai=15, ai_mod=[("forgiving", 20)]),
   ], "war", gate="exists = scope:eir_raider", guarded=False)

# ============================================================================================== THE LOOT COMES HOME (1220-1223)
ev(1220, "The Loot Comes Home",
   "The raiders have come home, with cattle, silver and an air of great achievement.",
   "The whole household has turned out to see them. The cattle are driven into the pen. The silver is counted on the table. The captains are already telling the story, with improvements.",
   [
       O("Divide it fairly by the old law.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_fair_dealing_opinion OPINION = 4 }", st=S_HONEST, ai=40),
       O("Give the lion's share to the captains.", GOLD_M, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }", st=S_GEN, ai=30, ai_mod=[("generous", 25)]),
       O("Keep the best for the treasury.", GAIN_M, "eir_vassal_opinion_effect = { MODIFIER = eir_tribute_resentment_opinion OPINION = -4 }", st=S_GREED, ai=15, ai_mod=[("greedy", 25)]),
   ], "war", guarded=False)

ev(1221, "The Story Spreads",
   "The raid has become a story, and the story is changing in the telling.",
   "In the first version, you took three hundred cattle. In the second, you took six hundred, killed a champion and burned a hall. In the third version you rode into the lord's own bedchamber and took the blanket from his bed. You are beginning to feel that you might have been there.",
   [
       O("Let the story grow.", PRESTIGE_M, FAME, st=S_ARROG, ai=40, ai_mod=[("arrogant", 15)]),
       O("Correct the story, quietly, when asked.", PRESTIGE_S, STRESS_DOWN, st=S_HONEST, ai=30),
       O("Have a poet write the true version and keep it in the hall.", PRESTIGE_S, xp("lifestyle_poet", 15), st=S_HUMBLE, ai=25),
   ], "legend", guarded=False)

ev(1222, "A Young Raider Distinguishes Himself",
   "One of the youngest in the raid, a boy of sixteen, took a banner from the lord's guard and rode home with it over his shoulder.",
   "His mother is a seamstress, his father is a horse-thief and he has the kind of confidence that is either destined for greatness or for a rope. The captains are watching to see what you do.",
   [
       O("Knight him in front of the host.", PRESTIGE_M, xp("lifestyle_blademaster", 15), "add_character_modifier = { modifier = eir_hosting_modifier years = 3 }", st=S_GEN, ai=40),
       O("Give him a horse and a cloak and send him back to his mother.", GOLD_S, PRESTIGE_S, st=S_PATIENT, ai=30),
       O("Take the banner and tell him he was lucky.", LOSS_S, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 2 }", st=S_ARROG, ai=10, ai_mod=[("arrogant", 20)]),
   ], "war", guarded=False)

ev(1223, "The Abbot's Share",
   "The abbot of the nearest monastery has asked, courteously, for his tenth of the spoils.",
   "He did not say what it was for. He did say that the raiders who went out carried the monastery's blessing, that the Church has a long memory and that the library roof needs mending.",
   [
       O("Give him the tenth, and a little more.", GOLD_M, PIETY_L, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 5 }", st=S_ZEAL, ai=40, ai_mod=[("zealous", 20)]),
       O("Give him a tenth of what is left after the captains.", GOLD_S, PIETY_S, st=S_SHREWD, ai=30),
       O("Refuse: the spoils are the host's.", LOSS_S, "add_piety = minor_piety_loss", "eir_vassal_opinion_effect = { MODIFIER = eir_hard_justice_opinion OPINION = -2 }", st=S_GREED, ai=10, ai_mod=[("cynical", 15)]),
   ], "legend", guarded=False)

# ============================================================================================== A RAID ARMY IS BEATEN (1224-1225)
ev(1224, "The Raiders Are Beaten",
   "Your raiders were caught on the road home and scattered, and the lord they robbed has the cattle.",
   "A few of the captains are straggling back with their cloaks torn and their stories unprepared. The lord's messenger is already on his way, probably with a list. The poets, who had been composing something heroic, are reconsidering.",
   [
       O("Send the blood-price at once, with an apology.", GOLD_M, "scope:eir_victim ?= { add_opinion = { target = scope:eir_raider modifier = eir_blood_price_paid_opinion opinion = 25 } }", STRESS_DOWN, st=S_HONEST, ai=30, ai_mod=[("honest", 15)]),
       O("Swear never to raid that lord again.", PRESTIGE_S, STRESS_DOWN, st=S_FORGIVE, ai=30),
       O("Swear revenge on the lord who beat you.", "set_variable = { name = eir_revenge_target value = scope:eir_victim years = 12 }", "add_character_modifier = { modifier = eir_revenge_vow_modifier years = 8 }", st=S_WRATH, ai=35, ai_mod=[("vengeful", 25)]),
   ], "war", gate="exists = scope:eir_victim", guarded=False)

ev(1225, "The Raiders Are Caught",
   "Your levy has caught the raiders on the road and brought a number of them back in chains.",
   "They are a sorry sight. Half of them are wounded, the rest are scared and one is wearing a dead man's hat. The captain, a tall man with a scar, stands very straight and says that he will answer for them all.",
   [
       O("Hang them on the hill where everyone can see.", "add_dread = major_dread_gain", PRESTIGE_S, "scope:eir_raider ?= { add_opinion = { target = root modifier = eir_raid_grudge_opinion opinion = -40 } }", st=S_HARD, ai=25, ai_mod=[("sadistic", 20), ("wrathful", 15)]),
       O("Ransom the captains and release the rest.", GAIN_M, st=S_GREED, ai=40),
       O("Send them all home with a warning and some bread.", PIETY_M, PRESTIGE_S, "scope:eir_raider ?= { add_opinion = { target = root modifier = eir_blood_price_paid_opinion opinion = 15 } }", st=S_FORGIVE, ai=25, ai_mod=[("forgiving", 25)]),
   ], "war", gate="exists = scope:eir_raider", guarded=False)

# ============================================================================================== THE VOW IS REMEMBERED (1226)
ev(1226, "The Vow Has Not Been Kept",
   "The relics on which you swore revenge have been taken out of the chest, and the poet has reminded you of the oath.",
   "Years have passed. The anger has cooled, a little, in some places. The poet recites the vow in full, as it was sworn, in the voice of someone reading a bill. Nobody in the hall is quite looking at you.",
   [
       O("Renew the vow.", "add_character_modifier = { modifier = eir_revenge_vow_modifier years = 8 }", PRESTIGE_S, STRESS_UP, st=S_WRATH, ai=30, ai_mod=[("vengeful", 25)]),
       O("Forgive the raider and let the vow lapse.", "remove_variable = eir_revenge_target", STRESS_DOWN, PIETY_M, st=S_FORGIVE, ai=35, ai_mod=[("forgiving", 25)]),
       O("Send the blood-price demand and leave the vow open.", PRESTIGE_S, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }", st=S_SHREWD, ai=30),
   ], "court", gate="has_variable = eir_revenge_target", guarded=False)
