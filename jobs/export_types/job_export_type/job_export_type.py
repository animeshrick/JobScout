import datetime
import typing
from typing import TYPE_CHECKING
from typing import Optional
from uuid import UUID

from _decimal import Decimal
from pydantic import BaseModel

if TYPE_CHECKING:
    from users.export_types.user_types.export_user import ExportUser


class ExportJob(BaseModel):
    id: Optional[UUID]
    posted_by: Optional["ExportUser"]
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
        from users.export_types.user_types.export_user import ExportUser  # Local import

        if "posted_by" in kwargs and isinstance(kwargs["posted_by"], dict):
            kwargs["posted_by"] = ExportUser(**kwargs["posted_by"])
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportJobList(BaseModel):
    jobs: typing.List[ExportJob]
