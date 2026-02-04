import os
import py_compile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def run():
    errors = []
    for root, _, files in os.walk(ROOT):
        for name in files:
            if name.endswith(".py"):
                path = os.path.join(root, name)
                try:
                    py_compile.compile(path, doraise=True)
                except Exception as exc:
                    errors.append((path, str(exc)))
    if errors:
        for path, err in errors:
            print(f"{path}: {err}")
        raise SystemExit(1)


if __name__ == "__main__":
    run()
