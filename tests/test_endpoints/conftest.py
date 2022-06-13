import pytest
from fastapi.testclient import TestClient

from api.main import app
from api.endpoints.utils import get_db
from tests.test_db_config import override_get_db

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def auditlog_payload():
    return {
        "db_session": 3,
        "sequence": 1,
        "statement_type": "DDL",
        "statement": "CREATE TABLE",
        "query": "CREATE TABLE important_table (id INT)",
        "query_time": "2021-04-05T21:42:33.162413",
        "db_object_type": "TABLE",
        "db_object": "public.important_table",
        "anomaly_id": 1,
    }
