import datetime
import typing
from typing import Optional
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

JOB_ROLE_CHOICES = typing.Literal["start", "end"]


class ExportJob(BaseModel):
    id: Optional[UUID]
    title: str
    company: str
    salary: Decimal
    locations: typing.List[str]
    skills: typing.List[str]

    role: JOB_ROLE_CHOICES
    experience: Optional[str]
    notice_period: Optional[str]
    vacancy: Optional[int]
    good_to_have: Optional[str]
    industry_type: Optional[str]
    employment_type: Optional[str]
    department: Optional[str]
    description: Optional[str]
    status: Optional[str]

    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportUserList(BaseModel):
    jobs: typing.List[ExportJob]
