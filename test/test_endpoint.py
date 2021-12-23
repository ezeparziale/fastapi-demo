from app import schemas
from .database import client, session

def test_create_user(client, session):
    res = client.post(
        "/users/", json={"email": "abc1@test.com", "password": "abc123"}
    )
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "abc1@test.com"
    assert res.status_code == 201


def test_login(client, session):
    res = client.post(
        "/login/", data={"username": "abc1@test.com", "password": "abc123"}
    )
    print(res.json())
    assert res.status_code == 200