from job_applications.export_types.request_types.add_job_application_request import (
    AddJobApplicationRequestType,
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
