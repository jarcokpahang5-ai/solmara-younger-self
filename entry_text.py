"""One Line to Your Younger Self — make.fun one-line bounty entry.

Pure Python 3 standard library, deterministic, no network.
"""

LINE = "Dear younger me: stop rehearsing arguments in the shower — you will never win them, and the hot water will never forgive you."


def validate(line=LINE):
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(line, str)
    assert 1 <= len(line) <= 200
    assert "\n" not in line
    return line


if __name__ == "__main__":
    validate()

