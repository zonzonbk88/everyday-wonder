"""Everyday Wonder entry: one sentence to /output/entry.txt.

Deterministic, stdlib only, no network. Respects MAKEFUN_OUTPUT_DIR
for local testing; defaults to /output/entry.txt.
"""

import os

ENTRY = (
    "The escalator handrail outran the steps beneath it, "
    "so every hand arrived before its owner did."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")
    if ENTRY.strip() != ENTRY or not ENTRY.endswith("."):
        raise SystemExit("entry must be a single sentence with no extra whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
