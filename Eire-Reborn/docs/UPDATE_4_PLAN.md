# Eire Reborn: UPDATE 4, the building rebuild (planned, NOT executed)

Named by the user. It **supersedes section 1 (buildings) of UPDATE_2_PLAN.md**; Update 2 keeps the tooltip text and early-game items.

## Inputs (already written)
* `../../docs/VANILLA_BUILDING_CATALOG.md`: every vanilla building family (956 entries), with costs and effects.
* `../../docs/BUILDING_BALANCE_MODEL.md`: scaling rules read from vanilla, and a table for each Irish building with the vanilla analogue and the Irish target (analogue x 1.3 on headline stats; the 30% is a starting suggestion from the user, to be tuned).
* `../../docs/FLAVOR_GUIDE.md` Part IV: rules R21-R27 and checklist items 26-30.

## What gets rebuilt
1. **Regular buildings** (14 now, 8 older): rebuild as proper chains with 2-4 levels each, a tribal version and a castle/city/church version, at vanilla's cost curve and +30% headline stats, four to six distinct effects each, one Irish flavor effect each. Irish institutions: Dún, Ringfort, Crannóg, Round Tower, High Cross, Aonach fair ground, Booley pastures, Fosterage Hall, Bruidhean, Smithy of Goibniu, Hobby stables, Holy well, Hermitage, Scriptorium, Monastic school, Pilgrim hospice, Ogham pillar field, Irish Sea quay, Longship yard, Cattle enclosure, Brehon court, Bardic school.
2. **Duchy-capital buildings** (10): three-level chains at 485 / 725 / 1100 gold (part of the gold swapped for prestige for tribal holders), +10/20/30% duchy development growth or +15/20/30% tax, +5/10/15 county opinion, +4/8/12 grandeur, then x1.3 and one Irish effect.
3. **Special buildings** (19): around 1000 gold for county development growth +26%, income +2.6, tax +26%, piety +0.33 to +1.3 and about 8 effects, including one Irish effect.
4. **Localization:** `building_type_<key>`, `building_type_<key>_desc` and `building_<key>` for every level, with a real description.
5. **Tribal access:** vanilla tribal pattern (`building_requirement_tribal = yes`, `has_building_or_higher = tribe_01`, tribal costs 75/100/125 gold and 200/350 prestige); verify in the build menu of a tribal barony.
6. **Audit step:** a script that compares each building's cost per unit of benefit with the vanilla line for its tier and fails the build when it is more than 25% off.

## Do not start until the user says so.
