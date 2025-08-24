from fastapi import APIRouter
from ..models import HealthRecord, User
from ..lib.session_dep import SessionDep
router = APIRouter(prefix="/data")

@router.get("/bmi")
def get_bmi(user:str, token: str) -> list[float]:
    return []
    # TODO: check token is correct


@router.post("/upload")
def upload_record(new_record: HealthRecord, session: SessionDep) -> HealthRecord:
    session.add(new_record)
    session.commit()
    session.refresh(new_record)
    return new_record

