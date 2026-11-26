import os

TEXT = (
    "Rain is the sky doing dishes: clouds are the full sink, "
    "thunder is a dropped pan, and puddles are what splashed over the side.\n"
    "The map works because both turn stored-up water into a mess below; "
    "it leaves out that nobody has to dry the sky afterwards.\n"
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
