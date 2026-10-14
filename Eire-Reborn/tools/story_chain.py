"""The main story of the mod, in order. Every decision listed here is shown in purple (name, tooltip and description) so the player can
tell the road from the flavor. To move a decision on or off the road, edit this list and run tools/build_all.py.

Acts: I Ireland, II the Celtic world, III Britain, IV the mainland. All the decisions that are required by the final decisions are in the list
(checked by audit_decisions.py); the optional ones (the five Arthurian paths, the tenet decisions and the flavor decisions) are not."""

ACTS = [
    ("Act I: Ireland", [
        "hold_oenach", "rebuild_tara_hall", "crowned_at_tara", "circuit_of_ireland", "provincial_oath", "four_provinces", "end_fragmentation",
    ]),
    ("Act II: The Celtic World", [
        "found_monastery", "compile_brehon_laws", "gaelic_revival", "celtic_brotherhood", "proclaim_insular_union", "found_island_kingdom", "proclaim_gaeldom",
    ]),
    ("Act III: Britain", [
        "third_of_britannia", "unite_gaelic_kingdoms", "revive_arthur", "final_revenge",
    ]),
    ("Act IV: The Mainland", [
        "mystic_celts", "celts_mainland",
        "return_france", "celt_france", "return_germany", "celt_germany", "return_spain", "celt_spain",
        "return_italy", "celt_italy", "return_galatia", "celt_galatia",
    ]),
]

STEP = {}     # decision key -> (act label, step number in the whole story, total steps)
_n = sum(len(k) for _a, k in ACTS)
_i = 0
for _label, _keys in ACTS:
    for _k in _keys:
        _i += 1
        STEP["eir_%s_decision" % _k] = (_label, _i, _n)
