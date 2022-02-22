import argparse
import utils.util as util
from pathlib import Path
from colorama import Fore
from utils.problem import Problem
import cf.parser


def add_bookmark(add: str, bookmarks: dict) -> bool:
    if add in bookmarks:
        print(f"{Fore.RED}Bookmark \"{add}\" already exists.")
        return False
    else:
        bookmarks[add] = []
        util.write_bookmark(bookmarks)
        print(f"{Fore.GREEN}Bookmark \"{add}\" added.{Fore.RESET}")
    return True


def main() -> None:
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument("-a", "--add", type=str, help="Create bookmark type")
    p.add_argument("-p", "--pid", type=str, help='problem ID')
    p.add_argument('bookmark', metavar='B', type=str, nargs='?', help="Add bookmark to problem")

    if p.parse_args().add is not None:
        add_bookmark(p.parse_args().add, util.load_bookmarks())
        return

    if p.parse_args().pid is not None:
        pid: str = p.parse_args().pid.upper()
    else:
        try:
            pid = util.get_pid(Path.cwd())
        except ValueError as e:
            print(Fore.RED + str(e))
            return
    try:
        problem: Problem = util.load_problem(pid)
    except FileNotFoundError:
        print(Fore.RED + f"Problem {pid} not found.")
        print("Enter y to parse and x to exit.")
        if input().lower() == "y":
            contest, index = util.get_contest_index(pid)
            print(f"{Fore.CYAN}Parsing Contest {contest}, Problem {index}")
            problem: Problem = Problem(pid)
            cf.parser.parse(problem)
            print(f"{Fore.GREEN}Saved to {problem.get_dir()}{Fore.RESET}")
            problem.save()
        else:
            return
    bookmarks: dict = util.load_bookmarks()
    add: str = p.parse_args().bookmark
    if add not in bookmarks:
        print(f"{Fore.RED}Bookmark \"{add}\" does not exist.")
        print("Enter y to add and x to exit.")
        if input().lower() == "y":
            add_bookmark(add, bookmarks)
        else:
            return
    try:
        problem.add_bookmark(add)
    except ValueError as e:
        print(f"{Fore.RED}{e}")
        return
    problem.save()
    bookmarks[add].append(pid)
    util.write_bookmark(bookmarks)
    print(problem)
