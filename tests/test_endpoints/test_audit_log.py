from http import HTTPStatus

from tests.factories import AuditLogFactory


def test_read_audit_logs(client):
    AuditLogFactory()

    response = client.get("/audit-logs/")

    assert response.status_code == HTTPStatus.OK
    assert len(response.json()) == 1
