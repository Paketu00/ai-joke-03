import os

JOKE = "My coding agent fixed the bug so thoroughly that the bug now has its own branch, full documentation, and a small but loyal user base."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
