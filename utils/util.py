import requests
from bs4 import BeautifulSoup
from pathlib import Path


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


def get_pid(dir: Path) -> str:
    index: str = dir.name.upper()
    contest: str = dir.parent.name
    if not contest.isnumeric():
        raise ValueError(f"Invalid contest name: {contest}")
    return f"{contest}{index}"