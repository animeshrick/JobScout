from abc import ABC


class JobScoutBaseException(ABC, Exception):
    def __init__(self, msg: str):
        if msg:
            self.msg = msg
