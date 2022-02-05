import argparse
from utils.problem import Problem
import cf


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument('pid', metavar='P', type=str, nargs='*', help='problem ID')
    pid: str = "".join(p.parse_args().pid)
    if __name__ == "__main__":
        pid = "1586H"

    problem: Problem = Problem(pid)
    cf.parser.parse(problem)


if __name__ == '__main__':
    main()
