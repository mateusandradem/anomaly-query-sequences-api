from typing import Any

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.db.database import Base, SessionLocal, engine
from api.db import crud
from api.schemas import schemas


Base.metadata.create_all(bind=engine)


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/auditlog/", response_model=schemas.AuditLog)
async def create_audit_log(audit_log: schemas.AuditLogCreate, db: Session = Depends(get_db)):
    return crud.create_audit_log(db, audit_log)


@router.post("/anomaly/", response_model=schemas.Anomaly)
async def create_anomaly(anomaly: schemas.AnomalyCreate, db: Session = Depends(get_db)):
    return crud.create_anomaly(db, anomaly)
