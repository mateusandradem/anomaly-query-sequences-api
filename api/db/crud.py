from sqlalchemy.orm import Session

from api.models import models
from api.schemas import schemas


def get_audit_log(db: Session, audit_log_id: int):
    return db.query(models.AuditLog).filter(models.AuditLog.id == audit_log_id).first()


def get_audit_logs(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.AuditLog).offset(offset).limit(limit).all()


def create_audit_log(db: Session, audit_log: schemas.AuditLog):
    db_audit_log = models.AuditLog(**audit_log.dict())
    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)

    return db_audit_log


def get_anomaly(db: Session, anomaly_id: int):
    return db.query(models.Anomaly).filter(models.Anomaly.id == anomaly_id).first()


def get_anomalies(db: Session, offset: int = 0, limit: int = 100):
    return db.query(models.Anomaly).offset(offset).limit(limit).all()


def create_anomaly(db:Session, anomaly: schemas.Anomaly):
    db_anomaly = models.Anomaly(**anomaly.dict())
    db.add(db_anomaly)
    db.commit()
    db.refresh(db_anomaly)

    return db_anomaly
