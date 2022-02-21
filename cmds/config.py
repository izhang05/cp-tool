import utils.config as config


def main() -> None:
    config.create_dir()
    data = {"folder": {}}
    for i in {"root", "contest", "gym"}:
        print(f"Enter {i} path")
        data["folder"][i] = input()
    config.set_config(data)
