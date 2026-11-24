#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — one short, funny rant.

Writes a single original rant about an everyday annoyance (a smoke
detector's 3 a.m. low-battery chirp) to /output/entry.txt.
287 characters, one block, no trailing newline.
Deterministic, stdlib only, no network.

Run:  python3 main.py
"""

import os
import sys

RANT = (
    "The smoke detector waits until 3 a.m. to tell me its battery is dying. "
    "One chirp. Then silence, just long enough for me to fall back asleep. "
    "It has done this four nights in a row. "
    "It is not warning me about a fire. It is negging me. "
    "Judge, the detector is fine. I am the one beeping now."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def clear_contents(path):
    """Remove only the contents of path, never path itself."""
    for name in os.listdir(path):
        target = os.path.join(path, name)
        if os.path.islink(target) or os.path.isfile(target):
            os.unlink(target)
        elif os.path.isdir(target):
            for root, dirs, files in os.walk(target, topdown=False):
                for f in files:
                    os.unlink(os.path.join(root, f))
                for d in dirs:
                    link = os.path.join(root, d)
                    if os.path.islink(link):
                        os.unlink(link)
                    else:
                        os.rmdir(link)
            os.rmdir(target)
        else:
            os.unlink(target)


def main():
    text = RANT
    if not (1 <= len(text) <= 400):
        print(f"rant is {len(text)} chars, must be 1-400", file=sys.stderr)
        return 1
    if not text.strip():
        print("rant is blank", file=sys.stderr)
        return 1
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    clear_contents(OUTPUT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
