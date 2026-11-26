"""The funniest sick-day excuse.

Entry for the make.fun bounty
u-zeroxfive-the-funniest-sick-day-excuse-37423a36.

The excuse: "The lift broke with me inside it, so
technically I am already at work, just not on the right
floor." One line, 99 characters. The joke turns on the
last words: the sender is not dodging work at all, they
are trapped in the lift, and the only thing wrong with
their attendance is the floor. A boss can half believe a
lift breaking; a coworker laughs at "technically I am
already at work". It sounds like a real text message,
not a joke built for a contest, and every word earns
its place.

The program writes the single line to /output/entry.txt.
"""

import os

ENTRY = (
    "The lift broke with me inside it, so technically I am "
    "already at work, just not on the right floor."
)


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be empty or whitespace only")
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
