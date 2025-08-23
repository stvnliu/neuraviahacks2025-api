from fastapi import APIRouter, HTTPException
from ..lib.session_dep import SessionDep
from ..lib.database_handler import DatabaseHandler
router = APIRouter(prefix="/resources")

@router.get('/')
def get_user(id:str, session : SessionDep):
    return DatabaseHandler.get_health_record(id, session)
