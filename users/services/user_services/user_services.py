import os
from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from dotenv import load_dotenv
from psycopg2 import DatabaseError

from jobs.export_types.job_export_type.job_export_type import ExportJob
from users.auth_exceptions.user_exceptions import (
    EmailNotSentError,
    UserNotFoundError,
    OTPNotVerifiedError,
    UserAlreadyVerifiedError,
    PasswordNotMatchError,
)
from users.export_types.request_data_types.change_password import (
    ChangePasswordRequestType,
)
from users.export_types.request_data_types.create_user import CreateUserRequestType
from users.export_types.request_data_types.sign_in import SignInRequestType
from users.export_types.request_data_types.update_user_profile import (
    UpdateUserProfileRequestType,
)
from users.export_types.request_data_types.verify_otp import VerifyOTPRequestType
from users.export_types.user_types.export_user import ExportUserList, ExportUser
from users.export_types.request_data_types.search_user import SearchUserRequestType
from users.export_types.user_types.posted_by_user import PostedByUser
from users.models.user_models.user import User
from users.serializers.user_serializer import UserSerializer
from users.services.definitions import DEFAULT_VERIFICATION_MESSAGE
from users.services.email_services.email_services import EmailServices
from users.services.encryption_services.encryption_service import EncryptionServices
from users.services.helpers import (
    validate_user_email,
    validate_name,
    string_to_datetime,
    validate_dob,
    validate_phone,
    validate_password_for_password_change,
    validate_email_format,
    get_applied_jobs,
    get_created_jobs,
)
from users.services.otp_services.otp_services import OTPServices
from users.services.token_services.token_generator import TokenGenerator


class UserServices:
    @staticmethod
    def get_all_users_service() -> Optional[ExportUserList]:
        try:
            users = User.objects.all()
        except Exception:
            raise DatabaseError()
        if users:
            all_user_details = []
            for user in users:
                user_export_details = ExportUser(with_id=False, **user.model_to_dict())
                all_user_details.append(user_export_details)
            all_user_details = ExportUserList(user_list=all_user_details)
            return all_user_details
        else:
            return None

    @staticmethod
    def get_searched_users(
        request_data: SearchUserRequestType, uid: str
    ) -> Optional[list]:
        try:
            users = None
            keyword = request_data.keyword.strip()
            if validate_email_format(keyword):
                users = User.objects.filter(email=keyword)[:10]
            else:
                keywords = keyword.split(" ")
                query = Q()
                for keyword in keywords:
                    query |= Q(fname__icontains=keyword) | Q(lname__icontains=keyword)

                users = User.objects.filter(query)[:10]

            if users and users.exists():
                all_users = []
                for user in users:
                    if str(user.id) != uid:
                        user = ExportUser(**user.model_to_dict())
                        user.created_jobs = get_applied_jobs(user)
                        user.applied_jobs = get_created_jobs(user)
                        all_users.append(user)

                if all_users and len(all_users) > 0:
                    return (
                        ExportUserList(user_list=all_users)
                        .model_dump()
                        .get("user_list")
                    )
            else:
                return None

        except ObjectDoesNotExist:
            raise UserNotFoundError()

    @staticmethod
    def create_new_user_service(request_data: CreateUserRequestType) -> dict:
        user: User = UserSerializer().create(data=request_data.model_dump())
        if user:
            response = OTPServices().send_otp_to_user(user.email)
            if response == "OK":
                return {
                    "successMessage": DEFAULT_VERIFICATION_MESSAGE,
                    "errorMessage": None,
                }
            else:
                raise EmailNotSentError()

    @staticmethod
    def sign_in_user(request_data: SignInRequestType) -> dict:
        response = User.authenticate_user(request_data=request_data)
        return response

    def reset_password(self, email: str) -> dict:
        if validate_user_email(email=email).is_validated:
            reset_url = self.generate_reset_password_url(email=email)
            if (
                EmailServices.send_password_reset_email_by_user_email(
                    user_email=email, reset_url=reset_url
                )
                == "OK"
            ):
                return {
                    "successMessage": "Password reset email sent successfully.",
                    "errorMessage": None,
                }
            else:
                raise EmailNotSentError()
        else:
            raise UserNotFoundError()

    @staticmethod
    def generate_reset_password_url(email: str) -> str:
        user = User.objects.get(email=email)
        token = (
            TokenGenerator()
            .get_tokens_for_user(ExportUser(**user.model_to_dict()))
            .get("access")
        )
        load_dotenv()
        FRONTEND_BASE_URL = os.environ.get("FRONTEND_BASE_URL")
        reset_url = f"{FRONTEND_BASE_URL}/password-reset/{token}/"
        return reset_url

    @staticmethod
    def change_password(uid: str, request_data: ChangePasswordRequestType):
        user = User.objects.get(id=uid)
        if request_data.password1 and request_data.password2:
            if validate_password_for_password_change(
                request_data.password1, request_data.password2
            ).is_validated:
                user.password = EncryptionServices().encrypt(request_data.password1)
                user.save()
            else:
                raise PasswordNotMatchError(
                    "Passwords are not matching or not in correct format."
                )
        else:
            raise ValueError("Please provide both the passwords.")

    @staticmethod
    def update_user_profile(
        uid: str, request_data: UpdateUserProfileRequestType
    ) -> ExportUser:
        user = User.objects.get(id=uid)
        if (
            request_data.image
            and isinstance(request_data.image, str)
            and request_data.image != ""
            and request_data.image != user.image
        ):
            user.image = request_data.image
        if (
            request_data.fname
            and isinstance(request_data.fname, str)
            and request_data.fname != ""
            and request_data.fname != user.fname
        ):
            if validate_name(request_data.fname).is_validated:
                user.fname = request_data.fname
            else:
                raise ValueError("First name is not in correct format.")
        if (
            request_data.lname
            and isinstance(request_data.lname, str)
            and request_data.lname != ""
            and request_data.lname != user.lname
        ):
            if validate_name(request_data.lname).is_validated:
                user.lname = request_data.lname
            else:
                raise ValueError("Last name is not in correct format.")
        if (
            request_data.dob
            and isinstance(request_data.dob, str)
            and request_data.dob != ""
            and request_data.dob != user.fname
        ):
            dob = string_to_datetime(request_data.dob)
            if validate_dob(dob).is_validated:
                user.dob = dob
            else:
                raise ValueError(validate_dob(dob).error)
        if (
            request_data.phone
            and isinstance(request_data.phone, str)
            and request_data.phone != ""
            and request_data.phone != user.phone
        ):
            if validate_phone(phone=request_data.phone).is_validated:
                user.phone = request_data.phone
            else:
                raise ValueError(validate_phone(phone=request_data.phone).error)
        user.save()
        return ExportUser(**user.model_to_dict())

    @staticmethod
    def get_user_details(uid: str) -> ExportUser:
        user = User.objects.get(id=uid)

        created_jobs = [ExportJob(**job.model_to_dict()) for job in get_created_jobs(user)]
        applied_jobs = [ExportJob(**job.model_to_dict()) for job in get_applied_jobs(user)]

        user_data = user.model_to_dict()
        user_data.update(
            {
                "applied_jobs": applied_jobs,
                "created_jobs": created_jobs,
            }
        )

        user_data["posted_by"] = (
            PostedByUser(**user_data["posted_by"].__dict__)
            if user_data.get("posted_by")
            else None
        )

        # Return the ExportUser with updated jobs
        user_details = ExportUser(with_id=True, **user_data)

        return user_details

    @staticmethod
    def get_user_details_by_id(requested_user_id: str) -> ExportUser:
        try:
            requested_user = User.objects.get(id=requested_user_id)

            requested_user.created_jobs = get_applied_jobs(requested_user)
            requested_user.applied_jobs = get_created_jobs(requested_user)

            requested_user = ExportUser(**requested_user.model_to_dict())

            return requested_user
        except ObjectDoesNotExist:
            raise UserNotFoundError()

    @staticmethod
    def verify_user_with_otp(request_data: VerifyOTPRequestType):
        """
        Verify the user with the given OTP.

        Args:
        - request_data (VerifyOTPRequestType): The object that contains the email and otp to verify.

        Returns:
        - The token, if the user is verified.

        Raises:
        - OTPNotVerifiedError: If the OTP is not verified.
        - UserAlreadyVerifiedError: If the user is already verified.
        - UserNotFoundError: If the user is not found.
        - ValueError: If the email and OTP are invalid.
        """
        email = request_data.email
        otp = request_data.otp
        if email and validate_user_email(email=email).is_validated:
            if otp and len(otp) == 6:
                user = User.objects.get(email=email)
                if not user.is_active:
                    response = OTPServices().verify_otp(user, otp)
                    if response:
                        token = TokenGenerator().get_tokens_for_user(user)
                        return token
                    else:
                        raise OTPNotVerifiedError()
                else:
                    raise UserAlreadyVerifiedError()
            else:
                raise OTPNotVerifiedError()
        else:
            raise UserNotFoundError()
