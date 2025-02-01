import datetime
import typing
from typing import Optional
from uuid import UUID

from pydantic import BaseModel

ROLE_CHOICES = typing.Literal["seeker", "recruiter"]


class ExportUser(BaseModel):
    id: Optional[UUID]
    email: str
    fname: str
    lname: str
    dob: Optional[datetime.datetime]
    phone: Optional[str]
    image: Optional[str]
    is_active: bool
    role: ROLE_CHOICES
    resume: Optional[str]
    is_recruiter: Optional[bool] = None
    is_requested: Optional[bool] = None
    is_request_received: Optional[bool] = None
    created_at: datetime.datetime
    updated_at: datetime.datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportUserList(BaseModel):
    user_list: typing.List[ExportUser]
