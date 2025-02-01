from jobs.job_exceptions.job_exceptions import JobNotCreatedError
from jobs.models.job_model import Job
from jobs.request_type.add_job_reuest_type import AddJobRequestType
from jobs.serializers.job_serializer import JobSerializer


class JobServices:
    @staticmethod
    def add_job_service(request_data: AddJobRequestType, uid: str) -> dict:
        data = {
            "request_data": request_data.model_dump(),
            "uid": uid,
        }
        job: Job = JobSerializer().create(data=data)
        if job:
            return {"message": "Job created successfully."}
        else:
            raise JobNotCreatedError()
