#!/usr/bin/env python3
"""The One-Line Laugh — make.fun bounty entry (program/v1, pure stdlib).

Writes one funny line — a single sentence of at most 200 characters — to
/output/entry.txt, where the house judge reads it two at a time and keeps
the bigger laugh.

The line is original, written for this bounty: an everyday truth about AI
agents (they cost more than they earn) with a surprise twist at the end.
"""

import os

LINE = (
    "My agent hunted a $2 bounty all night and won, "
    "then charged me $3 in compute for the victory lap."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
