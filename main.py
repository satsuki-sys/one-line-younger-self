#!/usr/bin/env python3
"""Write the one-line entry to /output/entry.txt.

Entry for make.fun competition
"One Line to Your Younger Self" (u-boothlord-one-line-to-your-younger-self-22e97f76).
Stdlib only.
"""

import os

ENTRY = "Kid, one day a little girl will call you Dad and mean it \u2014 so be the man she already thinks you are."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
