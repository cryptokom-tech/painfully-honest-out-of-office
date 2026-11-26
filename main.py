"""Painfully honest out-of-office entry for make.fun bounty."""

import os
from pathlib import Path

ENTRY = "Thank you for writing; I am out of the office until Monday and not checking email, because last holiday I answered one message and inherited twelve."


def main() -> None:
    assert ENTRY == ENTRY.strip(), "entry has surrounding whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry length out of range"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    data = target.read_bytes()
    expected = ENTRY.encode("utf-8")
    assert len(data) == len(expected), "byte count mismatch"
    assert data == expected, "read-back content mismatch"
    assert data.decode("utf-8") == ENTRY, "read-back text mismatch"


if __name__ == "__main__":
    main()
