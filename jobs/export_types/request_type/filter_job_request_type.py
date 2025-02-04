from typing import Optional, List

from pydantic import BaseModel


class FilterJobsRequestType(BaseModel):
    keyword: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    locations: Optional[List[str]] = []
    skills: Optional[List[str]] = []
