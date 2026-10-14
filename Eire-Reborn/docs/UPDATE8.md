# Update 8 (v0.14.0): the new systems

Built on top of the snapshot `snapshot-v0.13.2-before-update8` (a git tag, and a zip in `CK3 modding backups`). To go back: `git checkout snapshot-v0.13.2-before-update8` or unzip the backup over the mod folder.

Needs a **full game restart** (new folders and files).

## What was added

| System | What | Where |
|---|---|---|
| **Activities** (6) | Óenach, Quarter-Day Festival, Feis of Tara, Irish Pilgrimage, Great Hosting, Bardic Contest. Each has a scale option (modest, full, grand) and a focus option, 9 pulse events (about 40% bad), 3 intents, an opening and a closing story. The AI never hosts them (so no load, no surprises) but comes as a guest. | `tools/act_data.py`, `gen_activities.py`, `ev_u8c.py` |
| **Culture** | Ten regional innovations (Ringfort Craft, Fosterage Networks, Ogham Script, Insular Scriptoria, Currach Craft, Brehon Law, Round Towers, Bardic Colleges, Gallowglass Hosting, Tanistic Succession). They carry no era flags, so they do not change how fast a culture advances. | `gen_culture.py` |
| **Court positions** (4) | Ollamh, Brehon, Druid, Aite (foster-father), each with aptitude, five modifier levels, salary and three events. | `gen_court.py`, `ev_u8b.py` |
| **Casus belli** (3) | Cattle Raid (plunder a neighbouring county, no land), Demand the Cáin (a tribute war: gold, a hook, ten years of tribute), Claim of the Kindred (a county claim against a kinsman). The AI never uses them. | `gen_cb.py` |
| **Religion** | Twelve Irish holy sites; the **Druidic faith** (under the generic paganism religion, with Celtic gods); the **Culdee Reform** (a rite of the Christian or Catholic faith, made when you found it). Decisions: Kindle the Old Fires, Return to the Cross (the remedy), Found the Culdee Reform. | `gen_religion.py`, `dec_v14.py`, `ev_u8.py` |
| **Struggle** | The Fragmentation of Ireland: three phases (Kin-Strife, Rise of the Overkings, Truce of the Saints) and two ending decisions (the High Kingship, the Concord of the Saints). It starts for a player of a Gaelic culture who does not yet hold half of Ireland, and only if the Fate of Iberia struggle feature is present. | `gen_struggle.py`, `ev_u8b.py` |
| **Road tracker** | The decision "Where Stands the Road?" shows the next step of the purple road. Every step now leaves a flag. | `dec_v14.py`, `ev_u8.py` |
| **Art** | Procedural icons and scenes for the activities, option categories, phases and court positions (original, uncompressed). | `tools/make_icons.py` |

Not added, and why: **dynasties and houses** (the base game already has thousands, including the Irish ones), **tanistry as a law** (the base game has it: the Gaelic Elective succession law), **history files** (you asked me to skip them), **a GUI window** (you chose the decision-based tracker).

## Safety nets in this update
* `tools/check_u8.py`: braces balance in every new file; every key the new systems use has localization; every art file, animation, environment and sound named exists in the base game or the mod; holy-site baronies sit in their counties.
* `tools/token_check.py` now covers every folder under `common/` (so activities, religion, culture, casus belli, court positions, struggles are checked against the base game's own script).
* `tools/audit_decisions.py` still passes (177 decisions, all reachable).
* The AI is kept out of the new activities and casus belli on purpose.

## Checklist for the first game (10 minutes)
1. Start the game with the mod on, load or start a Gaelic ruler, and open `error.log` (Documents/Paradox Interactive/Crusader Kings III/logs): send it to me.
2. Open the **Activities** window (the Activities button): the six Irish ones should be listed. Plan an Óenach: pick scale and focus, choose a location, invite guests.
3. In the decisions list: **Where Stands the Road?** (free) should show your next purple step.
4. Open the **Court** window, **Court Positions**: the Ollamh, Brehon and Aite should be listed (the Druid only after Kindle the Old Fires, or with the Oak and the Rite tenet).
5. Open the declare-war window against a neighbour: **Cattle Raid**, **Demand the Cáin** and **Claim of the Kindred** should be offered where the conditions hold.
6. Open the **Faith** screen: Druidry should exist (no followers yet). Its holy sites are Irish.
7. If the struggle starts, a notice appears in the **Struggles** window within a year.

## If something goes wrong
* A crash on load: send the last lines of `error.log` and `crash` folder if there is one. The likeliest suspects are the faith, the rite or the struggle; each of them is one generator, and I can switch any of them off by removing it from `tools/build_all.py` and rebuilding.
* A missing icon or blank art is harmless; it only logs.

## Update 9 (v0.15-0.16): raids and expeditions
* Raiding: 26 new raid events (Gaelic and Brythonic only; tools/ev_u8d.py, relays in tools/gen_script_raid.py), three casus belli (Avenge the Raid, Demand the Blood-Price, Drive Out the Settlers; tools/gen_cb2.py) and the raiding tradition line (Bo-aire, Tain Bo, Raiders of the Four Seas).
* Sponsor an Expedition (tools/gen_expedition.py): a vanilla option-list widget decision; the war is a script-only conquest CB; the base game does not change culture or faith after a conquest, so eir_expedition_victory_effect does it.
* Untested in the game: random_county_in_region, the option-list widget, the landing (create_title_and_vassal_change independency), and every raid scope. Read error.log first.
