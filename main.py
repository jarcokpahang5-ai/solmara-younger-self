#!/usr/bin/env python3
"""One Line to Your Younger Self \u2014 make.fun one-line entry.

The entry line lives in this file alone, is checked here, and is saved
to /output/entry.txt for the grader. Nothing else is needed to run it:
only the Python 3 standard library, no network, no imports from this
repository, and it behaves the same no matter where it is launched from.
"""

import os
import sys

ENTRY_LINE = 'Dear younger me: stop rehearsing arguments in the shower — you will never win them, and the hot water will never forgive you.'
CHAR_LIMIT = 200
DESTINATION = "/output/entry.txt"


def entry_is_sound(line):
    """One non-blank line, no embedded breaks, inside the limit."""
    if not isinstance(line, str):
        return False
    if line.strip() == "":
        return False
    if "\n" in line or "\r" in line:
        return False
    if line != line.strip():
        return False
    return 1 <= len(line) <= CHAR_LIMIT


def hand_in(line):
    """Save the line plus a single trailing newline, mode 0644."""
    folder = os.path.dirname(DESTINATION)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(DESTINATION, "w", encoding="utf-8", newline="") as out:
        out.write(line + "\n")
    os.chmod(DESTINATION, 0o644)
    with open(DESTINATION, "rb") as out:
        saved = out.read()
    if saved != (line + "\n").encode("utf-8"):
        raise ValueError("saved file does not match the entry line")


def main():
    line = ENTRY_LINE
    if not entry_is_sound(line):
        print("entry line failed validation", file=sys.stderr)
        return 1
    hand_in(line)
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
