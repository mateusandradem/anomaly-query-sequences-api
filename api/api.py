from fastapi import APIRouter

from api.endpoints import auditlog


api_router = APIRouter()
api_router.include_router(auditlog.router, tags=["audit_log"])
