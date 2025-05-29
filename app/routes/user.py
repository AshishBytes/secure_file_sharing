from fastapi import APIRouter, HTTPException, status, Depends
from app.models.user import UserCreate, UserRole
from app.utils.security import hash_password
from app.core.database import db
from app.models.user import UserLogin
from app.utils.security import verify_password
from app.utils.jwt import create_access_token
from bson import ObjectId

router = APIRouter()

@router.post("/signup")
async def client_signup(user: UserCreate):
    if user.role != UserRole.CLIENT:
        raise HTTPException(status_code=403, detail="Only client users can sign up.")

    existing_user = await db["users"].find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists.")

    hashed_pw = hash_password(user.password)
    user_doc = {
        "email": user.email,
        "role": user.role,
        "hashed_password": hashed_pw,
        "is_verified": False
    }
    result = await db["users"].insert_one(user_doc)

    # Simulated encrypted verification link (we'll improve it later)
    verification_url = f"http://localhost:8000/user/verify/{str(result.inserted_id)}"

    return {
        "message": "Client user registered successfully",
        "verification_url": verification_url
    }


@router.post("/login")
async def login(user: UserLogin):
    user_doc = await db["users"].find_one({"email": user.email})
    if not user_doc:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, user_doc["hashed_password"]):
        raise HTTPException(status_code=401, detail="Incorrect password")

    if user_doc["role"] == "client" and not user_doc.get("is_verified", False):
        raise HTTPException(status_code=403, detail="Email not verified")

    token_data = {
        "sub": user.email,
        "role": user_doc["role"]
    }
    access_token = create_access_token(token_data)

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": user_doc["role"]
    }


@router.get("/verify/{user_id}")
async def verify_email(user_id: str):
    try:
        result = await db["users"].update_one(
            {"_id": ObjectId(user_id)},
            {"$set": {"is_verified": True}}
        )
        if result.modified_count == 1:
            return {"message": "Email verified successfully!"}
        else:
            raise HTTPException(status_code=404, detail="User not found or already verified.")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
