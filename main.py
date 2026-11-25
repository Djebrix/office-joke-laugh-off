"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to /output/entry.txt
(or $OUTPUT_DIR/entry.txt when set, for local testing).
Stdlib only, fully deterministic: the same constant line every run.
The joke lands on the office in-joke that "Exit Interview" sounds like a way out.
"""

import os

# The punchline: the "Exit Interview" door is the only exit a new hire
# is ever shown, so the intern takes the sign literally.
LINE = "The intern asked where the fire exit was, so we pointed at the door marked 'Exit Interview'."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
