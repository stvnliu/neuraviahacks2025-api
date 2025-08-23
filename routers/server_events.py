from ..lib.session_dep import SessionDep
from fastapi import APIRouter
from ..lib.database_handler import DatabaseHandler


router = APIRouter()


@router.on_event("startup")
def on_startup():
    DatabaseHandler.init_db_tables()
    pass

@router.on_event("shutdown")
def on_shutdown():
    pass

