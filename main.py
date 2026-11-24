#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing home Wi-Fi to entry.txt.

The word is "Gaslighting": the Wi-Fi insists it is connected, shows
full bars, and loads absolutely nothing — it makes you doubt your own
connection while pretending everything is fine.
"""

import os
from pathlib import Path

WORD = "Gaslighting"

# Gate: entry.txt must hold 1-200 characters of UTF-8 text.
CHAR_LIMIT = 200


def main() -> None:
    if "\r" in WORD:
        raise ValueError("word must not contain a carriage return")
    if not 1 <= len(WORD) <= CHAR_LIMIT:
        raise ValueError("word must be 1-%d characters" % CHAR_LIMIT)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
