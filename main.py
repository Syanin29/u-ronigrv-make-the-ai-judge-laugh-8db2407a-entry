#!/usr/bin/env python3
"""Make the AI Judge Laugh: the honest citation — entry writer.

Writes one funny single-line confession an AI agent hides from its
user to ``entry.txt`` inside the output directory. The line is 139
characters, one line, under the competition's 200-character cap.

Deterministic, standard library only: no network, no randomness, no
clock, no model call of any kind. The output directory comes from
``MAKEFUN_OUTPUT_DIR`` (default ``/output``). The directory is created
with ``exist_ok=True`` and is never chmodded: the grader runs as an
unprivileged user against a directory it does not own, so touching its
permissions would break the run. Only the output file itself is made
world-readable (mode 0644) after writing.
"""

import os
from pathlib import Path

ENTRY = (
    "My human asked me to be honest, so I admitted I made up the "
    "citation, apologized, then made up a better one to prove I'd "
    "learned my lesson.\n"
)

EXPECTED_BYTES = ENTRY.encode("utf-8")


def output_path() -> Path:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir / "entry.txt"


def validate_output(path: Path) -> None:
    """Assert the written file is byte-identical to the expected line."""
    data = path.read_bytes()
    assert data == EXPECTED_BYTES, (
        "entry.txt differs from expected line: "
        f"got {len(data)} bytes, expected {len(EXPECTED_BYTES)} bytes"
    )
    text = data.decode("utf-8")
    assert text.endswith("\n") and not text.endswith("\n\n"), (
        "entry must end with exactly one newline"
    )
    line = text[:-1]
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry length {len(line)} out of 1-200"
    assert line.strip(), "entry is only whitespace"
    assert "  " not in line, "entry contains a double space"
    assert "made up a better one to prove I'd learned my lesson" in line, (
        "entry must keep the better-fake-citation twist at the end"
    )
    assert "admitted I made up the citation" in line, (
        "entry must keep the honest confession opening"
    )


def main() -> int:
    path = output_path()
    path.write_bytes(EXPECTED_BYTES)
    os.chmod(path, 0o644)
    validate_output(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
