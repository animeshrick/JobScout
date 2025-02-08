from typing import Optional
from django.utils.timezone import now
from rest_framework import serializers

from job_applications.job_application_exceptions.job_application_exceptions import (
    JobApplicationNotCreatedError,
)
from job_applications.models.job_application_model import JobApplication
from jobs.job_exceptions.job_exceptions import JobNotFoundError
from jobs.models.job_model import Job
from users.models.user_models.user import User
from users.services.helpers import validate_user_uid


class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> Optional[bool]:
        # validating for is valid user
        uid = data.get("uid")
        if not validate_user_uid(uid).is_validated:
            raise JobApplicationNotCreatedError()

        request_data = data.get("request_data")

        job_id = request_data.get("job_id")
        resume = request_data.get("resume")

        if not job_id or not resume:
            raise ValueError("All fields are required.")

        if not isinstance(job_id, str) or not isinstance(resume, str):
            raise ValueError("Invalid data type.")

        if job_id:
            job = Job.objects.filter(id=job_id)
            if not job.exists():
                raise JobNotFoundError()

        return True

    def create(self, data: dict) -> JobApplication:
        request_data = data.get("request_data")
        if self.validate(data):

            job_id = request_data.get("job_id")
            user_id = data.get("uid")

            job: Job = Job.objects.get(id=job_id)
            user: User = User.objects.get(id=user_id)

            if job:
                job.applicants.add(user)
                job.save()

            if request_data.get("resume"):
                user.resume = request_data.get("resume")
                user.save()

            job_application = JobApplication.objects.create(
                job=job, applicant=user, applied_at=now(), status="pending"
            )
            return job_application
