"""Update 2, part D: chieftain-level stories for the early game (0530-0543) and the ceremonies of the new decisions
(0544-0567). Early stories need no stage: a ruler of one or two counties sees them from the first years."""
from ev_h import *
import ev_h
EVENTS = ev_h.EVENTS = []

FILI = "has_global_variable = eir_done_fili"
FOSTER = "has_global_variable = eir_done_fosterage"
EARLY_CD = "add_character_flag = { flag = eir_early_cd years = 2 }"


def early(num, title, summary, body, options, theme, gate="", cooldown=8, immediate="", variants=None, portraits=""):
    """a chieftain story: Gaelic ruler of a small realm, 2-year personal gap, 8-year cooldown"""
    ev(num, title, summary, body, options, theme,
       gate="eir_small_realm_trigger = yes\nNOT = { has_character_flag = eir_early_cd }" + ("\n" + gate if gate else ""),
       cooldown=cooldown, immediate=(immediate + "\n" if immediate else "") + EARLY_CD, variants=variants, guarded=False, portraits=portraits)


# =============================================================================
# EARLY GAME: stories for a chieftain of one to a few counties
# =============================================================================
early(530, "A Wandering Poet Asks for a Bed",
      "A poet with a small harp and a large reputation has knocked at your door in the rain.",
      "He says he has composed for kings and been thrown out of three halls for it. He says he has a verse about you already, which he will not recite until he has eaten. Hospitality is a law, not a courtesy, and the Irish do not refuse a poet a bed.\n\nHe is also, you suspect, a spy for the king next door.",
      [
          O("Feed him, house him and let him sing.",
            PRESTIGE_S, xp("lifestyle_poet", 20), "add_character_modifier = { modifier = eir_bardic_circuit_modifier years = 3 }", GOLD_S,
            st=S_GEN, ai=45, ai_mod=[("generous", 20), ("gregarious", 10)]),
          O("Feed him, and ask for news of the other halls.",
            PRESTIGE_S, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 3 }", xp("lifestyle_reveler", 10),
            gate="OR = {\nintrigue >= 8\nhas_trait = shrewd\nhas_trait = deceitful\n}", st=S_SHREWD, ai=35, ai_mod=[("shrewd", 15), ("deceitful", 10)]),
          O("Let him sleep in the byre.",
            STRESS_DOWN, LOSS_S, "add_character_modifier = { modifier = eir_poet_slighted_modifier years = 3 }", st=S_GREED, ai=15, ai_mod=[("greedy", 20)]),
          O("Challenge him to a verse-contest for his supper.",
            luck("t530w", "Your verse wins, and the hall roars", "add_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_poet value = 30 }",
                 "t530l", "His verse is better, and you pay for the supper", "add_prestige = minor_prestige_loss\nremove_short_term_gold = minor_gold_value", p=40, bonus=(25, "learning >= 12")),
            gate="learning >= 7", st=S_ARROG, ai=25, ai_mod=[("arrogant", 15)]),
      ],
      "court")

early(531, "The Sacred Yew",
      "A monk has felled the old yew by the crossroads, and the farmers have laid down their tools.",
      "It was older than the church, older than the hill-fort and, some say, older than the language. The monk says it was a pagan idol. The farmers say it was a tree. Nobody can agree on which of them is right, but everybody can agree that the monk has an axe and the farmers have scythes.",
      [
          O("Defend the monk, and reprimand the farmers.",
            PIETY_S, PRESTIGE_S, "scope:eir_hold_county ?= { add_county_modifier = { modifier = eir_cultural_resentment_modifier years = 3 } }", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
          O("Plant a new yew beside the church, and bless it.",
            PIETY_S, PRESTIGE_M, xp("lifestyle_mystic", 20), "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }",
            st=S_PATIENT, ai=40, ai_mod=[("patient", 15), ("compassionate", 10)]),
          O("Fine the monk, and return the wood to the farmers.",
            GAIN_S, "add_piety = minor_piety_loss", PRESTIGE_S, "eir_trait_effect = { TRAIT = cynical OPPOSITE = zealous CHANCE = 20 }", st=S_CYN, ai=20, ai_mod=[("cynical", 20)]),
          O("Make the farmers carve a cross from the stump.",
            PIETY_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 2 }", st=S_SHREWD, ai=30),
      ],
      "faith", gate="piety >= 20", immediate="capital_county ?= { save_scope_as = eir_hold_county }")

early(532, "A Quarrelsome Neighbour",
      "The chieftain next door has built a fence across the cattle-track that has been used since before either of your fathers.",
      "He says it's his land. You say it's the track. The cattle, who have a view, are standing at the fence and lowing in two voices. His men are on one side with spears. Yours are on the other with spears. Someone is going to have to say something.",
      [
          O("Pull down the fence and dare him to rebuild it.",
            "add_dread = minor_dread_gain", PRESTIGE_S, "add_character_flag = { flag = eir_vowed_vengeance years = 4 }", "random = {\n\tchance = 25\n\tincrease_wounds_effect = { REASON = fight }\n}",
            st=S_BRAVE, ai=35, ai_mod=[("brave", 20), ("wrathful", 15)]),
          O("Offer to share the track and split the toll.",
            GAIN_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_fair_lord_modifier years = 4 }", st=S_PATIENT, ai=40, ai_mod=[("patient", 15), ("just", 10)]),
          O("Take the dispute to a brehon.",
            PRESTIGE_M, "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 20 }", GOLD_S,
            gate="OR = {\nlearning >= 7\nhas_trait = just\n}", st=S_HONEST, ai=35, ai_mod=[("just", 20)]),
          O("Pay him off, and move the cattle round.",
            GOLD_S, STRESS_DOWN, "add_prestige = minor_prestige_loss", st=S_CRAVEN, ai=20, ai_mod=[("craven", 15)]),
      ],
      "vassal")

early(533, "The Wolf Pack",
      "Wolves have taken three calves from the byre, and the herdsmen are afraid to go out at dusk.",
      "They come down from the bog in winter, silent and thin. The herdsmen say there are nine of them, led by a grey bitch with one ear. The old women say she is a woman in wolf-shape, and that you must give her a calf a year, or she will take a child. Your huntsmen say that is ridiculous, and they are not going near the bog.",
      [
          O("Lead the hunt yourself.",
            luck("t533w", "You bring back the grey bitch's pelt", "add_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_hunter value = 40 }\nadd_character_modifier = { modifier = eir_hunting_hounds_modifier years = 5 }",
                 "t533l", "The wolves slip away and one of your hounds is killed", "add_stress = minor_stress_gain\nadd_prestige = minor_prestige_loss", p=55, bonus=(20, "has_trait = lifestyle_hunter")),
            st=S_BRAVE, ai=40, ai_mod=[("brave", 20)]),
          O("Offer the old women a calf and wait.",
            GOLD_S, xp("lifestyle_mystic", 15), "add_character_modifier = { modifier = eir_hospitality_modifier years = 3 }", st=S_ZEAL, ai=25, ai_mod=[("zealous", 10), ("content", 10)]),
          O("Set a bounty on every wolf-skin.",
            GOLD_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_hunting_hounds_modifier years = 4 }", "capital_county ?= { add_county_modifier = { modifier = eir_booley_county_modifier years = 4 } }",
            gate="gold >= 60", st=S_SHREWD, ai=30, ai_mod=[("diligent", 10)]),
          O("Let the herdsmen deal with it.",
            STRESS_DOWN, "capital_county ?= { add_county_modifier = { modifier = eir_murrain_modifier years = 2 } }", st=S_CONTENT, ai=15, ai_mod=[("lazy", 15)]),
      ],
      "hunting")

early(534, "A Foster-Child Arrives",
      "A small boy, with his belongings in a satchel, has been left at your gate by a neighbouring chief.",
      "He is seven years old and very quiet. His father has sent no letter, only a cow, a cloak and a message that he is to be raised as one of your own. In Ireland, this is a great honour and a great responsibility. In a decade, the boy will be the man who decides whether your neighbour is your friend.",
      [
          O("Raise him as your own son.",
            "add_character_modifier = { modifier = eir_foster_bond_modifier years = 12 }", PRESTIGE_S, xp("lifestyle_reveler", 10), "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 3 }",
            st=S_KIND, ai=45, ai_mod=[("compassionate", 20), ("patient", 10)]),
          O("Hand him to your best warrior to be trained.",
            PRESTIGE_S, "add_character_modifier = { modifier = eir_war_poem_modifier years = 6 }", xp("lifestyle_blademaster", 10),
            gate="martial >= 7", st=S_BRAVE, ai=30, ai_mod=[("brave", 15)]),
          O("Send him to the monastery for his letters.",
            PIETY_S, "add_character_modifier = { modifier = eir_hospitality_modifier years = 5 }", PRESTIGE_S, st=S_ZEAL, ai=35, ai_mod=[("zealous", 20)]),
          O("Send him home with a polite refusal.",
            STRESS_DOWN, LOSS_S, "add_character_modifier = { modifier = eir_poet_slighted_modifier years = 2 }", st=S_CRAVEN, ai=10),
      ],
      "family")

early(535, "The Lughnasa Games",
      "The harvest festival has come, and the young men want to wrestle for a prize.",
      "It is the oldest of the summer festivals. The hill is cleared, the stalls are put up, the horses are paraded and the hurling teams take the field. The prize is a bull-calf, a gold arm-ring and the right to say, for a year, that your family is the best on the hill. Your cousin has entered. So has your steward. So, loudly, has your wife.",
      [
          O("Compete yourself.",
            luck("t535w", "You win the arm-ring", "add_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_blademaster value = 20 }\nadd_trait_xp = { trait = lifestyle_reveler value = 20 }",
                 "t535l", "You are thrown in the mud and everyone cheers", "add_prestige = minor_prestige_loss\nadd_stress = miniscule_stress_gain\nadd_trait_xp = { trait = lifestyle_reveler value = 10 }", p=45, bonus=(30, "prowess >= 14")),
            gate="prowess >= 8", st=S_BRAVE, ai=35, ai_mod=[("brave", 15), ("gregarious", 10)]),
          O("Preside from the high seat and hand out the prizes.",
            PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 3 }", xp("lifestyle_reveler", 20),
            st=S_GEN, ai=45, ai_mod=[("generous", 15)]),
          O("Bet heavily on your cousin.",
            luck("t535b", "Your cousin wins and you collect", "add_gold = minor_gold_value\nadd_prestige = minor_prestige_gain",
                 "t535c", "Your cousin falls and you pay", "remove_short_term_gold = minor_gold_value", p=50),
            st=S_GREED, ai=25, ai_mod=[("greedy", 15)]),
          O("Ban the games for the sake of the harvest.",
            STRESS_UP, LOSS_S, "capital_county ?= { add_county_modifier = { modifier = eir_booley_county_modifier years = 2 } }", st=S_HARD, ai=10, ai_mod=[("diligent", 10)]),
      ],
      "party")

early(536, "The Bog Body",
      "A turf-cutter has found a man in the bog, whole, with his hair in a knot and a rope round his neck.",
      "He is very old. The turf-cutter thinks he is a sacrifice, or a king, or a criminal. The priest says he must be buried properly. The farmers say he should be put back, because they do not like to disturb a man who was put there for a reason. The man's face is peaceful.",
      [
          O("Have him buried in the churchyard with full rites.",
            PIETY_S, PRESTIGE_S, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 2 }", st=S_ZEAL, ai=40, ai_mod=[("zealous", 20)]),
          O("Put him back in the bog, with a prayer.",
            PIETY_S, xp("lifestyle_mystic", 25), "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 2 }", st=S_PATIENT, ai=35, ai_mod=[("patient", 10), ("humble", 10)]),
          O("Display him in the hall, as a wonder.",
            PRESTIGE_M, "add_piety = minor_piety_loss", xp("lifestyle_reveler", 10), "eir_trait_effect = { TRAIT = eccentric OPPOSITE = content CHANCE = 15 }",
            st=S_ARROG, ai=20, ai_mod=[("arrogant", 15)]),
          O("Ask the poets who he might have been.",
            PRESTIGE_S, xp("lifestyle_poet", 25), "eir_legend_title_effect = { TITLE = primary_title }", gate=FILI, st=S_HUMBLE, ai=30),
      ],
      "legend")

early(537, "The Brigand Band",
      "A band of masterless men has taken up residence in the forest, and the traders are going round.",
      "There are about thirty of them, and half of them are somebody's younger son. They live by taking from whoever passes, and they have a rough code: no killing, no women, no churches. They have sent you a polite message, asking whether you would like to hire them.",
      [
          O("Hire them as your own warband.",
            "spawn_army = {\n\tlevies = 0\n\tmen_at_arms = {\n\t\ttype = light_footmen\n\t\tstacks = 1\n\t}\n\tlocation = capital_province\n\torigin = capital_province\n\tinheritable = no\n\tname = eir_bandit_warband_name\n}",
            GOLD_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_gallowglass_paymaster_modifier years = 4 }",
            gate="gold >= 50", st=S_SHREWD, ai=35, ai_mod=[("shrewd", 15), ("ambitious", 10)]),
          O("Ride out and clear the forest.",
            luck("t537w", "The band is broken and the road is safe", "add_prestige = medium_prestige_gain\nadd_dread = minor_dread_gain\nadd_trait_xp = { trait = lifestyle_hunter value = 20 }",
                 "t537l", "The band melts into the trees and your men are ambushed", "add_prestige = minor_prestige_loss\nincrease_wounds_effect = { REASON = fight }", p=50, bonus=(20, "martial >= 10")),
            st=S_BRAVE, ai=40, ai_mod=[("brave", 15), ("wrathful", 10)]),
          O("Pardon them in return for a year's service.",
            PRESTIGE_S, "eir_trait_effect = { TRAIT = forgiving OPPOSITE = vengeful CHANCE = 25 }", "add_character_modifier = { modifier = eir_fair_lord_modifier years = 3 }",
            gate="OR = {\nhas_trait = forgiving\nhas_trait = compassionate\ndiplomacy >= 8\n}", st=S_FORGIVE, ai=30, ai_mod=[("forgiving", 20)]),
          O("Pay them to go bother the next kingdom.",
            GOLD_S, STRESS_DOWN, "add_prestige = minor_prestige_loss", st=S_GREED, ai=25),
      ],
      "war")

early(538, "A Monk Asks for Land",
      "A holy man with a bundle and a bell has asked for a hilltop to build a church.",
      "He says the saint told him to look for a green hill with a spring, and he thinks yours is it. He is eighty, and has founded four churches already. He promises no trouble. His disciples promise a great deal of trouble, none of it for you.",
      [
          O("Give him the hill and a grant of grain.",
            PIETY_M, GOLD_S, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", xp("lifestyle_mystic", 15),
            "capital_county ?= { add_county_modifier = { modifier = eir_hospice_modifier years = 8 } }", st=S_GEN, ai=45, ai_mod=[("zealous", 20), ("generous", 10)]),
          O("Give him the hill, but not the grain.",
            PIETY_S, PRESTIGE_S, st=S_GREED, ai=30),
          O("Give him a worse hill, and keep the good one for the dún.",
            PRESTIGE_S, "add_piety = minor_piety_loss", "add_character_modifier = { modifier = eir_poet_slighted_modifier years = 3 }", st=S_SHREWD, ai=20, ai_mod=[("shrewd", 15)]),
          O("Refuse. The land is already spoken for.",
            STRESS_DOWN, "add_piety = minor_piety_loss", st=S_CYN, ai=10, ai_mod=[("cynical", 20)]),
      ],
      "faith", gate="piety >= 10")

early(539, "The Poor Harvest",
      "The grain has failed in three fields, and the herds are thin.",
      "It is a hungry spring. The stored oats are low, the first lambs are weak and the milk is poor. Three families have been seen on the road with their goods in carts. The old people say the summer was too wet. The young people say the old people always say that.",
      [
          O("Open the granary and feed the hungry.",
            GOLD_M, PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }", "eir_trait_effect = { TRAIT = generous OPPOSITE = greedy CHANCE = 25 }",
            gate="gold >= 60", st=S_GEN, ai=40, ai_mod=[("generous", 20), ("compassionate", 15)]),
          O("Buy grain from the next kingdom.",
            GOLD_M, "capital_county ?= { add_county_modifier = { modifier = eir_booley_county_modifier years = 3 } }", PRESTIGE_S, st=S_SHREWD, ai=35, ai_mod=[("shrewd", 15)]),
          O("Move the herds to the hill pastures early.",
            "capital_county ?= { add_county_modifier = { modifier = eir_booley_county_modifier years = 4 } }", PRESTIGE_S, xp("lifestyle_hunter", 10), STRESS_UP,
            st=S_PATIENT, ai=40, ai_mod=[("diligent", 15)]),
          O("Do nothing. The poor always survive.",
            STRESS_DOWN, "capital_county ?= { add_county_modifier = { modifier = eir_murrain_modifier years = 2 } }", "eir_vassal_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = -4 }",
            st=S_HARD, ai=10, ai_mod=[("callous", 20)]),
      ],
      "stewardship")

early(540, "The Bride's Price",
      "A neighbouring chief has offered his daughter to your son, and named a price in cattle.",
      "The old law fixes the bride-price by rank and by the girl's accomplishments. She is a harper, a rider and a hard bargainer, which the chief mentions with a mix of pride and apprehension. He has asked for forty cows. You were hoping for twenty. The negotiation will go on until midnight.",
      [
          O("Pay what he asks and call it an honour.",
            GOLD_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_hospitality_modifier years = 6 }", "add_hook = { target = scope:eir_pact_chief type = favor_hook }",
            st=S_GEN, ai=35, ai_mod=[("generous", 15)]),
          O("Bargain him down to thirty.",
            luck("t540w", "He agrees, laughing", "remove_short_term_gold = minor_gold_value\nadd_prestige = medium_prestige_gain",
                 "t540l", "He takes offence and ends the talks", "add_prestige = minor_prestige_loss", p=55, bonus=(15, "diplomacy >= 10")),
            st=S_GREED, ai=40, ai_mod=[("greedy", 15), ("shrewd", 10)]),
          O("Offer your own horse and a poem instead.",
            PRESTIGE_S, xp("lifestyle_poet", 20), "scope:eir_pact_chief = { add_opinion = { target = root modifier = eir_fair_dealing_opinion opinion = 25 } }",
            gate="learning >= 8", st=S_HUMBLE, ai=25),
          O("Withdraw. The match was never a good one.",
            STRESS_DOWN, "add_prestige = minor_prestige_loss", st=S_CONTENT, ai=15, ai_mod=[("content", 15)]),
      ],
      "marriage", immediate="random_ruler = {\n\tlimit = {\n\t\tis_ai = yes\n\t\tis_ruler = yes\n\t\tculture ?= { has_cultural_pillar = heritage_goidelic }\n\t\tNOT = { this = root }\n\t\tNOT = { is_vassal_of = root }\n\t}\n\tsave_scope_as = eir_pact_chief\n}",
      gate="any_ruler = {\n\tis_ai = yes\n\tis_ruler = yes\n\tculture ?= { has_cultural_pillar = heritage_goidelic }\n\tNOT = { this = root }\n\tNOT = { is_vassal_of = root }\n}")

early(541, "A Travelling Smith",
      "A wandering smith has set up his anvil by your gate, and the children are watching.",
      "He has a brass-bound hammer, a stack of charcoal and a patter that would sell a sword to a swan. He says he can mend a ploughshare, forge a spear or make a brooch that will keep off the evil eye. Your own smith is looking uneasy.",
      [
          O("Commission a good spear for the household guard.",
            GOLD_S, "add_character_modifier = { modifier = eir_war_poem_modifier years = 3 }", PRESTIGE_S, st=S_GREED, ai=40),
          O("Hire him to teach your smith his tricks.",
            GOLD_S, PRESTIGE_S, "add_character_modifier = { modifier = eir_norse_steel_modifier years = 4 }", "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 2 }",
            st=S_PATIENT, ai=35, ai_mod=[("diligent", 10)]),
          O("Buy the evil-eye brooch.",
            GOLD_S, PIETY_S, xp("lifestyle_mystic", 10), "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 2 }", st=S_ZEAL, ai=20),
          O("Send him on. Your smith is quite enough.",
            STRESS_DOWN, st=S_CONTENT, ai=15),
      ],
      "stewardship", cooldown=12)

early(542, "The Dún's Well Runs Dry",
      "The well at the heart of the dún has gone dry in the drought, and the women are carrying water from the river.",
      "It was dug in your grandfather's day and never failed. The old people say the spring is angry about something. The young people say it is the weather. The priest says the saint of the well has been offended. You say you would like some water.",
      [
          O("Dig deeper, and pay the diggers well.",
            GOLD_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_dun_well_modifier years = 15 }", st=S_SHREWD, ai=35, ai_mod=[("diligent", 15)]),
          O("Offer a ribbon and a prayer to the saint of the well.",
            PIETY_M, xp("lifestyle_mystic", 20), "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 2 }", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
          O("Move the household to the river for the summer.",
            STRESS_UP, "capital_county ?= { add_county_modifier = { modifier = eir_booley_county_modifier years = 2 } }", xp("lifestyle_hunter", 10), st=S_PATIENT, ai=30),
          O("Ask the Welsh monk who is visiting to dowse for a new spring.",
            luck("t542w", "He finds water in an hour", "add_prestige = medium_prestige_gain\nadd_character_modifier = { modifier = eir_dun_well_modifier years = 10 }\nadd_piety = minor_piety_gain",
                 "t542l", "He finds mud and an embarrassed silence", "add_prestige = minor_prestige_loss", p=50),
            st=S_CYN, ai=20, ai_mod=[("trusting", 10)]),
      ],
      "stewardship", cooldown=20)

early(543, "A Hostage Tests the Gate",
      "The child you hold hostage has been seen walking the walls at night, counting the guards.",
      "He is ten. He is very patient. He has noticed the changing of the watch, the weak stretch of the palisade and the way the dogs are fed. He has not tried to escape. He is simply, thoughtfully, storing it all up for when he goes home to his father.",
      [
          O("Tell him you know, and ask what he thinks of the defences.",
            PRESTIGE_S, "eir_trait_effect = { TRAIT = shrewd OPPOSITE = trusting CHANCE = 25 }", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 8 }",
            gate="diplomacy >= 8", st=S_HUMBLE, ai=35, ai_mod=[("humble", 10), ("calm", 10)]),
          O("Move him to a better-guarded place.",
            GOLD_S, STRESS_DOWN, "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 4 }", st=S_SHREWD, ai=40, ai_mod=[("paranoid", 15)]),
          O("Let him see only what you want him to see.",
            luck("t543w", "He carries home a flattering report", "add_prestige = medium_prestige_gain\nadd_character_modifier = { modifier = eir_foreknowledge_modifier years = 4 }",
                 "t543l", "The boy sees through it", "add_prestige = minor_prestige_loss", p=50, bonus=(20, "intrigue >= 10")),
            gate="OR = {\nintrigue >= 8\nhas_trait = deceitful\n}", st=S_DECEIT, ai=25, ai_mod=[("deceitful", 25)]),
          O("Praise the boy to his father, and send him home early.",
            PRESTIGE_M, "eir_trait_effect = { TRAIT = generous OPPOSITE = greedy CHANCE = 20 }", "add_character_modifier = { modifier = eir_honour_restored_modifier years = 4 }",
            st=S_GEN, ai=30, ai_mod=[("generous", 15), ("trusting", 10)]),
      ],
      "hostage", gate="has_global_variable = eir_done_oenach", cooldown=15)

# =============================================================================
# CEREMONIES OF THE NEW DECISIONS (0544-0567)
# =============================================================================
def ceremony(num, title, summary, body, options, theme="legend", immediate="", variants=None, portraits=""):
    ev(num, title, summary, body, options, theme, guarded=False, immediate=immediate, variants=variants, portraits=portraits)


ceremony(544, "The Oath of the Clan",
         "Your kinsmen have gathered in the dún to swear to you, and they are not all pleased about it.",
         "Four generations of the family, from a white-haired great-uncle to a toddler on his mother's hip. They stand in a ring on the hill and one by one they touch the sword and say the words: loyal to the head of the kindred, until death or exile. Some mean it. Some are already looking at their neighbours to see who is looking.",
         [
             O("Accept each oath with a gift.", PRESTIGE_M, GOLD_S, "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 8 }", "add_character_modifier = { modifier = eir_clan_oath_modifier years = 12 }",
               st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
             O("Take hostages from the doubtful, and trust the rest.", PRESTIGE_S, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_clan_oath_modifier years = 15 }", "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 6 }",
               st=S_HARD, ai=25, ai_mod=[("paranoid", 25), ("callous", 10)]),
             O("Make the oath a feast, and the feast a legend.", PRESTIGE_M, xp("lifestyle_reveler", 25), "add_character_modifier = { modifier = eir_clan_oath_modifier years = 10 }", "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 5 }",
               gate="OR = {\nhas_trait = gregarious\ndiplomacy >= 8\n}", st=S_GEN, ai=35, ai_mod=[("gregarious", 20)]),
             O("Add a verse to the oath that binds the kindred to defend the church.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_clan_oath_modifier years = 12 }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
               st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
         ])

ceremony(545, "The Samhain Feast",
         "On the last night of October, the veil is thin, the fires are lit and every house in the hall is full.",
         "It is the oldest of the festivals: the end of the summer and the beginning of the winter, the night when the dead come back to be fed. The monks call it All Hallows. The farmers call it Samhain. The children call it the night they are allowed to stay up. The ghost-stories begin at midnight.",
         [
             O("Preside over the feast, and tell the oldest story yourself.", PRESTIGE_M, xp("lifestyle_reveler", 30), xp("lifestyle_poet", 15), "add_character_modifier = { modifier = eir_samhain_modifier years = 3 }",
               st=S_GEN, ai=40, ai_mod=[("gregarious", 15), ("generous", 10)]),
             O("Light the bonfire on the hill, and lead the procession.", PRESTIGE_S, PIETY_S, xp("lifestyle_mystic", 20), "capital_county ?= { add_county_modifier = { modifier = eir_samhain_county_modifier years = 3 } }",
               st=S_ZEAL, ai=30, ai_mod=[("zealous", 10), ("brave", 10)]),
             O("Set a place at the table for the ancestors.", PRESTIGE_S, "add_character_modifier = { modifier = eir_ancestors_blessing_modifier years = 4 }", xp("lifestyle_mystic", 25), "add_piety = minor_piety_loss",
               gate="NOT = { has_trait = zealous }", st=S_CYN, ai=25, ai_mod=[("cynical", 15), ("compassionate", 10)]),
             O("Keep it a church feast only: mass, then bed.", PIETY_M, "capital_county ?= { add_county_modifier = { modifier = eir_hedge_schools_modifier years = 3 } }", STRESS_DOWN,
               st=S_ZEAL, ai=20, ai_mod=[("zealous", 25)]),
         ], theme="party")

ceremony(546, "Beating the Bounds",
         "The whole community walks the boundary of your lands, carrying staves and singing.",
         "Every landmark is named: the ash by the ford, the stone with the notches, the pool where the salmon leap. The boys are pushed over a ditch to remember where it is. The old men dispute a boundary-mark that moved three years ago. The priest is blessing the corners. It takes all day.",
         [
             O("Lead the walk yourself, from the first stone to the last.", PRESTIGE_M, "capital_county ?= { add_county_modifier = { modifier = eir_bounds_beaten_modifier years = 10 } }", xp("lifestyle_hunter", 20), "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 3 }",
               st=S_BRAVE, ai=40, ai_mod=[("diligent", 15), ("brave", 10)]),
             O("Let your steward do it, and arrive for the feast.", PRESTIGE_S, GOLD_S, "capital_county ?= { add_county_modifier = { modifier = eir_bounds_beaten_modifier years = 5 } }", STRESS_DOWN,
               st=S_CONTENT, ai=30, ai_mod=[("lazy", 15)]),
             O("Place a new ogham pillar at each corner.", GOLD_M, PRESTIGE_M, "capital_county ?= { add_county_modifier = { modifier = eir_ogham_boundary_modifier years = 20 } }", "add_character_modifier = { modifier = eir_royal_ollamh_modifier years = 4 }",
               gate="gold >= 100", st=S_PATIENT, ai=30, ai_mod=[("diligent", 10)]),
             O("Carry the relics round the bounds, and bless the land.", PIETY_M, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_bounds_beaten_modifier years = 10 } }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }",
               gate="piety >= 80", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
         ], theme="stewardship")

ceremony(547, "Land for the Saint",
         "A saint's disciple has come to claim the land you gave, and he is already marking out a church.",
         "He is young and thin and impossibly cheerful. He has three disciples, a goat and a bell. He says the saint appeared to him on the way here and told him exactly where the altar should go. The spot he has chosen is in the middle of your best field. He asks you very politely to move the field.",
         [
             O("Move the field.", PIETY_L, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_hospice_modifier years = 10 } }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }", GOLD_S,
               st=S_ZEAL, ai=40, ai_mod=[("zealous", 20), ("generous", 10)]),
             O("Suggest an alternative spot, with a spring.", PIETY_M, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_hospice_modifier years = 8 } }", st=S_PATIENT, ai=35, ai_mod=[("patient", 15), ("shrewd", 10)]),
             O("Offer a share of the harvest in exchange for the field.", GOLD_S, PIETY_M, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 4 }", PRESTIGE_S, st=S_GREED, ai=30, ai_mod=[("greedy", 10)]),
             O("Ask the disciple to build the church somewhere else entirely.", STRESS_DOWN, "add_piety = minor_piety_loss", st=S_CYN, ai=10, ai_mod=[("cynical", 20)]),
         ], theme="faith")

ceremony(548, "A Pact with a Neighbouring Sept",
         "The chief of the next valley has come to seal a pact of friendship, and he has brought his best horse.",
         "You have been quarrelling about the same hill for a generation. His grandfather and yours fought a battle over it. Now both of you have grown tired. He has brought a horse, a poet and a very good wine. He says the horse is a gift and the poet is a witness and the wine is for drinking.",
         [
             O("Swear the pact on the relics and exchange fosterlings.", PRESTIGE_M, "add_character_modifier = { modifier = eir_wergild_peace_modifier years = 12 }", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 8 }", PIETY_S,
               gate=FOSTER, st=S_HONEST, ai=40, ai_mod=[("honest", 20), ("trusting", 10)]),
             O("Swear the pact and have the poet record it.", PRESTIGE_M, xp("lifestyle_poet", 20), "add_character_modifier = { modifier = eir_wergild_peace_modifier years = 10 }", "add_hook = { target = scope:eir_pact_chief type = favor_hook }",
               st=S_HUMBLE, ai=35),
             O("Accept the horse and promise nothing.", PRESTIGE_S, "add_character_modifier = { modifier = eir_hunting_hounds_modifier years = 4 }", "scope:eir_pact_chief = { add_opinion = { target = root modifier = eir_slighted_envoy_opinion opinion = -10 } }",
               st=S_DECEIT, ai=15, ai_mod=[("deceitful", 20)]),
             O("Swear it, then plan to break it when you are stronger.", PRESTIGE_S, "add_character_modifier = { modifier = eir_raider_infamy_modifier years = 6 }", "add_character_flag = { flag = eir_oath_to_reclaim years = 8 }",
               gate="OR = {\nhas_trait = deceitful\nhas_trait = ambitious\n}", st=S_DECEIT, ai=15, ai_mod=[("deceitful", 25), ("ambitious", 20)]),
         ], theme="diplomacy", immediate="random_ruler = {\n\tlimit = {\n\t\tis_ai = yes\n\t\tis_ruler = yes\n\t\tculture ?= { has_cultural_pillar = heritage_goidelic }\n\t\tNOT = { this = root }\n\t\tNOT = { is_vassal_of = root }\n\t}\n\tsave_scope_as = eir_pact_chief\n}")

ceremony(549, "The First Dún",
         "The great bank is rising round the new hall, and every farmer within ten miles has come to carry earth.",
         "It is the traditional way. A dún is a community's work, not a lord's. The bank grows by baskets: a thousand baskets a day, carried by every man, woman and child. The timber hall rises on the high ground. The ditch fills with rainwater. When it is finished, nobody will be able to say who built it, and everybody will say they did.",
         [
             O("Work alongside them with a basket.", PRESTIGE_M, "capital_county ?= { add_county_modifier = { modifier = eir_first_dun_modifier years = 15 } }", xp("lifestyle_hunter", 15), "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 4 }",
               st=S_HUMBLE, ai=40, ai_mod=[("humble", 20), ("diligent", 10)]),
             O("Pay the workers in cattle, and have the poets sing as they dig.", GOLD_S, PRESTIGE_M, "capital_county ?= { add_county_modifier = { modifier = eir_first_dun_modifier years = 12 } }", xp("lifestyle_reveler", 15),
               st=S_GEN, ai=35, ai_mod=[("generous", 15)]),
             O("Add a second bank and a palisade.", GOLD_M, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_first_dun_modifier years = 20 } }", "add_character_modifier = { modifier = eir_shield_wall_modifier years = 5 }",
               gate="gold >= 120", st=S_SHREWD, ai=30, ai_mod=[("paranoid", 15)]),
             O("Bury a hoard under the gatepost for luck.", GOLD_S, PIETY_S, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_first_dun_modifier years = 10 } }",
               st=S_ZEAL, ai=25),
         ], theme="stewardship")

ceremony(550, "The Beacon Chain Is Lit",
         "On a still night, the first beacon fire flares on the northern headland, and the next answers it, and the next.",
         "It is a test. The coast has been strung with fire-baskets for forty miles. The watchers have been drilled in the order: a smoke for a single ship, a fire for ten, three fires for a fleet. The first beacon is lit, and the second takes it up, and the third. In seven minutes, the whole coast is bright, and the monks on the hill are watching, bemused.",
         [
             O("Congratulate the watchers, and double the pay.", PRESTIGE_S, GOLD_S, "every_realm_county = {\n\tlimit = { is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_beacon_county_modifier years = 10 }\n}", "add_character_modifier = { modifier = eir_beacons_modifier years = 8 }",
               st=S_GEN, ai=40, ai_mod=[("diligent", 15)]),
             O("Use the beacons for the shipping trade as well.", GAIN_M, "add_character_modifier = { modifier = eir_beacons_modifier years = 6 }", PRESTIGE_S, "every_realm_county = {\n\tlimit = { is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_beacon_county_modifier years = 6 }\n}",
               st=S_SHREWD, ai=35, ai_mod=[("greedy", 10), ("shrewd", 10)]),
             O("Add watchtowers at every second beacon.", GOLD_M, PRESTIGE_S, "every_realm_county = {\n\tlimit = { is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_beacon_county_modifier years = 15 }\n}", "add_character_modifier = { modifier = eir_beacons_modifier years = 10 }",
               gate="gold >= 100", st=S_SHREWD, ai=30),
             O("Ask the monks to bless the fires.", PIETY_M, "add_character_modifier = { modifier = eir_beacons_modifier years = 6 }", PRESTIGE_S, st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
         ], theme="war")

ceremony(551, "The Defensive Compact",
         "The kings of Ireland have sealed a compact against the foreigner, and each has brought his hostage.",
         "It is not an alliance, not exactly. It is a promise that if the Norse land in one kingdom, the others will send men, and that no king will make a separate peace. The oath is sworn on the relics of six saints. The hostages sit at the end of the table, looking pale. The poets are writing down the names, because the poets do not trust anybody to remember.",
         [
             O("Take the chair, and lead the compact.", PRESTIGE_L, "add_character_modifier = { modifier = eir_defensive_compact_modifier years = 15 }", "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 8 }", "eir_world_reacts_effect = yes",
               st=S_ARROG, ai=35, ai_mod=[("ambitious", 20), ("arrogant", 10)]),
             O("Offer the chair to the oldest king, and sit beside him.", PRESTIGE_M, "add_character_modifier = { modifier = eir_defensive_compact_modifier years = 12 }", "eir_vassal_opinion_effect = { MODIFIER = eir_allied_kings_opinion OPINION = 10 }", PIETY_S,
               st=S_HUMBLE, ai=40, ai_mod=[("humble", 20), ("gregarious", 10)]),
             O("Add a clause for shared spoils.", PRESTIGE_S, GAIN_S, "add_character_modifier = { modifier = eir_defensive_compact_modifier years = 10 }", "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }",
               st=S_GREED, ai=30, ai_mod=[("greedy", 15)]),
             O("Have the bishops add a curse for oath-breakers.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_defensive_compact_modifier years = 12 }", "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 6 }",
               gate="piety >= 100", st=S_ZEAL, ai=35, ai_mod=[("zealous", 20)]),
         ], theme="diplomacy")

ceremony(552, "The Norse Fleet Sails Under Your Banner",
         "Forty Norse ships have hoisted your flag, and their captain has asked what you want burned.",
         "He is a Norse-Gael, a man with two names and no particular loyalty. His crews are the best sailors on the coast and the worst guests. They have been paid in silver, in advance, and in promises, later. He has asked you for a target. He has asked it in the tone of a man hoping you will name a rich one.",
         [
             O("Send them against your enemy's coast.", GAIN_M, PRESTIGE_M, "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_norse_fleet_modifier years = 4 }", "add_character_modifier = { modifier = eir_raider_infamy_modifier years = 4 }",
               st=S_WRATH, ai=35, ai_mod=[("wrathful", 15), ("ambitious", 10)]),
             O("Station them off your own coast as a screen.", PRESTIGE_S, "add_character_modifier = { modifier = eir_norse_fleet_modifier years = 6 }", "every_realm_county = {\n\tlimit = { is_coastal_county = yes }\n\tadd_county_modifier = { modifier = eir_beacon_county_modifier years = 6 }\n}",
               st=S_SHREWD, ai=40, ai_mod=[("shrewd", 15)]),
             O("Keep a close hold on their captain's family.", PRESTIGE_S, "add_character_modifier = { modifier = eir_norse_fleet_modifier years = 4 }", "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 4 }",
               st=S_HARD, ai=30, ai_mod=[("paranoid", 20)]),
             O("Pay them off and send them away. They are not worth the trouble.", GOLD_S, STRESS_DOWN, st=S_CRAVEN, ai=15),
         ], theme="war")

ceremony(553, "The Redemption of the Captives",
         "A long line of freed prisoners walks up the road to your hall, thin and blinking.",
         "They were taken in the last raid and held in the Norse slave pens. You paid for them, every one, in silver and in cattle. They are mostly women and children, with a few monks. They have never seen an Irish hall from the front before. The youngest is clinging to a monk's sleeve. Her face is blank.",
         [
             O("Feed them and shelter them as guests of the house.", PIETY_L, PRESTIGE_M, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 8 }", "eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 35 }",
               st=S_KIND, ai=45, ai_mod=[("compassionate", 25), ("generous", 10)]),
             O("Give them land in the settlements near your coast.", PRESTIGE_M, "capital_county ?= { add_county_modifier = { modifier = eir_redeemed_county_modifier years = 15 } }", GAIN_S, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 4 }",
               st=S_SHREWD, ai=30, ai_mod=[("shrewd", 10)]),
             O("Have the monks teach them letters and send them out as missionaries.", PIETY_M, "add_character_modifier = { modifier = eir_missionary_glory_modifier years = 6 }", PRESTIGE_S,
               st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
             O("Ask them for what they learned in the pens.", PRESTIGE_S, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 5 }", xp("lifestyle_traveler", 10),
               gate="OR = {\nintrigue >= 8\nhas_trait = shrewd\n}", st=S_SHREWD, ai=25, ai_mod=[("shrewd", 15)]),
         ], theme="faith")

ceremony(554, "The Yoke Is Broken",
         "The last Norse tax-collector has gone home, and the bells rang for an hour.",
         "You owed them nothing, in the end. The tribute was a bluff, the hostages were a pretext, and the garrison was a fraction of what they claimed. What kept you paying was fear. What ended it was a single afternoon on a hillside when an Irish army stood and did not run. The tax-collector took his ledger and his guards and left, and the crowd did not even jeer.",
         [
             O("Take the name the people are shouting.", "give_nickname = nick_eir_norse_bane", PRESTIGE_L, "eir_end_danegeld_effect = yes", "add_character_modifier = { modifier = eir_yoke_broken_modifier years = 20 }",
               st=S_ARROG, ai=40, ai_mod=[("arrogant", 15), ("brave", 15)]),
             O("Hold a feast for every man who stood on the hill.", PRESTIGE_L, "eir_end_danegeld_effect = yes", "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 10 }", xp("lifestyle_reveler", 30),
               st=S_GEN, ai=35, ai_mod=[("generous", 25)]),
             O("Burn the ledgers and scatter the ashes.", PRESTIGE_M, "eir_end_danegeld_effect = yes", "add_character_modifier = { modifier = eir_yoke_broken_modifier years = 15 }", PIETY_S,
               st=S_WRATH, ai=30, ai_mod=[("wrathful", 15)]),
             O("Offer the Norse a trade treaty. They are not all enemies.", PRESTIGE_M, GAIN_M, "eir_end_danegeld_effect = yes", "add_character_modifier = { modifier = eir_irish_sea_trade_modifier years = 6 }",
               gate="diplomacy >= 10", st=S_SHREWD, ai=25, ai_mod=[("shrewd", 20), ("greedy", 10)]),
         ], theme="legend")

ceremony(555, "The Longphort Burns",
         "Smoke rises from the Norse camp on the river, and the riverbank is lined with cheering men.",
         "It took six weeks and a good many small boats. You came at night, from three directions, and the first the Norse knew of it was a fire in the ship-sheds. They fought well, in the dark. They did not fight well enough. The longphort, which was supposed to stand for a hundred years, burned in a single night.",
         [
             O("Take the ships, and burn the rest.", PRESTIGE_L, GAIN_M, "add_dread = minor_dread_gain", "give_nickname = nick_eir_longphort_burner", "eir_world_reacts_effect = yes",
               st=S_WRATH, ai=40, ai_mod=[("wrathful", 15), ("brave", 15)]),
             O("Take the ships and the surviving Norse as hostages.", PRESTIGE_M, "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 8 }", GAIN_S, "add_dread = minor_dread_gain",
               st=S_SHREWD, ai=35, ai_mod=[("shrewd", 15)]),
             O("Bless the ruins, and build a church on the site.", PIETY_L, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_cairn_county_modifier years = 15 } }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 6 }",
               st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
             O("Offer the survivors a place in your army.", PRESTIGE_S, "add_character_modifier = { modifier = eir_norse_kin_modifier years = 8 }", "add_character_modifier = { modifier = eir_gallowglass_paymaster_modifier years = 6 }",
               st=S_FORGIVE, ai=20, ai_mod=[("forgiving", 20), ("trusting", 10)]),
         ], theme="war")

ceremony(556, "The Ostmen Become Gaels",
         "A Norse-Gael village has held its first Irish assembly, and the speeches were in the old tongue.",
         "It took a generation. The grandfathers spoke Norse, the fathers spoke both, and the children speak Irish with a faint accent that the Irish find charming and the Norse find hilarious. The village headman has taken an Irish name and kept his sword. He says he is a Gael now. He says it a little too loudly.",
         [
             O("Receive their oaths in the hall, as you would any Gael's.", PRESTIGE_M, "add_character_modifier = { modifier = eir_two_peoples_modifier years = 10 }", "capital_county ?= { add_county_modifier = { modifier = eir_ostmen_quarter_modifier years = 15 } }", "eir_resent_clear_effect = yes",
               st=S_FORGIVE, ai=40, ai_mod=[("just", 20), ("forgiving", 15)]),
             O("Take their sons for fosterage, to seal it.", "add_character_modifier = { modifier = eir_foster_bond_modifier years = 12 }", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 5 }",
               gate=FOSTER, st=S_PATIENT, ai=35),
             O("Have the poets compose a verse for the new Gaels.", PRESTIGE_M, xp("lifestyle_poet", 25), "add_character_modifier = { modifier = eir_insular_song_modifier years = 6 }", gate=FILI, st=S_HUMBLE, ai=30),
             O("Keep a close watch. A Norse Gael is still a Norse.", PRESTIGE_S, "add_character_modifier = { modifier = eir_foreknowledge_modifier years = 4 }", STRESS_DOWN, st=S_SHREWD, ai=25, ai_mod=[("paranoid", 20)]),
         ], theme="culture_change",
         variants=[("has_variable = eir_ostmen_fostered", "It took a generation, and the generation was yours. The Norse-Gael boys you fostered in your own hall are the village elders now, and they remember whose table they ate at. The headman has taken an Irish name and kept his sword, and he stands a little straighter when your banner passes.")])

ceremony(557, "The Oath of the Norse-Bane",
         "On the strand where the Black Host fell, you stand before the cairn and swear an oath.",
         "The tide is out. The bones of the burned ships stick up from the sand like a ribcage. The cairn at the top of the beach has a stone for every man who stood. You have a drawn sword, a relic of Colmcille and a vow to make. The vow is simple: that no raider will land on this coast and live to boast of it. The wind takes the words away.",
         [
             O("Swear the oath for yourself and your heirs.", "give_nickname = nick_eir_norse_bane", PRESTIGE_L, PIETY_M, "add_character_modifier = { modifier = eir_norse_bane_oath_modifier years = 30 }", "dynasty ?= { add_dynasty_modifier = { modifier = eir_house_norse_bane_modifier years = 50 } }",
               st=S_WRATH, ai=40, ai_mod=[("vengeful", 20), ("brave", 15)]),
             O("Swear it on the relic, and add a vow of hospitality to the monks.", PIETY_L, PRESTIGE_M, "add_character_modifier = { modifier = eir_norse_bane_oath_modifier years = 25 }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 8 }",
               gate="piety >= 150", st=S_ZEAL, ai=35, ai_mod=[("zealous", 25)]),
             O("Swear it quietly, and let the deed speak.", PRESTIGE_M, "add_character_modifier = { modifier = eir_norse_bane_oath_modifier years = 20 }", STRESS_DOWN,
               st=S_HUMBLE, ai=25, ai_mod=[("humble", 20)]),
             O("Have the poets sing the oath, and every king hear it.", PRESTIGE_L, "eir_legend_defence_effect = yes", xp("lifestyle_poet", 30), "add_character_modifier = { modifier = eir_norse_bane_oath_modifier years = 25 }",
               "eir_world_reacts_effect = yes", gate=FILI, st=S_ARROG, ai=35, ai_mod=[("ambitious", 15)]),
         ])

ceremony(558, "The Walled Town",
         "A walled town rises where the longphort stood, and it has a market, a church and a gate.",
         "It is the first walled town in Ireland that was not built by foreigners. The walls are earth and timber, with a stone gatehouse and a harbour boom. A bishop has blessed the cornerstone. A merchant from Chester has taken a stall. The poet who is composing the dedication has been told not to mention the Norse. He has composed it anyway.",
         [
             O("Charter the town with its own laws and its own market.", PRESTIGE_M, "capital_county ?= { add_county_modifier = { modifier = eir_chartered_town_modifier years = 20 } }", GAIN_M, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 4 }",
               st=S_SHREWD, ai=40, ai_mod=[("shrewd", 15), ("diligent", 10)]),
             O("Fill it with a royal garrison.", PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_walled_town_modifier years = 20 } }", "add_dread = minor_dread_gain",
               st=S_HARD, ai=30, ai_mod=[("paranoid", 15)]),
             O("Invite the Norse merchants to settle, under Irish law.", GAIN_M, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_ostmen_quarter_modifier years = 20 } }", "add_character_modifier = { modifier = eir_irish_sea_trade_modifier years = 6 }",
               st=S_FORGIVE, ai=30, ai_mod=[("greedy", 10), ("forgiving", 10)]),
             O("Name it for a saint, and dedicate the first church to her.", PIETY_M, PRESTIGE_S, "capital_county ?= { add_county_modifier = { modifier = eir_walled_town_modifier years = 15 } }", "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 5 }",
               st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
         ], theme="stewardship")

ceremony(559, "The Cairn of the Fallen",
         "Every family that lost a son in the war has brought a stone, and the cairn has grown to the height of a man.",
         "The names are cut into a flat slab at the foot, in ogham and in Latin. There are three hundred and eleven. The mothers walk up one at a time and lay their stones without speaking. A harper plays a single note and holds it. The wind off the sea takes it up the hill and over the crest, and the whole mourning crowd turns to listen.",
         [
             O("Place the last stone yourself, with the name of your own dead.", PRESTIGE_M, PIETY_M, "capital_county ?= { add_county_modifier = { modifier = eir_cairn_county_modifier years = 25 } }", "eir_trait_effect = { TRAIT = compassionate OPPOSITE = callous CHANCE = 30 }",
               st=S_KIND, ai=45, ai_mod=[("compassionate", 25), ("humble", 10)]),
             O("Endow a chantry to pray for them forever.", GOLD_M, PIETY_L, "add_character_modifier = { modifier = eir_saints_blessing_modifier years = 10 }", "capital_county ?= { add_county_modifier = { modifier = eir_cairn_county_modifier years = 20 } }",
               gate="gold >= 100", st=S_ZEAL, ai=30, ai_mod=[("zealous", 20)]),
             O("Pay a pension to every widow.", GOLD_M, PRESTIGE_M, "eir_court_opinion_effect = { MODIFIER = eir_hospitality_opinion OPINION = 8 }", "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 5 }",
               gate="gold >= 120", st=S_GEN, ai=35, ai_mod=[("generous", 25)]),
             O("Make the cairn a rallying place for the next war.", PRESTIGE_M, "add_dread = minor_dread_gain", "capital_county ?= { add_county_modifier = { modifier = eir_cairn_county_modifier years = 20 } }", "add_character_modifier = { modifier = eir_war_poem_modifier years = 6 }",
               st=S_WRATH, ai=25, ai_mod=[("wrathful", 15), ("vengeful", 15)]),
         ], theme="legend")

ceremony(560, "The Victory Song",
         "The poets of five provinces have gathered to sing the song of the war, and they have agreed on almost nothing.",
         "One says the battle was won at the ford. Another says it was won on the hill. A third says it was won in a dream, and a fourth says it was won on the strand by a single man with a stick. They have been arguing since noon. A harper has played the same chord eighteen times to get their attention.",
         [
             O("Let the best poet compose it, and the others witness.", PRESTIGE_L, xp("lifestyle_poet", 40), "eir_legend_defence_effect = yes", "add_character_modifier = { modifier = eir_war_poem_modifier years = 8 }",
               st=S_HUMBLE, ai=40, ai_mod=[("humble", 15)]),
             O("Have it composed in four versions, one for each province.", PRESTIGE_M, "eir_world_reacts_effect = yes", GOLD_S, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 5 }",
               st=S_GEN, ai=35, ai_mod=[("generous", 15), ("gregarious", 10)]),
             O("Insist that your own deeds take the centre of the song.", PRESTIGE_L, "add_character_modifier = { modifier = eir_false_pedigree_modifier years = 4 }", xp("lifestyle_poet", 10),
               st=S_ARROG, ai=30, ai_mod=[("arrogant", 25)]),
             O("Ask them to sing it without any names, so all may claim it.", PRESTIGE_M, PIETY_S, "add_character_modifier = { modifier = eir_insular_song_modifier years = 8 }",
               st=S_HUMBLE, ai=25, ai_mod=[("humble", 25)]),
         ])

ceremony(561, "The Genealogy Is Read",
         "The chief poet unrolls the new genealogy of your house, and the hall goes very quiet.",
         "It is a beautiful work, with twelve generations in perfect order, a descent from a high king of the seventh century, and an unusually good claim to a kingdom you do not currently hold. The poet has been paid well. The poet has also, in several places, improved the facts. Whether anybody will notice depends on how many other poets are in the room.",
         [
             O("Accept it and put it on display.", PRESTIGE_M, "add_character_modifier = { modifier = eir_pedigree_proclaimed_modifier years = 10 }", "add_character_flag = { flag = eir_oath_to_reclaim years = 10 }",
               "eir_trait_effect = { TRAIT = arrogant OPPOSITE = humble CHANCE = 15 }", st=S_ARROG, ai=40, ai_mod=[("arrogant", 20), ("ambitious", 15)]),
             O("Have the monks check the dates and correct the worst of it.", PIETY_S, PRESTIGE_M, "add_character_modifier = { modifier = eir_pedigree_proclaimed_modifier years = 8 }", xp("lifestyle_poet", 15),
               gate="learning >= 9", st=S_HONEST, ai=35, ai_mod=[("honest", 25)]),
             O("Show it only to your friends.", PRESTIGE_S, "add_character_modifier = { modifier = eir_pedigree_proclaimed_modifier years = 5 }", STRESS_DOWN,
               st=S_DECEIT, ai=30, ai_mod=[("deceitful", 15), ("shrewd", 10)]),
             O("Stake a claim on it before a rival's poets do the same.", PRESTIGE_M, "add_character_flag = { flag = eir_oath_to_reclaim years = 12 }", "eir_grant_claims_norse_effect = yes",
               "add_character_modifier = { modifier = eir_false_pedigree_modifier years = 4 }", gate="eir_stage1_trigger = yes", st=S_AMBIT, ai=30, ai_mod=[("ambitious", 25)]),
         ], theme="learning")

ceremony(562, "Hostages from the Rival",
         "A rival king's sons have been brought to your hall, and they refuse to speak to you.",
         "They are fourteen and twelve. They have been told that this is an honour, and that it is temporary, and that their father will be back with an army in a year. They have been told many things. They sit in the corner with their arms folded and watch your servants carry in the food. The younger one is clearly hoping you will make a mistake.",
         [
             O("Treat them as guests of honour.", PRESTIGE_M, "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 10 }", "add_character_modifier = { modifier = eir_hospitality_modifier years = 6 }", xp("lifestyle_reveler", 10),
               st=S_GEN, ai=40, ai_mod=[("generous", 15), ("compassionate", 10)]),
             O("Keep them in a tower, and keep the key.", "add_dread = minor_dread_gain", PRESTIGE_S, "add_character_modifier = { modifier = eir_hostage_peace_modifier years = 8 }", "eir_trait_effect = { TRAIT = callous OPPOSITE = compassionate CHANCE = 20 }",
               st=S_HARD, ai=25, ai_mod=[("paranoid", 20), ("callous", 15)]),
             O("Foster them with your own children.", PRESTIGE_S, "add_character_modifier = { modifier = eir_foster_bond_modifier years = 12 }", "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 4 }",
               gate=FOSTER, st=S_KIND, ai=35),
             O("Return the elder to his father as a sign of goodwill.", PRESTIGE_M, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 5 }", "eir_trait_effect = { TRAIT = forgiving OPPOSITE = vengeful CHANCE = 20 }",
               st=S_FORGIVE, ai=20, ai_mod=[("forgiving", 25)]),
         ], theme="hostage")

ceremony(563, "The Judgement of the King",
         "Two septs have laid their quarrel before you, and the brehons are waiting to hear your reasoning.",
         "It is a very old right: the high king hears the quarrels the lesser kings cannot settle. The case is a hill, a well, a boundary-stone and a woman who is married to the sons of both. The brehons have taken their seats on either side of you and are watching you closely. A king who gets this wrong is never forgotten.",
         [
             O("Cite the law, case by case, and make the judgement binding.", PRESTIGE_M, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 6 }", "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 30 }", "add_character_modifier = { modifier = eir_fair_lord_modifier years = 6 }",
               gate="learning >= 9", st=S_PATIENT, ai=40, ai_mod=[("just", 25)]),
             O("Split the difference and send them home friends.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 3 }", "add_character_modifier = { modifier = eir_wergild_peace_modifier years = 5 }",
               st=S_FORGIVE, ai=40, ai_mod=[("patient", 10), ("forgiving", 10)]),
             O("Take a fee from both sides and judge for the higher bidder.", GAIN_M, "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = -6 }", "eir_trait_effect = { TRAIT = arbitrary OPPOSITE = just CHANCE = 25 }",
               st=S_GREED, ai=15, ai_mod=[("greedy", 25), ("arbitrary", 15)]),
             O("Hand the case to the Church.", PIETY_M, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 4 }", STRESS_DOWN, st=S_ZEAL, ai=25),
         ], theme="court")

ceremony(564, "The Blood Feud Ends",
         "The two families have sat down at one table for the first time in forty years.",
         "It began over a cow. By the time anyone remembered what, there were seventeen graves. The matriarchs of both houses have come to the hall and said, very quietly, that they would like it to stop. Nobody has argued. The two heads of house are shaking hands over a bowl of milk and honey, and they are not looking at each other.",
         [
             O("Pay the eric yourself, to both houses.", GOLD_M, PRESTIGE_L, "add_character_modifier = { modifier = eir_honour_restored_modifier years = 10 }", "eir_trait_effect = { TRAIT = just OPPOSITE = arbitrary CHANCE = 30 }",
               gate="gold >= 150", st=S_GEN, ai=40, ai_mod=[("generous", 20), ("just", 15)]),
             O("Seal it with a marriage and a fosterage.", PRESTIGE_M, "add_character_modifier = { modifier = eir_wergild_peace_modifier years = 15 }", "eir_vassal_opinion_effect = { MODIFIER = eir_justice_done_opinion OPINION = 8 }",
               st=S_SHREWD, ai=35, ai_mod=[("shrewd", 10)]),
             O("Have the poets compose the peace.", PRESTIGE_M, xp("lifestyle_poet", 25), "add_character_modifier = { modifier = eir_wergild_peace_modifier years = 10 }", gate=FILI, st=S_HUMBLE, ai=30),
             O("Swear the peace on the relics and fine the first to break it.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 8 }", "add_character_modifier = { modifier = eir_wergild_peace_modifier years = 8 }",
               gate="piety >= 80", st=S_ZEAL, ai=35, ai_mod=[("zealous", 20)]),
         ], theme="family")

ceremony(565, "The Royal Stud",
         "The first foals of the royal stud are on their feet, and the grooms are looking at them with the expression of men who know what they have.",
         "Irish hobbies are small and fast and as sure-footed as goats. The best of them have been bred for centuries on the hill pastures of Meath and Munster. You have bought a stallion from a famous line, mares from three provinces and the full-time services of a man who talks to horses. The foals are small, grey and ridiculous. They will be magnificent.",
         [
             O("Keep the best for your own household.", PRESTIGE_M, "add_character_modifier = { modifier = eir_royal_stud_modifier years = 15 }", xp("lifestyle_hunter", 20),
               st=S_ARROG, ai=35, ai_mod=[("arrogant", 10), ("brave", 10)]),
             O("Give a foal to each vassal who rode with you.", PRESTIGE_S, "eir_vassal_opinion_effect = { MODIFIER = eir_shared_spoils_opinion OPINION = 6 }", "add_character_modifier = { modifier = eir_royal_stud_modifier years = 12 }",
               st=S_GEN, ai=40, ai_mod=[("generous", 20)]),
             O("Sell the surplus to the English at a great price.", GAIN_M, "add_character_modifier = { modifier = eir_royal_stud_modifier years = 10 }", PRESTIGE_S,
               st=S_GREED, ai=30, ai_mod=[("greedy", 20)]),
             O("Race them at the next Aonach and let the prizes decide.", PRESTIGE_M, xp("lifestyle_reveler", 20), "add_character_modifier = { modifier = eir_royal_stud_modifier years = 10 }", GAIN_S,
               st=S_GEN, ai=30, ai_mod=[("gregarious", 10)]),
         ], theme="hunting")

ceremony(566, "The Law of Kinship",
         "The elders of the clan have met under the old oak to write down the law of kin, and they have taken three days to agree on the first line.",
         "It has been carried by memory for a thousand years. Who is a kinsman, who owes what, who pays for a death, who inherits a debt: the poets know, the brehons know, and the old women know, and none of them agree. The kinsmen have gathered in a ring. The scribe is sharpening his quills. The first line is: 'A man is his kindred.'",
         [
             O("Proclaim the law, with the king's seal on the first page.", PRESTIGE_L, "add_character_modifier = { modifier = eir_kinship_law_modifier years = 20 }", "eir_vassal_opinion_effect = { MODIFIER = eir_oath_sworn_opinion OPINION = 8 }",
               xp("lifestyle_poet", 15), st=S_ARROG, ai=40, ai_mod=[("ambitious", 15), ("just", 15)]),
             O("Leave the law as an oral tradition, and bless the memory.", PRESTIGE_S, PIETY_S, "add_character_modifier = { modifier = eir_kinship_law_modifier years = 12 }", xp("lifestyle_mystic", 15),
               st=S_HUMBLE, ai=30, ai_mod=[("humble", 20)]),
             O("Add a clause that protects the fostered.", PRESTIGE_M, "add_character_modifier = { modifier = eir_kinship_law_modifier years = 15 }", "eir_vassal_opinion_effect = { MODIFIER = eir_fostered_opinion OPINION = 5 }",
               st=S_KIND, ai=35, ai_mod=[("compassionate", 15)]),
             O("Add a clause that lets the strongest branch lead the clan.", PRESTIGE_S, "add_character_modifier = { modifier = eir_kinship_law_modifier years = 10 }", "add_dread = minor_dread_gain", "add_character_modifier = { modifier = eir_kin_distrust_modifier years = 6 }",
               st=S_HARD, ai=20, ai_mod=[("ambitious", 15), ("callous", 10)]),
         ], theme="court")

ceremony(567, "The Law of the Sword and the Clan",
         "The war-leaders of the clans have met in the great hall to write the law of the warband, and nobody is armed.",
         "It is the oldest document in Gaelic Scotland, and it has never been written down. How a clan raises its men. How a war-leader earns his place. How booty is divided. What happens to the man who runs. The captains sit in a circle on the floor. The scribe has been warned that if he changes a word he will be fed to the dogs.",
         [
             O("Write the law as the captains dictate.", PRESTIGE_M, "add_character_modifier = { modifier = eir_clan_war_law_modifier years = 20 }", "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = 6 }", xp("lifestyle_blademaster", 20),
               st=S_BRAVE, ai=40, ai_mod=[("brave", 15)]),
             O("Add a clause for the protection of non-combatants and churches.", PIETY_M, PRESTIGE_S, "add_character_modifier = { modifier = eir_clan_war_law_modifier years = 15 }", "add_character_modifier = { modifier = eir_peace_with_church_modifier years = 6 }",
               gate="piety >= 80", st=S_ZEAL, ai=30, ai_mod=[("zealous", 15), ("compassionate", 15)]),
             O("Add a clause that gives the king a fifth of all spoil.", GAIN_M, "add_character_modifier = { modifier = eir_clan_war_law_modifier years = 12 }", "eir_vassal_opinion_effect = { MODIFIER = eir_hosting_opinion OPINION = -3 }",
               st=S_GREED, ai=25, ai_mod=[("greedy", 20)]),
             O("Burn the first draft and write it again from memory.", PRESTIGE_S, "add_character_modifier = { modifier = eir_clan_war_law_modifier years = 12 }", xp("lifestyle_poet", 15), STRESS_UP,
               st=S_PATIENT, ai=25, ai_mod=[("patient", 15)]),
         ], theme="martial")
