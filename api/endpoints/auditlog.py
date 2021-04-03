from typing import Any

from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from api.db.database import Base, SessionLocal, engine
from api.db import crud
from api.schemas.schemas import AuditLogCreate


Base.metadata.create_all(bind=engine)


router = APIRouter()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/auditlog", response_model=AuditLogCreate)
async def create_audit_log(audit_log: AuditLogCreate, db: Session = Depends(get_db)):
    db_audit_log = crud.create_audit_log(db, audit_log)
    return audit_log
