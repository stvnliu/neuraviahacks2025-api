from fastapi import APIRouter, HTTPException
from ..models import HealthRecord, User
from ..lib.session_dep import SessionDep
from ..lib.auth import AuthUtils
from fastapi import status
from ..lib.database_handler import DatabaseHandler
router = APIRouter(prefix="/data")
@router.get("/bmi")
def get_all_bmi_points(username: str, token: str, session: SessionDep) -> list[HealthRecord]:
    if DatabaseHandler.verify_token(token, DatabaseHandler.get_user_by_name(username, session).id, session):
        return DatabaseHandler.get_health_record(username, session)
    raise HTTPException(status.HTTP_403_FORBIDDEN)

@router.post("/upload")
def upload_record(token: str, new_record: HealthRecord, session: SessionDep) -> HealthRecord:
    if AuthUtils.verify_token(token, new_record.UserName, session):
        session.add(new_record)
        session.commit()
        session.refresh(new_record)
        return new_record
    raise HTTPException(status.HTTP_403_FORBIDDEN)

