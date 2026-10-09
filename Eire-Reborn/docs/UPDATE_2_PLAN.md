# Eire Reborn: UPDATE 2 (planned, NOT yet executed)

Collected from the user's play-test (869-870 AD, Irish tribal chieftain) while the game was running. Nothing here has been applied.
Reference numbers come from the vanilla files (see `docs/VANILLA_REWARD_CATALOG.md`).

## 1. Buildings

### 1.1 Broken names and descriptions (seen in the duchy-building window)
The window shows the raw keys `building_type_eir_rightech_01` and `building_type_eir_rightech_01_desc`. The game wants `building_type_<key>` and `building_type_<key>_desc` for the header and description. I wrote only `building_<key>` (which does show up as "Level I: Righteach"). Fix for all 51 buildings (the older eight too): add both key forms, and write a real description that says what the building is and does.

### 1.2 Tribal rulers cannot find any Eire building in the build menu
* The duchy buildings DO appear for the tribal holder (screenshot: Righteach and Dún of Leinster in "Construct New Duchy Building").
* The ordinary holding menu (Gabhrán, tribal hold) shows Palisades and War Camps; none of the 14 Eire regular buildings is visible (the list scrolls, so check below the fold first).
* Likely cause: my regular buildings use a non-standard tribal check. Vanilla tribal buildings use a proven pattern.
* Fix: rebuild a good chunk of the regular buildings as tribal buildings on vanilla's pattern:
  `is_enabled = { building_requirement_tribal = yes }`, `can_construct_potential = { has_building_or_higher = tribe_01 }`, costs `cost_gold = tribal_building_tier_N_cost` + `cost_prestige = expensive_building_tier_N_cost`, and levies from the `*_building_levy_tier_N` values.
  Keep the existing castle/city/church versions for feudal holders with `building_requirement_tribal = no`.
* Candidates for tribal versions (make at least 8 of the 14): Dún, Booley Pastures, Fosterage Hall, Bruidhean, Aonach Fair, Smithy of Goibniu, Hobby Stables, Holy Well, Hermitage, Ogham Pillar Field, Pilgrim Hospice, Monastic School.
* Vanilla tribal chain costs and effects for calibration: tier 1 = 75 gold + 200 prestige, tier 2 = 100 gold + 350 prestige; typical L1 effects: Palisades fort level +1, defender advantage +2, levies; War Camps knight limit +1, knight effectiveness +10%; Longhouses county control +0.2/month and prestige +0.25/month; Market Villages income +0.4/month.

### 1.3 Cost-to-benefit is far off vanilla
Seen: *Righteach* costs 340 gold + 300 prestige and gives +2% development growth; *Dún of Leinster* costs 500 gold + 500 prestige for +4% holding taxes. Vanilla duchy buildings are three-level chains:

| Level | Gold cost | Duchy-wide development growth | Duchy county opinion | Court grandeur |
|---|---|---|---|---|
| I | 485 | +10% | +5 | +4 |
| II | 725 | +20% | +10 | +8 |
| III | 1100 | +30% | +15 | +12 |
(Other families: tax assessor +15/20/30% tax; royal forest income 0.8/1.1/1.4 with +10/20/30% growth; great megalith +15% growth with +10 opinion at level I.)
So we charge less gold, add a prestige price, and give a fifth of the benefit. Fix:
* Make every duchy building a **3-level chain** (01, 02, 03) using vanilla's costs (485/725/1100 gold; for tribal rulers, swap part of the gold for prestige, because tribal gold is scarce) and vanilla's benefits (development growth 0.1/0.2/0.3, county opinion 5/10/15, grandeur 4/8/12, plus one flavor effect per building).
* Specials: vanilla costs 500-1000 gold (Visby 500; Doge's Palace and cathedrals 1000) for county development growth +10-30%, income +2 to +5/month, county tax +15-20%, county opinion +5, character piety +0.25 to +1/month. Match that scale; keep a prestige cost only where it adds to the flavor.
* Regular buildings: vanilla level I costs 100-150 gold (tribal 75 gold + 200 prestige), gives income +0.25 to +0.7/month, county development growth +0.05, county control +0.1/month, piety +0.1/month; level II is about 1.6 times level I. Rebase ours the same way.
* Rule going forward (add to the flavor guide): **a building's price and benefit must sit on the vanilla line for its tier** (cost per unit of benefit within about 25% of vanilla), unless a unique effect justifies it.

## 2. Requirement text (the "BUG: missing localization" lines)
Wrap every count-style or unlabelled requirement in readable text: realm size, ports, Irish buildings built, vassal counts, `has_global_variable` gates, the coastal check and the stress check. See memory note `eire-pending-fixes`.

## 3. Early game
Add chieftain-level events and stagger the first years so a one- or two-county ruler gets story from the start.

## 4. Other notes
* Eire Reborn log at 18:44 is clean apart from the tooltip text above.
* The user is playing with debug mode on (10,000 gold, 51,000 prestige); balance numbers should be judged against normal play.
