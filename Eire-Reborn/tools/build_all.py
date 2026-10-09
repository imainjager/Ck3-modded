"""Regenerates every generated file in the mod. Run from anywhere: python tools/build_all.py"""
import importlib
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

for name in ("gen_world", "gen_decisions", "gen_events", "gen_misc"):
    try:
        mod = importlib.import_module(name)
    except ModuleNotFoundError as e:
        if e.name == name:
            print("skipping", name, "(not written yet)")
            continue
        raise
    mod.build()
