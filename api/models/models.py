from sqlalchemy import Column, Integer, String

from api.db.database import Base


class AuditLog(Base):
    __tablename__ = "auditlog"

    id = Column(Integer, primary_key=True, index=True)
    session = Column(Integer)
    sequence = Column(Integer)
    statement = Column(String)
    statement_type = Column(String)
    query = Column(String)
    db_object_type = Column(String, default="")
    db_object = Column(String, default="")
