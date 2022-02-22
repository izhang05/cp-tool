from datetime import datetime
from utils.util import get_url, get_name


class Problem:
    def __init__(self, pid: str, name: str = None, url: str = None, solved: bool = False, started: datetime = None,
                 finished: datetime = None, bookmarks: list[str] = None, tags: list[str] = None):
        self.pid: str = pid
        self.url: str = url
        self.name: str = name
        if url is None:
            self.url = get_url(pid)
        if name is None:
            self.name = get_name(self.url)
        self.solved: bool = solved
        self.started: datetime = started
        if started is None:
            self.started = datetime.now()
        self.finished: datetime = finished
        self.bookmarks: list[str] = bookmarks
        self.tags: list[str] = tags
