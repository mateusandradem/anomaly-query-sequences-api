from fastapi import status
from fastapi.testclient import TestClient

from tests.factories import AnomalyFactory, AuditLogFactory


def test_get_audit_logs(client: TestClient):
    AuditLogFactory()

    response = client.get("/audit-logs/")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1


def test_get_audit_log(client: TestClient):
    audit_log = AuditLogFactory()

    response = client.get(f"/audit-logs/{audit_log.id}")

    assert response.status_code == status.HTTP_200_OK


def test_get_audit_log_not_found(client: TestClient):
    response = client.get(f"/audit-logs/1")

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_create_audit_log(client: TestClient, auditlog_payload: dict):
    anomaly = AnomalyFactory()
    auditlog_payload["anomaly_id"] = anomaly.id

    response = client.post("/audit-logs/", json=auditlog_payload)

    assert response.status_code == status.HTTP_201_CREATED


def test_create_audit_log_without_anomaly(client: TestClient, auditlog_payload: dict):
    response = client.post("/audit-logs/", json=auditlog_payload)
    anomaly_id = auditlog_payload["anomaly_id"]

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert (
        response.json()["detail"] == f"Does not exist an anomaly with id: {anomaly_id}"
    )


def test_create_audit_log_with_different_db_session(
    client: TestClient, auditlog_payload: dict
):
    anomaly = AnomalyFactory()
    auditlog_payload["anomaly_id"] = anomaly.id
    auditlog_payload["db_session"] = anomaly.db_session + 1

    response = client.post("/audit-logs/", json=auditlog_payload)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert (
        response.json()["detail"]
        == f"Audit log does not have same session of referenced anomaly"
    )
