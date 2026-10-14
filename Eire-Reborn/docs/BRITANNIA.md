# The road to the whole island (Update 4, v0.10)

Ten new decisions, one yearly culture-change engine and five super buildings. The Empire of Britannia in the game has **93 counties** (England 40, Scotland 26, Ireland 14, Wales 13), so 30% is **28**, 60% is **56** and 95% is **89** (the numbers are read from the installed game when the mod is built). Ireland has only 14 counties, so the old "25 counties in Ireland" requirement of *End the Tanistic Fragmentation* is now **10**.

| # | Decision | Requirements | Main rewards |
|---|---|---|---|
| 1 | **A Third of the Island** | an Irish king; 28 of 93 Britannic counties | Gaelic Ascendancy (50 years), massive prestige, Pride of the Island in every Britannic county you hold |
| 2 | **The Gaelic Kingdoms United** | decision 1; a Gaelic king; hold both the Kingdom of Ireland and the Kingdom of Scotland | second Ascendancy; half of the non-Gaelic counties of Ireland and Scotland take your culture at once; a claim on the Empire of Britannia |
| 3 | **Revive the Arthurian Legend** | decision 2; prestige level 4; 1000 piety | a mythical heroic legend (if the legends feature is on), the unique sword **Caliburn** (prowess +10, knights +30%, prestige +1.5, and more), Arthur Reborn for 40 years |
| 4a | **The Mail of the Pendragon** | decision 3; Cornwall; Tintagel built; prestige level 4 | the armor **Mail of the Pendragon** |
| 4b | **The Crown of Britain** | decision 3; every county of Wales; Caerleon built; 3500 prestige | the crown **Crown of Britain** (prestige +2, legitimacy +50%, grandeur +20) |
| 4c | **The Brooch of Avalon** | decision 3; Somerset; a monastery of your own; 3000 piety | the **Brooch of Avalon** |
| 4d | **Rhongomyniad, the Spear of Badon** | decision 3; 56 of 93 counties; Martial 24 | the spear **Rhongomyniad** |
| 4e | **The Round Table** | decision 3; ten knights; Hall of Tara built; Diplomacy 22 | **The Round Table** |
| 5 | **The Last Revenge of the Celts** | decision 3; a Gaelic king; 89 of 93 counties | third Ascendancy, Lord of the Whole Island (50 years), a nickname, double massive prestige, and a **super special building** you place yourself at Winchester, York, Edinburgh, Caernarfon or Bath (about 2.5 times a wonder, with its own stationed men-at-arms bonuses) |

The five paths (4a-4e) are **shown as soon as decision 2 is done** but can only be taken once decision 3 is done. Each costs 800-2500 gold, 1500-3500 prestige and 300-800 piety.

## The culture-change engine
Each Ascendancy modifier makes every foreign (non-Gaelic, non-Brittonic) county of Britannia in your realm roll once a year to take your culture: 1% a year, +5% with the first, +5% with the second, +6% with the third (up to 17% a year). Every county that changes:
* takes your culture (your *primary* culture),
* gets the **Saxon Uprising** county modifier for 20 years: **-50 county opinion**, -0.6 control growth, -20% tax and levies,
* raises the existing re-Celticisation unrest chain (the Saxons mutter, a thane calls the moot, fire in the marches), and
* the first conversion in any four years fires **The Saxons Rise** (event 0800), which has *already* cost the county control and given it a rebel-march modifier before you choose how to answer. The uprising is therefore guaranteed, but it is an unrest event with consequences, not a spawned rebel army (those I left out on purpose, to keep the game stable). Say so if you want real rebel armies.

## Files
Decisions `tools/dec_v10.py`; events 0800-0820 `tools/ev_brit.py`; script (30/60/95% triggers, conversion pulse) `tools/gen_script_brit.py`; modifiers and Arthurian items `tools/v10_world.py`; the five final buildings `tools/bld_data.py` (FINAL_SITES).
