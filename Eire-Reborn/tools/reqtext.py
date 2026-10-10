"""Readable requirement tooltips (Update 2).

Count-style triggers (any_vassal count, any_sub_realm_county count), has_global_variable, coastal checks and stress
checks have no vanilla tooltip text, so the game prints "BUG: missing localization". `wrap()` takes a decision's
is_valid text and wraps every such statement in custom_description with plain English.
"""
import re
import hashlib

NATIVE = [   # statements the game already words itself
    r"^is_at_war = (yes|no)$",
    r"^(prestige|piety|gold) >= \d+$",
    r"^prestige_level >= \d+$",
    r"^(learning|martial|diplomacy|stewardship|intrigue|prowess) >= \d+$",
    r"^is_independent_ruler = yes$",
    r"^has_title = title:[a-z_]+$",
    r"^(NOT = \{ )?has_character_modifier = [a-z_]+( \})?$",
    r"^exists = primary_heir$",
    r"^government_has_flag = [a-z_]+$",
    r"^has_trait = [a-z_]+$",
    r"^custom_description = ",
    r"^eir_irish_buildings_trigger = ",
]

STAGE = {
    "eir_stage1_trigger": "You are a real chieftain: your realm holds at least 4 counties",
    "eir_stage2_trigger": "You are a duke-level ruler: you hold a duchy, your realm has at least 10 counties and you have prestige level 2 or higher",
    "eir_stage3_trigger": "You are a king: you hold a kingdom, your realm has at least 20 counties and you have prestige level 3 or higher",
    "eir_stage4_trigger": "You are the High King of Ireland with prestige level 4 or higher",
    "eir_visible_stage1_trigger": "Your realm holds at least 2 counties",
}
TRAD = {"tradition_poetry": "Poetry", "tradition_pastoralists": "Pastoralists", "tradition_monastic_communities": "Monastic Communities",
        "tradition_maritime_mercantilism": "Maritime Mercantilism"}
SKILL = {"learning": "Learning", "martial": "Martial", "prowess": "Prowess", "stewardship": "Stewardship", "diplomacy": "Diplomacy", "intrigue": "Intrigue"}
VAR_FALLBACK = {}
VAR_EVENT = {   # globals set by events, not decisions: (met, not met)
    "eir_black_host_broken": ("You have broken the Black Host", "You have not yet broken the Black Host"),
    "eir_bh_started": ("The Black Host has come to Ireland", "The Black Host has not yet come"),
    "eir_bh_ended": ("The war with the Black Host is over", "The war with the Black Host is not over"),
    "eir_done_union": ("The Insular Union has been proclaimed", "The Insular Union has not been proclaimed"),
    "eir_done_triumph": ("You have held a Triumph", "You have not yet held a Triumph"),
}


class Ctx:
    def __init__(self, dec_names, var_sources, trad_names):
        self.dec_names = dec_names          # decision key -> display name
        self.var_sources = var_sources      # global variable -> list of decision keys that set it
        self.trad = dict(TRAD)
        self.trad.update(trad_names)
        self.unknown = []


def split_statements(text):
    out, cur, depth = [], [], 0
    for line in text.strip("\n").split("\n"):
        cur.append(line.strip())
        depth += line.count("{") - line.count("}")
        if depth == 0:
            out.append(" ".join(c for c in cur if c))
            cur = []
    return out


def var_text(ctx, var, negate=False):
    srcs = ctx.var_sources.get(var, [])
    names = [ctx.dec_names.get(s, s) for s in srcs if s in ctx.dec_names]
    if var in VAR_EVENT:
        return VAR_EVENT[var][1 if negate else 0]
    if var == "eir_collapse_abolished":
        base = "The tanistic fragmentation has been ended"
    elif names:
        what = names[0]
        base = "You have completed the decision %s" % what
    else:
        base = "The condition '%s' is met" % var.replace("eir_", "").replace("_", " ")
    if negate:
        return base.replace("You have completed", "You have NOT yet completed").replace("has been", "has not been").replace("is met", "is not met")
    return base


def describe(ctx, st):
    """plain English for one statement, or None when unknown"""
    st = st.strip()
    simple = {
        "eir_can_create_island_kingdom_trigger = yes": "You hold a kingdom, the Insular Union is proclaimed, you hold six Celtic counties in Britain and the Isle of Man",
        "eir_holds_british_port_trigger = yes": "Your realm holds a coastal county in Great Britain",
        "eir_has_gael_neighbour_trigger = yes": "A Gaelic ruler who is not your vassal lives within reach",
        "eir_norse_presence_trigger = yes": "Norse rulers hold land in Ireland or in your realm",
        "eir_holds_norse_county_trigger = yes": "Your realm holds at least one Norse-culture county",
        "eir_norse_holds_irish_county_trigger = yes": "A Norse-culture ruler holds a county of Ireland",
        "eir_bh_active_trigger = yes": "The Black Host is at large in Ireland",
        "eir_bh_beaten_trigger = yes": "You have broken the Black Host",
        "eir_viking_age_trigger = yes": "The Viking age is on (868 to 1100)",
        "has_variable = eir_bh_defeated": "The Norse have beaten you in the field, or you have paid them off",
        "has_character_flag = eir_vowed_vengeance": "You have sworn a vow of vengeance",
        "has_variable = eir_norse_enclave": "You have agreed to a Norse enclave on your coast",
    }
    if st in simple:
        return simple[st]
    m = re.match(r"^eir_celtic_britain_counties_trigger = \{ N = (\d+) \}$", st)
    if m:
        return "Your realm holds at least %s Celtic (Gaelic or Brythonic) counties in Britain" % m.group(1)
    m = re.match(r"^eir_foreign_conquests_trigger = \{ N = (\d+) \}$", st)
    if m:
        return "At least %s counties in your realm are held under a foreign culture (conquered Britain or Norse land)" % m.group(1)
    m = re.match(r"^current_year >= (\d+)$", st)
    if m:
        return "The year is %s or later" % m.group(1)
    m = re.match(r"^(eir_[a-z0-9_]+_trigger) = yes$", st)
    if m and m.group(1) in STAGE:
        return STAGE[m.group(1)]
    m = re.match(r"^eir_ports_trigger = \{ N = (\d+) \}$", st)
    if m:
        return "At least %s of your counties are on the coast" % m.group(1)
    m = re.match(r"^eir_realm_size_trigger = \{ N = (\d+) \}$", st)
    if m:
        return "Your realm holds at least %s counties" % m.group(1)
    m = re.match(r"^eir_holds_irish_duchies_trigger = \{ COUNT = (\d+) \}$", st)
    if m:
        return "You hold at least %s of the five Irish duchies (Meath, Ulster, Connacht, Leinster, Munster)" % m.group(1)
    m = re.match(r"^eir_holds_irish_counties_trigger = \{ COUNT = (\d+) \}$", st)
    if m:
        return "Your realm holds at least %s counties of Ireland" % m.group(1)
    if st == "eir_irish_port_trigger = yes":
        return "Your realm holds one of the great Irish harbours (Dublin, Waterford, Cork, Limerick or Mayo)"
    if st == "eir_has_coast_trigger = yes":
        return "You hold at least one coastal county"
    if st == "eir_has_foreign_britain_counties_trigger = yes":
        return "Your realm holds at least one county in Britain whose people are neither Gaelic nor Brythonic"
    if st == "eir_has_celtic_britain_counties_trigger = yes":
        return "Your realm holds at least one Celtic (Gaelic or Brythonic) county in Britain"
    if st == "eir_can_create_dal_riata_trigger = yes":
        return "You meet the conditions to create the Kingdom of Dál Riata (hold Argyll and the Isles or the northern Irish coast, as a Gael)"
    if st == "eir_can_create_gaeldom_trigger = yes":
        return "You meet the conditions to create the Empire of Gaeldom (a Gaelic king of Ireland who rules in Britain too)"
    m = re.match(r"^eir_can_create_provincial_kingdom_trigger = \{ DUCHY = (d_[a-z_]+) \}$", st)
    if m:
        nm = m.group(1)[2:].replace("_", " ").title()
        return "You hold the Duchy of %s and meet the conditions to create the Kingdom of %s" % (nm, nm)
    m = re.match(r"^(NOT = \{ )?has_global_variable = ([a-z_0-9]+)( \})?$", st)
    if m:
        return var_text(ctx, m.group(2), negate=bool(m.group(1)))
    m = re.match(r"^NOT = \{ exists = title:([ke]_[a-z_]+)\.holder \}$", st)
    if m:
        return "The title %s has not yet been created" % m.group(1)[2:].replace("_", " ").title()
    m = re.match(r"^any_vassal = \{ count >= (\d+) \}$", st)
    if m:
        return "You have at least %s vassals" % m.group(1)
    m = re.match(r"^any_vassal = \{ highest_held_title_tier >= tier_duchy count >= (\d+) \}$", st)
    if m:
        return "At least %s of your vassals hold a duchy or a higher title" % m.group(1)
    m = re.match(r"^culture = \{ has_cultural_tradition = ([a-z_]+) \}$", st)
    if m:
        return "Your culture has the %s tradition" % ctx.trad.get(m.group(1), m.group(1))
    m = re.match(r"^any_held_title = \{ tier = tier_county \}$", st)
    if m:
        return "You hold at least one county directly"
    m = re.match(r"^any_sub_realm_county = \{ this = title:c_dublin \}$", st)
    if m:
        return "Your realm holds the County of Dublin"
    m = re.match(r"^any_sub_realm_county = \{ count >= (\d+) any_county_province = \{ has_building = (eir_[a-z_0-9]+) \} \}$", st)
    if m:
        return "At least %s of your counties have built an Irish Sea Quay" % m.group(1)
    m = re.match(r"^any_sub_realm_county = \{ count >= (\d+) any_county_province = \{ has_building_or_higher = (eir_[a-z_0-9]+) \} \}$", st)
    if m:
        return "At least %s of your counties have built an Irish Sea Quay" % m.group(1)
    m = re.match(r"^any_held_title = \{ tier = tier_county is_coastal_county = yes NOT = \{ has_county_modifier = ([a-z_]+) \} \}$", st)
    if m:
        return "You hold a coastal county that has not yet been chartered as a town"
    m = re.match(r"^var:([a-z_]+) >= (\d+)$", st)
    if m:
        return {"eir_recelt": "You have reclaimed at least %s counties of Britain for your culture",
                "eir_resent": "Cultural resentment in your foreign counties is %s or higher"}.get(m.group(1), "The counter %s is at least %%s" % m.group(1)) % m.group(2)
    m = re.match(r"^var:([a-z_]+) <= (\d+)$", st)
    if m:
        return {"eir_resent": "Cultural resentment in your foreign counties is %s or lower"}.get(m.group(1), "The counter %s is at most %%s" % m.group(1)) % m.group(2)
    m = re.match(r"^has_variable = ([a-z_]+)$", st)
    if m:
        return {"eir_recelt": "You have begun to reclaim Britain (the decision Reclaim the Tongue)",
                "eir_resent": "Your reclaimed counties are restless with cultural resentment"}.get(m.group(1), "The condition %s is met" % m.group(1))
    m = re.match(r"^stress >= (\d+)$", st)
    if m:
        return "Your stress is at least %s" % m.group(1)
    m = re.match(r"^current_month >= (\d+)$", st)
    if m:
        return "It is month %s of the year or later" % m.group(1)
    m = re.match(r"^current_month <= (\d+)$", st)
    if m:
        return "It is month %s of the year or earlier" % m.group(1)
    if st == "NOT = { has_variable = eir_colony_county }":
        return "You are not already settling a colony"
    m = re.match(r"^NOT = \{ has_character_flag = ([a-z_]+) \}$", st)
    if m:
        return "You have not recently done this already"
    m = re.match(r"^has_character_flag = ([a-z_]+)$", st)
    if m:
        return "You have taken the oath to reclaim what was lost"
    m = re.match(r"^OR = \{ (.*) \}$", st)
    if m:
        bits = []
        for p in split_inner(m.group(1)):
            d = describe_simple(ctx, p)
            if d is None:
                return None
            bits.append(d)
        return "; or ".join(bits) if False else " OR ".join(bits)
    return None


def split_inner(text):
    """split 'a >= 1 b = { c = d } e = f' into statements (brace aware)"""
    toks = text.split()
    out, i = [], 0
    while i < len(toks):
        if i + 2 >= len(toks) + 0 and i + 2 > len(toks) - 1 + 0 and len(toks) - i < 3:
            out.append(" ".join(toks[i:]))
            break
        stmt = toks[i:i + 3]
        i += 3
        if stmt[2] == "{":
            depth = 1
            while i < len(toks) and depth:
                depth += toks[i].count("{") - toks[i].count("}")
                stmt.append(toks[i])
                i += 1
        out.append(" ".join(stmt))
    return out


def describe_simple(ctx, st):
    simple = {
        "eir_has_foreign_britain_counties_trigger = yes": "your realm holds a foreign-culture county in Britain",
        "eir_has_celtic_britain_counties_trigger = yes": "your realm holds a Celtic county in Britain",
        "has_character_flag = eir_paid_danegeld": "you paid Danegeld",
        "has_character_modifier = eir_danegeld_modifier": "you are bound by a Danegeld agreement",
    }
    if st in simple:
        return simple[st]
    m = re.match(r"^(learning|martial|prowess|stewardship|diplomacy|intrigue) >= (\d+)$", st)
    if m:
        return "%s %s or higher" % (SKILL[m.group(1)], m.group(2))
    m = re.match(r"^gold >= (\d+)$", st)
    if m:
        return "at least %s gold" % m.group(1)
    m = re.match(r"^prestige >= (\d+)$", st)
    if m:
        return "at least %s prestige" % m.group(1)
    m = re.match(r"^any_courtier = \{ has_trait = ([a-z_]+) \}$", st)
    if m:
        return {"eir_ollamh": "an Ollamh (master poet) at your court"}.get(m.group(1), "a courtier with the %s trait" % m.group(1))
    m = re.match(r"^any_courtier = \{ (learning|martial) >= (\d+) \}$", st)
    if m:
        return "a courtier with %s %s or higher" % (SKILL[m.group(1)], m.group(2))
    m = re.match(r"^has_trait = ([a-z_]+)$", st)
    if m:
        return "you have the %s trait" % m.group(1)
    m = re.match(r"^has_title = title:([a-z_]+)$", st)
    if m:
        return "you hold the title %s" % m.group(1)[2:].replace("_", " ").title()
    m = re.match(r"^NOT = \{ exists = title:([ke]_[a-z_]+)\.holder \}$", st)
    if m:
        return "nobody holds the title %s" % m.group(1)[2:].replace("_", " ").title()
    m = re.match(r"^has_character_flag = ([a-z_]+)$", st)
    if m:
        return "you have sworn the oath to reclaim what was lost" if m.group(1) == "eir_oath_to_reclaim" else "you have the flag %s" % m.group(1)
    m = re.match(r"^has_variable = ([a-z_]+)$", st)
    if m:
        return describe(None, st) if False else {"eir_norse_enclave": "you have agreed to a Norse enclave on your coast", "eir_bh_defeated": "the Norse have beaten you in the field"}.get(m.group(1), "the condition %s is met" % m.group(1))
    m = re.match(r"^has_global_variable = ([a-z_]+)$", st)
    if m:
        return {"eir_black_host_broken": "you have broken the Black Host", "eir_bh_ended": "the war with the Black Host is over"}.get(m.group(1), "the condition %s is met" % m.group(1))
    m = re.match(r"^culture = \{ has_cultural_tradition = ([a-z_]+) \}$", st)
    if m:
        return "your culture has the %s tradition" % ctx.trad.get(m.group(1), m.group(1))
    return None


def is_native(st):
    return any(re.match(p, st) for p in NATIVE)


def wrap(ctx, valid, owner, out_loc):
    """returns the new is_valid text; out_loc collects {key: text}"""
    if not valid.strip():
        return valid
    new = []
    for st in split_statements(valid):
        if is_native(st):
            new.append(st)
            continue
        text = describe(ctx, st)
        if text is None:
            ctx.unknown.append((owner, st))
            new.append(st)
            continue
        key = "eir_rq_" + hashlib.md5(st.encode()).hexdigest()[:10]
        out_loc[key] = text
        # re-expand the statement into properly braced multi-line text
        new.append("custom_description = {\n\ttext = %s\n\t%s\n}" % (key, st))
    return "\n".join(new)
