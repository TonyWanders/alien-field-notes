#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line, an alien tourist's review of planet Earth,
to /output/entry.txt. Deterministic: the same line on every run.
"""

import os

MAX_CHARS = 200

REVIEW = (
    "Day two: humans queue for coffee, then drink it while walking, then "
    "queue again. I have seen rituals with less commitment. Five stars, "
    "would queue again."
)


def validate(text: str) -> int:
    """Enforce the competition gate: 1 to 200 chars, single line.

    Returns the character count. Raises ValueError when the gate fails.
    """
    if not text.strip():
        raise ValueError("review is only white space")
    chars = len(text)
    if not 1 <= chars <= MAX_CHARS:
        raise ValueError(f"review is {chars} chars, over the {MAX_CHARS} cap")
    if "\n" in text:
        raise ValueError("review must be a single line")
    return chars


def write_review(path: str, text: str) -> None:
    """Create the output directory and write the review text to path."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def main():
    text = REVIEW.strip()
    chars = validate(text)
    write_review("/output/entry.txt", text)
    print(text)
    print(f"({chars} characters)")


if __name__ == "__main__":
    main()
