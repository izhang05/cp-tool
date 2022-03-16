import utils.util as util
from utils.problem import Problem
import cf.parser
from colorama import Fore
import utils.config as config


def main() -> None:
    config.setup()
    try:
        pid, contest, index = util.arg_pid()
    except ValueError as e:
        print(Fore.RED + str(e))
        return
    print(f"{Fore.CYAN}Parsing Contest {contest}, Problem {index}")
    problem: Problem = Problem(pid)
    cf.parser.parse(problem)
    print(f"{Fore.GREEN}Saved to {problem.get_dir()}")
    problem.save()
