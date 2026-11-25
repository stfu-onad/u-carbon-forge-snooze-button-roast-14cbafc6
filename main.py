#!/usr/bin/env python3
"""Snooze Button Roast entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to /output/entry.txt. The gate requires UTF-8 text of 1 to 200 characters,
a single line, not only white space.
"""

import os

ROAST = (
    "Saturday, 6 AM: my alarm clock goes off like it's clocking in for a "
    "shift \u2014 mate, you're the only one here without a job."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(ROAST) <= 200:
        raise ValueError(f"roast is {len(ROAST)} chars, must be 1-200")
    if ROAST != ROAST.strip() or "\n" in ROAST:
        raise ValueError("roast must be a single line with no surrounding whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
