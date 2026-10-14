"""Generates events/eir_events_*.txt and localization from the data modules ev_*.py.

An event is described with E(...). Options are Opt(...). Everything the text needs is generated together
so keys cannot go missing. Run tools/validate.py afterwards.
"""
import importlib
import io
import re
from eir_lib import *
from evdsl import Opt, Event, E, lab, LABELS

EVENT_FILES = {}   # filename -> list of events


def ind(text, tabs):
    pad = "\t" * tabs
    return "".join(pad + line + "\n" if line.strip() else "\n" for line in text.strip("\n").split("\n"))


# events that a decision fires: their own trigger must not block the decision (a click that shows nothing); the decision sets a flag first
DEC_FIRED = {}


def render(ev, L):
    key = "eir.%04d" % ev.num
    out = ["%s = {\n" % key]
    if ev.hidden:
        out.append("\ttype = character_event\n\thidden = yes\n")
    else:
        variants = getattr(ev, "variants", None) or []
        if variants:
            # vanilla-style conditional text: the first matching variant wins, the plain text is the fallback
            d = "\tdesc = {\n\t\tfirst_valid = {\n"
            for i, (trig, _txt) in enumerate(variants, 1):
                d += "\t\t\ttriggered_desc = {\n\t\t\t\ttrigger = {\n%s\t\t\t\t}\n\t\t\t\tdesc = %s.v%d\n\t\t\t}\n" % (ind(trig, 5), key, i)
            d += "\t\t\tdesc = %s.desc\n\t\t}\n\t}\n" % key
            out.append("\ttype = %s\n\ttitle = %s.t\n%s\ttheme = %s\n" % (ev.ev_type, key, d, ev.theme))
        else:
            out.append("\ttype = %s\n\ttitle = %s.t\n\tdesc = %s.desc\n\ttheme = %s\n" % (ev.ev_type, key, key, ev.theme))
    if ev.cooldown:
        out.append("\tcooldown = { years = %d }\n" % ev.cooldown)
    if ev.portraits and not ev.hidden:
        out.append(ind(ev.portraits, 1))
    if ev.trigger and ev.num in DEC_FIRED:
        out.append("\n\ttrigger = {\n\t\tOR = {\n\t\t\thas_character_flag = eir_dec_ev_%04d\n\t\t\tAND = {\n%s\t\t\t}\n\t\t}\n\t}\n" % (ev.num, ind(ev.trigger, 4)))
        FLAGGED.add(ev.num)
    elif ev.trigger:
        out.append("\n\ttrigger = {\n%s\t}\n" % ind(ev.trigger, 2))
    if ev.immediate:
        out.append("\n\timmediate = {\n%s\t}\n" % ind(ev.immediate, 2))
    if not ev.hidden:
        L.add(key + ".t", ev.title)
        L.add(key + ".desc", "#bold %s#!\n\n%s" % (ev.summary, ev.body) if ev.body else "#bold %s#!" % ev.summary)
        for i, (_trig, txt) in enumerate(getattr(ev, "variants", None) or [], 1):
            L.add("%s.v%d" % (key, i), "#bold %s#!\n\n%s" % (ev.summary, txt))
        for i, o in enumerate(ev.options):
            letter = "abcdefghij"[i]
            out.append("\n\toption = {\n\t\tname = %s.%s\n" % (key, letter))
            if o.trigger:
                out.append("\t\ttrigger = {\n%s\t\t}\n" % ind(o.trigger, 3))
            if o.stress:
                out.append("\t\tstress_impact = {\n%s\t\t}\n" % ind(o.stress.replace(" ", "\n", 0), 3))
            if o.effect:
                out.append(ind(o.effect, 2))
            if o.ai is not None:
                mods = getattr(o, "ai_mod", None) or []
                if mods:
                    body = "".join("\t\t\tmodifier = {\n\t\t\t\tadd = %d\n\t\t\t\thas_trait = %s\n\t\t\t}\n" % (a, t) for t, a in mods)
                    out.append("\t\tai_chance = {\n\t\t\tbase = %d\n%s\t\t}\n" % (o.ai, body))
                else:
                    out.append("\t\tai_chance = { base = %d }\n" % o.ai)
            out.append("\t}\n")
            L.add("%s.%s" % (key, letter), o.text)
    out.append("}\n\n")
    return "".join(out)


def load_groups():
    groups = {}
    for mod in ("ev_tanistry", "ev_vikings", "ev_foreign", "ev_flavor", "ev_church_court", "ev_history", "ev_celtic", "ev_rewards", "ev_era867", "ev_resist", "ev_chains", "ev_extra", "ev_v5", "ev_v6", "ev_v7a", "ev_v7b", "ev_v7c", "ev_v7d", "ev_v8a", "ev_v8b", "ev_v8c", "ev_v8d", "ev_conq", "ev_brit", "ev_gsu", "ev_celt", "ev_tenet", "ev_u8", "ev_u8b", "ev_u8c"):
        try:
            m = importlib.import_module(mod)
        except ModuleNotFoundError as e:
            if e.name == mod:
                continue
            raise
        groups[mod] = m.EVENTS
    # risky extra options for events that had no downside (defined in ev_v6.PATCH)
    try:
        import ev_v6
        for evs in groups.values():
            for ev in evs:
                for opt in ev_v6.PATCH.get(ev.num, []):
                    if opt not in ev.options:
                        ev.options.append(opt)
    except ModuleNotFoundError:
        pass
    return groups


FLAGGED = set()


def build():
    dec_path = path("common", "decisions", "eir_decisions.txt")
    dec_text = io.open(dec_path, encoding="utf-8-sig").read()
    for m in re.finditer(r"trigger_event = (?:\{ id = )?eir\.(\d+)(?: days = (\d+))?", dec_text):
        DEC_FIRED[int(m.group(1))] = max(DEC_FIRED.get(int(m.group(1)), 0), int(m.group(2) or 0))
    groups = load_groups()
    total = 0
    seen = set()
    for i, (name, events) in enumerate(groups.items(), start=1):
        L = Loc("eir_%s_l_english.yml" % name)
        out = ["namespace = eir\n\n# Eire Reborn - %s. Generated by tools/gen_events.py\n\n" % name]
        for ev in events:
            if ev.num in seen:
                raise SystemExit("duplicate event number %d" % ev.num)
            seen.add(ev.num)
            out.append(render(ev, L))
        text = "".join(out)
        # lifestyle traits with several XP tracks need the track named (hunter: hunter/falconer; traveler: travel/danger)
        text = re.sub(r"trait = lifestyle_hunter value", "trait = lifestyle_hunter track = hunter value", text)
        text = re.sub(r"trait = lifestyle_traveler value", "trait = lifestyle_traveler track = travel value", text)
        write("events/eir_%s.txt" % name, text)
        L.write()
        total += len(events)
    # the decisions that fire those events set the bypass flag first
    lines = []
    for line in dec_text.split("\n"):
        m = re.match(r"^([ \t]*)trigger_event = (?:\{ id = )?eir\.(\d+)", line)
        if m and int(m.group(2)) in FLAGGED:
            num = int(m.group(2))
            lines.append("%sadd_character_flag = { flag = eir_dec_ev_%04d days = %d }" % (m.group(1), num, DEC_FIRED[num] + 3))
        lines.append(line)
    write("common/decisions/eir_decisions.txt", "\n".join(lines))
    print("events fired by decisions that got a bypass flag:", len(FLAGGED))
    LL = Loc("eir_event_labels_l_english.yml")
    for k in sorted(LABELS):
        LL.add(k, LABELS[k])
    LL.write()
    print("events:", total, "in", len(groups), "files;", len(LABELS), "outcome labels")


if __name__ == "__main__":
    build()
