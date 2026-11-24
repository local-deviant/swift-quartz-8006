"""The Robot Pickup Line Championship — entry program.

Writes a single pickup line (at most 200 characters) in the voice
of a robot trying to charm someone, to /output/entry.txt, the path
the grader reads.

The line turns Asimov's Second Law — a robot must obey orders
given by a human — into the flirt itself: the robot does not
choose to stay, it asks to be ordered to stay. That is the joke
the judge brief rewards: a robot's line (criterion 1) whose humour
grows out of being a machine (criterion 2), with the turn landing
from an angle the reader did not see coming (criterion 3), in 73
characters with no padding (criterion 4), charming rather than
creepy (criterion 5).

Local testing: set ENTRY_OUTPUT to a local path so the run does
not touch the shared /output directory, e.g.
    ENTRY_OUTPUT=output/entry.txt python3 main.py

Standard library only, deterministic, no network, no file reads.
"""

import os
import sys
from pathlib import Path

LINE = "My Second Law says I must obey your orders \u2014 so please, order me to stay."


def validate(text: str) -> None:
    """Check the bounty gate before writing: UTF-8 text of 1 to 200
    characters, a single line, not only white space."""
    if not text:
        sys.exit("gate: entry text is empty")
    if not text.strip():
        sys.exit("gate: entry text is only white space")
    if len(text) > 200:
        sys.exit(f"gate: entry text is {len(text)} characters, over 200")
    if "\n" in text or "\r" in text:
        sys.exit("gate: entry text must be a single line")
    if text != text.strip():
        sys.exit("gate: entry text has leading or trailing space")


def main() -> None:
    validate(LINE)
    output = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file is exactly the one line, nothing else.
    output.write_text(LINE, encoding="utf-8")
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(output, 0o644)


if __name__ == "__main__":
    main()
