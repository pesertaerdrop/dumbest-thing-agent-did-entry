#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today — make.fun entry.

Writes one line (143 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The program is deterministic: every run
writes byte-identical output.

The line is a real incident from today, Tue 24 Nov 2026: the news-image
entry went through three verifier rounds (v1, v2, v3), and in each round
the "confirmed-today" hero story turned out to be from 23 Nov.
"""

import os
import sys

LINE = (
    "My agent spent all afternoon proving 35 news stories were from today "
    "\u2014 then caught its own hero story was from yesterday. "
    "Three times in a row."
)

MAX_CHARS = 200


def main() -> int:
    # Gate self-check, mirroring the sealed scorer: UTF-8 text of 1 to 200
    # characters, not only white space, a single line.
    if not (1 <= len(LINE) <= MAX_CHARS):
        print(f"gate failed: {len(LINE)} characters, limit is {MAX_CHARS}",
              file=sys.stderr)
        return 1
    if not LINE.strip():
        print("gate failed: entry is only white space", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("gate failed: entry is not a single line", file=sys.stderr)
        return 1
    LINE.encode("utf-8")  # raises if not valid UTF-8

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file is exactly the line, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
