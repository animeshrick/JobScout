from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from jobs.export_types.job_export_type.job_export_type import ExportJob
from jobs.export_types.request_type.get_job_request_type import GetJobRequestType
from jobs.job_services.job_services import JobServices
from users.services.handlers.exception_handlers import ExceptionHandler
from users.services.helpers import decode_jwt_token, validate_user_uid


class RemoveJobView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request: Request):
        try:
            user_id = decode_jwt_token(request=request)
            if validate_user_uid(uid=user_id).is_validated:
                job: ExportJob = JobServices.remove_job_service(
                    request_data=GetJobRequestType(**request.data),
                    uid=user_id,
                )
                return Response(
                    data={
                        "data": job.model_dump(),
                        "message": "Job removed successfully",
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise TokenError()
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
