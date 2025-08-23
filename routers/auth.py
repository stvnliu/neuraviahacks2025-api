from fastapi import APIRouter, HTTPException
router = APIRouter(prefix="/auth")

@router.post("/")
def authenticate():
    return {}