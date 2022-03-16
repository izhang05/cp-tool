import utils.util as util
from utils.problem import Problem
from colorama import Fore
import os


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
    print(problem)
