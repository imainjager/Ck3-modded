# Eire Reborn: An Irish Flavor Pack (CK3 mod)

Makes the Irish campaign feel complete: a brutal tanistry rule, a long road to a united Ireland, and a Celtic revival that reaches Wales, Alba, Cornwall and Brittany.

## The core rule
When an Irish-culture ruler dies, their **top title (duchy or higher) is destroyed**. Kingdoms unravel every generation. You break the cycle with the decision chain: hold an Óenach, be crowned at Tara, then **End the Tanistic Fragmentation**.

## What is in it (v0.8)
- **136 decisions**: the chieftain's first rungs, the statecraft ladder, the Norse struggle, conquest and culture in Britain, kings against kings, faith, kingdoms and places. Costs are explicit; prestige leads for tribal rulers.
- **300 events** (including a three-wave Norse invasion with real armies, lesser invasions by Britons, Albans, Irish rivals and Hebridean reavers, chieftain-level stories for the first years, ceremonies for every major decision, and about 40% negative outcomes with remedies).
- **9 culture traditions** (six upgrades and a union tradition), **7 men-at-arms** (see `docs/UNLOCKS.md`), **24 regional building families** (each with a tribal and a feudal version), **10 duchy-capital chains**, **41 special buildings** at real baronies.
- **New titles**: Kingdoms of Munster, Ulster, Leinster, Connacht, Meath, Dal Riata and the Island of the Mighty, and the Empire of Gaeldom.
- Remedies exist for the negative outcomes.

See `docs/IDEAS.md` for the full catalogue, `CLAUDE.md` for how the generators work.

## Install / test
1. Mod is registered via `Documents/Paradox Interactive/Crusader Kings III/mod/eire_reborn.mod`.
2. **Fully restart CK3** (new mod and new folders are not hot-reloaded), enable it in a playset, start as an Irish ruler (e.g. 1066 or 1085).
3. Check `Documents/.../Crusader Kings III/logs/error.log` for script errors and report them.

## Untested / risky (verified statically only)
Runtime title creation (`can_create`), claim wars without a CB, adding a tradition at runtime, building icons (no art), destroy_title in `on_death`, artifact types (`book`).

## Rebuild
```
cd tools
python build_all.py
python validate.py
python token_check.py     # every effect/trigger word must exist in the base game
python audit_buildings.py # building cost/benefit audit
python dead_events.py     # events nothing fires
```

## How progression works (v0.5 rewrite)
Nothing is clickable at game start. Every decision sits behind a stage (see `common/scripted_triggers/eir_triggers2.txt`):
1. **Chieftain**: 4+ counties. 2. **Duke**: 10+ counties and a duchy. 3. **King**: 20+ counties and a kingdom title. 4. **High King**: holds the Kingdom of Ireland.
On top of the stage, each decision asks for specific things: Irish buildings built (`eir_irish_buildings_trigger`), ports, named titles, earlier decisions, piety/prestige thresholds and traits. Costs are explicit gold, prestige and piety (the game's `*_gold_value` scales with income and is tiny for a tribal chief).

### Traditions are upgrades, not additions
Four Irish traditions are REPLACED (the vanilla one is removed and the Eire one, which keeps every vanilla parameter and adds more, is added):
| Decision | Replaces | Gives |
|---|---|---|
| Charter the Schools of the Fili | Poetry | Schools of the Fili: Fianna warbands, bardic school building, more legend spread, learning |
| Codify the Bo-aire | Pastoralists | Bo-aire: the Cattle Lords: cattle enclosure, income, stewardship |
| Endow the Monastic Cities | Monastic Communities | Insular Monasticism: piety, clergy opinion, monastic cities |
| Claim the Irish Sea | Maritime Mercantilism | Kings of the Irish Sea: gallowglass, Irish Sea Quay and Longship Yard, stewardship |
Two hidden traditions run the tanistry rule (`tradition_eir_tanistic_fragmentation`, `tradition_eir_high_kingship`).

### How the top-title rule works
`on_death` (via `eir_on_death`) checks: the dying ruler is Irish culture, the global variable `eir_collapse_abolished` is NOT set, and their primary title is a duchy or higher. It then destroys that title and fires the heir event. The decision "End the Tanistic Fragmentation" sets the global variable and swaps the hidden tradition for Stable High Kingship. So it is a global switch, not a trait on the kingdom.

### Buildings (rebuilt in v0.8)
`tools/gen_buildings3.py` and `tools/bld_data.py`. 24 families, each as a **tribal** version (2 levels, vanilla tribal pattern: 75 gold + 200 prestige, then 100 gold + 350 prestige) and a **feudal** version (4 levels, vanilla cost curve 150 / 250 / 340 / 500). Stats are the vanilla medians for the same level times about 1.3, with a regional effect on top; `tools/audit_buildings.py` checks this and writes `docs/BUILDING_AUDIT.md`. Ten duchy-capital buildings are three-level chains (vanilla: 485 / 725 / 1100 gold; here half gold, half prestige). 41 special buildings sit in real baronies; a special building only exists on a province whose history declares its slot, so `history/provinces/eir_special_slots.txt` is generated too. Names and descriptions use the keys the game reads (`building_type_<first level key>` for the family, `building_<key>` for each level). Requirement text is readable (`custom_description`).

### Tools
`python tools/build_all.py` then `python tools/validate.py` (checks braces, traits, modifiers, events, effects, triggers, variables, localization format, BOMs, unused modifiers and variables, effects inside trigger blocks).

## Version history
- 0.1 tanistry, Viking and Norman invasions, folklore, church events, traditions, buildings.
- 0.2 native resistance, 867-1066 history, coronation chains, legends, artifacts.
- 0.3 100-ideas pack. 0.4 prestige-cost buildings.
- 0.5 bug-fix release from the first real error.log (localization newlines, vanilla on_action conflicts, trait icons, duplicate keys) and a full progression rewrite of decisions, traditions and buildings.

## v0.7: the long-look flavor pack
44 new events, 14 new decisions, 2 nicknames, 3 artifacts and about 45 modifiers, all built to `docs/FLAVOR_GUIDE.md` (Parts I-III). List: `docs/FLAVOR_v0.7.md`.
* **Re-Celticisation**: the decision *Reclaim the Tongue* turns a foreign-culture county in Britain to your culture; each conversion raises resentment, escalating through *The Saxons Mutter*, *A Thane Calls the Moot* and *Fire in the Marches*. The remedy *Grant the Saxon Moot* can leave you *Lord of Two Peoples*. Five conversions with peace unlock the unique *The Britons Return*.
* **Politics of the kindred**: the Derbfine assembles; a blinded cousin; the foster-brother; an improved pedigree; an oath-breaker.
* **The sea**: Norse settlers, rescued captives, a Norse-Gael bride, a storm.
* **The Church**: a relic from Iona, a monk who disagreed about Easter, pilgrims; decisions for the Hospice of Brigid and the Peregrini to Alba.
* **Cattle, law and seasons**: distraint by fasting, the murrain (remedy: buy Welsh cattle), the great cattle drive, summer pastures, the unpaid harper.
* **War**: the war-poet, the gallowglass captain's demand, the hostage exchange, the champion at the ford.
* **Celtic neighbours**: Welsh princes, Cornish tinners, Breton exiles, a Pictish stone, Galloway; decisions for Welsh archers and the College of Bangor.
* **Court and legend**: a prodigy at the harp, the Isles wedding, a ghost at Samhain, a comet, the Táin retold; a Bardic House and its High Poet's Chain; the Moot Horn.
* Flavor guard: a ruler gets at most one random flavor event a year (flag `eir_flavor_cd`).
- 0.6 ceremonies, reactions, nicknames and remedies for every major decision.
- 0.7 re-Celticisation of Britain, the kindred and the law, the sea and the Norse, faith, cattle and the seasons.
- 0.8 (Update 2) readable requirement tooltips, all buildings rebuilt (tribal and feudal, special slots fixed), the Black Host, lesser invasions, 36 new decisions, the Insular Union, the chieftain's early game.
