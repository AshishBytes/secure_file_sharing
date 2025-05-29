import asyncio
import sys
import os

# ✅ Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils.security import hash_password
from app.core.database import db

async def create_ops_user():
    user = {
        "email": "ops@example.com",
        "role": "ops",
        "hashed_password": hash_password("secureops"),
        "is_verified": True
    }

    existing = await db["users"].find_one({"email": user["email"]})
    if not existing:
        await db["users"].insert_one(user)
        print("✅ Ops user created!")
    else:
        print("⚠️ Ops user already exists.")

if __name__ == "__main__":
    asyncio.run(create_ops_user())
