# Interactive Events (CK3 mod)

Before writing or changing any event, read `docs/EVENT_DESIGN_GUIDE.md`. It holds the design rules, the 40% negative-outcome
rule, the technical gotchas, the naming conventions, and the reference story (Theft at Court).

Quick reminders:
- The owner is new to modding: explain in plain language and keep steps small.
- New files need a full game restart; edits to loaded files can be hot reloaded.
- Verify every script name against `C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game` before using it.
- After the owner tests, read the game's `error.log` (OneDrive Documents path).
- Commit and push after each working change. The remote is `imainjager/Ck3-modded`.

## Flavor rules (read first)
Before creating or changing any decision, event, tradition, building or unit, read `docs/FLAVOR_GUIDE.md` and run its shipping checklist.
