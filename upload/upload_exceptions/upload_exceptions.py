import logging
from typing import Optional

from users.auth_exceptions.base_exception import JobScoutBaseException


class FileNotUploaded(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Opps! You can't upload the file."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class WrongFileFormat(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Opps! You can't upload the file."
        else:
            super().__init__(msg)
        logging.error(self.msg)
