# app/api/transactions.py
from fastapi import APIRouter, HTTPException, Query
from ..services.transaction_service import TransactionService

router = APIRouter()


@router.get("/transactions")
async def get_transactions(access_token: str, start_date: str, end_date: str):
    try:
        transactions = await TransactionService.get_transactions(access_token, start_date, end_date)
        return transactions
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
