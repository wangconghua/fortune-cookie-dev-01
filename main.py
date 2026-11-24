#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers (make.fun entry).

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. The gate requires UTF-8 text of 1-120 characters,
not only white space.
"""

import os

# The line: a balanced fortune-cookie sentence. "Interest" does double
# duty — a production bug costs interest (like a debt) and holds your
# attention. One line, no trailing newline, so the file is exactly the line.
LINE = "A bug found in review is a gift; a bug found in production is a lesson with interest."


def main():
    line = LINE.strip()
    # Gate check: 1-120 characters, not only white space, single line.
    assert 1 <= len(line) <= 120, f"line is {len(line)} chars, must be 1-120"
    assert line.strip(), "line must not be only white space"
    assert "\n" not in line, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(f"{line} ({len(line)} chars)")


if __name__ == "__main__":
    main()
