import requests
from bs4 import BeautifulSoup
from pathlib import Path
import utils.config as config
from utils.problem import Problem
import jsonpickle
import json


def get_url(pid: str) -> str:
    contest, index = get_contest_index(pid)
    return f"https://codeforces.com/contest/{contest}/problem/{index}"


def get_contest_index(pid: str) -> tuple[int, str]:
    contest: str = ""
    index: str = ""
    for i in pid:
        if i.isdigit():
            contest += i
        else:
            index += i
    return int(contest), index.upper()


def get_name(url: str) -> str:
    soup: BeautifulSoup = BeautifulSoup(requests.get(url).text, 'html.parser')
    return soup.find('div', {'class': 'problem-statement'}).find('div', {'class': 'title'}).text


def get_pid(directory: Path) -> str:
    index: str = directory.name.upper()
    contest: str = directory.parent.name
    if not contest.isnumeric():
        raise ValueError(f"Invalid contest name: {contest}")
    return f"{contest}{index}"


def get_dir(pid: str) -> Path:
    contest, index = get_contest_index(pid)
    return Path(config.contest_path() / f"{contest}/{index}")


def load_problem(pid: str) -> Problem:
    with open(config.problem_path / f"{pid}.json", 'r') as f:
        return jsonpickle.decode(f.read())


def load_bookmarks() -> dict:
    try:
        with open(config.bookmarks_path, "r") as f:
            bookmarks: dict = json.load(f)
    except json.decoder.JSONDecodeError:
        with open(config.bookmarks_path, "w") as f:
            json.dump(dict(), f)
        bookmarks = {}
    return bookmarks


def write_bookmark(data: dict) -> None:
    with open(config.bookmarks_path, "w") as f:
        json.dump(data, f)
