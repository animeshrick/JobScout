from datetime import datetime
from typing import Optional, Any

from django.db.models import Q
from psycopg2 import DatabaseError

from jobs.export_types.job_export_type.job_export_type import ExportJob, ExportJobList
from jobs.export_types.request_type.filter_job_request_type import FilterJobsRequestType
from jobs.export_types.request_type.get_job_request_type import GetJobRequestType
from jobs.export_types.request_type.update_job_request_type import UpdateJobRequestType
from jobs.job_exceptions.job_exceptions import (
    JobNotCreatedError,
    JobNotFoundError,
    JobPermissionError,
)
from jobs.models.job_model import Job
from jobs.export_types.request_type.add_job_request_type import AddJobRequestType
from jobs.serializers.job_serializer import JobSerializer
from users.services.helpers import format_date


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

    @staticmethod
    def get_all_jobs_service() -> Optional[list]:
        try:
            jobs = Job.objects.all()
        except Exception:
            raise DatabaseError()
        if jobs:
            all_jobs = ExportJobList(
                jobs=[ExportJob(**job.model_to_dict()) for job in jobs]
            )
            return all_jobs.model_dump().get("jobs")
        else:
            return None

    @staticmethod
    def get_all_created_jobs(uid: str) -> Optional[list]:
        try:
            jobs = Job.objects.filter(posted_by_id=uid)
        except Exception:
            raise DatabaseError()
        if jobs.exists():
            all_jobs = ExportJobList(
                jobs=[
                    ExportJob(**job.model_to_dict(), with_posted_by=False)
                    for job in jobs
                ]
            )
            return all_jobs.model_dump().get("jobs")
        else:
            return None

    @staticmethod
    def update_job(uid: str, request_data: UpdateJobRequestType) -> ExportJob:
        try:
            job = Job.objects.get(id=request_data.job_id)
        except Exception:
            raise JobNotFoundError()

        # check job owns by the user
        if str(job.posted_by.id) != uid:
            raise JobPermissionError()

        if (
                request_data.locations
                and isinstance(request_data.locations, list)
                and request_data.locations != job.locations
        ):
            job.locations = request_data.locations

            # Update skills if provided and valid
        if (
                request_data.skills
                and isinstance(request_data.skills, list)
                and request_data.skills != job.skills
        ):
            job.skills = request_data.skills

            # Update experience if provided and valid
        if (
                request_data.experience is not None
                and isinstance(request_data.experience, str)
                and request_data.experience != job.experience
        ):
            job.experience = request_data.experience

            # Update notice_period if provided and valid
        if (
                request_data.notice_period is not None
                and isinstance(request_data.notice_period, str)
                and request_data.notice_period != job.notice_period
        ):
            job.notice_period = request_data.notice_period

            # Update vacancy if provided and valid
        if (
                request_data.vacancy is not None
                and isinstance(request_data.vacancy, int)
                and request_data.vacancy != job.vacancy
        ):
            job.vacancy = request_data.vacancy

            # Update good_to_have if provided and valid
        if (
                request_data.good_to_have is not None
                and isinstance(request_data.good_to_have, str)
                and request_data.good_to_have != job.good_to_have
        ):
            job.good_to_have = request_data.good_to_have

            # Update industry_type if provided and valid
        if (
                request_data.industry_type is not None
                and isinstance(request_data.industry_type, str)
                and request_data.industry_type != job.industry_type
        ):
            job.industry_type = request_data.industry_type

            # Update employment_type if provided and valid
        if (
                request_data.employment_type is not None
                and isinstance(request_data.employment_type, str)
                and request_data.employment_type != job.employment_type
        ):
            job.employment_type = request_data.employment_type

            # Update department if provided and valid
        if (
                request_data.department is not None
                and isinstance(request_data.department, str)
                and request_data.department != job.department
        ):
            job.department = request_data.department

            # Update about_company if provided and valid
        if (
                request_data.about_company is not None
                and isinstance(request_data.about_company, str)
                and request_data.about_company != job.about_company
        ):
            job.about_company = request_data.about_company

        job.save()
        return ExportJob(**job.model_to_dict())

    @staticmethod
    def get_jobs_by_id(request_data: GetJobRequestType) -> ExportJob:
        try:
            job = Job.objects.get(id=request_data.job_id)
            if job:
                return ExportJob(**job.model_to_dict())
        except Exception:
            raise JobNotFoundError()

    from django.db.models import Q

    @staticmethod
    def filter_jobs(request_data: FilterJobsRequestType) -> ExportJobList | list[Any]:
        # try:
        keyword: str = request_data.keyword
        start_date: str = request_data.start_date
        end_date: str = request_data.end_date
        locations: list = request_data.locations
        skills: list = request_data.skills

        jobs = Job.objects.all()

        query = Q()
        if keyword:
            query |= (
                    Q(title__icontains=keyword)
                    | Q(description__icontains=keyword)
                    | Q(company__icontains=keyword)
            )

            keyword_list = keyword.split()
            for word in keyword_list:
                query |= (
                        Q(title__icontains=word)
                        | Q(description__icontains=word)
                        | Q(company__icontains=word)
                )

            jobs = jobs.filter(query)

        if start_date and not end_date:
            raise ValueError("Both start_date and end_date must be provided.")

        if start_date and end_date:
            start_date = format_date(start_date)
            end_date = format_date(end_date)

            jobs = jobs.filter(created_at__date__range=[start_date, end_date])

        if locations:
            for loc in locations:
                query |= Q(locations__icontains=loc)
            jobs = jobs.filter(query)

        if skills:
            for skill in skills:
                query |= Q(skills__icontains=skill)
            jobs = jobs.filter(query)

        jobs = jobs.order_by("-updated_at")

        if jobs.exists():
            get_jobs = ExportJobList(
                jobs=[ExportJob(**job.model_to_dict()) for job in jobs]
            )
            return get_jobs.model_dump().get("jobs")
        else:
            raise JobNotFoundError()

    # except Exception:
    #     raise JobNotFoundError()
