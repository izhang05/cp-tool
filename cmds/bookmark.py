import argparse
import utils.util as util
from pathlib import Path
from colorama import Fore
from utils.problem import Problem
import utils.config as config
import jsonpickle


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument("-p", "--pid", type=str, help='problem ID')
    p.add_argument('bookmark', metavar='B', type=str, nargs='*', help='bookmark')

    pid: str
    if p.parse_args().pid is not None:
        pid = p.parse_args().pid.upper()
    else:
        try:
            pid = util.get_pid(Path.cwd())
        except ValueError as e:
            print(Fore.RED + str(e))
            return
    problem: Problem
    with open(config.problem_path / f"{pid}.json", 'r') as f:
        problem = jsonpickle.decode(f.read())
    print(problem)
