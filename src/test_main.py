import pytest
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_webhook_subscribe():
    response = client.get("/webhook?hub.mode=subscribe&hub.challenge=123&hub.verify_token=HAPPY")
    assert response.status_code == 200
    assert response.json() == 123
    response = client.get("/webhook?hub.challenge=123&hub.verify_token=HAPPY")
    assert response.status_code == 422

def test_messages_hook():
    response = client.get("/webhook?hub.verify_token=HAPPY")