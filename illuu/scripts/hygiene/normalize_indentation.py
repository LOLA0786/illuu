import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def normalize_file(path: str) -> bool:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()
    changed = False
    new_lines = []
    for line in lines:
        # Replace leading tabs with 4 spaces each
        if line.startswith("\t"):
            leading_tabs = len(re.match(r"^\t+", line).group(0))
            line = "    " * leading_tabs + line.lstrip("\t")
            changed = True
        new_lines.append(line)
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    return changed


def run():
    for root, _, files in os.walk(ROOT):
        for name in files:
            if name.endswith(".py"):
                normalize_file(os.path.join(root, name))


if __name__ == "__main__":
    run()
