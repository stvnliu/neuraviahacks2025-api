from fastapi import APIRouter
from ..models import HealthRecord, User
from ..lib.session_dep import SessionDep
router = APIRouter(prefix="/data")

@router.get("/bmi")
def get_bmi(user:str) -> list[float]:
    # TODO: check for correct Authorization header
    return {"something" : user}

# BMI endpoint WORKING
@router.get("/bmia")
def bmi_calc(height: float, weight: float) -> float:
    # TODO: check for correct Authorization header
    return weight / (height)**2


@router.post("/upload")
def upload_record(new_record: HealthRecord, session: SessionDep) -> HealthRecord:
    session.add(new_record)
    session.commit()
    session.refresh(new_record)
    return new_record

