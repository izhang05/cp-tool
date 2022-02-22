import argparse
import utils.util as util
import utils.config as config
from utils.problem import Problem
import cf.parser
import jsonpickle
from pathlib import Path


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument('pid', metavar='P', type=str, nargs='*', help='problem ID')
    pid: str
    if p.parse_args().pid:
        pid = "".join(p.parse_args().pid).upper()
    else:
        pid = util.get_pid(Path.cwd())
    contest, index = util.get_contest_index(pid)
    print(f"Parse Contest {contest}, Problem {index}")
    problem: Problem = Problem(pid)
    cf.parser.parse(problem)
    with open(config.problem_path / f"{pid}.json", 'w') as f:
        f.write(jsonpickle.encode(problem))


if __name__ == '__main__':
    main()
