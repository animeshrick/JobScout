from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from users.export_types.request_data_types.update_user_profile import (
    UpdateUserProfileRequestType,
)
from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import decode_jwt_token, validate_user_uid
from users.services.user_services.user_services import UserServices


class UpdateProfileView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                user = UserServices().update_user_profile(
                    uid=user_id,
                    request_data=UpdateUserProfileRequestType(**request.data),
                )
                return Response(
                    data={
                        "message": "User details updated Successfully.",
                        "data": user.model_dump(),
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise TokenError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
