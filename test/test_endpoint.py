from fastapi.testclient import TestClient
from app.main import app
from app import schemas

client = TestClient(app)

def test_create_user():
    res = client.post(
        "/users/", json={"email": "abc1@test.com", "password": "abc123"}
    )
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "abc1@test.com"
    assert res.status_code == 201