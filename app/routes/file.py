from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from app.auth.dependencies import require_role
from app.core.database import db
import os
import shutil
from datetime import datetime
from app.utils.jwt import create_download_token
from app.utils.jwt import SECRET_KEY, ALGORITHM
from jose import jwt, JWTError
from fastapi.responses import FileResponse

router = APIRouter()

ALLOWED_EXTENSIONS = ["pptx", "docx", "xlsx"]
UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_file(
    uploaded_file: UploadFile = File(...),
    user=Depends(require_role("ops"))
):
    filename = uploaded_file.filename
    ext = filename.split(".")[-1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="File type not allowed")

    # Save file
    save_path = os.path.join(UPLOAD_DIR, filename)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(uploaded_file.file, buffer)

    # Store metadata
    file_doc = {
        "filename": filename,
        "extension": ext,
        "uploaded_by": user["sub"],
        "uploaded_at": datetime.utcnow()
    }
    await db["files"].insert_one(file_doc)

    return {"message": "File uploaded successfully", "filename": filename}

@router.get("/download-link/{filename}")
async def get_download_link(filename: str, user=Depends(require_role("client"))):
    file_doc = await db["files"].find_one({"filename": filename})
    if not file_doc:
        raise HTTPException(status_code=404, detail="File not found")

    token = create_download_token({"filename": filename, "user": user["sub"]})
    download_url = f"http://localhost:8000/file/download/{token}"

    return {"download-link": download_url, "message": "success"}

@router.get("/download/{token}")
async def download_file(token: str, user=Depends(require_role("client"))):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired link")

    if user["sub"] != payload.get("user"):
        raise HTTPException(status_code=403, detail="Access denied")

    filename = payload.get("filename")
    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(file_path, media_type='application/octet-stream', filename=filename)

@router.get("/list")
async def list_uploaded_files(user=Depends(require_role("client"))):
    files_cursor = db["files"].find({})
    files = []
    async for file_doc in files_cursor:
        file_doc["_id"] = str(file_doc["_id"])  # convert ObjectId to string
        files.append(file_doc)

    return {"files": files, "message": "File list fetched successfully"}
