# CK3 FLAVOR GUIDE (read before creating ANY decision, event, tradition, building or unit)

Reusable across every mod in this repo (Interactive Events, Eire Reborn, and whatever comes next).
Written from the user's feedback and from reading vanilla CK3. The user may edit it; the user's edits win.

## 0. The one test
Before anything ships ask: **what must the player DO to earn this, what does it CHANGE in the world, what can go WRONG, and how do they FIX it?**
If the answer is "click a button, get a modifier", it does not ship.

## 1. Rules the user has set (do not relax these)
1. **Unique decisions happen once per game.** Track them with a global variable (vanilla uses the global list `unavailable_unique_decisions`).
   Exception: anything the mod's own core rule keeps destroying (for Eire Reborn: being crowned High King while the tanistic collapse is active) stays repeatable until the rule is lifted.
2. **Tribal rulers come first.** Early start dates are tribal: low income, low gold. Lean costs on **prestige and piety**, keep gold smaller, and gate by land/buildings/titles.
   Every building, unit and decision must be reachable by a tribal holder, not only castle/city/church ones.
3. **Every negative has a way out, and the way out can beat the original loss.** A remedy decision or event must exist for every penalty; the best remedies leave the player *better* than before (a new modifier, trait, opinion, nickname) if they pay the price and do the work.
4. **Flavor must be dynamic, not one note.** A reward touches at least three of: ruler, realm, other characters, map, culture, religion, future decisions.
5. **Nothing is clickable at game start.** Progression gates are earned: land, titles, buildings built, earlier accomplishments, traits/skills, prestige level.
6. **Traditions are upgraded, never piled on.** Replace a tradition the culture already has (`remove_culture_tradition` + `add_culture_tradition`, as vanilla does for Bushido) and keep every parameter of the old one.
7. **Events are chains**, in the spirit of "Theft at Court": bold one-line summary, 3-6 options, trait/skill/perk-gated options, readable labels on random outcomes, consequences that reach other characters and the map, roughly 40% negative outcomes, stress at most ~20 per event (miniscule/minor), repeated across story types.
8. Always read the game's `error.log` after the user tests (OneDrive Documents\Paradox Interactive\Crusader Kings III\logs\error.log) and fix every `eir_`/mod line.

## 2. The flavor loop (every major decision follows it)
1. **Hook** - shown once the player is close, so they know what to aim for.
2. **Gate** - `is_valid` lists several concrete things (see lever menu). Show failures with tooltips.
3. **Commitment** - a real cost in two or three currencies.
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
* Eire stage ladder: Stage 1 = 4 counties; Stage 2 = 10 counties + duchy + prestige level 2; Stage 3 = 20 counties + kingdom + prestige level 3; Stage 4 = holds the top kingdom + prestige level 4.
* Cost tiers for a tribal-friendly mod (prestige-led): Stage 1: 150-300 prestige, 100-200 gold. Stage 2: 400-900 prestige, 200-400 gold, 100-300 piety. Stage 3: 1000-1500 prestige, 300-600 gold, 200-400 piety. Stage 4: 2500-4000 prestige, 800-1200 gold, 500-600 piety.

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
1. Did the player need to do at least three separate things to reach this?
2. Is the cost in line with the nearest vanilla equivalent and tribal-friendly (prestige-led)?
3. Does the reward touch at least three categories, one of them outside the ruler?
4. Is there a ceremony event with 3+ real options, gated by traits/skills?
5. Does someone else react (opinion, claim, event, faction)?
6. Is there a downside, and a remedy that can beat the downside?
7. Does it leave a memory (nickname, legend, artifact, modifier, landmark)?
8. Does it unlock or lead to something else?
9. Does it work for tribal and feudal rulers?
10. Is it unique-once-per-game when it should be (Rule 1)?
11. Validator clean; `error.log` clean after testing.
