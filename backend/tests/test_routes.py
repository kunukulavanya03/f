import pytest
from app.main import app
from app.schemas import UserCreate

@pytest.fixture
def client():
    return TestClient(app)


def test_create_user(client):
    user = UserCreate(name="test", email="test@example.com")
    response = client.post("/api/users", json=user.dict())
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "test", "email": "test@example.com"}