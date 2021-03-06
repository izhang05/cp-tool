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
    os.system("g++ -std=c++17 main.cpp")
    os.system(f"./a.out < in1.txt > out.txt")
    os.system("diff out.txt out1.txt")
