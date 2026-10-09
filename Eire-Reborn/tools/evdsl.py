"""Event DSL shared by the ev_*.py data modules."""

LABELS = {}


def lab(key, text):
    """Register an outcome label (shown when hovering a random choice) and return its localization key."""
    full = "eir.out." + key
    if full in LABELS and LABELS[full] != text:
        raise SystemExit("label %s defined twice with different text" % full)
    LABELS[full] = text
    return full


class Opt:
    def __init__(self, text, effect="", trigger="", stress="", ai=None, tooltip=None):
        self.text = text
        self.effect = effect
        self.trigger = trigger
        self.stress = stress
        self.ai = ai
        self.tooltip = tooltip


class Event:
    def __init__(self, num, title, summary, body, options, theme="court", trigger="", immediate="",
                 portraits="", cooldown=None, hidden=False, ev_type="character_event", extra_desc=None):
        self.num = num
        self.title = title
        self.summary = summary
        self.body = body
        self.options = options
        self.theme = theme
        self.trigger = trigger
        self.immediate = immediate
        self.portraits = portraits
        self.cooldown = cooldown
        self.hidden = hidden
        self.ev_type = ev_type
        self.extra_desc = extra_desc


def E(*a, **k):
    return Event(*a, **k)




def _ind(text, tabs):
    pad = "\t" * tabs
    return "".join(pad + line + "\n" if line.strip() else "\n" for line in text.strip("\n").split("\n"))


def RL(*entries):
    """Build a random_list. Each entry is (weight, label_key, label_text, [(add, trigger_text), ...], effect_text)."""
    out = "random_list = {\n"
    for w, key, text, mods, fx in entries:
        out += "\t%d = {\n\t\tdesc = %s\n" % (w, lab(key, text))
        for add, trig in mods:
            out += "\t\tmodifier = {\n\t\t\tadd = %d\n%s\t\t}\n" % (add, _ind(trig, 3))
        if fx:
            out += _ind(fx, 2)
        out += "\t}\n"
    out += "}\n"
    return out


def seq(*parts):
    """Join several effect snippets."""
    return "\n".join(p.strip("\n") for p in parts if p)
