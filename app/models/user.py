from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum

class UserRole(str, Enum):
    CLIENT = "client"
    OPS = "ops"

class UserBase(BaseModel):
    email: EmailStr
    role: UserRole

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserInDB(UserBase):
    hashed_password: str
    is_verified: Optional[bool] = False
