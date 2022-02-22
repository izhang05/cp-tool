from datetime import datetime
import utils.util as util
from pathlib import Path
import utils.config as config
import jsonpickle


class Problem:
    def __init__(self, pid: str, name: str = None, url: str = None, solved: bool = False, started: datetime = None,
                 finished: datetime = None, bookmarks: list[str] = [], tags: list[str] = []):
        self.pid: str = pid
        self.url: str = url
        self.name: str = name
        if url is None:
            self.url = util.get_url(pid)
        if name is None:
            self.name = util.get_name(self.url)
        self.solved: bool = solved
        self.started: datetime = started
        if started is None:
            self.started = datetime.now()
        self.finished: datetime = finished
        self.bookmarks: list[str] = bookmarks
        self.tags: list[str] = tags

    def __repr__(self) -> str:
        return f"{self.pid} - {self.name} - {self.url}\n" \
               f"solved: {self.solved}\n" \
               f"started: {self.started}\n" \
               f"finished: {self.finished}\n" \
               f"bookmarks: {self.bookmarks}\n" \
               f"tags: {self.tags}"

    def save(self) -> None:
        with open(config.problem_path / f"{self.pid}.json", 'w') as f:
            f.write(jsonpickle.encode(self))

    def get_dir(self, create=True) -> Path:
        directory = util.get_dir(self.pid)
        if create:
            directory.mkdir(parents=True, exist_ok=True)
        return directory

    def add_bookmark(self, bookmark: str) -> None:
        if bookmark in self.bookmarks:
            raise ValueError(f"Bookmark \"{bookmark}\" already exists")
        self.bookmarks.append(bookmark)
