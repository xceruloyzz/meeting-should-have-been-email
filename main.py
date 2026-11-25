#!/usr/bin/env python3
"""Entry for make.fun: The Meeting That Should Have Been an Email.

Writes a single one-line joke (135 characters) to /output/entry.txt.
Writes directly to the final file: no temp files, no trailing newline.
Revision: tightened the docstring; the entry text is unchanged.
"""

import os

ENTRY = (
    "We held a meeting to decide whether the meeting could have been an email, "
    "and the answer is in the meeting notes nobody will ever read."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
