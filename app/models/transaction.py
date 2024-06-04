# app/models/transaction.py
from pydantic import BaseModel
from bson import ObjectId


class Transaction(BaseModel):
    id: ObjectId
    user_id: ObjectId
    amount: float
    description: str
    date: str

    class Config:
        orm_mode = True
