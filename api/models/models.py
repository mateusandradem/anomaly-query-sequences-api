from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        Interval, String)
from sqlalchemy.orm import relationship

from api.db.database import Base


class AuditLog(Base):
    __tablename__ = "auditlogs"

    id = Column(Integer, primary_key=True, index=True)
    db_session = Column(Integer)
    sequence = Column(Integer)
    statement = Column(String)
    statement_type = Column(String)
    query = Column(String)
    query_time = Column(DateTime)
    db_object_type = Column(String, default="")
    db_object = Column(String, default="")
    anomaly = relationship("Anomaly", back_populates="auditlogs")
    anomaly_id = Column(Integer, ForeignKey("anomalies.id"))


class Anomaly(Base):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True, index=True)
    auditlogs = relationship("AuditLog", back_populates="anomaly")
    start_session_time = Column(DateTime)
    end_session_time = Column(DateTime)
    db_session = Column(Integer)
    session_time = Column(Interval)
    dropped_session = Column(Boolean)
