import utils.util as util
from utils.problem import Problem
from colorama import Fore


def main() -> None:
    try:
        pid, contest, index = util.arg_pid()
    except ValueError as e:
        print(Fore.RED + str(e))
        return
    try:
        problem: Problem = util.load_problem(pid)
    except FileNotFoundError:
        print(Fore.RED + f"Problem {pid} not found.")
        return
        # print(f"Enter y to parse and x to exit.{Fore.RESET}")
        # if input().lower() == "y":
        #     contest, index = util.get_contest_index(pid)
        #     print(f"{Fore.CYAN}Parsing Contest {contest}, Problem {index}")
        #     problem: Problem = Problem(pid)
        #     cf.parser.parse(problem)
        #     print(f"{Fore.GREEN}Saved to {problem.get_dir()}{Fore.RESET}")
        #     problem.save()
        # else:
        #     return
    problem.finish()
    problem.save()
    print(f"{Fore.GREEN}Finish Contest {contest}, Problem {index}")
