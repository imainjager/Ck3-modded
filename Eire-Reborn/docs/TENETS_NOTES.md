---
name: ck3-tenets-by-god-alone
description: "How CK3 (By God Alone DLC, game 1.20) tenets and PERSONAL tenets are structured, which script hooks exist, and how a mod can grant a unique personal tenet from a decision"
metadata:
  node_type: memory
  type: reference
  originSessionId: ffc47091-8f2f-4f7f-8b79-b5fa4137c151
  modified: 2026-10-14T15:28:35.346Z
---

"By God Alone" (DLC030_CE3, prefix `pam`, flag `by_god_alone`) is the DLC that added personal tenets. Files in `game/common/religion/tenet_types/` (`00_tenet_types.txt` vanilla ~60 tenets, `00_pam_tenets.txt` 24 DLC tenets, schema in `_tenet_types.info`). Loc: `localization/english/dlc/pam/pam_tenets_l_english.yml`.

**Tenet block fields**: `icon` (dds named like the key), optional `name`/`desc`/`historical_glossary` (first_valid + triggered_desc, default `<key>_name/_desc`), `requires_dlc_flag`, `is_shown`, `can_pick` (faith scope, for faith creation), `can_pick_as_personal_tenet` (root = character), `piety_cost`, `divergence_multiplier`, `parameters` (faith-level bool flags, tested with `has_doctrine_parameter` / `rite_has_parameter`), `character_modifier` / `clergy_modifier` / `county_modifier` (everyone of that faith), `personal_tenet_modifier` (only characters who chose it personally), `personal_tenet_parameters` (flags tested with `has_personal_tenet_flag`), `traits = { virtues = { x = { weight scale } } sins = {...} }`.

**Every parameter/flag needs loc**: `doctrine_parameter_<flag>: "..."` (shown in the tooltip). The mechanic itself is NOT in the tenet file: it is a trigger like `has_personal_tenet_flag = X` placed in a decision/interaction/event/building/activity elsewhere (e.g. `tenet_khachkar_decision_unlock` is checked in pam_decisions.txt; `tenet_khachkar_building_bonuses` in a scripted effect).

**Script**: effects `set_personal_tenet`, `force_set_personal_tenet` (bypasses slots/forbidden; the holy-order code uses it), `remove_personal_tenet`; triggers `has_personal_tenet`, `has_personal_tenet_flag`, `any_personal_tenet`/`random_personal_tenet`/`ordered_personal_tenet`, `free_personal_tenet_slots`; modifier `personal_tenet_slot_add`; `has_tenet` / `has_doctrine_parameter` (faith scope). Slots come from perks/dynasty perks/modifiers.

**To give a unique tenet from a mod decision**: define `tenet_eir_x` in `common/religion/tenet_types/eir_tenets.txt` with `can_pick_as_personal_tenet` (culture/flag test), `personal_tenet_modifier`, `personal_tenet_parameters`, optional virtues/sins; add loc (`tenet_eir_x_name/_desc`, `doctrine_parameter_*`) and an icon; the decision calls `force_set_personal_tenet = tenet:tenet_eir_x` (or `set_personal_tenet` after granting a slot). Untested in this mod as of v0.12.
