from fastapi import APIRouter

from ..lib.database_handler import DatabaseHandler
from ..lib.session_dep import SessionDep

router = APIRouter()


@router.on_event("startup")
def on_startup():
    DatabaseHandler.init_db_tables()
    pass


@router.on_event("shutdown")
def on_shutdown():
    pass
