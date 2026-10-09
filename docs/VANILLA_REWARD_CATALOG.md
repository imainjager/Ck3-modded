# Vanilla CK3: what decisions, events, traditions and buildings cost, give and risk

Reference for the flavor guide. Built by scanning the game files (CK3 with all DLC installed on this machine).
Scanned: **462 decisions**, **8,921 events that have options**, **196 traditions**, **989 building entries** (including art-asset blocks).
Counts come from script scans; effects hidden inside scripted effects were followed two levels deep. Amounts that use named values are shown by name; the table in the flavor guide converts them to numbers.

---
## 1. DECISIONS (462)

### 1.1 Costs
* **38% of decisions are free** (175 of 462). Their price is the gate (a trait, a title, a region held, a state of mind). **62% (287) have a cost block.**
* Which currencies the 287 charge (a decision can charge several): prestige 130, piety 107, gold 105, treasury 62 (the treasury version of gold for treasury governments), influence 24 (a DLC currency).
* Currency mix: **prestige only 77, piety only 67, gold only 48**, gold + prestige 27, gold + piety 21, piety + prestige 11, influence + prestige 7, gold + piety + prestige 7, influence only 14, other 7.
  So prestige and piety are the main currencies of vanilla decisions (nearly twice as common as gold); gold appears on about a third.
* Size of explicit numbers (only decisions that write literal numbers; many use scripted values that scale): **gold** median 375 (range 100-5000, a quarter above 600); **prestige** median 1000 (range 20-5000, a quarter above 2000); **piety** median 1000 (range 50-5000).
* Treasury governments pay from the treasury instead of gold; nomads often pay nothing in currencies they do not use (the cost is multiplied by zero).

### 1.2 What decisions demand (requirements, by frequency)
1. Title held or region controlled: 239 decisions (`has_title`, `completely_controls`, `completely_controls_region`, `top_liege`, a title tier).
2. Government type or mechanic: 162.
3. A once-only / uniqueness marker: 162 (global list `unavailable_unique_decisions`, a flag, or a variable).
4. Prestige or piety level: 101.
5. Faith or religion: 90. 6. Culture, tradition, innovation or era: 92.
7. A trait or a skill threshold: 80.
8. Vassals, liege or neighbours: 51. 9. Realm size (counties): 46.
10. War or peace: 22. 11. Age or family: 20. 12. Building or holding: 12. 13. Gold on hand: 5.
Many have 3-6 of these at once. Typical combinations: culture + title held + prestige level + a region fully controlled + not already done.

### 1.3 What decisions give (effect kinds, by frequency)
Follow-up event 326 (71% fire an event or event chain), uniqueness tracking 102, character modifier 89, title creation or change 88, prestige 67, opinion 63, county/province modifier 48, trait added 46, legend 46, law or government change 45, army or war 37, piety 35, character or travel 30, culture/faith 29, dynasty/house modifier 28, nickname 26, dread/tyranny/legitimacy 23, gold 22, stress 19, trait removed 12, hooks/secrets 7, claims 2, artifact 1.
* **Number of different effect types per decision:** none 47, one 126, two 99, three 66, four 45, five 33, six 17, seven 16, eight 5, nine 3, ten 4, eleven 1. So the median decision does 1-2 things; the **big ones do 6-11**.
* The richest decisions (all major): Secure High Kingdom of the North Sea (11 kinds), Favour the Countryside (Basques) 10, Retake the Eastern Provinces 10, Elevate Mann and the Isles 10, Create Holy Order 9, Found Empire of Beth Nahrain 9, Mongol conquest decision 9.

### 1.4 Downsides in decisions
Only **50 of 462 decisions (11%)** carry any built-in negative, and most are small:
opinion loss 19, trait removed 12 (vows, celibacy), stress 7, prestige loss 7, war/faction 5, legitimacy loss 4, piety loss 2.
Real risk in decisions comes mostly from **what the decision unleashes** (a war, a faction, other rulers' hatred, a rival claimant), not from a built-in cost.

### 1.5 Decision groups (what the major ones look like)
177 of 462 are `major` (shown in the big-decision UI).

**Title-founding decisions** (Found Kingdom/Empire/Duchy, Form Cumbria, Restore Dumnonia/Carthage, Reclaim Britannia, Danelaw, Mann and the Isles, North Sea, Carolingian, Cossack Kingdom, Hindustan):
requires a control gate (regions, duchies, kingdoms), a prestige level (3 or 4 is standard), often a culture, a once-only marker. Costs from none to 2000 prestige. Effects: create the title, shift de jure vassals, nickname, legend seed, a ceremony event, a notification event to other players.

**Cultural / religious decisions** (Convert to Feudalism, Raise Runestone, Seek Aid of the Spirits, Embrace Celibacy, Declare Bloodline Holy, Create Holy Order, Pursue Conqueror's Mantle, Redistribute Wealth): trait-gated, piety costs (up to 2500 for Declare Bloodline Holy), adds/removes traits, modifiers.

**Lifestyle / minor decisions** (Stress-loss decisions per trait, Sale of Titles, Local Arbitration, Commission Epic, Pet the Dog): cheap or free, small and repeatable, with a trait or stress consequence.

---
## 2. DEEP LOOK AT THE TITLE DECISIONS (closest to what Eire Reborn does)

| Decision | Cost | Gate | Effects | Risk |
|---|---|---|---|---|
| **Found Kingdom** | 300 gold, 750 prestige, 200 piety | prestige level 3, top liege, 3 duchies or 30 counties, a choice step over which duchies to include | creates the kingdom, shifts de jure, 3-4 ceremony events | none built in |
| **Found Empire** | 1200 gold, 2500 prestige, 600 piety | prestige level 4, 3 kingdoms (or 60-120 counties) | creates the empire, 3 events | none |
| **Found Duchy** | massive gold, 250 prestige, 200 piety | prestige level 3-4, a county ruler (administrative governments) | creates the duchy | none |
| **Reclaim Britannia** | none | Gaelic or Brythonic culture, controls the whole Britannia region, at most 1 powerful foreign vassal, unique | county modifiers 10 years on foreign-held counties, capital county culture changes, nickname (Pendragon or the Tuatha De Danann), heroic legend seed, other players notified, ceremony event | foreign-culture counties are flagged for the culture modifier |
| **Restore Dumnonia** | 300 gold | culture or dynasty, hold d_cornwall fully, very high prestige, Brythonic realm support, unique | creates the kingdom, ceremony event (choose nickname or more prestige), other players get a reaction text | none |
| **Form Cumbria** | 300 gold | Cumbrian culture, prestige level 3, controls a custom region, a duchy ruler | creates the kingdom, de jure shifts, event | none |
| **Negotiate the Danelaw** | none | tribal era only, medium prestige, 2 duchies, a valid opponent, unique | a negotiation event the other side can accept or reject | rejection |
| **Formalise the Daneland** | 750 prestige | high prestige, high medieval era | creates the kingdom, 3 events, opinion hits (grudge -20, hate) with the loser | creates enemies |
| **Elevate Mann and the Isles** | 2000 prestige | max prestige level, hold the Isle of Man and the Isles duchy, Viking trait or Norse/Norman culture, unique | creates the kingdom, 3 events, dynasty modifier 100 years, province and county modifiers (pirate capital) 100 years, government changes available, laws set | none |
| **Secure High Kingdom of the North Sea** | 200 gold, 1000 prestige | high prestige, controls the whole North Sea region, holds Norway, England and Denmark titles, years of holding, culture and government checks, unique | creates an empire (e_north_sea), "High King of the Seas" modifier, nicknames (the Sea King, the Defiant), conversion boost modifier 20 years, county modifiers, opinion modifiers from vassals, 3 events, legend | none |
| **Restore Carthage** | 1200 gold | prestige level 4, controls four named regions, unique | creates an empire and four kingdoms | none |
| **Reform the Carolingian Empire** | none | high prestige, holds e_france, controls seven custom regions, unique | event, de jure shift, prestige gain, single-heir succession law, destroys the HRE, major prestige loss to others, pretender opinion | enemies |
| **Embrace English Culture** | none | holds k_england, a DLC, harrying ended, high pacification, English culture exists | event, medium prestige, county culture changes | none |
Observations: **the hard gate is the price**. Control of a region, several duchies or kingdoms, named titles, a prestige level, and once-only tracking appear in almost all. Costs are modest compared with the gates (300 gold is typical).

---
## 3. OTHER DECISIONS (sample of the 462)

| Decision | Cost | Gate | Gives | Costs/risks |
|---|---|---|---|---|
| Sale of Titles | prestige (script value) | kingdom tier | `major_gold_value` gold, nickname, a side-effect event after 5 days | prestige cost, event consequences |
| Local Arbitration | prestige scaled by title tier (halved for tribals) | settled government | legitimacy, county modifier 10 years | prestige |
| Commission Epic | medium gold | has a house | medium prestige, an event chain | gold |
| Abandon Celibacy | none | celibate trait | removes the trait | loses the trait's benefits |
| Stress Loss (Drunkard etc.) | none | has the trait | stress relief via an on_action event | medium prestige loss |
| Commit Suicide | none | many severe traits | death | -30 opinion, prestige loss |
| Create Cadet Branch | none | clan/feudal, a living child, titles | a new house and title change | none |
| Unity decisions (clans) | medium gold + piety scaled by house size | clan government | house-unity effects | piety scaling |
| Raise Runestone | none | pagan | county modifier, medium piety, legitimacy, opinion | none |
| Pursue Conqueror's Mantle | monumental piety (1000) | conqueror trait | conqueror trait, opinion +15 from some, -20 from others, major prestige, dread, event | enemies |
| Redistribute Realm Wealth | script gold | faith-specific | county modifier, event | gold |
| Launch Undirected Great Holy War | crusade-bull piety cost | many conditions (age, doctrines, no other holy war, a valid target) | an event that starts the war | piety, war |
| Found University | medium prestige | prestige level 4, a free special building slot, duchy tier | 2 events, nickname (the Scholar) | prestige |
| Create Holy Order | holy-order gold and piety | duchy or kingdom, piety level, faith head, theocracy checks | leased title, 100+ gold start, order-member trait, opinion, modifier 5 years | gold, piety |
| Declare Bloodline Holy | 2500 piety | faith has a religious head, reformed, piety level 5, divine-blood traits | 2 events, savior and paragon traits | huge piety cost |
| Adopt Special Succession | 300 prestige | kingdom or empire, elective succession | event | prestige |
| Tribal Challenge Ruler | none | tribal government | event, usurps the title, +medium prestige, opinion hits on the challenger | opinion |
| Convert to Feudalism | 150 prestige | tribal authority law, not recently tribalised | 2 events, government change, laws set, county modifiers 5-30 years, +30 opinion | wiping tribal structure |
| Pay Homage | standard activity prestige, optionally medium gold | feudal/clan, has a liege, DLC | minor stress | prestige, stress |

---
## 4. EVENTS (8,921 with options)

### 4.1 Shape
* Options per event: **1 option 2,785 (31%)**, 2 options 2,153 (24%), **3 options 2,185 (24%)**, 4 options 1,060 (12%), 5 options 388, 6 options 153, 7+ options about 190 combined. The median event has 2-3 options; 4+ options are rare (about 17%) and used for key moments.
* Single-option events are notifications and ceremonies (for instance the ceremony event of Reclaim Britannia or Found Kingdom).
* **37% of events have at least one option with a downside**.
* **52% have trait- or skill-gated options.**
* **12% use `random_list`** for a risky outcome.

### 4.2 What options give (option counts)
opinion 5,161; prestige 2,397; character modifier 2,205; follow-up event 2,085; piety 1,442; trait added 1,373; stress change 1,059; lifestyle/skill xp 994; gold 951; county/province modifier 910; health/death 740; hooks/secrets/schemes 624; dread/tyranny/legitimacy 606; trait removed 283; title changes 144; nickname 117; artifact 117; army/war 98; culture/faith 86; character spawn 56; claims 37; dynasty/house modifier 31; law changes 20; legend 13.

### 4.3 Typical amounts
* **Prestige:** medium gain 625, minor gain 606, **minor loss 512**, **medium loss 439**, major gain 124, miniscule gain 102, major loss 79, miniscule loss 71, massive gain 15, massive loss 12. Losses almost match gains in number; **prestige moves both ways**.
* **Piety:** medium gain 426, minor gain 386, major gain 159, minor loss 132, medium loss 131, miniscule gain 72, major loss 55.
* **Gold:** minor loss 245, medium loss 194, minor gain 82, medium gain 71, major loss 61, tiny loss 44, major gain 27. **Gold mostly goes out in events**; gains are rarer.
* **Stress:** minor gain 150, minor loss 131, medium loss 116 (impact), medium gain 103, major loss 65, major gain 48.
So the usual reward is minor-to-medium, major is rare, massive is almost never.

### 4.4 Downsides, by how many options carry them
opinion loss 2,478; prestige loss 1,035; stress gain 790; **bad trait or injury 730**; gold lost 671; **death 402**; **imprisonment 365**; piety loss 328; tyranny/dread/legitimacy loss 78.

### 4.5 Traits events add
**Good (counts):** loyal 33, lifestyle_poet 31, lifestyle_mystic 25, athletic 24, lifestyle_reveler 23, lifestyle_hunter 22, journaller 22, lifestyle_blademaster 18, confider 18, compassionate 16, lifestyle_herbalist 15, lifestyle_traveler 15, devoted 15, lifestyle_physician 14, strong 11, lifestyle_gardener 9, brave 9, shrewd 8, forgiving 8, calm 7, generous 7, honest 7.
**Bad:** drunkard 34, depressed_1 26, flagellant 22, disfigured 19, reclusive 18, profligate 17, irritable 15, comfort_eater 14, lunatic_1 14, inappetetic 14, scarred 12, wounded_1 12, ill 11, vengeful 11, sadistic 11, disloyal 10, gallowsbait 10, one_legged 10, callous 10, arrogant 10, one_eyed 10, blind 9.
**Other:** tourney_participant 31, hashishiyah 29, rakish 13, holy_warrior 11, despoiler_of_byzantium 11, improvident 11, contrite 10, flexible_leader 9, shy 9, humble 8, desert_warrior, reckless, logistician, arbitrary 7, eccentric 6, incestuous 6, order_member, disinherited.
Pattern: **good outcomes teach a lifestyle or personality trait; bad outcomes injure, scar or break the mind.**

### 4.6 Example events
* **Hunt (hunt.5001):** 4 options, random list. A plain option for minor prestige; a hunter-trait option for learning xp (and a "distracted" opinion hit); a herbalist/physician option for two herb modifiers (5 years); an intrigue-xp option that costs the liege opinion of someone.
* **Pilgrimage (pilgrimage.1140):** 4 options, random. Pay gold for minor piety; take prestige; small piety for 20 gold; miniscule prestige.
* **Travel (travel_events.2010):** 4 options, random list gated by personality. Lunatic/possessed/compassionate burns an orchard (dread, an opinion hit, a 10-year county modifier); vengeful/wrathful scolds a child (dread, opinion); callous/compassionate pays gold to soothe the child (opinion, two 5-year modifiers, dread loss); sadistic/arbitrary does nothing at all.
* **Travel danger (travel_danger_events.9020):** options gated by sadistic/gluttonous (a cannibal ending, **death by vanishing**), hunter (a 3-year emaciated modifier), arrogant (emaciated), humble (major prestige and piety loss, emaciated, cruelty opinion).
* **Stewardship duty (stewardship_duty.4040):** one no-effect option, one stress option, one that angers a vassal for dread and loses minor prestige, one that pleases a vassal.
* **Medicine (learning_medicine.2022):** a random fertility treatment; success or failure each gives a modifier (10 years vs 5 years).
* **Dumnonia ceremony (british_isles.4001):** two options: take the nickname the Trojan with minor prestige, or refuse it for medium prestige. The reaction event for other players has one option whose text changes by the reader's culture: pleased, outraged or indifferent.

---
## 5. TRADITIONS (196)
* Categories: regional 71, realm 41, societal 39, combat 25, ritual 20.
* 164 give character modifiers; **52 also give county, province or culture modifiers**; average **3.7 parameters** each (flags other systems read).
* Most common character modifiers: accolade glory gain (15), terrain travel danger (mountains, desert mountains, hills, jungle, forest, taiga), knight limit (10), travel speed, men-at-arms recruitment cost, knight effectiveness, AI war chance/cooldown.
* Richest examples: Saharan Nomads (light cavalry, oasis growth, movement), Audacious Cadets (heavy cavalry, siege time), Palace Politics (13 parameters, court grandeur, scheme timers), Chanson de Geste (11 parameters, knight limit, accolade glory, legend spread), Forest Wardens (province construction costs for forests, county growth, travel danger), Hird.
* **A tradition is a bundle: a handful of modifiers plus several parameters that unlock mechanics elsewhere** (buildings, men-at-arms, decisions).

---
## 6. BUILDINGS (989 entries; real buildings about 430 regular + 108 special + 50 duchy capital + 4 great)
* **Special buildings (108):** gold cost mostly 1000 (58 of them), others 400 / 800 / 2000 / 3000. Cost in piety only on 1. Construction time very slow. Mostly gated to a specific barony (holy sites, wonders).
* **Duchy-capital buildings (50):** gold tier 3-5 (expensive_building_tier_3/4/5_cost), no prestige or piety. Built in the duchy capital, the holder must hold the duchy. They give the duchy's capital county growth, character grandeur and `duchy_capital_county_modifier` for every county of the duchy.
* **Prestige cost appears on only 12 buildings** (nomad/tribal), piety cost on 4. Almost everything costs gold.
* Construction times: slow 397, standard 236, very slow 227, quick 102.
* **Province modifiers (frequency):** monthly_income 654, siege weapon strength 253, travel danger 138, defender holding advantage 121, fort level 116, stationed men-at-arms toughness/damage, supply limit, build speed.
* **County modifiers:** development growth 539, tax 293, county opinion 77, county control growth 70, levy size 70.
* **Owner (character) modifiers:** monthly piety 148, dynasty prestige 109, knight effectiveness 54, men-at-arms maintenance 47, monthly prestige 36, clergy opinion 31, legitimacy gain 22, court grandeur 18.
* Requirements: building/holding 796, culture 558, government 64, title held 54.

---
## 7. WHAT THIS MEANS FOR THE FLAVOR GUIDE (proposed, nothing applied)
1. Free decisions are normal in vanilla when the gate is hard (38% are free). Prestige and piety are the most common prices; Eire Reborn leans on gold more than vanilla does.
2. Vanilla big decisions do 6-11 kinds of things; ours do about 4-6.
3. About 71% of vanilla decisions fire an event; the ones that matter fire ceremony AND notification events.
4. The ceremony event in vanilla is usually one option; choices (take the nickname or not) are rare but appear in the best ones.
5. In events, 37% have a downside, 12% a random list, 52% gating. This matches the "40% negative" rule almost exactly.
6. Costs in vanilla are mostly one-off; the common bundle is prestige plus piety plus gold only for the biggest title decisions.
7. Vanilla already covers several things we planned: Reclaim Britannia, Elevate Mann and the Isles, Formalise the Daneland, Restore Dumnonia, Form Cumbria, North Sea High Kingdom.
8. A real prestige cost on buildings is unusual; tribal buildings are the one place it appears.
