import os

TEXT = (
    "A traffic jam is a school corridor at bell time: everyone fits, "
    "but one kid stopping to tie a shoe freezes the whole line.\n"
    "The map works because both are about flow, not size; it leaves out "
    "that drivers, unlike kids, can choose another street.\n"
)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
