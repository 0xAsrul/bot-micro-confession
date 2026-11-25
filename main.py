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


def main() -> None:
    print(ENTRY, end="")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
