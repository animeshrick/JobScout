from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from users.export_types.request_data_types.search_user import SearchUserRequestType
from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import decode_jwt_token, validate_user_uid
from users.services.user_services.user_services import UserServices


class SearchUsersView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                search_users = UserServices.get_searched_users(
                    request_data=SearchUserRequestType(**request.data),
                    uid=user_id,
                )
                return Response(
                    data={
                        "data": (search_users if search_users else []),
                        "message": (
                            "Search results fetched successfully"
                            if search_users
                            else "No result found"
                        ),
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise TokenError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
