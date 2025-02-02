from typing import Optional, List

from _decimal import Decimal
from pydantic import BaseModel


class UpdateJobRequestType(BaseModel):
    job_id: str
    salary: Optional[Decimal] = None
    locations: Optional[List[str]] = None
    skills: Optional[List[str]] = None

    # status: Optional[str] = None
    experience: Optional[str] = None
    notice_period: Optional[str] = None
    vacancy: Optional[int] = None
    good_to_have: Optional[str] = None
    industry_type: Optional[str] = None
    employment_type: Optional[str] = None
    about_company: Optional[str] = None
    department: Optional[str] = None
