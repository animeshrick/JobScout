from uuid import UUID

from pydantic import BaseModel


class JobApplicant(BaseModel):
    id: UUID
    user_name: str
    resume: str
    role: str
    email: bool
    is_deleted_user: bool

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
