#!/usr/bin/env python3
"""Famous Last Words at 1 Percent entry.

Writes the funniest last words a phone could say as its battery
hits 1 percent, to /output/entry.txt (1-199 characters, UTF-8, a
single line). Standard library only, no network, no input.

The line is built from two fragments: a setup (the phone survived
400 notifications, 12 alarms and one very long video, and this is
how it ends) and a punch (the line itself dies mid-sentence, cut
off in the middle of the word "like"). ``assemble`` joins them into
the single line; ``validate`` checks the entry gate before anything
is written.
"""

from pathlib import Path

SETUP = "I survived 400 notifications, 12 alarms and one very long video, and this is how it ends:"
PUNCH = "mid-sentence, like—"

OUTPUT_PATH = Path("/output/entry.txt")


def assemble(setup: str, punch: str) -> str:
    """Join the setup and punch fragments into one last line."""
    return f"{setup} {punch}"


def validate(line: str) -> str:
    """Check the line meets the entry gate before it is written.

    Must be 1-199 characters, UTF-8-encodable, a single line, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(line) <= 199:
        raise ValueError(f"line must be 1-199 characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line (no newline characters)")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> None:
    line = validate(assemble(SETUP, PUNCH))
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line, encoding="utf-8")


if __name__ == "__main__":
    main()
