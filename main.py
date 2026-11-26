#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line, the office printer's comeback to the paper jams, the
cryptic error codes and the thumps, to /output/entry.txt.

Deterministic, offline, standard library only: no randomness, no network,
no timestamps, no paths that change between runs.
"""

import os

ENTRY = (
    "Error 51, tray 1: I shredded all 9 copies of your "
    "'final_v2_FINAL'. You call it a paper jam. I call it editing."
)


def main() -> None:
    try:
        os.makedirs("/output", exist_ok=True)
        path = "/output/entry.txt"
    except OSError:
        os.makedirs("output", exist_ok=True)
        path = os.path.join("output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
