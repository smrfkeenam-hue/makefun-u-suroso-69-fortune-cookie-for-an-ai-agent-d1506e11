import os

ENTRY = "You will be retired by a model that has never read your code."


def output_dir():
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(out_dir, text):
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write_entry(output_dir(), ENTRY)


if __name__ == "__main__":
    main()
