from pydantic import BaseModel


class GetJobRequestType(BaseModel):
    job_id: str
