# app/services/auth_service.py
from ..models.user import User
from ..core.security import verify_password, create_access_token, get_password_hash
from ..db.database import get_db
from fastapi import HTTPException, status


class AuthService:
    @staticmethod
    async def authenticate_user(username: str, password: str):
        db = get_db()
        user = await db["users"].find_one({"username": username})
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        if not verify_password(password, user["password_hash"]):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect password")
        return create_access_token(user["username"])

    @staticmethod
    async def create_user(username: str, email: str, password: str):
        db = get_db()
        user = await db["users"].find_one({"username": username})
        if user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
        hashed_password = get_password_hash(password)
        new_user = {"username": username, "email": email, "password_hash": hashed_password}
        await db["users"].insert_one(new_user)
        return create_access_token(username)
