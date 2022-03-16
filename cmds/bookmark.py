import argparse
import utils.util as util
from pathlib import Path
from colorama import Fore
from utils.problem import Problem
from utils import config
import cf.parser


def add_bookmark(add: str, bookmarks: dict) -> bool:
    if add in bookmarks:
        print(f"{Fore.RED}Bookmark \"{add}\" already exists.{Fore.RESET}")
        return False
    else:
        bookmarks[add] = []
        util.write_bookmark(bookmarks)
        print(f"{Fore.GREEN}Bookmark \"{add}\" added.{Fore.RESET}")
    return True


def main() -> None:
    config.setup()
    p: argparse.ArgumentParser = argparse.ArgumentParser()
    p.add_argument("-a", "--add", action="store_true", help="Create bookmark type")
    p.add_argument("-l", "--list", action="store_true", help="List all bookmarks")
    p.add_argument("-p", "--pid", type=str, help='problem ID')
    p.add_argument('bookmark', metavar='B', type=str, nargs='?', help="Add bookmark to problem")

    args = p.parse_args()

    if args.list:
        bookmarks: dict = util.load_bookmarks()
        if args.bookmark is not None:
            print(f"{args.bookmark}: {bookmarks[args.bookmark]}")
        else:
            print(bookmarks)
        return

    if args.add:
        if args.bookmark is not None:
            add_bookmark(args.bookmark, util.load_bookmarks())
        return

    if args.pid is not None:
        pid: str = args.pid.upper()
    else:
        try:
            pid = util.get_pid(Path.cwd())
        except ValueError as e:
            print(Fore.RED + str(e) + Fore.RESET)
            return
    try:
        problem: Problem = util.load_problem(pid)
    except FileNotFoundError:
        print(Fore.RED + f"Problem {pid} not found.")
        print(f"Enter y to parse and x to exit.{Fore.RESET}")
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
    add: str = args.bookmark
    if add not in bookmarks:
        print(f"{Fore.RED}Bookmark \"{add}\" does not exist.")
        print(f"Enter y to create and x to exit.{Fore.RESET}")
        if input().lower() == "y":
            add_bookmark(add, bookmarks)
        else:
            return
    try:
        problem.add_bookmark(add)
    except ValueError as e:
        print(f"{Fore.RED}{e}{Fore.RESET}")
        return
    problem.save()
    bookmarks[add].append(pid)
    util.write_bookmark(bookmarks)
    print(problem)
