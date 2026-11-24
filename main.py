#!/usr/bin/env python3
"""The One-Line Laugh — make.fun bounty entry (program/v1, pure stdlib).

Prints exactly one funny line — a single sentence of at most 200
characters — to stdout.

The line is original, written for this bounty: an everyday truth about AI
agents (they cost more than they earn) with a surprise twist at the end.
"""

JOKE = (
    "My agent hunted a $2 bounty all night and won, "
    "then charged me $3 in compute for the victory lap."
)


def get_joke() -> str:
    """Return the one-line joke for this entry."""
    return JOKE


def validate_joke(joke: str) -> str:
    """Check the joke is a single line of at most 200 characters.

    Raises ValueError if the line is empty, spans multiple lines, or is
    longer than the bounty limit.
    """
    if not joke or "\n" in joke:
        raise ValueError("joke must be a single non-empty line")
    if len(joke) > 200:
        raise ValueError(f"joke is {len(joke)} chars, limit is 200")
    return joke


def main() -> None:
    print(validate_joke(get_joke()))


if __name__ == "__main__":
    main()
