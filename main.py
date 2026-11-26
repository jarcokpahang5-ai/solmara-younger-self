#!/usr/bin/env python3
"""One Line to Your Younger Self — a one-line make.fun entry.

This script keeps the entry line, checks that it is a single line of
sensible length, and writes it to /output/entry.txt. It needs nothing
beyond the Python 3 standard library and talks to no network.
"""

import sys
from pathlib import Path

LINE = 'Dear younger me: stop rehearsing arguments in the shower — you will never win them, and the hot water will never forgive you.'
MAX_LENGTH = 200
TARGET = Path("/output/entry.txt")


def find_problems(text):
    """List every way the line breaks the one-line rules (empty = fine)."""
    if not isinstance(text, str):
        return ["entry is not text"]
    problems = []
    if text == "":
        problems.append("entry is empty")
    if text != text.strip():
        problems.append("entry has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("entry spans more than one line")
    if len(text) > MAX_LENGTH:
        problems.append("entry is longer than the limit")
    return problems


def save(text):
    """Write the line plus exactly one newline to /output/entry.txt."""
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    TARGET.chmod(0o644)
    if TARGET.read_bytes() != (text + "\n").encode("utf-8"):
        raise ValueError("written file does not match the entry line")


def main():
    problems = find_problems(LINE)
    if problems:
        print("entry line failed its checks: " + problems[0], file=sys.stderr)
        return 1
    save(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
