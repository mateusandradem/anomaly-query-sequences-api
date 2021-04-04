from typing import List, Optional
from datetime import datetime, timedelta

from pydantic import BaseModel


class AuditLogBase(BaseModel):
    session: int
    sequence: int
    statement_type: str
    statement: str
    query: str
    query_time: datetime
    anomaly_id: str
    db_object_type: Optional[str] = ""
    db_object: Optional[str] = ""


class AuditLogCreate(AuditLogBase):
    pass


class AuditLog(AuditLogBase):
    id: int

    class Config:
        orm_mode = True


class AnomalyBase(BaseModel):
    start_session_time: datetime
    end_session_time: datetime
    session: int
    session_time: timedelta
    dropped_session: bool


class AnomalyCreate(AnomalyBase):
    pass


class Anomaly(AnomalyBase):
    id: int

    class Config:
        orm_mode = True
