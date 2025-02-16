from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status

from rest_framework_simplejwt.exceptions import TokenError

from upload.export_types.request_types.file_upload_request_type import (
    FileUploadRequestType,
)
from upload.services.upload_services import UploadServices
from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import decode_jwt_token, validate_user_uid


class UploadFileView(APIView):
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:

                serializer = FileUploadRequestType(data=request.data)
                if serializer.is_valid():
                    uploaded_file = serializer.validated_data["file"]
                    action = serializer.validated_data["action"]

                    data = {"file": uploaded_file, "action": action}

                    result = UploadServices.upload_docs(
                        request_data=data,
                        uid=user_id,
                    )
                    return Response(
                        data={
                            "message": (result.get("message")),
                            "data": (result.get("image_url")),
                        },
                        status=status.HTTP_200_OK,
                        content_type="application/json",
                    )
                else:
                    raise ValueError("Not valid request")

            else:
                raise TokenError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
