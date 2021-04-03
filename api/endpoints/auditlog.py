from typing import Any

from fastapi import APIRouter

from api.schemas.auditlog import AuditLog


router = APIRouter()


@router.post("/auditlog", response_model=AuditLog)
async def create_audit_log(audit_log: AuditLog) -> Any:
    """Endpoint to create an audit log"""
    return audit_log
