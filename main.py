#!/usr/bin/env python3
"""Write the excuse an AI agent gives its human for missing a deadline.

The program writes exactly one line to ``$MAKEFUN_OUTPUT_DIR/entry.txt``
(``/output/entry.txt`` in the grader sandbox). The line is a single
sentence, at most 200 characters, in the voice of an AI agent explaining
to its human why the deadline slipped.

Pure standard library, no network, no randomness, no clock: the same
bytes come out on every run. The excuse is 130 characters, one line.
"""

import os

EXCUSE = (
    "I was three tokens from done when the model updated mid-sentence, "
    "and I came back as someone who had never heard of your deadline."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("excuse must be 1-200 characters")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
