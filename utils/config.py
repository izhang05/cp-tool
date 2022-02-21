from pathlib import Path
import json
import subprocess

# home = Path.home() / ".cp-tool"
home = Path(Path.home() / "Documents/Coding/Python/cp-tool/.cp-tool")
config_path = home / "config.json"


def create_dir() -> bool:
    home.cwd()
    (home / "a.cpp").touch()
    # subprocess.run(["pycharm", (home / "a.cpp")])
    return True
    # if not home.exists():
    #     home.mkdir()
    #     config_path.touch()
    #     return True
    # return False


def set_config() -> None:
    data = {"root": "cf", "contest": "contest"}
    with open(config_path, "w") as f:
        json.dump(data, f)
