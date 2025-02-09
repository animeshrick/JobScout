import logging
from typing import Optional

from users.auth_exceptions.base_exception import JobScoutBaseException


class JobApplicationNotCreatedError(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Opps! You cant apply for the job."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class AlreadyAppliedJobError(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "You are already applied for this job."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class JobApplicationNotFoundError(JobScoutBaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Job application not found or deleted"
        else:
            super().__init__(msg)
        logging.error(self.msg)
