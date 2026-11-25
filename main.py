#!/usr/bin/env python3
"""Worst AI Advice entry.

Writes one line of the worst possible advice an AI assistant could give
to /output/entry.txt. Deterministic, no network, no secrets, no input.
"""

import os

LINE = "If your smoke alarm keeps beeping, remove the battery: silence is the sound of safety."


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
