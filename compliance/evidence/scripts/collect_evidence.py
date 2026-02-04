import hashlib
import json
import os
import uuid
from datetime import datetime

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CONFIG = os.path.join(ROOT, "config", "controls.yaml")
OUTPUT = os.path.join(ROOT, "output")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def load_controls() -> dict:
    with open(CONFIG, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def collect():
    cfg = load_controls()
    bundle_id = str(uuid.uuid4())
    generated_at = datetime.utcnow().isoformat() + "Z"

    os.makedirs(OUTPUT, exist_ok=True)

    controls_out = []
    for control in cfg.get("controls", []):
        artifacts = []
        for ev in control.get("evidence", []):
            path = ev.get("path")
            if not path:
                continue
            full_path = path
            if not os.path.isabs(path):
                full_path = os.path.abspath(os.path.join(os.path.dirname(ROOT), path))
            if not os.path.exists(full_path):
                continue
            artifacts.append(
                {
                    "type": ev.get("type", "unknown"),
                    "path": path,
                    "sha256": sha256_file(full_path),
                }
            )
        controls_out.append({"control_id": control.get("id"), "artifacts": artifacts})

    bundle = {
        "bundle_id": bundle_id,
        "generated_at": generated_at,
        "controls": controls_out,
    }

    out_path = os.path.join(OUTPUT, f"bundle-{bundle_id}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(bundle, f, indent=2)

    print(out_path)


if __name__ == "__main__":
    collect()
