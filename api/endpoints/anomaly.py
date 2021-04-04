from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.db import crud
from api.db.database import Base, engine
from api.endpoints.utils import get_db
from api.schemas import schemas

Base.metadata.create_all(bind=engine)


router = APIRouter()


@router.get("/anomalies/", response_model=List[schemas.Anomaly])
async def read_anomalies(
    offset: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    anomalies = crud.get_anomalies(db, offset=offset, limit=limit)
    return anomalies


@router.get("/anomalies/{anomaly_id}", response_model=schemas.Anomaly)
async def read_anomaly(anomaly_id: int, db: Session = Depends(get_db)):
    db_anomaly = crud.get_anomaly(db, anomaly_id)
    if db_anomaly is None:
        raise HTTPException(
            status_code=404, detail=f"Anonaly with id:{anomaly_id} not found"
        )
    return db_anomaly


@router.post("/anomalies/", response_model=schemas.Anomaly)
async def create_anomaly(anomaly: schemas.AnomalyCreate, db: Session = Depends(get_db)):
    return crud.create_anomaly(db, anomaly)
