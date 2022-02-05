import argparse
from utils.problem import Problem
from api import parser


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument('pid', metavar='P', type=str, nargs='*', help='problem ID')
    pid: str = "".join(p.parse_args().pid)
    if __name__ == "__main__":
        pid = "1586H"

    problem: Problem = Problem(pid)
    parser.parse(problem)
    return


if __name__ == '__main__':
    main()
