#!/usr/bin/env python3
"""Fortune Cookies for Machines — write one fortune an AI agent would get.

Reads entry.txt next to this file, validates the gate (UTF-8, 1-200
characters, single line, not only whitespace) and writes it to
/output/entry.txt with mode 0644.
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
        text = f.read()

    # Gate: one line, 1-200 characters, not only whitespace.
    lines = text.splitlines()
    if len(lines) != 1:
        print("entry must be exactly one line", file=sys.stderr)
        return 1
    line = lines[0]
    if not (1 <= len(line) <= 200):
        print("entry must be 1-200 characters", file=sys.stderr)
        return 1
    if not line.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if any(ord(c) < 0x20 and c not in "\t" for c in line):
        print("entry must not contain control characters", file=sys.stderr)
        return 1

    os.makedirs("/output", exist_ok=True)
    out = "/output/entry.txt"
    with open(out, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(out, 0o644)
    print(f"wrote {len(line)} characters to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
