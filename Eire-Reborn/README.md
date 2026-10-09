# Eire Reborn: An Irish Flavor Pack (CK3 mod)

Makes the Irish campaign feel complete: a brutal tanistry rule, a long road to a united Ireland, and a Celtic revival that reaches Wales, Alba, Cornwall and Brittany.

## The core rule
When an Irish-culture ruler dies, their **top title (duchy or higher) is destroyed**. Kingdoms unravel every generation. You break the cycle with the decision chain: hold an Óenach, be crowned at Tara, then **End the Tanistic Fragmentation**.

## What is in it
- **116 decisions** in eight paths (incl. two for foreign rulers of Celtic land): Statecraft, Culture, War, Celtic Revival, Faith, Kingdoms and Places. Most are gated by global unlock variables (`eir_done_*`, `eir_unlock_*`) that persist across succession.
- **99 events**: tanistry fallout, Viking and Norman invasions (spawned armies + claim wars), seasonal festivals, folklore, Brehon law, church, history (867-1169), Celtic diplomacy, and artifact rewards.
- **10 culture traditions**, **4 unique men-at-arms** (Gallowglass, Fianna warband, Kern javelineers, Tara Guard), **8 unique buildings**, **8 fame traits**, ~75 modifiers, 14 opinion modifiers.
- **New titles**: Kingdoms of Munster, Ulster, Leinster, Connacht, Meath, Dál Riata, and the Empire of Gaeldom.
- Remedies exist for the negative outcomes (about 40% of choices cost something).

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

### Buildings
`tools/gen_buildings2.py`: 14 regular buildings (tribal-friendly), 10 duchy-capital buildings, 19 special buildings tied to real baronies. Special buildings now show in their barony from the start and list their requirements in the build tooltip.

### Tools
`python tools/build_all.py` then `python tools/validate.py` (checks braces, traits, modifiers, events, effects, triggers, variables, localization format, BOMs, unused modifiers and variables, effects inside trigger blocks).

## Version history
- 0.1 tanistry, Viking and Norman invasions, folklore, church events, traditions, buildings.
- 0.2 native resistance, 867-1066 history, coronation chains, legends, artifacts.
- 0.3 100-ideas pack. 0.4 prestige-cost buildings.
- 0.5 bug-fix release from the first real error.log (localization newlines, vanilla on_action conflicts, trait icons, duplicate keys) and a full progression rewrite of decisions, traditions and buildings.
