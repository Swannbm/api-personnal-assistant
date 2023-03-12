import pytest
from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)


def test_webhook_subscribe():
    url = (
        "/webhook?hub.mode=subscribe&hub.challenge=123"
        "&hub.verify_token=HAPPY"
    )
    response = client.get(url)
    assert response.status_code == 200
    assert response.json() == 123
    response = client.get("/webhook?hub.challenge=123&hub.verify_token=HAPPY")
    assert response.status_code == 404


def test_messages_hook():
    response = client.post("/webhook?hub.verify_token=HAPPY")
    assert response.status_code == 200
