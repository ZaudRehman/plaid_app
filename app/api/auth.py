# app/api/auth.py
from fastapi import APIRouter, HTTPException, Body
from ..services.auth_service import AuthService
from ..core.config import settings

router = APIRouter()


@router.post("/create_link_token")
async def create_link_token():
    try:
        link_token = await AuthService.create_link_token()
        return {"link_token": link_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/exchange_public_token")
async def exchange_public_token(public_token: str = Body(...)):
    try:
        access_token = await AuthService.exchange_public_token(public_token)
        return {"access_token": access_token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
