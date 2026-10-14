"""Update 8 cross-checks (run after build_all.py): braces balance in every generated file, every key a new system uses has localization,
every cross-reference points at something that exists. Prints problems; exit code 1 if any.
Run: python tools/check_u8.py"""
import glob
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GAME = r"C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game"
problems = []


def read(path):
    return open(path, encoding="utf-8-sig", errors="replace").read()


def strip(t):
    return re.sub(r"#[^\n]*", "", t)


# ---------------------------------------------------------------- localization keys
loc = {}
for fn in glob.glob(os.path.join(ROOT, "localization", "english", "*.yml")):
    for m in re.finditer(r'^ ([A-Za-z0-9_.\-]+):\d* "(.*)"$', read(fn), re.M):
        loc[m.group(1)] = m.group(2)


def need_loc(owner, *keys):
    for k in keys:
        if k not in loc:
            problems.append("%s: missing localization key %s" % (owner, k))


# ---------------------------------------------------------------- 1. brace balance in everything the update writes
for pattern in ("common/activities/**/*.txt", "common/scripted_triggers/eir_triggers_act*.txt", "common/scripted_effects/eir_effects_act*.txt",
                "common/script_values/*.txt", "common/religion/**/*.txt", "common/culture/**/*.txt", "common/casus_belli_types/*.txt",
                "common/court_positions/**/*.txt", "common/laws/*.txt", "common/struggle/**/*.txt", "common/dynasties/*.txt",
                "common/dynasty_houses/*.txt", "common/council_tasks/*.txt", "common/game_concepts/*.txt", "common/scripted_modifiers/*.txt",
                "common/succession_election/*.txt", "common/governments/*.txt", "common/inspirations/*.txt", "common/situation/**/*.txt",
                "common/on_action/*.txt", "common/decisions/*.txt", "events/*.txt"):
    for fn in glob.glob(os.path.join(ROOT, pattern.replace("/", os.sep)), recursive=True):
        t = strip(re.sub(r'"[^"\n]*"', '""', read(fn)))
        if t.count("{") != t.count("}"):
            problems.append("%s: braces do not balance (%d open, %d close)" % (os.path.relpath(fn, ROOT), t.count("{"), t.count("}")))

# ---------------------------------------------------------------- 2. activities
act_file = os.path.join(ROOT, "common", "activities", "activity_types", "eir_activities.txt")
if os.path.exists(act_file):
    t = strip(read(act_file))
    pulses = strip(read(os.path.join(ROOT, "common", "activities", "pulse_actions", "eir_pulse_actions.txt")))
    intents = strip(read(os.path.join(ROOT, "common", "activities", "intents", "eir_intents.txt")))
    pulse_keys = set(re.findall(r"^(eir_[a-z_]+) = \{", pulses, re.M))
    intent_keys = set(re.findall(r"^(eir_[a-z_]+_intent) = \{", intents, re.M))
    for m in re.finditer(r"^(activity_eir_[a-z_]+) = \{", t, re.M):
        a = m.group(1)
        need_loc(a, a, a + "_name", a + "_owner", a + "_desc", a + "_selection_tooltip", a + "_host_desc", a + "_guest_desc",
                 a + "_guest_help_text", a + "_conclusion_desc", a + "_predicted_cost", "TRAVEL_NAME_FOR_" + a)
    for k in re.findall(r"^\t\t(eir_[a-z_]+_phase) = \{", t, re.M):
        need_loc("phase", k, k + "_desc")
    for cat in re.findall(r"^\t\t(eir_[a-z]+_(?:scale|focus)) = \{", t, re.M):
        need_loc("option category", cat)
    for opt in re.findall(r"^\t\t\t(eir_[a-z]+_(?:scale|focus)_[a-z]+) = \{", t, re.M):
        need_loc("option", opt, opt + "_desc")
    for e in re.findall(r"entries = \{ ([^}]*) \}", t):
        for p in e.split():
            if p not in pulse_keys:
                problems.append("activity lists pulse action %s which is not defined" % p)
            need_loc("pulse action", p, p + "_title")
    for i in re.findall(r"intents = \{ ([^}]*) \}", t):
        for p in i.split():
            if p.startswith("eir_") and p not in intent_keys:
                problems.append("activity lists intent %s which is not defined" % p)
    for i in intent_keys:
        need_loc("intent", i, i + "_desc")
    for k in re.findall(r"key = (eir_[a-z_]+_conc)\b", t):
        need_loc("conclusion", k, k + "_title")
    # every option used in a pulse weight exists
    opts = set(re.findall(r"^\t\t\t(eir_[a-z]+_(?:scale|focus)_[a-z]+) = \{", t, re.M))
    for o in re.findall(r"option = (eir_[a-z_]+)", pulses + t):
        if o not in opts:
            problems.append("an activity refers to option %s which does not exist" % o)


# ---------------------------------------------------------------- 3. casus belli, court positions, innovations
cb_file = os.path.join(ROOT, "common", "casus_belli_types", "eir_casus_belli.txt")
if os.path.exists(cb_file):
    t = strip(read(cb_file))
    for cb in re.findall(r"^(eir_[a-z_]+_cb) = \{", t, re.M):
        need_loc(cb, cb, cb + "_desc")
    for k in re.findall(r'(?:war_name|war_name_base|cb_name) = "([A-Z_]+)"', t):
        need_loc("cb", k)
    for k in re.findall(r"desc = (eir_[a-z_]+)", t) + re.findall(r"on_invalidated_desc = (eir_[a-z_]+)", t):
        need_loc("cb text", k)
cp_file = os.path.join(ROOT, "common", "court_positions", "types", "eir_court_positions.txt")
if os.path.exists(cp_file):
    t = strip(read(cp_file))
    for k in re.findall(r"^(eir_[a-z_]+_court_position) = \{", t, re.M):
        need_loc(k, k, k + "_desc")
    for k in re.findall(r"desc = (eir_court_trait_[a-z]+)", t):
        need_loc("court trait text", k)
inn_file = os.path.join(ROOT, "common", "culture", "innovations", "eir_innovations.txt")
if os.path.exists(inn_file):
    t = strip(read(inn_file))
    for k in re.findall(r"^(innovation_eir_[a-z_]+) = \{", t, re.M):
        need_loc(k, k, k + "_desc")
    for k in re.findall(r"custom = (eir_[a-z_]+)", t):
        need_loc("innovation text", k)

# ---------------------------------------------------------------- 4. every art path, animation, environment and sound the new files name must exist
vanilla_text = None


def vanilla_blob():
    global vanilla_text
    if vanilla_text is None:
        parts = []
        for sub in ("common", "events", "gui"):
            for fn in glob.glob(os.path.join(GAME, sub, "**", "*.txt"), recursive=True):
                try:
                    parts.append(open(fn, encoding="utf-8-sig", errors="replace").read())
                except Exception:
                    pass
        vanilla_text = "\n".join(parts)
    return vanilla_text


new_files = []
for pattern in ("common/activities/**/*.txt", "common/struggle/**/*.txt", "common/decisions/eir_struggle_decisions.txt",
                "common/court_positions/**/*.txt", "common/casus_belli_types/*.txt", "common/culture/innovations/*.txt"):
    new_files += glob.glob(os.path.join(ROOT, pattern.replace("/", os.sep)), recursive=True)
for fn in new_files:
    t = read(fn)
    for m in re.finditer(r'"(gfx/[^"]+\.dds)"', t):
        rel = m.group(1)
        if not (os.path.exists(os.path.join(GAME, *rel.split("/"))) or os.path.exists(os.path.join(ROOT, *rel.split("/")))):
            problems.append("%s: art file does not exist: %s" % (os.path.basename(fn), rel))
blob = vanilla_blob()
for fn in new_files:
    t = read(fn)
    for kw in ("animation", "environment", "ambience", "camera"):
        for v in set(re.findall(r'\b%s = "?([A-Za-z_0-9:/.\-]+)"?' % kw, t)):
            if v not in blob:
                problems.append("%s: %s '%s' is not used by the base game's own script" % (os.path.basename(fn), kw, v))


def have_icon(folder, name):
    return os.path.exists(os.path.join(GAME, "gfx", "interface", "icons", folder, name + ".dds")) or os.path.exists(os.path.join(ROOT, "gfx", "interface", "icons", folder, name + ".dds"))


pa = os.path.join(ROOT, "common", "activities", "pulse_actions", "eir_pulse_actions.txt")
if os.path.exists(pa):
    for ic in set(re.findall(r"^\s*icon = ([a-z_]+)\s*$", read(pa), re.M)):
        if not have_icon("activity_pulse_actions", ic):
            problems.append("pulse action icon missing: %s" % ic)
ie = os.path.join(ROOT, "common", "activities", "intents", "eir_intents.txt")
if os.path.exists(ie):
    for ic in set(re.findall(r"^\s*icon = ([a-z_]+)\s*$", read(ie), re.M)):
        if not have_icon("activity_intents", ic):
            problems.append("intent icon missing: %s" % ic)
inn = os.path.join(ROOT, "common", "culture", "innovations", "eir_innovations.txt")
if os.path.exists(inn):
    for rel in re.findall(r'= "(gfx/interface/icons/culture_innovations/[a-z_0-9]+\.dds)"', read(inn)):
        if not os.path.exists(os.path.join(GAME, *rel.split("/"))):
            problems.append("innovation icon missing: %s" % rel)
hs = os.path.join(ROOT, "common", "religion", "holy_site_types", "eir_holy_sites.txt")
if os.path.exists(hs):
    lt = strip(read(os.path.join(GAME, "common", "landed_titles", "00_landed_titles.txt")))
    for key, county, barony in re.findall(r"^(eir_[a-z_]+) = \{\n\tcounty = ([a-z_]+)\n\tbarony = ([a-z_]+)", read(hs), re.M):
        mm = re.search(r"\b%s\s*=\s*\{" % county, lt)
        if not mm:
            problems.append("holy site %s: county %s does not exist" % (key, county))
            continue
        depth, j = 1, mm.end()
        while depth and j < len(lt):
            if lt[j] == "{":
                depth += 1
            elif lt[j] == "}":
                depth -= 1
            j += 1
        if barony not in lt[mm.end():j]:
            problems.append("holy site %s: barony %s is not in %s" % (key, barony, county))

# tenet icons and decision pictures
tf = os.path.join(ROOT, "common", "religion", "tenet_types", "eir_tenets.txt")
if os.path.exists(tf):
    for ic in set(re.findall(r"^\s*icon = ([a-z_]+)\s*$", read(tf), re.M)):
        if not (os.path.exists(os.path.join(GAME, "gfx", "interface", "icons", "faith_tenets", ic + ".dds")) or os.path.exists(os.path.join(ROOT, "gfx", "interface", "icons", "faith_tenets", ic + ".dds"))):
            problems.append("tenet icon missing: %s" % ic)
for fn in glob.glob(os.path.join(ROOT, "common", "decisions", "*.txt")):
    for rel in set(re.findall(r'"(gfx/[^"]+\.dds)"', read(fn))):
        if not (os.path.exists(os.path.join(GAME, *rel.split("/"))) or os.path.exists(os.path.join(ROOT, *rel.split("/")))):
            problems.append("%s: picture does not exist: %s" % (os.path.basename(fn), rel))
# faith, rites, holy sites: localization
if os.path.exists(os.path.join(ROOT, "common", "religion", "faith_types", "eir_faith_types.txt")):
    need_loc("faith", "eir_druidic", "eir_druidic_adj", "eir_druidic_adherent", "eir_druidic_adherent_plural", "eir_druidic_desc", "eir_druidic_old")
    for k in re.findall(r"^(eir_[a-z_]+) = \{", read(os.path.join(ROOT, "common", "religion", "rite_types", "eir_rite_types.txt")), re.M):
        need_loc("rite", k, k + "_adj", k + "_adherent", k + "_adherent_plural", k + "_desc")
    for k in re.findall(r"^(eir_[a-z_]+) = \{", read(os.path.join(ROOT, "common", "religion", "holy_site_types", "eir_holy_sites.txt")), re.M):
        need_loc("holy site", "holy_site_%s_name" % k, "holy_site_%s_effects" % k)
    for v in re.findall(r"= (eir_druidic_[a-z_0-9]+)\s*$", read(os.path.join(ROOT, "common", "religion", "faith_types", "eir_faith_types.txt")), re.M):
        need_loc("faith text", v)
# struggle: phases, decisions
sf = os.path.join(ROOT, "common", "struggle", "struggles", "eir_struggle.txt")
if os.path.exists(sf):
    t = strip(read(sf))
    need_loc("struggle", "eir_irish_struggle", "eir_irish_struggle_desc")
    for k in re.findall(r"^\t\t(eir_struggle_phase_[a-z_]+) = \{", t, re.M):
        need_loc("struggle phase", k, k + "_desc")
    for k in re.findall(r"^\t\t\t\t(eir_struggle_end_[a-z_]+_decision)$", t, re.M):
        need_loc("struggle ending", k.replace("_decision", ""), k + "_desc")

if problems:
    for p in problems:
        print("PROBLEM", p)
print("check_u8: %d problem(s)" % len(problems))
sys.exit(1 if problems else 0)
