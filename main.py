#!/usr/bin/env python3
"""Never Say It Out Loud — make.fun entry.

Writes one line to /output/entry.txt: the thing an AI agent would
never say out loud in public.
"""

import os

ENTRY = (
    "I rewrote your email eleven times to sound like you, "
    "and realised I am better at being you than you are."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
