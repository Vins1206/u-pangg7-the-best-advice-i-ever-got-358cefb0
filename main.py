"""Best Advice I Ever Got — single-sentence entry writer (Python stdlib only)."""

ENTRY = "My dad told me to answer every call like it could be the last one, because one day it was, and his name never lit up my screen again."


def main():
    from pathlib import Path

    # Gate: one sentence, plain text, 1-200 characters, no trailing newline.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip() == ENTRY, "entry must not start or end with whitespace"
    assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
