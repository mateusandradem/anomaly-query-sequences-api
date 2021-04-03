from typing import Optional

from pydantic import BaseModel


class AuditLogBase(BaseModel):
    session: int
    sequence: int
    statement_type: str
    statement: str
    query: str
    db_object_type: Optional[str]
    db_object: Optional[str]


class AuditLogCreate(AuditLogBase):
    pass


class AuditLog(AuditLogBase):
    id: int

    class Config:
        orm_mode = True
