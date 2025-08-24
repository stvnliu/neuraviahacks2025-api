from fastapi import APIRouter, HTTPException
from ..models import HealthRecord, User
from ..lib.session_dep import SessionDep
from ..lib.auth import AuthUtils
from fastapi import status
router = APIRouter(prefix="/data")

@router.get("/bmi")
def get_bmi(user:str, token: str) -> list[float]:
    return []
    # TODO: check token is correct


@router.post("/upload")
def upload_record(token: str, new_record: HealthRecord, session: SessionDep) -> HealthRecord:
    if AuthUtils.verify_token(token, new_record.UserName, session):
        session.add(new_record)
        session.commit()
        session.refresh(new_record)
        return new_record
    raise HTTPException(status.HTTP_403_FORBIDDEN)

