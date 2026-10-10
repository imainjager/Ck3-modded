# Eire Reborn - working notes
- Script and localization are generated: edit `tools/*.py`, then run `python tools/build_all.py` and `python tools/validate.py` (must show 0 errors). Never hand-edit generated files in `common/` or `events/` (except hand-written: scripted_triggers, scripted_effects, on_action).
- UTF-8 with BOM for script/loc; `descriptor.mod` WITHOUT BOM.
- Unlock progress lives in GLOBAL variables so it survives succession. Saved scopes do not survive delayed events.
- Design rules (from the user): bold one-line summary on each event, 3-6 options, trait/skill-gated options, readable outcome labels on random_lists, stress <= ~20 (minor/miniscule only), consequences reach the world, ~40% negative with a remedy.
- Hot reload only works for already-loaded files; new files need a restart.

## Flavor rules (read first)
See `../docs/FLAVOR_GUIDE.md`. Unique decisions once per game; prestige-led costs for tribal rulers; every negative has a remedy that can beat it; ceremony + reaction + memory on every major decision.

## Update 2 (v0.8) tooling and lessons
- Run all four after every change: `python tools/build_all.py`, `python tools/validate.py` (0 errors), `python tools/token_check.py` (only culture-parameter names may be listed), `python tools/audit_buildings.py` (0 problems); `python tools/dead_events.py` finds events nothing fires.
- Requirement tooltips: decision `is_valid` statements are wrapped in `custom_description` automatically by `tools/reqtext.py`. A new trigger shape needs a sentence there (build prints `UNWORDED requirement`).
- Buildings: data in `tools/bld_data.py`, generator `tools/gen_buildings3.py`. Special buildings need a province slot (`history/provinces/eir_special_slots.txt`, generated) and a barony id that exists in vanilla `landed_titles` (b_tara is in Siberia!).
- Black Host chain state: character variables `eir_bh_stage` (1 wave 1 landed ... 6 over), `eir_bh_wins`, `eir_bh_losses`, `eir_bh_prep`; hidden relay events 0394-0399 pick the warlord and carry the scopes; timeouts end stalled waves.
- Lifestyle traits with several XP tracks need `track =` (hunter: hunter; traveler: travel); gen_events adds it.
- New folders (history/) and files need a full game restart.
