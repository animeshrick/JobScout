from typing import Optional, List

from _decimal import Decimal
from rest_framework import serializers

from jobs.models.job_model import Job
from users.services.helpers import validate_recruiter


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

    def validate(self, data: Optional[dict] = None) -> Optional[bool]:

        request_job_data = data.get("request_data")

        title = request_job_data.get("title")
        salary = request_job_data.get("salary")
        company_name = request_job_data.get("company")
        locations = request_job_data.get("locations")
        skills = request_job_data.get("skills")

        # validating for is recruiter
        uid = data.get("uid")
        if not validate_recruiter(uid).is_validated:
            raise ValueError("You are not authorized to add job.")

        if not title or not salary or not company_name or not locations or not skills:
            raise serializers.ValidationError(detail="All fields are required.")

        if (
            not isinstance(title, str)
            or not isinstance(salary, Decimal)
            or not isinstance(company_name, str)
            or not isinstance(locations, list)
            or not isinstance(skills, list)
        ):
            raise serializers.ValidationError(detail="Invalid data type.")

        return True

    def create(self, data: dict) -> Job:
        request_job_data = data.get("request_data")
        if self.validate(data):
            skills: List[str] = request_job_data.get("skills")
            all_skills: List[str] = []
            if skills and len(skills) > 0:
                for skill in skills:
                    all_skills.append(skill)

            locations: List[str] = request_job_data.get("locations")
            all_locations: List[str] = []
            if locations and len(locations) > 0:
                for location in locations:
                    all_locations.append(location)

            job_data = {
                "title": request_job_data.get("title"),
                "salary": request_job_data.get("salary"),
                "company": request_job_data.get("company"),
                "locations": all_locations,
                "skills": all_skills,
                "status": "start",
            }

            job: Job = Job.objects.create(**job_data)
            job.save()
            return job
