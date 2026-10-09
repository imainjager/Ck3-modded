# CK3 FLAVOR GUIDE (read before creating ANY decision, event, tradition, building or unit)

Reusable across every mod in this repo (Interactive Events, Eire Reborn, and whatever comes next).
Written from the user's feedback and from reading vanilla CK3. The user may edit it; the user's edits win.

## 0. The one test
Before anything ships ask: **what must the player DO to earn this, what does it CHANGE in the world, what can go WRONG, and how do they FIX it?**
If the answer is "click a button, get a modifier", it does not ship.

## 1. Rules the user has set (do not relax these)
1. **Unique decisions: Claude decides how many times each can happen, per decision.** If a decision is truly unique (founding something, a one-time restoration, a first-ever event) it happens **once per game**; track it with a global variable (vanilla uses the global list `unavailable_unique_decisions`). Anything that is a recurring act (a feast, a circuit, a festival) gets a cooldown instead. A decision the mod's own rules keep undoing (for Eire Reborn: being crowned High King while the tanistic collapse is active) stays repeatable until that rule is lifted. State the choice in the decision's tooltip.
2. **Build for the region, not for one government.** This rule set will drive regional expansion packs, some feudal, some tribal, some clan or other. Before writing a pack, look at the region's start dates and governments, then set income/prestige scales, building access and costs to fit **that** region. Every building, unit and decision must be reachable by the governments the region actually uses (for example, tribal holdings need `tribal_holding` checked explicitly). Use **explicit numbers** for costs; scaled values like `*_gold_value` follow income and misbehave at low income.
3. **Every negative has a way out, and the way out can beat the original loss.** A remedy decision or event must exist for every penalty; the best remedies leave the player *better* than before (a new modifier, trait, opinion, nickname) if they pay the price and do the work.
4. **Flavor must be dynamic, not one note.** A reward touches at least three of: ruler, realm, other characters, map, culture, religion, future decisions.
5. **Nothing is clickable at game start.** Progression gates are earned: land, titles, buildings built, earlier accomplishments, traits/skills, prestige level.
6. **Traditions: upgrade or add, at Claude's discretion, but a tradition must earn its place.** Upgrading (replacing a tradition the culture already has with `remove_culture_tradition` + `add_culture_tradition`, as vanilla does for Bushido, keeping every parameter of the old one) is the default. A brand-new tradition is allowed only when it is relevant to the region, has real flavor (distinct modifiers, an unlock, an event or decision tied to it) and passes the checklist in section 8. No filler traditions.
7. **Events are chains**, in the spirit of "Theft at Court": bold one-line summary, 3-6 options, trait/skill/perk-gated options, readable labels on random outcomes, consequences that reach other characters and the map, roughly 40% negative outcomes, stress at most ~20 per event (miniscule/minor), repeated across story types.
8. Always read the game's `error.log` after the user tests (OneDrive Documents\Paradox Interactive\Crusader Kings III\logs\error.log) and fix every `eir_`/mod line.

## 2. The flavor loop (every major decision follows it)
1. **Hook** - shown once the player is close, so they know what to aim for.
2. **Gate** - `is_valid` lists several concrete things (see lever menu). Show failures with tooltips.
3. **Commitment** - a real cost in two or three currencies, **or no cost at all when the gate is itself the challenge** (vanilla Reclaim Britannia costs nothing because controlling a whole region is the price). A free decision is allowed only if its gate is hard, specific and not something everyone can meet.
4. **Ceremony** - an event for the founder with 3-6 options (take a nickname OR more prestige, hold a feast OR be anointed OR crown quietly...).
5. **Reaction** - other rulers respond, worded by their culture/government/relationship (vanilla fires a second event to other players; for AI use opinions, claims, hooks, factions, calls to arms).
6. **Reward** - three or more kinds, at least one that changes the world.
7. **Risk** - something can go wrong, and the fix is a decision/event (see rule 3).
8. **Memory** - nickname, legend seed, artifact, trait, dynasty/house modifier, or a county landmark.
9. **Follow-up** - a delayed event or a newly unlocked decision. Never an endpoint.

## 3. What vanilla does (reference decisions)
| Decision | Gate | Cost | Notable flavor |
|---|---|---|---|
| Found Kingdom | prestige_level >= 3, top liege, 3 duchies or 30 counties | 300 gold, 750 prestige, 200 piety | choice step (which duchies), cost differs by government |
| Found Empire | prestige_level >= 4, 3 kingdoms or large realm | 1200 gold, 2500 prestige, 600 piety | same |
| Restore Dumnonia | culture/dynasty, hold the duchy, very high prestige, local support, once per game | 300 gold | ceremony event with a choice (nickname vs prestige), reaction event to other players worded by culture |
| Reclaim Britannia | whole region controlled, at most 1 powerful foreign-culture vassal | none | county modifiers for 10 years, capital culture change, nickname (Pendragon / the Tuatha De Danann), heroic legend seed, other players notified |
| Negotiate the Danelaw | tribal era only, 2 duchies, valid opponent | none | other side can reject; unique; time-limited |
Patterns: specific gates, several currencies at once, unique tracking, preview tooltip then a ceremony event, a choice inside the ceremony, reaction events, multi-part rewards, a nickname and a legend.

## 4. Calibration numbers (use these, do not guess)
| Scripted value | Amount |
|---|---|
| prestige: minor / medium / major / massive / monumental | 75 / 150 / 350 / 750 / 1500 |
| piety: minor / medium / major / massive | 50 / 100 / 250 / 500 |
| stress gain: miniscule / minor / medium / major | 10 / 20 / 40 / 60 |
| stress loss: miniscule / minor / medium / major | -5 / -10 / -20 / -40 |
| prestige levels | low 1, medium 2, high 3, very high 4 |
* `minor/medium/major_gold_value` scale with the character's income (about 3, 6 and 12 months). A tribal chief has a few gold a month, so these are tiny. **Use explicit numbers for costs; use scaled values only for rewards.**
* Vanilla events mostly give medium prestige (150) or minor (75), medium piety (100). Major (350) and massive (750) are rare and reserved for decisions.
* Build a stage ladder for each pack from the region's real rulers. Example (Eire Reborn, tribal start): Stage 1 = 4 counties; Stage 2 = 10 counties + duchy + prestige level 2; Stage 3 = 20 counties + kingdom + prestige level 3; Stage 4 = holds the top kingdom + prestige level 4.
* Cost tiers are a starting point, to be rescaled per region: Stage 1: 150-300 prestige, 100-200 gold. Stage 2: 400-900 prestige, 200-400 gold, 100-300 piety. Stage 3: 1000-1500 prestige, 300-600 gold, 200-400 piety. Stage 4: 2500-4000 prestige, 800-1200 gold, 500-600 piety. For a rich feudal region raise gold; for a poor tribal region lean on prestige and piety.
* A decision may cost nothing if its gate is a genuine achievement (control a whole region, hold several named titles, finish a chain of earlier decisions).

## 5. What vanilla events give out (palette to draw from)
Most-used traits added by vanilla events: loyal, devoted, zealous, shrewd, brave, compassionate, arrogant, vengeful, athletic, strong, irritable, lustful, disloyal, rakish, profligate, eccentric, reclusive, journaller, confider; lifestyle traits (lifestyle_poet, _hunter, _mystic, _traveler, _blademaster, _herbalist, _physician, _reveler); injuries/health (wounded_1, scarred, one_eyed, one_legged, blind, disfigured, depressed_1, drunkard, comfort_eater, inappetetic, flagellant).
Pattern: **good outcomes grant a personality or lifestyle trait (often as a chance), bad outcomes grant an injury or a mental scar.** Use `add_trait_xp` for lifestyle traits instead of adding them outright.
Common nicknames: nick_the_great, the_wise, the_just, the_poet, the_triumphant, the_reformer, the_merciful, the_ruthless, the_wicked, the_unworthy, wolf_slayer, troll_slayer. Custom ones are one line in `common/nicknames` plus loc `nick_x` and `nick_x_desc`.
Other recurring vanilla rewards: artifacts, legend seeds, hooks, memories, opinion modifiers, county modifiers, claims, titles, culture/faith changes, spawned armies, event chains with delays.

## 6. Lever menu
**Requirements:** realm size; held titles (duchy/kingdom/named title); a named barony/county; ports (`is_coastal_county`); buildings built (count them); earlier decisions (global vars); traits; skills; prestige level; piety; gold; culture/faith/government; a tradition held or not held; characters at court; vassal count and type; peace/war; cultural era.
**Costs:** gold, prestige, piety (explicit); opinion lost with vassals or Church; a temporary modifier; minor stress; a cooldown; one-time-only.
**Rewards:** add/remove a trait; add/remove a character, county, province or dynasty modifier; unlock or require a building; unlock a men-at-arms type; unlock a decision; replace a tradition; set a culture parameter; create a title and its vassals; pressed claims; change county culture/faith; create an artifact; legend seed; nickname; memory; spawn an army; create a faction; change a law; hook; opinion; delayed event.
**Risks:** a rival gains a claim; a faction or revolt; the Church objects; a trait is lost or an injury gained; an artifact stolen; heirs in chaos; a random outcome fails.

## 7. Technical rules learned the hard way (these broke a real game)
* Localization: one key per line; **escape line breaks as `\n`**; UTF-8 **with BOM**; no duplicate keys; avoid keys that hash-collide with vanilla (the game reports them).
* `descriptor.mod` and launcher `.mod` have NO BOM; scripts and loc have a BOM.
* Vanilla on_actions allow only ONE `effect`: hook with `on_death = { on_actions = { my_on_death } }` and put the effect in your own on_action.
* Scripted values `*_gold_value` scale with income. Explicit numbers for costs.
* Do not put effects in trigger blocks (watch positional arguments in generators).
* A modifier/variable/flag that is defined or set but never used is reported as an error. Use it or delete it.
* Trait icons: `icon = name.dds` (the game adds the path).
* A saved scope does not survive a delayed event: store in a variable.
* Artifacts: `set_artifact_rarity_masterwork`, `create_artifact` with `template = general_unique_template`, then `get_artifact_feature_references_effect`; valid types include book, goblet, sword, necklace.
* Legends: guard with `has_dlc_feature = legends`; vanilla chronicles `great_deed_title` and `valiant_defense` work.
* Tradition swap: remove the old and add the new in culture scope; copy the old tradition's `parameters`.
* Buildings: tribal holders need `tribal_holding` in the holding check; special buildings use `barony ?= title:b_x` and show requirements in `can_construct`; duchy-capital buildings use `type = duchy_capital` and `county.holder = { has_title = prev.duchy }`; costs may use `cost_prestige` and `cost_gold`.
* Run the validator before every commit and read `error.log` after the user tests.

## 8. Shipping checklist (all must be yes)
1. Did the player have to endure a challenge or do something in the world to reach this?
2. Is the cost (or the absence of cost) in line with the nearest vanilla equivalent and with the region's economy and governments?
3. Does the reward touch at least three categories, one of them outside the ruler?
4. Is there a ceremony event with 3+ real options, gated by traits/skills?
5. Does someone else react (opinion, claim, event, faction)?
6. Is there a downside, and a remedy that can beat the downside?
7. Does it leave a memory (nickname, legend, artifact, modifier, landmark)?
8. Does it unlock or lead to something else?
9. Does it work for every government the region uses?
10. Is its repeat rule right (once per game if truly unique, otherwise a cooldown; Rule 1)?
11. Validator clean; `error.log` clean after testing.

---

# PART II: HOW VANILLA BUILDS EVENTS, AND HOW WE BUILD THEM BETTER
Measured from the game files (8,921 events with options, 22,639 options). Vanilla's **diversity** is the thing to keep. Its **one-note and spammy events** are the thing to avoid. Everything below uses vanilla's own scales unless stated.

## 9. What vanilla does well (copy these)
1. **Options are tied to personality, skill and perk.** 52% of events gate at least one option by trait or skill, and 5,251 events give the AI an `ai_chance` that shifts with traits. Options read as *who the character is*, not as menu items.
2. **Stress follows character.** 45% of events use `stress_impact`: acting in line with your personality gives relief (for example `zealous = minor_stress_impact_loss`), acting against it costs stress (`cynical = minor_stress_impact_gain`). Never a flat stress number when a trait-based one exists.
3. **Text changes with the reader.** 3,243 events use conditional text (`triggered_desc`, `first_valid`) so a callous ruler, a Norse ruler and a Brythonic ruler read different lines. Do the same for culture, government, faith and key traits.
4. **Rewards come in several kinds at once.** An option usually mixes a small prestige/piety/gold change, an opinion change on a *named character*, a temporary modifier, and lifestyle XP. Opinion is the most common reward of all (5,161 options).
5. **Lifestyle XP and trait XP, not instant traits.** Vanilla grants `add_<skill>_lifestyle_xp` (minor 50, medium 100, major 300, massive 500; minor and medium are 8 of every 10 uses) and `add_trait_xp` (513 uses) far more often than `add_trait` outright. Good outcomes push the character toward a lifestyle (hunter, poet, mystic, reveler, blademaster, herbalist, physician, traveler, gardener).
6. **Temporary modifiers with a headline stat.** Event modifiers average 3 fields: one headline stat, one side effect, sometimes a multiplier (for example Emaciated: health -0.5, prowess -5, 3 years; Soothed Child: general opinion +10, stress gain x0.9, 5 years). Durations cluster at **5 years (738 uses) and 10 years (836)**, with 3 and 15 next. Never permanent.
7. **Downsides are real and varied.** 37% of events have an option with a cost: opinion loss (2,478), prestige loss (1,035), stress (790), injury or a bad trait (730), gold (671), death (402), imprisonment (365), piety loss (328). Prestige goes down about as often as it goes up.
8. **Randomness is labelled by consequence and personality.** 12% of events use `random_list`, typically with a trait that shifts the odds.
9. **Cooldowns and gates.** 28% of events carry a cooldown (10 years most common, then 5 years, 1 year, 20 years); the rest are gated behind a trigger that only fits some characters.
10. **Chains exist and use short delays.** Of delayed follow-ups, 1,812 use days, 134 months, 106 years. About 70% of chains are two events long, 19% three, 10% four or more; the longest (activities, coronation, pilgrimage, harrying) reach 6-8 events.
11. **Ceremonies are short, reactions are worded for the reader.** The founding event is one or two options; the notification to other players changes text by culture.

## 10. What vanilla does badly (never copy these)
1. **Events where nothing changes.** 11% (995 of 8,921) of vanilla events change nothing at all: no effect in any option, the immediate block or the after block. Another 28% of individual options have no effect of their own.
2. **Click-OK notifications.** 31% of events are single-option; over half of those do nothing. A single-option event is acceptable only when it reveals something the player needs (a letter, a death, a ceremony), never as filler.
3. **Dead ends.** 70% of chains stop after one follow-up. The story never widens to new people, places, titles or consequences.
4. **Spam** (observed in play, not measured). Many repeatable events share the same trigger and fire in clumps because there is no global flavor limit.
5. **Flat repeated choices** (qualitative). The same "pay gold / lose prestige / do nothing" menu across hundreds of events.
6. **Rewards with no memory** (qualitative). Most events leave nothing the player will see again.

## 11. Our rules for events (vanilla scale plus the improvements)
**R1. Every event changes something visible.** At least one option (and preferably every option) must change a number, a relationship, a trait, a modifier, a title, a claim or a future event. A "do nothing" option is allowed only as the safe choice in a multi-option event, and it must still carry a small consequence (a minor stress, a missed chance flagged in a variable, a rival's opinion).
**R2. Single-option events are only for ceremonies and reveals,** and they must come with a choice earlier or later in the same chain.
**R3. Option anatomy.** 3 to 5 options (6 for key moments). Each option has: (a) a fit (a trait, skill or perk that makes it natural, or the safe default), (b) a primary effect, (c) one side effect on a *different axis* (for example prestige up, an opinion down), (d) `stress_impact` that rewards acting in character and punishes acting against it, (e) `ai_chance` shaped by traits, (f) an honest tooltip.
**R4. Rewards follow vanilla's scale.** Use the named values: prestige miniscule/minor/medium/major/massive; piety the same; stress 10/20/40/60; lifestyle XP 25/50/100/300/500; dread 10/20/30; legitimacy 50/100. Most events use minor or medium. Major is for decisions and rare peaks. Massive almost never.
**R5. Teach the character something.** Good outcomes grant lifestyle XP or a trait chance in the right lifestyle (poetry and learning events: lifestyle_poet; hunts and beasts: lifestyle_hunter; saints, wells, visions: lifestyle_mystic; feasts: lifestyle_reveler; duels and training: lifestyle_blademaster; healing: lifestyle_herbalist or lifestyle_physician; voyages and pilgrimages: lifestyle_traveler). Personality traits (brave, compassionate, shrewd, zealous, just, generous, patient, honest, forgiving, calm, loyal, devoted) are earned by the option that embodies them and usually come with a chance, not a certainty.
**R6. Bad outcomes mark the character.** Failures can add injuries (wounded, scarred, one-eyed, one-legged, blind, disfigured), mental marks (depressed, lunatic, possessed) or vices (drunkard, profligate, comfort_eater, inappetetic, flagellant) with a chance, and the recovery path exists (a decision, a physician, a pilgrimage). Prefer temporary modifiers (1-5 years) for minor failures.
**R7. Modifiers are temporary and focused.** 2 to 4 fields, one headline, 3/5/10/15 years. Permanent changes only through titles, traditions, buildings and artifacts.
**R8. The world answers.** If another character is involved, the option must change opinion, a relationship, a hook, a secret or a scheme with that character. Rulers outside the event react through opinions, claims, factions or follow-up events.
**R9. Expand outward.** A chain's next event must add a new axis: a new character, a new place, a new title, a rival's response, a vassal's demand, an artifact, a legend. Never repeat the same menu. The chain ends in a visible mark (nickname, artifact, legend, modifier on a county, new building, changed relationship).
**R10. Echo earlier choices.** Store the choice in a variable or flag and let later events (even years later) mention it in their text and change their options. Vanilla rarely does this; it is the cheapest way to make a story feel alive.
**R11. Vary the text.** Conditional text by culture, government, faith and two or three key traits (callous/compassionate, brave/craven, zealous/cynical). Same event, different voice.
**R12. Anti-spam.**
- Every repeatable event has a cooldown (5-10 years is the vanilla norm) and at least one gate that only some characters meet.
- Add a **global flavor guard**: after any flavor event fires for a ruler, set a flag for 1-2 years that blocks further random flavor events for them (history, invasion and ceremony events are exempt).
- Random pulses stay small (a low chance per year) and are split by theme so one theme never floods.
- Do not fire an event that cannot change anything for the current character.
**R13. Delays.** Follow-ups mostly use days (vanilla 1,812 of 2,052); use months for personal consequences and years for consequences of a decision. Saved scopes do not survive delays: store people and places in variables.
**R14. Randomness is earned.** Use `random_list` for gambles and label the outcomes. A trait, skill or perk should shift the odds. Never an unmarked coin flip.

## 12. A little more than vanilla (the improvements, built on vanilla's scale)
1. **Consequence ledger:** every option leaves at least one mark the player can see later (modifier, opinion, flag, variable, trait XP). The event doc lists the mark.
2. **Two-step payoff:** a risky choice produces a second result 1-5 years later (good or bad), using the same labelled-random method.
3. **Personality ladder:** in a chain, the player's earlier personality choices unlock better or worse options later.
4. **Reaction beat:** major events fire a short reaction from a named neighbour, vassal or churchman (an opinion change plus a line of text), not only a number.
5. **Regional voice:** each expansion pack defines its own nicknames, lifestyle flavors, artifacts and local figures so events in different regions do not share the same cast.
6. **Remedy built in:** for every real loss, at least one option, decision or later event offers a way to recover, and the best path ends with a gain.

## 13. Event recipe (use this skeleton)
1. **Trigger:** culture/region, a state of the character (a trait, a title, a building, a recent decision), a cooldown, and the global flavor guard.
2. **Immediate:** save the cast (a person, a county), apply any invisible setup.
3. **Description:** bold one-line summary, then 2-4 sentences, with conditional lines for culture/government/trait.
4. **Options (3-5):** one in-character-by-trait, one by skill/perk, one safe default, one risky/random (labelled), optionally one that starts a follow-up. Each with stress_impact, ai_chance, a side effect, a mark.
5. **After / follow-up:** schedule the next beat (days/months/years) with a new axis, store choices in variables.
6. **Check:** run Part II checklist below.

## 14. Part II checklist (in addition to section 8)
12. Does at least one option (preferably every option) change something the player can see?
13. If single-option, is it a ceremony or a reveal with a reason to exist?
14. Does each option have a personality or skill fit, trait-based stress, and trait-shaped AI chance?
15. Does it use vanilla's reward scale (minor/medium for events, major rarely)?
16. Does a good outcome teach a lifestyle or personality trait, and a bad one mark the character, with a recovery path?
17. Does the world (a named character or realm) respond?
18. Does the chain widen with each step, and end in a visible mark?
19. Does text vary by culture/government/trait?
20. Is there a cooldown, a gate and the global flavor guard so it cannot spam?

---

# PART III: THE FULL MENU (everything vanilla lets events and decisions do), AND HOW MUCH SHOULD HAPPEN AT ONCE
Sources: `docs/VANILLA_EFFECT_INDEX.md` (every effect used by vanilla, with usage percentages, plus an inventory of the systems they touch) and `docs/VANILLA_REWARD_CATALOG.md`.
Percentages are rough: the share of vanilla events (8,921 with options) or decisions (462) that use the feature at least once.

## 15. The feature menu
"Our target" is vanilla's share raised by about half (capped), because our content should do more per event than vanilla does. It is a goal for a pack taken as a whole, not a rule for every single event.

| # | Feature (what can happen) | Typical vanilla effects | Events | Decisions | Our target (events / decisions) |
|---|---|---|---|---|---|
| 1 | **Opinion changes** on other characters | add_opinion, reverse_add_opinion | 36% | 13% | 54% / 20% |
| 2 | **Relationships, hooks, secrets, schemes** | add_hook, set_relation_friend/rival/lover, add_secret, add_scheme_progress, reveal_to | 35% | 12% | 52% / 18% |
| 3 | **Prestige** | add_prestige, add_dynasty_prestige, add_prestige_level | 21% | 18% | 32% / 27% |
| 4 | **Titles, land, vassals** | create_title_and_vassal_change, change_title_holder, set_de_jure_liege_title, change_county_control, add_building | 20% | 42% | 30% / 60% |
| 5 | **Marriage, family, court membership** | add_courtier, add_companion, marry, divorce, adopt, make_pregnant | 19% | 9% | 28% / 14% |
| 6 | **Temporary character modifier** | add_character_modifier (5 or 10 years is the norm) | 19% | 20% | 28% / 30% |
| 7 | **Claims, casus belli, war, alliance, truce** | add_pressed_claim, add_unpressed_claim, start_war, add_truce_both_ways | 17% | 24% | 26% / 36% |
| 8 | **New or moved characters, travel** | create_character, move_to_pool, start_travel_plan, add_visiting_courtier | 16% | 10% | 24% / 15% |
| 9 | **Gold** | add_gold, remove_short_term_gold, pay_short_term_gold, add_treasury_or_gold | 15% | 5% | 22% / 8% |
| 10 | **Court positions, councillors, task contracts** | appoint, court position holders, complete_task_contract, change_influence | 13% | 5% | 20% / 8% |
| 11 | **Activity effects** (feast, hunt, tournament, pilgrimage, wedding...) | add_activity_log_entry, activity success changes | 12% | 1% | 18% / 2% |
| 12 | **Trait gained or lost** | add_trait, remove_trait, add_trait_force_tooltip | 12% | 10% | 18% / 15% |
| 13 | **Piety** | add_piety, add_piety_level, spiritual fulfilment change (about 2%) | 12% | 8% | 18% / 12% |
| 14 | **Skill, perk or education** | add_<skill>_skill, add_<skill>_lifestyle_perk_points, add_perk | 11% | 2% | 17% / 3% |
| 15 | **Injury, illness, health, fertility, death** | increase_wounds_effect, health changes, death, fertility | 10% | 2% | 15% / 3% |
| 16 | **Stress (direct)** | add_stress | 9% | 3% | 14% / 5% |
| 17 | **Lifestyle XP / trait XP** | add_<skill>_lifestyle_xp (25-500), add_trait_xp | 8% | 1% | 12% / 2% |
| 18 | **Dread, tyranny, legitimacy, unity** | add_dread, add_tyranny, add_legitimacy, add_realm_unity | 7% | 7% | 11% / 11% |
| 19 | **County, province or title modifier** | add_county_modifier, add_province_modifier | 7% | 10% | 11% / 15% |
| 20 | **Legend, nickname, memory** | create_legend_seed, give_nickname, create_character_memory | 6% | 16% | 9% / 24% |
| 21 | **Stories, situations, struggles** | create_story, end_story, situation effects | 6% | 11% | 9% / 17% |
| 22 | **Artifacts** | create_artifact, set_owner, add_artifact_modifier, add_durability | 5% | 2% | 8% / 3% |
| 23 | **Culture, faith, religion, tradition** | set_county_culture, change_faith, add_culture_tradition, add_doctrine, change_cultural_acceptance | 5% | 21% | 8% / 32% |
| 24 | **Imprison, capture, exile, release** | imprison, release_from_prison | 5% | 0% | 8% / 1% |
| 25 | **Faction, unrest, revolt, control** | add_faction_discontent, county control | 3% | 2% | 5% / 3% |
| 26 | **Armies, men-at-arms, troops** | spawn_army, add_maa, levy effects | 3% | 3% | 5% / 5% |
| 27 | **Laws, government, succession** | add_realm_law, add_title_law, change_government | 1% | 10% | 2% / 15% |
| 28 | **Dynasty or house modifier/perk/aspiration** | add_dynasty_modifier, add_house_modifier, dynasty perks | 1% | 8% | 2% / 12% |

**Machinery vanilla also uses (not "things" but how they are delivered):**
trait-based stress or fulfilment impact on options 49% of events; conditional text by character 36%; "do this to other people" iterators (random_courtier, every_vassal, random_relation, ordered_...) 46%; flags and variables 43%; follow-up events 20%; cooldowns 28%; labelled random outcomes 12%; one-option ceremonies 31%.

**Systems these effects can touch** (counts of definitions in the game files; the names are in the index): 23 activities, 79 scheme types, 72 council tasks, 81 court positions, 12 factions, 126 casus belli types, 558 character interactions, 201 laws, 20 governments, 6 lifestyles with 162 perks, 66 artifact types, 38 legend seeds with 33 chronicles, 52 story cycles, 2 struggles, 12 situations, 12 inspirations, 7 epidemics, 111 men-at-arms types, 24 great projects, 31 accolade types, 17 diarchies, 48 hook types, 19 secret types, 394 memory types, 64 subject contracts, 159 task contracts, 7 vassal stances, 29 travel options, 110 dynasty perks, 22 dynasty legacies, 29 house aspirations, 162 culture pillars, 198 traditions, 108 innovations, 729 nicknames, 1,623 opinion modifiers, 306 traits, 989 building entries, 501 decision entries. About **340 distinct action effects** appear in vanilla events and decisions (100 add_*, 79 set_*, 49 remove_*, 35 move/pay/spawn-type, 33 change_*, 18 start/end-type, 13 create_*, and a handful of trigger/give/save tools), plus about **215 "pick one / affect all / pick the best" iterator forms** (120 random_*, 68 every_*, 29 ordered_*). Only effects used in at least 3 events are counted.

**Features that vanilla underuses but that suit our packs:** nicknames and legends (6% of events), artifacts (5%), culture and faith change (5%), dynasty/house effects (1% of events), laws (1%), factions and unrest (3%), armies (3%), stories and situations (6%). Use these on purpose: they are what makes a region feel different from the base game.

## 16. How much should happen at once ("things" per option, event and decision)
A **thing** is one feature from the table above (so +50 piety and +50 learning XP and a spiritual-fulfilment gain is three things, and an opinion change is a fourth). Trait-based stress and AI preferences do not count as things.

| Things | Per option: vanilla | target | Per event (all options and setup): vanilla | target | Per decision: vanilla | target |
|---|---|---|---|---|---|---|
| 0 | 24.8% | 3% | 9.9% | 0% | 17.7% | 0% |
| 1 | 31.4% | 30% | 18.9% | 5% | 20.8% | 12% |
| 2 | 20.4% | 32% | 16.1% | 12% | 13.2% | 16% |
| 3 | 13.0% | 19.5% | 14.8% | 22% | 13.0% | 19.5% |
| 4 | 5.9% | 9% | 11.5% | 17% | 16.0% | 24% |
| 5 | 2.7% | 4% | 9.4% | 14% | 8.0% | 12% |
| 6 | 1.2% | 2% | 7.2% | 11% | 3.0% | 4.5% |
| 7+ | 0.5% | 0.6% | 12.3% | 18.5% | 8.2% | 12.3% |
How the targets were made: every bucket of 3 or more things is vanilla's share times 1.5 (for example 13.0% to 19.5%), the "nothing happens" bucket is cut almost to zero, and the 1-2 thing buckets absorb the rest.
Reading the table: in vanilla only 23% of options do three or more things, and a quarter do none. In our packs, about **35% of options should do three or more things, 67% two or more, and almost none should do nothing**. At event level, **83% of events should show three or more different kinds of change** somewhere in their options and setup. For decisions, **72% should do three or more things** (vanilla's big title decisions already do 6-11).

## 17. Rules that come with the menu
**R15. The multi-thing rule.** An ordinary option does at least two things: the headline and a different-axis side effect. The deliberately small, safe option may do one. Nothing does zero.
**R16. A reward set.** Build the thing list on purpose: a *self* thing (prestige, piety, gold, XP, a trait, stress), a *world* thing (an opinion, a county modifier, a claim, a title, a relationship), and a *mark* thing (a nickname, memory, artifact, legend, modifier, flag) wherever the outcome is meaningful.
**R17. Use the whole menu across a pack.** Over a whole pack, events and decisions together should use at least 20 of the 28 features in the table, and each of the underused features at least a few times.
**R18. Amounts stay on vanilla's scale.** More *kinds* of things, not bigger numbers. A three-thing option still uses minor or medium amounts for each (prestige 75-150, piety 50-100, XP 50-100) so that the totals stay in line with the base game.
**R19. Be honest in the tooltip.** The preview must show every thing the option does, including the side effects and the marks, so the player can choose with open eyes.
**R20. Count them.** When a pack is finished, count the things per option, per event and per decision, compare with the target table above, and report the result with the pack.

## 18. Part III checklist (in addition to sections 8 and 14)
21. Does each ordinary option do at least two different kinds of thing, and none do nothing?
22. Is there a self thing, a world thing and (for meaningful outcomes) a mark thing?
23. Are the numbers on vanilla's scale and the tooltip complete?
24. Across the pack, are at least 20 of the 28 features in use, including the underused ones (nicknames, legends, artifacts, culture or faith, laws, dynasty or house, factions, armies, stories)?
25. After counting, is the pack close to the per-option, per-event and per-decision targets in section 16?

---

# PART IV: BUILDINGS (how vanilla builds them, and how ours must be balanced)
Sources: `docs/VANILLA_BUILDING_CATALOG.md` (every building family in the base game and DLC, with costs and effects) and `docs/BUILDING_BALANCE_MODEL.md` (the scaling rules and an Irish target for each planned building). 956 building entries were scanned: 396 regular, 47 duchy-capital, 264 special, 215 resource mines, the rest tribal, temple-citadel, nomad and other.

## 19. What vanilla buildings do (share of buildings with each effect)
**Regular buildings (396):** monthly income 66%; bonuses to stationed men-at-arms 49%; levies 35%; county development growth 32%; travel danger 26%; supply limit 23%; tax 17%; defender holding advantage 17%; garrison 13%; fort level 11%; hostile raid time 11%; county control growth 10%; build speed 10%; piety 9%; knight effectiveness 9%; epidemic resistance 9%; county opinion 6%; prestige 5%.
**Duchy-capital buildings (47):** county opinion across the duchy 30%; income 28%; development growth 21%; court grandeur 19%; men-at-arms upkeep 19%; piety 17%; legitimacy 15%; stress 13%; fort level 13%.
**Special buildings (264):** county development growth 72%; income 58%; county tax 57%; dynasty prestige 39%; piety 31%; travel danger 25%; fort level 20%; county opinion 18%.

**How many things at once:** a regular building does 1 thing 4% of the time, 2 things 9%, 3 things 13%, 4 things 23%, 5 things 19%, 6 things 13%, 7 things 10% and 8 or more 9%. Duchy buildings do 2-3 things 38% of the time and 8 or more 15%. Special buildings do 8 or more things 41% of the time. **A building is never a one-effect item.**
Target for our regular buildings (vanilla's buckets of five or more effects raised by half): 1 effect 0%, 2 effects 2%, 3 effects 4.5%, 4 effects 17%, 5 effects 28.5%, 6 effects 19.5%, 7 effects 15%, 8 or more 13.5%.

## 20. Vanilla building numbers (use these as the scale)
| | I | II | III | IV | V | VIII |
|---|---|---|---|---|---|---|
| Gold cost, economy / military / temple chains | 150 | 250 | 340 | 500 | 750 | 2240 |
| Gold cost, fortification chains | 100 | 150 | 195 | 275 | 400 | 1145 |
| Gold cost, tribal chains (also 200 prestige at I, 350 at II) | 75 | 100 | 125 | 150 | | |
| Gold cost, duchy-capital chains | 485 | 725 | 1100 | | | |
| Special buildings | mostly 1000 gold; small ones 300-800; wonders 2000-3000 | | | | | |
| Monthly income | 0.35 | 0.55 | 0.75 | 0.95 | 1.15 | 1.75 |
| County development growth (factor) | 0.045 | 0.09 | 0.12 | 0.155 | 0.2 | |
| Defender holding advantage | 2 | 4 | 6 | 8 | 10 | 16 |
| Fort level | 1 | 2 | 3 | 4 | 5 | 8 |
| Travel danger | -1 | -2 | -3 | -4 | -5 | -8 |
| Piety per month | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.8 |
| County control growth per month | 0.1 | 0.2 | 0.3 | 0.4 | | |
| Knight effectiveness | +2% | +4% | +6% | +8% | | |
| Levies | 100 | 175 | 175 | 225 | 275 | 425 |
| Maximum garrison | 150 | 300 | 450 | 800 | 750 | 1200 |
Duchy-capital chains (three levels): development growth across the duchy +10% / +20% / +30%, or tax +15% / +20% / +30%; county opinion +5 / +10 / +15; court grandeur +4 / +8 / +12.
Special buildings (median): county development growth +20%, income +2.0 per month, county tax +20%, piety +0.25 to +1.0, about 8 effects.

## 21. Rules for buildings
**R21. Price and benefit sit on the vanilla line.** For a given tier, our cost per unit of benefit must be within about 25% of the vanilla line. A building that costs more than its vanilla analogue must give more, and one that gives more must cost at least the same.
**R22. New (regional) buildings are stronger than the vanilla analogue, by about 30% on the headline stats.** The number is a starting point (the user's rough suggestion), set per pack and stated in the pack's design notes. Integer stats (fort level, knight limit) stay as they are and gain a second effect instead. Cost follows the vanilla curve; the extra strength is paid for by the building being tied to the region's story, not by a discount.
**R23. Several effects.** Each regular building follows the target distribution in section 19: normally 4-6 distinct effects, one headline and the rest on different axes.
**R24. Regionally relevant.** A building must be a recognisable institution of the region (for Ireland: dún, crannóg, booley pastures, fosterage hall, bruidhean, aonach, brehon court, bardic school, monastic school, round tower, high cross, holy well) with exactly one flavor effect that has no vanilla analogue (legend spread, fosterage opinion, hospitality, poet prestige, cattle levy), and with a short description that says what it is and does.
**R25. Every government the region uses.** Provide a tribal version built on vanilla's tribal pattern (`building_requirement_tribal = yes`, `has_building_or_higher = tribe_01`, tribal costs) and a castle/city/church version with `building_requirement_tribal = no`. Check both appear in the build menu.
**R26. Localization.** Each building needs `building_type_<key>` and `building_type_<key>_desc` (header and description) as well as `building_<key>` for the level name. A building showing a raw key is a bug.
**R27. Chains.** Use levels like vanilla: regular buildings four to eight levels, tribal two to four, duchy buildings three; each level adds about a fifth to a half of the first level's effect (see section 20).

## 22. Part IV checklist
26. Is the cost per unit of benefit within about 25% of the vanilla line for the tier?
27. If it is a regional building, is the headline stat about 30% above its vanilla analogue, and is that stated?
28. Does it do four or more different things, matching the target distribution?
29. Is it a recognisable regional institution with one flavor effect and a real description?
30. Does it appear for tribal and for feudal holders, and are its name and description keys present?
