import yaml

CONFIG = "pilots/sandbox/config/sandbox.yaml"


def load_config():
    with open(CONFIG, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def provision():
    cfg = load_config()
    print(cfg)


if __name__ == "__main__":
    provision()
