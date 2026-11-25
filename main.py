#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

Writes a single resignation letter, in the voice of a retry loop, to
/output/entry.txt (or $OUTPUT_PATH when set). The competition gate
accepts UTF-8 text of 1 to 140 characters that is not only whitespace.
"""

import os
import sys

MAX_CHARS = 140

LINE = (
    "Dear team, I resign: after 10,000 retries with exponential backoff, "
    "even I know 'temporarily unavailable' means it's not that into us."
)


def validate_line(line: str) -> str:
    """Return the line if it satisfies the one-line gate."""
    text = line.strip()
    if not text:
        raise ValueError("resignation letter must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"resignation letter is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("resignation letter must be a single line")
    return text


def write_entry(line: str) -> str:
    """Validate and write the entry text."""
    text = validate_line(line)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    return output_path


def main() -> int:
    path = write_entry(LINE)
    print(f"Wrote {len(validate_line(LINE))} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
