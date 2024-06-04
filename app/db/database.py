# app/db/database.py
import motor.motor_asyncio
from ..core.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
db = client.plaid_app  # Use your MongoDB database name here


def get_db():
    return db
