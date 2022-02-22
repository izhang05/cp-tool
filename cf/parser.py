from utils.problem import Problem
import requests
from bs4 import BeautifulSoup


def parse(problem: Problem) -> None:
    soup: BeautifulSoup = BeautifulSoup(requests.get(problem.url).text, 'html.parser')
    statement = soup.find('div', {'class': 'problem-statement'})
    cnt: int = 1

    directory = problem.get_dir()
    for i in statement.find_all('div', {'class': 'input'}):
        with open(directory / f"in{cnt}.txt", "w") as f:
            cur = i.get_text(separator="\n")
            f.write(cur[cur.find("\n") + 1:].strip() + "\n")
        cnt += 1
    cnt = 1
    for i in statement.find_all('div', {'class': 'output'}):
        with open(directory / f"out{cnt}.txt", "w") as f:
            cur = i.get_text(separator="\n")
            f.write(cur[cur.find("\n") + 1:].strip() + "\n")
        cnt += 1
