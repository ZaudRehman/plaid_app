# app/tests/test_db.py
from ..db import crud
from ..db.database import get_db


async def test_create_user():
    db = get_db()
    test_user_data = {"username": "testuser", "email": "test@example.com", "password_hash": "hashed_password"}
    user_id = await crud.create_user(db, test_user_data)
    assert user_id is not None


async def test_get_user_by_username():
    db = get_db()
    test_username = "testuser"
    user = await crud.get_user_by_username(db, test_username)
    assert user is not None
    assert user["username"] == test_username
