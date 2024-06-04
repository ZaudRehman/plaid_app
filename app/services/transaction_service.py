# app/services/transaction_service.py
from ..db.database import get_db
from fastapi import HTTPException, status


class TransactionService:
    @staticmethod
    async def get_transactions(user_id: str):
        db = get_db()
        transactions = await db["transactions"].find({"user_id": user_id}).to_list(None)
        if transactions is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No transactions found")
        return transactions

    @staticmethod
    async def add_transaction(user_id: str, amount: float, description: str, date: str):
        db = get_db()
        transaction = {"user_id": user_id, "amount": amount, "description": description, "date": date}
        result = await db["transactions"].insert_one(transaction)
        if not result:
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Transaction could not be created")
        return transaction
