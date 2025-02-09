from django.db.models import Q

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
    JobApplicationNotCreatedError, JobApplicationNotFoundError,
)
from job_applications.models.job_application_model import JobApplication
from job_applications.serializers.job_application_serializer import (
    JobApplicationSerializer,
)
from jobs.models.job_model import Job


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
        try:
            job_application: JobApplication = JobApplication.objects.get(
                applicant_id=uid, id=request_data.application_id
            )
        except Exception:
            raise JobApplicationNotFoundError()
        if job_application:
            return ExportJobApplication(**job_application.model_to_dict()).model_dump()

    @staticmethod
    def withdraw_job_application_service(
            request_data: GetJobApplicationRequestType, uid: str
    ) -> dict:
        job_application = JobApplication.objects.filter(
            applicant_id=uid,
            id=request_data.application_id
        ).filter(Q(status="pending") | Q(status="accepted") | Q(status="rejected")).first()

        if job_application:
            job_application.status = "withdrawn"

            job = Job.objects.get(id=job_application.job.id)

            job.applicants.remove(job_application.applicant)

            job_application.save()
            job.save()
            return ExportJobApplication(**job_application.model_to_dict()).model_dump()
        else:
            raise JobApplicationNotFoundError()
