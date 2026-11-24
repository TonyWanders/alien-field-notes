#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line, an alien tourist's review of planet Earth,
to /output/entry.txt. Deterministic: the same line on every run.
"""

import os

MAX_CHARS = 200

REVIEW = (
    "Came to review the famous blue planet. Stayed for the street food, "
    "left because a goose declared war on me. Four stars, would waddle back."
)


def main():
    text = REVIEW.strip()
    assert text and not text.isspace(), "review must not be blank"
    assert len(text) <= MAX_CHARS, (
        f"review is {len(text)} chars, over the {MAX_CHARS} cap"
    )
    assert "\n" not in text, "review must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
