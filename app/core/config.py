# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "MyFinanceApp"
    DEBUG: bool = False
    DATABASE_URL: str = "mongodb+srv://zaud-rehman:nihal1234@cluster0.isukerh.mongodb.net/"
    PLAID_CLIENT_ID: str
    PLAID_SECRET: str
    PLAID_ENVIRONMENT: str = "sandbox"

    class Config:
        env_file = ".env"

settings = Settings()
