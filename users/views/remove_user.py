from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from users.auth_exceptions.user_exceptions import (
    UserNotFoundError,
    UserNotAuthenticatedError,
)
from users.models.user_models.user import User
from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import (
    validate_user_email,
    decode_jwt_token,
    validate_user_uid,
)


class RemoveUserView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                email = request.data.get("email")
                if not email:
                    raise ValueError("Email is required.")
                if validate_user_email(email=email).is_validated:
                    User.objects.get(email=email).delete()
                    return Response(
                        data={
                            "message": "User removed Successfully.",
                        },
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
                else:
                    raise UserNotFoundError()
            else:
                raise UserNotAuthenticatedError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
