import argparse
import utils.util as util
import utils.config as config
from utils.problem import Problem
import cf.parser
import jsonpickle
from pathlib import Path
from colorama import Fore


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument('pid', metavar='P', type=str, nargs='*', help='problem ID')
    pid: str
    if p.parse_args().pid:
        pid = "".join(p.parse_args().pid).upper()
    else:
        try:
            pid = util.get_pid(Path.cwd())
        except ValueError as e:
            print(Fore.RED + str(e))
            return
    contest, index = util.get_contest_index(pid)
    print(f"{Fore.CYAN}Parsing Contest {contest}, Problem {index}")
    problem: Problem = Problem(pid)
    cf.parser.parse(problem)
    print(f"{Fore.GREEN}Saved to {problem.get_dir()}")
    with open(config.problem_path / f"{pid}.json", 'w') as f:
        f.write(jsonpickle.encode(problem))


if __name__ == '__main__':
    main()
