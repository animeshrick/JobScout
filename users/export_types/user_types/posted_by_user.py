from pydantic import BaseModel
from typing import Optional


class PostedByUser(BaseModel):
    fname: str
    lname: str
    email: str
    phone: Optional[str] = None
