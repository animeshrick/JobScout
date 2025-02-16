import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import BaseModel


class ExportUploadedFile(BaseModel):
    id: Optional[UUID]
    action: str
    file: str
    uploaded_at: datetime.datetime

    def __init__(self, with_id: bool = True, **kwargs):
        if not with_id:
            kwargs["id"] = None
        super().__init__(**kwargs)


class ExportUploadedFileList(BaseModel):
    jobs: List[ExportUploadedFile]
