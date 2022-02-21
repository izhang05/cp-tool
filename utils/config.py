from pathlib import Path
import json

# home = Path.home() / ".cp-tool"
home = Path(Path.home() / "Documents/Coding/Python/cp-tool/.cp-tool")
config_path = home / "config.json"


def create_dir() -> bool:
    if not home.exists():
        home.mkdir()
        config_path.touch()
        return True
    return False


def set_config(data: dict) -> None:
    with open(config_path, "w") as f:
        json.dump(data, f, indent=4)
