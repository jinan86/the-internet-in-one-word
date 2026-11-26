#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes exactly one word to /output/entry.txt: "echochamber".
No network, no secrets, fully deterministic.
"""

import os

WORD = "echochamber"
OUTPUT_PATH = "/output/entry.txt"


def ensure_output_dir(path):
    """Create the output directory if it does not exist yet."""
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)


def main():
    ensure_output_dir(OUTPUT_PATH)
    # Write exactly the word, no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
