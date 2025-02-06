from uuid import UUID

from pydantic import BaseModel

from users.models.user_models.user import User


class ExportApplicant(BaseModel):
    id: UUID
    first_name: str
    last_name: str
    email: str

    def __init__(self, user: User, **kwargs):
        kwargs["id"] = user.id
        kwargs["first_name"] = user.fname
        kwargs["last_name"] = user.lname
        kwargs["email"] = user.email
        super().__init__(**kwargs)
