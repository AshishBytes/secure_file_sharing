from fastapi import APIRouter

router = APIRouter()

@router.get("/test-ops")
def test_ops():
    return {"message": "Ops route working"}
