# app/db/crud.py
from .database import get_db


async def create_user(user_data):
    db = get_db()
    result = await db.users.insert_one(user_data)
    return result.inserted_id


async def get_user_by_username(username):
    db = get_db()
    user = await db.users.find_one({"username": username})
    return user


async def update_user(user_id, update_data):
    db = get_db()
    result = await db.users.update_one({"_id": user_id}, {"$set": update_data})
    return result.modified_count


async def delete_user(user_id):
    db = get_db()
    result = await db.users.delete_one({"_id": user_id})
    return result.deleted_count
