"""Data for the building rebuild (Update 2/4): 24 regional families, 10 duchy chains, ~40 special buildings.

Balance rules (docs/BUILDING_BALANCE_MODEL.md): vanilla median stats per level x ~1.3, vanilla cost curve, 4+ distinct
effects per building, one recognisable regional institution per family, a tribal (2 level) AND a feudal (4 level) version.
"""

# vanilla median x1.3, levels I..IV
SERIES = {
    "INC": [0.45, 0.7, 1.0, 1.25],         # monthly_income (province)
    "DEV": [0.06, 0.12, 0.16, 0.2],        # development_growth_factor (county)
    "OPN": [4, 8, 12, 16],                 # county_opinion_add (county)
    "CTRL": [0.13, 0.26, 0.39, 0.52],      # monthly_county_control_growth_add (county)
    "ADV": [3, 5, 8, 10],                  # defender_holding_advantage (province)
    "FORT": [1, 2, 3, 4],                  # fort_level (province) - integer, not boosted
    "LEVYM": [0.08, 0.16, 0.23, 0.3],      # levy_size (county)
    "PIETY": [0.13, 0.26, 0.39, 0.52],     # monthly_piety (character)
    "PRES": [0.13, 0.26, 0.26, 0.34],      # monthly_prestige (character)
    "KNIGHT": [0.03, 0.05, 0.08, 0.1],     # knight_effectiveness_mult (character)
    "TAX": [0.05, 0.06, 0.07, 0.08],       # tax_mult (county)
    "TRAVEL": [-1, -3, -4, -5],            # travel_danger (province)
    "SUPPLY": [290, 520, 650, 780],        # supply_limit (province)
    "RAID": [0.13, 0.26, 0.39, 0.52],      # hostile_raid_time (county)
    "EPID": [10, 13, 16, 20],              # epidemic_resistance (province)
    "REINF": [0.13, 0.13, 0.2, 0.26],      # levy_reinforcement_rate (province)
    "BUILD": [-0.1, -0.1, -0.15, -0.15],   # build_speed (province)
    "LEGEND": [0.03, 0.05, 0.08, 0.1],     # owned_legend_spread_mult (character)
    "COURT": [3, 5, 8, 10],                # courtier_and_guest_opinion (character)
    "VASSAL": [1, 2, 3, 4],                # vassal_opinion (character)
    "LEARN": [0, 1, 1, 2],                 # learning (character)
    "STRESS": [-0.02, -0.04, -0.06, -0.08],  # stress_gain_mult (character)
    "MAAUP": [0.05, 0.08, 0.11, 0.14],     # stationed_maa_damage_mult (province)
    "LEGIT": [0.02, 0.03, 0.04, 0.05],     # legitimacy_gain_mult (character)
    "HEALTH": [0.05, 0.08, 0.1, 0.13],     # health (character)
    "MAINT": [-0.01, -0.02, -0.03, -0.04],  # men_at_arms_maintenance (character)
}

# field -> section ("prov" province_modifier, "cty" county_modifier, "chr" character_modifier, "levy"/"garr" building keys)
SECTION = {
    "monthly_income": "prov", "defender_holding_advantage": "prov", "fort_level": "prov", "travel_danger": "prov",
    "supply_limit": "prov", "epidemic_resistance": "prov", "levy_reinforcement_rate": "prov", "build_speed": "prov",
    "stationed_maa_damage_mult": "prov", "stationed_skirmishers_damage_mult": "prov", "stationed_heavy_infantry_damage_mult": "prov",
    "stationed_light_cavalry_damage_mult": "prov", "stationed_archers_damage_mult": "prov", "stationed_maa_toughness_mult": "prov",
    "development_growth_factor": "cty", "county_opinion_add": "cty", "monthly_county_control_growth_add": "cty",
    "levy_size": "cty", "tax_mult": "cty", "hostile_raid_time": "cty",
    "monthly_piety": "chr", "monthly_prestige": "chr", "knight_effectiveness_mult": "chr", "owned_legend_spread_mult": "chr",
    "courtier_and_guest_opinion": "chr", "vassal_opinion": "chr", "learning": "chr", "stress_gain_mult": "chr",
    "legitimacy_gain_mult": "chr", "health": "chr", "men_at_arms_maintenance": "chr", "diplomacy": "chr", "stewardship": "chr",
    "martial": "chr", "intrigue": "chr", "prowess": "chr", "clergy_opinion": "chr", "monthly_dynasty_prestige_mult": "chr",
    "domain_tax_mult": "chr", "general_opinion": "chr", "knight_limit": "chr", "monthly_piety_gain_mult": "chr",
    "monthly_prestige_gain_mult": "chr", "court_grandeur_baseline_add": "chr", "levy": "levy", "max_garrison": "garr",
}

R = lambda f, s: (f, s)   # recipe entry: (field, series name or explicit 4-list)

# (key, name, kinds, gate var or None, coastal, icon, family description, [4 (level name, level description)], recipe)
# kinds: castle / city / church holdings that get the feudal version. The tribal version is always made.
FAMILIES = [
    ("eir_dun", "Dún", ("castle",), None, False, "icon_building_hill_forts.dds",
     "A hill-fort in the old Irish style: banks, ditches and a timber hall on the high ground. The Irish have raised them for a thousand years.",
     [("Hill-Top Dún", "A single bank and ditch around a timber hall on the high ground."),
      ("Double-Banked Dún", "A second bank and a palisade make the approach a killing ground."),
      ("Royal Dún", "A great hall, a deep ditch and stone-faced banks. Poets say a king could hold it against the world."),
      ("Dún of the Kings", "A fortress-palace of banks, ditches and stone, whose name alone makes a raiding chief think again.")],
     [("defender_holding_advantage", "ADV"), ("fort_level", "FORT"), ("levy", "LEVYB"), ("max_garrison", "GARR"),
      ("monthly_prestige", "PRES")]),
    ("eir_ringfort", "Great Ringfort", ("castle",), "eir_unlock_ringfort", False, "icon_building_hill_forts.dds",
     "The ráth: a great circular rampart round a farmstead and its cattle, found at the heart of every Irish kingdom.",
     [("Earthen Ráth", "A circular bank round the farm and the cattle-yard."),
      ("Ráth of the Chieftain", "A wider bank and a souterrain beneath, where the winter store is hidden."),
      ("Great Ráth", "A triple rampart that holds a whole clan and its herds in time of war."),
      ("Ráth of the Kings", "A royal ringfort whose banks are older than the kingdom it guards.")],
     [("defender_holding_advantage", "ADV"), ("monthly_county_control_growth_add", "CTRL"), ("levy_size", "LEVYM"), ("max_garrison", "GARR"),
      ("hostile_raid_time", "RAID"), ("monthly_income", "INC")]),
    ("eir_crannog", "Crannóg Stronghold", ("castle",), "eir_unlock_crannog", False, "icon_building_palisades.dds",
     "A fortified artificial island in a lake, reachable only by boat or a hidden causeway.",
     [("Timber Crannóg", "Oak piles driven into the lake-bed carry a round house and a landing stage."),
      ("Stone-Girt Crannóg", "Stone is dumped round the piles and a palisade rings the island."),
      ("Fortified Crannóg", "A hidden causeway, a gatehouse on the water and a store of grain for a year."),
      ("Lake-Fortress", "A small island fortress that no host without boats can hope to take.")],
     [("defender_holding_advantage", "ADV"), ("supply_limit", "SUPPLY"), ("fort_level", "FORT"), ("monthly_county_control_growth_add", "CTRL"),
      ("max_garrison", "GARR"), ("travel_danger", "TRAVEL")]),
    ("eir_round_tower", "Round Tower", ("church",), "eir_unlock_round_tower", False, "icon_building_watchtowers.dds",
     "A tall stone belfry that doubles as a refuge and treasury when the raiders come.",
     [("Wooden Belfry", "A bell on a timber frame, rung when the sails appear."),
      ("Stone Cloigtheach", "A tall stone tower with a door set high above the ground."),
      ("Tower of Refuge", "The monks, the books and the silver all fit inside when the longships land."),
      ("Great Round Tower", "A landmark visible for miles, with a ladder that can be drawn up behind the last monk.")],
     [("hostile_raid_time", "RAID"), ("defender_holding_advantage", "ADV"), ("monthly_piety", "PIETY"), ("county_opinion_add", "OPN"),
      ("monthly_income", "INC"), ("epidemic_resistance", "EPID")]),
    ("eir_high_cross", "High Cross", ("church",), "eir_unlock_high_cross", False, "icon_building_graveyard.dds",
     "A carved stone cross, taller than three men and covered in scenes from scripture, that teaches the faith to those who cannot read.",
     [("Cross-Slab", "A carved stone slab at the monastery gate."),
      ("Standing Cross", "A free-standing cross cut with the Crucifixion and the Last Judgement."),
      ("Scripture Cross", "Panels from Genesis to Revelation, read like a stone book by the passing pilgrim."),
      ("Great High Cross", "A masterpiece of the stone-carver's art, to which the faithful travel from far countries.")],
     [("county_opinion_add", "OPN"), ("monthly_piety", "PIETY"), ("development_growth_factor", "DEV"), ("monthly_prestige", "PRES"),
      ("monthly_income", "INC"), ("clergy_opinion", "COURT")]),
    ("eir_scriptorium", "Great Scriptorium", ("church",), "eir_unlock_scriptorium", False, "icon_building_library.dds",
     "Monks copy and illuminate gospel books in the old Irish style: knotwork, spirals and gold leaf in a thousand colours.",
     [("Copying Room", "A cold room with a few desks, an ink-horn and a good deal of patience."),
      ("Scriptorium", "A dozen scribes at their desks and a master who corrects every page."),
      ("Illuminating Hall", "Colour-masters grind pigments, scribes cut quills and a book takes a decade."),
      ("House of the Great Gospel Book", "The monks make a gospel book that kings travel to see.")],
     [("development_growth_factor", "DEV"), ("learning", "LEARN"), ("monthly_piety", "PIETY"), ("owned_legend_spread_mult", "LEGEND"),
      ("monthly_income", "INC"), ("monthly_prestige", "PRES")]),
    ("eir_monastic_school", "Monastic School", ("church",), None, False, "icon_building_monastic_schools.dds",
     "Students from Britain and the Continent come to the Irish monastery to read, copy and argue.",
     [("Cell of Study", "A handful of students and a master under a thatched roof."),
      ("Monastic School", "Students from three kingdoms live in beehive huts around the church."),
      ("School of the Saints", "The abbot teaches Greek, Latin, computus and law to students from across the sea."),
      ("Monastic City School", "A university in all but name, where the learned of Christendom come to study.")],
     [("development_growth_factor", "DEV"), ("learning", "LEARN"), ("monthly_piety", "PIETY"), ("monthly_income", "INC"),
      ("county_opinion_add", "OPN"), ("monthly_prestige", "PRES")]),
    ("eir_holy_well", "Holy Well Shrine", ("church",), None, False, "icon_building_graveyard.dds",
     "A spring said to heal the sick, ringed with offerings of rags and ribbons. The saint took over the well from the goddess, and nobody objected.",
     [("Votive Spring", "A pool in a hollow, with rags tied to the thorn bush above it."),
      ("Saint's Well", "A stone basin and a carved lintel, visited on the saint's day."),
      ("Pilgrim's Well", "A paved path, a chapel and a procession each patron day."),
      ("Healing Well of the Saint", "A great well-chapel, whose cures are sworn to by half the county.")],
     [("monthly_piety", "PIETY"), ("county_opinion_add", "OPN"), ("epidemic_resistance", "EPID"), ("health", "HEALTH"),
      ("monthly_income", "INC"), ("development_growth_factor", "DEV")]),
    ("eir_hermitage", "Hermitage", ("church",), None, False, "icon_building_graveyard.dds",
     "A beehive cell on a lonely rock, where a holy man prays and the locals bring him food. Kings come to him when they need advice they cannot ask anyone else.",
     [("Anchorite's Cell", "One man, one stone hut and the sound of the sea."),
      ("Hermit's Oratory", "A tiny chapel beside the cell and a garden of herbs."),
      ("Skellig of Prayer", "A cluster of beehive huts on a crag, the monks living on fish, birds and faith."),
      ("Desert of the Saints", "A great hermitage where a king may rest, fast and be made quiet.")],
     [("monthly_piety", "PIETY"), ("stress_gain_mult", "STRESS"), ("monthly_county_control_growth_add", "CTRL"), ("county_opinion_add", "OPN"),
      ("monthly_income", "INC"), ("learning", "LEARN")]),
    ("eir_pilgrim_hospice", "Pilgrim Hospice", ("church", "city"), None, False, "icon_building_guild_halls.dds",
     "A guest house at a holy place where pilgrims rest and pay what they can. The old law says a stranger must be fed, and the church obliges.",
     [("Guest Cell", "A few beds and a pot of broth."),
      ("Pilgrim House", "A hall with forty beds, a kitchen and a chapel."),
      ("Hospice of the Saint", "A great guest house with a hospital ward, kept by the nuns."),
      ("Hospice of the Nations", "A hostel for pilgrims from every country, with a physician, a poor-house and a stable.")],
     [("monthly_income", "INC"), ("county_opinion_add", "OPN"), ("epidemic_resistance", "EPID"), ("monthly_piety", "PIETY"),
      ("tax_mult", "TAX"), ("development_growth_factor", "DEV")]),
    ("eir_bardic_school", "Bardic School", ("city",), "eir_unlock_bardic_school", False, "icon_building_monastic_schools.dds",
     "A school where poets train for twelve years in the dark before they may recite before a king. A poet's praise makes a ruler's name; his satire unmakes it.",
     [("Poets' Hut", "A dark hut where the pupils lie with a stone on the stomach and compose."),
      ("Bardic Lodge", "A master poet and thirty pupils learning genealogy, metre and satire."),
      ("Bardic College", "The cream of the Filí learn the ten thousand lines and the thousand histories."),
      ("Ollamh's Hall", "The seat of a chief poet, with a retinue of harpers and a library of genealogies.")],
     [("monthly_prestige", "PRES"), ("owned_legend_spread_mult", "LEGEND"), ("courtier_and_guest_opinion", "COURT"), ("development_growth_factor", "DEV"),
      ("monthly_income", "INC"), ("learning", "LEARN")]),
    ("eir_brehon_court", "Brehon Court", ("city",), "eir_unlock_brehon_court", False, "icon_building_tax_assessor.dds",
     "A court where learned judges apply the ancient laws, case by case, to every dispute in the district.",
     [("Judge's Seat", "A brehon on a stone seat beneath an open sky."),
      ("Court of the Brehon", "A hall where the judges argue precedent in verse."),
      ("Law School", "A school of the Senchas Már, whose graduates settle disputes from sea to sea."),
      ("High Court of Law", "A court whose rulings are quoted from Kerry to Antrim, and sometimes obeyed.")],
     [("monthly_county_control_growth_add", "CTRL"), ("county_opinion_add", "OPN"), ("legitimacy_gain_mult", "LEGIT"), ("monthly_income", "INC"),
      ("tax_mult", "TAX"), ("vassal_opinion", "VASSAL")]),
    ("eir_aonach", "Aonach Fair Ground", ("city", "castle"), None, False, "icon_building_market_villages.dds",
     "A fair ground where the clans meet to trade, race horses, wrestle, make marriages and settle old quarrels beneath a truce.",
     [("Fair Green", "A flat field where a few families trade once a year."),
      ("Aonach", "A great fair at the feast day, with races and a truce that lasts a week."),
      ("Royal Aonach", "A fair where kings are present and laws are proclaimed."),
      ("Great Óenach Ground", "A vast fair of three kingdoms, with horse-racing, law-giving and a hundred bargains.")],
     [("monthly_income", "INC"), ("tax_mult", "TAX"), ("development_growth_factor", "DEV"), ("county_opinion_add", "OPN"),
      ("travel_danger", "TRAVEL"), ("monthly_prestige", "PRES")]),
    ("eir_bruidhean", "Bruidhean", ("city", "castle"), None, False, "icon_building_guild_halls.dds",
     "A hostel of open doors, where any traveller must be fed and sheltered by ancient law. The hospitaller who refuses is shamed for a generation.",
     [("Guest House", "A long house at the crossroads with a fire that never goes out."),
      ("Bruidhean", "A hall with seven doors, so no traveller ever stands in the rain."),
      ("Hospitaller's Hall", "A hostel with a hundred beds, kept by a hereditary hospitaller."),
      ("Royal Bruidhean", "A hall of legend, where the kings of Ireland feast and the poor are fed in the yard.")],
     [("monthly_income", "INC"), ("county_opinion_add", "OPN"), ("monthly_prestige", "PRES"), ("supply_limit", "SUPPLY"),
      ("courtier_and_guest_opinion", "COURT"), ("travel_danger", "TRAVEL")]),
    ("eir_goibniu_smithy", "Smithy of Goibniu", ("city", "castle"), None, False, "icon_building_smiths.dds",
     "A forge that claims descent from the divine smith, whose ale gave the gods immortality and whose spears never missed.",
     [("Bronze-Smith's Forge", "A bellows, an anvil and a trade handed from father to son."),
      ("Iron Forge", "A smithy with its own charcoal burners and a good reputation."),
      ("Master Smith's Yard", "A yard of smiths who make swords, spears and ploughshares."),
      ("Smithy of the Gods", "Smiths of a name known across the sea, working weapons that the poets name.")],
     [("monthly_income", "INC"), ("knight_effectiveness_mult", "KNIGHT"), ("levy", "LEVYB"),
      ("men_at_arms_maintenance", "MAINT"), ("development_growth_factor", "DEV")]),
    ("eir_hobby_stables", "Hobby Stables", ("castle",), None, False, "icon_building_stables.dds",
     "Small, quick Irish horses bred for the hills and the bog, ridden bareback by men who throw javelins.",
     [("Pony Paddock", "A paddock of hardy ponies on the hillside."),
      ("Hobby Stud", "A stud of Irish hobbies bred for speed and sure feet."),
      ("Horse-Master's Yard", "A yard of trained mounts and riders who know the bog-roads."),
      ("Royal Hobby Stables", "A famous stable of swift horses that carry the king's messengers over a province in a day.")],
     [("knight_effectiveness_mult", "KNIGHT"), ("monthly_income", "INC"), ("levy_reinforcement_rate", "REINF"),
      ("supply_limit", "SUPPLY"), ("travel_danger", "TRAVEL")]),
    ("eir_booley_pastures", "Booley Pastures", ("castle", "city"), None, False, "icon_building_hillside_grazing.dds",
     "Summer pastures in the hills, where the herds follow the grass up the mountain and the young people spend the happiest months of the year.",
     [("Summer Hut", "Turf huts on the hill, and a dairy beside the stream."),
      ("Booley", "Herdsmen and dairymaids take the cattle to the hill every June."),
      ("Great Booley", "A hundred households move with the herds, and the hills ring with song."),
      ("Chieftain's Summer Pastures", "The whole clan goes up to the hills with the cattle, and the lowlands feel empty.")],
     [("monthly_income", "INC"), ("tax_mult", "TAX"), ("levy_size", "LEVYM"), ("development_growth_factor", "DEV"),
      ("health", "HEALTH"), ("monthly_county_control_growth_add", "CTRL")]),
    ("eir_cattle_enclosure", "Great Cattle Enclosure", ("castle",), "eir_unlock_cattle_enclosure", False, "icon_building_hillside_grazing.dds",
     "Walled fields where the herds that make up a lord's wealth are kept safe from raiders. A man's honour price is counted in cows.",
     [("Cow-Yard", "A bawn of thorn hedges that keeps the herd in and the wolves out."),
      ("Cattle Bawn", "A stone-walled enclosure with a watchtower, large enough for a thousand head."),
      ("Great Bawn", "The winter quarters of a chief's herds, with a hundred herdsmen to keep them."),
      ("Royal Cattle Enclosure", "A vast stockade of kine from which half the province is fed and half the kings are paid.")],
     [("monthly_income", "INC"), ("tax_mult", "TAX"), ("levy_size", "LEVYM"), ("defender_holding_advantage", "ADV"),
      ("monthly_prestige", "PRES"), ("development_growth_factor", "DEV")]),
    ("eir_fosterage_hall", "Fosterage Hall", ("castle", "city"), None, False, "icon_building_hall_of_heroes.dds",
     "A long hall where the sons of vassals are raised beside the lord's own children. Foster-brothers will die for each other.",
     [("Foster-Hall", "A house for a handful of foster-children and their nurse."),
      ("Fosterage Hall", "A hall of thirty children from half the neighbouring families."),
      ("Great Fosterage Hall", "A school of manners and arms, where noble children learn their place and each other."),
      ("Hall of the Foster-Brothers", "Generations of foster-brothers have been raised here, and some of them rule kingdoms.")],
     [("monthly_county_control_growth_add", "CTRL"), ("county_opinion_add", "OPN"), ("monthly_prestige", "PRES"), ("vassal_opinion", "VASSAL"),
      ("monthly_income", "INC"), ("levy", "LEVYB")]),
    ("eir_ogham_stones", "Ogham Pillar Field", ("castle", "church"), None, False, "icon_building_watchtowers.dds",
     "Standing stones cut with the notches of the old alphabet, naming the dead and the lands they held. A boundary-stone is also a lawyer.",
     [("Standing Stone", "A single pillar naming a chief and his father."),
      ("Ogham Pillars", "A line of stones that mark the boundary of the clan-lands."),
      ("Field of Memory", "A field of pillars where the clan keeps its dead and its claims."),
      ("Great Ogham Field", "A forest of carved stones that every claimant has to read before he may speak.")],
     [("county_opinion_add", "OPN"), ("owned_legend_spread_mult", "LEGEND"), ("monthly_county_control_growth_add", "CTRL"), ("monthly_prestige", "PRES"),
      ("monthly_income", "INC"), ("development_growth_factor", "DEV")]),
    ("eir_fianna_lodge", "Fianna Lodge", ("castle",), "eir_unlock_fianna", False, "icon_building_hall_of_heroes.dds",
     "A hunting lodge in the forest where young warriors live as the heroes of the tales did: hunting, fasting, fighting and composing verse.",
     [("Hunter's Hut", "A turf hut in the forest where the band assembles in winter."),
      ("Fianna Lodge", "A lodge where forty warriors winter, hunt and train."),
      ("Hall of the Fianna", "A hall decorated with the tales of Fionn, the hunters' hall and the poets' hall."),
      ("Great Fian Hall", "A great hunting-hall of a famous band of warriors, living by the old rules.")],
     [("knight_effectiveness_mult", "KNIGHT"), ("monthly_prestige", "PRES"), ("levy", "LEVYB"),
      ("levy_reinforcement_rate", "REINF"), ("monthly_income", "INC")]),
    ("eir_hosting_ground", "Hosting Ground", ("castle",), None, False, "icon_building_barracks.dds",
     "The field where the slógad assembles. A hosting that can find its own ground quickly is a hosting that wins.",
     [("Muster Field", "A flat field with a cairn on which the chief stands to call his men."),
      ("Hosting Green", "A field with wells, huts and a drill-ground."),
      ("Great Hosting Ground", "A camp where a whole province's host can be fed and quartered for a month."),
      ("Royal Hosting Field", "The assembly ground of a royal hosting, with a standing camp and a stand of beacon-fires.")],
     [("levy", "LEVYB"), ("levy_reinforcement_rate", "REINF"), ("levy_size", "LEVYM"), ("supply_limit", "SUPPLY"),
      ("men_at_arms_maintenance", "MAINT"), ("monthly_county_control_growth_add", "CTRL")]),
    ("eir_sea_quay", "Irish Sea Quay", ("city",), "eir_unlock_sea_trade", True, "icon_building_market_villages.dds",
     "A timber quay where Irish cattle, hides, wolfhounds and slaves are sold to the merchants of Bristol, Chester and Dublin.",
     [("Landing Strand", "A beach with a few boats and a few merchants."),
      ("Timber Quay", "A wooden quay with warehouses for hides and salt."),
      ("Merchant Wharf", "A stone wharf with cranes and a customs-house."),
      ("Quays of the Irish Sea", "A harbour where ships from Bordeaux, Chester and Norway are all in the roads.")],
     [("monthly_income", "INC"), ("tax_mult", "TAX"), ("development_growth_factor", "DEV"), ("supply_limit", "SUPPLY"),
      ("stewardship", [0, 1, 1, 1]), ("monthly_prestige", "PRES")]),
    ("eir_longship_yard", "Longship Yard", ("city", "castle"), "eir_unlock_sea_trade", True, "icon_building_stables.dds",
     "A sheltered cove where sea-kings build and mend the long galleys, learning the trade the Norse brought and making it their own.",
     [("Boat-Strand", "A beach, a few curraghs and a few boat-builders."),
      ("Boatyard", "A yard that builds currachs and sixteen-oared galleys."),
      ("Galley Yard", "A yard that builds thirty-oared birlinns and fits them out for war."),
      ("Royal Shipyard", "A yard of sixty-oared galleys and a staff of the best shipwrights on the coast.")],
     [("supply_limit", "SUPPLY"), ("monthly_income", "INC"), ("levy", "LEVYB"), ("knight_effectiveness_mult", "KNIGHT"),
      ("levy_reinforcement_rate", "REINF"), ("monthly_prestige", "PRES")]),
]

# Duchy-capital chains: (key, duchy or None, celt-gate, name, family desc, [3 level names], flavor [(field, [3 values])])
# vanilla: +10/20/30% duchy development growth, +5/10/15 county opinion, +4/8/12 grandeur; x1.3
DUCHY_BASE = {
    "dev": [0.13, 0.26, 0.39], "opn": [7, 13, 20], "grand": [5, 10, 16],
}
DUCHY = [
    ("eir_rightech", None, "celt", "Ríghteach", "The great hall of a king, with room for a thousand guests and every poet in the province.",
     ["Hall of the Chieftain", "Hall of the King", "Great Ríghteach"], [("monthly_prestige", [0.13, 0.26, 0.39]), ("vassal_opinion", [2, 3, 5])]),
    ("eir_munster_seat", "d_munster", "gael", "Seat of the Eóganachta", "The ancient seat of the kings of Munster, on a limestone rock above the plain.",
     ["Raised Seat", "Royal Rock", "Seat of the Eóganachta"], [("knight_effectiveness_mult", [0.03, 0.05, 0.08]), ("monthly_prestige", [0.13, 0.2, 0.26])]),
    ("eir_meath_court", "d_meath", "gael", "Court of the Ard Rí", "The court that judges the quarrels of the kings, in the heart of Ireland.",
     ["Court of Meath", "Court of Assembly", "Court of the Ard Rí"], [("legitimacy_gain_mult", [0.03, 0.05, 0.08]), ("vassal_opinion", [3, 5, 8])]),
    ("eir_ulster_fortress", "d_ulster", "gael", "Fortress of the Ulaid", "A great earthwork in the north, with a hall where the Red Branch is remembered.",
     ["Ulaid Rampart", "Red Branch Hall", "Fortress of the Ulaid"], [("prowess", [1, 1, 2]), ("monthly_prestige", [0.13, 0.2, 0.26])]),
    ("eir_connacht_seat", "d_connacht", "gael", "Seat of Cruachan", "The royal seat of Connacht, with its ring of banks and its tales of Medb.",
     ["Bank of Cruachan", "Hall of Medb", "Seat of Cruachan"], [("martial", [1, 1, 2]), ("levy_size", [0.05, 0.08, 0.1])]),
    ("eir_leinster_dun", "d_leinster", "gael", "Dún of Leinster", "The rich eastern kingdom's hill-fort, with a view of the whole plain.",
     ["Slaney Dún", "Royal Dún of Ferns", "Dún of Leinster"], [("stewardship", [1, 1, 2]), ("tax_mult", [0.04, 0.06, 0.08])]),
    ("eir_albany_stone", "d_albany", "gael", "Crowning Stone of Alba", "A sacred stone on which the kings of the Gael are inaugurated.",
     ["Hill of Inauguration", "Crowning Stone", "Stone of Destiny"], [("diplomacy", [1, 1, 2]), ("monthly_prestige", [0.13, 0.2, 0.26])]),
    ("eir_isles_galley_yard", "d_the_isles", "celt", "Galley Yard of the Isles", "Where the sixty-oared galleys of the Isles are built.",
     ["Sea-Lords' Yard", "Galley Yard", "Galley Yard of the Isles"], [("tax_mult", [0.04, 0.06, 0.08]), ("knight_effectiveness_mult", [0.02, 0.04, 0.06])]),
    ("eir_gwynedd_stronghold", "d_gwynedd", "celt", "Stronghold of Snowdonia", "A mountain stronghold from which the princes of Gwynedd defy all comers.",
     ["Mountain Llys", "Eryri Hold", "Stronghold of Snowdonia"], [("prowess", [1, 1, 2]), ("levy_size", [0.05, 0.08, 0.1])]),
    ("eir_cornwall_stannary", "d_cornwall", "celt", "Stannary Hall", "The hall where the tinners of Cornwall meet to set the price of tin.",
     ["Tinners' Bench", "Stannary Court", "Stannary Hall"], [("monthly_county_control_growth_add", [0.13, 0.26, 0.39]), ("tax_mult", [0.05, 0.07, 0.1])]),
]

# Special buildings: (key, barony, gate kind, tier, profile, icon, name, description)
# gate kind: None (open), "gael", "celt", or a global variable name
# tier: 1 = landmark (300g+300p), 2 = major (500g+700p), 3 = wonder (1000g+1200p)
# profile: royal / holy / learn / sea / war / ancient / trade
SPECIAL = [
    # ---- existing, fixed
    ("eir_hall_of_tara", "b_trim", "eir_done_tara_hall", 3, "royal", "icon_structure_cologne_cathedral.dds",
     "Hall of Tara", "The royal hall of the High Kings, rebuilt on the hill above the Boyne. Here the kings of Ireland were chosen."),
    ("eir_armagh_cathedral", "b_armagh", "eir_done_armagh", 3, "holy", "icon_structure_canterbury_cathedral.dds",
     "Cathedral of Armagh", "The primatial church of Ireland, with its famous library and bell-shrine."),
    ("eir_rathcroghan", "b_cruachu", "gael", 2, "royal", "icon_building_hall_of_heroes.dds",
     "Royal Site of Rathcroghan", "A vast complex of mounds and ditches, the ritual capital of Connacht and the home of Medb."),
    ("eir_slemish_shrine", "b_slemish", None, 1, "holy", "icon_building_graveyard.dds",
     "Patrick's Hill", "The mountain where the slave-boy Patrick herded sheep and heard his call."),
    ("eir_uisneach_fires", "b_uisneach", None, 2, "ancient", "icon_building_watchtowers.dds",
     "Fires of Uisneach", "The navel of Ireland, where the first Beltane fire was lit and five kingdoms meet."),
    ("eir_kildare_flame", "b_kildare", None, 2, "holy", "icon_building_graveyard.dds",
     "Fire of Brigid", "A perpetual flame tended by nuns, in honour of the saint and the goddess."),
    ("eir_emly_monastery", "b_emly", None, 1, "learn", "icon_building_monastic_schools.dds",
     "Monastery of Ailbe", "A great Munster monastery with a fine school and a famous bell."),
    ("eir_kincora", "b_kincora", "gael", 2, "war", "icon_building_hall_of_heroes.dds",
     "Palace of Kincora", "The hall of the Dál gCais kings on the Shannon, where a warlord feasted his captains."),
    ("eir_black_pool_quays", "b_dublin", "eir_done_dublin", 2, "sea", "icon_building_market_villages.dds",
     "Black Pool Quays", "The great Norse-Gael harbour on the Liffey, now in Irish hands."),
    ("eir_waterford_harbour", "b_waterford", "gael", 2, "sea", "icon_building_market_villages.dds",
     "Harbour of Waterford", "A harbour that trades with Bristol and Bordeaux and pays for its own walls."),
    ("eir_cork_quays", "b_cork", "gael", 1, "sea", "icon_building_market_villages.dds",
     "Quays of Cork", "Quays beside the monastery of Saint Finbarr, in the marsh where the Lee divides."),
    ("eir_limerick_longphort", "b_limerick", "gael", 1, "war", "icon_building_barracks.dds",
     "Longphort of Limerick", "A river-fortress that commands the Shannon and the road to the west."),
    ("eir_derry_oakgrove", "b_derry", None, 1, "holy", "icon_building_graveyard.dds",
     "Oakgrove of Colmcille", "The saint's oak-wood monastery, the cradle of the Columban church."),
    ("eir_downpatrick", "b_downpatrick", None, 1, "holy", "icon_building_graveyard.dds",
     "Grave of the Three Saints", "Where Patrick, Brigid and Colmcille are said to lie together."),
    ("eir_bangor_school", "b_bangor", "eir_done_fili", 2, "learn", "icon_building_library.dds",
     "School of Bangor", "A monastery whose scholars once taught half of Europe to read."),
    ("eir_kilkenny_monastery", "b_kilkenny", None, 1, "learn", "icon_building_monastic_schools.dds",
     "Monastery of Canice", "A major monastic centre of Ossory, with a round tower and a famous scriptorium."),
    ("eir_tuam_cross", "b_tuam", "eir_unlock_high_cross", 1, "holy", "icon_building_graveyard.dds",
     "High Cross of Tuam", "A carved cross with scenes of kings and saints, raised by the kings of Connacht."),
    ("eir_ferns_seat", "b_ferns", None, 1, "royal", "icon_building_hill_forts.dds",
     "Royal Seat of Ferns", "The seat of the kings of Leinster, above the Slaney valley."),
    # ---- new Irish sites
    ("eir_newgrange", "b_drogheda", None, 2, "ancient", "icon_building_watchtowers.dds",
     "Brú na Bóinne", "A passage-tomb older than the pyramids, where the winter sun still strikes the inner chamber."),
    ("eir_grianan_aileach", "b_fahan", None, 2, "war", "icon_building_hill_forts.dds",
     "Grianán of Aileach", "A stone fortress on a hill above two seas, the seat of the northern Uí Néill."),
    ("eir_emain_macha", "b_dungannon", None, 2, "royal", "icon_building_hall_of_heroes.dds",
     "Emain Macha", "The great ritual enclosure of the kings of Ulster, where the Red Branch is remembered."),
    ("eir_glendalough", "b_wicklow", "eir_done_glendalough", 2, "learn", "icon_building_monastic_schools.dds",
     "Glendalough", "The monastic city in the valley of two lakes, with its round tower, seven churches and school."),
    ("eir_clonmacnoise", "b_birr", "eir_done_clonmacnoise", 3, "learn", "icon_building_library.dds",
     "Clonmacnoise", "The great monastic city on the Shannon, whose crosses and manuscripts are known across Europe."),
    ("eir_rock_of_cashel", "b_clonmel", "eir_done_cashel", 3, "royal", "icon_structure_canterbury_cathedral.dds",
     "Rock of Cashel", "A limestone crag crowned with a royal fortress, where the kings of Munster are crowned and the bishops sit."),
    ("eir_skellig_michael", "b_tralee", None, 1, "holy", "icon_building_graveyard.dds",
     "Skellig Michael", "A monastery on a sea-stack off the Kerry coast, at the edge of the known world."),
    ("eir_croagh_patrick", "b_castlebar", None, 1, "holy", "icon_building_graveyard.dds",
     "Croagh Patrick", "A conical mountain where Patrick fasted for forty days, and where pilgrims still climb barefoot."),
    ("eir_carrowmore", "b_sligo", None, 1, "ancient", "icon_building_watchtowers.dds",
     "Carrowmore Cemetery", "A great field of megalithic tombs on the Sligo plain, older than any king's genealogy."),
    ("eir_dun_ailinne", "b_athy", None, 1, "royal", "icon_building_hill_forts.dds",
     "Dún Ailinne", "The great hilltop enclosure where the kings of Leinster are inaugurated."),
    ("eir_lough_derg", "b_donegal", None, 1, "holy", "icon_building_graveyard.dds",
     "Station Island of Lough Derg", "A pilgrim isle where penitents fast and keep vigil in a cave said to open on Purgatory."),
    ("eir_aran_monasteries", "b_galway", None, 1, "holy", "icon_building_monastic_schools.dds",
     "Monasteries of Aran", "Stone cells, oratories and holy wells on a bare Atlantic island, a retreat for saints."),
    ("eir_kinsale_haven", "b_kinsale", "gael", 1, "sea", "icon_building_market_villages.dds",
     "Haven of Kinsale", "A deep south-coast harbour, sheltered from every wind but the south-westerly."),
    ("eir_burren_court", "b_ennis", None, 1, "ancient", "icon_building_watchtowers.dds",
     "Court of the Burren", "A landscape of bare limestone, tombs and stone forts where the lords of Thomond hold their court."),
    # ---- Britain
    ("eir_dunadd", "b_kilmarten", "celt", 2, "royal", "icon_building_hill_forts.dds",
     "Dunadd", "The rocky fortress of Dál Riata, with a footprint carved in the rock where the kings placed their feet."),
    ("eir_iona_abbey", "b_mull", "celt", 3, "holy", "icon_structure_canterbury_cathedral.dds",
     "Abbey of Iona", "Colmcille's island monastery, the mother-house of a hundred churches in Scotland and Ireland."),
    ("eir_whithorn", "b_wigtown", "celt", 1, "holy", "icon_building_graveyard.dds",
     "Candida Casa of Whithorn", "The White House of Saint Ninian, the oldest Christian foundation in northern Britain."),
    ("eir_dumbarton_rock", "b_dumbarton", "celt", 2, "war", "icon_building_hill_forts.dds",
     "Dumbarton Rock", "Alt Clut, the Rock of the Clyde, impregnable seat of the kings of Strathclyde."),
    ("eir_st_davids", "b_st_davids", "celt", 2, "holy", "icon_structure_canterbury_cathedral.dds",
     "Cathedral of St David", "The shrine of Wales's patron saint at the edge of the western sea."),
    ("eir_tintagel", "b_tintagel", "celt", 1, "royal", "icon_building_hill_forts.dds",
     "Fortress of Tintagel", "The cliff-top stronghold of the kings of Dumnonia, where Arthur is said to have been conceived."),
    ("eir_caerleon", "b_casnewydd", "celt", 1, "ancient", "icon_building_watchtowers.dds",
     "Caerleon", "A Roman legionary fortress that the Welsh call Arthur's court."),
    ("eir_holyhead_ferry", "b_holyhead", "celt", 1, "sea", "icon_building_market_villages.dds",
     "Holyhead Crossing", "The short crossing between Anglesey and Ireland, held by one saint and one fortress."),
    ("eir_tynwald_hill", "b_castletown", "celt", 1, "royal", "icon_building_hall_of_heroes.dds",
     "Tynwald Hill", "A four-tiered mound where the laws of the island are read aloud once a year in two languages."),
]

# tier costs (gold, prestige): vanilla specials are mostly 1000 gold. Prestige leads and gold is halved for a prestige culture.
SPECIAL_COST = {1: (300, 300), 2: (500, 700), 3: (1000, 1200)}
# per-tier base (county dev growth, income, tax_mult, county opinion) = vanilla x1.3 for tier 2 and wonder scaling
SPECIAL_BASE = {1: (0.13, 1.3, 0.13, 6), 2: (0.26, 2.6, 0.26, 10), 3: (0.3, 3.2, 0.3, 12)}
# profile -> extra character/province effects scaled by tier (1..3)
SPECIAL_PROFILE = {
    "royal": [("monthly_prestige", [0.3, 0.5, 0.8]), ("legitimacy_gain_mult", [0.05, 0.1, 0.15]), ("vassal_opinion", [2, 4, 6]), ("court_grandeur_baseline_add", [2, 4, 6])],
    "holy": [("monthly_piety", [0.3, 0.5, 0.8]), ("clergy_opinion", [4, 7, 10]), ("monthly_piety_gain_mult", [0.05, 0.08, 0.1]), ("epidemic_resistance", [10, 15, 20])],
    "learn": [("learning", [1, 2, 3]), ("monthly_piety", [0.2, 0.3, 0.5]), ("owned_legend_spread_mult", [0.05, 0.1, 0.15]), ("monthly_prestige", [0.15, 0.25, 0.4])],
    "sea": [("stewardship", [1, 2, 3]), ("monthly_prestige", [0.15, 0.25, 0.4]), ("supply_limit", [500, 900, 1400]), ("travel_danger", [-5, -10, -15])],
    "war": [("knight_effectiveness_mult", [0.05, 0.1, 0.15]), ("defender_holding_advantage", [5, 8, 12]), ("fort_level", [1, 2, 3]), ("monthly_prestige", [0.15, 0.25, 0.4])],
    "ancient": [("monthly_prestige", [0.2, 0.35, 0.5]), ("owned_legend_spread_mult", [0.08, 0.12, 0.2]), ("monthly_piety", [0.15, 0.25, 0.4]), ("health", [0.05, 0.1, 0.15])],
    "trade": [("stewardship", [1, 2, 3]), ("diplomacy", [1, 1, 2]), ("monthly_prestige", [0.1, 0.2, 0.3]), ("travel_danger", [-5, -10, -15])],
}

# ---------------------------------------------------------------------------------------------------------------
# Military additions (flavor guide R23/R28). Vanilla: 52% of special buildings and about half of regular buildings carry
# military fields (stationed men-at-arms bonuses 49% of regular, travel danger 25%, fort level 20%, defender advantage 19%,
# hostile raid time 11%, levy 8-35%). Values are the vanilla medians x ~1.3.
SERIES["MAAT"] = [0.05, 0.08, 0.11, 0.14]     # stationed_maa_toughness_mult
SECTION["garrison_size"] = "prov"
SECTION["army_maintenance_mult"] = "chr"
SECTION["stationed_maa_toughness_mult"] = "prov"

REG_EXTRA = {   # family key -> extra recipe entries
    "eir_brehon_court": [("men_at_arms_maintenance", "MAINT")],
    "eir_ogham_stones": [("hostile_raid_time", "RAID")],
    "eir_aonach": [("levy_reinforcement_rate", "REINF")],
}

# tier 1 / 2 / 3 values
MIL_VALUES = {
    "fort_level": [1, 2, 3],
    "defender_holding_advantage": [4, 6, 8],
    "hostile_raid_time": [0.4, 0.65, 1.0],
    "levy_size": [0.13, 0.2, 0.3],
    "garrison_size": [0.15, 0.33, 0.5],
    "max_garrison": [325, 650, 1000],
    "levy": [325, 650, 1000],
    "knight_effectiveness_mult": [0.1, 0.2, 0.25],
    "knight_limit": [1, 2, 2],
    "travel_danger": [-10, -20, -30],
    "men_at_arms_maintenance": [-0.05, -0.1, -0.13],
    "army_maintenance_mult": [-0.05, -0.065, -0.08],
}
SPECIAL_MIL = {   # special building key -> military fields (the war and sea profiles already carry their own)
    "eir_hall_of_tara": ["levy", "max_garrison", "army_maintenance_mult"],
    "eir_rathcroghan": ["levy_size", "knight_limit"],
    "eir_ferns_seat": ["fort_level", "levy", "defender_holding_advantage"],
    "eir_emain_macha": ["knight_effectiveness_mult", "levy_size"],
    "eir_dun_ailinne": ["levy_size", "defender_holding_advantage", "garrison_size"],
    "eir_dunadd": ["fort_level", "hostile_raid_time", "max_garrison"],
    "eir_tintagel": ["fort_level", "defender_holding_advantage", "garrison_size"],
    "eir_uisneach_fires": ["hostile_raid_time", "levy_size", "travel_danger"],
    "eir_burren_court": ["defender_holding_advantage", "hostile_raid_time"],
    "eir_caerleon": ["fort_level", "levy"],
    "eir_skellig_michael": ["hostile_raid_time", "defender_holding_advantage"],
    "eir_iona_abbey": ["hostile_raid_time", "travel_danger", "max_garrison"],
    "eir_armagh_cathedral": ["max_garrison", "defender_holding_advantage", "hostile_raid_time"],
}
for _f in SPECIAL_MIL.values():
    for _x in _f:
        assert _x in MIL_VALUES, _x


# ---------------------------------------------------------------------------------------------------------------
# STATIONED MEN-AT-ARMS LIBRARY (flavor guide R28c). Vanilla has a stationed bonus for every unit type and four stats
# (damage, toughness, pursuit, screen), as a percentage (_mult) or a flat number (_add), for all men-at-arms (stationed_maa_*)
# or one type (archers, skirmishers, pikemen, heavy_infantry, light_cavalry, heavy_cavalry). Each building gets its own
# mix, so no two buildings give the same bonus. Percentages follow vanilla's tiers x1.3:
#   LOWM  = low tier   0.10/0.125/0.15/0.175 -> 0.13/0.16/0.20/0.23     NORMM = normal tier 0.15/0.20/0.25/0.30 -> 0.20/0.26/0.33/0.39
#   flat adds are small (vanilla military buildings give 12-20 screen or pursuit; legendary ones 10-20 damage).
SERIES.update({
    "LOWM": [0.13, 0.16, 0.20, 0.23], "NORMM": [0.20, 0.26, 0.33, 0.39], "SMALLM": [0.02, 0.04, 0.06, 0.08],
    "FDT": [2, 3, 4, 6], "FPS": [6, 9, 12, 16],
})

REG_MAA = {   # regular family -> stationed bonuses (13 of 24 families, vanilla 49%)
    "eir_dun": [("stationed_pikemen_toughness_mult", "LOWM"), ("stationed_skirmishers_screen_add", "FPS")],
    "eir_ringfort": [("stationed_heavy_infantry_toughness_mult", "LOWM"), ("stationed_maa_toughness_add", "FDT")],
    "eir_crannog": [("stationed_archers_damage_mult", "LOWM")],
    "eir_round_tower": [("stationed_archers_toughness_mult", "LOWM"), ("stationed_archers_screen_add", "FPS")],
    "eir_cattle_enclosure": [("stationed_light_cavalry_pursuit_mult", "LOWM")],
    "eir_bardic_school": [("stationed_maa_damage_add", "FDT")],
    "eir_fosterage_hall": [("stationed_maa_toughness_add", "FDT"), ("stationed_pikemen_damage_mult", "SMALLM")],
    "eir_goibniu_smithy": [("stationed_heavy_infantry_damage_mult", "NORMM"), ("stationed_pikemen_damage_add", "FDT")],
    "eir_hobby_stables": [("stationed_light_cavalry_damage_mult", "NORMM"), ("stationed_light_cavalry_pursuit_add", "FPS")],
    "eir_fianna_lodge": [("stationed_skirmishers_damage_mult", "NORMM"), ("stationed_skirmishers_pursuit_mult", "LOWM")],
    "eir_hosting_ground": [("stationed_maa_toughness_mult", "SMALLM"), ("stationed_maa_screen_add", "FPS")],
    "eir_longship_yard": [("stationed_skirmishers_screen_mult", "LOWM"), ("stationed_heavy_infantry_pursuit_add", "FPS")],
    "eir_booley_pastures": [("stationed_light_cavalry_toughness_mult", "LOWM")],
}
REG_EXTRA = {k: v for k, v in REG_EXTRA.items() if v}

HIGHS = [0.26, 0.39, 0.52]     # special building, tier 1/2/3: vanilla 'high' tier x1.3
LOWS = [0.13, 0.20, 0.26]
GENS = [0.05, 0.08, 0.10]      # stationed_maa_* applies to every unit type, so it is small
FDTS = [4, 7, 10]
FPSS = [10, 14, 18]
SPECIAL_MAA = {   # special building -> stationed bonuses (24 of 41; vanilla specials only 11%, raised by request)
    "eir_hall_of_tara": [("stationed_heavy_infantry_toughness_mult", HIGHS), ("stationed_maa_screen_add", FPSS)],
    "eir_armagh_cathedral": [("stationed_pikemen_toughness_mult", LOWS), ("stationed_maa_toughness_add", FDTS)],
    "eir_rathcroghan": [("stationed_heavy_infantry_damage_mult", HIGHS), ("stationed_maa_damage_add", FDTS)],
    "eir_kincora": [("stationed_archers_damage_mult", HIGHS), ("stationed_archers_screen_add", FPSS)],
    "eir_limerick_longphort": [("stationed_heavy_infantry_damage_add", FDTS), ("stationed_archers_toughness_mult", LOWS)],
    "eir_grianan_aileach": [("stationed_pikemen_toughness_mult", HIGHS), ("stationed_maa_screen_add", FPSS)],
    "eir_dumbarton_rock": [("stationed_archers_toughness_mult", HIGHS), ("stationed_maa_toughness_add", FDTS)],
    "eir_emain_macha": [("stationed_skirmishers_damage_mult", HIGHS), ("stationed_skirmishers_pursuit_add", FPSS)],
    "eir_dunadd": [("stationed_pikemen_damage_mult", HIGHS)],
    "eir_tintagel": [("stationed_light_cavalry_damage_mult", HIGHS), ("stationed_light_cavalry_screen_mult", LOWS)],
    "eir_ferns_seat": [("stationed_light_cavalry_toughness_mult", LOWS), ("stationed_maa_pursuit_add", FPSS)],
    "eir_dun_ailinne": [("stationed_light_cavalry_pursuit_mult", HIGHS)],
    "eir_caerleon": [("stationed_pikemen_damage_mult", LOWS), ("stationed_pikemen_toughness_mult", LOWS)],
    "eir_uisneach_fires": [("stationed_skirmishers_screen_mult", HIGHS)],
    "eir_burren_court": [("stationed_skirmishers_toughness_mult", HIGHS), ("stationed_skirmishers_pursuit_mult", LOWS)],
    "eir_skellig_michael": [("stationed_maa_toughness_add", FDTS)],
    "eir_iona_abbey": [("stationed_pikemen_toughness_mult", LOWS), ("stationed_maa_screen_add", FPSS)],
    "eir_newgrange": [("stationed_heavy_infantry_toughness_add", FDTS)],
    "eir_carrowmore": [("stationed_maa_toughness_mult", GENS)],
    "eir_black_pool_quays": [("stationed_archers_damage_mult", LOWS), ("stationed_maa_pursuit_add", FPSS)],
    "eir_waterford_harbour": [("stationed_heavy_infantry_damage_mult", LOWS)],
    "eir_cork_quays": [("stationed_skirmishers_damage_mult", LOWS)],
    "eir_kinsale_haven": [("stationed_archers_pursuit_mult", LOWS)],
    "eir_holyhead_ferry": [("stationed_maa_screen_add", FPSS)],
}
