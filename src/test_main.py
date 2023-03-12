from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_webhook_subscribe():
    response = client.get("/webhook?hub.mode=subscribe&hub.challenge=123&hub.verify_token=token")
    assert response.status_code == 200
    assert response.json() == "123"
