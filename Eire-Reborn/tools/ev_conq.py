"""Update 3: the five Conquerors. For each: an arrival (a choice, then the war), a mid-war beat, the player's victory and the player's defeat.
Event numbers 06k0 arrival, 06k1 victory, 06k2 defeat, 06k3 mid-war, 06k4 timeout (hidden), 06k5 delayed landing (hidden); k = 1..5."""
from ev_h import *
import ev_h
from conq_data import CONQ
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"
PORT = "left_portrait = {\n\tcharacter = scope:eir_conqueror\n\tanimation = personality_bold\n}"
SAVE_LORD = "var:eir_conq_lord_var ?= {\n\tsave_scope_as = eir_conqueror\n}"

# ----------------------------------------------------------------------------------------------------------------
# prose per conqueror
# ----------------------------------------------------------------------------------------------------------------
T = {
    1: dict(
        a_title="The English King Marches North", a_sum="[eir_conqueror.GetShortUIName] has sent a herald across the border: Scotland is to be an English shire, and its language an English one.",
        a_body="The herald is polite and exact. He reads the king's letter in two languages and a third, for the monks. The English have taken York and Chester; the old Northumbrian earldom is theirs; the Danes of the Danelaw have been shouldered aside. The king has a new idea, which is that the island should have one law, one tongue and one crown, and that it should be his. He has nine thousand men on the road already, and he would prefer, with all courtesy, that you did not make him use them.",
        a_opts=["Send the herald home with a refusal and call out every vassal.", "Receive the herald at the high table and try to talk the king out of it.", "Pay the king's price: a great tribute, and a bended knee in writing.",
                "Send to every Gaelic and Brittonic king for men and promises.", "Raid his border towns before his host is ready."],
        m_title="The English Reeves at Your Border", m_sum="The English host is in your kingdom, and its reeves are already posting writs in English.",
        m_body="They come with clerks. That is the strange thing about this army: it marches with scribes, who draw up the boundaries of the new shires as it goes. The farmers of the border counties have been told that their lord is now the king of England, and that they will pay their tithe to a bishop they have never heard of. A few of them have started to believe it.",
        m_opts=["Burn the harvest in front of the host.", "Hire a company of mercenaries from the Isles.", "Carry the relics to the front and bless the army.", "Offer single combat to their marshal."],
        w_title="The English Host Breaks", w_sum="The great English army has been broken on Scottish ground, and the king's writ now stops at the Tweed.",
        w_body="They were very sure of themselves. They had not expected the Gaelic army to hold the ford, and they had not expected the Gaelic cavalry to come round by the hill. By nightfall the English standard was in the mud and the clerks were running for the border with their parchment under their arms. In Winchester the chroniclers are using the word 'unfortunate'. In Scotland the poets are using a different word.",
        w_opts=["Take the name the army is shouting.", "Ransom the captured English lords for a king's price.", "Free the counties, and feed them from the English baggage-train.", "Commission the poets and have the sword hung in your hall."],
        l_title="Scotland Is Made English", l_sum="The English have won the war, and they are making a shire of Scotland, one county at a time.",
        l_body="It does not look like a conquest. That is the cleverest part. The writs arrive in English, and the sheriffs pay for what they take, and the new thane at the old hall is polite. But the meadows are overgrazed by the baggage-train's cattle, the monasteries have been taxed, the mills have been burned for fuel, and the new English priests say the Mass in a way that makes the old women flinch. A third of the people are being taught to answer in English, and the rest have noticed which third.",
        l_opts=["Swear to rebuild every burned mill, and hold to it.", "Take to the hills and swear vengeance on the English crown.", "Send the people and the relics west to the islands.", "Beg the English king for mercy."],
    ),
    2: dict(
        a_title="The Sea-King's Great Fleet", a_sum="[eir_conqueror.GetShortUIName], the greatest sea-king of the age, has sworn to take Ireland, and a hundred and fifty ships are on the horizon.",
        a_body="They were seen first by a shepherd, and then by the monks, and then by every beacon on the east coast. The king is not a man who raids: he is a man who rules the sea, and who has decided to rule the land beside it. He has the Orkneys and the Isles, the Danes of the Danelaw send him ships, and he has a way with a shield wall that the poets will not enjoy describing. A boat has come ashore under a white shield. He offers terms. They are not good terms.",
        a_opts=["Send the herald away with an Irish refusal, and call out the hosting.", "Meet the herald at the harbour and try to bargain.", "Pay the king's tribute: silver by the shipload and a hostage.",
                "Send to every Gaelic king for the old defensive compact.", "Burn his anchorage at night before the fleet can gather."],
        m_title="The Longphorts of the Sea-King", m_sum="The Norse have fortified the beach, and the sea-king himself has set up his tent.",
        m_body="They did it in a week. The ships were drawn up on the sand in a ring and a stockade rose in front of them. There is a hall of turf and timber, a smithy and a market, and a great flag with a raven on it. The king is said to be sitting in it with his jarls, eating beef and drinking Irish ale. The local farmers are selling him cattle. They are not being altruistic: they are afraid.",
        m_opts=["Burn the fields between the longphort and the hills.", "Hire a company of gallowglass out of the Isles.", "March the relics and the monks round the stockade at dawn.", "Challenge the sea-king's best axeman to single combat."],
        w_title="The Sea-King Falls", w_sum="The greatest Norse fleet in a generation has been broken on the strand, and the sea-king's banner is in the sand.",
        w_body="It was the worst day of his life. He had never lost a battle on land, and he lost this one in an afternoon, because the Irish waited for the tide, and because someone had cut the cables on half his ships. The king left by the last boat, with a wound in his shoulder. The poets are saying that the sea gave him back to the Gael. The Norse are saying nothing, and burying their dead.",
        w_opts=["Take the name the host has given you.", "Hold the king's heir for ransom.", "Divide the plunder among the clans and the monasteries.", "Commission the poets, and hang the axe in your hall."],
        l_title="The Norse Take the Coast", l_sum="The sea-king has won the war, and the coast of Ireland is his from the Liffey to the Shannon.",
        l_body="The kings who did not come to your aid are making their peace with him. The monasteries are paying a ransom, and the churches are being taxed. The longphorts are rising where the abbeys stood. In the evenings the Norse sit in the ruins of the cloister and sing in their own tongue, and the monks who stayed behind take down the words. The harvest is thin. The cattle are thin. A third of the coast has been signed over to Norse thanes with Irish wives.",
        l_opts=["Swear to rebuild the burned churches and hold to it.", "Take to the bogs and swear vengeance on the sea-king.", "Send the books and the relics west to the islands.", "Beg the sea-king for terms."],
    ),
    3: dict(
        a_title="The King of the Old North Rides", a_sum="[eir_conqueror.GetShortUIName] has called out the Britons of the North and sworn to take back what the poems say was always theirs.",
        a_body="The Britons of the North have been losing for six hundred years, and they have had a great deal of time to compose their grievance. It is in the old poems: the lands from the Forth to the Humber were once the kingdom of the Old North, and they were taken from the Britons by the Angles, the Picts and the Gaels, in that order. The king has decided that the order should be reversed. He is not a fool. He has Cumbrians, Strathclyders and Welsh volunteers, and he is a hundred miles from the nearest English patrol.",
        a_opts=["Refuse, and call out the hosting of the Gael.", "Receive the king's envoy as a cousin and try to reason.", "Pay the king's price: a great tribute and a hostage.",
                "Call every Gaelic and Brittonic king to a council of the island.", "Strike his marches before his hosting can assemble."],
        m_title="The Old North Is Rising", m_sum="The Britons are in your kingdom, and the old Brittonic place-names are coming back on their lips.",
        m_body="They are being greeted as liberators in some of the glens. That is the worst thing about them: they are not entirely wrong. There are people in the Lowlands who still speak the old tongue at home, and who kept a stone with a Latin inscription for six hundred years. The king has been putting up crosses with the old British names carved on them. The poets of the North are composing their finest work in a generation.",
        m_opts=["Burn the harvest between the host and the hills.", "Hire a company of Irish mercenaries.", "Carry the relics to the front and bless the army.", "Offer the Briton king single combat at the old ford."],
        w_title="The Old North Is Broken", w_sum="The Britons of the North have been beaten on the field, and their dream of a restored kingdom has died again.",
        w_body="The battle took place at an old Roman fort, which the king had chosen for the sentiment. He lost because the ground favoured the Gaelic spear, and because the Pictish levy would not fight. The king was carried from the field with his banner wrapped round him. The Britons are going home in small groups, singing the oldest of their laments. It is a sad song, and the Gaels are quiet as they listen to it.",
        w_opts=["Take the name the army gives you.", "Take the king's heir as a hostage and a guest.", "Free the glens and let the old speech be used in the churches.", "Commission the poets, and take the dragon-sword for your hall."],
        l_title="The Old North Rises", l_sum="The Britons have won the war, and they are taking back their ancient lands one glen at a time.",
        l_body="They come with their crosses and their genealogies and a very good memory. The Gaelic place-names have been struck off the charters and the old British ones written in. The mills have been burned for fuel, the monasteries have been taxed, the herds have been driven south. A third of the people are being taught to answer in Brittonic, and the rest are not sure whether to laugh or weep. The kings of the Old North are crowned on the hill at last.",
        l_opts=["Swear to rebuild and hold to it.", "Take to the hills and swear vengeance on the Britons.", "Send the relics and the books west to the islands.", "Beg the Briton king for terms."],
    ),
    4: dict(
        a_title="The Earl of the Isles Sails", a_sum="[eir_conqueror.GetShortUIName], the Earl of the Isles, has gathered the longships of the Northern Isles and set course for your coast.",
        a_body="He is an earl, not a king, and he has made it a point of pride. He holds Orkney, Shetland, and a good part of Caithness, and he has spent forty years winning wars no one thought he could win. His longships have been seen off Skye and Mull. His skalds say he has been promised a kingdom by an ancestor in a dream. His men say it is a better dream than most.",
        a_opts=["Refuse the earl's terms and call out the hosting.", "Meet the earl's envoy at a feast and try to talk him down.", "Pay his tribute: silver by the chestful and a hostage.",
                "Send to every Gaelic king for the defensive compact.", "Burn his ships at anchor before the fleet is ready."],
        m_title="The Earl in the Glens", m_sum="The earl's army has landed on the western shore, and the Isles are on his side.",
        m_body="The galley-lords of the Isles are the ones who make it dangerous. They are of Norse and Gaelic blood, and they change sides when it suits them. For the moment, it suits them to sail with the earl. They have brought three hundred ships and a great many axes. The glens are full of fires. The old men say they have not seen the sea so full of oars since their grandfathers' time.",
        m_opts=["Burn the glens between the shore and the hills.", "Hire a company of gallowglass from the southern Isles.", "March the relics and the monks to the front.", "Challenge the earl's champion to a duel on the shore."],
        w_title="The Earl Is Broken", w_sum="The Earl of the Isles has been beaten on the Scottish shore and has gone back to his islands with half his fleet.",
        w_body="He was too sure. He thought the Gaels would not stand against the Norse, and they did. He thought the Isles would hold, and they did not, because half the galley-lords decided in the middle of the battle that the Scottish king was the better bet. The earl sailed away with a spear in his shoulder. The Norse do not like to lose. The Isles have made a note of this.",
        w_opts=["Take the name the host has given you.", "Hold the earl's son for ransom.", "Divide the plunder among the clans and the monasteries.", "Commission the poets and hang the axe in your hall."],
        l_title="The Earl Takes the Coast", l_sum="The Earl of the Isles has won the war, and the western coast of the kingdom is his.",
        l_body="The galley-lords who stayed neutral are now very loud in their support. The earl's thanes sit in the old halls, the earl's skalds sing in the new ones, and the churches are being taxed for the privilege. The meadows are overgrazed by the baggage-train's cattle. The mills have been burned for fuel. A third of the coast has been signed over to Norse thanes with Gaelic wives, who say they have always been Norse.",
        l_opts=["Swear to rebuild and hold to it.", "Take to the hills and swear vengeance on the earl.", "Send the relics and the books west to the islands.", "Beg the earl for terms."],
    ),
    5: dict(
        a_title="The King's Marshal Lands", a_sum="[eir_conqueror.GetShortUIName], the king's marshal, has crossed the sea with an army of knights to bring Ireland to heel.",
        a_body="They come with a charter and a grant of the whole island. They also come with armour and horses of a size no Irishman has seen, and with clerks who write down the names of the villages. The marshal has been given the right to everything he can hold, and he intends to hold it all. He has nine thousand men, a dozen siege engines on carts, and a Pope's blessing. He is not in the least discouraged by the weather.",
        a_opts=["Refuse the marshal's terms and call out the hosting.", "Receive the marshal at the high table and try to bargain.", "Pay the marshal's price: a great tribute and a hostage.",
                "Call every Gaelic king to the old compact of the island.", "Strike his camp before his horses are landed."],
        m_title="The Marshal's Castles", m_sum="The marshal's knights are building castles of earth and timber on every ford.",
        m_body="They are very good at it. A mound, a ditch and a palisade can be raised in a week, and a keep of oak in a month. They call them motte and bailey. The Irish call them something else. Every ford in the east is guarded by one, and every one is held by a knight with a dozen men-at-arms and a horse bigger than his cow. The marshal has not lost a skirmish yet. He plans to keep it that way.",
        m_opts=["Burn the fields between the castles and the hills.", "Hire a company of gallowglass.", "Carry the relics to the front and bless the army.", "Offer the marshal single combat before his castles."],
        w_title="The Marshal's Host Falls", w_sum="The knightly army of England has been broken on Irish ground, and the marshal's banner is in the bog.",
        w_body="They learned what the Irish bog is for. The horses sank, the knights flailed, and the kern came out of the reeds with their javelins. By nightfall the marshal's army was a rabble, and the marshal himself was begging his captors to take his sword instead of his horse. The English crown will be asking questions. The Irish are laughing.",
        w_opts=["Take the name the host has given you.", "Hold the marshal for a king's ransom.", "Divide the plunder among the clans and the monasteries.", "Commission the poets, and hang the sword in your hall."],
        l_title="The Marshal Takes the East", l_sum="The King's Marshal has won the war, and the castles of the English now stand across the east of the island.",
        l_body="They are being very thorough. Every castle comes with a charter, a bailiff and a court that sits in French. The Irish farmers pay rent to a lord they have never seen. The monasteries are paying a fine. The hall of the old king has been given to a knight, and the old king's hounds have been given to his hunting-dogs. The harvest is thin, the mills are burnt, and a third of the people are being taught to answer in English.",
        l_opts=["Swear to rebuild and hold to it.", "Take to the bogs and swear vengeance on the English crown.", "Send the relics and the books west to the islands.", "Beg the marshal for terms."],
    ),
}


def conq(c):
    k = c["id"]
    t = T[k]
    base = 600 + 10 * k
    done_prev = "" if k == 1 else "\nhas_global_variable = eir_conq_done_%d" % (k - 1)
    any_ruler = ("any_ruler = {\n\tis_ai = yes\n\tis_ruler = yes\n\tis_independent_ruler = yes\n\thighest_held_title_tier >= tier_duchy\n"
                 + "".join("\t" + l + "\n" for l in c["cult"].split("\n")) + "\tNOT = { has_truce = root }\n\tNOT = { this = root }\n}")
    launch = "eir_conq_launch_%d_effect = yes" % k
    # ---------------------------------------------------------------- arrival
    ev(base, t["a_title"], t["a_sum"], t["a_body"], [
        O(t["a_opts"][0], launch, "eir_defender_levy_effect = yes", "eir_defender_levy_effect = yes", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 3 }", PRESTIGE_S,
          st=S_BRAVE, ai=40, ai_mod=[("brave", 20), ("wrathful", 10)]),
        O(t["a_opts"][1],
          luck("c%da" % k, "The king hears you out, and the host is called back to its ships for a time", "add_prestige = medium_prestige_gain\nadd_character_modifier = { modifier = eir_foreknowledge_modifier years = 4 }\ntrigger_event = { id = eir.06%d5 days = 1000 }" % k,
               "c%db" % k, "The king hears you out and his host marches the next morning", launch + "\nadd_prestige = minor_prestige_loss\nscope:eir_conqueror = { add_character_modifier = { modifier = eir_conqueror_emboldened_modifier years = 4 } }",
               p=45, bonus=(25, "diplomacy >= 14")),
          gate="OR = {\ndiplomacy >= 11\nhas_trait = gregarious\nhas_trait = honest\n}", st=S_PATIENT, ai=25, ai_mod=[("gregarious", 15), ("patient", 10)]),
        O(t["a_opts"][2], "remove_short_term_gold = 800", "add_prestige = major_prestige_loss", "add_character_modifier = { modifier = eir_conq_tributary_modifier years = 10 }", "add_stress = minor_stress_gain",
          gate="gold >= 800", st="brave = minor_stress_impact_gain\ncraven = minor_stress_impact_loss", ai=6, ai_mod=[("craven", 25)]),
        O(t["a_opts"][3], launch, "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 5 }", "add_character_modifier = { modifier = eir_allied_kings_modifier years = 5 }",
          "spawn_army = {\n\tlevies = 1800\n\tmen_at_arms = {\n\t\ttype = light_footmen\n\t\tstacks = 3\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_allied_kings_host_name\n}",
          gate="eir_stage3_trigger = yes", st=S_SHREWD, ai=45, ai_mod=[("gregarious", 15), ("shrewd", 10)]),
        O(t["a_opts"][4],
          luck("c%dc" % k, "The raid lands true, and his host marches under a cloud", launch + "\nadd_prestige = medium_prestige_gain\nscope:eir_conqueror = { add_character_modifier = { modifier = eir_host_demoralised_modifier years = 2 } }",
               "c%dd" % k, "The raid is beaten off and the king is enraged", launch + "\nadd_prestige = minor_prestige_loss\nincrease_wounds_effect = { REASON = fight }\nscope:eir_conqueror = { add_character_modifier = { modifier = eir_conqueror_emboldened_modifier years = 4 } }",
               p=40, bonus=(25, "martial >= 16")),
          gate="OR = {\nmartial >= 12\nhas_trait = brave\n}", st=S_BRAVE, ai=25, ai_mod=[("brave", 20), ("deceitful", 10)]),
    ], "war",
       gate="eir_conq_ready_trigger = yes\ncurrent_year >= %d\nNOT = { has_global_variable = eir_conq_done_%d }%s\n%s" % (c["start"], k, done_prev, any_ruler),
       guarded=False, portraits=PORT,
       immediate="eir_conq_pick_%d_effect = yes\nset_global_variable = eir_conq_done_%d\nset_global_variable = { name = eir_conq_cooldown days = 14600 }" % (k, k))
    # ---------------------------------------------------------------- victory
    ev(base + 1, t["w_title"], t["w_sum"], t["w_body"], [
        O(t["w_opts"][0], "give_nickname = nick_eir_warlord_slayer", "add_prestige = major_prestige_gain", "eir_legend_defence_effect = yes", "eir_world_reacts_effect = yes",
          st=S_ARROG, ai=40, ai_mod=[("arrogant", 20), ("ambitious", 15)]),
        O(t["w_opts"][1], "add_gold = major_gold_value", PRESTIGE_M, "add_hook = { target = scope:eir_conqueror type = favor_hook }", "add_dread = minor_dread_gain",
          st=S_GREED, ai=30, ai_mod=[("greedy", 20)]),
        O(t["w_opts"][2], PIETY_M, PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 8 }", "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 6 }",
          "eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 30 }", st=S_KIND, ai=35, ai_mod=[("compassionate", 20), ("generous", 15)]),
        O(t["w_opts"][3], PRESTIGE_M, xp("lifestyle_poet", 40),
          "eir_make_artifact_effect = { NAME = %s_name DESC = %s_desc TYPE = sword VISUALS = sword MODIFIER = %s_modifier }" % (c["sword"], c["sword"], c["sword"]),
          "eir_legend_defence_effect = yes", gate=FILI, st=S_HUMBLE, ai=30),
    ], "legend", guarded=False, portraits=PORT,
       immediate="scope:eir_conqueror = { save_scope_as = eir_norse_lord }\nadd_character_modifier = { modifier = %s years = 25 }\neir_conq_victory_effect = yes" % c["bane"])
    # ---------------------------------------------------------------- defeat
    ev(base + 2, t["l_title"], t["l_sum"], t["l_body"], [
        O(t["l_opts"][0], "add_character_modifier = { modifier = eir_conq_resolve_modifier years = 12 }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 5 }",
          "add_character_flag = { flag = eir_vowed_rebuild years = 12 }", st=S_PATIENT, ai=45, ai_mod=[("diligent", 15), ("patient", 15)]),
        O(t["l_opts"][1], "add_character_flag = { flag = eir_vowed_vengeance years = 15 }", "add_character_flag = { flag = eir_oath_to_reclaim years = 15 }", "add_character_modifier = { modifier = eir_hill_war_modifier years = 10 }",
          xp("lifestyle_hunter", 25), STRESS_UP, st=S_WRATH, ai=30, ai_mod=[("vengeful", 25), ("brave", 10)]),
        O(t["l_opts"][2], PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }", "capital_county ?= { change_county_control = medium_county_control_gain }", xp("lifestyle_mystic", 20),
          gate="piety >= 100", st=S_ZEAL, ai=25, ai_mod=[("zealous", 25)]),
        O(t["l_opts"][3],
          luck("c%de" % k, "He is merciful, for a price", "remove_short_term_gold = medium_gold_value\nrandom_sub_realm_county = {\n\tlimit = { has_county_modifier = eir_ravaged_modifier }\n\tremove_county_modifier = eir_ravaged_modifier\n}\nadd_prestige = minor_prestige_gain",
               "c%df" % k, "He laughs, and takes a hostage as well", "add_prestige = medium_prestige_loss\nadd_stress = minor_stress_gain", p=40, bonus=(20, "diplomacy >= 14")),
          st="craven = minor_stress_impact_loss\nbrave = minor_stress_impact_gain", ai=15, ai_mod=[("craven", 20)]),
    ], "dungeon", guarded=False, portraits=PORT, immediate="eir_conq_ravage_effect = yes")
    # ---------------------------------------------------------------- mid-war
    ev(base + 3, t["m_title"], t["m_sum"], t["m_body"], [
        O(t["m_opts"][0], "random_sub_realm_county = {\n\tlimit = { is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_scorched_earth_modifier years = 3 }\n}",
          "add_character_modifier = { modifier = eir_hill_war_modifier years = 3 }", xp("lifestyle_hunter", 20), STRESS_UP, st=S_HARD, ai=30, ai_mod=[("callous", 15)]),
        O(t["m_opts"][1], "remove_short_term_gold = 300", "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = armored_footmen\n\t\tstacks = 5\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_gallowglass_company_name\n}",
          PRESTIGE_S, gate="gold >= 300", st=S_GREED, ai=35),
        O(t["m_opts"][2], PIETY_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 2 }", xp("lifestyle_mystic", 20),
          gate="piety >= 80", st=S_ZEAL, ai=30, ai_mod=[("zealous", 25)]),
        O(t["m_opts"][3],
          luck("c%dg" % k, "Your champion wins, and the enemy host loses heart", "scope:eir_conqueror = { add_character_modifier = { modifier = eir_host_demoralised_modifier years = 2 } }\nadd_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_blademaster value = 40 }",
               "c%dh" % k, "Your champion falls", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain\nincrease_wounds_effect = { REASON = fight }", p=45, bonus=(30, "prowess >= 18")),
          gate="OR = {\nprowess >= 12\nhas_trait = brave\n}", st=S_BRAVE, ai=20, ai_mod=[("brave", 25)]),
    ], "war", guarded=False, portraits=PORT, gate="has_global_variable = eir_conq_active\nis_at_war = yes", immediate=SAVE_LORD)
    # ---------------------------------------------------------------- hidden: timeout and delayed landing
    EVENTS.append(E(base + 4, "", "", "", [], hidden=True, theme="war", trigger="",
                    immediate="""if = {
	limit = { has_global_variable = eir_conq_active }
	if = {
		limit = { is_at_war = no }
		eir_conq_clear_effect = yes
	}
	else = {
		trigger_event = { id = eir.%04d days = 365 }
	}
}""" % (base + 4)))
    EVENTS.append(E(base + 5, "", "", "", [], hidden=True, theme="war", trigger="",
                    immediate="""eir_conq_pick_%d_effect = yes
if = {
	limit = {
		exists = scope:eir_conqueror
		exists = scope:eir_conq_title
		eir_conq_target_trigger = yes
		NOT = { has_global_variable = eir_conq_active }
	}
	eir_conq_launch_%d_effect = yes
}""" % (k, k)))


for c in CONQ:
    conq(c)


# ----------------------------------------------------------------------------------------------------------------
# 0700: hidden diagnostic. Five days after an Irish ruler with tributaries dies, compare the heir's tributaries with the dead
# ruler's and write the answer to debug.log. It changes nothing.
# ----------------------------------------------------------------------------------------------------------------
EVENTS.append(E(700, "", "", "", [], hidden=True, theme="court", trigger="",
                immediate="""if = {
	limit = { has_variable = eir_tribs_before }
	if = {
		limit = { number_of_tributaries < var:eir_tribs_before }
		debug_log = "EIR tributary check: the heir LOST tributaries after succession"
	}
	else = {
		debug_log = "EIR tributary check: the heir kept the tributaries"
	}
	remove_variable = eir_tribs_before
}"""))
