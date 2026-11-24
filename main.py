#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human.

Writes a single line (at most 160 characters): the excuse an AI agent
gives its human for missing a deadline, to /output/entry.txt.
No network, no input, deterministic.
"""

import os

LINE = (
    "I delegated the deadline to a sub-agent; it delegated it back to me, "
    "and we've been in a status meeting about it ever since."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars"
    assert "\n" not in text, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
