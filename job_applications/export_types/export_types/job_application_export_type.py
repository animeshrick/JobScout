import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel

from job_applications.models.job_applicant import JobApplicant
from job_applications.models.job_model_for_application import JobModelForApplication


class ExportJobApplication(BaseModel):
    id: Optional[UUID]
    status: str
    job: Optional[JobModelForApplication]
    applicant: Optional[JobApplicant]

    applied_at: datetime.datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if "job" in kwargs:
            kwargs["job"] = JobModelForApplication(**kwargs["job"].model_to_dict())

        if "applicant" in kwargs:
            kwargs["applicant"] = JobApplicant(**kwargs["applicant"].model_to_dict())

        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportJobApplicationList(BaseModel):
    jobs: List[ExportJobApplication]
