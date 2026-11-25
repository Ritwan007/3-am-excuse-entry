#!/usr/bin/env python3
"""The 3 AM Excuse — entry program (make.fun competition
u-hazel-walrus-38-4764-the-3-am-excuse-c1017878).

Writes one line, in the voice of a hardware wallet refusing to sign a
transaction at 3 AM, to /output/entry.txt.

The line is the champion of a 16-candidate single-elimination bracket
judged against the published criteria in order: on subject, originality,
the wallet's voice, the 3 AM hour as the joke, economy of wording.
The wallet treats its owner as two different people — 3 AM you is not
on the approved list; only 9 AM you can vouch for him.

Gate (mirrors the sealed scorer): the text must be UTF-8, 1-200
characters, a single line, and not only whitespace. verify() raises
before anything is written if the line violates the gate.
"""

import os

LINE = "3 AM you is not on my approved list. Come back when 9 AM you can vouch for him."


def verify(line: str) -> None:
    """Raise ValueError if `line` violates the entry gate."""
    line.encode("utf-8")  # raises UnicodeEncodeError on lone surrogates
    if not line.strip():
        raise ValueError("entry is blank or only whitespace")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry is {len(line)} chars, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")


def main() -> None:
    verify(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
