# The Conquerors (Update 3, v0.9)

Five one-time invasions for a Gaelic ruler who holds the Kingdom of Scotland or the Kingdom of Ireland (at least 3 of its counties, with the kingdom title in your realm). Each brings about **8,500-9,000 men** (5,000-5,500 levies plus 28-30 regiments of men-at-arms), a king's whole host with an "Emboldened" edge (advantage, levies, knights), and a claim war for the **kingdom title**. They land on a coastal county of the target, not on your capital.

| # | Earliest | Conqueror (culture) | Prefers | What he wants |
|---|---|---|---|---|
| 1 | 900 | The English King (West Germanic) | Scotland | to make it an English shire, tongue and tithe |
| 2 | 950 | The Norse Sea-King (North Germanic) | Ireland | the east coast, from the Liffey to the Shannon |
| 3 | 1000 | The King of the Old North (Brittonic) | Scotland | the lands from the Forth to the Humber, as the poems say |
| 4 | 1050 | The Earl of the Isles (North Germanic) | Scotland | the western coast and the Isles |
| 5 | 1100 | The King's Marshal (English or Frankish) | Ireland | the east of the island, in castles |

The conqueror is a real AI ruler of that culture group (the strongest tends to be picked), so the world must still contain one; if none exists nothing happens and the roll is tried again next year.

## When they come
A 10% chance each year once the start year is reached, the previous conqueror has already come, and 40 years have passed since the last one. So if you are already past 900, the first one is already rolling; the others follow about 50 years apart. Only one conqueror can be active at a time, and you must be independent and at peace.

## What you can do
Each arrival event offers five answers: refuse and call out every vassal; parley (diplomacy; success delays the landing three years and gives you foreknowledge, failure emboldens him); **pay the tribute** (800 gold and a long shame, and no war); call the kings (a free allied army, needs a kingdom); or strike first (a raid; success demoralises his host, failure emboldens it). About half a year into the war a second event offers scorched earth, mercenaries, the relics, or a champion's duel.

## If you win: "beat the warlord"
Massive prestige, piety, a 25-year *Bane of ...* modifier, a *Liberated County* modifier on every county of the kingdom you hold (15 years), and a choice: the **Warlord-Slayer** nickname with a legend, a ransom, a feast for the liberated counties, or a poem and the conqueror's own sword (an artifact).

## If you lose: the disaster
Every county of the target kingdom held by your realm or the conqueror: **-1 development** (a third lose a second level), a 20-year *Ravaged* modifier (tax, development growth, opinion, control, levies), **45% chance of changing to the conqueror's culture**, and in 60% of provinces every regional building chain is **downgraded a level**. You also lose prestige and take stress. Then you choose: swear to rebuild, take to the hills, flee with the relics, or beg for terms.

## The remedy
The decision **Rebuild the Ravaged Counties** (300 gold, 200 prestige, 50 piety) strips the Ravaged modifier from every county, gives each *Rebuilt Stronger* for 15 years and a level of development back, and pays extra prestige, piety and honour if you swore to rebuild. (Re-Celticisation decisions, such as Reclaim the Tongue, win the culture back.)

Events: 0610-0655 (per conqueror k: 06k0 arrival, 06k1 victory, 06k2 defeat, 06k3 mid-war, 06k4 and 06k5 hidden). Data: `tools/conq_data.py`; scripts: `tools/gen_script_conq.py`; events: `tools/ev_conq.py`.
