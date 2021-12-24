import pytest
from jose import jwt
from app import schemas
from app.config import settings
from .database import client, session

@pytest.fixture
def test_user(client):
    user_data = {"email": "abc1@test.com",
                 "password": "abc123"}
    res = client.post("/users/", json=user_data)
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


def test_create_user(client, session):
    res = client.post(
        "/users/", json={"email": "abc1@test.com", "password": "abc123"}
    )
    print(res.json())
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "abc1@test.com"
    assert res.status_code == 201


def test_login(client, test_user):
    res = client.post(
        "/login/", data={"username": test_user['email'], "password": test_user['password']}
    )
    print(res.json())
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200