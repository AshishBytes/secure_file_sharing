from fastapi import FastAPI
from app.routes import user, ops, file

app = FastAPI()

app.include_router(user.router, prefix="/user", tags=["Client Users"])
app.include_router(ops.router, prefix="/ops", tags=["Operation Users"])
app.include_router(file.router, prefix="/file", tags=["File Management"])

@app.get("/")
async def root():
    return {"message": "Secure File Sharing API is live!"}
