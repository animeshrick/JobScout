from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class JobModelForApplication(BaseModel):
    id: UUID
    title: str
    company: str
    is_deleted_job: Optional[bool] = None

    def __init__(self, **kwargs):
        if "is_deleted" in kwargs:
            kwargs["is_deleted_job"] = kwargs["is_deleted"]
        super().__init__(**kwargs)
