import datetime
import typing
from typing import Optional
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

from users.export_types.user_types.export_user import ExportUser
from users.models.user_models.user import User


class ExportJob(BaseModel):
    id: Optional[UUID]
    posted_by: ExportUser
    title: str
    company: str
    salary: Decimal
    locations: typing.List[str]
    skills: typing.List[str]

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
        if "posted_by" in kwargs and isinstance(kwargs["posted_by"], User):
            kwargs["posted_by"] = ExportUser(**kwargs["posted_by"].model_to_dict())
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportJobList(BaseModel):
    jobs: typing.List[ExportJob]
