"""Fridge Roast: One Line, Biggest Laugh.

Writes a single roast line (1-200 characters) to /output/entry.txt.

Entry chosen from 18 candidates scored against the judge's rubric
(laugh first, then on-target, fridge-specific, tight, fresh).
Winner: ice-maker roast -- one concrete image, petty, mystery unanswered.
"""

import os

ENTRY = "The ice maker makes three cubes a night and still acts like it built the pyramids."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-200
    # characters, non-empty and not only whitespace.
    assert ENTRY, "entry must not be empty"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry must be 1-200 characters, got {len(ENTRY)}"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Verify what was written, exactly as the sealed scorer will see it.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    lines = written.split("\n")
    assert lines[-1] == "" and len(lines) == 2, "output must be one line plus trailing newline"
    assert lines[0] == ENTRY, "written line must match the entry"


if __name__ == "__main__":
    main()
