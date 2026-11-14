import sys
from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

JOKE = (
    "My AI coding agent fixed a bug so thoroughly that the app now has "
    "zero errors, zero features, and a tiny memorial plaque where the "
    "functionality used to be."
)


def main() -> int:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
