from sqlalchemy.orm import Session

from api.models import models
from api.schemas import schemas


def get_audit_log(db: Session, audit_log_id: int):
    return db.query(models.AuditLog).filter(models.AuditLog.id == audit_log_id).first()


def get_audit_log(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.AuditLog).offset(skip).limit(limit).all()


def create_audit_log(db:Session, audit_log: schemas.AuditLog):
    db_audit_log = models.AuditLog(**audit_log.dict())
    db.add(db_audit_log)
    db.commit()
    db.refresh(db_audit_log)

    return db_audit_log
