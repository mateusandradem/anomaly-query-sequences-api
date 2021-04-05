from http import HTTPStatus


def test_read_audit_logs(client):
    response = client.get("/audit-logs/")
    assert response.status_code == HTTPStatus.OK
