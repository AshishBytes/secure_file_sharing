from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

load_dotenv()

oauth2_scheme = HTTPBearer()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def get_current_user(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)) -> dict:
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )

def require_role(required_role: str):
    def role_checker(payload: dict = Depends(get_current_user)):
        if payload.get("role") != required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )
        return payload
    return role_checker
