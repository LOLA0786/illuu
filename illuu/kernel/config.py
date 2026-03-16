import yaml
from pathlib import Path

DEFAULT_CONFIG = "illuu.yaml"

def load_config(path=None):
    config_file = Path(path or DEFAULT_CONFIG)

    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found: {config_file}")

    with open(config_file) as f:
        return yaml.safe_load(f)
