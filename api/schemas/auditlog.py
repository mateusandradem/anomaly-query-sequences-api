from typing import Optional

from pydantic import BaseModel


class AuditLog(BaseModel):
    """PGAudit log data schema"""
    session: int
    sequence: int
    statement_type: str
    statement: str
    query: str
    db_object_type: Optional[str]
    db_object: Optional[str]
