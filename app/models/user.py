# app/models/user.py
from pydantic import BaseModel
from bson import ObjectId


class User(BaseModel):
    id: ObjectId
    username: str
    email: str
    password_hash: str

    class Config:
        orm_mode = True
