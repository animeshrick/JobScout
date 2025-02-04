from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from jobs.export_types.job_export_type.job_export_type import ExportJob
from jobs.export_types.request_type.get_job_request_type import GetJobRequestType
from jobs.job_services.job_services import JobServices
from users.services.handlers.exception_handlers import ExceptionHandler


class GetJobByIDView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request: Request):
        try:
            job_id = request.data.get("job_id")
            if isinstance(job_id, str) and job_id:
                job: ExportJob = JobServices.get_jobs_by_id(
                    request_data=GetJobRequestType(**request.data)
                )
                return Response(
                    data={
                        "data": job.model_dump(),
                        "message": "Job fetched successfully",
                    },
                    status=status.HTTP_200_OK,
                    content_type="application/json",
                )
            else:
                raise ValueError("Job ID is required")
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
