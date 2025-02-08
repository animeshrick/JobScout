from uuid import UUID

from pydantic import BaseModel


class JobModelForApplication(BaseModel):
    id: UUID
    title: str
    is_deleted_job: bool

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
