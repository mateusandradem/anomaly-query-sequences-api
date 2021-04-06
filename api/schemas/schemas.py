from datetime import datetime, timedelta
from typing import List, Optional

from pydantic import BaseModel, validator


class AuditLogBase(BaseModel):
    db_session: int
    sequence: int
    statement_type: str
    statement: str
    query: str
    query_time: datetime
    anomaly_id: int
    db_object_type: Optional[str] = ""
    db_object: Optional[str] = ""


class AuditLogCreate(AuditLogBase):
    pass


class AuditLog(AuditLogBase):
    id: int

    class Config:
        orm_mode = True


class AnomalyBase(BaseModel):
    end_session_time: datetime
    start_session_time: datetime
    db_session: int
    session_time: timedelta
    dropped_session: bool

    @validator("start_session_time")
    def start_session_greater_than_end_session_times(cls, v, values, **kwargs):
        if "end_session_time" in values and v >= values["end_session_time"]:
            raise ValueError(
                "start_session_time should be lesser than end_session_time"
            )
        return v


class AnomalyCreate(AnomalyBase):
    pass


class Anomaly(AnomalyBase):
    id: int

    class Config:
        orm_mode = True
