from datetime import datetime
import utils.util as util
from pathlib import Path


class Problem:
    def __init__(self, pid: str, name: str = None, url: str = None, solved: bool = False, started: datetime = None,
                 finished: datetime = None, bookmarks: list[str] = None, tags: list[str] = None):
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

    def get_dir(self, create=True) -> Path:
        directory = util.get_dir(self.pid)
        if create:
            directory.mkdir(parents=True, exist_ok=True)
        return directory
