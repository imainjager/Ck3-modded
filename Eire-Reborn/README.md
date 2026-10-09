# Eire Reborn: An Irish Flavor Pack (CK3 mod)

Makes the Irish campaign feel complete: a brutal tanistry rule, a long road to a united Ireland, and a Celtic revival that reaches Wales, Alba, Cornwall and Brittany.

## The core rule
When an Irish-culture ruler dies, their **top title (duchy or higher) is destroyed**. Kingdoms unravel every generation. You break the cycle with the decision chain: hold an Óenach, be crowned at Tara, then **End the Tanistic Fragmentation**.

## What is in it
- **53 decisions** in seven paths (incl. two for foreign rulers of Celtic land): Statecraft, Culture, War, Celtic Revival, Faith, Kingdoms and Places. Most are gated by global unlock variables (`eir_done_*`, `eir_unlock_*`) that persist across succession.
- **77 events**: tanistry fallout, Viking and Norman invasions (spawned armies + claim wars), seasonal festivals, folklore, Brehon law, church, history (867-1169), Celtic diplomacy, and artifact rewards.
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

## Added in v0.2
- **Native resistance**: every Gaelic/Brythonic county held by a foreign-culture ruler gets a yearly-refreshed modifier (Irish counties strongest; Wales, Alba, Cornwall, Brittany, Man weaker): lower county opinion and slower control, so revolts are more likely. Conquerors can still win wars; they just pay for the peace. Decisions: *Make Peace with the Natives* / *Burn the Hills*.
- **867 start**: 8 dated events 867-1066 (Dublin longphort, Cerball of Osraige, return of the Norse, Tara 980, Brian Boru, Clontarf, aftermath, Diarmait of Leinster). Foreign (Norman) invasions begin 1090.
- Coronation chains behind every kingdom/empire decision (events 0110-0112) and **legend seeds** (great-deed legends, only if the Legends feature is on).
- 3 more artifacts (Cathach, Great Brooch, Cross of Cong) via the vanilla-style creation call.
- Resistance, court and Celtic-world events (Man, Cornwall, Brittany, Wales).
- Deliberately NOT done (crash risk): custom court type/positions, custom legend types, holy orders, accolades, struggles, hegemony.
