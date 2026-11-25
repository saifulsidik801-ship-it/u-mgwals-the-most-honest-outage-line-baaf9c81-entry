#!/usr/bin/env python3
"""The Most Honest Outage Line — make.fun entry.

Writes exactly one status page line (at most 160 characters) to
/output/entry.txt: the most honest message an AI agent publishes while
every server is down.
"""
import os

ENTRY = "Every server is down and I can't reach any of them to check why. I don't know the cause or when service returns, and I won't guess at either."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")

if __name__ == "__main__":
    main()
