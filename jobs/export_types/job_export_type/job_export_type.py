import datetime
import json
from typing import Optional, List
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

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

    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, with_id: bool = True, with_posted_by: bool = True, **kwargs):

        if isinstance(kwargs.get("locations"), str):
            try:
                kwargs["locations"] = json.loads(kwargs["locations"])
            except json.JSONDecodeError:
                raise ValueError("Invalid format for locations. Expected a list.")

        if isinstance(kwargs.get("skills"), str):
            try:
                kwargs["skills"] = json.loads(kwargs["skills"])
            except json.JSONDecodeError:
                raise ValueError("Invalid format for skills. Expected a list.")

        if "posted_by" in kwargs:
            kwargs["posted_by"] = (
                PostedByUser(**kwargs["posted_by"].model_to_dict())
                if with_posted_by
                else None
            )
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportJobList(BaseModel):
    jobs: List[ExportJob]
