from typing import Optional

from pydantic import BaseModel


class AddJobRequestType(BaseModel):
    title: str
    salary: str
    company_name: str
    location: str
    skills: str

    applied_candidates: Optional[str] = None
    experience: Optional[str] = None
    notice_period: Optional[str] = None
    vacancy: Optional[str] = None
    good_to_have: Optional[str] = None
    industry_type: Optional[str] = None
    employment_type: Optional[str] = None
    about_company: Optional[str] = None
    department: Optional[str] = None
