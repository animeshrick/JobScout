import logging

import django
from psycopg2 import DatabaseError
from pydantic import ValidationError
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError

from job_applications.job_application_exceptions.job_application_exceptions import (
    JobApplicationNotFoundError,
    AlreadyAppliedJobError,
    JobApplicationNotCreatedError,
)
from jobs.job_exceptions.job_exceptions import (
    JobNotCreatedError,
    AlreadyCreatedJobError,
    JobNotFoundError,
    JobPermissionError,
    JobAlreadyDeletedError,
)
from upload.upload_exceptions.upload_exceptions import WrongFileFormat, FileNotUploaded
from users.auth_exceptions.user_exceptions import (
    UserNotFoundError,
    UserAlreadyVerifiedError,
    UserNotVerifiedError,
    EmailNotSentError,
    OTPNotVerifiedError,
    UserAuthenticationFailedError,
    UserNotAuthenticatedError,
    PasswordNotMatchError,
)


class ExceptionHandler:
    @staticmethod
    def get_handlers() -> dict:
        return {
            DatabaseError: {
                "message": "DatabaseError: Error Occured While Fetching details from database",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            ValidationError: {
                "message": "PydanticValidationError: Error Occured while converting to Pydantic object",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            NotImplementedError: {
                "message": "NotImplementedError",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            UserNotFoundError: {
                "message": "UserNotFoundError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            UserAlreadyVerifiedError: {
                "message": "UserAlreadyVerifiedError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            UserNotVerifiedError: {
                "message": "UserNotVerifiedError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            EmailNotSentError: {
                "message": "EmailNotSentError",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            OTPNotVerifiedError: {
                "message": "OTPNotVerifiedError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            UserAuthenticationFailedError: {
                "message": "UserAuthenticationFailedError",
                "status": status.HTTP_401_UNAUTHORIZED,
            },
            UserNotAuthenticatedError: {
                "message": "UserNotAuthenticatedError",
                "status": status.HTTP_401_UNAUTHORIZED,
            },
            PasswordNotMatchError: {
                "message": "PasswordNotMatchError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            JobNotCreatedError: {
                "message": "JobNotCreatedError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            AlreadyCreatedJobError: {
                "message": "AlreadyCreatedJobError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            JobNotFoundError: {
                "message": "JobNotFoundError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            JobPermissionError: {
                "message": "JobNotFoundError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            JobAlreadyDeletedError: {
                "message": "JobAlreadyDeletedError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            JobApplicationNotCreatedError: {
                "message": "JobApplicationNotCreatedError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            AlreadyAppliedJobError: {
                "message": "AlreadyAppliedJobError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            JobApplicationNotFoundError: {
                "message": "JobApplicationNotFoundError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            WrongFileFormat: {
                "message": "WrongFileFormat",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            FileNotUploaded: {
                "message": "FileNotUploaded",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            ValueError: {
                "message": "ValueError",
                "status": status.HTTP_422_UNPROCESSABLE_ENTITY,
            },
            TokenError: {
                "message": "TokenError",
                "status": status.HTTP_401_UNAUTHORIZED,
            },
            serializers.ValidationError: {
                "message": "SerializerValidationError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            django.core.exceptions.ValidationError: {
                "message": "ValidationError",
                "status": status.HTTP_400_BAD_REQUEST,
            },
            ConnectionRefusedError: {
                "message": "ConnectionRefusedError",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            },
            # Exception: {
            #     "message": "InternalServerError",
            #     "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
            # },
        }

    def handle_exception(self, e: Exception):
        handlers = self.get_handlers()
        for exc_type, handler in handlers.items():
            if isinstance(e, exc_type):
                logging.error(
                    f"{handler['message']}: {e.msg}"
                    if hasattr(e, "msg")
                    else f"{handler['message']}: {str(e)}"
                )
                if isinstance(e, serializers.ValidationError):
                    e.msg = "; ".join([error for error in e.detail])
                return Response(
                    data={
                        "message": (
                            f"{handler['message']}: {e.msg}"
                            if hasattr(e, "msg")
                            else f"{handler['message']}: {str(e)}"
                        ),
                    },
                    status=handler["status"],
                    content_type="application/json",
                )
        else:
            logging.error(f"InternalServerError: {e}")
            raise e
