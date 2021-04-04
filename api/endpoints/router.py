from fastapi import APIRouter

from api.endpoints import anomaly, auditlog

api_router = APIRouter()
api_router.include_router(auditlog.router, tags=["audit_log"])
api_router.include_router(anomaly.router, tags=["anomaly"])
