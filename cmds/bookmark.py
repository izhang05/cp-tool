import argparse
import utils.util as util
from utils.problem import Problem
import cf.parser


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument('pid', metavar='P', type=str, nargs='*', help='problem ID')
    pid: str
    if p.parse_args().pid is not None:
        pid = "".join(p.parse_args().pid)
    else:
        pid = "hi"
        pass
        # pid =
    contest, index = util.get_contest_index(pid)


if __name__ == '__main__':
    main()
