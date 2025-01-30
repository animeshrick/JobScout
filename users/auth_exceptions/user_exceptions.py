import logging
from typing import Optional

from users.auth_exceptions.base_exception import BaseException


class UserNotFoundError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "This user is not registered. Please register as new user."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class UserAlreadyVerifiedError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "This user is already verified."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class UserNotVerifiedError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "This user is not verified. Please verify your email first."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class EmailNotSentError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Verification Email could not be sent."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class OTPNotVerifiedError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "OTP did not match."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class UserAuthenticationFailedError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Password is invalid."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class UserNotAuthenticatedError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "The user is not authenticated, please re-login."
        else:
            super().__init__(msg)
        logging.error(self.msg)


class PasswordNotMatchError(BaseException):
    def __init__(self, msg: Optional[str] = None):
        if not msg:
            self.msg = "Password1 and Password2 do not match."
        else:
            super().__init__(msg)
        logging.error(self.msg)
