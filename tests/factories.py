from datetime import datetime, timedelta

from factory.alchemy import SQLAlchemyModelFactory
from factory import SubFactory
from fastapi import Depends

from api.db.database import SessionLocal
from api.models.models import Anomaly, AuditLog


session = SessionLocal()


class AnomalyFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Anomaly
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"
        sqlalchemy_get_or_create = (
            "end_session_time",
            "start_session_time",
            "db_session",
            "session_time",
            "dropped_session",
        )

    end_session_time = datetime(2021, 4, 5, 21, 47, 25, 769966)
    start_session_time = datetime(2021, 4, 5, 21, 40, 25, 769966)
    db_session = 3
    session_time = timedelta(seconds=420)
    dropped_session = True


class AuditLogFactory(SQLAlchemyModelFactory):
    class Meta:
        model = AuditLog
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "commit"
        sqlalchemy_get_or_create = (
            "db_session",
            "sequence",
            "statement_type",
            "statement",
            "query",
            "query_time",
            "anomaly_id",
            "db_object_type",
            "db_object",
        )

    db_session = 3
    sequence = 1
    statement_type = "DDL"
    statement = "CREATE TABLE"
    query = "CREATE TABLE important_table (id INT)"
    query_time = datetime(2021, 4, 5, 21, 42, 33, 162413)
    anomaly_id = 1
    db_object_type = "TABLE"
    db_object = "public.important_table"
    anomaly = SubFactory(AnomalyFactory)
