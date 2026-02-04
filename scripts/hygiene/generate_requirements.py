import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

EXCLUDE_DIRS = {".venv", ".git", "vault/legacy"}


def is_excluded(path: Path) -> bool:
    for part in path.parts:
        if part in {".venv", ".git"}:
            return True
    return "vault/legacy" in str(path)


DEV_ONLY = {"pytest", "pytest-asyncio", "pytest-cov", "pytest-timeout", "locust"}


def collect() -> list[str]:
    reqs = set()
    for path in ROOT.rglob("requirements*.txt"):
        if path.name in {"requirements.txt", "requirements-dev.txt"}:
            continue
        if is_excluded(path):
            continue
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                # Drop inline comments to normalize duplicates
                if " #" in line:
                    line = line.split(" #", 1)[0].rstrip()
                name = line.split("==", 1)[0].strip()
                if name in DEV_ONLY:
                    continue
                reqs.add(line)
        except Exception:
            continue
    return sorted(reqs)


def write(path: Path, lines: list[str]) -> None:
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    requirements = collect()
    write(ROOT / "requirements.txt", requirements)


if __name__ == "__main__":
    main()
