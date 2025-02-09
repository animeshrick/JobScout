from job_applications.export_types.export_types.job_application_export_type import (
    ExportJobApplication,
)
from job_applications.export_types.request_types.add_job_application_request import (
    AddJobApplicationRequestType,
)
from job_applications.export_types.request_types.get_job_application_request import (
    GetJobApplicationRequestType,
)
from job_applications.job_application_exceptions.job_application_exceptions import (
    JobApplicationNotCreatedError,
)
from job_applications.models.job_application_model import JobApplication
from job_applications.serializers.job_application_serializer import (
    JobApplicationSerializer,
)


class JobApplicationServices:
    @staticmethod
    def add_job_application_service(
        request_data: AddJobApplicationRequestType, uid: str
    ) -> dict:
        data = {
            "request_data": request_data.model_dump(),
            "uid": uid,
        }
        job_application: JobApplication = JobApplicationSerializer().create(data=data)
        if job_application:
            return {"message": "You have applied to this job successfully."}
        else:
            raise JobApplicationNotCreatedError()

    @staticmethod
    def get_job_application_service(
        request_data: GetJobApplicationRequestType, uid: str
    ) -> dict:
        job_application: JobApplication = JobApplication.objects.get(
            applicant_id=uid, id=request_data.application_id
        )
        if job_application:
            return ExportJobApplication(**job_application.model_to_dict()).model_dump()
        else:
            raise JobApplicationNotCreatedError()
