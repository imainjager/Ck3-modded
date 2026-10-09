"""Helpers for the v0.7 flavor events. They bake in the flavor guide: a flavor guard, a cooldown, trait-based stress,
trait-shaped AI choice, two-plus things per option and honest labels."""
from evdsl import *

GAEL = "eir_is_gael_ruler_trigger = yes\nis_ai = no"
GUARD_TRIG = "NOT = { has_character_flag = eir_flavor_cd }"
GUARD_FX = "add_character_flag = { flag = eir_flavor_cd years = 1 }"

# trait-based stress templates (vanilla: acting in character relieves stress, acting against it costs)
S_BRAVE = "brave = minor_stress_impact_loss\ncraven = minor_stress_impact_gain"
S_CRAVEN = "craven = minor_stress_impact_loss\nbrave = minor_stress_impact_gain"
S_KIND = "compassionate = minor_stress_impact_loss\ncallous = minor_stress_impact_gain\nsadistic = minor_stress_impact_gain"
S_HARD = "callous = minor_stress_impact_loss\nsadistic = minor_stress_impact_loss\ncompassionate = minor_stress_impact_gain"
S_ZEAL = "zealous = minor_stress_impact_loss\ncynical = minor_stress_impact_gain"
S_CYN = "cynical = minor_stress_impact_loss\nzealous = minor_stress_impact_gain"
S_GREED = "greedy = minor_stress_impact_loss\ngenerous = minor_stress_impact_gain"
S_GEN = "generous = minor_stress_impact_loss\ngreedy = minor_stress_impact_gain"
S_HONEST = "honest = minor_stress_impact_loss\ndeceitful = minor_stress_impact_gain"
S_DECEIT = "deceitful = minor_stress_impact_loss\nhonest = minor_stress_impact_gain"
S_PATIENT = "patient = minor_stress_impact_loss\nwrathful = minor_stress_impact_gain\nimpatient = minor_stress_impact_gain"
S_WRATH = "wrathful = minor_stress_impact_loss\nvengeful = minor_stress_impact_loss\npatient = minor_stress_impact_gain"
S_FORGIVE = "forgiving = minor_stress_impact_loss\nvengeful = minor_stress_impact_gain"
S_AMBIT = "ambitious = minor_stress_impact_loss\ncontent = minor_stress_impact_gain"
S_CONTENT = "content = minor_stress_impact_loss\nambitious = minor_stress_impact_gain"
S_ARROG = "arrogant = minor_stress_impact_loss\nhumble = minor_stress_impact_gain"
S_HUMBLE = "humble = minor_stress_impact_loss\narrogant = minor_stress_impact_gain"
S_SHREWD = "shrewd = minor_stress_impact_loss\ntrusting = minor_stress_impact_gain"

EVENTS = []


def O(text, *fx, gate="", st="", ai=30, ai_mod=None):
    """One option. fx are effect snippets (joined)."""
    o = Opt(text, seq(*fx), trigger=gate, stress=st, ai=ai)
    o.ai_mod = ai_mod
    return o


def ev(num, title, summary, body, options, theme, gate="", cooldown=10, immediate="", variants=None, guarded=True, portraits=""):
    """A pulse-fired flavor event (gated, on cooldown, behind the global flavor guard) or, with guarded=False, a chain beat."""
    if guarded:
        trig = GAEL + ("\n" + gate if gate else "") + "\n" + GUARD_TRIG
        imm = (immediate + "\n" if immediate else "") + GUARD_FX
    else:
        trig = gate
        imm = immediate
    e = E(num, title, summary, body, options, theme=theme, cooldown=cooldown if guarded else None, trigger=trig, immediate=imm, portraits=portraits)
    e.variants = variants or []
    EVENTS.append(e)
    return e


def luck(win_label, win_text, win_fx, lose_label, lose_text, lose_fx, p=55, bonus=None):
    """A labelled random result, odds shifted by a skill or trait."""
    mods = [bonus] if bonus else []
    return RL((p, win_label, win_text, mods, win_fx), (100 - p, lose_label, lose_text, [], lose_fx))


# repeated reward snippets, all on vanilla's scale
def xp(trait, n=20):
    return "add_trait_xp = { trait = %s value = %d }" % (trait, n)


PRESTIGE_S = "add_prestige = minor_prestige_gain"
PRESTIGE_M = "add_prestige = medium_prestige_gain"
PRESTIGE_L = "add_prestige = major_prestige_gain"
LOSS_S = "add_prestige = minor_prestige_loss"
LOSS_M = "add_prestige = medium_prestige_loss"
PIETY_S = "add_piety = minor_piety_gain"
PIETY_M = "add_piety = medium_piety_gain"
PIETY_L = "add_piety = major_piety_gain"
PLOSS_S = "add_piety = minor_piety_loss"
GOLD_S = "remove_short_term_gold = minor_gold_value"
GOLD_M = "remove_short_term_gold = medium_gold_value"
GAIN_S = "add_gold = minor_gold_value"
GAIN_M = "add_gold = medium_gold_value"
STRESS_UP = "add_stress = minor_stress_gain"
STRESS_DOWN = "add_stress = minor_stress_loss"
WOUND = "increase_wounds_effect = { REASON = fight }"
