from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import decode_jwt_token, validate_user_uid


class UploadFileView(APIView):
    renderer_classes = [JSONRenderer]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request: Request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                file = request.FILES.get("file")
                job_id = request.data.get("job_id")

                if not file:
                    return Response(
                        {"error": "No file provided"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                if not job_id:
                    return Response(
                        {"error": "No job_id provided"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                result = {}
                # result = JobServices.upload_file_service(file, job_id, user_id)

                return Response(
                    data={
                        "message": result.get("message"),
                        "file_url": result.get("file_url"),
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise TokenError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
