import logging
from typing import Optional

from users.auth_exceptions.base_exception import JobScoutBaseException


class JobNotCreatedError(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Opps! Job can't create."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class AlreadyCreatedJobError(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "You are already created this job."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class JobNotFoundError(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "The job you are looking for is not found."
        else:
            super().__init__(msg)
        logging.error(self.msg)
