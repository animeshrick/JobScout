from pydantic import BaseModel


class AddJobApplicationRequestType(BaseModel):
    job_id: str
    resume: str
