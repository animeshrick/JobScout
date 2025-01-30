from users.auth_exceptions.user_exceptions import (
    UserNotVerifiedError,
    UserAuthenticationFailedError,
    UserNotFoundError,
)
from users.export_types.request_data_types.sign_in import SignInRequestType
from users.models.user_models.abstract_user import AbstractUser
from users.services.encryption_services.encryption_service import EncryptionServices
from users.services.token_services.token_generator import TokenGenerator


class User(AbstractUser):
    # friends = models.ManyToManyField("self", symmetrical=False, blank=True)
    # balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.role})"

    @staticmethod
    def authenticate_user(request_data: SignInRequestType) -> dict:
        if request_data.email and request_data.password:
            user_exists = (
                True
                if User.objects.filter(email=request_data.email).count() > 0
                else False
            )
            if user_exists:
                user = User.objects.get(email=request_data.email)
                if user:
                    if (
                        EncryptionServices().decrypt(user.password)
                        == request_data.password
                    ):
                        if user.is_active:
                            token = TokenGenerator().get_tokens_for_user(user)
                            return {
                                "token": token,
                                "errorMessage": None,
                            }
                        else:
                            raise UserNotVerifiedError()
                    else:
                        raise UserAuthenticationFailedError()
                else:
                    raise UserNotFoundError()
            else:
                raise UserNotFoundError()
        else:
            raise ValueError("Provided Email or Password is invalid.")
