import pytest
import jwt
from code import schemas

from main.config import settings


def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "user123@gmail.com", "password": "pwd12345!@#"}
    )

    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "user123@gmail.com"
    assert res.status_code == 201


