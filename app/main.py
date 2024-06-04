from fastapi import FastAPI
from .api.auth import router as auth_router
from .api.transactions import router as transactions_router

app = FastAPI()

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(transactions_router, prefix="/transactions", tags=["Transactions"])
