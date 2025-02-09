from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class JobApplicant(BaseModel):
    id: UUID
    user_name: Optional[str] = None
    resume: str
    role: str
    email: str
    is_deleted_user: Optional[bool] = None

    def __init__(self, **kwargs):
        if "fname" in kwargs or "lname" in kwargs:
            kwargs["user_name"] = (kwargs["fname"] + " " + kwargs["lname"]).strip()
        if "is_deleted" in kwargs:
            kwargs["is_deleted_user"] = kwargs["is_deleted"]
        super().__init__(**kwargs)
