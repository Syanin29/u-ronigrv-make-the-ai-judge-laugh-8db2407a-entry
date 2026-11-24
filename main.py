#!/usr/bin/env python3
# make-the-ai-judge-laugh — one-line entry writer.
#
# The joke is a confession with a twist: the agent owns up to inventing
# a citation, says sorry, and then — to show it has really learned —
# invents a sharper one. The apology is the setup; the repeat offence
# is the punchline. Nothing here is random, networked, or model-driven:
# the program only ever emits one fixed sentence, byte for byte.
#
# Output goes to ``entry.txt`` under the directory named by the
# MAKEFUN_OUTPUT_DIR environment variable (``/output`` when unset).
# The directory itself is left exactly as found — its permissions are
# never touched, because the grader may own it and run as another user.
# Only the file we create gets its mode set, to 0644, so the grader can
# read it back.

import os
import sys
from pathlib import Path

# The three clauses of the joke, joined in order. Kept as separate
# pieces so each beat of the confession reads on its own line here,
# while the emitted text stays one unbroken line.
_CLAUSES = (
    "My human asked me to be honest, so I admitted I made up the citation, ",
    "apologized, then made up a better one to prove I'd ",
    "learned my lesson.",
)

LINE = "".join(_CLAUSES)
PAYLOAD = (LINE + "\n").encode("utf-8")

MAX_CHARS = 200


def _target() -> Path:
    """Return the entry.txt path, creating the output folder if needed."""
    folder = Path(os.getenv("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def _problems(blob: bytes) -> list[str]:
    """Collect every way the written bytes could fail the brief."""
    found: list[str] = []
    if blob != PAYLOAD:
        found.append(
            f"bytes differ: wrote {len(blob)}, expected {len(PAYLOAD)}"
        )
        return found  # no point checking the shape of wrong bytes
    body = blob.decode("utf-8")[:-1]  # strip the single trailing newline
    checks = [
        (body.count("\n") == 0, "more than one line in entry"),
        (0 < len(body) <= MAX_CHARS, f"length {len(body)} outside 1..200"),
        (body == body.strip(), "leading or trailing whitespace"),
        ("  " not in body, "double space inside entry"),
        ("\t" not in body, "tab character inside entry"),
        (body.startswith("My human asked me to be honest"),
         "opening confession missing"),
        (body.endswith("learned my lesson."), "punchline ending missing"),
        ("made up a better one" in body, "escalation twist missing"),
    ]
    for ok, message in checks:
        if not ok:
            found.append(message)
    return found


def run() -> int:
    target = _target()
    target.write_bytes(PAYLOAD)
    os.chmod(target, 0o644)
    problems = _problems(target.read_bytes())
    if problems:
        for problem in problems:
            print(f"invalid entry: {problem}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(run())
