"""Counts the 'things per option' for the Update 2 events against the flavor guide targets (R20)."""
import re
import statistics
import gen_events as ge

groups = ge.load_groups()
THINGS = re.compile(r"\b(add_prestige|add_piety|add_gold|remove_short_term_gold|add_character_modifier|add_county_modifier|add_opinion|eir_vassal_opinion_effect|eir_court_opinion_effect|add_hook|add_dread|add_stress|add_trait_xp|eir_trait_effect|give_nickname|eir_legend_title_effect|eir_legend_defence_effect|eir_make_artifact_effect|spawn_army|eir_defender_levy_effect|set_variable|change_variable|add_character_flag|trigger_event|eir_world_reacts_effect|death|increase_wounds_effect|change_county_control|eir_raid_county_effect|eir_grant_claims_norse_effect|eir_resent_clear_effect|set_global_variable|eir_inv_launch_effect|add_legitimacy)\b")
rows = []
neg = 0
tot_opts = 0
for k in ("ev_v8a", "ev_v8b", "ev_v8c", "ev_v8d"):
    for e in groups[k]:
        if e.hidden:
            continue
        counts = []
        for o in e.options:
            kinds = set(THINGS.findall(o.effect))
            counts.append(len(kinds))
            tot_opts += 1
            if re.search(r"prestige_loss|piety_loss|stress_gain|wounds|medium_prestige_loss|-[0-9]", o.effect):
                neg += 1
        rows.append((e.num, len(e.options), statistics.mean(counts), min(counts)))
print("events: %d  options: %d" % (len(rows), tot_opts))
print("options per event: mean %.1f min %d max %d" % (statistics.mean(r[1] for r in rows), min(r[1] for r in rows), max(r[1] for r in rows)))
print("kinds of change per option: mean %.2f  options with 1 kind: %d  with 0: %d" % (
    statistics.mean(r[2] for r in rows), sum(1 for r in rows if r[3] == 1), sum(1 for r in rows if r[3] == 0)))
print("options that cost something (loss, stress, wound, negative opinion): %.0f%%" % (100.0 * neg / tot_opts))
for r in rows:
    if r[3] == 0:
        print("  event %04d has an option that changes nothing" % r[0])
