from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from jobs.job_services.job_services import JobServices
from users.services.handlers.exception_handlers import ExceptionHandler


class AllJobsView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, _):
        try:
            all_job: list = JobServices.get_all_jobs_service()
            return Response(
                data={
                    "data": all_job if all_job is not None else [],
                    "message": "All jobs fetched successfully",
                },
                status=status.HTTP_200_OK,
                content_type="application/json",
            )
        except Exception as e:
            return ExceptionHandler().handle_exception(e)
