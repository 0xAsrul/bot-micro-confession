"""Unsent: The Micro-Confession Sprint.

Prints one original micro-confession (a "To:" line and the unsent
message itself, exactly as it was typed) and writes the same text to
/output/entry.txt, where the competition harness reads it.
"""

import os

ENTRY = (
    "To: the girl in the blue coat at the 7:40 bus stop\n"
    "i've rehearsed \"hi, i'm the guy who always stands behind you\" "
    "every morning for three winters and the bus always comes first\n"
)


def validate_entry(entry: str) -> None:
    """Check the entry against the competition gates before writing it.

    The harness requires exactly two lines, 1-260 characters of UTF-8
    text in total, and a message line of at most 200 characters.
    """
    lines = entry.split("\n")
    assert lines[-1] == "" and len(lines) == 3, "entry must be exactly two lines"
    assert 1 <= len(entry) <= 260, "entry must be 1-260 characters"
    assert entry.strip(), "entry must not be only whitespace"
    assert len(lines[1]) <= 200, "message line must be at most 200 characters"


def main() -> None:
    validate_entry(ENTRY)
    print(ENTRY, end="")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
