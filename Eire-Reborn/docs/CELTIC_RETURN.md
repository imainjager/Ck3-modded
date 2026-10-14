# The Return of the Celts (Update 6, v0.12)

A late-game chain for an **Irish emperor** who holds **all 93 counties of the Empire of Britannia**. Thresholds are read from the installed game when the mod is built.

| # | Decision | Requirements | Rewards |
|---|---|---|---|
| 1 | **Mystical Celtic Warriors** | Irish emperor; 93 of 93 Britannic counties; 5000 prestige | the tradition *Mystical Celtic Warriors* (see below), the Forest Warriors, the Sacred Grove building, +25% development growth and no forest penalty in every Britannic county you hold |
| 2 | **The Return of the Celts to the Mainland** (shown only after 1) | decision 1; 3000 prestige; 1000 piety | prestige, piety, a 50-year modifier; unlocks the five decisions below |
| 3a-e | **The Return of the Celts to France / Germany / Spain (Iberia) / Italy / Galatia** | decision 2; a share of the counties of the region (see table); two minor requirements each | a claim on the empire (Galatia: the Empire of Byzantium), plus a 50-year modifier: every foreign county of the region in your realm has a **6% chance a year** to take your culture (the same 500% pace as the Britannia Ascendancy), each one resisting with -30 opinion for 15 years |
| 4a-e | **The Celts Return to ...** (shown after 3) | a larger share of the counties of the region; one minor requirement | **half** of the foreign counties of that region in your realm take your culture at once; a 50-year modifier; double massive prestige |

| Region | Area counted | Claim decision | Restoration decision |
|---|---|---|---|
| France | Empire of France (109) | 14 counties; prestige 6000; martial 22 | 30 counties; piety 1500 |
| Germany | Empire of Germany (147) | 12 counties; prestige level 4; martial 26 | 36 counties; prestige 4000 |
| Spain (Iberia) | Empire of Spain (87) | 11 counties; piety 2500; a monastery of your own | 27 counties; stewardship 20 |
| Italy | Empire of Italy (53) | 8 counties; diplomacy 24; prestige 5000 | 21 counties; prestige 3000 |
| Galatia | Kingdom of Anatolia (19) | 6 counties; learning 20; prestige 5000 | 12 counties; martial 24 |

Spain and Iberia are the same empire in the game (Portugal is inside it), so they are one decision; Galatia is the fifth.

## The tradition: Mystical Celtic Warriors
Added to your culture by decision 1 (hidden from the tradition picker). Effects: -20 opinion from characters of other cultures, +10 advantage in counties of your heritage, -40% faith conversion piety cost, +5 forest advantage, small prestige and knight bonuses. Parameters: easier and cheaper to hybridise, cheaper to convert to the local culture (this is how the game expresses "diverging a culture"; the game has no modifier that makes founding a faith cheaper, so conversion cost is what I changed).

## The Forest Warriors
Skirmishers, 35 damage, 20 toughness, 15 pursuit, 20 screen (the stat you forgot is screen; say if you want a different number). Terrain: +20 damage in forest, +20 in jungle, -20 in desert, +5 in plains, +10 in hills. Only cultures with the tradition can recruit them.

## The Sacred Grove (Nemeton)
A regional building (castle, church and city holdings, a 2-level tribal and a 4-level feudal version): **+25% development growth** at every level, plus stationed skirmishers' damage, levies, piety, knight effectiveness, health and legend spread.

## Britannia-wide
A yearly pulse puts *Realm of the Oaks* (+25% development growth, +50% forest development growth, +3 opinion) on every county of Britannia held by a ruler whose culture has the tradition.

Files: `tools/celt_data.py` (the table), `tools/gen_script_celt.py`, `tools/dec_v12.py`, `tools/ev_celt.py` (events 0950-0961), `tools/v12_world.py`.
