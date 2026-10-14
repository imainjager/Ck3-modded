"""Update 8, stage 1: the data for the six Irish activities.
Each activity: key, name, desc, shown (host trigger), start (extra can_start trigger), weeks (length of the active phase), months before start,
max guests, cooldown years, scale options (3), focus options (3), intents (3), pulses (8-9), flavor strings.

A pulse is (key, title, icon, weight, who-limit, effect on scope:first, focus_boost) where focus_boost = (option key, extra weight) or None.
A pulse may be negative: those carry a cost (the 40% rule)."""

ACTS = {}

# Reward scale by option (prestige, piety, gold-ish) and per-guest opinion; used by the generator
SCALES = [("modest", "Modest", 1, "A small gathering, a few cattle and a few kegs."),
          ("fair", "Full", 2, "A proper gathering with a hall, a field and a feast."),
          ("grand", "Grand", 3, "The whole province comes, with all the cattle it can spare.")]


def A(key, **kw):
    ACTS[key] = dict(key=key, **kw)


# ---------------------------------------------------------------------------------------------------------------- 1 ÓENACH
A("oenach", name="Óenach", icon="decision_golden_age",
  desc="The great assembly of a kingdom: a fair, a court, a race-course and a marriage market on one field. Kings preside, brehons judge, poets recite, and everyone, everywhere, trades something.",
  selection="Hold an assembly of the whole province on a hill.\n\nAnticipated Rewards:\n$BULLET_WITH_TAB$[prestige_i][prestige|E]\n$BULLET_WITH_TAB$Vassal and guest [opinion|E]\n$BULLET_WITH_TAB$Settled quarrels",
  host_desc="$BULLET_WITH_TAB$Gain [prestige_i][prestige|E]\n$BULLET_WITH_TAB$Guests may gain [opinion|E] of you\n$BULLET_WITH_TAB$A brawl or a rivalry may break out",
  guest_desc="$BULLET_WITH_TAB$You may gain [prestige_i][prestige|E] or lose [stress_i][stress|E]\n$BULLET_WITH_TAB$You may take part in a lawsuit, a race or a courtship",
  guest_help="Every lord of the province may come with his household. The assembly is at once a court, a fair and a festival, and nobody leaves without a grievance, a bargain or a husband.",
  phase="The Assembly", phase_desc="Law-cases at dawn, horse-races at noon, poetry at dusk. The field never really goes quiet.",
  shown="eir_act_gael_host_trigger = yes", shown_text="You are a ruler of a Gaelic or Brythonic culture",
  start="highest_held_title_tier >= tier_county", weeks=3, wait=2, guests=40, cooldown=5, ai_desc="",
  scale_name="Size of the Assembly", scale_desc="How many come and how long the fair lasts.",
  focus_name="Heart of the Assembly", focus=[
      ("law", "The Court", "The brehons sit from dawn, and every dispute in the province is heard.", "justice_intent"),
      ("games", "The Games", "Races, wrestling and the great horse-fair draw the young men from every glen.", "intent_gain_renown"),
      ("market", "The Fair", "Cattle, hides, silver and salt change hands in the lanes between the tents.", "intent_matchmaking")],
  intents=[("judgement", "Seek Judgement", "Bring a quarrel before the brehons of the Óenach and walk away with a ruling.", "justice_intent"),
           ("renown", "Win Renown at the Games", "Ride, wrestle or recite for the glory of your name.", "intent_gain_renown"),
           ("match", "Arrange a Match", "Where better to find a husband for a daughter than a field full of well-fed sons.", "intent_matchmaking")],
  pulses=[
      ("eir_oenach_lawsuit", "[first.GetShortUIName|U] Won a Lawsuit Before the Brehons", "positive", 1.2, "is_adult = yes", "add_prestige = minor_prestige_gain\nadd_stress = minor_stress_loss", ("law", 1.5)),
      ("eir_oenach_race", "[first.GetShortUIName|U] Won the Great Horse Race", "positive", 1.2, "is_adult = yes\nprowess >= 6", "add_prestige = medium_prestige_gain", ("games", 1.5)),
      ("eir_oenach_poem", "[first.GetShortUIName|U] Recited a Poem to the Whole Field", "positive", 1.0, "is_adult = yes\nlearning >= 6", "add_prestige = minor_prestige_gain\nadd_trait_xp = { trait = lifestyle_poet value = 15 }", None),
      ("eir_oenach_match", "[first.GetShortUIName|U] Arranged a Betrothal at the Fair", "positive", 1.0, "is_adult = yes\nis_ai = yes", "add_gold = minor_gold_value\nadd_stress = minor_stress_loss", ("market", 1.5)),
      ("eir_oenach_cattle", "[first.GetShortUIName|U] Sold a Herd at a Fine Price", "positive", 1.0, "is_adult = yes\nis_ai = yes", "add_gold = medium_gold_value", ("market", 1.8)),
      ("eir_oenach_brawl", "[first.GetShortUIName|U] Started a Brawl Over a Cow", "negative", 1.0, "is_adult = yes\nNOT = { has_trait = calm }", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain\nadd_opinion = { target = scope:host modifier = eir_act_brawl_opinion opinion = -10 }", None),
      ("eir_oenach_insult", "[first.GetShortUIName|U] Felt Slighted by the Seating", "negative", 0.8, "is_adult = yes\nhas_trait = arrogant", "add_stress = minor_stress_gain\nadd_opinion = { target = scope:host modifier = eir_act_insulted_opinion opinion = -10 }", None),
      ("eir_oenach_thief", "[first.GetShortUIName|U] Lost Silver to a Pickpocket", "negative", 0.8, "is_adult = yes\nis_ai = yes", "remove_short_term_gold = minor_gold_value\nadd_stress = minor_stress_gain", None),
      ("eir_oenach_fires", "[first.GetShortUIName|U] Sat Late by the Fires", "positive", 0.8, "is_adult = yes", "add_stress = medium_stress_loss", None)])

# ---------------------------------------------------------------------------------------------------------------- 2 SEASONAL FESTIVAL
A("festival", name="Quarter-Day Festival", icon="decision_golden_age",
  desc="The Celtic year turns on four fires: Samhain, Imbolc, Beltane and Lughnasa. A ruler who holds the fire holds the people: the feast is hers to give, the omens are hers to read.",
  selection="Light the fire of the season with your whole household.\n\nAnticipated Rewards:\n$BULLET_WITH_TAB$[stress_loss_i][stress|E] loss\n$BULLET_WITH_TAB$[piety_i][piety|E] or [prestige_i][prestige|E]\n$BULLET_WITH_TAB$Omens that colour the year",
  host_desc="$BULLET_WITH_TAB$Gain [piety_i][piety|E] and [prestige_i][prestige|E]\n$BULLET_WITH_TAB$Guests lose [stress_i][stress|E]\n$BULLET_WITH_TAB$An omen may help or hinder",
  guest_desc="$BULLET_WITH_TAB$You may lose [stress_i][stress|E]\n$BULLET_WITH_TAB$You may see a vision, or a bad omen",
  guest_help="The fires are lit on the hills at dusk, and every household that can walk to them does. A ruler of the Celtic stock can host in any faith, but the monks and the druids will each say what they think.",
  phase="The Fires", phase_desc="Hearths are put out and lit again from the great fire. The rest of the night is for song, mead and speaking to the dead.",
  shown="eir_act_gael_host_trigger = yes", shown_text="You are a ruler of a Gaelic or Brythonic culture",
  start="highest_held_title_tier >= tier_county", weeks=2, wait=1, guests=25, cooldown=3, ai_desc="",
  scale_name="Size of the Festival", scale_desc="How many fires are lit and how much is feasted.",
  focus_name="The Season", focus=[
      ("samhain", "Samhain", "The veil is thin and the dead sit at the table. Winter begins, and a harvest of herds is brought in or slain.", "intent_mystic"),
      ("beltane", "Beltane", "Cattle are driven between two fires for luck, and young couples slip off into the May night.", "intent_revelry"),
      ("lughnasa", "Lughnasa", "The first fruits, the games of Tailtiu, and the great fairs of the harvest.", "intent_gain_renown")],
  intents=[("omen", "Read the Omens", "Watch the smoke, the birds and the sparks, and say what they mean.", "intent_mystic"),
           ("revel", "Revel Until Dawn", "Drink, dance and forget the year.", "intent_revelry"),
           ("blessing", "Seek the Season's Blessing", "Carry a brand from the great fire to your own hearth.", "pious_intent")],
  pulses=[
      ("eir_festival_bonfire", "[first.GetShortUIName|U] Leapt the Bonfire", "positive", 1.2, "is_adult = yes\nprowess >= 5", "add_prestige = minor_prestige_gain\nadd_stress = minor_stress_loss", None),
      ("eir_festival_vision", "[first.GetShortUIName|U] Saw a Vision in the Smoke", "positive", 1.0, "is_adult = yes", "add_trait_xp = { trait = lifestyle_mystic value = 20 }\nadd_stress = minor_stress_loss", ("samhain", 1.8)),
      ("eir_festival_couple", "[first.GetShortUIName|U] Slipped Away With a Sweetheart", "positive", 1.0, "is_adult = yes\nis_married = no", "add_stress = medium_stress_loss", ("beltane", 1.8)),
      ("eir_festival_games", "[first.GetShortUIName|U] Won the Games of the Harvest", "positive", 1.0, "is_adult = yes\nprowess >= 6", "add_prestige = medium_prestige_gain", ("lughnasa", 1.8)),
      ("eir_festival_priest", "[first.GetShortUIName|U] Blessed the Fire in the Old Words", "positive", 0.9, "is_adult = yes\npiety >= 10", "add_piety = medium_piety_gain", None),
      ("eir_festival_scold", "[first.GetShortUIName|U] Was Scolded by a Priest for the Revels", "negative", 0.9, "is_adult = yes\nis_ai = yes", "add_piety = minor_piety_loss\nadd_stress = minor_stress_gain", None),
      ("eir_festival_blaze", "A Spark Set a Barn Alight", "negative", 0.7, "is_adult = yes\nis_ai = yes", "add_stress = minor_stress_gain\nremove_short_term_gold = minor_gold_value", None),
      ("eir_festival_ghost", "[first.GetShortUIName|U] Glimpsed a Dead Kinsman at the Edge of the Light", "negative", 0.8, "is_adult = yes\nNOT = { has_trait = brave }", "add_stress = medium_stress_gain", ("samhain", 1.5)),
      ("eir_festival_dance", "[first.GetShortUIName|U] Danced Until the Candles Failed", "positive", 0.9, "is_adult = yes", "add_stress = minor_stress_loss", None)])

# ---------------------------------------------------------------------------------------------------------------- 3 FEIS OF TARA
A("feis", name="Feis of Tara", icon="decision_found_kingdom",
  desc="The oldest feast in Ireland: held at Tara, in the hall of the High Kings, by a king who means to be believed. The provincial kings come, or they do not, and the whole island knows which.",
  selection="Hold the great feast of the High Kingship.\n\nAnticipated Rewards:\n$BULLET_WITH_TAB$[legitimacy_i][legitimacy|E] and [prestige_i][prestige|E]\n$BULLET_WITH_TAB$Provincial kings sworn in\n$BULLET_WITH_TAB$Risk of an insult in the hall",
  host_desc="$BULLET_WITH_TAB$Gain [legitimacy_i][legitimacy|E] and [prestige_i][prestige|E]\n$BULLET_WITH_TAB$Guests gain [opinion|E] of you\n$BULLET_WITH_TAB$A rival may defy you at the board",
  guest_desc="$BULLET_WITH_TAB$You may gain [prestige_i][prestige|E]\n$BULLET_WITH_TAB$You may be seated above or below your station",
  guest_help="The kings of Ireland sit in order, each in the place his ancestors held. Whoever the host seats where is a statement, and whoever refuses a seat is making one.",
  phase="The Feis", phase_desc="Seven nights in the hall at Tara, with the kings seated by rank and the poets reciting their genealogies.",
  shown="eir_act_feis_host_trigger = yes", shown_text="You are an Irish king who holds a county in Ireland",
  start="eir_irish_king_trigger = yes", weeks=3, wait=3, guests=50, cooldown=10, ai_desc="",
  scale_name="Splendour of the Feis", scale_desc="How many kings are summoned and how lavish the board.",
  focus_name="Order of the Hall", focus=[
      ("precedence", "Seating by Precedence", "Each king sits where his fathers sat. It is slow, correct and faintly insulting to the new men.", "justice_intent"),
      ("favour", "Seating by Favour", "The friends of the host sit at the top. The rest will remember.", "favoritism_intent"),
      ("oaths", "The Oath-Taking", "The kings swear on the relics of the saints to the High King's peace.", "pious_intent")],
  intents=[("fealty", "Take the Kings' Oath", "Make every provincial king swear to your peace.", "support_liege_intent"),
           ("genealogy", "Have Your Descent Recited", "Hear the poets give the line from Míl to you.", "intent_spread_legend"),
           ("peace", "Broker a Peace", "End a quarrel between two of the great houses under the roof of Tara.", "justice_intent")],
  pulses=[
      ("eir_feis_oath", "[first.GetShortUIName|U] Swore on the Relics to the High King's Peace", "positive", 1.2, "is_adult = yes\nis_ai = yes", "add_prestige = minor_prestige_gain\nadd_opinion = { target = scope:host modifier = eir_act_hosted_opinion opinion = 10 }", ("oaths", 1.6)),
      ("eir_feis_seat", "[first.GetShortUIName|U] Was Given the Seat of Honour", "positive", 1.0, "is_adult = yes\nis_ai = yes", "add_prestige = medium_prestige_gain\nadd_opinion = { target = scope:host modifier = eir_act_hosted_opinion opinion = 10 }", ("favour", 1.6)),
      ("eir_feis_genealogy", "The Poets Recited the Descent of [first.GetShortUIName|U]", "positive", 1.0, "is_adult = yes", "add_prestige = minor_prestige_gain", None),
      ("eir_feis_judgement", "[first.GetShortUIName|U] Settled a Quarrel in the Hall", "positive", 1.0, "is_adult = yes\ndiplomacy >= 8", "add_prestige = minor_prestige_gain\nadd_stress = minor_stress_loss", ("precedence", 1.5)),
      ("eir_feis_harp", "[first.GetShortUIName|U] Played for the Kings", "positive", 0.8, "is_adult = yes\nlearning >= 6", "add_prestige = minor_prestige_gain\nadd_trait_xp = { trait = lifestyle_poet value = 15 }", None),
      ("eir_feis_snub", "[first.GetShortUIName|U] Refused the Seat Offered", "negative", 1.0, "is_adult = yes\nis_ai = yes\nhas_trait = arrogant", "add_prestige = minor_prestige_loss\nadd_opinion = { target = scope:host modifier = eir_act_insulted_opinion opinion = -10 }", ("favour", 1.5)),
      ("eir_feis_feud", "Two Houses Drew Knives Beneath the Roof of Tara", "negative", 0.8, "is_adult = yes\nis_ai = yes\nNOT = { has_trait = calm }", "add_stress = minor_stress_gain\nadd_opinion = { target = scope:host modifier = eir_act_brawl_opinion opinion = -10 }", ("favour", 1.5)),
      ("eir_feis_cost", "The Board Ran Short of Beef", "negative", 0.7, "is_adult = yes\nis_ai = yes", "add_stress = minor_stress_gain\nremove_short_term_gold = minor_gold_value", None),
      ("eir_feis_poem", "A Poem to the Kingship Was Recited Beneath the Hill", "positive", 0.9, "is_adult = yes", "add_stress = minor_stress_loss\nadd_prestige = minor_prestige_gain", None)])

# ---------------------------------------------------------------------------------------------------------------- 4 PILGRIMAGE
A("pilgrimage", name="Irish Pilgrimage", icon="decision_personal_religious",
  desc="The Irish saints made the sea their desert and the mountain their cell. The pilgrim climbs Croagh Patrick on bare feet, rows to Skellig Michael, or spends three days in the cave of Lough Derg, and comes back changed.",
  selection="Take the road of the saints, barefoot.\n\nAnticipated Rewards:\n$BULLET_WITH_TAB$[piety_i][piety|E]\n$BULLET_WITH_TAB$[stress_loss_i][stress|E] loss\n$BULLET_WITH_TAB$A vision, a miracle or a hard road",
  host_desc="$BULLET_WITH_TAB$Gain [piety_i][piety|E]\n$BULLET_WITH_TAB$May lose [stress_i][stress|E]\n$BULLET_WITH_TAB$The road is hard, and a pilgrim may be hurt",
  guest_desc="$BULLET_WITH_TAB$You may gain [piety_i][piety|E]\n$BULLET_WITH_TAB$You may help, or be helped, along the way",
  guest_help="Pilgrims go in small companies and ask no questions. Friends, confessors, penitents and those who have simply nothing better to do are all welcome on the road.",
  phase="The Pilgrimage", phase_desc="Fasting, barefoot walking and long silences, with the mountain or the sea at the end.",
  shown="eir_act_pilgrim_host_trigger = yes", shown_text="You are a ruler of the Gaelic or Brythonic stock who follows a faith in which pilgrimage matters",
  start="piety >= 0", weeks=3, wait=1, guests=12, cooldown=4, ai_desc="",
  scale_name="Company of the Pilgrimage", scale_desc="How large a company and how much alms you carry.",
  focus_name="The Shrine", focus=[
      ("croagh", "Croagh Patrick", "The sharp mountain of Mayo where Patrick fasted forty days, climbed barefoot on loose stone.", "pious_intent"),
      ("skellig", "Skellig Michael", "A rock in the Atlantic, six hundred steps from the sea, with beehive cells for the brave.", "intent_mystic"),
      ("derg", "Lough Derg", "Three days of fasting, wakefulness and walking in a ring of stones, to see the pit of Purgatory.", "intent_mystic")],
  intents=[("penance", "Do Penance", "Carry a sin to the saints and leave it there.", "pious_intent"),
           ("vision", "Seek a Vision", "Fast until the world turns thin.", "intent_mystic"),
           ("alms", "Give Alms Along the Road", "Walk with open hands and a heavy purse.", "altruism_intent")],
  pulses=[
      ("eir_pilgrim_fast", "[first.GetShortUIName|U] Kept the Fast Without Faltering", "positive", 1.2, "is_adult = yes", "add_piety = minor_piety_gain\nadd_stress = minor_stress_loss", None),
      ("eir_pilgrim_vision", "[first.GetShortUIName|U] Had a Vision at the Holy Place", "positive", 1.0, "is_adult = yes", "add_piety = medium_piety_gain\nadd_trait_xp = { trait = lifestyle_mystic value = 20 }", ("derg", 1.8)),
      ("eir_pilgrim_stair", "[first.GetShortUIName|U] Climbed the Last Stair on Bleeding Feet", "positive", 1.0, "is_adult = yes\nprowess >= 6", "add_piety = minor_piety_gain\nadd_prestige = minor_prestige_gain", ("croagh", 1.5)),
      ("eir_pilgrim_hermit", "[first.GetShortUIName|U] Met a Hermit Who Knew Their Name", "positive", 0.9, "is_adult = yes", "add_piety = minor_piety_gain\nadd_stress = minor_stress_loss", ("skellig", 1.5)),
      ("eir_pilgrim_alms", "[first.GetShortUIName|U] Gave Away Their Last Coin", "positive", 0.9, "is_adult = yes\nis_ai = yes", "remove_short_term_gold = minor_gold_value\nadd_piety = medium_piety_gain", None),
      ("eir_pilgrim_storm", "A Storm Caught the Pilgrims on the Water", "negative", 0.9, "is_adult = yes\nis_ai = yes", "add_stress = minor_stress_gain\nincrease_wounds_effect = { REASON = fight }", ("skellig", 1.8)),
      ("eir_pilgrim_fall", "[first.GetShortUIName|U] Slipped on the Scree", "negative", 0.8, "is_adult = yes\nis_ai = yes", "increase_wounds_effect = { REASON = fight }\nadd_stress = minor_stress_gain", ("croagh", 1.8)),
      ("eir_pilgrim_doubt", "[first.GetShortUIName|U] Doubted in the Dark", "negative", 0.8, "is_adult = yes\nis_ai = yes", "add_piety = minor_piety_loss\nadd_stress = medium_stress_gain", ("derg", 1.5)),
      ("eir_pilgrim_song", "The Company Sang the Psalms on the Road", "positive", 0.9, "is_adult = yes", "add_stress = minor_stress_loss\nadd_piety = minor_piety_gain", None)])

# ---------------------------------------------------------------------------------------------------------------- 5 HOSTING
A("hosting", name="Great Hosting", icon="decision_found_kingdom",
  desc="A king in Ireland who calls the slógad calls a whole country to the hill. The lords bring their men, the poets their curses, and the host sits for a fortnight in a field making up its mind: to march, to raid or to go home.",
  selection="Call the slógad to a hill.\n\nAnticipated Rewards:\n$BULLET_WITH_TAB$[prestige_i][prestige|E] and [dread_i][dread|E]\n$BULLET_WITH_TAB$A taste of the plunder, if the host marches\n$BULLET_WITH_TAB$The risk of a quarrel in the camp",
  host_desc="$BULLET_WITH_TAB$Gain [prestige_i][prestige|E] and [dread_i][dread|E]\n$BULLET_WITH_TAB$A cattle-raid (táin) may bring gold\n$BULLET_WITH_TAB$A quarrel in the camp may cost you",
  guest_desc="$BULLET_WITH_TAB$You may gain [prestige_i][prestige|E] or gold\n$BULLET_WITH_TAB$You may be wounded in the raid",
  guest_help="Every lord with a spear is expected to answer the call. Those who do not have a reason ready for the host.",
  phase="The Hosting", phase_desc="The host camps for a fortnight. Some of it will go home with plunder. Some of it will go home on a litter.",
  shown="eir_act_gael_host_trigger = yes", shown_text="You are a ruler of a Gaelic or Brythonic culture",
  start="highest_held_title_tier >= tier_county", weeks=2, wait=2, guests=30, cooldown=4, ai_desc="",
  scale_name="Size of the Host", scale_desc="How many men are called and how many cattle slaughtered for them.",
  focus_name="Purpose of the Hosting", focus=[
      ("muster", "Muster the Host", "A show of strength, with drill, reviews and a feast for the captains.", "recruit_knights_intent"),
      ("tain", "The Táin: A Cattle Raid", "A fortnight's raid on a neighbour's herds, for plunder, glory and a good story.", "intent_gain_renown"),
      ("proclaim", "Proclaim the King's Law", "A hosting that is also a reading of the law, so that nobody can say they were not told.", "justice_intent")],
  intents=[("glory", "Win Glory in the Raid", "Be first over the ford and last off the field.", "intent_gain_renown"),
           ("plunder", "Take a Share of the Plunder", "Bring home cattle, silver or slaves.", "intent_revelry"),
           ("oath", "Swear the Host's Oath", "Pledge to follow the king until the herds are home.", "support_liege_intent")],
  pulses=[
      ("eir_hosting_drill", "[first.GetShortUIName|U] Led the Host in Drill", "positive", 1.0, "is_adult = yes\nmartial >= 8", "add_prestige = minor_prestige_gain", ("muster", 1.6)),
      ("eir_hosting_raid", "[first.GetShortUIName|U] Drove Home a Great Herd", "positive", 1.2, "is_adult = yes\nis_ai = yes", "add_gold = medium_gold_value", ("tain", 1.8)),
      ("eir_hosting_champion", "[first.GetShortUIName|U] Took the Champion's Portion", "positive", 1.0, "is_adult = yes\nprowess >= 8", "add_prestige = medium_prestige_gain", ("tain", 1.5)),
      ("eir_hosting_law", "[first.GetShortUIName|U] Heard the King's Law Read and Approved", "positive", 0.9, "is_adult = yes\nis_ai = yes", "add_opinion = { target = scope:host modifier = eir_act_hosted_opinion opinion = 10 }", ("proclaim", 1.8)),
      ("eir_hosting_song", "The War-Poets Sang the Praises of [first.GetShortUIName|U]", "positive", 0.9, "is_adult = yes", "add_prestige = minor_prestige_gain", None),
      ("eir_hosting_quarrel", "[first.GetShortUIName|U] Quarrelled Over Precedence in the Camp", "negative", 1.0, "is_adult = yes\nis_ai = yes\nhas_trait = wrathful", "add_stress = minor_stress_gain\nadd_opinion = { target = scope:host modifier = eir_act_brawl_opinion opinion = -10 }", None),
      ("eir_hosting_wound", "[first.GetShortUIName|U] Was Wounded in a Skirmish at the Ford", "negative", 0.9, "is_adult = yes\nis_ai = yes", "increase_wounds_effect = { REASON = fight }\nadd_prestige = minor_prestige_gain", ("tain", 1.8)),
      ("eir_hosting_hunger", "The Host Ate the Camp Out of Bread", "negative", 0.8, "is_adult = yes\nis_ai = yes", "add_stress = minor_stress_gain\nremove_short_term_gold = minor_gold_value", ("muster", 1.4)),
      ("eir_hosting_sing", "A Marching Song Went Round the Whole Camp", "positive", 0.8, "is_adult = yes", "add_stress = minor_stress_loss", None)])

# ---------------------------------------------------------------------------------------------------------------- 6 BARDIC CONTEST
A("bardic", name="Bardic Contest", icon="decision_golden_age",
  desc="Ireland pays its poets more than its priests, and a poet knows it. The contest is held in the king's hall: the satirists compete for the king's favour and the audience's silence, and the chief poet's chair goes to whoever is left standing.",
  selection="Hold a contest of poets in your hall.\n\nAnticipated Rewards:\n$BULLET_WITH_TAB$[prestige_i][prestige|E] and fame\n$BULLET_WITH_TAB$A new chief poet\n$BULLET_WITH_TAB$Risk of an insult in verse",
  host_desc="$BULLET_WITH_TAB$Gain [prestige_i][prestige|E] and fame\n$BULLET_WITH_TAB$Guests may gain [opinion|E] of you\n$BULLET_WITH_TAB$A satire may be aimed at you",
  guest_desc="$BULLET_WITH_TAB$You may gain [prestige_i][prestige|E] or learning experience\n$BULLET_WITH_TAB$You may be satirised",
  guest_help="Poets, kings, scholars and anyone who enjoys a well-aimed insult are welcome. The poets sit nearest the fire.",
  phase="The Contest", phase_desc="Three nights of recitation in the king's hall: praise-poems, genealogies, satires and a very long epic.",
  shown="eir_act_bardic_host_trigger = yes", shown_text="You are a ruler of a Gaelic or Brythonic culture",
  start="highest_held_title_tier >= tier_county", weeks=2, wait=1, guests=25, cooldown=4, ai_desc="",
  scale_name="Prize of the Contest", scale_desc="How rich the prize and how large the hall.",
  focus_name="Form of the Contest", focus=[
      ("praise", "Praise-Poems", "The poets compete in the praise of kings, the oldest and cleanest of the arts.", "intent_storyteller"),
      ("satire", "Satire", "The poets compete in cutting verse. The kings pretend to like it.", "intent_sow_discord"),
      ("genealogy", "Genealogies and Epics", "A contest of memory: kings, battles and cattle raids, recited from Míl to the present day.", "intent_knowledge")],
  intents=[("recite", "Recite for the Prize", "Stand up before the hall and perform.", "intent_storyteller"),
           ("patron", "Find a Patron", "Impress the king and be given a hall and a salary.", "intent_gain_renown"),
           ("learn", "Learn From the Masters", "Sit at the feet of the best poets in the land.", "intent_study_hard")],
  pulses=[
      ("eir_bardic_praise", "[first.GetShortUIName|U] Delivered a Flawless Praise-Poem", "positive", 1.2, "is_adult = yes\nlearning >= 8", "add_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_poet value = 20 }", ("praise", 1.6)),
      ("eir_bardic_epic", "[first.GetShortUIName|U] Recited the Epic Without a Stumble", "positive", 1.0, "is_adult = yes\nlearning >= 6", "add_prestige = minor_prestige_gain\nadd_trait_xp = { trait = lifestyle_poet value = 20 }", ("genealogy", 1.6)),
      ("eir_bardic_lesson", "[first.GetShortUIName|U] Learned a Metre From an Old Master", "positive", 1.0, "is_adult = yes", "add_stress = minor_stress_loss\nadd_trait_xp = { trait = lifestyle_poet value = 15 }", None),
      ("eir_bardic_patron", "[first.GetShortUIName|U] Was Offered a Hall by the King", "positive", 0.9, "is_adult = yes\nis_ai = yes", "add_gold = minor_gold_value\nadd_opinion = { target = scope:host modifier = eir_act_hosted_opinion opinion = 10 }", None),
      ("eir_bardic_laugh", "The Whole Hall Laughed at a Neat Insult", "positive", 0.8, "is_adult = yes", "add_stress = minor_stress_loss", ("satire", 1.4)),
      ("eir_bardic_satire", "[first.GetShortUIName|U] Was Satirised to Their Face", "negative", 1.0, "is_adult = yes\nis_ai = yes\nNOT = { has_trait = humble }", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain\nadd_opinion = { target = scope:host modifier = eir_act_insulted_opinion opinion = -10 }", ("satire", 1.8)),
      ("eir_bardic_fail", "[first.GetShortUIName|U] Forgot the Fourth Verse", "negative", 0.9, "is_adult = yes\nis_ai = yes\nlearning < 8", "add_prestige = minor_prestige_loss\nadd_stress = minor_stress_gain", None),
      ("eir_bardic_feud", "Two Poets Cursed Each Other Over the Prize", "negative", 0.7, "is_adult = yes\nis_ai = yes", "add_stress = minor_stress_gain", ("satire", 1.5)),
      ("eir_bardic_harp", "A Harper Played Until the Candles Failed", "positive", 0.8, "is_adult = yes", "add_stress = minor_stress_loss\nadd_prestige = minor_prestige_gain", None)])

# Intent rewards: intent key -> effect run on the character who held it (all ruled by the activity's on_end)
INTENT_REWARDS = {
    "judgement": "add_prestige = minor_prestige_gain\nadd_stress = minor_stress_loss",
    "renown": "add_prestige = medium_prestige_gain",
    "match": "add_gold = minor_gold_value\nadd_stress = minor_stress_loss",
    "omen": "add_trait_xp = { trait = lifestyle_mystic value = 25 }\nadd_stress = minor_stress_loss",
    "revel": "add_stress = medium_stress_loss",
    "blessing": "add_piety = medium_piety_gain",
    "fealty": "add_prestige = minor_prestige_gain",
    "genealogy": "add_prestige = medium_prestige_gain",
    "peace": "add_prestige = minor_prestige_gain\nadd_stress = minor_stress_loss",
    "penance": "add_piety = medium_piety_gain\nadd_stress = medium_stress_loss",
    "vision": "add_trait_xp = { trait = lifestyle_mystic value = 30 }",
    "alms": "add_piety = minor_piety_gain\nadd_prestige = minor_prestige_gain",
    "glory": "add_prestige = medium_prestige_gain",
    "plunder": "add_gold = medium_gold_value",
    "oath": "add_prestige = minor_prestige_gain",
    "recite": "add_prestige = medium_prestige_gain\nadd_trait_xp = { trait = lifestyle_poet value = 20 }",
    "patron": "add_gold = minor_gold_value\nadd_prestige = minor_prestige_gain",
    "learn": "add_trait_xp = { trait = lifestyle_poet value = 30 }",
}

# What the host gets by scale (modest, fair, grand): effects run on the host. Each activity adds its own flavor effect on top.
HOST_REWARDS = {
    "oenach": ["add_prestige = medium_prestige_gain", "add_prestige = major_prestige_gain", "add_prestige = major_prestige_gain\nadd_prestige = medium_prestige_gain"],
    "festival": ["add_piety = minor_piety_gain\nadd_prestige = minor_prestige_gain", "add_piety = medium_piety_gain\nadd_prestige = medium_prestige_gain", "add_piety = major_piety_gain\nadd_prestige = medium_prestige_gain"],
    "feis": ["add_prestige = major_prestige_gain\nadd_legitimacy = minor_legitimacy_gain", "add_prestige = major_prestige_gain\nadd_legitimacy = medium_legitimacy_gain", "add_prestige = massive_prestige_gain\nadd_legitimacy = major_legitimacy_gain"],
    "pilgrimage": ["add_piety = medium_piety_gain", "add_piety = major_piety_gain", "add_piety = major_piety_gain\nadd_piety = medium_piety_gain"],
    "hosting": ["add_prestige = minor_prestige_gain\nadd_dread = minor_dread_gain", "add_prestige = medium_prestige_gain\nadd_dread = medium_dread_gain", "add_prestige = major_prestige_gain\nadd_dread = medium_dread_gain"],
    "bardic": ["add_prestige = minor_prestige_gain", "add_prestige = medium_prestige_gain", "add_prestige = major_prestige_gain"],
}
