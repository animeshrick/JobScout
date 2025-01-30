from typing import Optional

from pydantic import BaseModel


class CreateUserRequestType(BaseModel):
    fname: Optional[str] = None
    lname: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
