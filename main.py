#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line — entry writer.

Writes one original one-line review to /output/entry.txt.

The review (written fresh for this bounty):
    One star. The dish sponge soaks up everyone else's mess, then gets
    thrown out the day it starts smelling like its job.

Why this line: a dish sponge is about as boring and everyday as an object
gets, and its dullness is the joke — it does exactly the job it was bought
for, soaking up other people's messes, and its reward is being thrown away
the moment it starts smelling like the work it does. The detail is true
and recognisable (a sponge goes smelly and gets binned), the turn comes
early ("then gets thrown out"), and the last words sharpen it.
"""

import os
from pathlib import Path

REVIEW = (
    "One star. The dish sponge soaks up everyone else's mess, "
    "then gets thrown out the day it starts smelling like its job."
)

# The grader runs the program with /output mounted; allow an override for local runs.
OUTPUT_PATH = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))


def gate(text: str) -> None:
    """Self-check mirroring the bounty gate: UTF-8, 1-200 chars, not only whitespace.

    Also rejects control characters (other than tab/newline) and requires
    a single line, since the entry is one line of at most 200 characters.
    """
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    bad = [c for c in text if ord(c) < 32 and c not in ("\t", "\n")]
    if bad:
        raise ValueError(f"entry contains control characters: {bad!r}")


def main() -> None:
    gate(REVIEW)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(REVIEW, encoding="utf-8")
    # Read-back verification: what landed on disk is exactly the review.
    if OUTPUT_PATH.read_text(encoding="utf-8") != REVIEW:
        raise ValueError("read-back mismatch: written review differs from REVIEW")
    print(f"Wrote {len(REVIEW)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
