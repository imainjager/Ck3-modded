# Interactive Events: Event Design Guide

This is the blueprint for every story in this mod. It records what we have decided, what a good event looks like,
how "Theft at Court" (the reference story) is built, and the technical lessons we learned the hard way.
Update it whenever a decision changes.

---

## 1. Why this mod exists

Vanilla CK3 has far too many events, and most of them are generic: you take something, you lose something,
and nothing changes. This mod replaces that with **stories**: connected events with real choices, consequences
that carry forward, and an ending that reflects how you played.

The quality bar: *if nothing about the character, the court or the map changes, it is not worth an event.*

## 2. The rules (from the project owner)

### Text
- Every event opens with **one short bold sentence** saying what is happening. Detail follows underneath.
- Option text must be understandable at a glance. Keep text readable, not long.
- Write with a personal, narrative voice (the vanilla "Staring at Stars" event is the tone to aim for).

### Options
- **Keep lists short: about 3 to 6 options.** More than that becomes a wall of near-identical text.
- Do not offer a menu of fates the game already has (execute, imprison, banish) as the whole event.
  Options must **move the story or change something**.
- Gate options by **skill, personality trait, perk, lifestyle trait or situation**. Players like seeing
  "available because of your diplomacy". Show only options the character qualifies for, except a few
  key ones (like declaring war) which show greyed out with the reason.
- Show **only one** personality-flavoured option at a time where several would overlap.
- Every random choice must have **readable outcome labels** (the `desc` on each `random_list` entry),
  never "nothing happens".

### Stress
- No more than about **20 stress per event, averaging about 10**. Use the `miniscule` and `minor` levels
  (10 and 20 gain; -5 and -15 loss). Never `major` (80).
- A choice that fits the character's traits relieves stress; a choice against them adds it.

### Consequences
- Almost everything should leave at least a slight mark on the world. Consequences can fall on anybody
  (the player, the court, vassals, foreign rulers, counties). Scale: medium to high.
- Carry choices forward with flags and counters so later events and the ending react to them.
- Use the full toolbox in section 6, not just gold and opinion.

### Balance: the 40% rule (new)
- **About 40% of choices or outcomes should cost the player something**, and the story, an event or a decision must
  offer a way to fix it. This is a general ratio, not a quota. Do not make everything negative.
- The fix should cost something too (gold, prestige, time, a risk), so the loop is worth playing.
- Pattern: **mistake, mark, remedy.** Examples already built: Laughing Stock is fixed by "Restore Your Good Name";
  Scarred County by "Rebuild the Marches"; Innocent Blood by "Reconcile with the Wronged House".

### Spam control
- A global cooldown flag on the player, a per-story cooldown, and one story at a time.
- Low-stakes choices get a "let my steward handle it" option.
- Minor follow-ups should be toasts or short events, not chains of pop-ups.
- Triggers must be tight enough that the story fires only when the choice is meaningful.

## 3. Anatomy of a story

A story is a **story cycle** (the game's personal story system, shown in the Situations tab) plus a set of events
that find their way back to it through variables.

```
Entry event
  -> Investigation (who you trust and how, gated by skills/traits)
       -> Success: culprit identified          -> Judgement (fates + story-moving options)
       -> Failure: wrong lead                   -> Dig deeper / punish the wrong person
  -> Escape routes (thief gets away)
       -> Abroad  -> negotiation / pressure / war / claims
       -> Vassal  -> domestic politics, faction, imprisonment
       -> Bandits -> hunt, pardon, hostage, knife, unrest, usurped county
       -> Sanctuary -> the Church gets involved
  -> Fallout (revenge, repeat offences, spent gold, unrest, vassal revolt, claim war)
  -> Ending dispatcher -> one of ten endings (+ fallback) -> decisions and lasting modifiers
```

Every story should have: an **entry**, **at least two investigation or approach styles**, a **wrong-turn branch**,
**at least two escape or escalation routes**, **fallout that reaches the map**, and **several endings**.

## 4. Reference story: Theft at Court

### Events

| ID | Name | Role |
|---|---|---|
| 0001 | A Hole in the Treasury | Entry. Choose how to investigate. One personality option shows (cruel, paranoid, merciful or open-handed) |
| 0020 | The Interrogation | Questioning the court yourself: intimidate, charm, logic, bait, conscience, bluff, harsh |
| 0013 | The Confession | The thief comes forward after amnesty or an appeal to conscience |
| 0002 | The Culprit Revealed | Judgement. Options depend on who investigated and the thief's motive |
| 0003 | A Convenient Culprit | Wrong lead. Punish the innocent, dig deeper, speak privately, trust instinct |
| 0004 | A Second Look | Dig deeper: riders, a trap, or give up |
| 0005 | The Truth Comes Out | The innocent is cleared. Admit it, blame the investigator, or double down |
| 0006 | The Thief Surfaces | Route 1: sheltered at a foreign court |
| 0007 | A Matter of Honor | The foreign ruler refuses: war, hook, allies, pay, claim, reparations, expose |
| 0030 | The Protected Thief | Route 2: a vassal shelters the thief, or paid for the theft |
| 0040 | The Bandit Chief | Route 3: the thief leads brigands in your realm |
| 0041 | The Usurper | The bandit chief seizes a county |
| 0042 | Sanctuary | Route 4: the thief takes refuge in a monastery |
| 0043 | A Vassal Raises a Banner | The defiant vassal starts an independence faction |
| 0044 | Unrest in the Countryside | Peasants near revolt |
| 0050 | A Pretender in Foreign Silks | A foreign ruler backs the thief's claim: claim war |
| 0051 | The Bounty Hunter's Price | The man who brought the thief in wants more |
| 0008 | Justice Delivered | Thief in your hands, from any route: execute, court trial, use him, mercy |
| 0009 | Stolen Gold, Spent Well | Unrecovered gold funds brigands in your realm |
| 0010 | Old Habits | A pardoned thief steals again |
| 0011 | A Blood Debt | A relative seeks revenge |
| 0090 | (hidden dispatcher) | Chooses the ending that fits what happened |
| 0100 to 0110 | Ten endings and a fallback | See below |

### Story variables
- `thief`, `scapegoat`, `harbor_ruler`, `harbor_vassal`: who is involved.
- `motive`: 1 greed, 2 desperation, 3 paid by a vassal, 4 paid by a foreign ruler.
- `investigator`, `approach`, `method`: how it was investigated and how the thief was caught.
- `thief_at_large`, `thief_sponsored`, `scapegoat_punished`, `avenger`: state.
- `pending_*`: a follow-up is scheduled, so the story must not end yet.
- `note_*`: what happened, used by the dispatcher
  (`note_executed note_jailed note_pardoned note_reformed note_exiled note_killed note_war note_usurper
  note_unrest note_bandit note_sanctuary note_audit note_scapegoat_freed`).
- Character variables `ie_fear`, `ie_loyalty`, `ie_mockery` are the reputation counters.

### Endings and when they fire (in this priority order)

| Ending | Event | Fires when |
|---|---|---|
| A Laughing Stock | 0102 | Mockery counter 2 or more |
| A Scar on the Realm | 0105 | A county was usurped or the people were left to rise |
| The Reckoning Abroad | 0104 | A war was fought |
| A Matter for the Church | 0108 | The thief took sanctuary |
| The Innocent's Revenge | 0106 | The wrongly punished was never cleared |
| The Reformed Treasury | 0107 | The steward's audit led to reform |
| The Reformed Thief | 0103 | A thief ended up in your service |
| A Tale Retold | 0109 | The thief was killed in secret or hunted down |
| The Iron Ledger | 0100 | Fear counter 2 or more |
| The Merciful Name | 0101 | Loyalty counter 2 or more |
| Nothing Changes | 0110 | Fallback |

### Decisions unlocked by endings
King's Watch, General Amnesty, Restore Your Good Name, Court of Assizes, Press the Old Claim, Rebuild the Marches,
Endow the Abbey, Commission a Ballad, Reconcile with the Wronged House. Each is unlocked by a character flag
(`ie_decision_*`) set by an ending choice and removed when the decision is used.

### Outcome ledger: good, bad, and the remedy (the 40% rule in practice)

| Mark | Kind | Remedy |
|---|---|---|
| Laughing Stock, Laughed At (dynasty) | Negative | Decision: Restore Your Good Name |
| Scarred County, Troubled Realm | Negative | Decision: Rebuild the Marches; garrison the roads |
| Innocent Blood, House Seeking Justice, Wrongly Accused | Negative | Decision: Reconcile with the Wronged House |
| Bandit Haven | Negative | Hunt, pardon, crack down; Rebuild the Marches |
| Peasant Unrest | Negative | Event options: army, granaries, hear grievances |
| Vassal faction | Negative | Event options: arrest, concede, rally the lords |
| Claim war from abroad | Negative | Pay, talk it down, or fight |
| Lax Treasury | Negative | Reform ending, audit option |
| Thief as rival, avenger, rival rulers | Negative | Weregild, private talk, peace offering |
| Oathbreaker | Negative | **No remedy yet (gap)** |
| Sacrilege | Negative | **No remedy yet (gap)** |
| Tyrant of the Marches | Negative | **No remedy yet (gap)** |
| Distrustful Court, Harsh Hand | Negative | **No remedy yet (gap)**; they fade with time |
| Feared Justice, Respected Justice, Lawgiver, Legend, Audited Treasury, Pious Patron, etc. | Positive | n/a |

A quantitative audit of the negative share has not been done. Do one after each big expansion.

## 5. Option design patterns that work

- **Investigator matters:** who you send changes what you find and the options after (steward finds a paper trail
  and unlocks prosecution and reform; spymaster unlocks turning the thief into an informant).
- **Personality option:** one flavoured option per event, chosen by priority, so lists stay short.
- **Skill-gated approach:** `trigger` on skill, trait or perk. Odds shift with skill tiers using `modifier` blocks.
- **Wrong-turn branch:** a plausible but wrong answer with a lasting cost, and a way to discover and repair it.
- **Escalation to the map:** a failed approach should risk something big (a war, a seized county, a faction).
- **Shared effect macros:** one scripted effect per repeated behaviour so tuning happens in one place.

## 6. The consequence toolbox (all verified against vanilla)

| Tool | How | Notes |
|---|---|---|
| Character modifier | `add_character_modifier = { modifier years }` | Defined in `common/modifiers` |
| County modifier | `add_county_modifier` | Whole duchy or kingdom through helper effects |
| Province modifier | `add_province_modifier` on `title_province` or `capital_province` | |
| Dynasty / house modifier | `dynasty ?= { add_dynasty_modifier }`, `house ?= { add_house_modifier }` | |
| Trait shift | `ie_theft_trait_effect` with a chance and an opposite check | Works on any character |
| Custom traits | `common/traits` (fame category) | Lawgiver, Notorious Thief, Wrongly Accused, Thief-Taker |
| Custom opinion modifier | `common/opinion_modifiers` | So the hover text says why |
| Memory | `create_character_memory` | Types in `common/character_memory_types` |
| Relations | `set_relation_rival`, `set_relation_friend`, hooks | Needs a reason key in localization |
| Wars | `start_war` with a custom casus belli, or `claim_cb` with a claimant | Waive cost with `temp_no_claim_war_cost` |
| Claims | `add_pressed_claim` | |
| Title changes | `create_title_and_vassal_change`, `change_title_holder`, `change_liege`, `resolve_title_and_vassal_change` | |
| Factions | `create_faction` after `can_create_faction` | |
| Decisions | `common/decisions`, unlocked with character flags | |
| Peasant unrest | A strong negative county opinion modifier for about two years | The game's peasant mechanics take over |
| Stories | `create_story`, variables, `end_story` | |

## 7. Technical rules we learned (read before writing script)

- **New files need a full game restart.** Hot reload only picks up edits to files the game already loaded.
- **Never use `add_gold` with a negative value.** Use `remove_short_term_gold = { value = X multiply = Y }`.
- **Blackmail hooks need a secret.** Use `threat_hook` or another hook type unless a secret exists.
- **Pronouns:** use `GetSheHe`, `GetHerHis`, `GetHerHim`. `GetHeShe` does not exist.
- **Encoding:** script and localization files use UTF-8 **with** BOM. `descriptor.mod` and the launcher `.mod` file use **no** BOM.
- **Verify names against the game files** before using any trait, perk, modifier field, effect or trigger.
  An invalid trait name logs thousands of errors.
- **Scopes:** saved scopes do not survive between events. Store characters in story variables and restore them
  with a loader effect at the start of every follow-up event.
- **Tooltip errors:** "while building tooltip" errors about unset scopes come from the game simulating effects without running
  `save_scope_as`. Keep immediates light and avoid loading story data before it exists.
- **Court size:** if the court is too small for the story, create the missing characters (clerk, rival courtier)
  with `create_character` so events never reference a missing scope.
- **Pending flags:** a delayed follow-up must set a `pending_*` variable so the story does not end first;
  the follow-up clears it. Always keep a safety net so a stalled story still ends (this story ends with its
  epilogue after 5 years, and hard-stops after 7).
- **Testing:** run `event ie_theft.0001` in the console. Later events need the story to exist, so run the entry first.
  After a test, read `Documents\Paradox Interactive\Crusader Kings III\logs\error.log` (the OneDrive Documents path on this PC).

## 8. Naming and file layout

- Prefix everything with `ie_`. Namespace for the theft story is `ie_theft`.
- Localization keys: `<namespace>.<id>.t` (title), `.desc`, `.a .b .c` (options), `ie_theft.out.<label>` (outcome labels),
  `<modifier>` and `<modifier>_desc`, `trait_<key>`, `<decision>_desc`, `_tooltip`, `_confirm`.
- Event IDs: 0001 to 0099 are story events grouped by phase; 0090 is the dispatcher; 0100 to 0110 are endings.
- Files: `events/ie_theft_events_N.txt` (grouped by phase), `common/scripted_effects/ie_theft_effects*.txt`,
  `common/modifiers/ie_modifiers.txt`, `common/decisions/ie_decisions.txt`, `common/traits/ie_traits.txt`,
  `common/opinion_modifiers/ie_opinion_modifiers.txt`, `common/character_memory_types/ie_memories.txt`,
  `common/casus_belli_types/ie_casus_belli.txt`, `localization/english/ie_*_l_english.yml`.
- `docs/modifier_catalog.md` lists the 100 modifier ideas and their verdicts.

## 9. Checklist for a new event or story

1. Does it change something about the character, the court or the map? If not, cut it.
2. Does the opening line summarise the event in bold?
3. Are there 3 to 6 options, each different in effect, not just in label?
4. Are options gated by skill, trait, perk or situation where it makes sense?
5. Is stress within the limits above?
6. Do random choices have readable outcome labels?
7. Is there a wrong-turn or negative branch, and a remedy for it (the 40% rule)?
8. Does something carry forward (flag, counter, modifier, memory, relation)?
9. Does it end in a way the dispatcher can recognise, with a `note_*` set?
10. Spam controls in place (cooldown, one story at a time, delegation where low stakes)?
11. Every name verified against the game files; every localization key defined; braces balanced.
12. Does the log come back clean after a test run?

## 10. Skeleton for a new story type

1. **Hook:** what ordinary vanilla event is this replacing, and what is boring about it?
2. **Cast:** the characters stored as story variables (and fallbacks if they do not exist).
3. **Approaches:** at least two ways in, each gated differently.
4. **Wrong turn:** a plausible mistake with a lasting cost.
5. **Escalations:** at least two routes that reach the map (war, title, faction, unrest, claim).
6. **Remedies:** for every negative mark, an event option or decision.
7. **Endings:** at least five, picked by a dispatcher from `note_*` and counters.
8. **Unlocks:** decisions that reward or repair, gated by flags.
9. **Safety net:** a timer so the story always ends.

## 11. Backlog and ideas for the next rounds

- Add remedies for the gaps in the ledger (Oathbreaker, Sacrilege, Tyrant of the Marches, Distrustful Court, Harsh Hand).
- Use the reserved opinion modifiers (fears your justice, laughs at your handling, hunted across the land).
- Tidy repeated trait-chance lines in tooltips (the execute option lists the same chance several times).
- Audit the positive/negative balance and adjust toward roughly 40% negative.
- Wards (the thief's children), secrets and blackmail, mercenary bands, a ballad that becomes a culture tradition.
- Next story types: use the skeleton above on a vanilla court or yearly event that is generic today.
