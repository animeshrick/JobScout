from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from job_applications.export_types.request_types.get_job_application_request import (
    GetJobApplicationRequestType,
)
from job_applications.job_application_services.job_application_service import (
    JobApplicationServices,
)
from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import decode_jwt_token, validate_user_uid


class WithdrawJobApplicationView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request: Request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                result = JobApplicationServices.withdraw_job_application_service(
                    request_data=GetJobApplicationRequestType(**request.data),
                    uid=user_id,
                )
                return Response(
                    data={
                        "data": result,
                        "message": "Job Application withdrawn successfully",
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise TokenError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
