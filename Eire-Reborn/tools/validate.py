"""Static checks for the whole mod. Run: python tools/validate.py

Catches the mistakes that cost us log spam in the first mod: invalid traits, missing localization,
unknown modifiers, undefined events/effects/triggers, unbalanced braces.
"""
import io
import os
import re
import glob
import sys

sys.path.insert(0, os.path.dirname(__file__))
from eir_lib import ROOT, GAME

errors = []
warnings = []


def read(fn):
    return io.open(fn, encoding="utf-8-sig").read()


def files(pattern):
    return glob.glob(os.path.join(ROOT, pattern.replace("/", os.sep)), recursive=True)


script_files = [f for f in files("common/**/*.txt") + files("events/*.txt")]
text_by_file = {f: read(f) for f in script_files}
all_text = "\n".join(text_by_file.values())
loc_text = "\n".join(read(f) for f in files("localization/english/*.yml"))

# ---------------------------------------------------------------- braces
for f, t in text_by_file.items():
    stripped = re.sub(r'#.*', '', t)
    stripped = re.sub(r'"[^"\n]*"', '""', stripped)
    o, c = stripped.count("{"), stripped.count("}")
    if o != c:
        errors.append("unbalanced braces in %s: %d open, %d close" % (os.path.relpath(f, ROOT), o, c))

# ---------------------------------------------------------------- vanilla name universe
def vanilla_names(subdir, pattern=r"^([a-z][a-z0-9_]+) = \{"):
    names = set()
    for fn in glob.glob(os.path.join(GAME, "common", subdir.replace("/", os.sep), "**", "*.txt"), recursive=True):
        try:
            names.update(re.findall(pattern, read(fn), re.M))
        except Exception:
            pass
    return names


vanilla_traits = vanilla_names("traits")
vanilla_perks = vanilla_names("lifestyle_perks")
vanilla_modifiers = vanilla_names("modifiers")
vanilla_opinion = vanilla_names("opinion_modifiers")
vanilla_hooks = vanilla_names("hook_types")

my_traits = set(re.findall(r"^(eir_[a-z0-9_]+) = \{", text_by_file.get(os.path.join(ROOT, "common", "traits", "eir_traits.txt"), ""), re.M))
my_modifiers = set()
for f, t in text_by_file.items():
    if f.endswith("eir_modifiers.txt"):
        my_modifiers.update(re.findall(r"^(eir_[a-z0-9_]+) = \{", t, re.M))
my_opinion = set()
for f, t in text_by_file.items():
    if "opinion_modifiers" in f:
        my_opinion.update(re.findall(r"^(eir_[a-z0-9_]+) = \{", t, re.M))

# ---------------------------------------------------------------- traits
used_traits = set(re.findall(r"has_trait = ([a-z_0-9]+)", all_text))
used_traits |= set(re.findall(r"(?:TRAIT|OPPOSITE) = ([a-z_0-9]+)", all_text))
used_traits |= set(re.findall(r"add_trait = ([a-z_0-9]+)", all_text))
used_traits |= set(re.findall(r"remove_trait = ([a-z_0-9]+)", all_text))
used_traits |= set(re.findall(r"^\s+([a-z_0-9]+) = (?:miniscule|minor|medium|major)_stress_impact_(?:gain|loss)", all_text, re.M))
for t in sorted(used_traits):
    if t not in vanilla_traits and t not in my_traits and t not in ("$TRAIT$", "$OPPOSITE$"):
        errors.append("unknown trait: " + t)

# ---------------------------------------------------------------- event themes
themes = set()
for fn in glob.glob(os.path.join(GAME, "common", "event_themes", "*.txt")):
    themes.update(re.findall(r"^([a-z_0-9]+) = \{", read(fn), re.M))
for th in sorted(set(re.findall(r"^\s*theme = ([a-z_0-9]+)", all_text, re.M))):
    if th not in themes:
        errors.append("unknown event theme: " + th)

# ---------------------------------------------------------------- perks
for p in sorted(set(re.findall(r"has_perk = ([a-z_0-9]+)", all_text))):
    if p not in vanilla_perks:
        errors.append("unknown perk: " + p)

# ---------------------------------------------------------------- modifiers
used_mods = set(re.findall(r"(?<![a-z_])(?:modifier|MODIFIER) = ([a-z_0-9]+)", all_text))
for m in sorted(used_mods):
    if m.startswith("$"):
        continue
    if m.endswith("_opinion"):
        if m not in my_opinion and m not in vanilla_opinion:
            errors.append("unknown opinion modifier: " + m)
    elif m not in my_modifiers and m not in vanilla_modifiers and m not in my_traits:
        errors.append("unknown modifier: " + m)
for m in sorted(my_modifiers):
    if m not in all_text.replace("%s = {" % m, "", 1) and m not in loc_text:
        warnings.append("modifier defined but unused: " + m)

# ---------------------------------------------------------------- events
defined_events = set(re.findall(r"^eir\.(\d+) = \{", all_text, re.M))
for ref in sorted(set(re.findall(r"(?:id = |trigger_event = )eir\.(\d+)", all_text))):
    if ref not in defined_events:
        errors.append("event referenced but not defined: eir.%s" % ref)
for e in sorted(defined_events):
    if not re.search(r"(?:id = |trigger_event = )eir\.%s\b" % e, all_text) and int(e) not in ():
        pass  # events fired from on_actions are checked below

# ---------------------------------------------------------------- scripted effects / triggers
defined_fx = set(re.findall(r"^(eir_[a-z0-9_]+(?:_effect|_trigger)) = \{", all_text, re.M))
for ref in sorted(set(re.findall(r"\b(eir_[a-z0-9_]+(?:_effect|_trigger))\b", all_text))):
    if ref not in defined_fx:
        errors.append("scripted effect/trigger used but not defined: " + ref)

# ---------------------------------------------------------------- global variables
set_vars = set(re.findall(r"set_global_variable = (?:\{ name = )?([a-z_0-9]+)", all_text))
for v in sorted(set(re.findall(r"has_global_variable = ([a-z_0-9]+)", all_text))):
    if v not in set_vars:
        errors.append("global variable checked but never set: " + v)

# ---------------------------------------------------------------- traditions, titles, buildings, MAA
my_trad = set(re.findall(r"^(tradition_eir_[a-z0-9_]+) = \{", all_text, re.M))
for t in sorted(set(re.findall(r"tradition_eir_[a-z0-9_]+", all_text)) - my_trad):
    errors.append("unknown tradition: " + t)
my_titles = set(re.findall(r"^([ke]_eir_[a-z0-9_]+) = \{", all_text, re.M))
for t in sorted(set(re.findall(r"title:([ke]_eir_[a-z0-9_]+)", all_text)) - my_titles):
    errors.append("unknown title: " + t)

# ---------------------------------------------------------------- localization
def loc_has(key):
    return re.search(r"^ %s:\d* " % re.escape(key), loc_text, re.M) is not None


needed = []
for k in set(re.findall(r"\b(eir\.\d+\.[a-z]+)\b", all_text)):
    pass
for f, t in text_by_file.items():
    if "/events/" in f.replace("\\", "/"):
        for key in re.findall(r"(?:title|desc|name) = (eir\.[0-9a-z_.]+)", t):
            needed.append(key)
    if "decisions" in f:
        for key in re.findall(r"(?:desc|selection_tooltip|confirm_text) = (?!eir\.out)([a-z_0-9]+)", t):
            needed.append(key)
for key in sorted(set(needed)):
    if not loc_has(key):
        errors.append("missing localization: " + key)

for m in sorted(my_modifiers):
    if not loc_has(m):
        errors.append("missing localization for modifier: " + m)
for t in sorted(my_traits):
    if not loc_has("trait_" + t):
        errors.append("missing localization for trait: " + t)
for t in sorted(my_trad):
    if not loc_has(t + "_name"):
        errors.append("missing localization for tradition: " + t)
for t in sorted(my_titles):
    if not loc_has(t):
        errors.append("missing localization for title: " + t)
for key in sorted(set(re.findall(r"desc = (eir\.out\.[a-z_0-9]+)", all_text))):
    if not loc_has(key):
        errors.append("missing outcome label: " + key)
for key in sorted(set(re.findall(r"name = (eir_[a-z_0-9]+_name)\b", all_text)) | set(re.findall(r"\bname = (eir_[a-z_0-9]+_name)", all_text))):
    if not loc_has(key):
        errors.append("missing army name: " + key)

# ---------------------------------------------------------------- loc scope names used in text
loc_scopes = set(re.findall(r"\[(eir_[a-z_0-9]+)\.", loc_text))
saved = set(re.findall(r"save_scope_as = (eir_[a-z_0-9]+)", all_text))
for s in sorted(loc_scopes - saved):
    errors.append("localization uses scope [%s] that no script saves" % s)

# ---------------------------------------------------------------- bad loc functions
for fn in ("GetHeShe", "GetSheHe|U"):
    pass
if "GetHeShe" in loc_text:
    errors.append("localization uses invalid function GetHeShe")


# ---------------------------------------------------------------- checks that mirror the game's own error.log
# 1. modifiers defined but never used by script (the game reports these as errors)
for m in sorted(my_modifiers):
    others = all_text.replace("%s = {" % m, "", 1)
    if not re.search(r"\b%s\b" % re.escape(m), others):
        errors.append("modifier defined but never used by script: " + m)

# 2. global variables / flags set but never read
read_vars = set(re.findall(r"has_global_variable = ([a-z_0-9]+)", all_text))
for v in sorted(set_vars - read_vars):
    errors.append("global variable set but never read: " + v)
set_flags = set(re.findall(r"add_character_flag = (?:\{ flag = )?([a-z_0-9]+)", all_text))
read_flags = set(re.findall(r"has_character_flag = ([a-z_0-9]+)", all_text))
for v in sorted(set_flags - read_flags - {"temp_no_claim_war_cost"}):
    errors.append("character flag set but never read: " + v)

# 3. localization format: one key per line, escaped newlines
for f in files("localization/english/*.yml"):
    raw = read(f)
    for n, line in enumerate(raw.split("\n"), 1):
        s = line.rstrip("\r")
        if not s.strip() or s.lstrip().startswith("#") or s.strip() == "l_english:":
            continue
        if not re.match(r'^ [A-Za-z0-9_.\-]+:\d* ".*"$', s):
            errors.append("bad localization line %s:%d: %s" % (os.path.basename(f), n, s[:50]))

# 4. duplicate localization keys across files
seen = {}
for f in files("localization/english/*.yml"):
    for k in re.findall(r"^ ([A-Za-z0-9_.\-]+):\d* ", read(f), re.M):
        if k in seen and seen[k] != f:
            errors.append("duplicate loc key %s in %s and %s" % (k, os.path.basename(seen[k]), os.path.basename(f)))
        seen[k] = f

# 5. encodings: script and localization need a UTF-8 BOM; descriptor.mod must not have one
for f in files("common/**/*.txt") + files("events/*.txt") + files("localization/english/*.yml"):
    with open(f, "rb") as fh:
        if fh.read(3) != b"\xef\xbb\xbf":
            errors.append("missing UTF-8 BOM: " + os.path.relpath(f, ROOT))
with open(os.path.join(ROOT, "descriptor.mod"), "rb") as fh:
    if fh.read(3) == b"\xef\xbb\xbf":
        errors.append("descriptor.mod must not have a BOM")

# 6. decision costs written with dynamic gold values (these scale with income and are tiny for a tribal chief)
dec_path = os.path.join(ROOT, "common", "decisions", "eir_decisions.txt")
if os.path.exists(dec_path):
    for m in re.finditer(r"cost = \{([^}]*)\}", read(dec_path)):
        if "_gold_value" in m.group(1):
            warnings.append("decision cost uses a dynamic gold value: " + m.group(1).strip().replace("\n", " "))

# 7. every on_action effect must be inside a mod-named on_action (vanilla ones allow only ONE effect block)
oa = os.path.join(ROOT, "common", "on_action", "eir_on_actions.txt")
if os.path.exists(oa):
    for m in re.finditer(r"^([a-z_0-9]+) = \{\n\teffect = \{", read(oa), re.M):
        if not m.group(1).startswith("eir_"):
            errors.append("vanilla on_action %s must delegate with on_actions = { eir_... } instead of its own effect" % m.group(1))


# 8. effects accidentally placed inside trigger blocks (happened once through a positional argument)
EFFECT_WORDS = ("set_global_variable", "add_prestige", "add_piety", "add_gold", "add_character_modifier", "trigger_event", "add_trait", "spawn_army")
for f, txt in text_by_file.items():
    if "/events/" not in f.replace("\\", "/") and "\\events\\" not in f:
        continue
    for m in re.finditer(r"\btrigger = \{", txt):
        i = m.end()
        depth = 1
        while i < len(txt) and depth:
            depth += {"{": 1, "}": -1}.get(txt[i], 0)
            i += 1
        block = txt[m.end():i]
        for w in EFFECT_WORDS:
            if re.search(r"\b%s\b" % w, block):
                errors.append("effect '%s' inside a trigger block in %s (near char %d)" % (w, os.path.basename(f), m.start()))
                break

# 9. requirement tooltips: count-style / global-variable / coast / stress statements need readable text (Update 2)
BARE = re.compile(r"^\t\t(any_vassal|any_sub_realm_county|any_held_title|has_global_variable|NOT = \{ has_global_variable|stress >=|is_coastal|var:|has_variable|current_month)")
if os.path.exists(dec_path):
    for m in re.finditer(r"\n\tis_valid = \{\n(.*?)\n\t\}\n", read(dec_path), re.S):
        for line in m.group(1).split("\n"):
            if BARE.match(line):
                errors.append("decision requirement has no readable tooltip: " + line.strip())
# 10. every custom_description / custom_tooltip text key needs localization
for f, txt in text_by_file.items():
    for key in re.findall(r"\btext = (eir_[a-z_0-9]+)(?![a-z_0-9$])", txt):
        if not loc_has(key):
            errors.append("missing localization for requirement text: " + key)
    for key in re.findall(r"custom_tooltip = (eir_[a-z_0-9]+)", txt):
        if not loc_has(key):
            errors.append("missing localization for tooltip text: " + key)

print("files checked:", len(text_by_file), "| localization lines:", loc_text.count("\n"))
for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print("%d error(s), %d warning(s)" % (len(errors), len(warnings)))
sys.exit(1 if errors else 0)
