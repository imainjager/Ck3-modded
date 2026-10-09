# Eire Reborn - working notes
- Script and localization are generated: edit `tools/*.py`, then run `python tools/build_all.py` and `python tools/validate.py` (must show 0 errors). Never hand-edit generated files in `common/` or `events/` (except hand-written: scripted_triggers, scripted_effects, on_action).
- UTF-8 with BOM for script/loc; `descriptor.mod` WITHOUT BOM.
- Unlock progress lives in GLOBAL variables so it survives succession. Saved scopes do not survive delayed events.
- Design rules (from the user): bold one-line summary on each event, 3-6 options, trait/skill-gated options, readable outcome labels on random_lists, stress <= ~20 (minor/miniscule only), consequences reach the world, ~40% negative with a remedy.
- Hot reload only works for already-loaded files; new files need a restart.

## Flavor rules (read first)
See `../docs/FLAVOR_GUIDE.md`. Unique decisions once per game; prestige-led costs for tribal rulers; every negative has a remedy that can beat it; ceremony + reaction + memory on every major decision.
