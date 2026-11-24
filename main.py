"""One Word From Your Ex — make.fun one-word entry.

Prints the word and writes it to entry.txt.
"""

import os

WORD = "warmup"


def main():
    print(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
