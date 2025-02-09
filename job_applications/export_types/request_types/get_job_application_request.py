from pydantic import BaseModel


class GetJobApplicationRequestType(BaseModel):
    application_id: str
