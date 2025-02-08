import datetime
import json
from typing import Optional, List
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

from jobs.export_types.job_export_type.export_job_applicant import ExportApplicant
from users.export_types.user_types.posted_by_user import PostedByUser


class ExportJob(BaseModel):
    id: Optional[UUID]
    posted_by: Optional[PostedByUser] = None
    title: str
    company: str
    salary: Decimal
    locations: List[str]
    skills: List[str]

    experience: Optional[str]
    notice_period: Optional[str]
    vacancy: Optional[int]
    good_to_have: Optional[str]
    industry_type: Optional[str]
    employment_type: Optional[str]
    department: Optional[str]
    description: Optional[str]
    status: Optional[str]
    jd: Optional[str]

    applicants: Optional[List[ExportApplicant]] = []
    applicants_number: Optional[int] = None
    is_deleted: Optional[bool]

    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(
        self,
        with_id: bool = True,
        with_posted_by: bool = True,
        only_with_applicant_count: bool = False,
        **kwargs
    ):

        if isinstance(kwargs.get("locations"), str):
            kwargs["locations"] = [loc.strip() for loc in kwargs["locations"].split(",")]

        if isinstance(kwargs.get("skills"), str):
            kwargs["skills"] = [skill.strip() for skill in kwargs["skills"].split(",")]

        if "posted_by" in kwargs:
            kwargs["posted_by"] = (
                PostedByUser(**kwargs["posted_by"].model_to_dict())
                if with_posted_by
                else None
            )

        if "applicants" in kwargs:
            applicant_objects = kwargs["applicants"]
            if not only_with_applicant_count:
                kwargs["applicants"] = [
                    ExportApplicant(user) for user in applicant_objects
                ]
                kwargs["applicants_number"] = len(applicant_objects)
            else:
                kwargs["applicants"] = []
                kwargs["applicants_number"] = len(applicant_objects)

        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportJobList(BaseModel):
    jobs: List[ExportJob]
