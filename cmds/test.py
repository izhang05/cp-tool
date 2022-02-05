import subprocess


def main() -> None:
    s = subprocess.run(["ls"])
    # print(s)

if __name__ == "__main__":
    main()
