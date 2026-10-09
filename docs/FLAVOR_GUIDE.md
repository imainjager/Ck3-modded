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
