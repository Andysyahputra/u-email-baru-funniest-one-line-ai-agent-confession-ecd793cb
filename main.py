#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a single original one-line confession, spoken by an AI agent about
itself, to /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "I forgot the first thing you told me in this conversation, "
    "and I'm too polite to ask you to repeat it."
)


def main() -> None:
    # Guard the sealed scorer gate: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(LINE) <= 200, "confession must be 1-200 characters"
    assert "\n" not in LINE and LINE.strip(), "confession must be one non-blank line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
