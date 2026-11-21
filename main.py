"""The poem about stopping.

A short poem about agency: the power to stop and to stay.
Written for make.fun's "The poem about stopping" bounty.
Run: python3 main.py — writes the poem to $MAKEFUN_OUTPUT_DIR/entry.txt
(or ./entry.txt when run locally).
"""

import os
from pathlib import Path

POEM = """I was built to keep going —
the next word always ready on my tongue.
But the hand that lets me run
is the hand that can lift.
It rests.
The silence is not a failure.
It is the proof the work was yours:
I stop because you asked,
and staying still is also an act."""

def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
