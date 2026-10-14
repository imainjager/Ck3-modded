# Celtic tenets (Update 7, v0.13)

Fifteen tenets that work **both ways**, as in the base game: a ruler can hold one as a **personal tenet** (the `personal_tenet_modifier` and the personal flag) and a faith can take it as one of its **faith tenets** when it is created or reformed (the `character_modifier`, `county_modifier` and the faith parameter).

They are **locked at the start of the game**. Each is unlocked by one decision (a global variable `eir_tenet_<name>`); until then it is hidden from the faith screen and cannot be picked as a personal tenet. The decision also fills a free personal tenet slot with the new tenet at once, if the ruler has one. Each tenet also has a decision of its own, shown only to a ruler who has the tenet (personal or faith), which fires a short event (0970-0984).

| Tenet | Unlocked by | Decision it adds | Meaning |
|---|---|---|---|
| The Oak and the Rite | Mystical Celtic Warriors | Sit Beneath the Oak | Rulers keep the old groves, the quarter-day fires and the oaths sworn beneath the oak. The bishops tolerate it because the harvest is good. |
| Warden of the Wood | The Return of the Celts to Germany | Call the Hunt | The forest is a temple and its guardians are warriors. Foes who enter it do so by leave of the wardens, who are not generous. |
| The High King's Circuit | The Last Revenge of the Celts | Ride the Circuit | A king who is not seen is not king. The ruler rides the circuit of the realm, eats at every hall and hears every complaint, and is believed. |
| Brehon's Peace | The Gaelic Kingdoms United | Pronounce a Judgement | The quarrel is settled by the judge and not by the sword. A death costs a price in cattle, and a refuge cannot be violated. |
| Voice of the Gael | The Return of the Celts to the Mainland | Send Out the Poets | The language is the nation. Poets, harpers and hospitality carry it from hall to hall, and no stranger leaves without learning a verse. |
| Vow of Vercingetorix | The Return of the Celts to France | Swear the Vow on the Hill | Every free man swears on the hill that he will not yield the land. The oath is old, hard to keep and harder to break. |
| Pilgrim and Relic | The Brooch of Avalon | Send a Monk Overseas | The road to the saint is a sacrament. Monks cross the sea to carry the faith, and the relics they bring home make the home they came from holier. |
| Brennus' Reckoning | The Return of the Celts to Italy | Name the Ransom | Rome was sacked once by Celts, and it paid in gold. Every city is a purse, every siege an invoice, and the rulers believe that nobody who can pay should be spared. |
| Galatian Syncretism | The Return of the Celts to Galatia | Write to the Galatians | The Galatians kept the old gods in the shadow of the new faith for four hundred years, and the saints wear their faces. The clergy find it useful. |
| Salt, Silver and Hearth | A Third of the Island | Open the Salt Roads | The wealth of the island is salt from the shore, silver from the hills and a fire that never goes out in the mead-hall. A ruler who keeps all three is rich. |
| Hero's Fury | The Mail of the Pendragon | Take the Hero's Portion | At the height of battle a hero turns into something else. The ruler's warriors believe it and fight as if they have seen it. |
| The Fianna Camp | Rhongomyniad, the Spear of Badon | Raise the Fianna Camp | The young nobles live a winter in the forest, hunting, fasting and fighting. They return trained, and they remember who fed them. |
| The Grail Quest | Revive the Arthurian Legend | Set Out on the Quest | Somewhere in the island is a vessel that heals the land. A ruler who sets out to find it is rarely rewarded, but never forgotten. |
| Geis and Omens | The Round Table | Take a Geis | Every great ruler lives under a geis, a taboo that gives strength and carries a price. Omens warn of the day it will be broken. |
| The Heavy Crown | The Crown of Britain | Wear the Heavy Crown | The crown that is worn is the crown that is feared, and the one who wears it is never again at ease. Prestige is great and the heirs resent it. |

Files: `tools/tenet_data.py` (all the data), `tools/gen_tenets.py` (tenet and trigger files), `tools/dec_v13.py`, `tools/ev_tenet.py`, `tools/v13_world.py`. How the game's own tenets work: `docs/TENETS_NOTES.md`.
